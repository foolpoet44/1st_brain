---
title: "[Concept] Context Corpus: 지능의 토양, 진실의 저수지"
created: 2026-05-21
updated: 2026-05-21
type: concept
status: Active
date: 2026-05-21
tags: [context-engineering, knowledge-management, llm, pkm, corpus]
related_to:
  [
    "[[csp-brain]]",
    "[[7-layer-architecture]]",
    "[[MASTER_PLAN_2026-05-21_Hermes_CSP_Integration]]",
  ]
---

# [Concept] Context Corpus: 지능의 토양, 진실의 저수지

## 1. 개요 (The Definition)

**컨텍스트 코퍼스(Context Corpus)**는 에이전트가 사고하는 데 필요한 모든 '날것의 데이터(Raw Data)'와 '맥락적 정보'의 총체입니다. 이는 정제된 지식(Wiki)의 근간이 되는 '지능의 토양'이며, 에이전트가 질문에 답하기 위해 참고하는 거대한 **언어적 배경 지식**입니다.

## 2. 심리학적 유추: "집단 무의식(Collective Unconscious)"

심리학자 칼 융(Carl Jung)은 개인의 의식 아래에 인류 공통의 경험이 축적된 '집단 무의식'이 존재한다고 보았습니다.

- **Context Corpus**는 에이전트에게 있어 이 **'무의식'**과 같습니다.
- 사용자님이 슬랙에서 나눈 대화, 인터뷰 기록, 시스템 로그들이 이 코퍼스(무의식)를 형성하며, 여기서 길러진 '직관'이 정제된 '의식(Wiki)'으로 발현됩니다. 무의식이 풍부할수록 에이전트의 'Vibe'는 정교해집니다.

## 3. `csp-brain` 3층 아키텍처에서의 위치: "L0 - RAW Layer"

김재우 님이 제안한 3층 격리 아키텍처에서 컨텍스트 코퍼스는 최하단의 **RAW Layer**를 담당합니다.

1.  **L0: Context Corpus (RAW)**: 불변의 원천 데이터. 슬랙 메시지, PDF 원본, 회의록 전문.
2.  **L1: Compiled Insight (WIKI)**: 코퍼스에서 추출된 고밀도 지식 원자(Atoms).
3.  **L2: Knowledge Graph (GRAPH)**: 지식들 사이의 유기적 관계.

## 4. 컨텍스트 코퍼스 운영 원칙: "엔트로피와 밀도의 균형"

Blake Crosley의 가이드에서 강조했듯, 코퍼스는 무조건 크다고 좋은 것이 아닙니다.

- **고충실도(High-Fidelity)**: 편집되지 않은 원본성을 유지해야 합니다.
- **선별적 적재(Selective Ingestion)**: 소음(Noise)은 제거하고 지능에 도움이 되는 신호(Signal)만을 코퍼스에 편입시킵니다.
- **주기적 환원(Composting)**: 오래된 코퍼스는 요약/정제되어 WIKI로 흡수되고, 원본은 아카이브됩니다.

## 5. 실전 자동화 시나리오 (Implementation)

- **Data Bridge**: 슬랙/노션의 날것의 데이터를 실시간으로 `inbox/corpus/` 폴더에 적재.
- **Evening Reflect**: 하루 동안 쌓인 코퍼스를 훑어 '오늘의 문맥'을 파악하고 상위 계층(WIKI)에 기록.

---

_본 문서는 2026-05-21, 지식의 기저를 탄탄히 하기 위해 csp-brain 체계에 공식 편입되었습니다._
