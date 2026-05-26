---
title: GraphRAG (Graph-based Retrieval-Augmented Generation)
created: 2026-05-26
type: concept
tags: [ai, rag, graph-theory, knowledge-management, pulse]
related_to: "[[csp-brain-system]], [[knowledge-capitalization]]"
---

# GraphRAG: 지식의 신경망과 다차원 추론

## 개요
GraphRAG는 전통적인 벡터 기반 RAG의 한계를 극복하기 위해 지식 그래프(Knowledge Graph)의 구조적 정보와 LLM의 추론 능력을 결합한 최신 기술입니다. 정보를 단순한 텍스트 덩어리가 아닌, **노드(개념)**와 **엣지(관계)**의 네트워크로 파악합니다.

## 핵심 메커니즘
1. **Entity Extraction**: 텍스트에서 주요 개념(사람, 조직, 개념, 사건 등)을 추출합니다.
2. **Relationship Mapping**: 추출된 엔티티 간의 관계를 정의하고 선으로 연결합니다.
3. **Community Detection**: 그래프 알고리즘을 통해 밀접하게 연결된 지식 군집(Community)을 발견합니다.
4. **Hierarchical Summarization**: 군집별로 요약문을 생성하여 상위 수준의 맥락을 확보합니다. (예: RAPTOR 방식)

## CSP Brain v2.0에서의 의미 (Knowledge Pulse)
- **맥락적 연결**: "회복 탄력성"이라는 키워드 검색 시, 단순히 해당 단어가 포함된 문서를 찾는 것이 아니라, "스트레스 관리", "조직 문화", "심리학적 안전감"과의 거리와 관계를 추론할 수 있게 합니다.
- **나이테(Growth Rings)의 구현**: 새로운 지식이 들어올 때 기존 노드들과 어떻게 결합되는지 실시간으로 시각화하여 지식의 '대사(Metabolism)' 과정을 보여줍니다.
- **고차원 질문 대응**: "우리 조직의 HR 전략은 최근 3개월간 어떻게 진화했는가?"와 같은 거시적이고 시계열적인 질문에 대해 그래프 군집 요약을 통해 답할 수 있습니다.

## 주요 연구 흐름 (2026 기준)
- **Microsoft GraphRAG**: 전역적 요약(Global Summarization)에 강점.
- **LightRAG**: 그래프 구조 최적화를 통한 실시간 지식 갱신 특화.
- **HippoRAG**: 해마(Hippocampus)의 기억 원리를 모방한 연상 검색.

---
_참조: https://wikidocs.net/book/19813_
