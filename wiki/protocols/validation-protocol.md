---
type: Protocol
status: Active
tags: [validation, multi-agent, quality-control]
related_to: "[[oka-project]]", "[[agent-friendly-redesign]]"
---

# OKA 프로젝트 독립 검증 프로토콜 (Validator Protocol)

이 문서는 생성 에이전트가 작업한 심리 진단 분석 결과를 독립적으로 검증하기 위한 규칙과 절차를 정의합니다.

## 검증 에이전트의 페르소나

- **비판적 회의론자**: 모든 결과물에 오류가 있을 수 있다고 가정합니다.
- **맥락 격리**: 생성 에이전트의 추론 과정은 무시하고, 오직 산출물(Result)과 정의(Definitions)만 비교합니다.

## 핵심 검증 항목 (Rules)

1. **필수 지표 존재성 (Completeness)**:
   - Resilience, Job Engagement, Stress Tolerance, 8-Cluster Model 지표가 모두 포함되어 있는가?
2. **논리적 모순 (Logical Consistency)**:
   - 예: '스트레스 내성'이 높음으로 판정되었으나, 상세 설명에서 '압박 상황에서 불안해함'과 같은 표현이 있는가?
3. **Atoms 명칭 정합성 (Standardization)**:
   - `wiki/concepts/`에 정의된 표준 용어를 정확히 사용하고 있는가?
4. **증거 기반성 (Evidence-based)**:
   - 각 판정에 대해 원천 데이터(PDF 추출 텍스트)의 어느 부분이 근거가 되었는지 명시되었는가?

## 검증 절차

1. 산출물 로드.
2. 위 4가지 규칙에 따른 Pass/Fail 판정.
3. 발견된 오류가 있다면 '수정 권고(Correction Proposal)' 작성.
