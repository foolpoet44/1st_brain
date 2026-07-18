---
title: EX Insight Mining Pipeline (귀납 × 연역 교차 분석 엔진)
created: 2026-07-18
updated: 2026-07-18
type: concept
status: seed
tags: [ex, nlp, clustering, phenomenology, weak-signal, triage]
aliases: [EX 인사이트 마이닝, Insight Mining Pipeline]
---

# EX Insight Mining Pipeline (귀납 × 연역 교차 분석 엔진)

## Compiled Truth

EX Insight Mining Pipeline은 [[bp-signal-intelligence]]의 **Triage 모듈로 끼워지는 텍스트 인사이트 발굴 엔진**이다. 독립 산출물이 아니라, 상태 기계에서 신호가 verifying → triaged로 넘어갈 때 Triage 에이전트가 호출해 클러스터·티어·프레임워크 메타·인과 간선을 산출한다. 목표는 단어를 세는 빈도 분석이 아니라, 직원의 언어(summary·opinions) 속에 응결된 경험을 다시 살아있는 의미로 풀어내는 것이다.

세 개의 인식론적 기둥 위에 선다. (1) **현상학적 귀납** — Husserl의 epoché처럼 분석자의 이론적 선입견을 괄호 치고, 임베딩 공간의 코사인 거리로 의미 구조가 스스로 떠오르게 한다. (2) **귀납–연역 교차검증** — 데이터가 발견한 클러스터와 조직심리 이론의 격자를 겹쳐, 발견이 해석을 만나고 해석이 발견을 검증한다. (3) **약신호 우선** — 빈도 분석은 과거(자주 나온 것)를 보지만, [[weak-signal-theory]] Ansoff는 정반대로 드물지만 의미적으로 새로운 신호를 미래의 강신호 후보로 건진다.

여섯 단계는 하나의 하강이다 — 표면의 빈도에서 의미로, 의미에서 구조로, 구조에서 시간과 대조로. ① 귀납 클러스터링(embedding→UMAP→HDBSCAN, 클러스터 수를 미리 정하지 않아 '몇 개로 나눌까'라는 선입견 자체를 제거, 노이즈는 약신호 후보로), ② 연역 프레임워크 평정(SDT/LMX/POS/JD-R 각 0~1 연속값 + evidence·rationale 강제), ③ **교차 매핑**(이 엔진의 핵심 — 각 신호가 귀납 좌표와 연역 좌표 둘을 갖고, 표면 단어 '퇴사'가 의미 구조로는 '과부하'임을 드러냄), ④ 인과 사슬 추출('인력 공백→실무 90%→소진→이탈'을 causal 간선으로), ⑤ 약신호 신규성 탐지(기존 분포에서 동떨어진 점), ⑥ **Positive Deviance 대조**(위험군만 보면 경보기로 전락하므로, 건강한 조직의 언어에서 처방의 마커를 읽는다 — 감시에서 돌봄으로).

**표본에 대한 정직한 전제**: 49건은 통계적 토픽 모델링에 작다. 현 단계 주력은 LLM 질적 코딩 + 임베딩 이웃 탐색이고 클러스터는 '확정'이 아닌 '가설'이다. 데이터가 수백 건이면 BERTopic으로 EX 8-클러스터 통제어휘를 확정하고, 수천 건이면 시계열 담론 진화 분석이 합류한다. 파이프라인을 먼저 깔고 데이터가 차오를수록 기법이 깊어지는 구조 — 조직 이니셔티브를 미래 SaaS의 PoC로 다루는 CSP 방식 그대로다. EX 8-클러스터는 top-down 보편 온톨로지가 아니라 3-레이어(Energy&Survival / Direction&Meaning / Relationship&Trust)에 bottom-up으로 귀속된다.

---

## Timeline

### 2026-07-18

- Drive 설계문서에서 편입: **EX Insight Mining Pipeline 설계서**.
- [[bp-signal-intelligence]]의 Triage 에이전트(§4.3)가 호출하는 분석 엔진으로 자리매김.
- 6단계: 귀납 클러스터링 → 연역 평정 → 교차 매핑 → 인과 추출 → 신규성 탐지 → PD 대조.
- 기술 스택: pgvector 임베딩 + UMAP + HDBSCAN + LLM 구조화 평정 + Supabase(jsonb·signal_edges·ex_insights).
- 심리 프레임워크 4렌즈(SDT/LMX/POS/JD-R)로 원시 언어를 조직적 의미로 변환 — [[data-sensing]] 아키텍처와 정합.
- 소표본 정직성: 클러스터는 가설, 사람 검토 게이트 필수. 데이터 규모별 진화 로드맵 내장.
