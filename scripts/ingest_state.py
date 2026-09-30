#!/usr/bin/env python3
"""
단계 A 편입 신뢰성 — 공통 상태 모듈

이 모듈은 "완료 표시"와 "실제 편입"을 구분하기 위한 공통 규칙을 한 곳에 모읍니다.
처리기(stage_a_ingest.py)와 대시보드(update_dashboard.py)가 같은 함수를 쓰므로
같은 문서를 서로 다르게 판정하는 문제가 생기지 않습니다.

담당 범위
  1. frontmatter 해석과 processed 상태 판정 (중복 키·모호한 값은 완료로 읽지 않음)
  2. 원문 버전 해시 두 종류 (파일 전체 / 내용 기준)
  3. 반영 블록(작업 식별자 주석) 생성·탐색·검증
  4. 경로 안전 검사 (Vault 탈출·심볼릭 링크 우회 거부)
  5. 원자적 파일 쓰기, 실행 잠금, SQLite 처리 기록

표준 라이브러리 + PyYAML(이미 설치되어 있는 의존성)만 사용합니다.
PyYAML은 YAML 문법 검증과 중복 키 탐지에만 쓰고, 파일을 다시 덤프하지 않습니다.
(다시 덤프하면 주석·키 순서·인용 스타일이 사라지기 때문입니다.)
"""

from __future__ import annotations

import fcntl
import hashlib
import os
import re
import sqlite3
import tempfile
from contextlib import contextmanager
from datetime import datetime
from pathlib import Path

try:  # PyYAML 이 없는 환경(예: CI)에서도 import 자체는 실패하지 않게 한다
    import yaml
except ImportError:  # pragma: no cover - 환경 의존
    yaml = None

# ──────────────────────────────────────────────────────────────────────────
# 상수
# ──────────────────────────────────────────────────────────────────────────

SOURCE_ROOTS = ("inbox", "outputs/briefings")
TARGET_ROOTS = ("wiki/signals", "wiki/concepts")

# 탐색에서 제외할 폴더 (생성물·캐시·첨부)
EXCLUDED_DIRS = {
    ".git", "node_modules", ".venv", "venv", "__pycache__", "dist", "build",
    ".next", "attachments", "_attachments", ".obsidian", ".cache", "cache",
    ".trash",
}

# 처리기가 직접 쓰는 관리 키. 원문 "내용 버전" 계산에서 제외된다.
# (이 키들이 바뀌어도 원문 내용은 그대로이므로 같은 버전으로 본다)
PROCESSOR_KEYS = ("processed", "processed_date", "processed_note")

BLOCK_BEGIN_RE = re.compile(
    r"^<!-- stage-a:begin id=(?P<id>[0-9a-f]{16}) source=(?P<source>\S+) "
    r"rev=(?P<rev>[0-9a-f]{12}) sha=(?P<sha>[0-9a-f]{64}) -->$"
)
BLOCK_END_FMT = "<!-- stage-a:end id={id} -->"

# 효과적 상태 (대시보드·보고서 공통 어휘)
EFFECTIVE_STATES = (
    "verified",            # 처리 기록 + 실제 대상 본문 검증 통과
    "legacy_unverified",   # processed: true 만 있고 처리 기록 없음
    "pending",             # 아직 편입 안 됨 (표시 없음 / false)
    "held",                # 보류 (판단 필요, 형식 미지원 등)
    "failed",              # 처리 기록상 실패 또는 검증 실패
    "conflict",            # processed 키 중복
)


class StageAError(Exception):
    """설명 가능한 처리 오류 (비정상 종료 코드로 변환됨)."""


# ──────────────────────────────────────────────────────────────────────────
# 1. 해시와 frontmatter
# ──────────────────────────────────────────────────────────────────────────

def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_text(text: str) -> str:
    return sha256_bytes(text.encode("utf-8"))


def normalize_text(text: str) -> str:
    """BOM 제거 + 줄바꿈 통일. 해시가 편집기 설정에 흔들리지 않도록."""
    return text.lstrip("﻿").replace("\r\n", "\n").replace("\r", "\n")


def split_frontmatter(text: str):
    """
    frontmatter 경계를 찾는다.
    반환: (fm_lines, body, has_frontmatter, error)
      - 첫 줄이 '---' 일 때만 frontmatter 로 인정한다.
      - 닫는 줄은 '---' 또는 '...'.
      - 본문 중간의 '---' (수평선)는 frontmatter 로 오인하지 않는다.
    """
    text = normalize_text(text)
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return [], text, False, None
    for i in range(1, len(lines)):
        if lines[i].strip() in ("---", "..."):
            return lines[1:i], "\n".join(lines[i + 1:]), True, None
    return [], text, False, "닫히지 않은 frontmatter"


def _make_dup_loader():
    """중복 키를 조용히 덮어쓰지 않고 기록하는 YAML 로더를 만든다.

    PyYAML 기본 동작은 같은 키가 두 번 나오면 마지막 값을 채택한다.
    'processed: false' 뒤에 'processed: true' 가 붙은 문서를 '완료'로 읽는
    기존 결함의 원인이 바로 이 동작이므로, 중복을 기록해 상위에서 거부한다.
    """
    class DupLoader(yaml.SafeLoader):
        pass

    def construct_mapping(loader, node, deep=False):
        seen = set()
        for key_node, _ in node.value:
            key = loader.construct_object(key_node, deep=deep)
            try:
                if key in seen:
                    loader.duplicates.append(key)
                seen.add(key)
            except TypeError:  # 해시 불가능한 키 → 미지원 형식
                loader.duplicates.append(repr(key))
        return yaml.SafeLoader.construct_mapping(loader, node, deep=deep)

    DupLoader.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, construct_mapping)
    return DupLoader


def parse_yaml_mapping(fm_text: str):
    """YAML 을 해석해 (dict, duplicates, error) 를 반환한다."""
    if yaml is None:
        return None, [], "PyYAML 미설치 — frontmatter 해석 불가"
    loader_cls = _make_dup_loader()
    loader = loader_cls(fm_text)
    loader.duplicates = []
    try:
        data = loader.get_single_data()
    except yaml.YAMLError as exc:
        return None, loader.duplicates, f"YAML 문법 오류: {str(exc).splitlines()[0]}"
    finally:
        loader.dispose()
    if data is None:
        data = {}
    if not isinstance(data, dict):
        return None, loader.duplicates, "frontmatter 가 매핑(키: 값) 형식이 아님"
    return data, loader.duplicates, None


_TOP_KEY_RE = re.compile(r"^([A-Za-z_][\w\-]*)\s*:(.*)$")


def top_level_key(line: str):
    """최상위(들여쓰기 없는) 'key: value' 행이면 key 를 반환."""
    if not line or line[0] in " \t#-":
        return None
    m = _TOP_KEY_RE.match(line)
    return m.group(1) if m else None


def _strip_inline_comment(value: str) -> str:
    """'true # 메모' → 'true'. 인용 문자열 안의 # 은 건드리지 않는다."""
    value = value.strip()
    if value[:1] in ("'", '"'):
        return value
    return re.split(r"\s+#", value, maxsplit=1)[0].strip()


def processor_key_spans(fm_lines):
    """
    처리기 관리 키(processed*)가 차지하는 행 번호 목록을 반환한다.
    값이 여러 줄(블록 스칼라·목록)이면 미지원으로 표시한다.
    반환: (indices, unsupported_reason)
    """
    idx = []
    for i, line in enumerate(fm_lines):
        key = top_level_key(line)
        if key in PROCESSOR_KEYS:
            value = _strip_inline_comment(line.split(":", 1)[1])
            nxt = fm_lines[i + 1] if i + 1 < len(fm_lines) else ""
            multi = value in ("", "|", ">", "|-", ">-") or (
                nxt[:1] in (" ", "\t") or nxt.startswith("- "))
            if multi:
                return idx, f"'{key}' 값이 여러 줄 형식이라 자동 수정 미지원"
            idx.append(i)
    return idx, None


def analyze_source_text(text: str) -> dict:
    """
    원문 텍스트의 상태를 판정한다. (파일 I/O 없음 — 테스트하기 쉽게)

    marker_state 값
      marked_true / marked_false / unmarked : 정상 해석
      conflict       : processed 키 중복 → 자동 완료 금지
      invalid_value  : processed 값이 true/false 리터럴이 아님 (예: yes, "true")
      yaml_error     : 문법 오류·닫히지 않은 frontmatter
      unsupported    : 다른 키 중복, 여러 줄 processed 값 등 → 보류
      no_frontmatter : frontmatter 없음 (= 표시 없음과 동일하게 대기)
    """
    raw = normalize_text(text)
    fm_lines, body, has_fm, fm_err = split_frontmatter(raw)
    result = {
        "file_sha256": sha256_text(raw),
        "has_frontmatter": has_fm,
        "marker_state": None,
        "marker_detail": None,
        "processed_raw": [],
        "meta": {},
        "h1": first_h1(body if has_fm else raw),
    }
    if fm_err:
        result.update(marker_state="yaml_error", marker_detail=fm_err)
        result["revision_sha256"] = sha256_text(raw)
        return result
    if not has_fm:
        result.update(marker_state="no_frontmatter")
        result["revision_sha256"] = compute_revision([], raw)
        return result

    # frontmatter 안의 최상위 processed 행만 상태로 읽는다 (본문 문자열은 무시)
    raw_values = []
    for line in fm_lines:
        if top_level_key(line) == "processed":
            raw_values.append(_strip_inline_comment(line.split(":", 1)[1]))
    result["processed_raw"] = raw_values
    result["revision_sha256"] = compute_revision(fm_lines, body)

    data, dups, err = parse_yaml_mapping("\n".join(fm_lines))
    if "processed" in dups or len(raw_values) > 1:
        result.update(marker_state="conflict",
                      marker_detail=f"processed 키 {len(raw_values)}회: {raw_values}")
        return result
    if err:
        result.update(marker_state="yaml_error", marker_detail=err)
        return result
    if dups:
        result.update(marker_state="unsupported",
                      marker_detail=f"중복 키: {sorted(set(map(str, dups)))}")
        return result
    _, span_err = processor_key_spans(fm_lines)
    if span_err:
        result.update(marker_state="unsupported", marker_detail=span_err)
        return result
    result["meta"] = data
    if not raw_values:
        result["marker_state"] = "unmarked"
        return result
    token, value = raw_values[0], data.get("processed")
    # YAML 1.1 은 yes/on 도 참으로 읽지만, 여기서는 true/false 리터럴만 인정한다
    if value is True and token.lower() == "true":
        result["marker_state"] = "marked_true"
    elif value is False and token.lower() == "false":
        result["marker_state"] = "marked_false"
    else:
        result.update(marker_state="invalid_value",
                      marker_detail=f"processed 값 해석 불명확: {token!r}")
    return result


def compute_revision(fm_lines, body: str) -> str:
    """
    source_revision_sha256 계산 규칙 (runbook 에도 문서화):
      1) BOM 제거, 줄바꿈을 \\n 으로 통일
      2) frontmatter 에서 최상위 키 processed / processed_date / processed_note 행 제거
      3) frontmatter 의 빈 행 제거 (YAML 의미 없음)
      4) '---\\n' + 남은 행 + '\\n---\\n' + 본문 을 UTF-8 로 SHA-256
    → 처리기가 완료 표시만 바꾼 경우 같은 버전, 본문·다른 메타데이터가 바뀌면 새 버전.
    """
    kept = [ln for ln in fm_lines
            if ln.strip() and top_level_key(ln) not in PROCESSOR_KEYS]
    canon = "---\n" + "\n".join(kept) + "\n---\n" + normalize_text(body)
    return sha256_text(canon)


def first_h1(body: str):
    in_code = False
    for line in body.split("\n"):
        if line.startswith("```"):
            in_code = not in_code
        if not in_code and line.startswith("# "):
            return line[2:].strip()
    return None


def set_processed_marker(text: str, value: bool, note: str, date_str: str) -> str:
    """
    frontmatter 의 processed* 행을 모두 지우고, 닫는 '---' 직전에 단일 행으로 다시 쓴다.
    다른 키의 행·순서·주석·인용 스타일은 문자 그대로 보존한다.
    (YAML 을 재덤프하지 않는 이유: 주석과 스타일 보존)
    """
    raw = normalize_text(text)
    fm_lines, body, has_fm, err = split_frontmatter(raw)
    if err:
        raise StageAError(f"frontmatter 수정 불가: {err}")
    note = note.replace("\n", " ").replace('"', "'")
    new_lines = [f"processed: {'true' if value else 'false'}"]
    if value:
        new_lines.append(f"processed_date: {date_str}")
    new_lines.append(f'processed_note: "{note}"')
    if not has_fm:
        return "---\n" + "\n".join(new_lines) + "\n---\n" + raw
    spans, span_err = processor_key_spans(fm_lines)
    if span_err:
        raise StageAError(span_err)
    drop = set(spans)
    kept = [ln for i, ln in enumerate(fm_lines) if i not in drop]
    # processed 사이에 끼어 있던 빈 행 때문에 frontmatter 끝에 빈 행이 남지 않게 정리
    while kept and not kept[-1].strip():
        kept.pop()
    return "---\n" + "\n".join(kept + new_lines) + "\n---\n" + body


# ──────────────────────────────────────────────────────────────────────────
# 2. 경로 안전
# ──────────────────────────────────────────────────────────────────────────

def resolve_vault(path) -> Path:
    """연결 경로(예: ~/Desktop/@26/dev)를 실제 경로로 해석한다."""
    p = Path(path).expanduser()
    if not p.exists():
        raise StageAError(f"Vault 경로가 존재하지 않음: {p}")
    real = p.resolve(strict=True)
    if not real.is_dir():
        raise StageAError(f"Vault 경로가 폴더가 아님: {real}")
    return real


def safe_rel_path(vault: Path, rel: str, allowed_roots) -> Path:
    """
    수정안에 적힌 상대 경로를 검증해 절대 경로로 돌려준다.
    거부 대상: 절대 경로, '..', 허용 루트 밖, 경로 중간·끝의 심볼릭 링크.
    (파일이 아직 없으면 존재하는 부모까지만 링크 검사)
    """
    if not isinstance(rel, str) or not rel.strip():
        raise StageAError("빈 경로")
    if rel.startswith("/") or rel.startswith("~") or "\\" in rel or "\x00" in rel:
        raise StageAError(f"절대 경로·특수 문자 경로 거부: {rel}")
    parts = Path(rel).parts
    if any(p in ("..", ".") for p in parts):
        raise StageAError(f"상위 경로 이동 거부: {rel}")
    if not rel.endswith(".md"):
        raise StageAError(f"Markdown 파일만 허용: {rel}")
    if not any(rel == r or rel.startswith(r.rstrip("/") + "/") for r in allowed_roots):
        raise StageAError(f"허용 범위 밖 경로: {rel} (허용: {', '.join(allowed_roots)})")
    cur = vault
    for part in parts:
        cur = cur / part
        if cur.is_symlink():
            raise StageAError(f"심볼릭 링크 경유 거부: {rel}")
    full = vault / rel
    real_parent = full.parent.resolve() if full.parent.exists() else None
    if real_parent is not None and vault not in (real_parent, *real_parent.parents):
        raise StageAError(f"Vault 탈출 거부: {rel}")
    return full


def ensure_outside(vault: Path, path: Path, what: str):
    """scan/plan 결과·상태 폴더가 Vault 안에 생기지 않게 막는다."""
    real = path.expanduser().resolve()
    if real == vault or vault in real.parents:
        raise StageAError(f"{what} 은(는) Vault 밖이어야 합니다: {real}")
    return real


def iter_markdown(vault: Path, roots):
    """허용 루트 아래 모든 .md (하위 폴더 포함, 심볼릭 링크는 따라가지 않음)."""
    missing = []
    found = []
    for root in roots:
        start = vault / root
        if start.is_symlink():
            missing.append({"root": root, "error": "루트가 심볼릭 링크 — 따라가지 않음"})
            continue
        if not start.is_dir():
            missing.append({"root": root, "error": "폴더 없음"})
            continue
        errors = []
        for d, dirs, files in os.walk(start, followlinks=False,
                                      onerror=lambda e: errors.append(str(e))):
            dirs[:] = sorted(x for x in dirs
                             if x not in EXCLUDED_DIRS and not (Path(d) / x).is_symlink())
            for name in sorted(files):
                p = Path(d) / name
                if p.suffix.lower() == ".md" and not p.is_symlink():
                    found.append(p)
        for e in errors:
            missing.append({"root": root, "error": f"읽기 실패: {e}"})
    return found, missing


# ──────────────────────────────────────────────────────────────────────────
# 3. 반영 블록
# ──────────────────────────────────────────────────────────────────────────

def make_op_id(source_rel: str, source_rev: str, target_rel: str, kind: str) -> str:
    """원문 경로 + 원문 버전 + 대상 + 종류 → 안정적인 작업 식별자."""
    return sha256_text(f"{source_rel}|{source_rev}|{target_rel}|{kind}")[:16]


def source_ref_line(source_rel: str) -> str:
    stem = Path(source_rel).stem
    return f"- 출처: [[{stem}]] (`{source_rel}`)"


def render_block(op_id: str, source_rel: str, source_rev: str, heading: str,
                 content: str) -> str:
    """
    반영 블록 = 시작 주석 + (제목) + 내용 + 출처 행 + 끝 주석.
    시작 주석에 내부 내용 해시를 기록해 나중에 '삭제·변경'을 감지한다.
    """
    inner_lines = []
    if heading:
        inner_lines.append(heading.strip())
        inner_lines.append("")
    inner_lines.append(content.strip())
    inner_lines.append("")
    inner_lines.append(source_ref_line(source_rel))
    inner = "\n".join(inner_lines)
    begin = (f"<!-- stage-a:begin id={op_id} source={source_rel.replace(' ', '%20')} "
             f"rev={source_rev[:12]} sha={sha256_text(inner)} -->")
    return f"{begin}\n{inner}\n{BLOCK_END_FMT.format(id=op_id)}"


def find_blocks(text: str, op_id: str | None = None):
    """문서 안의 반영 블록을 모두 찾는다. 반환: [{id, sha, inner, start_line, ...}]"""
    lines = normalize_text(text).split("\n")
    blocks = []
    i = 0
    while i < len(lines):
        m = BLOCK_BEGIN_RE.match(lines[i])
        if m and (op_id is None or m.group("id") == op_id):
            end_marker = BLOCK_END_FMT.format(id=m.group("id"))
            j = i + 1
            while j < len(lines) and lines[j] != end_marker:
                j += 1
            inner = "\n".join(lines[i + 1:j]) if j < len(lines) else None
            blocks.append({
                "id": m.group("id"), "sha": m.group("sha"),
                "source": m.group("source").replace("%20", " "),
                "rev": m.group("rev"), "inner": inner,
                "start_line": i + 1, "closed": j < len(lines),
            })
            i = j
        i += 1
    return blocks


def verify_block(text: str, op_id: str, source_rel: str, expected_sha: str | None = None):
    """
    반영 블록 검증. (ok, reason, block)
      - 정확히 1개 존재 / 닫힘 / 내부 해시 = 기록된 해시 / 출처 행 존재 / 실제 내용 존재
    '식별자만 있고 내용이 없는' 블록은 실패로 본다.
    """
    blocks = find_blocks(text, op_id)
    if not blocks:
        return False, "block_missing", None
    if len(blocks) > 1:
        return False, "block_duplicated", blocks[0]
    b = blocks[0]
    if not b["closed"] or b["inner"] is None:
        return False, "block_unclosed", b
    actual = sha256_text(b["inner"])
    if actual != b["sha"] or (expected_sha and actual != expected_sha):
        return False, "block_modified", b
    if source_ref_line(source_rel) not in b["inner"]:
        return False, "source_ref_missing", b
    content = b["inner"].replace(source_ref_line(source_rel), "")
    content = re.sub(r"^#+ .*$", "", content, flags=re.M)
    if len(re.sub(r"\s+", "", content)) < 20:
        return False, "block_empty", b
    return True, "ok", b


def insert_into_timeline(text: str, block: str) -> str:
    """
    '## Timeline' 섹션 끝(다음 '## ' 제목 직전 또는 문서 끝)에 블록을 추가한다.
    Timeline 이 없으면 문서 끝에 새로 만든다. 기존 행은 수정하지 않는다(append-only).
    """
    text = normalize_text(text)
    lines = text.split("\n")
    start = next((i for i, ln in enumerate(lines)
                  if re.match(r"^##\s+.*\btimeline\b", ln.strip(), re.I)), None)
    if start is None:
        base = text.rstrip("\n")
        return f"{base}\n\n## Timeline\n\n{block}\n"
    end = next((i for i in range(start + 1, len(lines))
                if lines[i].startswith("## ")), len(lines))
    head = lines[:end]
    while head and not head[-1].strip():
        head.pop()
    tail = lines[end:]
    out = head + ["", block, ""] + tail
    result = "\n".join(out)
    return result if result.endswith("\n") else result + "\n"


# ──────────────────────────────────────────────────────────────────────────
# 4. 파일 쓰기와 잠금
# ──────────────────────────────────────────────────────────────────────────

def atomic_write(path: Path, text: str):
    """같은 폴더의 임시 파일에 쓴 뒤 os.replace 로 교체 (중간 상태 노출 방지)."""
    fd, tmp = tempfile.mkstemp(dir=str(path.parent), prefix=f".{path.name}.", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(text)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, path)
    except BaseException:
        if os.path.exists(tmp):
            os.unlink(tmp)
        raise


def atomic_create(path: Path, text: str):
    """신규 파일 생성 — 이미 있으면 FileExistsError (절대 덮어쓰지 않음)."""
    fd, tmp = tempfile.mkstemp(dir=str(path.parent), prefix=f".{path.name}.", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(text)
            f.flush()
            os.fsync(f.fileno())
        os.link(tmp, path)  # 대상이 존재하면 실패 → 덮어쓰기 불가능
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)


def default_lock_dir() -> Path:
    return Path.home() / ".cache" / "csp-brain-stage-a" / "locks"


@contextmanager
def vault_lock(vault: Path, lock_dir: Path):
    """
    실제 Vault 경로 기준 배타 잠금. 연결 경로로 실행해도 같은 잠금 파일을 쓴다.
    잠금을 쓰지 않는 외부 편집기까지 막지는 못하므로, 적용 직전 해시 대조를 함께 쓴다.
    """
    lock_dir.mkdir(parents=True, exist_ok=True)
    key = sha256_text(str(vault))[:16]
    lock_path = lock_dir / f"{key}.lock"
    fh = open(lock_path, "a+")
    try:
        try:
            fcntl.flock(fh.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            raise StageAError(f"다른 실행이 같은 Vault 를 처리 중 (잠금: {lock_path})")
        fh.seek(0)
        fh.truncate()
        fh.write(f"pid={os.getpid()} vault={vault} at={now_iso()}\n")
        fh.flush()
        yield lock_path
    finally:
        try:
            fcntl.flock(fh.fileno(), fcntl.LOCK_UN)
        finally:
            fh.close()


def now_iso() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def fault(point: str):
    """
    테스트용 강제 실패 지점. 환경변수 STAGE_A_FAULT 에 지점 이름을 넣으면 발동.
      'marker_write'          → 프로세스 강제 중단(SystemExit)을 흉내
      'marker_write:oserror'  → 디스크 쓰기 실패(OSError)를 흉내 — 처리기가 잡아서 기록해야 함
    """
    for spec in os.environ.get("STAGE_A_FAULT", "").split(","):
        name, _, mode = spec.partition(":")
        if point and name == point:
            if mode == "oserror":
                raise OSError(f"[FAULT] 쓰기 실패 흉내: {point}")
            raise SystemExit(f"[FAULT] 강제 중단: {point}")


# ──────────────────────────────────────────────────────────────────────────
# 5. SQLite 처리 기록
# ──────────────────────────────────────────────────────────────────────────

DB_NAME = "stage_a_state.sqlite3"

SCHEMA = """
CREATE TABLE IF NOT EXISTS sources (
    source_path TEXT NOT NULL,
    source_revision TEXT NOT NULL,
    decision TEXT,
    status TEXT NOT NULL,            -- pending/held/failed/verified
    marker_status TEXT,              -- none/written/failed/not_needed
    index_status TEXT,               -- none/written/failed/not_needed
    reason TEXT,
    plan_sha256 TEXT,
    run_id TEXT,
    updated_at TEXT NOT NULL,
    PRIMARY KEY (source_path, source_revision)
);
CREATE TABLE IF NOT EXISTS operations (
    op_id TEXT PRIMARY KEY,
    source_path TEXT NOT NULL,
    source_revision TEXT NOT NULL,
    kind TEXT NOT NULL,              -- merge/new/evidence/marker/index
    target_path TEXT NOT NULL,
    stage TEXT NOT NULL,             -- intent/written/verified/failed
    block_sha256 TEXT,
    evidence_sha256 TEXT,
    evidence_text TEXT,
    target_sha_before TEXT,
    target_sha_after TEXT,
    backup_path TEXT,
    error TEXT,
    run_id TEXT,
    updated_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ts TEXT NOT NULL,
    run_id TEXT,
    source_path TEXT,
    op_id TEXT,
    stage TEXT,
    detail TEXT
);
"""


def open_db(state_dir: Path) -> sqlite3.Connection:
    state_dir.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(state_dir / DB_NAME), timeout=10)
    conn.row_factory = sqlite3.Row
    conn.executescript(SCHEMA)
    return conn


def open_db_readonly(state_dir: Path):
    """읽기 전용 열기. 파일이 없으면 None (→ '집계 불가', 검증 완료로 추정하지 않음)."""
    db = Path(state_dir) / DB_NAME
    if not db.is_file():
        return None
    conn = sqlite3.connect(f"file:{db}?mode=ro", uri=True, timeout=10)
    conn.row_factory = sqlite3.Row
    return conn


def log_event(conn, run_id, source_path, op_id, stage, detail=""):
    fault(f"db_event_{stage}")
    conn.execute("INSERT INTO events(ts, run_id, source_path, op_id, stage, detail) "
                 "VALUES (?,?,?,?,?,?)", (now_iso(), run_id, source_path, op_id, stage, detail))


def upsert_op(conn, op: dict):
    op = dict(op, updated_at=now_iso())
    cols = ",".join(op)
    marks = ",".join("?" for _ in op)
    updates = ",".join(f"{k}=excluded.{k}" for k in op if k != "op_id")
    conn.execute(f"INSERT INTO operations({cols}) VALUES ({marks}) "
                 f"ON CONFLICT(op_id) DO UPDATE SET {updates}", tuple(op.values()))


def upsert_source(conn, row: dict):
    row = dict(row, updated_at=now_iso())
    cols = ",".join(row)
    marks = ",".join("?" for _ in row)
    updates = ",".join(f"{k}=excluded.{k}" for k in row
                       if k not in ("source_path", "source_revision"))
    conn.execute(f"INSERT INTO sources({cols}) VALUES ({marks}) "
                 f"ON CONFLICT(source_path, source_revision) DO UPDATE SET {updates}",
                 tuple(row.values()))


def get_op(conn, op_id):
    return conn.execute("SELECT * FROM operations WHERE op_id=?", (op_id,)).fetchone()


# ──────────────────────────────────────────────────────────────────────────
# 6. 효과적 상태 (처리기·대시보드 공통)
# ──────────────────────────────────────────────────────────────────────────

def verify_operation(vault: Path, op) -> tuple[bool, str]:
    """처리 기록 1건을 실제 대상 본문과 대조한다 (읽기 전용)."""
    target = vault / op["target_path"]
    if target.is_symlink() or not target.is_file():
        return False, "target_missing"
    text = target.read_text(encoding="utf-8")
    if op["kind"] in ("merge", "new"):
        ok, reason, _ = verify_block(text, op["op_id"], op["source_path"], op["block_sha256"])
        return ok, reason
    if op["kind"] == "evidence":
        ev = op["evidence_text"] or ""
        if not ev or ev not in normalize_text(text):
            return False, "evidence_missing"
        if sha256_text(ev) != op["evidence_sha256"]:
            return False, "evidence_record_mismatch"
        return True, "ok"
    return True, "ok"


def effective_status(vault: Path, rel: str, analysis: dict, conn) -> tuple[str, str]:
    """
    한 원문의 효과적 상태를 결정한다.
      verified 는 '처리 기록의 verified + 현재 원문 버전 일치 + 대상 본문 재검증 통과
      + 원문 완료 표시'가 모두 성립할 때만.
    """
    ms = analysis["marker_state"]
    if ms == "conflict":
        return "conflict", analysis.get("marker_detail") or ""
    if ms in ("yaml_error", "unsupported", "invalid_value"):
        return "held", analysis.get("marker_detail") or ms
    rev = analysis["revision_sha256"]
    row = None
    if conn is not None:
        row = conn.execute("SELECT * FROM sources WHERE source_path=? AND source_revision=?",
                           (rel, rev)).fetchone()
    if row is not None:
        if row["status"] == "verified":
            ops = conn.execute("SELECT * FROM operations WHERE source_path=? AND source_revision=? "
                               "AND kind IN ('merge','new','evidence')", (rel, rev)).fetchall()
            if not ops:
                return "failed", "verified 기록에 대상 작업 없음"
            for op in ops:
                ok, why = verify_operation(vault, op)
                if not ok:
                    return "failed", f"{op['target_path']}: {why}"
            if ms != "marked_true":
                return "failed", "검증은 통과했으나 원문 완료 표시 누락 (apply 재실행으로 복구)"
            return "verified", ""
        if row["status"] == "held" and ms == "marked_true":
            # 기존 완료 표시 + 이번 검토에서 보류 → 여전히 '미검증 기존 표시'로 집계
            return "legacy_unverified", f"보류: {row['reason'] or ''}"
        if row["status"] in ("held", "failed"):
            return row["status"], row["reason"] or ""
        if row["status"] == "pending" and ms != "marked_true":
            return "pending", row["reason"] or ""
    if ms == "marked_true":
        # 이전 원문 버전이 검증됐는데 원문 내용이 바뀐 경우도 여기로 온다
        if conn is not None:
            old = conn.execute("SELECT 1 FROM sources WHERE source_path=? AND status='verified'",
                               (rel,)).fetchone()
            if old:
                return "failed", "검증 이후 원문 내용 변경 — 재검토 필요"
        return "legacy_unverified", ""
    return "pending", ""
