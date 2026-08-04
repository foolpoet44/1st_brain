#!/usr/bin/env python3
"""
위키링크 정리 — 자동 링커가 만든 파손과 오탐을 걷어낸다 (2026-08-04)

왜 필요한가
-----------
커맨드센터 첫 실행에서 "해결되지 않는 링크 79종 / 172회"가 잡혔다. 조사해보니
세 유형이 섞여 있었다.

  A. 일반어 오탐    — SKILL, SOUL, CLAUDE, AGENTS 같은 단어에 링크가 걸림
  B. 이름 불일치    — [[EX Intelligence]] 인데 실제 문서는 ex-intelligence.md
  C. 경로형·중첩 파손 — [[Understand-Anything/.../gin.md|gin]] 이 링크 안에 중첩 삽입됨

C 가 특히 심각하다. 자동 링커가 이미 링크인 구간에 또 링크를 삽입해
`[[X[[Y|Z]]` 같은 중첩 파손을 만들었다. 문서 제목이 통째로 깨진 사례도 있다.

연결이 아니라 착각
------------------
깨진 링크는 밀도 지표를 부풀린다. 커맨드센터가 "문서당 링크 3.4개"라고 말할 때
그중 172회가 아무 데도 닿지 않는다면, 그 숫자는 지능의 증거가 아니라 노이즈다.
CLAUDE.md 가 말하는 "연결의 밀도"는 실제로 이어진 것만 세야 의미가 있다.

사용
----
  python3 scripts/fix_wikilinks.py --dry    # 무엇이 바뀔지만 출력
  python3 scripts/fix_wikilinks.py          # 실제 적용
"""

import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"

# A. 링크를 걸면 안 되는 일반어·파일명. 문서가 아니라 단어다.
GENERIC = {
    "SKILL", "SOUL", "CLAUDE", "AGENTS", "README", "AI", "BRIDGE",
    "HR", "DESIGN", "AIHR", "HR-AX", "RESOLVER", "KNOWLEDGE_PULSE",
    "INDEX_SUMMARY", "GUIDE", "NOTE",
}

# 중첩 파손: [[...[[대상|표시]]  → 안쪽 표시 텍스트만 남긴다.
#   원래 문장이 무엇이었는지는 복원할 수 없다. 링커가 덮어썼기 때문이다.
NESTED = re.compile(r"\[\[[^\[\]]*?\[\[([^\]|]*?)\|([^\]]*?)\]\]")
# 경로형: [[a/b/c.md|표시]] 또는 [[a/b/c|표시]]
PATHLINK = re.compile(r"\[\[([^\]|]*/[^\]|]*?)(?:\.md)?\|([^\]]*?)\]\]")
# 일반 링크: [[대상]] 또는 [[대상|표시]]
PLAIN = re.compile(r"\[\[([^\]|/]+?)(?:\|([^\]]*?))?\]\]")


def wiki_stems():
    return {p.stem: p for p in WIKI.rglob("*.md")}


def slugify(name):
    """표시명을 파일 슬러그 후보로 바꾼다. 'EX Intelligence' → 'ex-intelligence'"""
    s = name.strip().lower()
    s = re.sub(r"\([^)]*\)", "", s)          # 괄호 주석 제거: 'LMX (설명)' → 'LMX'
    s = re.sub(r"[:：].*$", "", s)            # 콜론 뒤 제거: 'Layer 1: COMPASS' → 'Layer 1'
    s = re.sub(r"[^\w가-힣\s-]", "", s)
    s = re.sub(r"\s+", "-", s.strip())
    return s


def fix_text(text, stems, stats):
    # 1) 중첩 파손 — 가장 먼저 푼다. 남겨두면 아래 정규식이 오작동한다.
    def _nested(m):
        stats["nested"] += 1
        return m.group(2)
    prev = None
    while prev != text:                       # 삼중 중첩까지 대비해 수렴할 때까지
        prev = text
        text = NESTED.sub(_nested, text)

    # 2) 경로형 링크 — 대상이 위키 문서면 슬러그 링크로, 아니면 링크 해제
    def _path(m):
        target, display = m.group(1), m.group(2)
        stem = target.split("/")[-1]
        if stem in stems:
            stats["path_fixed"] += 1
            return f"[[{stem}]]"
        stats["path_unlinked"] += 1
        return display
    text = PATHLINK.sub(_path, text)

    # 3) 일반 링크 — 일반어는 해제, 이름만 다른 실재 문서는 교정
    def _plain(m):
        target = m.group(1).strip()
        display = m.group(2)
        if target in stems:
            return m.group(0)                 # 정상 링크는 손대지 않는다
        if target in GENERIC or (len(target) <= 3 and target.isupper()):
            stats["generic"] += 1
            return display or target
        cand = slugify(target)
        if cand in stems:
            stats["renamed"] += 1
            return f"[[{cand}|{display or target}]]"
        # 실재하지 않지만 개념으로 보이는 것은 남긴다 — 앞으로 만들 문서의 좌표다
        stats["kept"] += 1
        return m.group(0)
    return PLAIN.sub(_plain, text)


def residue(text):
    """처리 후에도 남은 링크 문법 잔해를 센다.

    자동 링커는 링크를 '삽입'한 게 아니라 원문 문자열을 '덮어썼다'.
    'Compiled Truth' → 'Compiled T[[...|ru]]th' 처럼 표시 텍스트가 원문 조각인
    경우는 링크만 풀면 완전히 복구된다. 그러나 '매칭(matching)' → '([[...|SKILL]]ching)'
    처럼 원문 'mat' 이 SKILL 로 대체된 경우는 복구할 방법이 없다.

    복구 불가 지점을 자동으로 건드리면 손상 위에 손상을 더한다. 잔해가 남으면
    그 파일은 원본 그대로 두고 사람이 볼 목록으로 넘긴다."""
    return len(re.findall(r"\[\[|\]\]|[^\s(]+\.md\|", text))


def main():
    dry = "--dry" in sys.argv
    stems = wiki_stems()
    stats = Counter()
    changed, manual = [], []

    for p in sorted(WIKI.rglob("*.md")):
        orig = p.read_text(encoding="utf-8", errors="ignore")
        probe = Counter()
        new = fix_text(orig, stems, probe)
        if new == orig:
            continue

        # 처리 후에도 잔해가 남으면 복구 실패다. 손상 위에 손상을 더하지 않는다.
        #   판정 1: 링크 괄호 불균형 — [[ 와 ]] 개수가 다르면 구조가 깨진 것
        #   판정 2: 본문에 'xxx.md|' 가 남아 있으면 링크 문법이 텍스트로 새어나온 것
        if new.count("[[") != new.count("]]") or ".md|" in new:
            manual.append(p.relative_to(ROOT))
            continue

        stats.update(probe)
        changed.append(p.relative_to(ROOT))
        if not dry:
            p.write_text(new, encoding="utf-8")

    print(f"{'[DRY RUN] ' if dry else ''}처리 파일 {len(changed)}개")
    print(f"  중첩 파손 해제 : {stats['nested']}")
    print(f"  경로형 → 슬러그: {stats['path_fixed']}")
    print(f"  경로형 링크해제 : {stats['path_unlinked']}")
    print(f"  일반어 링크해제 : {stats['generic']}")
    print(f"  이름 교정       : {stats['renamed']}")
    print(f"  유지(생성 후보) : {stats['kept']}")
    if manual:
        print(f"\n⚠️  자동 복구 불가 {len(manual)}개 — 원문이 링커에 덮어써져 손대지 않음")
        for m in manual:
            print(f"  {m}")
    if changed:
        print(f"\n처리한 파일(상위 12):")
        for c in changed[:12]:
            print(f"  {c}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
