---
title: 이중구조 결손 명단 — 요약·기록 둘 다 없는 위키 문서
created: 2026-11-16
updated: 2026-11-17
type: ops
status: Active
generated:
  by: ai-assisted-ingest
  at: 2026-11-17
evidence: confirmed
---

# 이중구조 결손 명단 (둘 다 결손)

> 2026-11-15 성찰 처방 ② 의 집행물. `wiki/` 모집단에서 `_index.md` 를 제외한 문서 중
> `## Compiled Truth` 와 `## Timeline` 을 **둘 다** 갖지 않고, `processed: true`(종결 선언)도 아닌 문서의 전수 명단이다.
> 2026-11-14 까지의 집행 큐(기준 B — 기록은 있고 요약만 없는 문서)는 이 명단을 한 번도 포함하지 않았다.
> **매 회차 기계로 다시 산출한다. 손으로 고치지 않는다.**

## 집행 경과

| 날짜 | 집행 문서 | 남은 편수 |
| :-- | :-- | --: |
| 2026-11-16 | `wiki/concepts/knowledge-graph-as-map.md` (점수 B 1위) | 57 → 56 |
| 2026-11-17 | `wiki/concepts/execution-surface.md` (점수 B 2위) | 56 → **55** |

## 순위 기준 두 가지 — 왜 나눠 세는가

인용을 셀 때 **출처를 묻지 않으면** 관찰자가 그린 연결이 지식의 중요도로 보고된다.
2026-11-17 재산출 기준 이 명단 55편의 인용(편수 기준)을 출처별로 가른 결과는 다음과 같다.

| 인용 출처 | 편수 | 비중 |
| :-- | --: | --: |
| 지식 영역 (`wiki/` 본문 · `projects/`) | 35 | 12% |
| 자동 생성 목차 (`wiki/**/_index.md`) | 41 | 14% |
| 본 성찰 계열 자기 인용 (`outputs/` · `_ops/`) | 205 | 71% |
| 그 밖 | 6 | 2% |
| **합계** | **287** | 100% |

- **점수 A (전체 인용)** = 미갱신일수 × (1 + 전체 인용 편수). 2026-11-12 이후 쓰던 방식.
- **점수 B (지식 인용)** = 미갱신일수 × (1 + 지식 영역 인용 편수). 목차와 자기 인용을 뺀 값. **집행 순서는 B 를 따른다.**

## 명단 (점수 B 내림차순, 2026-11-17 재산출)

| # | 문서 | 마지막 갱신 | 미갱신일 | 지식 인용 | 목차 | 자기 인용 | 점수 B | 점수 A |
| --: | :-- | :-- | --: | --: | --: | --: | --: | --: |
| 1 | `wiki/concepts/maximal-knowledge-exactness.md` | 2026-04-29 | 202 | 3 | 0 | 2 | 808 | 1212 |
| 2 | `wiki/concepts/skillopt.md` | 2026-04-29 | 202 | 3 | 0 | 0 | 808 | 808 |
| 3 | `wiki/concepts/agent-friendly-redesign.md` | 2026-04-29 | 202 | 2 | 1 | 0 | 606 | 808 |
| 4 | `wiki/concepts/constructed-fit.md` | 2026-04-29 | 202 | 2 | 1 | 0 | 606 | 808 |
| 5 | `wiki/concepts/durable-execution.md` | 2026-04-29 | 202 | 2 | 1 | 38 | 606 | 8484 |
| 6 | `wiki/concepts/eval.md` | 2026-06-27 | 143 | 2 | 1 | 4 | 429 | 1144 |
| 7 | `wiki/concepts/graph-rag.md` | 2026-07-02 | 138 | 2 | 1 | 1 | 414 | 690 |
| 8 | `wiki/concepts/8-cluster-model.md` | 2026-04-29 | 202 | 1 | 1 | 1 | 404 | 808 |
| 9 | `wiki/concepts/codegraph-efficiency.md` | 2026-04-29 | 202 | 1 | 0 | 2 | 404 | 808 |
| 10 | `wiki/concepts/contextual-ingestion.md` | 2026-04-29 | 202 | 1 | 1 | 6 | 404 | 1818 |
| 11 | `wiki/concepts/digital-unconscious.md` | 2026-04-29 | 202 | 1 | 1 | 1 | 404 | 1010 |
| 12 | `wiki/concepts/gemini-spark.md` | 2026-04-29 | 202 | 1 | 1 | 0 | 404 | 606 |
| 13 | `wiki/concepts/memo-architecture.md` | 2026-04-29 | 202 | 1 | 1 | 0 | 404 | 606 |
| 14 | `wiki/concepts/meta-harnessing.md` | 2026-04-29 | 202 | 1 | 1 | 2 | 404 | 1010 |
| 15 | `wiki/concepts/token-maxing.md` | 2026-04-29 | 202 | 1 | 0 | 0 | 404 | 404 |
| 16 | `wiki/frameworks/weak-signal-ansoff.md` | 2026-04-29 | 202 | 1 | 1 | 4 | 404 | 1414 |
| 17 | `wiki/protocols/validation-protocol.md` | 2026-04-29 | 202 | 1 | 1 | 0 | 404 | 606 |
| 18 | `wiki/signals/talent-market-disruption.md` | 2026-04-29 | 202 | 1 | 1 | 1 | 404 | 808 |
| 19 | `wiki/signals/2026-05-30-automated-task-packaging.md` | 2026-05-31 | 170 | 1 | 1 | 2 | 340 | 850 |
| 20 | `wiki/concepts/ai-evaluation-system.md` | 2026-06-27 | 143 | 1 | 1 | 2 | 286 | 715 |
| 21 | `wiki/signals/2026-06-27-autonomous-talent-agency-shift.md` | 2026-06-27 | 143 | 1 | 1 | 2 | 286 | 715 |
| 22 | `wiki/concepts/antigravity-2-0.md` | 2026-04-29 | 202 | 0 | 1 | 0 | 202 | 404 |
| 23 | `wiki/concepts/automated-ontology-generation.md` | 2026-04-29 | 202 | 0 | 1 | 1 | 202 | 606 |
| 24 | `wiki/concepts/competency-question.md` | 2026-04-29 | 202 | 0 | 1 | 1 | 202 | 606 |
| 25 | `wiki/concepts/failed-pattern-trading.md` | 2026-04-29 | 202 | 0 | 1 | 0 | 202 | 404 |
| 26 | `wiki/concepts/hermes-pi-philosophy.md` | 2026-04-29 | 202 | 0 | 1 | 29 | 202 | 6464 |
| 27 | `wiki/concepts/knowledge-synthesis-steps.md` | 2026-04-29 | 202 | 0 | 1 | 0 | 202 | 404 |
| 28 | `wiki/concepts/linkedin-agent-automation-20260525.md` | 2026-04-29 | 202 | 0 | 1 | 0 | 202 | 404 |
| 29 | `wiki/signals/transportation-ai-pivot.md` | 2026-04-29 | 202 | 0 | 1 | 0 | 202 | 404 |
| 30 | `wiki/signals/2026-05-20-google-io-sign-of-agentic-shift.md` | 2026-05-20 | 181 | 0 | 1 | 1 | 181 | 724 |
| 31 | `wiki/concepts/context-corpus.md` | 2026-05-21 | 180 | 0 | 1 | 1 | 180 | 540 |
| 32 | `wiki/signals/2026-05-30-claude-opus-4-8-detailed-harnessing.md` | 2026-05-30 | 171 | 0 | 1 | 2 | 171 | 684 |
| 33 | `wiki/signals/2026-05-30-claude-opus-4-8-launch-and-prompting-shift.md` | 2026-05-30 | 171 | 0 | 1 | 2 | 171 | 684 |
| 34 | `wiki/signals/2026-05-30-hs-top-failure-long-strategy.md` | 2026-05-30 | 171 | 0 | 1 | 2 | 171 | 684 |
| 35 | `wiki/signals/2026-05-30-josh-kim-ai-native-company-record.md` | 2026-05-30 | 171 | 0 | 1 | 2 | 171 | 684 |
| 36 | `wiki/signals/2026-05-30-obelisk-sqlite-durable-execution.md` | 2026-05-30 | 171 | 0 | 1 | 1 | 171 | 513 |
| 37 | `wiki/concepts/gbrain-personal-ai-os.md` | 2026-05-31 | 170 | 0 | 1 | 0 | 170 | 340 |
| 38 | `wiki/signals/2026-05-30-db-schema-knowledge-automation.md` | 2026-05-31 | 170 | 0 | 1 | 2 | 170 | 680 |
| 39 | `wiki/signals/2026-05-30-dynamic-workflow-harness.md` | 2026-05-31 | 170 | 0 | 1 | 2 | 170 | 680 |
| 40 | `wiki/signals/2026-06-03-logicrag-lazy-graph-reasoning.md` | 2026-06-03 | 167 | 0 | 1 | 1 | 167 | 501 |
| 41 | `wiki/signals/2026-06-13-agentic-ta-mainstream-shift.md` | 2026-06-13 | 157 | 0 | 1 | 2 | 157 | 628 |
| 42 | `wiki/signals/2026-06-13-hermes-agent-infrastructure-shift.md` | 2026-06-13 | 157 | 0 | 1 | 1 | 157 | 471 |
| 43 | `wiki/signals/2026-06-15-agentic-ta-reset.md` | 2026-06-15 | 155 | 0 | 1 | 1 | 155 | 465 |
| 44 | `wiki/signals/2026-06-22-agentic-orchestration-shift.md` | 2026-06-22 | 148 | 0 | 1 | 1 | 148 | 444 |
| 45 | `wiki/signals/2026-06-25-hr-performance-architect-pivot.md` | 2026-06-25 | 145 | 0 | 1 | 1 | 145 | 435 |
| 46 | `wiki/signals/2026-07-06-dawn-of-hr-superagents.md` | 2026-07-06 | 134 | 0 | 0 | 2 | 134 | 402 |
| 47 | `wiki/briefings/HR_TECH_PSYCH_2026-07-31.md` | —(날짜 칸 없음) | — | 0 | 0 | 1 | 0 | 0 |
| 48 | `wiki/concepts/agentic-roi.md` | —(날짜 칸 없음) | — | 2 | 0 | 73 | 0 | 0 |
| 49 | `wiki/concepts/aihr-design-framework-tom-sdm.md` | —(날짜 칸 없음) | — | 0 | 0 | 2 | 0 | 0 |
| 50 | `wiki/people/duckjung-kim.md` | —(날짜 칸 없음) | — | 2 | 0 | 1 | 0 | 0 |
| 51 | `wiki/signals/2026-07-11-deepwiki-post.md` | —(날짜 칸 없음) | — | 0 | 0 | 2 | 0 | 0 |
| 52 | `wiki/signals/hr-tech/2026-07-30-agentic-adoption.md` | —(날짜 칸 없음) | — | 0 | 0 | 1 | 0 | 0 |
| 53 | `wiki/synapse/HR_TECH_PSYCHOLOGY_2026-07-29.md` | —(날짜 칸 없음) | — | 0 | 0 | 1 | 0 | 0 |
| 54 | `wiki/synapses/IO_PSYCHOLOGY_SYNAPSE_2026-07-30.md` | —(날짜 칸 없음) | — | 0 | 0 | 0 | 0 | 0 |
| 55 | `wiki/tools/deepwiki.md` | —(날짜 칸 없음) | — | 1 | 0 | 1 | 0 | 0 |

## 판독 (2026-11-17)

- 전체 **55편**. 그중 **31편**은 지식 영역 인용이 **0** 이다 — 목차와 본 성찰 계열만 이 문서들을 부른다.
- 날짜 칸(`updated`)이 없어 나이를 셀 수 없는 문서 **9편**은 점수가 0 으로 깔린다. 나이를 모르는 문서는 순위에서 가장 젊게 취급된다 — 2026-11-11 에 적발한 것과 같은 결함이다.
- **집행이 순위를 바꾼다.** 11-16 에 집행한 `knowledge-graph-as-map` 의 새 요약이 [[maximal-knowledge-exactness]] 를 인용했고, 그 결과 그 문서의 지식 인용이 2 → 3 으로 올라 점수 B 1위가 됐다(어제 4위). 지식 영역 인용이라도 **집행자가 그린 엣지**라면 관찰자 기여다. 자기 인용만 걷어 내는 것으로는 충분하지 않다는 뜻이며, 이 구분을 어떻게 셀지는 미해소 항목으로 등재했다.
- 점수 A 1위는 여전히 `wiki/concepts/durable-execution.md`(자기 인용 38편)이다. 두 순위의 1위가 다르다.

## 갱신 규칙

- 집행(요약·기록 신설)이 일어난 날마다 이 명단을 **기계로** 다시 산출한다. 줄어든 편수와 남은 편수를 함께 적는다.
- 명단에서 문서가 빠지는 경우는 두 가지뿐이다 — ① 이중구조를 갖춤 ② `processed: true` 로 종결 선언. 그 밖의 이유로 사라지면 그것이 사고다.
