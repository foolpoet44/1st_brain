---
type: Note
---

status: Active

## LINT-LOG: 2026-06-27 (wiki-scoped)

> 대시보드 고아 탐지가 레포 전체를 스캔해 루트 스크래치 파일(`2605.md`, `KNOWLEDGE_PULSE.md` 등)을 오탐하던 문제를 발견. `wiki/`만 정밀 스캔하니 실제 구조적 부채가 드러남.

### 점검 전 (Before)

- 고립 문서 (inbound 0): **30개** (개념 9, 신호 19, 프레임워크 1, 프로토콜 1)
- 필수 필드 누락: **51개** (자동 수집 문서들이 `title/created/updated` 없이 `date`만 보유)
- Frontmatter 파싱 실패: 0개
- 갱신 정체(6주+): 24개 (단, `updated` 필드 자체가 없어 과소 집계됨)

### 조치 (Actions)

1. **프론트매터 정규화 (51개)** — 누락된 `title`(H1/파일명 유도)·`created`·`updated`·`status` 보강, `type` 값 소문자 정규화(Note→concept). 날짜는 문서의 `date` 필드 또는 파일명 날짜 접두사에서 가져와 **정체 신호를 위조하지 않음**.
2. **고립 해소 (30개)** — 각 섹션 `_index.md` 허브가 깨진 제목 링크(`[[AI Boom and Labor Distribution]]`) 대신 **해결 가능한 stem 링크**로 모든 문서를 가리키도록 재구성. `wiki/signals/_index.md`(19개 전체 주제별 재편), `wiki/concepts/_index.md`(누락 9개 추가), `wiki/frameworks/_index.md`(손상된 줄번호 접두사 복구 + `weak-signal-ansoff` 추가), `wiki/protocols/_index.md`(신규 생성).

### 점검 후 (After)

- 고립 문서: **0개** ✅
- 필수 필드 누락: **0개** ✅
- Frontmatter 파싱 실패: 0개 ✅
- 인덱스 링크 해결 불가: 0개 ✅
- 갱신 정체(6주+): **56개** — 정규화로 `updated`가 정직하게 채워지며 드러난 콘텐츠 신선도 백로그. 날짜 위조 대신 후속 과제로 보고.

### 남은 과제 (CSP 보고)

- 56개 노후 문서(대부분 2026-04-29 생성 후 미갱신)의 Compiled Truth 재방문 — 특히 조직심리학 코어(SDT, LMX, weak-signal-theory)는 최신 신호와 재연결 필요.
- 대시보드 고아 탐지 로직을 `wiki/` 스코프로 한정하는 수정 권고(현재 루트 파일 오탐).

---

## LINT-LOG: 2026-05-17 14:28:47

### [Isolated Documents (Backlinks: 0)]

- [[claude-code]] (wiki/tools/claude-code.md)
- [[notion]] (wiki/tools/notion.md)
- [[obsidian]] (wiki/tools/obsidian.md)
- [[_index]] (wiki/tools/\_index.md)
- [[2026-05-10-system-evolution]] (wiki/decisions/2026-05-10-system-evolution.md)
- [[csp]] (wiki/people/csp.md)
- [[pulse-check]] (wiki/concepts/pulse-check.md)
- [[competency-question]] (wiki/concepts/competency-question.md)
- [[self-determination-theory]] (wiki/concepts/self-determination-theory.md)
- [[ax-internalization]] (wiki/concepts/ax-internalization.md)
- [[vibe-coding]] (wiki/concepts/vibe-coding.md)
- [[leader-member-exchange]] (wiki/concepts/leader-member-exchange.md)
- [[ai-recruitment-behavioral-economics]] (wiki/concepts/ai-recruitment-behavioral-economics.md)
- [[economic-freedom]] (wiki/concepts/economic-freedom.md)
- [[weak-signal-theory]] (wiki/concepts/weak-signal-theory.md)
- [[knowledge-capitalization]] (wiki/concepts/knowledge-capitalization.md)
- [[data-sensing]] (wiki/concepts/data-sensing.md)
- [[ex-intelligence]] (wiki/concepts/ex-intelligence.md)
- [[csp-brain-system]] (wiki/concepts/csp-brain-system.md)
- [[memory-save]] (wiki/skills/memory-save.md)
- [[context-restore]] (wiki/skills/context-restore.md)
- [[dream-cycle]] (wiki/skills/dream-cycle.md)
- [[weak-signal-ansoff]] (wiki/frameworks/weak-signal-ansoff.md)
- [[7-layer-architecture]] (wiki/frameworks/7-layer-architecture.md)
- [[compiled-truth-timeline]] (wiki/frameworks/compiled-truth-timeline.md)
- [[protocols]] (wiki/frameworks/protocols.md)

### [Outdated (No update for 6+ weeks)]

### [Frontmatter Issues]

- wiki/decisions/2026-05-10-system-evolution.md (YAML Error: mapping values are not allowed here
  in "<unicode string>", line 1, column 35:
  title: 2026-05-10 System Evolution: Transition to Coding Factory C ...
  ^)
- wiki/concepts/ai-recruitment-behavioral-economics.md (YAML Error: mapping values are not allowed here
  in "<unicode string>", line 1, column 32:
  title: AI Recruitment Solutions: Collaboration & Behavioral Eco ...
  ^)
- wiki/frameworks/layer-1-compass.md (YAML Error: mapping values are not allowed here
  in "<unicode string>", line 1, column 15:
  title: Layer 1: COMPASS (방향)
  ^)
- wiki/frameworks/weak-signal-ansoff.md (YAML Error: while parsing a block mapping
  in "<unicode string>", line 1, column 1:
  title: "Ansoff's Weak Signal Fra ...
  ^
  expected <block end>, but found ','
  in "<unicode string>", line 4, column 34:
  related_to: "[[layer-1-compass]]", "[[opq-framework]]"
  ^)

---

# Lint Log

위키 자가 점검 결과 기록입니다.

---

## 2026-04-30 Dream Cycle

- status 점검 실행: `bash scripts/status.sh`
- 발견 사항:
  - 미추적 폴더: `dev/`
  - 고립 문서 후보: `wiki/frameworks/compiled-truth-timeline.md`
  - 비어 있는 운영 로그: `question-log.md`, `bridge-log.md`
- 조치:
  - 변경 가시성 로그와 weekly/dashboard는 정상 작동 확인
  - 고립 문서와 `dev/` 폴더는 별도 정리 대상으로 보류
