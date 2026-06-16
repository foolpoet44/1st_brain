---
type: Skill
title: OKF PUBLISH Protocol — csp-brain
description: 옵시디언 작성본을 OKF-conformant 번들로 발행하는 7번째 프로토콜의 실행 사양과 참조 구현.
tags: [okf, protocol, publish, lint, python]
timestamp: 2026-06-16T00:00:00Z
status: 🔄
---
# OKF PUBLISH Protocol — csp-brain
> 정본 설계는 `OKF_ADOPTION_SPEC.md`. 이 문서는 **PUBLISH 패스가 정확히 무엇을 어떻게 하는지**를 규정한다.
> Claude Code는 이 사양을 `scripts/okf/` 아래 구현한다. **작성본 비파괴, `dist/okf/`로만 출력.**
## 1. 개요
| 항목 | 값 |
| --- | --- |
| Trigger | `publish` (기존 6 프로토콜 트리거 관례 계승) |
| 입력 | 번들 IN 디렉터리(SPEC §3.1)의 옵시디언 작성본 |
| 출력 | `dist/okf/` 아래 OKF-conformant 번들 + `lint-report.md` |
| 안전 | 멱등(idempotent), 작성본 read-only, 기본 `--dry-run` |
## 2. 파이프라인 (단계 순서 고정)
```
[0] discover      번들 IN 스캔 → ConceptFile 목록 + 전역 파일명 인덱스 구성
[1] derive_type   경로 → type 유도(SPEC §5). 실패 시 fallback + 경고
[2] frontmatter   프론트매터 보강(없으면 생성, 있으면 병합·비파괴)
[3] index         _index(.md) → index.md, moc/ 흡수 검토, 루트 index.md에 okf_version
[4] links         [[wikilink]] → bundle-relative 링크(SPEC §7)
[5] log           weekly/ · Timeline → 디렉터리별 log.md (ISO 날짜)
[6] relations     본문 링크 ↔ frontmatter relations 동기화(typed-edge profile)
[7] conformance   LINT 검사(§4) → dist/okf/lint-report.md
```
각 단계는 순수 함수로 분리하고, `--only <stage>`로 단독 실행 가능하게 한다(테스트 용이성).
## 3. 변환 규칙 (정밀)
### 3.1 derive_type
- SPEC §5 prefix 매칭. 가장 긴 prefix 우선.
- 매칭 실패 → `type: Concept` + `lint: type-fallback` 플래그.
### 3.2 frontmatter 병합 (비파괴)
- 기존 프론트매터가 있으면 **기존 값 우선**, 누락 키만 채운다.
- `type`이 이미 있고 유도값과 다르면 **기존 값 유지** + 경고(사람이 판단).
- `timestamp` 없으면 git 마지막 커밋 시각으로 채운다(`git log -1 --format=%cI <file>`).
### 3.3 index 변환
- `_index` 또는 `_index.md` → 같은 디렉터리에 `index.md` 생성.
- `index.md`는 OKF §6 규칙상 **프론트매터 없음**(예외: 번들 루트 `index.md`에 `okf_version: "0.1"`만 허용).
- 내용: 디렉터리 항목을 `* [title](relative-url) - description` 형식으로. description은 대상 노트 프론트매터에서 가져온다.
- `moc/` 항목이 디렉터리 색인 성격이면 해당 `index.md`로 병합, 독립 개념이면 concept으로 둔다(Phase 0 판단 결과 반영).
### 3.4 wikilink 변환 (가장 주의)
옵시디언 위키링크는 두 형태가 섞여 있다:
```
경로형:  [[wiki/concepts/foo/_index|개념]]   → [개념](/wiki/concepts/foo/index.md)
이름형:  [[foo]]                              → [foo](/<resolved path>/foo.md)
별칭형:  [[foo|보이는 라벨]]                    → [보이는 라벨](/<resolved>/foo.md)
임베드:  ![[foo.png]]                          → ![foo](/<resolved>/foo.png) (자산 경로 보존)
```
해석 규칙:
1. target에 `/`가 있으면 **경로형**으로 직접 매핑(+ `_index`→`index`).
2. `/`가 없으면 **이름형** — [0]에서 만든 전역 파일명 인덱스로 경로 해석.
3. 이름이 vault에 둘 이상이면(충돌) 변환하지 않고 `lint: ambiguous-link`로 기록(사람이 명시 경로로 수정).
4. 해석 실패 → 변환하지 않고 placeholder 보존 + `lint: unresolved-link`.
5. heading anchor(`[[foo#섹션]]`)는 `/path/foo.md#섹션`으로 보존.
### 3.5 log.md 생성
- 입력: `weekly/`, `projects/*/Timeline` 등 시계열 소스(Phase 0에서 확정).
- 출력: 해당 scope 디렉터리에 `log.md`, OKF §7 형식.
```
# Directory Update Log
## 2026-06-16
* **Update**: ...
* **Creation**: ...
```
- 날짜 헤딩은 ISO `YYYY-MM-DD` 강제. `2605.md` 같은 비정형은 파싱 시도 후 실패하면 LINT 격리.
### 3.6 relations 동기화
- 본문에 typed 관계를 나타내는 링크가 있으나 frontmatter `relations`에 없으면 보강(또는 역으로).
- 관계 타입 추론은 자동화하지 않는다(오분류 위험). 대신: frontmatter `relations`를 **정본**으로 보고, 본문에 대응 마크다운 링크가 없으면 LINT 경고만 낸다. 관계 타입 입력은 사람이 한다.
## 4. LINT = Conformance Checker 사양
SPEC §8 기준을 검사한다. 출력은 `dist/okf/lint-report.md`.
### 4.1 검사 항목 (severity)
| 코드 | severity | 조건 |
| --- | --- | --- |
| `missing-frontmatter` | ERROR | 번들 IN .md에 프론트매터 블록 없음/파싱 실패 |
| `missing-type` | ERROR | `type` 누락 또는 빈 값 |
| `bad-index` | ERROR | `index.md`에 (루트 제외) 프론트매터 존재 |
| `type-fallback` | WARN | 경로 매칭 실패로 fallback type 부여 |
| `type-conflict` | WARN | 기존 type ≠ 유도 type |
| `ambiguous-link` | WARN | 이름형 위키링크 충돌 |
| `unresolved-link` | INFO | 해석 실패(= 아직 안 쓴 지식, 허용) |
| `legacy-dialect` | WARN | 발행본에 `_index`/`[[ ]]`/비정형 날짜 잔존 |
| `relation-target-missing` | INFO | `relations[].target` 미존재(허용) |
### 4.2 게이트 기준
- **PASS**: ERROR 0건.
- WARN/INFO는 리포트에 집계하되 빌드를 막지 않는다.
- `--strict`: WARN도 실패로 취급(CI용).
### 4.3 리포트 포맷
- 상단 요약 표(코드별 건수), 이어서 파일별 상세(경로 + 코드 + 라인).
- `_ops/` 또는 `dist/okf/`에 타임스탬프로 누적(트렌드 추적).
## 5. 참조 구현 스켈레톤
> 의존성 최소화: 표준 라이브러리 + `PyYAML`만. 실제 구현 시 함수별 단위 테스트 우선(harness/ 활용).
```python
# scripts/okf/publish.py  (skeleton — Claude Code가 채운다)
from __future__ import annotations
import argparse, re, subprocess
from dataclasses import dataclass, field
from pathlib import Path
import yaml
BUNDLE_IN = ["wiki", "concepts", "decisions", "people", "references",
             "permanent", "projects", "research", "analysis", "moc"]
TYPE_MAP = [  # (prefix, type) — 긴 prefix 우선 정렬
    ("wiki/concepts", "Concept"), ("wiki/tools", "Tool"),
    ("wiki/frameworks", "Framework"), ("wiki/skills", "Skill"),
    ("wiki/decisions", "Decision"), ("concepts", "Concept"),
    ("decisions", "Decision"), ("people", "Person"),
    ("references", "Reference"), ("projects", "Project"),
    ("research", "Research"), ("analysis", "Analysis"),
    ("permanent", "Note"),
]
WIKILINK = re.compile(r"!?\[\[([^\]|#]+)(#[^\]|]+)?(?:\|([^\]]+))?\]\]")
@dataclass
class Concept:
    src: Path                 # 작성본 경로
    rel: str                  # 번들 상대 경로 (예: wiki/concepts/foo.md)
    frontmatter: dict = field(default_factory=dict)
    body: str = ""
    lint: list[str] = field(default_factory=list)
def discover(root: Path) -> tuple[list[Concept], dict[str, str]]:
    """번들 IN 스캔. (Concept 목록, 파일명→상대경로 인덱스) 반환."""
    ...
def derive_type(rel: str) -> tuple[str, bool]:
    """경로 prefix → type. (type, is_fallback)."""
    for prefix, t in sorted(TYPE_MAP, key=lambda x: -len(x[0])):
        if rel.startswith(prefix + "/") or rel == prefix:
            return t, False
    return "Concept", True
def ensure_frontmatter(c: Concept) -> None:
    """비파괴 병합. 누락 키만 채움. timestamp는 git에서."""
    t, fallback = derive_type(c.rel)
    c.frontmatter.setdefault("type", t)
    if fallback: c.lint.append("type-fallback")
    if "timestamp" not in c.frontmatter:
        c.frontmatter["timestamp"] = git_last_commit_iso(c.src)
    ...
def convert_wikilinks(body: str, name_index: dict[str, str]) -> tuple[str, list[str]]:
    """[[...]] → bundle-relative markdown link. (변환본, lint 코드들)."""
    ...
def rename_index(rel: str) -> str:
    return rel.replace("_index.md", "index.md").replace("/_index", "/index")
def generate_log(scope_dir: Path, sources: list[Path]) -> str:
    """weekly/Timeline → OKF §7 log.md 텍스트."""
    ...
def check_conformance(out_root: Path) -> "Report":
    """SPEC §8 검사 → lint-report.md."""
    ...
def git_last_commit_iso(p: Path) -> str:
    return subprocess.run(["git","log","-1","--format=%cI",str(p)],
                          capture_output=True, text=True).stdout.strip()
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="dist/okf")
    ap.add_argument("--dry-run", action="store_true", default=True)
    ap.add_argument("--write", dest="dry_run", action="store_false")
    ap.add_argument("--only", choices=["discover","type","frontmatter",
                    "index","links","log","relations","conformance"])
    ap.add_argument("--strict", action="store_true")
    args = ap.parse_args()
    # 파이프라인 [0]..[7] 순서 실행. dry-run이면 stdout diff만.
    ...
if __name__ == "__main__":
    main()
```
## 6. 안전·멱등성 규칙
1. 작성본(번들 IN 원본)은 **절대 수정 금지**. 모든 출력은 `dist/okf/`.
2. 기본 `--dry-run`. 실제 쓰기는 `--write` 명시.
3. 멱등: 같은 입력 → 같은 출력. 재실행이 누적 손상 없음.
4. `dist/okf/`는 `.gitignore` 또는 별도 발행 브랜치(`okf-dist`)로 분리(BUILD_PLAN Phase 0 결정).
5. 모든 변환은 git 커밋된 상태에서 실행(롤백 가능).
## 7. CLI 요약
```
python -m scripts.okf.publish --dry-run            # 기본: diff 미리보기
python -m scripts.okf.publish --write --out dist/okf
python -m scripts.okf.publish --only links --dry-run
python -m scripts.okf.publish --write --strict     # CI 게이트
```
