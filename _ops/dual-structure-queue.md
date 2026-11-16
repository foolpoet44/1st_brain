---
title: 이중구조 결손 명단 — 요약·기록 둘 다 없는 위키 문서
created: 2026-11-16
updated: 2026-11-16
type: ops
status: Active
generated:
  by: ai-assisted-ingest
  at: 2026-11-16
evidence: confirmed
---

# 이중구조 결손 명단 (둘 다 결손)

> 2026-11-15 성찰 처방 ② 의 집행물. `wiki/` 모집단 125편(`_index.md` 9편 제외) 중
> `## Compiled Truth` 와 `## Timeline` 을 **둘 다** 갖지 않고, `processed: true`(종결 선언)도 아닌 문서의 전수 명단이다.
> 2026-11-14 까지의 집행 큐(기준 B — 기록은 있고 요약만 없는 문서)는 이 명단을 한 번도 포함하지 않았다.

## 순위 기준 두 가지 — 왜 나눠 세는가

어제 처방은 "인용 많고 오래된 순"이라고만 적었다. 그대로 세면 **인용의 출처를 묻지 않는다.**
이 명단 57편의 인용을 출처별로 가른 결과는 다음과 같다.

| 인용 출처 | 건수 | 비중 |
| :-- | --: | --: |
| 지식 영역 (`wiki/` 본문 · `projects/`) | 38 | 11% |
| 자동 생성 목차 (`wiki/**/_index.md`) | 42 | 12% |
| 본 성찰 계열 자기 인용 (`outputs/` · `_ops/`) | 253 | 74% |
| 그 밖 | 6 | 1% |
| **합계** | **339** | 100% |

그래서 두 가지 점수를 함께 적는다.

- **점수 A (전체 인용)** = 미갱신일수 × (1 + 전체 인용 수). 2026-11-12 이후 쓰던 방식.
- **점수 B (지식 인용)** = 미갱신일수 × (1 + 지식 영역 인용 수). 목차와 자기 인용을 뺀 값. **집행 순서는 B 를 따른다.**

## 명단 (점수 B 내림차순)

| # | 문서 | 마지막 갱신 | 미갱신일 | 지식 인용 | 목차 | 자기 인용 | 점수 B | 점수 A |
| --: | :-- | :-- | --: | --: | --: | --: | --: | --: |
| 1 | `wiki/concepts/knowledge-graph-as-map.md` | 2026-04-29 | 201 | 5 | 0 | 15 | 1206 | 4221 |
| 2 | `wiki/concepts/execution-surface.md` | 2026-04-29 | 201 | 3 | 1 | 34 | 804 | 7839 |
| 3 | `wiki/concepts/skillopt.md` | 2026-04-29 | 201 | 3 | 0 | 0 | 804 | 804 |
| 4 | `wiki/concepts/maximal-knowledge-exactness.md` | 2026-04-29 | 201 | 2 | 0 | 2 | 603 | 1005 |
| 5 | `wiki/concepts/constructed-fit.md` | 2026-04-29 | 201 | 2 | 1 | 0 | 603 | 804 |
| 6 | `wiki/concepts/agent-friendly-redesign.md` | 2026-04-29 | 201 | 2 | 1 | 0 | 603 | 804 |
| 7 | `wiki/concepts/eval.md` | 2026-06-27 | 142 | 2 | 1 | 4 | 426 | 1136 |
| 8 | `wiki/concepts/durable-execution.md` | 2026-04-29 | 201 | 1 | 1 | 38 | 402 | 8241 |
| 9 | `wiki/frameworks/weak-signal-ansoff.md` | 2026-04-29 | 201 | 1 | 1 | 4 | 402 | 1407 |
| 10 | `wiki/concepts/digital-unconscious.md` | 2026-04-29 | 201 | 1 | 1 | 1 | 402 | 1005 |
| 11 | `wiki/concepts/meta-harnessing.md` | 2026-04-29 | 201 | 1 | 1 | 1 | 402 | 804 |
| 12 | `wiki/concepts/8-cluster-model.md` | 2026-04-29 | 201 | 1 | 1 | 1 | 402 | 804 |
| 13 | `wiki/concepts/codegraph-efficiency.md` | 2026-04-29 | 201 | 1 | 0 | 2 | 402 | 804 |
| 14 | `wiki/signals/talent-market-disruption.md` | 2026-04-29 | 201 | 1 | 1 | 1 | 402 | 804 |
| 15 | `wiki/concepts/memo-architecture.md` | 2026-04-29 | 201 | 1 | 1 | 0 | 402 | 603 |
| 16 | `wiki/protocols/validation-protocol.md` | 2026-04-29 | 201 | 1 | 1 | 0 | 402 | 603 |
| 17 | `wiki/concepts/token-maxing.md` | 2026-04-29 | 201 | 1 | 0 | 0 | 402 | 402 |
| 18 | `wiki/signals/2026-05-30-automated-task-packaging.md` | 2026-05-31 | 169 | 1 | 1 | 2 | 338 | 845 |
| 19 | `wiki/concepts/ai-evaluation-system.md` | 2026-06-27 | 142 | 1 | 1 | 2 | 284 | 710 |
| 20 | `wiki/signals/2026-06-27-autonomous-talent-agency-shift.md` | 2026-06-27 | 142 | 1 | 1 | 2 | 284 | 710 |
| 21 | `wiki/concepts/graph-rag.md` | 2026-07-02 | 137 | 1 | 1 | 1 | 274 | 548 |
| 22 | `wiki/concepts/hermes-pi-philosophy.md` | 2026-04-29 | 201 | 0 | 1 | 29 | 201 | 6432 |
| 23 | `wiki/concepts/contextual-ingestion.md` | 2026-04-29 | 201 | 0 | 1 | 6 | 201 | 1608 |
| 24 | `wiki/concepts/competency-question.md` | 2026-04-29 | 201 | 0 | 1 | 1 | 201 | 603 |
| 25 | `wiki/concepts/automated-ontology-generation.md` | 2026-04-29 | 201 | 0 | 1 | 1 | 201 | 603 |
| 26 | `wiki/concepts/antigravity-2-0.md` | 2026-04-29 | 201 | 0 | 1 | 0 | 201 | 402 |
| 27 | `wiki/concepts/linkedin-agent-automation-20260525.md` | 2026-04-29 | 201 | 0 | 1 | 0 | 201 | 402 |
| 28 | `wiki/concepts/failed-pattern-trading.md` | 2026-04-29 | 201 | 0 | 1 | 0 | 201 | 402 |
| 29 | `wiki/concepts/knowledge-synthesis-steps.md` | 2026-04-29 | 201 | 0 | 1 | 0 | 201 | 402 |
| 30 | `wiki/concepts/gemini-spark.md` | 2026-04-29 | 201 | 0 | 1 | 0 | 201 | 402 |
| 31 | `wiki/signals/transportation-ai-pivot.md` | 2026-04-29 | 201 | 0 | 1 | 0 | 201 | 402 |
| 32 | `wiki/signals/2026-05-20-google-io-sign-of-agentic-shift.md` | 2026-05-20 | 180 | 0 | 1 | 1 | 180 | 720 |
| 33 | `wiki/concepts/context-corpus.md` | 2026-05-21 | 179 | 0 | 1 | 1 | 179 | 537 |
| 34 | `wiki/signals/2026-05-30-josh-kim-ai-native-company-record.md` | 2026-05-30 | 170 | 0 | 1 | 2 | 170 | 680 |
| 35 | `wiki/signals/2026-05-30-claude-opus-4-8-detailed-harnessing.md` | 2026-05-30 | 170 | 0 | 1 | 2 | 170 | 680 |
| 36 | `wiki/signals/2026-05-30-hs-top-failure-long-strategy.md` | 2026-05-30 | 170 | 0 | 1 | 2 | 170 | 680 |
| 37 | `wiki/signals/2026-05-30-claude-opus-4-8-launch-and-prompting-shift.md` | 2026-05-30 | 170 | 0 | 1 | 2 | 170 | 680 |
| 38 | `wiki/signals/2026-05-30-obelisk-sqlite-durable-execution.md` | 2026-05-30 | 170 | 0 | 1 | 1 | 170 | 510 |
| 39 | `wiki/signals/2026-05-30-dynamic-workflow-harness.md` | 2026-05-31 | 169 | 0 | 1 | 2 | 169 | 676 |
| 40 | `wiki/signals/2026-05-30-db-schema-knowledge-automation.md` | 2026-05-31 | 169 | 0 | 1 | 2 | 169 | 676 |
| 41 | `wiki/concepts/gbrain-personal-ai-os.md` | 2026-05-31 | 169 | 0 | 1 | 0 | 169 | 338 |
| 42 | `wiki/signals/2026-06-03-logicrag-lazy-graph-reasoning.md` | 2026-06-03 | 166 | 0 | 1 | 1 | 166 | 498 |
| 43 | `wiki/signals/2026-06-13-agentic-ta-mainstream-shift.md` | 2026-06-13 | 156 | 0 | 1 | 2 | 156 | 624 |
| 44 | `wiki/signals/2026-06-13-hermes-agent-infrastructure-shift.md` | 2026-06-13 | 156 | 0 | 1 | 1 | 156 | 468 |
| 45 | `wiki/signals/2026-06-15-agentic-ta-reset.md` | 2026-06-15 | 154 | 0 | 1 | 1 | 154 | 462 |
| 46 | `wiki/signals/2026-06-22-agentic-orchestration-shift.md` | 2026-06-22 | 147 | 0 | 1 | 1 | 147 | 441 |
| 47 | `wiki/signals/2026-06-25-hr-performance-architect-pivot.md` | 2026-06-25 | 144 | 0 | 1 | 1 | 144 | 432 |
| 48 | `wiki/signals/2026-07-06-dawn-of-hr-superagents.md` | 2026-07-06 | 133 | 0 | 0 | 2 | 133 | 399 |
| 49 | `wiki/concepts/aihr-design-framework-tom-sdm.md` | —(날짜 칸 없음) | — | 0 | 0 | 2 | 0 | 0 |
| 50 | `wiki/concepts/agentic-roi.md` | —(날짜 칸 없음) | — | 2 | 0 | 73 | 0 | 0 |
| 51 | `wiki/synapse/HR_TECH_PSYCHOLOGY_2026-07-29.md` | —(날짜 칸 없음) | — | 0 | 0 | 1 | 0 | 0 |
| 52 | `wiki/briefings/HR_TECH_PSYCH_2026-07-31.md` | —(날짜 칸 없음) | — | 0 | 0 | 1 | 0 | 0 |
| 53 | `wiki/signals/2026-07-11-deepwiki-post.md` | —(날짜 칸 없음) | — | 0 | 0 | 2 | 0 | 0 |
| 54 | `wiki/signals/hr-tech/2026-07-30-agentic-adoption.md` | —(날짜 칸 없음) | — | 0 | 0 | 1 | 0 | 0 |
| 55 | `wiki/tools/deepwiki.md` | —(날짜 칸 없음) | — | 1 | 0 | 1 | 0 | 0 |
| 56 | `wiki/synapses/IO_PSYCHOLOGY_SYNAPSE_2026-07-30.md` | —(날짜 칸 없음) | — | 0 | 0 | 0 | 0 | 0 |
| 57 | `wiki/people/duckjung-kim.md` | —(날짜 칸 없음) | — | 2 | 0 | 1 | 0 | 0 |

## 판독

- 전체 **57편**. 그중 **33편**은 지식 영역 인용이 **0** 이다 — 목차와 본 성찰 계열만 이 문서들을 부른다.
- 날짜 칸(`updated`)이 없어 나이를 셀 수 없는 문서 **9편**은 점수가 0 으로 깔린다. 나이를 모르는 문서는 순위에서 가장 젊게 취급된다 — 2026-11-11 에 적발한 것과 같은 결함이다.
- 점수 A 1위는 `wiki/concepts/durable-execution.md`(자기 인용 38건), 점수 B 1위는 `wiki/concepts/knowledge-graph-as-map.md`(지식 인용 5건)이다. 두 순위의 1위가 다르다.

## 갱신 규칙

- 집행(요약·기록 신설)이 일어난 날마다 이 명단을 다시 산출한다. 줄어든 편수와 남은 편수를 함께 적는다.
- 명단에서 문서가 빠지는 경우는 두 가지뿐이다 — ① 이중구조를 갖춤 ② `processed: true` 로 종결 선언. 그 밖의 이유로 사라지면 그것이 사고다.
