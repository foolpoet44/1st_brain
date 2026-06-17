# scripts/okf — OKF PUBLISH 프로토콜

옵시디언 작성본을 OKF v0.1 conformant 번들로 발행하는 7번째 프로토콜 구현.

- 설계 정본: `_ops/okf/OKF_ADOPTION_SPEC.md`
- 실행 사양: `_ops/okf/OKF_PUBLISH_PROTOCOL.md`
- 빌드 순서: `_ops/okf/OKF_BUILD_PLAN.md`
- Phase 0 검증: `_ops/okf-phase0-findings.md`

## 안전 원칙

1. **작성본 비파괴** — 번들 IN 원본은 절대 수정하지 않는다. 출력은 `--out`(기본 `dist/okf/`)으로만.
2. **기본 dry-run** — 실제 쓰기는 `--write` 명시. `dist/`는 `.gitignore` 대상(멱등 재생성 가능 파생물).
3. **파괴적 변경(파일 이동/삭제)은 사람 확인 후** — 루트 정크 격리는 리포트에 큐로만 남긴다.

## 사용법

```bash
# conformance 미리보기 (기본 dry-run, 쓰지 않음)
python -m scripts.okf.publish --only conformance

# 베이스라인 리포트 작성 → dist/okf/lint-report.md
python -m scripts.okf.publish --only conformance --write

# CI 게이트 (WARN 도 실패로)
python -m scripts.okf.publish --only conformance --write --strict

# 단위 테스트
python -m unittest scripts.okf.test_publish -v
```

## 구현 현황 (Phase 1 + 2)

| 단계 | 함수 | 상태 |
| --- | --- | --- |
| [0] discover | `discover` | ✅ 번들 IN 스캔 + 전역 파일명 인덱스 |
| [1] derive_type | `derive_type` / `normalize_type` | ✅ §5+§11 보정 반영 |
| [2] frontmatter | `ensure_frontmatter` / `repair_frontmatter_text` | ✅ 비파괴 병합 + malformed YAML 수리 |
| [3] index | `rename_index` / `build_index_md` | ✅ `_index`→`index.md`, 루트 okf_version |
| [4] links | `convert_wikilinks` / `build_link_index` | ✅ slug·aliases 인덱스, 충돌/미해석 처리 |
| [5] log | `extract_timeline_entries` / `generate_log` | ✅ projects Timeline → log.md |
| [7] conformance | `check_conformance` / `render_report` | ✅ SPEC §8 검사 |
| 발행 통합 | `publish_bundle` | ✅ dist/okf 전체 발행 (멱등) |
| 정크 격리 큐 | `scan_root_junk` | ✅ (실행: 11건 inbox/raw/ 이관 완료) |
| [6] relations | — | ⏸️ Phase 3 (typed-edge) |

## 발행 (Phase 2)

```bash
python -m scripts.okf.publish              # 전체 발행 미리보기 (dry-run)
python -m scripts.okf.publish --write       # dist/okf/ 번들 발행
```

현재 베이스라인: **PASS ✅ (ERROR 0 · WARN 38 · INFO 18)**, 153개 파일.
malformed `related_to` 18건 수리, log.md 7개·index.md 8개 생성, 위키링크 67건 변환.
남은 WARN/INFO: 이름 충돌 17 + type-conflict 21 + 미해석 링크 18(사람이 명시 경로로 보강).

## 번들 IN (Phase 0 확정본)

`wiki/`, `projects/`, `references/`, `research/`, `analysis/`.
루트 `concepts/`(추출 덤프)·`people/`(슬라이드 이미지)·빈 폴더는 제외(§11 보정 1).

## LINT 검사 코드

| 코드 | severity | 의미 |
| --- | --- | --- |
| `missing-frontmatter` | ERROR | `---` 블록 없음 |
| `malformed-frontmatter` | ERROR | 블록은 있으나 YAML 파싱 실패(예: `related_to` 다중 위키링크) |
| `missing-type` | ERROR | `type` 누락/빈값 |
| `bad-index` | ERROR | `index.md`에 프론트매터 존재 |
| `type-conflict` | WARN | 기존 type ≠ 유도 type |
| `type-fallback` | WARN | prefix 매칭 실패 → fallback |
| `legacy-dialect` | WARN | `_index`/`[[wikilink]]` 잔존 |
| `root-junk` | WARN | 루트 정크 파일 |
| `unresolved-link` | INFO | 이름형 링크 미해석(허용) |
| `relation-target-missing` | INFO | relations target 미존재(허용) |
