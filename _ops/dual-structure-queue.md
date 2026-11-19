---
title: 이중구조 결손 명단 — 요약·기록 둘 다 없는 위키 문서
created: 2026-11-16
updated: 2026-11-19
type: ops
status: Active
generated:
  by: ai-assisted-ingest
  at: 2026-11-19
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
| 2026-11-18 | `wiki/concepts/skillopt.md` | **점수 D 1위**(집행분까지 제외) | 55 → 54 |
| 2026-11-19 | `wiki/concepts/agent-friendly-redesign.md` | 점수 D 1위 (816) — **저장된 도구 `_ops/scripts/ledger.py` 로 산출** | 54 → **53** |

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

## 명단 (점수 D 내림차순, 2026-11-19 `_ops/scripts/ledger.py` 산출)

> **2026-11-19 부터 이 표는 손이 아니라 저장된 도구가 만든다.** `python3 _ops/scripts/ledger.py --date YYYY-MM-DD`
> 모집단·인용을 세는 자리·검색어가 전부 그 파일 안에 주석과 함께 있다. 정의를 바꾸려면 파일을 고치고, 고친 사실을 그날 성찰에 적는다.

| # | 문서 | 마지막 갱신 | 미갱신일 | 본문 | 머리말 | 집행분 | 점수 D | 점수 B |
| --: | :-- | :-- | --: | --: | --: | --: | --: | --: |
| 1 | `wiki/concepts/maximal-knowledge-exactness.md` | 2026-04-29 | 204 | 1 | 1 | 2 | 612 | 1020 |
| 2 | `wiki/concepts/token-maxing.md` | 2026-04-29 | 204 | 1 | 1 | 0 | 612 | 612 |
| 3 | `wiki/concepts/8-cluster-model.md` | 2026-04-29 | 204 | 1 | 0 | 0 | 408 | 408 |
| 4 | `wiki/concepts/codegraph-efficiency.md` | 2026-04-29 | 204 | 1 | 0 | 1 | 408 | 612 |
| 5 | `wiki/concepts/digital-unconscious.md` | 2026-04-29 | 204 | 1 | 0 | 0 | 408 | 408 |
| 6 | `wiki/concepts/memo-architecture.md` | 2026-04-29 | 204 | 0 | 1 | 0 | 408 | 408 |
| 7 | `wiki/concepts/ai-evaluation-system.md` | 2026-06-27 | 145 | 1 | 0 | 0 | 290 | 290 |
| 8 | `wiki/concepts/eval.md` | 2026-06-27 | 145 | 1 | 0 | 1 | 290 | 435 |
| 9 | `wiki/concepts/antigravity-2-0.md` | 2026-04-29 | 204 | 0 | 0 | 0 | 204 | 204 |
| 10 | `wiki/concepts/automated-ontology-generation.md` | 2026-04-29 | 204 | 0 | 0 | 0 | 204 | 204 |
| 11 | `wiki/concepts/competency-question.md` | 2026-04-29 | 204 | 0 | 0 | 0 | 204 | 204 |
| 12 | `wiki/concepts/constructed-fit.md` | 2026-04-29 | 204 | 0 | 0 | 3 | 204 | 816 |
| 13 | `wiki/concepts/contextual-ingestion.md` | 2026-04-29 | 204 | 0 | 0 | 1 | 204 | 408 |
| 14 | `wiki/concepts/durable-execution.md` | 2026-04-29 | 204 | 0 | 0 | 3 | 204 | 816 |
| 15 | `wiki/concepts/failed-pattern-trading.md` | 2026-04-29 | 204 | 0 | 0 | 0 | 204 | 204 |
| 16 | `wiki/concepts/gemini-spark.md` | 2026-04-29 | 204 | 0 | 0 | 1 | 204 | 408 |
| 17 | `wiki/concepts/hermes-pi-philosophy.md` | 2026-04-29 | 204 | 0 | 0 | 0 | 204 | 204 |
| 18 | `wiki/concepts/knowledge-synthesis-steps.md` | 2026-04-29 | 204 | 0 | 0 | 0 | 204 | 204 |
| 19 | `wiki/concepts/linkedin-agent-automation-20260525.md` | 2026-04-29 | 204 | 0 | 0 | 1 | 204 | 408 |
| 20 | `wiki/concepts/meta-harnessing.md` | 2026-04-29 | 204 | 0 | 0 | 1 | 204 | 408 |
| 21 | `wiki/frameworks/weak-signal-ansoff.md` | 2026-04-29 | 204 | 0 | 0 | 0 | 204 | 204 |
| 22 | `wiki/protocols/validation-protocol.md` | 2026-04-29 | 204 | 0 | 0 | 4 | 204 | 1020 |
| 23 | `wiki/signals/talent-market-disruption.md` | 2026-04-29 | 204 | 0 | 0 | 3 | 204 | 816 |
| 24 | `wiki/signals/transportation-ai-pivot.md` | 2026-04-29 | 204 | 0 | 0 | 0 | 204 | 204 |
| 25 | `wiki/signals/2026-05-20-google-io-sign-of-agentic-shift.md` | 2026-05-20 | 183 | 0 | 0 | 0 | 183 | 183 |
| 26 | `wiki/concepts/context-corpus.md` | 2026-05-21 | 182 | 0 | 0 | 0 | 182 | 182 |
| 27 | `wiki/signals/2026-05-30-claude-opus-4-8-detailed-harnessing.md` | 2026-05-30 | 173 | 0 | 0 | 0 | 173 | 173 |
| 28 | `wiki/signals/2026-05-30-claude-opus-4-8-launch-and-prompting-shift.md` | 2026-05-30 | 173 | 0 | 0 | 0 | 173 | 173 |
| 29 | `wiki/signals/2026-05-30-hs-top-failure-long-strategy.md` | 2026-05-30 | 173 | 0 | 0 | 0 | 173 | 173 |
| 30 | `wiki/signals/2026-05-30-josh-kim-ai-native-company-record.md` | 2026-05-30 | 173 | 0 | 0 | 0 | 173 | 173 |
| 31 | `wiki/signals/2026-05-30-obelisk-sqlite-durable-execution.md` | 2026-05-30 | 173 | 0 | 0 | 0 | 173 | 173 |
| 32 | `wiki/concepts/gbrain-personal-ai-os.md` | 2026-05-31 | 172 | 0 | 0 | 0 | 172 | 172 |
| 33 | `wiki/signals/2026-05-30-automated-task-packaging.md` | 2026-05-31 | 172 | 0 | 0 | 1 | 172 | 344 |
| 34 | `wiki/signals/2026-05-30-db-schema-knowledge-automation.md` | 2026-05-31 | 172 | 0 | 0 | 0 | 172 | 172 |
| 35 | `wiki/signals/2026-05-30-dynamic-workflow-harness.md` | 2026-05-31 | 172 | 0 | 0 | 0 | 172 | 172 |
| 36 | `wiki/signals/2026-06-03-logicrag-lazy-graph-reasoning.md` | 2026-06-03 | 169 | 0 | 0 | 0 | 169 | 169 |
| 37 | `wiki/signals/2026-06-13-agentic-ta-mainstream-shift.md` | 2026-06-13 | 159 | 0 | 0 | 0 | 159 | 159 |
| 38 | `wiki/signals/2026-06-13-hermes-agent-infrastructure-shift.md` | 2026-06-13 | 159 | 0 | 0 | 0 | 159 | 159 |
| 39 | `wiki/signals/2026-06-15-agentic-ta-reset.md` | 2026-06-15 | 157 | 0 | 0 | 0 | 157 | 157 |
| 40 | `wiki/signals/2026-06-22-agentic-orchestration-shift.md` | 2026-06-22 | 150 | 0 | 0 | 0 | 150 | 150 |
| 41 | `wiki/signals/2026-06-25-hr-performance-architect-pivot.md` | 2026-06-25 | 147 | 0 | 0 | 0 | 147 | 147 |
| 42 | `wiki/signals/2026-06-27-autonomous-talent-agency-shift.md` | 2026-06-27 | 145 | 0 | 0 | 2 | 145 | 435 |
| 43 | `wiki/concepts/graph-rag.md` | 2026-07-02 | 140 | 0 | 0 | 2 | 140 | 420 |
| 44 | `wiki/signals/2026-07-06-dawn-of-hr-superagents.md` | 2026-07-06 | 136 | 0 | 0 | 0 | 136 | 136 |
| 45 | `wiki/briefings/HR_TECH_PSYCH_2026-07-31.md` | — | — | 0 | 0 | 0 | 0 | 0 |
| 46 | `wiki/concepts/agentic-roi.md` | — | — | 1 | 0 | 1 | 0 | 0 |
| 47 | `wiki/concepts/aihr-design-framework-tom-sdm.md` | — | — | 0 | 0 | 0 | 0 | 0 |
| 48 | `wiki/people/duckjung-kim.md` | — | — | 0 | 2 | 0 | 0 | 0 |
| 49 | `wiki/signals/2026-07-11-deepwiki-post.md` | — | — | 0 | 0 | 0 | 0 | 0 |
| 50 | `wiki/signals/hr-tech/2026-07-30-agentic-adoption.md` | — | — | 0 | 0 | 0 | 0 | 0 |
| 51 | `wiki/synapse/HR_TECH_PSYCHOLOGY_2026-07-29.md` | — | — | 0 | 0 | 0 | 0 | 0 |
| 52 | `wiki/synapses/IO_PSYCHOLOGY_SYNAPSE_2026-07-30.md` | — | — | 0 | 0 | 0 | 0 | 0 |
| 53 | `wiki/tools/deepwiki.md` | — | — | 1 | 0 | 0 | 0 | 0 |

합계: 본문 9 · 머리말 5 · 집행분 27 · 지식 인용 0편 42/53

## 판독 (2026-11-19)

- 전체 **53편**. 지식 영역 인용은 원문 본문 9 · 머리말 5 · 집행분 27 이다. 집행분을 걷어 내면 지식 인용이 **0 인 문서가 42편**(전체의 79%)이다.
- **같은 줄이 세 값으로 산출됐다.** 「머리말 인용」 합계는 2026-11-18 자 표에 8, 금일 범위를 저장소 전체로 잡은 1차 집계에서 10, 위키로 한정한 저장 도구에서 7(집행 전) 이었다. 숫자가 흔들린 것이 아니라 **모집단 정의가 저장되지 않아 매일 다시 만들어졌다.** 2026-11-19 부터 정의는 `ledger.py` 에 고정된다.
- 금일 집행도 엣지를 그렸다. 새 요약이 결손 문서 3편을 인용해 집행분이 23 → 27 로 늘었다. 점수 D 는 집행분을 세지 않으므로 **순위 변동 0** — 기준 교체의 효과가 이틀째 확인됐다.
- 날짜 칸(`updated`)이 없어 나이를 셀 수 없는 문서 **9편**은 점수가 0 으로 깔린다(2026-11-11 적발 결함, 미해소).

## 갱신 규칙

- 집행(요약·기록 신설)이 일어난 날마다 이 명단을 **저장된 도구(`_ops/scripts/ledger.py`)로** 다시 산출한다. 세션 안에서 즉석으로 만든 집계로 이 표를 갱신하지 않는다. 줄어든 편수와 남은 편수를 함께 적는다.
- 인용은 **출처 갈래를 함께** 센다. 갈래를 합쳐 하나의 숫자로 보고하지 않는다.
- 명단에서 문서가 빠지는 경우는 두 가지뿐이다 — ① 이중구조를 갖춤 ② `processed: true` 로 종결 선언. 그 밖의 이유로 사라지면 그것이 사고다.
