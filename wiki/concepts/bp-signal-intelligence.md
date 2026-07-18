---
title: BP Signal Intelligence (신호 생애주기 상태 기계)
created: 2026-07-18
updated: 2026-07-18
type: concept
status: seed
tags: [ex, signal, state-machine, claude-code, supabase, people-context-graph]
aliases: [BP 신호 인텔리전스, Signal Lifecycle State Machine]
---

# BP Signal Intelligence (신호 생애주기 상태 기계)

## Compiled Truth

BP Signal Intelligence는 [[ex-intelligence]]의 Relation Verification 층을 정적 아카이브에서 살아있는 파이프라인으로 전환하는 운영 아키텍처다. 진단의 출발점은 뼈아프다 — BP(Business Partner) 아카이브의 신호 49건이 전부 '접수' 상태에 정체되어 있어, 시스템이 설계 의도였던 *active signal verifier*가 아니라 *passive reporter*에 머물러 있다는 것이다.

핵심 설계 사상은 **"status = work queue"**다. 신호의 현재 상태가 곧 '어느 에이전트를 깨울 것인가'를 결정하므로 별도 오케스트레이터가 필요 없다. 상태 자체가 라우터다. 신호는 `접수(received) → 검증(verifying) → 분류(triaged) → 조치(acting) → 종결(closed)` 다섯 칸을 반드시 흘러가며, 신뢰도 D는 `반려(rejected)` 루프로 접수에 환류된다. 이 반려 루프가 BP를 passive reporter에서 active verifier로 강제 전환시키는 장치다 — 해석·근거 없는 단발 보고는 통과하지 못한다.

시스템은 세 층의 회로다. (1) **신호 생애주기 상태 기계**가 무엇을 할 차례인지 정의하고, (2) **Claude Code 멀티에이전트 런타임**(각 상태 칸을 지키는 문지기 — Ingest·Verifier·Triage·Graph·Digest 5+1 서브에이전트, tmux 24/7 폴링/webhook)이 실행하며, (3) **People Context Graph**(persons·orgs·ex_clusters·signal_edges)가 결과를 시간축에 누적한다. 동일 인물에 critical·alert가 누적되면 [[weak-signal-theory]]의 약신호 증폭 경보가 켜진다 — 개별로는 일회성 면담이나 누적되면 강신호다.

두 가지 윤리적 못이 박혀 있다. 첫째, **사람이 지키는 칸은 단 하나(조치)** — 사람에 대한 신호를 다루는 시스템에서 마지막 개입 판단을 기계에 넘기면 EX Intelligence는 돌봄이 아니라 감시로 변질된다. 둘째, **모든 질적 판단은 감사 가능해야 한다** — 신뢰도·클러스터 판정 근거를 PostToolUse hook으로 JSONL과 `status_transitions.reason`에 남긴다. `received → acting` 경과 시간이 곧 **time-to-action** KPI이며, 지금은 모두 접수에 멈춰 측정조차 불가능하다.

분류(Triage) 단계의 분석 엔진은 [[ex-insight-mining-pipeline]]이 담당하고, 개인 노드의 성향(Disposition) 속성은 [[opq-framework]]의 UCF×Leader Edge 산출이 선행 소스로 채운다. 상위 로드맵과 정렬: Phase 0–1(스키마·49건 정제)=Q2, Phase 2–3(에이전트·그래프)=Q3, Phase 4(관측)=Q4.

**핵심 판단**: 이것은 데이터 정제 프로젝트가 아니라 *입력 단계의 마찰 설계*다. `target` 자유텍스트 27종을 `person_id`로 정규화하는 단일 결정점이 개인 레벨 그래프의 구조적 갭을 메운다. 살아있는 파이프라인은 데이터를 한 번 청소하는 대신, 청소되지 않은 데이터가 애초에 흘러가지 못하게 막는다.

---

## Timeline

### 2026-07-18

- Drive 설계문서에서 편입: **BP Signal Intelligence 운영 시스템 개발 명세서**.
- status = work queue: 신호 상태가 곧 라우터. 5+1 Claude Code 서브에이전트가 각 상태 칸의 문지기.
- 상태 기계: 접수→검증→분류→조치→종결 + 반려 루프(신뢰도 D 환류). 조치 칸만 사람이 지킴(감시 아닌 돌봄).
- Supabase 스키마: `signal_status` enum, `reliability_grade`(A–D), `action_tier`(watch/alert/critical), persons·orgs·ex_clusters 마스터, signal_edges 그래프, status_transitions 로그.
- People Context Graph에서 동일 인물 누적 신호로 약신호 증폭 감지([[weak-signal-theory]] Ansoff).
- 감사 가능성: PostToolUse hook → JSONL, swim-lane 대시보드. Triage 엔진은 [[ex-insight-mining-pipeline]]이 수행.
