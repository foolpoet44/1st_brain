---
title: "Automated Ontology Generation (AOG)"
created: 2026-04-29
updated: 2026-04-29
type: concept
tags: [automation, ontology, knowledge-graph, ai-agents]
status: Active
---

# Automated Ontology G[[Understand-Anything/understand-anything-plu[[Understand-Anything/understand-anything-plugin/skills/understand/frameworks/gin.md|gin]]/skills/understand/locales/en.md|en]]eration (AOG)

## 정의 (Definition)

Automated Ontology Generation (AOG)는 비정형 텍스트(계약서, 정책, 매뉴얼 등)를 기계가 읽고 논리적 추론이 가능한 정형 데이터 구조(OWL/TTL/Knowledge Graph)로 자동 변환하는 프로세스입니다.

## 철학적 유추: 지식의 디지털 트윈 (Digital Twin of Knowledge)

현실 세계의 건축물을 디지털로 복제하여 시뮬레이션하듯, 인간의 머릿속에 있는 '희미한 지식'이나 종이 위의 '죽은 텍스트'를 살아있는 논리 구조로 복제하는 과정입니다. 이는 단순히 정보를 저장하는 것을 넘어, 지식 간의 유기적 관계를 정의함으로써 AI가 스스로 사고할 수 있는 '신경망의 뼈대'를 구축하는 작업과 같습니다.

## 핵심 아키텍처: Multi-Agent LLM Approach

단일 LLM의 일회성 생성 한계를 극복하기 위해 네 가지 특화된 에이전트의 협업 체계를 제안합니다:

1. **Domain Expert (전문가)**: 텍스트에서 핵심 의미(Semantic Requirements)를 추출.
2. **Manager (관리자)**: 추출된 의미를 온톨로지 설계 패턴(ODPs)에 맞게 구조화 및 계획 수립.
3. **Coder (코더)**: 실제 코드(RDF/Turtle)로 구현.
4. **Quality Assurer (QA)**: 구문 및 의미론적 일관성 검증.

## HR 도메인 적용 시나리오

- **정책 자동 답변**: 취업규칙이나 복리후생 규정을 온톨로지화하여 100% 신뢰할 수 있는 답변 생성.
- **역량-직무 매핑**: 심리 지표(8-Cluster 등)와 직무 요구사항 간의 복잡한 상관관계를 논리적으로 구조화.
- **감사 및 추적성**: AI의 답변이 어떤 규정의 어떤 논리에 근거했는지 투명하게 증명 가능.

## 참조 (References)

- Source: `Towards Automated Ontology Generation from Unst[[Understand-Anything/understand-anything-plugin/skills/understand/locales/ru.md|ru]]ctured Text: A Multi-Agent LLM Approach` (2025)
- Path: `/Users/dkmac/Desktop/@26/hermes/automated_ontology_generation.pdf`
