---
title: 이중구조 결손 명단 — 요약·기록 둘 다 없는 위키 문서
created: 2026-11-16
updated: 2026-11-18
type: ops
status: Active
generated:
  by: ai-assisted-ingest
  at: 2026-11-18
evidence: confirmed
---

# 이중구조 결손 명단 (둘 다 결손)

> 2026-11-15 성찰 처방 ② 의 집행물. `wiki/` 모집단에서 `_index.md` 를 제외한 문서 중
> `## Compiled Truth` 와 `## Timeline` 을 **둘 다** 갖지 않고, `processed: true`(종결 선언)도 아닌 문서의 전수 명단이다.
> **매 회차 기계로 다시 산출한다. 손으로 고치지 않는다.**

## 집행 경과

| 날짜 | 집행 문서 | 선정 기준 | 남은 편수 |
| :-- | :-- | :-- | --: |
| 2026-11-16 | `wiki/concepts/knowledge-graph-as-map.md` | 점수 B 1위(자기 인용·목차 제외) | 57 → 56 |
| 2026-11-17 | `wiki/concepts/execution-surface.md` | 점수 B 2위 | 56 → 55 |
| 2026-11-18 | `wiki/concepts/skillopt.md` | **점수 D 1위**(집행분까지 제외) | 55 → **54** |

## 순위 기준 — 왜 세 갈래로 가르는가

2026-11-16 에 자기 인용과 자동 목차를 걷어 냈고(점수 B), 2026-11-17 에 "집행자가 그린 엣지가 순위를 움직인다"는 사실을 적발했다.
2026-11-18 에 그 적발을 기계로 전수화했다. 지식 영역 인용을 **세 갈래**로 가른다.

- **원문 본문** — 2026-04~07 에 사람·이관이 쓴 본문 산문 안의 링크. 관찰자 기여가 아니다.
- **머리말** — 문서 생성 당시 `related_to` 에 적힌 링크. 역시 관찰자 기여가 아니다.
- **집행분** — **본 성찰 계열이 신설한 `## Compiled Truth` · `## Timeline` 안의 링크.** 관찰자 기여다.

측정의 결과가 다음 측정의 입력이 되면 순위는 지식의 중요도가 아니라 집행 이력을 그린다.

- **점수 B** = 미갱신일수 × (1 + 본문 + 머리말 + 집행분). 2026-11-17 까지 쓴 방식.
- **점수 D** = 미갱신일수 × (1 + 본문 + 머리말). 집행분을 뺀 값. **집행 순서는 D 를 따른다(2026-11-18 부터).**

| 인용 출처 | 건수 | 비중 |
| :-- | --: | --: |
| 지식 영역 — 원문 본문 | 10 | 3% |
| 지식 영역 — 머리말 `related_to` | 8 | 3% |
| 지식 영역 — **본 성찰이 쓴 요약·기록 안** | 19 | 7% |
| 자동 생성 목차 | 41 | 14% |
| 본 성찰 계열 자기 인용 | 206 | 71% |
| 그 밖 | 6 | 2% |
| **합계** | **290** | 100% |

## 명단 (점수 D 내림차순, 2026-11-18 기계 재산출)

| # | 문서 | 마지막 갱신 | 미갱신일 | 원문 본문 | 머리말 | 집행분 | 목차 | 자기 인용 | 점수 D | 점수 B |
| --: | :-- | :-- | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | `wiki/concepts/agent-friendly-redesign.md` | 2026-04-29 | 203 | 1 | 2 | 0 | 1 | 0 | 812 | 812 |
| 2 | `wiki/concepts/maximal-knowledge-exactness.md` | 2026-04-29 | 203 | 1 | 1 | 2 | 0 | 3 | 609 | 1015 |
| 3 | `wiki/concepts/token-maxing.md` | 2026-04-29 | 203 | 1 | 1 | 0 | 0 | 0 | 609 | 609 |
| 4 | `wiki/concepts/codegraph-efficiency.md` | 2026-04-29 | 203 | 1 | 0 | 1 | 0 | 2 | 406 | 609 |
| 5 | `wiki/concepts/8-cluster-model.md` | 2026-04-29 | 203 | 1 | 0 | 0 | 1 | 1 | 406 | 406 |
| 6 | `wiki/concepts/digital-unconscious.md` | 2026-04-29 | 203 | 1 | 0 | 0 | 1 | 1 | 406 | 406 |
| 7 | `wiki/concepts/memo-architecture.md` | 2026-04-29 | 203 | 0 | 1 | 0 | 1 | 0 | 406 | 406 |
| 8 | `wiki/frameworks/weak-signal-ansoff.md` | 2026-04-29 | 203 | 0 | 1 | 0 | 1 | 4 | 406 | 406 |
| 9 | `wiki/concepts/eval.md` | 2026-06-27 | 144 | 1 | 0 | 1 | 1 | 4 | 288 | 432 |
| 10 | `wiki/concepts/ai-evaluation-system.md` | 2026-06-27 | 144 | 1 | 0 | 0 | 1 | 2 | 288 | 288 |
| 11 | `wiki/concepts/constructed-fit.md` | 2026-04-29 | 203 | 0 | 0 | 2 | 1 | 0 | 203 | 609 |
| 12 | `wiki/concepts/durable-execution.md` | 2026-04-29 | 203 | 0 | 0 | 2 | 1 | 38 | 203 | 609 |
| 13 | `wiki/protocols/validation-protocol.md` | 2026-04-29 | 203 | 0 | 0 | 2 | 1 | 0 | 203 | 609 |
| 14 | `wiki/concepts/contextual-ingestion.md` | 2026-04-29 | 203 | 0 | 0 | 1 | 1 | 6 | 203 | 406 |
| 15 | `wiki/concepts/gemini-spark.md` | 2026-04-29 | 203 | 0 | 0 | 1 | 1 | 0 | 203 | 406 |
| 16 | `wiki/concepts/meta-harnessing.md` | 2026-04-29 | 203 | 0 | 0 | 1 | 1 | 2 | 203 | 406 |
| 17 | `wiki/signals/talent-market-disruption.md` | 2026-04-29 | 203 | 0 | 0 | 1 | 1 | 1 | 203 | 406 |
| 18 | `wiki/concepts/antigravity-2-0.md` | 2026-04-29 | 203 | 0 | 0 | 0 | 1 | 0 | 203 | 203 |
| 19 | `wiki/concepts/automated-ontology-generation.md` | 2026-04-29 | 203 | 0 | 0 | 0 | 1 | 1 | 203 | 203 |
| 20 | `wiki/concepts/competency-question.md` | 2026-04-29 | 203 | 0 | 0 | 0 | 1 | 1 | 203 | 203 |
| 21 | `wiki/concepts/failed-pattern-trading.md` | 2026-04-29 | 203 | 0 | 0 | 0 | 1 | 0 | 203 | 203 |
| 22 | `wiki/concepts/hermes-pi-philosophy.md` | 2026-04-29 | 203 | 0 | 0 | 0 | 1 | 29 | 203 | 203 |
| 23 | `wiki/concepts/knowledge-synthesis-steps.md` | 2026-04-29 | 203 | 0 | 0 | 0 | 1 | 0 | 203 | 203 |
| 24 | `wiki/concepts/linkedin-agent-automation-20260525.md` | 2026-04-29 | 203 | 0 | 0 | 0 | 1 | 0 | 203 | 203 |
| 25 | `wiki/signals/transportation-ai-pivot.md` | 2026-04-29 | 203 | 0 | 0 | 0 | 1 | 0 | 203 | 203 |
| 26 | `wiki/signals/2026-05-20-google-io-sign-of-agentic-shift.md` | 2026-05-20 | 182 | 0 | 0 | 0 | 1 | 1 | 182 | 182 |
| 27 | `wiki/concepts/context-corpus.md` | 2026-05-21 | 181 | 0 | 0 | 0 | 1 | 1 | 181 | 181 |
| 28 | `wiki/signals/2026-05-30-claude-opus-4-8-detailed-harnessing.md` | 2026-05-30 | 172 | 0 | 0 | 0 | 1 | 2 | 172 | 172 |
| 29 | `wiki/signals/2026-05-30-claude-opus-4-8-launch-and-prompting-shift.md` | 2026-05-30 | 172 | 0 | 0 | 0 | 1 | 2 | 172 | 172 |
| 30 | `wiki/signals/2026-05-30-hs-top-failure-long-strategy.md` | 2026-05-30 | 172 | 0 | 0 | 0 | 1 | 2 | 172 | 172 |
| 31 | `wiki/signals/2026-05-30-josh-kim-ai-native-company-record.md` | 2026-05-30 | 172 | 0 | 0 | 0 | 1 | 2 | 172 | 172 |
| 32 | `wiki/signals/2026-05-30-obelisk-sqlite-durable-execution.md` | 2026-05-30 | 172 | 0 | 0 | 0 | 1 | 1 | 172 | 172 |
| 33 | `wiki/signals/2026-05-30-automated-task-packaging.md` | 2026-05-31 | 171 | 0 | 0 | 1 | 1 | 2 | 171 | 342 |
| 34 | `wiki/concepts/gbrain-personal-ai-os.md` | 2026-05-31 | 171 | 0 | 0 | 0 | 1 | 0 | 171 | 171 |
| 35 | `wiki/signals/2026-05-30-db-schema-knowledge-automation.md` | 2026-05-31 | 171 | 0 | 0 | 0 | 1 | 2 | 171 | 171 |
| 36 | `wiki/signals/2026-05-30-dynamic-workflow-harness.md` | 2026-05-31 | 171 | 0 | 0 | 0 | 1 | 2 | 171 | 171 |
| 37 | `wiki/signals/2026-06-03-logicrag-lazy-graph-reasoning.md` | 2026-06-03 | 168 | 0 | 0 | 0 | 1 | 1 | 168 | 168 |
| 38 | `wiki/signals/2026-06-13-agentic-ta-mainstream-shift.md` | 2026-06-13 | 158 | 0 | 0 | 0 | 1 | 2 | 158 | 158 |
| 39 | `wiki/signals/2026-06-13-hermes-agent-infrastructure-shift.md` | 2026-06-13 | 158 | 0 | 0 | 0 | 1 | 1 | 158 | 158 |
| 40 | `wiki/signals/2026-06-15-agentic-ta-reset.md` | 2026-06-15 | 156 | 0 | 0 | 0 | 1 | 1 | 156 | 156 |
| 41 | `wiki/signals/2026-06-22-agentic-orchestration-shift.md` | 2026-06-22 | 149 | 0 | 0 | 0 | 1 | 1 | 149 | 149 |
| 42 | `wiki/signals/2026-06-25-hr-performance-architect-pivot.md` | 2026-06-25 | 146 | 0 | 0 | 0 | 1 | 1 | 146 | 146 |
| 43 | `wiki/signals/2026-06-27-autonomous-talent-agency-shift.md` | 2026-06-27 | 144 | 0 | 0 | 1 | 1 | 2 | 144 | 288 |
| 44 | `wiki/concepts/graph-rag.md` | 2026-07-02 | 139 | 0 | 0 | 2 | 1 | 1 | 139 | 417 |
| 45 | `wiki/signals/2026-07-06-dawn-of-hr-superagents.md` | 2026-07-06 | 135 | 0 | 0 | 0 | 0 | 2 | 135 | 135 |
| 46 | `wiki/briefings/HR_TECH_PSYCH_2026-07-31.md` | —(날짜 칸 없음) | — | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| 47 | `wiki/concepts/agentic-roi.md` | —(날짜 칸 없음) | — | 1 | 0 | 1 | 0 | 73 | 0 | 0 |
| 48 | `wiki/concepts/aihr-design-framework-tom-sdm.md` | —(날짜 칸 없음) | — | 0 | 0 | 0 | 0 | 2 | 0 | 0 |
| 49 | `wiki/people/duckjung-kim.md` | —(날짜 칸 없음) | — | 0 | 2 | 0 | 0 | 1 | 0 | 0 |
| 50 | `wiki/signals/2026-07-11-deepwiki-post.md` | —(날짜 칸 없음) | — | 0 | 0 | 0 | 0 | 2 | 0 | 0 |
| 51 | `wiki/signals/hr-tech/2026-07-30-agentic-adoption.md` | —(날짜 칸 없음) | — | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| 52 | `wiki/synapse/HR_TECH_PSYCHOLOGY_2026-07-29.md` | —(날짜 칸 없음) | — | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| 53 | `wiki/synapses/IO_PSYCHOLOGY_SYNAPSE_2026-07-30.md` | —(날짜 칸 없음) | — | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 54 | `wiki/tools/deepwiki.md` | —(날짜 칸 없음) | — | 1 | 0 | 0 | 0 | 1 | 0 | 0 |

## 판독 (2026-11-18)

- 전체 **54편**. 지식 영역 인용 37건의 출처는 원문 본문 10 · 머리말 8 · **집행분 19** 다. 즉 **절반이 넘는 인용을 본 성찰이 직접 썼다.** 2026-11-17 성찰은 이 중 1건만 적발했다.
- 집행분을 걷어 내면 지식 영역 인용이 **0 인 문서가 41편**(전체의 76%)이다. 어제 보고한 31편은 집행분을 인용으로 세고 있었다.
- 집행분 19건은 14편의 문서에 걸려 있고, 그 출처는 본 성찰이 요약을 신설한 소수의 문서다 — `knowledge-graph-as-map`(5건) · `2026-05-30-harness-is-not-just-a-leash`(4건) · `agentic-engineering`·`agentic-recruitment-proxy`·`rlm-forge`(각 2건) 등.
- **금일 집행이 다시 엣지를 그렸다.** `skillopt` 의 새 요약이 [[validation-protocol]] 을 인용했고, 그 문서의 집행분은 1 → 2 가 됐다. 점수 D 는 집행분을 세지 않으므로 순위는 움직이지 않았다 — 기준 교체의 효과를 당일에 확인했다.
- 날짜 칸(`updated`)이 없어 나이를 셀 수 없는 문서 **9편**은 점수가 0 으로 깔린다(2026-11-11 적발 결함, 미해소).

## 갱신 규칙

- 집행(요약·기록 신설)이 일어난 날마다 이 명단을 **기계로** 다시 산출한다. 줄어든 편수와 남은 편수를 함께 적는다.
- 인용은 **출처 갈래를 함께** 센다. 갈래를 합쳐 하나의 숫자로 보고하지 않는다.
- 명단에서 문서가 빠지는 경우는 두 가지뿐이다 — ① 이중구조를 갖춤 ② `processed: true` 로 종결 선언. 그 밖의 이유로 사라지면 그것이 사고다.
