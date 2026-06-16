---
title: OKF Phase 0 — 인벤토리 & 가정 검증 결과
created: 2026-06-16
updated: 2026-06-16
type: Decision
status: growing
tags: [okf, phase0, inventory, conformance, decision]
aliases: [OKF Phase 0 Findings]
---

# OKF Phase 0 — 인벤토리 & 가정 검증 결과

> 근거 문서: `_ops/okf/OKF_BUILD_PLAN.md`(Phase 0), `_ops/okf/OKF_PUBLISH_PROTOCOL.md`.
> 목적: 코드 작성 전에 OKF 패키지의 가정을 **실제 리포(`foolpoet44/1st_brain`)**로 검증하고,
> 어긋난 부분을 기록한다. 측정 기준일: **2026-06-16**, 브랜치 `claude/kind-pascal-rooxuv`.

## Compiled Truth

csp-brain은 패키지 주장(~90% OKF)과 달리, **정본 지식이 사실상 `wiki/` 트리 + `projects/`에만 모여 있다.**
BUILD_PLAN 부록 A가 IN으로 분류한 루트 디렉터리 다수(`concepts/`, `people/`, `decisions/`,
`permanent/`, `moc/`)는 실제로는 **추출 덤프·슬라이드 이미지·빈 폴더**다. 따라서 패키지의
`TYPE_MAP`과 IN/OUT 경계는 **코드 착수 전에 보정**해야 한다(BUILD_PLAN의 ⚠ 지침 발동).

**핵심 결정 (AC0 충족):**

1. **정본 개념 디렉터리 = `wiki/concepts/`** (루트 `concepts/`는 대화 추출 덤프 → 피드스톡으로 OUT).
2. **정본 IN 번들 = `wiki/`(전체 하위) + `projects/`.** 그 외 루트 후보는 아래 §3 표대로 보정.
3. **`dist/okf/` 격리 = `.gitignore`에 `dist/` 추가** (별도 발행 브랜치 불필요. 근거 §8).
4. **가장 큰 기술 위험 = 위키링크 변환** (99%가 이름형, 전역 인덱스 의존, 한글·공백·괄호 이름).

> ⚠ **선결 조건**: 패키지 읽기 순서 1번인 `OKF_ADOPTION_SPEC.md`가 **미수령**이다
> (`_ops/okf/OKF_ADOPTION_SPEC.PLACEHOLDER.md` 참조). SPEC §3/§5/§6/§7/§8을 확보해
> 아래 보정 사항을 반영한 뒤 Phase 1 코드에 착수한다.

---

## 1. 번들 IN 디렉터리 .md 개수 + 프론트매터 보유율

| 디렉터리 | .md | frontmatter | 보유율 | 판단 |
| --- | ---: | ---: | ---: | --- |
| `wiki/` (전체) | 81 | 79 | **98%** | ✅ 정본. OKF 거의 충족 |
| `wiki/concepts/` | 43 | (wiki 집합) | 高 | ✅ 정본 개념 |
| `projects/` | 60 | 60 | **100%** | ✅ 정본 |
| `concepts/` (루트) | 234 | **0** | **0%** | ❌ 추출 덤프 → OUT (§3) |
| `people/` (루트) | 15 | 14 | 93% | ⚠ 대부분 슬라이드 이미지 변환본 → 필터/OUT (§6 아님, §1.1) |
| `references/` | 1 | 1 | 100% | ✅ 소량 IN |
| `research/` | 1 | 1 | 100% | ✅ 소량 IN |
| `analysis/` | 2 | 2 | 100% | ✅ 소량 IN |
| `decisions/` (루트) | 0 | — | — | ⛔ `.gitkeep`만. 빈 폴더 |
| `permanent/` (루트) | 0 | — | — | ⛔ `.gitkeep`만. 빈 폴더 |
| `moc/` (루트) | 0 | — | — | ⛔ `.gitkeep`만. 빈 폴더 (§6) |

> 비교 참고: OUT 디렉터리 `dev/`(927), `dev2/`(928), `sync/`(831), `sy/`(928), `syncs/`(929)가
> 전체 5,083개 .md의 대부분을 차지한다 — 명백한 동기화/배포 사본. IN 후보가 아니다.

### 1.1 루트 `people/` 정밀 진단

`people/`의 15개 .md 중 실제 인물 노트는 `people/CSP.md` 정도이고, 나머지는
`exg팀_소개_260115.pptx.md`, `슬라이드5.PNG.md`, `팀소개_메일붙여넣게/슬라이드1.JPG.md` 등
**pptx/이미지 변환 산출물**이다. `wiki/people/`(2개)이 정본 인물 노트.
→ `people/`에 `Person` type을 일괄 부여하면 슬라이드 이미지가 전부 오분류된다.
**보정**: 정본 인물 = `wiki/people/`. 루트 `people/`는 OUT(피드스톡) 또는 명시적 화이트리스트만 IN.

## 2. 기존 프론트매터 키 분포 (충돌 키 식별)

- `wiki/` 노트: CLAUDE.md 표준(`title, created, updated, type, status, tags, aliases`) 사용.
- `projects/` 노트: `type, status, tags, related_to` 사용. **`related_to: "[[opq-framework]]"`** 형태로
  단일 관계를 위키링크 문자열로 보유 → OKF `relations[]`(typed-edge)와 **스키마 불일치**. Phase 3에서 매핑 필요.
- 충돌 키: `status` 값이 두 방언 혼재 — wiki는 `seed|growing|mature|archived`(CLAUDE.md),
  패키지 문서는 이모지(`🔄`,`🔴`) 사용. **PUBLISH 시 `status` 정규화 규칙을 SPEC에 명시해야 함**.
- `type` 값 표기: 패키지는 PascalCase(`Concept`,`Project`,`Skill`), CLAUDE.md는 소문자
  (`concept`,`framework`,`tool`). → **대소문자 정규화 결정 필요**(SPEC §5 보정 대상).

## 3. concepts/ vs wiki/concepts/ 드리프트 → 정본 결정

- 루트 `concepts/` 첫 파일 헤더: `# Extracted Knowledge from Conv: <uuid>` + `**Date**: ...` + 추출 코드 블록.
  → **대화에서 기계 추출한 아카이브**다. 큐레이션된 개념 노트가 아니다.
- 이름 중복(루트 `concepts/` ∩ `wiki/concepts/`): `ax-internalization`, `data-sensing`,
  `knowledge-capitalization`, `vibe-coding`, `weak-signal-theory` (5건). wiki 버전이 프론트매터 보유 = **정본**.
- **결정**: 정본 개념 = `wiki/concepts/`. 루트 `concepts/`는 `raw/`·`inbox/`와 같은 **피드스톡(OUT)**.
  → BUILD_PLAN 부록 A에서 `concepts`를 IN으로 둔 행, PROTOCOL `TYPE_MAP`의 `("concepts","Concept")` 항목 **삭제/보정**.

### 3.1 IN/OUT 보정표 (Phase 0 확정본)

| 디렉터리 | 패키지 판정 | **Phase 0 확정** | 근거 |
| --- | --- | --- | --- |
| `wiki/**` | IN | **IN (정본)** | 프론트매터 98%, OKF 거의 충족 |
| `projects/**` | IN | **IN (정본)** | 프론트매터 100% |
| `references/`,`research/`,`analysis/` | IN | **IN (소량)** | 소량이나 큐레이션됨 |
| `concepts/` (루트) | IN | **OUT (피드스톡)** | 추출 덤프, 프론트매터 0% |
| `people/` (루트) | IN | **OUT/화이트리스트** | 슬라이드 이미지 오염 |
| `decisions/`,`permanent/`,`moc/` (루트) | IN | **무효 (빈 폴더)** | `.gitkeep`만 존재 |

## 4. 위키링크 표본 분석 (IN 후보 디렉터리 전수)

IN 후보(`wiki concepts people references projects research analysis`)에서 추출한 **253개** 표본:

| 형태 | 건수 | 비율 |
| --- | ---: | ---: |
| 이름형 `[[foo]]` | ~212 | **~84%** |
| 별칭형 `[[foo\|라벨]]` | 38 | ~15% |
| 경로형 `[[a/b/c]]` | 3 | ~1% |
| 임베드 `![[...]]` | 0 | 0% |

- **함의**: PROTOCOL §3.4의 "경로형/이름형 혼재"라는 전제와 달리, **거의 전부 이름형**이다.
  링크 변환은 전적으로 [0] 전역 파일명 인덱스에 의존 → `ambiguous-link`/`unresolved-link`가 대량 발생할 위험.
- **충돌 위험 이름 패턴**: `[[Dream Cycle (주간 정리 루틴)]]`, `[[Context Restore (세션 복원)]]` 등
  **한글·공백·괄호 포함 표시명**과 `[[memory-save]]` 같은 **slug형**이 같은 대상을 가리키며 혼재
  (예: `[[Memory Save (대화 종료 기록)]]` vs `[[memory-save]]`). → 파일명 인덱스에 **별칭(aliases)·표시명까지 색인**해야 해석률이 오른다.
- **보정**: SPEC §7 / PROTOCOL §3.4에 (a) frontmatter `aliases` 기반 보조 인덱스, (b) slug 정규화
  (공백→`-`, 소문자화, 괄호 주석 제거) 규칙 추가 권고. 미해석은 `unresolved-link`(INFO)로 허용.

## 5. `_index` 파일 위치·확장자 분포

- 8개 전부 `wiki/<subdir>/_index.md` (확장자 `.md` 일관):
  `skills, projects, concepts, signals, tools, decisions, frameworks, people`.
- **비정형 없음**: 확장자 없는 `_index`는 발견되지 않음. → PROTOCOL §3.3 `rename_index`는
  `_index.md → index.md` 한 케이스만 처리하면 충분(추가 분기 불필요).

## 6. `moc/` 콘텐츠 성격 판정

- 루트 `moc/`는 **`.gitkeep`만 있는 빈 디렉터리**(.md 0개). → "색인 vs 독립 개념" 판단 자체가 무의미.
- PROTOCOL §3.3의 "moc 흡수 검토" 단계는 **현 리포에서 no-op**. (향후 `moc/`가 채워지면 재평가.)

## 7. `weekly/` · `projects/*/Timeline` 포맷 → log.md 매핑 규칙 초안

### 7.1 weekly/
- 정본: `2026-W16.md`, `2026-W17.md` (ISO 주차). 헤더 `# Weekly — 2026-W17 (2026-04-20 ~ 2026-04-26)`,
  섹션 `## 이번 주 핵심 활동`, `## 주요 결정사항`(표).
- 정크 혼재: `*.docx.md`, `*.pptx.md`, `*.xlsx.md` (양식·보고서 변환본) → **OUT**.
- **매핑 초안**: ISO 주차 파일만 입력으로. 주차 → 시작일(`YYYY-MM-DD`)로 변환해 `log.md`의 날짜 헤딩 생성.
  `## 이번 주 핵심 활동` 항목 → `* **Update**: ...`.

### 7.2 projects/*/Timeline
- 실제 포맷: `## 3. 타임라인` 아래 `### 2026-05-16`, `### 2026-05-31 (Planned)` 형태(ISO + 선택적 `(Planned)` 접미).
  하위 불릿 `- **심리 진단 모델 통합**: ...`.
- CLAUDE.md가 규정한 `## Timeline` 헤딩과 **실제 헤딩(`## 3. 타임라인`)이 드리프트**. → 파서는 헤딩 텍스트가 아니라
  `### <ISO-date>` 패턴으로 시계열 블록을 인식해야 함.
- **매핑 초안**: `### YYYY-MM-DD[ (Planned)]` → `log.md`의 `## YYYY-MM-DD`. `(Planned)`는 항목 라벨로 보존
  (`* **Planned**: ...`). 하위 불릿 → `* **Update**: ...`.

## 8. `dist/okf/` 격리 방식 결정

- 현 `.gitignore`는 `*.json`(일부 예외), `raw/archive/**`, `scripts/venv/` 등을 제외하나 **`dist/` 항목 없음**.
- `_config.yml`(Jekyll) 발행이 존재 → 발행 산출물이 소스 트리에 섞이는 것을 이미 경계하는 구조.
- **결정**: **`.gitignore`에 `dist/` 추가**(별도 `okf-dist` 브랜치 대신). 이유: (a) 발행본은 멱등 재생성 가능한
  파생물이라 버전 관리 불필요, (b) 브랜치 분리는 운영 복잡도만 키움, (c) 필요 시 CI에서 `dist/okf/`를
  아티팩트로 업로드하면 충분. → Phase 1 첫 작업으로 `.gitignore` 한 줄 추가.

---

## SPEC 보정 필요 목록 (코드 착수 전 반영)

1. **§3 IN/OUT**: 루트 `concepts/`(추출 덤프)·`people/`(슬라이드)·빈 폴더 3종을 IN에서 제거. 정본 = `wiki/**` + `projects/**` (+소량 references/research/analysis).
2. **§5 TYPE_MAP**: 루트 `concepts`,`decisions`,`people` prefix 항목 삭제/보정. `type` 대소문자 정규화 규칙 명시(PascalCase vs lower).
3. **§5/스키마**: `status` 이모지 ↔ 단어 방언 정규화 규칙 추가.
4. **§7 wikilink**: 이름형 84% 현실 반영 — `aliases` 보조 인덱스 + slug 정규화(공백/괄호/대소문자) 규칙 추가.
5. **§6.4 relations**: `projects/`의 `related_to` 단일 위키링크 → OKF `relations[]` 매핑 규칙(Phase 3).
6. **PROTOCOL §3.5**: Timeline 인식은 헤딩 텍스트가 아니라 `### <ISO-date>` 패턴 기반. `(Planned)` 접미 처리.

## 수용 기준(AC0) 체크

- [x] 8개 인벤토리 항목 결론 기재 (§1~§8).
- [x] SPEC §3/§5/§7 수정 필요분 명시 (위 보정 목록).
- [x] 정본 디렉터리 1개로 결정: **`wiki/`(+`projects/`)**, 개념 정본 = `wiki/concepts/`.

## 다음 단계 (사람 확인 대기)

1. `OKF_ADOPTION_SPEC.md` 원본 확보 → 위 6개 보정 반영.
2. 보정안 사람 승인 후 Phase 1 착수(`scripts/okf/` 스캐폴드 + LINT 베이스라인 + `.gitignore`에 `dist/`).
3. 코드는 아직 작성하지 않음 — BUILD_PLAN Phase 0 종료 지점에서 정지.

---

## Timeline

### 2026-06-16

- OKF Adoption Package 3종(README/PUBLISH_PROTOCOL/BUILD_PLAN)을 `_ops/okf/`에 보존.
- 실제 리포 인벤토리로 Phase 0 수행. 핵심 발견: 루트 `concepts/`는 추출 덤프(프론트매터 0%),
  정본 지식은 `wiki/`(98%)+`projects/`(100%)에 집중. 위키링크 84%가 이름형.
- `OKF_ADOPTION_SPEC.md` 미수령 확인 → 자리표시자 생성, 보정 목록 6건 도출.
- 관련 위키 개념: [[vibe-coding]], [[knowledge-capitalization]] (csp-brain 지식 자본화 맥락).
