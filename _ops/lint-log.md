## LINT-LOG: 2026-06-16 (OKF Conformance 베이스라인 — Phase 1)

> 트리거: `python -m scripts.okf.publish --only conformance --write`
> LINT 프로토콜이 OKF conformance checker(SPEC §8)로 승격된 첫 측정.
> 전체 리포트: `_ops/okf/lint-baseline-2026-06-16.md`

### 게이트: FAIL ❌ (ERROR 69 · WARN 49 · INFO 0)

| 코드 | severity | 건수 | 비고 |
| --- | --- | ---: | --- |
| `malformed-frontmatter` | ERROR | 69 | YAML 파싱 실패. 대부분 `related_to: "[[a]]", "[[b]]"` 쉼표 나열(§11 보정 4 대상). ex-intelligence 44건 집중 |
| `legacy-dialect` | WARN | 44 | 본문 위키링크 잔존(발행 시 변환 대상) |
| `type-conflict` | WARN | 5 | 기존 type ≠ 경로 유도 type |

- 대상: 번들 IN 145개 파일(`wiki, projects, references, research, analysis`).
- 루트 정크 격리 큐 11건(이동/삭제는 사람 확인 후).
- **다음 감소 작전**: ERROR 69건의 거의 전부가 malformed `related_to`이므로, Phase 2 frontmatter
  단계에서 `related_to` 쉼표 나열 → YAML 리스트 정규화 한 번으로 대량 해소 예상.

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
