"""
OKF PUBLISH 프로토콜 — csp-brain (7번째 프로토콜).

옵시디언 작성본을 OKF v0.1 conformant 번들로 발행한다.
설계 정본: _ops/okf/OKF_ADOPTION_SPEC.md
실행 사양: _ops/okf/OKF_PUBLISH_PROTOCOL.md
빌드 순서: _ops/okf/OKF_BUILD_PLAN.md

핵심 안전 원칙:
  - 작성본(번들 IN 원본)은 절대 수정하지 않는다. 출력은 --out(기본 dist/okf)로만.
  - 기본 --dry-run. 실제 쓰기는 --write 명시.
  - 멱등(idempotent): 같은 입력 → 같은 출력.

현재 구현 범위: Phase 1 (discover · derive_type · check_conformance).
  Phase 2 단계(frontmatter/index/links/log/relations 쓰기)는 스텁으로 둔다.
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

import yaml

# ─────────────────────────────────────────────────────────────────────────────
# 설정 — SPEC §3/§5 + Phase 0 보정(§11) 반영본
# ─────────────────────────────────────────────────────────────────────────────

# 번들 IN (conformance 대상). Phase 0 보정: 루트 concepts/people/decisions/
# permanent/moc 는 제외(추출 덤프·슬라이드·빈 폴더). 정본 = wiki/** + projects/**.
BUNDLE_IN = ["wiki", "projects", "references", "research", "analysis"]

# 경로 prefix → OKF type. 긴 prefix 우선(아래 derive_type 에서 정렬).
# PascalCase 정규화(§11 보정 2). wiki/signals·wiki/protocols 추가(§11 보정 2).
TYPE_MAP = [
    ("wiki/concepts", "Concept"),
    ("wiki/tools", "Tool"),
    ("wiki/frameworks", "Framework"),
    ("wiki/skills", "Skill"),
    ("wiki/decisions", "Decision"),
    ("wiki/people", "Person"),
    ("wiki/signals", "Signal"),
    ("wiki/protocols", "Protocol"),
    ("wiki/projects", "Project"),
    ("projects", "Project"),
    ("references", "Reference"),
    ("research", "Research"),
    ("analysis", "Analysis"),
]
FALLBACK_TYPE = "Concept"

# 기존 프론트매터 type 값 → PascalCase 정규화(§11 보정 2).
# CLAUDE.md 소문자 방언과 SPEC PascalCase 를 통일한다.
TYPE_NORMALIZE = {
    "concept": "Concept", "tool": "Tool", "framework": "Framework",
    "skill": "Skill", "decision": "Decision", "person": "Person",
    "signal": "Signal", "protocol": "Protocol", "project": "Project",
    "reference": "Reference", "research": "Research", "analysis": "Analysis",
    "note": "Note",
}

# status 단어 방언 ↔ 이모지 정규화(§11 보정 3). 발행본은 이모지로 통일.
STATUS_NORMALIZE = {
    "seed": "💡", "growing": "🔄", "mature": "✅", "archived": "📦",
}

# 예약 파일(conformance 비대상 — 별도 규칙으로 처리).
RESERVED = {"_index.md", "index.md", "log.md"}

# 루트 정크 격리 대상(§3.2, BUILD_PLAN Phase 1). 파일명 기준.
JUNK_NAME_RE = re.compile(
    r"^(무제|이름 없는 보드|untitled-daily-\d+|temp_readme)\.md$"
)
# 비정형(비 ISO) 날짜 파일명: 2605.md, 260506.md, 260429.md 등 6자리 yymmdd.
NONISO_DATE_RE = re.compile(r"^\d{4,6}\.md$")
# ISO 날짜 파일명(허용): 2026-04-29.md.
ISO_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}\.md$")

WIKILINK_RE = re.compile(r"!?\[\[[^\]]+\]\]")

# ─────────────────────────────────────────────────────────────────────────────
# 자료구조
# ─────────────────────────────────────────────────────────────────────────────


@dataclass
class Concept:
    src: Path                       # 작성본 절대경로
    rel: str                        # 번들 상대경로 (예: wiki/concepts/foo.md)
    frontmatter: dict = field(default_factory=dict)
    fm_status: str = "none"         # "ok" | "none" | "malformed"
    body: str = ""
    lint: list[tuple[str, str]] = field(default_factory=list)  # (code, detail)

    @property
    def has_frontmatter(self) -> bool:
        return self.fm_status == "ok"


@dataclass
class Finding:
    code: str
    severity: str                   # ERROR | WARN | INFO
    rel: str
    detail: str = ""


SEVERITY = {
    "missing-frontmatter": "ERROR",
    "malformed-frontmatter": "ERROR",
    "missing-type": "ERROR",
    "bad-index": "ERROR",
    "type-fallback": "WARN",
    "type-conflict": "WARN",
    "ambiguous-link": "WARN",
    "legacy-dialect": "WARN",
    "unresolved-link": "INFO",
    "relation-target-missing": "INFO",
    "root-junk": "WARN",
}

# ─────────────────────────────────────────────────────────────────────────────
# [1] derive_type — 경로 prefix → type
# ─────────────────────────────────────────────────────────────────────────────


def derive_type(rel: str) -> tuple[str, bool]:
    """번들 상대경로 → (type, is_fallback). 긴 prefix 우선."""
    rel = rel.replace("\\", "/")
    for prefix, t in sorted(TYPE_MAP, key=lambda x: -len(x[0])):
        if rel.startswith(prefix + "/") or rel == prefix:
            return t, False
    return FALLBACK_TYPE, True


def normalize_type(value: str) -> str:
    """기존 프론트매터 type 값을 PascalCase 로 정규화(§11 보정 2)."""
    if not value:
        return value
    return TYPE_NORMALIZE.get(value.strip().lower(), value.strip())


# ─────────────────────────────────────────────────────────────────────────────
# [0] discover — 번들 IN 스캔
# ─────────────────────────────────────────────────────────────────────────────


def parse_frontmatter(text: str) -> tuple[dict, str, str]:
    """선두 YAML 프론트매터 분리. (frontmatter, status, body) 반환.

    status: "ok"        — 구분자 + 유효 YAML dict
            "none"      — `---` 구분자 블록 없음
            "malformed" — 블록은 있으나 YAML 파싱 실패/비-dict
    BOM·CRLF 를 관대하게 처리한다.
    """
    text = text.lstrip("﻿")  # concepts/ 덤프 등의 BOM 제거
    if not text.startswith("---"):
        return {}, "none", text
    # 두 번째 --- 구분자 탐색
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", text, re.DOTALL)
    if not m:
        return {}, "malformed", text  # 여는 ---는 있으나 닫는 구분자 없음
    raw, body = m.group(1), m.group(2)
    try:
        data = yaml.safe_load(raw)
    except yaml.YAMLError:
        return {}, "malformed", body
    if not isinstance(data, dict):
        return {}, "malformed", body
    return data, "ok", body


def discover(root: Path, bundle_in=None) -> tuple[list[Concept], dict[str, list[str]]]:
    """번들 IN 스캔 → (Concept 목록, 전역 파일명 인덱스).

    전역 파일명 인덱스: stem(소문자) → [rel, ...]. 위키링크 해석(Phase 2)에 쓴다.
    충돌(같은 이름 둘 이상)은 리스트 길이로 드러난다.
    """
    bundle_in = bundle_in or BUNDLE_IN
    concepts: list[Concept] = []
    name_index: dict[str, list[str]] = {}
    for top in bundle_in:
        base = root / top
        if not base.is_dir():
            continue
        for path in sorted(base.rglob("*.md")):
            rel = path.relative_to(root).as_posix()
            name = path.name
            try:
                text = path.read_text(encoding="utf-8")
            except (UnicodeDecodeError, OSError):
                text = ""
            fm, status, body = parse_frontmatter(text)
            c = Concept(src=path, rel=rel, frontmatter=fm or {},
                        fm_status=status, body=body)
            concepts.append(c)
            if name not in RESERVED:
                name_index.setdefault(path.stem.lower(), []).append(rel)
    return concepts, name_index


# ─────────────────────────────────────────────────────────────────────────────
# 루트 정크 격리 큐(§3.2). 파괴적 이동/삭제는 하지 않고 목록만 만든다.
# ─────────────────────────────────────────────────────────────────────────────


def scan_root_junk(root: Path) -> list[str]:
    """리포 루트의 정크 .md 파일명 목록. 이동/삭제는 사람이 확인 후."""
    junk = []
    for path in sorted(root.glob("*.md")):
        name = path.name
        if JUNK_NAME_RE.match(name) or NONISO_DATE_RE.match(name):
            junk.append(name)
        elif ISO_DATE_RE.match(name):
            junk.append(name)  # 루트 데일리 — 번들 OUT, 격리 후보
    return junk


# ─────────────────────────────────────────────────────────────────────────────
# [7] check_conformance — SPEC §8 검사
# ─────────────────────────────────────────────────────────────────────────────


def check_conformance(concepts: list[Concept],
                      published: bool = False) -> list[Finding]:
    """SPEC §8 기준으로 Concept 목록을 검사 → Finding 목록.

    published=False: 작성본(번들 IN) 베이스라인. 위키링크 잔존을 legacy-dialect 로 본다.
    published=True : 발행본. 위키링크 잔존은 미해석/모호 링크(별도 보고)이므로 여기선 무시.
    """
    findings: list[Finding] = []
    for c in concepts:
        name = Path(c.rel).name
        # log.md 는 OKF 예약 생성 파일(프론트매터 없음이 정상). 검사 제외.
        if name == "log.md":
            continue
        is_index = name in ("_index.md", "index.md")

        # 예약 파일: index 계열은 프론트매터 없어야 함.
        # 예외: 번들 루트 index.md 는 okf_version 프론트매터 허용(§6.3).
        if is_index:
            if c.has_frontmatter and name == "index.md" and c.rel != "index.md":
                findings.append(Finding("bad-index", "ERROR", c.rel,
                                        "index.md 에 프론트매터 존재"))
            if name == "_index.md":
                findings.append(Finding("legacy-dialect", "WARN", c.rel,
                                        "_index 잔존(발행 시 index.md 로 변환)"))
            continue

        # 1. 프론트매터 파싱 가능?
        if c.fm_status == "none":
            findings.append(Finding("missing-frontmatter", "ERROR", c.rel))
            continue  # type 검사 무의미
        if c.fm_status == "malformed":
            # 블록은 있으나 YAML 파싱 실패. csp-brain 다수 사례:
            # related_to: "[[a]]", "[[b]]" 처럼 쉼표 나열(§11 보정 4 대상).
            findings.append(Finding("malformed-frontmatter", "ERROR", c.rel,
                                    "YAML 파싱 실패(예: related_to 다중 위키링크)"))
            continue

        # 2. type 존재?
        t = c.frontmatter.get("type")
        derived, fallback = derive_type(c.rel)
        if not t or not str(t).strip():
            findings.append(Finding("missing-type", "ERROR", c.rel,
                                    f"유도 type={derived}"))
        else:
            norm = normalize_type(str(t))
            if not fallback and norm != derived:
                findings.append(Finding("type-conflict", "WARN", c.rel,
                                        f"기존={norm} 유도={derived}"))
        if fallback:
            findings.append(Finding("type-fallback", "WARN", c.rel,
                                    f"prefix 매칭 실패 → {FALLBACK_TYPE}"))

        # 5. 레거시 방언: 작성본 베이스라인에서만 위키링크 잔존을 센다.
        #    발행본의 잔존 [[ ]]는 미해석/모호 링크로 별도 보고(중복 방지).
        if not published and WIKILINK_RE.search(c.body):
            n = len(WIKILINK_RE.findall(c.body))
            findings.append(Finding("legacy-dialect", "WARN", c.rel,
                                    f"위키링크 {n}건(발행 시 변환 대상)"))
    return findings


# ─────────────────────────────────────────────────────────────────────────────
# 리포트 생성
# ─────────────────────────────────────────────────────────────────────────────


def render_report(findings: list[Finding], junk: list[str],
                  total_files: int) -> str:
    """lint-report.md 텍스트. 상단 요약표 + 파일별 상세."""
    counts: dict[str, int] = {}
    for f in findings:
        counts[f.code] = counts.get(f.code, 0) + 1
    errors = sum(1 for f in findings if f.severity == "ERROR")
    warns = sum(1 for f in findings if f.severity == "WARN")
    infos = sum(1 for f in findings if f.severity == "INFO")
    gate = "PASS ✅" if errors == 0 else "FAIL ❌"

    lines = [
        "# OKF Conformance Report",
        "",
        f"> 생성: {datetime.now().isoformat(timespec='seconds')}",
        f"> 대상 파일: {total_files}개 (번들 IN: {', '.join(BUNDLE_IN)})",
        f"> 게이트: **{gate}** (ERROR {errors} · WARN {warns} · INFO {infos})",
        "",
        "## 요약 (코드별 건수)",
        "",
        "| 코드 | severity | 건수 |",
        "| --- | --- | ---: |",
    ]
    for code in sorted(counts, key=lambda c: (SEVERITY.get(c, "ZZZ"), c)):
        lines.append(f"| `{code}` | {SEVERITY.get(code, '?')} | {counts[code]} |")
    if not counts:
        lines.append("| (없음) | — | 0 |")

    lines += ["", "## 루트 정크 격리 큐", ""]
    if junk:
        lines.append(f"> {len(junk)}건. **이동/삭제는 사람 확인 후** (BUILD_PLAN 안전 체크리스트).")
        lines.append("")
        for n in junk:
            lines.append(f"- [ ] `{n}` → `inbox/raw/` 이동 또는 삭제")
    else:
        lines.append("- (없음)")

    lines += ["", "## 파일별 상세", ""]
    by_code: dict[str, list[Finding]] = {}
    for f in findings:
        by_code.setdefault(f.code, []).append(f)
    for code in sorted(by_code, key=lambda c: (SEVERITY.get(c, "ZZZ"), c)):
        lines.append(f"### `{code}` ({SEVERITY.get(code, '?')}) — {len(by_code[code])}건")
        lines.append("")
        for f in by_code[code][:200]:
            d = f" — {f.detail}" if f.detail else ""
            lines.append(f"- `{f.rel}`{d}")
        if len(by_code[code]) > 200:
            lines.append(f"- … 외 {len(by_code[code]) - 200}건")
        lines.append("")
    return "\n".join(lines) + "\n"


# ─────────────────────────────────────────────────────────────────────────────
# Phase 2 — 변환 단계 (frontmatter 수리/보강 · index · wikilink · log)
# ─────────────────────────────────────────────────────────────────────────────


def git_last_commit_iso(p: Path) -> str:
    try:
        out = subprocess.run(
            ["git", "log", "-1", "--format=%cI", str(p)],
            capture_output=True, text=True, check=False,
        )
        return out.stdout.strip()
    except OSError:
        return ""


# malformed 수리: `key: "[[a]]", "[[b]]"` (쉼표 나열) → YAML 블록 리스트.
_MULTI_WIKILINK_RE = re.compile(
    r'^(?P<key>\w[\w-]*):\s*(?P<val>"?\[\[.+?\]\]"?(?:\s*,\s*"?\[\[.+?\]\]"?)+)\s*$'
)
# 단일 비인용 위키링크: `key: [[a]]` → `key: "[[a]]"` (YAML 플로우 시퀀스 오인 방지).
_SINGLE_WIKILINK_RE = re.compile(
    r'^(?P<key>\w[\w-]*):\s*(?P<val>\[\[.+?\]\])\s*$'
)


def repair_frontmatter_text(raw: str) -> tuple[str, bool]:
    """malformed YAML 프론트매터를 보수적으로 수리. (수리본, 변경여부).

    csp-brain 최빈 패턴: related_to 등에 위키링크를 쉼표로 나열 → 유효 YAML 아님.
    이를 블록 리스트로, 단일 비인용 위키링크는 인용 스칼라로 바꾼다(§11 보정 4 선행).
    """
    out, changed = [], False
    for line in raw.splitlines():
        m = _MULTI_WIKILINK_RE.match(line)
        if m:
            key = m.group("key")
            items = re.findall(r'\[\[.+?\]\]', m.group("val"))
            out.append(f"{key}:")
            for it in items:
                out.append(f'  - "{it}"')
            changed = True
            continue
        m = _SINGLE_WIKILINK_RE.match(line)
        if m:
            out.append(f'{m.group("key")}: "{m.group("val")}"')
            changed = True
            continue
        out.append(line)
    return "\n".join(out), changed


def ensure_frontmatter(c: Concept, root: Path) -> None:
    """비파괴 보강. malformed면 수리 시도, 누락 키만 채움(§3.2).

    작성본은 만지지 않는다 — c.frontmatter(메모리)만 갱신한다.
    """
    if c.fm_status == "malformed":
        # 원문에서 프론트매터 블록만 재추출해 수리 후 재파싱.
        text = c.src.read_text(encoding="utf-8").lstrip("﻿")
        m = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", text, re.DOTALL)
        if m:
            repaired, changed = repair_frontmatter_text(m.group(1))
            try:
                data = yaml.safe_load(repaired)
                if isinstance(data, dict):
                    c.frontmatter = data
                    c.fm_status = "ok"
                    if changed:
                        c.lint.append(("repaired-frontmatter",
                                       "malformed YAML 수리(위키링크 리스트화)"))
            except yaml.YAMLError:
                pass

    # 누락 키 보강 (기존 값 우선).
    derived, fallback = derive_type(c.rel)
    if not c.frontmatter.get("type"):
        c.frontmatter["type"] = derived
        if fallback:
            c.lint.append(("type-fallback", f"→ {FALLBACK_TYPE}"))
    else:
        c.frontmatter["type"] = normalize_type(str(c.frontmatter["type"]))
    if not c.frontmatter.get("title"):
        c.frontmatter["title"] = c.src.stem
    if not c.frontmatter.get("timestamp"):
        ts = git_last_commit_iso(c.src)
        if ts:
            c.frontmatter["timestamp"] = ts
    # status 단어 → 이모지 정규화(§11 보정 3).
    st = c.frontmatter.get("status")
    if isinstance(st, str) and st.strip().lower() in STATUS_NORMALIZE:
        c.frontmatter["status"] = STATUS_NORMALIZE[st.strip().lower()]


def serialize_frontmatter(fm: dict) -> str:
    """프론트매터 dict → `---\\n...\\n---` 블록. type 을 맨 위로."""
    ordered = {}
    for key in ("type", "title", "description", "status", "importance",
                "tags", "timestamp"):
        if key in fm:
            ordered[key] = fm[key]
    for k, v in fm.items():
        if k not in ordered:
            ordered[k] = v
    dumped = yaml.safe_dump(ordered, allow_unicode=True, sort_keys=False,
                            default_flow_style=False).strip()
    return f"---\n{dumped}\n---\n"


def slugify(name: str) -> str:
    """링크 해석용 정규화: 소문자, 공백→-, 괄호 주석 제거(§11 보정 5)."""
    name = re.sub(r"\([^)]*\)", "", name)          # (주석) 제거
    name = name.strip().lower().replace(" ", "-")
    return re.sub(r"-+", "-", name).strip("-")


def build_link_index(concepts: list[Concept]) -> dict[str, set[str]]:
    """링크 해석 인덱스: key(여러 형태) → {rel,...}.

    key 형태: 파일 stem, slug(stem), frontmatter title·aliases 의 slug.
    """
    index: dict[str, set[str]] = {}

    def add(key: str, rel: str):
        if key:
            index.setdefault(key, set()).add(rel)

    for c in concepts:
        if Path(c.rel).name in RESERVED:
            continue
        stem = Path(c.rel).stem
        add(stem.lower(), c.rel)
        add(slugify(stem), c.rel)
        fm = c.frontmatter or {}
        title = fm.get("title")
        if isinstance(title, str):
            add(slugify(title), c.rel)
        aliases = fm.get("aliases")
        if isinstance(aliases, str):
            aliases = [aliases]
        if isinstance(aliases, list):
            for a in aliases:
                if isinstance(a, str):
                    add(slugify(a), c.rel)
    return index


def rename_index(rel: str) -> str:
    """`_index.md` → `index.md` (경로 보존)."""
    return rel.replace("/_index.md", "/index.md")
    # 루트 단독 _index.md 케이스는 번들 IN 에 없음(전부 wiki/<sub>/).


def _resolve_target(target: str, link_index: dict[str, set[str]],
                    rel_set: set[str]) -> tuple[str | None, str | None]:
    """위키링크 target → (bundle-relative path, lint-code).

    반환 path 는 `/`로 시작하는 번들 절대경로. 실패 시 (None, code).
    """
    target = target.strip()
    if "/" in target:  # 경로형
        p = target
        if not p.endswith(".md"):
            p = p + ".md"
        p = p.replace("/_index.md", "/index.md")
        cand = p.lstrip("/")
        if cand in rel_set or rename_index(cand) in rel_set:
            return "/" + rename_index(cand), None
        return "/" + cand, None  # 경로형은 명시적이므로 신뢰(미존재여도 INFO 아님)
    # 이름형/별칭형
    for key in (target.lower(), slugify(target)):
        hits = link_index.get(key)
        if hits:
            if len(hits) == 1:
                return "/" + next(iter(hits)), None
            return None, "ambiguous-link"
    return None, "unresolved-link"


def convert_wikilinks(body: str, link_index: dict[str, set[str]],
                      rel_set: set[str]) -> tuple[str, list[tuple[str, str]]]:
    """본문 [[...]] → bundle-relative 마크다운 링크. (변환본, lint 목록)."""
    lint: list[tuple[str, str]] = []

    def repl(m: re.Match) -> str:
        whole = m.group(0)
        embed = whole.startswith("!")
        inner = whole[3:-2] if embed else whole[2:-2]   # ![[ ]] / [[ ]]
        # 별칭 분리
        if "|" in inner:
            target, label = inner.split("|", 1)
        else:
            target, label = inner, None
        # heading anchor 분리
        anchor = ""
        if "#" in target:
            target, anchor = target.split("#", 1)
            anchor = "#" + anchor
        path, code = _resolve_target(target, link_index, rel_set)
        if path is None:
            lint.append((code, inner))
            return whole  # placeholder 보존
        text = label if label else (Path(target).name if "/" in target else target)
        if embed:
            return f"![{text}]({path}{anchor})"
        return f"[{text}]({path}{anchor})"

    new = re.sub(r"!?\[\[[^\]]+\]\]", repl, body)
    return new, lint


# 시계열 인식: `### 2026-05-16` 또는 `### 2026-05-31 (Planned)` (§11 보정 6).
_TIMELINE_DATE_RE = re.compile(
    r"^#{2,4}\s+(?P<date>\d{4}-\d{2}-\d{2})\s*(?P<suffix>\([^)]*\))?\s*$"
)
_WEEKLY_FILE_RE = re.compile(r"^(\d{4})-W(\d{2})\.md$")


def extract_timeline_entries(text: str) -> list[tuple[str, list[str]]]:
    """본문에서 `### <ISO-date>` 블록 추출 → [(date, [bullet,...])]."""
    entries: list[tuple[str, list[str]]] = []
    cur_date, cur_lines = None, []
    for line in text.splitlines():
        m = _TIMELINE_DATE_RE.match(line)
        if m:
            if cur_date:
                entries.append((cur_date, cur_lines))
            planned = m.group("suffix") or ""
            cur_date = m.group("date") + (" " + planned if planned else "")
            cur_lines = []
        elif cur_date is not None:
            s = line.strip()
            if s.startswith(("-", "*")):
                # 선행 리스트 마커 한 개만 제거(굵게 ** 보존).
                cur_lines.append(re.sub(r"^[-*]\s+", "", s).strip())
    if cur_date:
        entries.append((cur_date, cur_lines))
    return entries


def generate_log(entries: list[tuple[str, list[str]]]) -> str:
    """OKF §7 log.md 텍스트. ISO 날짜 헤딩 강제."""
    out = ["# Directory Update Log", ""]
    for date, bullets in entries:
        out.append(f"## {date}")
        if bullets:
            for b in bullets:
                label = "Planned" if "Planned" in date else "Update"
                out.append(f"* **{label}**: {b}")
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def build_index_md(dir_concepts: list[Concept]) -> str:
    """디렉터리 색인 → OKF index.md (프론트매터 없음). §6.3."""
    out = ["# Index", ""]
    for c in sorted(dir_concepts, key=lambda x: x.rel):
        fm = c.frontmatter or {}
        title = fm.get("title") or Path(c.rel).stem
        desc = fm.get("description", "")
        url = "/" + (rename_index(c.rel))
        line = f"* [{title}]({url})"
        if desc:
            line += f" - {desc}"
        out.append(line)
    return "\n".join(out) + "\n"


def publish_bundle(root: Path, out: Path, dry_run: bool) -> tuple[list[Finding], dict]:
    """전체 PUBLISH 패스. 작성본 → dist/okf 번들. (output 기준 findings, 통계)."""
    concepts, _ = discover(root)
    for c in concepts:
        ensure_frontmatter(c, root)
    link_index = build_link_index(concepts)
    rel_set = {c.rel for c in concepts} | {rename_index(c.rel) for c in concepts}

    stats = {"files": 0, "wikilinks_converted": 0, "ambiguous": 0,
             "unresolved": 0, "repaired": 0, "logs": 0, "indexes": 0}
    written: list[tuple[str, str]] = []   # (out-rel, content)
    link_findings: list[Finding] = []
    by_dir: dict[str, list[Concept]] = {}

    for c in concepts:
        name = Path(c.rel).name
        if name == "_index.md":
            continue  # index.md 는 디렉터리 단위로 따로 생성
        total_links = len(WIKILINK_RE.findall(c.body))
        body, link_lint = convert_wikilinks(c.body, link_index, rel_set)
        for code, inner in link_lint:
            link_findings.append(Finding(code, SEVERITY[code], rename_index(c.rel),
                                         inner))
            if code == "ambiguous-link":
                stats["ambiguous"] += 1
            elif code == "unresolved-link":
                stats["unresolved"] += 1
        stats["wikilinks_converted"] += total_links - len(link_lint)
        if any(code == "repaired-frontmatter" for code, _ in c.lint):
            stats["repaired"] += 1
        content = serialize_frontmatter(c.frontmatter) + "\n" + body.lstrip("\n")
        out_rel = rename_index(c.rel)
        written.append((out_rel, content))
        by_dir.setdefault(str(Path(c.rel).parent), []).append(c)

        # projects/<proj> Timeline → 같은 디렉터리 log.md (§11 보정 6).
        if c.rel.startswith("projects/"):
            entries = extract_timeline_entries(c.body)
            if entries:
                log_rel = str(Path(c.rel).parent / "log.md")
                written.append((log_rel, generate_log(entries)))
                stats["logs"] += 1

    # 디렉터리별 index.md (원래 _index.md 있던 곳).
    index_dirs = {str(Path(c.rel).parent) for c in concepts
                  if Path(c.rel).name == "_index.md"}
    for d in index_dirs:
        members = [c for c in concepts
                   if str(Path(c.rel).parent) == d and Path(c.rel).name != "_index.md"]
        written.append((str(Path(d) / "index.md"), build_index_md(members)))
        stats["indexes"] += 1

    # 번들 루트 index.md (okf_version 선언 — 프론트매터 허용 유일 index).
    root_index = ('---\nokf_version: "0.1"\n---\n\n# csp-brain OKF Bundle\n\n'
                  "옵시디언 작성본에서 발행된 OKF v0.1 conformant 번들.\n")
    written.append(("index.md", root_index))

    # 중복 log.md 제거(같은 경로 마지막 우선).
    dedup: dict[str, str] = {}
    for rel, content in written:
        dedup[rel] = content
    stats["files"] = len(dedup)

    if not dry_run:
        out.mkdir(parents=True, exist_ok=True)
        for rel, content in dedup.items():
            dest = out / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(content, encoding="utf-8")

    # 발행본 기준 conformance 재검사 (메모리 상 Concept 재구성).
    out_concepts = []
    for rel, content in dedup.items():
        fm, status, body = parse_frontmatter(content)
        out_concepts.append(Concept(src=out / rel, rel=rel, frontmatter=fm or {},
                                    fm_status=status, body=body))
    findings = check_conformance(out_concepts, published=True) + link_findings
    return findings, stats



# ─────────────────────────────────────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────────────────────────────────────


def run(root: Path, out: Path, only: str | None, dry_run: bool,
        strict: bool) -> int:
    junk = scan_root_junk(root)

    if only == "conformance":
        # 작성본 기준 베이스라인 측정(Phase 1).
        concepts, _ = discover(root)
        findings = check_conformance(concepts)
        report = render_report(findings, junk, total_files=len(concepts))
        if dry_run:
            print(report)
            print(f"[okf] (dry-run) 미리보기. --write 로 {out}/lint-report.md 생성.",
                  file=sys.stderr)
        else:
            out.mkdir(parents=True, exist_ok=True)
            (out / "lint-report.md").write_text(report, encoding="utf-8")
            print(f"[okf] 리포트 작성: {out / 'lint-report.md'}", file=sys.stderr)
    else:
        # 전체 PUBLISH 패스(Phase 2). 발행본 기준 conformance.
        findings, stats = publish_bundle(root, out, dry_run)
        report = render_report(findings, junk, total_files=stats["files"])
        if dry_run:
            print(report)
            print(f"[okf] (dry-run) 발행 미리보기 — {stats['files']}개 파일 예정. "
                  f"수리 {stats['repaired']} · log {stats['logs']} · index {stats['indexes']} · "
                  f"ambiguous {stats['ambiguous']} · unresolved {stats['unresolved']}. "
                  f"--write 로 {out} 생성.", file=sys.stderr)
        else:
            (out / "lint-report.md").write_text(report, encoding="utf-8")
            print(f"[okf] 발행: {out} ({stats['files']}개 파일). "
                  f"수리 {stats['repaired']} · log {stats['logs']} · index {stats['indexes']}. "
                  f"리포트: {out / 'lint-report.md'}", file=sys.stderr)

    errors = sum(1 for f in findings if f.severity == "ERROR")
    warns = sum(1 for f in findings if f.severity == "WARN")
    if errors > 0:
        print(f"[okf] 게이트 FAIL: ERROR {errors}건", file=sys.stderr)
        return 1
    if strict and warns > 0:
        print(f"[okf] --strict: WARN {warns}건으로 FAIL", file=sys.stderr)
        return 1
    print(f"[okf] 게이트 PASS (ERROR 0, WARN {warns})", file=sys.stderr)
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(
        prog="scripts.okf.publish",
        description="OKF PUBLISH — 옵시디언 작성본 → OKF conformant 번들 (Phase 1: conformance)",
    )
    ap.add_argument("--root", default=".", help="리포 루트(기본 현재 디렉터리)")
    ap.add_argument("--out", default="dist/okf", help="발행 출력 디렉터리")
    ap.add_argument("--dry-run", action="store_true", default=True,
                    help="기본값. 쓰지 않고 미리보기.")
    ap.add_argument("--write", dest="dry_run", action="store_false",
                    help="실제 쓰기 활성화.")
    ap.add_argument("--only", choices=["discover", "type", "frontmatter",
                    "index", "links", "log", "relations", "conformance"],
                    help="단일 단계만 실행.")
    ap.add_argument("--strict", action="store_true",
                    help="WARN 도 실패로 취급(CI 게이트).")
    args = ap.parse_args(argv)

    root = Path(args.root).resolve()
    out = (root / args.out) if not Path(args.out).is_absolute() else Path(args.out)
    return run(root, out, args.only, args.dry_run, args.strict)


if __name__ == "__main__":
    raise SystemExit(main())
