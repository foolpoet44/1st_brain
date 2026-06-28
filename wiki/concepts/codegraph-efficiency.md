---
type: Concept
related_to: "[[knowledge-graph-as-map]]", "[[maximal-knowledge-exactness]]"
status: Active
tags: [indexing, cost-efficiency, codegraph, token-optimization]
---

# CodeGraph Efficiency (지능적 인덱싱과 비용 효율성)

> "관계를 선행 학습한 에이전트는 무모하게 파일을 뒤지지 않습니다. 지도(Graph)가 있다면 토큰 비용은 절반으로 줄어듭니다."

## 1. 핵심 가치: 시맨틱 내비게이션

CodeGraph는 코드베이스나 지식 저장소를 '지식 그래프'로 미리 인덱싱하여, 에이전트가 불필요한 데이터를 탐색하는 데 지출하는 토큰 비용을 최소화합니다.

- **토큰 감소 (-57%)**: 전체 텍스트가 아닌, 관계가 입증된 경로(Path)만 문맥으로 로드함.
- **속도 향상 (+46%)**: 무작위 검색(Grep/Search) 대신 그래프 쿼리를 통해 즉시 타겟 노드에 도달함.

## 2. csp-brain 적용 원칙: 'Lean Thinking'

에이전트가 방대한 데이터를 다룰 때 다음의 **'인덱스 우선 전략'**을 취해야 함.

- **Pre-indexing**: 새로운 지식이 들어오면 즉시 다른 노드와의 관계(Edge)를 정의하여 나중에 검색 비용을 줄임.
- **Chain of Evidence**: 질문에 답하기 위해 필요한 '최소한의 노드 집합'만 로드함.

## 3. HR 운영에의 함의

- 대규모 인사 데이터나 사규집을 분석할 때, 모든 페이지를 읽는 대신 인덱싱된 관계를 통해 **'핵심 조항과 관련 판례'**만 즉시 연결하는 아키텍처로 진화해야 함.
