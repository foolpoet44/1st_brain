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


def check_conformance(concepts: list[Concept]) -> list[Finding]:
    """SPEC §8 기준으로 Concept 목록을 검사 → Finding 목록.

    Phase 1 에서는 작성본(번들 IN)을 대상으로 베이스라인을 측정한다.
    """
    findings: list[Finding] = []
    for c in concepts:
        name = Path(c.rel).name
        is_index = name in ("_index.md", "index.md")

        # 예약 파일: index 계열은 프론트매터 없어야 함(루트 index 예외는 Phase 2).
        if is_index:
            if c.has_frontmatter and name == "index.md":
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

        # 5. 레거시 방언: 본문 위키링크 잔존(발행본 기준 경고. 작성본 베이스라인).
        if WIKILINK_RE.search(c.body):
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
# Phase 2 스텁 (아직 미구현)
# ─────────────────────────────────────────────────────────────────────────────


def _phase2_not_implemented(stage: str):
    print(f"[okf] '{stage}' 단계는 Phase 2 범위입니다(미구현). "
          f"BUILD_PLAN Phase 2 참조.", file=sys.stderr)


def git_last_commit_iso(p: Path) -> str:
    try:
        out = subprocess.run(
            ["git", "log", "-1", "--format=%cI", str(p)],
            capture_output=True, text=True, check=False,
        )
        return out.stdout.strip()
    except OSError:
        return ""


# ─────────────────────────────────────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────────────────────────────────────


def run(root: Path, out: Path, only: str | None, dry_run: bool,
        strict: bool) -> int:
    concepts, name_index = discover(root)
    junk = scan_root_junk(root)

    # Phase 2 단계는 스텁.
    if only in ("frontmatter", "index", "links", "log", "relations"):
        _phase2_not_implemented(only)
        return 0

    findings = check_conformance(concepts)
    report = render_report(findings, junk, total_files=len(concepts))

    errors = sum(1 for f in findings if f.severity == "ERROR")
    warns = sum(1 for f in findings if f.severity == "WARN")

    if dry_run:
        print(report)
        print(f"[okf] (dry-run) 리포트를 쓰지 않음. --write 로 {out}/lint-report.md 생성.",
              file=sys.stderr)
    else:
        out.mkdir(parents=True, exist_ok=True)
        (out / "lint-report.md").write_text(report, encoding="utf-8")
        print(f"[okf] 리포트 작성: {out / 'lint-report.md'}", file=sys.stderr)

    # 게이트 판정
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
