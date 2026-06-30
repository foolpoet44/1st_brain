---
title: "MEMO (Memory as a Model)"
created: 2026-04-29
updated: 2026-04-29
type: concept
status: Active
related_to: "[[llm-knowledge-base]]", "[[ax-internalization]]"
---

# MEMO (Memory as a Model)

## 개념 정의

전통적인 RAG(Retrieval-Augmented Generation)가 외부 벡터 DB에서 문서 조각을 찾아오는 '도서관 사서' 방식이라면, MEMO는 지식을 가중치 파라미터 내에 직접 암기한 **'소형 지식 비서 모델(sLM)'**을 메인 LLM 옆에 두는 방식입니다.

## 핵심 메커니즘

- **Memory as a Model**: 1.5B~14B 체급의 소형 모델을 특정 지식 코퍼스로 SFT 학습시켜 '암기 전문가'로 만듭니다.
- **Natural Language Interview**: 메인 모델(Executive)은 외부 DB를 검색하는 대신, 이 비서 모델에게 자연어로 질문을 던지며 지식을 캐냅니다.
- **Anti-Catastrophic Forgetting**: 메인 모델의 가중치는 건드리지 않으므로 기존 성능을 유지하면서 새로운 지식만 유연하게 결합할 수 있습니다.

## 성능상 우위

- **NarrativeQA**: 기존 Graph RAG 대비 2배 이상의 추론 성능 (53.58% vs 23.21%).
- **Noise Resilience**: 무관한 데이터가 섞여도 정답률 하락이 미미(0.55% 내외)하여 극강의 맷집을 보여줌.

## HR 및 Vibe Coding 관점의 유유

조직 내에 '규정집(Vector DB)'을 비치해두는 것과, 그 규정을 완벽하게 숙지하고 있는 '베테랑 담당자(MEMO 모델)'를 바로 옆에 앉혀두는 것의 차이입니다. 단순 참조를 넘어 맥락적 추론이 필요한 사내 전략이나 복잡한 인사 제도 상담에 최적화된 아키텍처입니다.

---

_Source: 염기웅 LinkedIn (Original Paper: "MEMO: Memory as a Model")_
_Last Updated: {now}_
