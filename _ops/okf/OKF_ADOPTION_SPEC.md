---
type: Decision
title: OKF Adoption Spec — csp-brain
description: csp-brain(1st_brain)에 Open Knowledge Format v0.1을 적용하기 위한 정본(正本) 설계 명세.
tags: [okf, knowledge-management, architecture, csp-brain]
timestamp: 2026-06-16T00:00:00Z
status: 🔄
okf_target_version: "0.1"
---
# OKF Adoption Spec — csp-brain
> 이 문서는 **무엇을·왜** 바꾸는지를 정의하는 정본 설계서다.
> **어떻게 돌리는지**는 `OKF_PUBLISH_PROTOCOL.md`,
> **어떤 순서로 빌드하는지**는 `OKF_BUILD_PLAN.md`를 본다.
> Claude Code는 이 세 문서를 함께 읽고 빌드한다.

> 📌 **Phase 0 검증 반영본 (2026-06-16).** 본문은 저자 원본을 비파괴 보존한다.
> 실제 리포 인벤토리 검증 결과 어긋난 가정에는 `> ⚠ Phase 0 보정` 주석을 덧붙였고,
> 전체 보정 요약은 **§11**에 모았다. 근거: `_ops/okf-phase0-findings.md`.
## 0. 한 문장 요약
csp-brain은 이미 ~90% OKF다(markdown + git + 디렉터리 계층 + `references/` + Compiled Truth/Timeline 이분법). 갈아엎지 않는다. **번들 경계를 긋고(지식 서브트리만), 발행 프로토콜(PUBLISH) 하나를 추가해** 옵시디언 방언을 OKF-conformant 발행본으로 변환한다. 작성 경험은 옵시디언 네이티브로 보존한다.
## 1. 목적 (Goals)
1. csp-brain의 지식 서브트리를 **OKF v0.1 conformant 번들**로 발행 가능하게 만든다.
2. 옵시디언 작성 워크플로우(`[[wikilinks]]`, `_index`)를 **깨지 않는다**. 변환이 아니라 발행이다.
3. 외부 소비자(LLM 컨텍스트 로더, OKF 그래프 뷰어, Jekyll 정적 사이트)가 별도 어댑터 없이 번들을 읽게 한다.
4. 기존 6 프로토콜(INGEST/QUERY/LINT/DIGEST/BRIDGE/GENERATE)을 OKF로 날카롭게 벼린다.
5. 락인을 구조적으로 제거한다 — 어느 도구가 사라져도 지식은 OKF 마크다운으로 남는다.
## 2. 비범위 (Non-goals)
- 레포 전체를 OKF화하지 않는다. 코드/운영/서브모듈은 conformance 밖이다(§3).
- 옵시디언 플러그인 설정(`.obsidian`)이나 Jekyll 설정(`_config.yml`)을 바꾸지 않는다.
- 작성본(authoring source)을 파괴적으로 수정하지 않는다. 발행은 `dist/okf/`로만 나간다(§7).
- 새 RAG 인프라를 만들지 않는다. `ragapp/`는 OKF 번들의 소비자가 될 뿐, 이 스펙의 대상이 아니다.
## 3. 핵심 설계 결정 ① — 번들 경계
OKF 번들은 **레포 전체가 아니라 지식 서브트리**다. OKF 명세상 번들은 더 큰 레포 안의 하위 디렉터리로 배포될 수 있다.
### 3.1 번들 IN (conformance 대상)
| 디렉터리 | 비고 |
| --- | --- |
| `wiki/` | 6 카테고리 정식 위키. 번들의 중심. |
| `concepts/` | 루트 개념 — `wiki/concepts/`와의 중복 여부를 빌드 시 확인(§9 검증항목). |
| `decisions/` | 의사결정 이력. |
| `people/` | People Context Graph. |
| `references/` | OKF §8 인용 미러. 폴더명까지 일치. |
| `permanent/` | 영구 노트(Zettelkasten). |
| `projects/` | 프로젝트별 Compiled Truth + Timeline. |
| `research/` | 리서치 노트. |
| `analysis/` | 분석 노트. |
| `moc/` | Map of Content — `index.md` 후보(§6). |

> ⚠ **Phase 0 보정 (§3.1)**: 실측 결과 아래 행은 가정과 다르다.
> - `concepts/`(루트, 234개): 프론트매터 0%. 첫 줄이 `# Extracted Knowledge from Conv: <uuid>` — **대화 추출 덤프**다. 큐레이션 개념이 아니므로 **IN 제외 → 피드스톡(§3.2)**. 정본 개념 = `wiki/concepts/`(43개). 이름 중복 5건(`ax-internalization`,`data-sensing`,`knowledge-capitalization`,`vibe-coding`,`weak-signal-theory`)은 wiki 버전이 정본.
> - `people/`(루트, 15개): 대부분 pptx 슬라이드 이미지 변환본(`슬라이드5.PNG.md` 등). 정본 인물 = `wiki/people/`. **IN 제외 또는 명시 화이트리스트만 IN**.
> - `decisions/`,`permanent/`,`moc/`(루트): `.gitkeep`만 있는 **빈 폴더**. 정본은 `wiki/decisions/` 등. → IN 무효.
> - 확정 정본 IN 번들 = **`wiki/**` + `projects/**`** (+소량 `references/`·`research/`·`analysis/`).
### 3.2 번들 OUT (conformance 제외)
- **피드스톡(원료)**: `inbox/`, `raw/`, `Clippings/`, `Toss/`, `Atoms/` — 인간이 던지는 미정제 자료. INGEST가 이걸 번들 concept으로 정제한다.
- **코드/운영**: `_ops/`, `scripts/`, `ragapp/`, `harness/`, `dev/`, `dev2/`, `sync/`, `sy/`, `syncs/`.
- **에이전트/도구 설정**: `.claude/`, `.agents/`, `.github/`, `.obsidian/`, `.obsidian-1st_brain/`, `.understand-anything/`.
- **서브모듈**: `open-design@`, `Understand-Anything@`, `temp_skill@`.
- **산출물/공유**: `outputs/`, `sharing/`, `weekly/`, `thinklog/`, `syncs/` — 발행 대상이지 지식 소스가 아님. `weekly/`는 `log.md` 생성 입력으로만 사용(§6).
- **루트 정크**: `무제.md`, `이름 없는 보드.md`, `untitled-daily-*.md`, 비정형 데일리(`2605.md` 등) — LINT가 격리(§8, BUILD_PLAN Phase 1).

> ⚠ **Phase 0 보정 (§3.2)**: 위 피드스톡 목록에 **루트 `concepts/`(추출 덤프)** 와 **루트 `people/`(슬라이드 이미지)** 를 추가한다. `dev/`·`dev2/`·`sync/`·`sy/`·`syncs/`가 전체 5,083개 .md의 대부분(각 ~900개)을 차지하는 동기화 사본임을 실측 확인 — OUT 유지.
> 검증 필요: 위 분류는 디렉터리명 기반 추론이다. Claude Code는 BUILD_PLAN Phase 0에서 각 디렉터리 내용을 표본 확인해 IN/OUT을 최종 확정한다.

> ✅ **검증 완료 (2026-06-16)**: 위 "검증 필요" 항목은 Phase 0에서 수행됨. 결과는 위 §3.1/§3.2 보정 및 `_ops/okf-phase0-findings.md`.
## 4. 핵심 설계 결정 ② — 이중 방언(Dual-Dialect)
```
작성(authoring)        →   옵시디언 네이티브: [[wikilinks]], _index, .obsidian
        │
        ▼  PUBLISH 프로토콜 (7번째 프로토콜, 신규)
발행(publishing)       →   OKF-conformant: index.md, /bundle-relative links, type 프론트매터
        │
        ▼
소비(consumption)      →   viz.html · LLM context · Jekyll · Notion(BRIDGE)
```
원칙: **작성본은 비파괴 보존, OKF는 발행 산출물.** 변환은 PUBLISH 패스가 `dist/okf/`로만 수행한다. 이로써 옵시디언 ergonomics와 OKF 상호운용성을 동시에 갖는다.
## 5. Concept Type 매핑
OKF의 유일한 필수 필드는 `type`이다. csp-brain은 폴더가 곧 타입이므로 경로에서 유도한다.
| 경로 prefix | `type` 값 | 비고 |
| --- | --- | --- |
| `wiki/concepts/`, `concepts/` | `Concept` | |
| `wiki/tools/` | `Tool` | |
| `wiki/frameworks/` | `Framework` | |
| `wiki/skills/` | `Skill` | ESCON typed-edge 대상(§6.4). |
| `wiki/decisions/`, `decisions/` | `Decision` | `supersedes` 관계 대상. |
| `people/` | `Person` | People Context Graph 관계 대상. |
| `references/` | `Reference` | |
| `projects/` | `Project` | |
| `research/` | `Research` | |
| `analysis/` | `Analysis` | |
| `permanent/` | `Note` | 영구 노트. |
| `moc/` | (변환) | `index.md`로 흡수 검토(§6.1). |
| 그 외 매칭 실패 | `Concept` (fallback) + LINT 경고 | 수동 확인 큐. |
> OKF 규칙: type 값은 중앙 등록되지 않으며, 소비자는 미지의 type을 관대하게 처리해야 한다. 위 값은 자명성만 만족하면 된다.

### 5.1 정본 Type 어휘 (Controlled Vocabulary) — OKF 결함 ③에 대한 응답

OKF의 가장 깊은 결함은 **의미가 아니라 컨테이너만 표준화**한다는 점이다. `type`이 자유 형식이라
"BigQuery 테이블"·"테이블"·"관계형 자산"이 모두 유효하지만 서로 다른 언어가 된다. csp-brain은
"상자의 합의를 사용자에게 떠넘기지 않는다" — 아래를 **정본 어휘**로 고정한다. OKF의 관대함은
*외부 소비*에서만 유지하고, *내부 작성*에는 이 폐쇄 집합을 강제한다(`derive_type`/`normalize_type`).

```
Concept · Tool · Framework · Skill · Decision · Person ·
Signal · Protocol · Project · Reference · Research · Analysis
```

- 경로가 타입을 유도하므로(§5 표), 작성본의 `type`은 **경로 유도값과 일치**해야 한다. 불일치 시
  `type-conflict` WARN.
- `Note` 는 정본 어휘가 **아니다**. `permanent/`(번들 OUT)의 영구 노트에서만 의미를 가지며,
  번들 IN(`wiki/**`·`references/**` 등)에서 `type: Note` 는 막연한 레이블이므로 경로 유도값으로
  교정한다. 복수형/대소문자 방언(`people`→`Person` 등)은 `normalize_type`이 흡수한다.

> ⚠ **Phase 0 보정 (§5)**:
> - 루트 prefix `concepts/`·`decisions/`·`people/`·`permanent/`·`moc/`는 §3.1 보정으로 IN에서 빠지므로 TYPE_MAP에서 **제거**(또는 fallback 처리). 유효 매핑은 `wiki/*` prefix + `projects/`(+`references/`·`research/`·`analysis/`).
> - **type 대소문자 정규화 필요**: 본 SPEC은 PascalCase(`Concept`), CLAUDE.md는 소문자(`concept`)를 쓴다. PUBLISH는 기존 프론트매터 `type` 값을 PascalCase로 정규화하되, 충돌 시 §6.1 비파괴 병합 규칙을 따른다.
> - **`wiki/signals/`·`wiki/protocols/` 미정의**: 실제 wiki 하위에 `signals/`,`protocols/` 디렉터리가 존재하나 TYPE_MAP에 없다. → `Signal`,`Protocol` 추가 권고(자명성 충족).
## 6. Frontmatter 표준
### 6.1 필드
```yaml
---
type: <REQUIRED>                 # §5에서 유도
title: <권장>                     # 없으면 소비자가 파일명에서 유도
description: <권장>               # 한 문장 요약. index.md·검색 스니펫이 사용
resource: <선택>                  # 실제 자산의 canonical URI (추상 개념은 생략)
tags: [<tag>, ...]               # 선택
timestamp: <ISO 8601>            # 선택. 마지막 의미있는 변경 시각
# --- csp-brain 확장 (OKF 확장 키, conformant) ---
status: 💡 | 🔄 | ✅ | 📦         # userPreferences 아카이빙 규칙과 정렬
importance: ⭐ | ⭐⭐ | ⭐⭐⭐
relations:                       # typed edges (§6.4)
  - rel: <relation type>
    target: /<bundle-relative path>.md
---
```
- `status`/`importance`는 userPreferences의 Notion 아카이빙 규칙(중요도·상태)과 1:1 매핑되어 BRIDGE에서 그대로 흐른다.
- 확장 키는 OKF가 명시적으로 허용한다(소비자는 미지의 키를 거부하면 안 됨).

> ⚠ **Phase 0 보정 (§6.1)**: 기존 노트의 `status`가 **두 방언으로 혼재**한다 — wiki 노트는 CLAUDE.md 단어값(`seed|growing|mature|archived`), 본 SPEC/패키지는 이모지(`💡🔄✅📦`). PUBLISH는 단어↔이모지 정규화 매핑표를 두고 **발행본에서 한 방언으로 통일**해야 한다(작성본은 비파괴). `projects/` 노트는 `related_to: "[[opq-framework]]"`처럼 관계를 단일 위키링크 문자열로 보유 → §6.4 `relations[]`로의 매핑 규칙을 Phase 3에서 적용.
### 6.2 본문 관례 섹션
적용 가능할 때 OKF 관례 헤딩을 쓴다: `# Schema`, `# Examples`, `# Citations`(§8).
### 6.3 예약 파일
| 파일 | csp-brain 현재 | OKF | 처리 |
| --- | --- | --- | --- |
| 디렉터리 색인 | `_index` (옵시디언) | `index.md` | PUBLISH가 `_index(.md)` → `index.md` 사본 생성. `moc/` 콘텐츠도 해당 디렉터리 `index.md`로 흡수 검토. |
| 변경 이력 | `projects/*/Timeline`, `weekly/` | `log.md` | PUBLISH가 디렉터리별 `log.md`를 ISO 날짜 형식으로 생성. |
| 버전 선언 | 없음 | `okf_version: "0.1"` | 번들 루트 `index.md` 프론트매터에만 기입(OKF가 프론트매터를 허용하는 유일한 index). |

> ⚠ **Phase 0 보정 (§6.3)**: `_index`는 8개 전부 `wiki/<subdir>/_index.md`로 확장자 일관 — `rename_index`는 단일 케이스만 처리하면 충분. `moc/`는 빈 폴더라 "흡수 검토"는 현재 no-op. `projects/*` 타임라인은 헤딩이 `## Timeline`이 아니라 `## 3. 타임라인`이므로 파서는 헤딩 텍스트가 아닌 `### <ISO-date>` 패턴으로 인식해야 한다(`(Planned)` 접미 보존).
### 6.4 Relations Profile (typed edges)
OKF 기본 링크는 untyped다. csp-brain은 본문 마크다운 링크(그래프 뷰어가 즉시 소비) + 프론트매터 `relations`(타입 보존)를 **둘 다** 둔다.
| 도메인(type) | relation 어휘 |
| --- | --- |
| 공통 | `related_to`, `broader`, `narrower` |
| `Skill`/`Concept` | `prerequisite_of`, `co_required_with` |
| `Decision` | `supersedes`, `superseded_by`, `depends_on` |
| `Person` | `reports_to`, `mentors`, `collaborates_with` |
| `Project` | `part_of`, `produces` |
> 각 `relations[].target`은 §5 경로의 bundle-relative path. 대상이 아직 없으면 OKF 규칙상 깨진 링크가 아니라 "아직 안 쓴 지식"으로 허용한다.
## 7. 링크 규약
- **권장**: bundle-relative 절대 링크 `[label](/wiki/concepts/foo.md)` — 하위 디렉터리 이동에도 안정적.
- PUBLISH가 옵시디언 위키링크를 변환한다:
  - `[[wiki/concepts/foo/_index|개념]]` → `[개념](/wiki/concepts/foo/index.md)`
  - `[[foo]]`(이름 기반) → vault 전역 파일명 인덱스로 경로 해석 후 변환(PROTOCOL §3 참조).
- 미해석 위키링크는 깨진 링크 placeholder로 보존하고 LINT 리포트에 기록.

> ⚠ **Phase 0 보정 (§7)**: 실측 위키링크 253개 중 **84%가 이름형**(`[[foo]]`), 별칭형 15%, 경로형 1%, 임베드 0%. 변환이 전역 파일명 인덱스에 전적으로 의존하므로 충돌·미해석 위험이 가장 크다. 게다가 `[[Dream Cycle (주간 정리 루틴)]]`(한글·공백·괄호)과 `[[memory-save]]`(slug)가 같은 대상을 가리키며 혼재한다. → 인덱스에 **frontmatter `aliases`·표시명까지 색인**하고 **slug 정규화**(공백→`-`, 소문자화, 괄호 주석 제거)를 추가한다. 미해석은 `unresolved-link`(INFO)로 허용.
## 8. Conformance 기준
OKF §9 + csp-brain 추가 규칙. 번들이 conformant하려면:
1. 번들 IN(§3.1)의 모든 비예약 `.md`가 **파싱 가능한 YAML 프론트매터**를 가진다.
2. 모든 프론트매터에 **비어있지 않은 `type`**이 있다.
3. `index.md`/`log.md`가 존재할 때 OKF §6/§7 구조를 따른다.
4. (csp 추가) `relations[].target`은 bundle-relative path 형식이다(존재 보장은 안 함).
5. (csp 추가) 번들 IN에 `_index`·`[[wikilink]]`·미정형 날짜 파일명이 남아있지 않다(발행본 기준).
6. (csp 추가) 작성본 concept의 콘텐츠 최신 날짜(`updated` 또는 마지막 Timeline 날짜)가 6주(기본
   `STALE_WEEKS`) 이내다 — OKF 결함 ①(드리프트)에 대한 측정 가능한 게이트. 초과 시
   `stale-compiled-truth` WARN. git timestamp는 신선도 신호에서 제외(파일 이동에도 갱신되므로).
연성 규칙(소비자가 거부하면 안 됨): 선택 필드 누락, 미지 type, 미지 확장 키, 깨진 링크, `index.md` 부재.
## 9. 6 프로토콜과의 관계
| 프로토콜 | OKF로 벼려지는 방식 |
| --- | --- |
| INGEST | 피드스톡(§3.2) → 번들 IN concept. type 부여가 INGEST 출력 규약이 됨. |
| QUERY | bundle-relative 링크 그래프를 순회 가능 → 답변 근거 추적 향상. |
| LINT | §8 conformance checker로 승격. 모호한 "자가 점검" → 측정 가능한 게이트. |
| DIGEST | `weekly/` → `log.md` 생성 입력. |
| BRIDGE | OKF를 Obsidian↔Notion 교환 포맷으로. status/importance가 그대로 매핑. |
| GENERATE | 발행 산출에 `viz.html`(Cytoscape 그래프) 추가. |
| **PUBLISH (신규)** | §4 발행 패스. `dist/okf/` 산출. PROTOCOL 문서가 상세. |
## 10. 가정 & 검증 필요 항목 (Claude Code가 Phase 0에서 확인)
- [x] 번들 IN 노트들에 이미 프론트매터가 있는가? 있다면 기존 키와 충돌하는가? → wiki 98%/projects 100% 보유. `status` 방언 충돌·`related_to` 스키마 충돌 확인(§6.1 보정).
- [x] `concepts/` vs `wiki/concepts/`, `decisions/` vs `wiki/decisions/` — 중복/드리프트 여부와 정본(canonical) 결정. → 정본 = `wiki/*`. 루트 `concepts/`는 추출 덤프(§3.1 보정).
- [x] 위키링크가 경로 기반인가 이름 기반인가의 비율. → 이름형 84% : 별칭 15% : 경로 1%(§7 보정).
- [x] `_index` 파일이 `.md` 확장자를 갖는가, 어느 디렉터리에 존재하는가. → 8개 전부 `wiki/<sub>/_index.md`(§6.3 보정).
- [x] `moc/`의 콘텐츠가 디렉터리 색인 성격인가 독립 개념인가. → 빈 폴더(no-op).
- [x] `weekly/`·`projects/*/Timeline`의 실제 포맷(→ `log.md` 매핑 규칙 확정). → §6.3 보정 + findings §7.

---
## 11. Phase 0 검증 결과 반영 요약 (2026-06-16)

> BUILD_PLAN의 ⚠ 지침("Phase 0 결과가 SPEC 가정과 다르면 코드 작성 전에 SPEC을 먼저 갱신하고 사람 확인을 받는다")에 따른 보정 통합. 근거: `_ops/okf-phase0-findings.md`. **이 6건은 사람 확인 후 Phase 1 코드에 반영한다.**

1. **IN/OUT 경계 (§3)**: 루트 `concepts/`(추출 덤프)·`people/`(슬라이드 이미지)를 IN→피드스톡(OUT)으로. 빈 폴더 `decisions/`·`permanent/`·`moc/`(루트)는 IN 무효. **확정 정본 IN = `wiki/**` + `projects/**`** (+소량 `references/`·`research/`·`analysis/`).
2. **TYPE_MAP (§5)**: 루트 prefix 5종 제거. `wiki/signals/`→`Signal`, `wiki/protocols/`→`Protocol` 추가. type 값 PascalCase 정규화.
3. **status 정규화 (§6.1)**: 단어 방언(`seed|growing|mature|archived`) ↔ 이모지(`💡🔄✅📦`) 매핑표로 발행본 통일.
4. **relations 매핑 (§6.1/§6.4)**: `projects/`의 `related_to: "[[x]]"` 단일 위키링크 → `relations[]` 매핑(Phase 3).
5. **위키링크 변환 (§7)**: 이름형 84% 현실 반영 — `aliases` 보조 인덱스 + slug 정규화 규칙 추가.
6. **Timeline 파싱 (§6.3)**: 헤딩 텍스트(`## 3. 타임라인`)가 아니라 `### <ISO-date>` 패턴 기반 인식, `(Planned)` 접미 보존.
