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

---

## LINT-LOG: 2026-10-13 — 링크 부스팅 손상 일괄 복원

> 2026-07-27 Hermes Agent 의 링크 부스터(`fecec41`·`82164c3`·`7a51a3e`·`694e697`)가 본문 문자열을 무관한 파일 링크로 바꾼 손상을 CSP 결정으로 일괄 복원했다.

- **손상의 모양.** 단어 일부를 링크로 치환(`Compiled Truth` → `Compiled T[[…ru.md|ru]]th`, `www.notion.so` → `www.[[wiki/tools/notion.md|notion]].so`)했다. 대소문자도 바꿨다(`Claude` → `[[CLAUDE.md|CLAUDE]]`, `skill_manage` → `SKILL_manage`). 제목 줄 전체를 자기 링크로 덮기도 했다(`# SOUL.md - The Synaptic Orchestrator…` → `# [[SOUL.md|SOUL]]`). 그래서 링크를 푸는 것만으로는 원문이 돌아오지 않는다.
- **복원 방법.** 손상 커밋이 바꾼 줄을 직전 판본의 줄과 짝지어 "손상 줄 → 원래 줄" 사전(965 쌍)을 만들었다. 그 뒤 현재 파일에서 손상 줄과 정확히 같은 줄만 되돌렸다(`scripts/restore_link_boost_lines.py`). 이후에 정상적으로 편집되어 사전과 어긋난 줄은 링크만 풀었다(`scripts/restore_link_boost_unwrap.py`). 원본이 없는 파일 몇 개는 사람이 줄 단위로 고쳤다.
- **결과.** 487 개 파일, 1,089 줄 복원. 손상 커밋 외에는 손대지 않은 파일 442 개는 손상 이전 판본의 줄이 **하나도 빠짐없이** 돌아왔다(검산 442/442). 부스터가 함께 넣은 `type`/`status` 머리말 정보는 정당한 변경이라 유지했다.
- **의도적으로 남긴 것.** 손상을 *설명하는* 기록(`_ops/bridge-log.md` 675 행, `_ops/change-log.md`, `scripts/fix_wikilinks.py` 주석, 저녁 성찰 인용)은 원문 그대로 두었다. `templates/wiki-note.md` 는 PR #28 에서 새로 쓰므로 제외했다.
- **원문을 알 수 없어 추정한 곳 (3 곳).** `inbox/notes/2026-07-14.md` 제목은 처음부터 손상된 채 만들어져 "README 생성 SKILL"로, `무제.md` 의 URL 은 `claude.ai` 로, `변재민 등.md` 711 행의 `SKILLii` 는 대소문자를 알 수 없어 그대로 두었다.
- **덤으로 확인한 것.** 첫 시도의 보조 스크립트가 `git ls-files` 를 그대로 읽어 한글 이름 파일을 전부 건너뛰었다. 10-11 저녁 성찰이 지적한 것과 같은 함정이다. `-z` 옵션으로 고쳤다.
