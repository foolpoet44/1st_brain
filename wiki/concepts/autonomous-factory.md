---
title: Autonomous Factory (자율공장)
created: 2026-10-12
updated: 2026-10-13
type: concept
status: seed
tags: [autonomous-factory, physical-ai, ai-factory, process-knowledge, talent-development]
aliases: [AF, 자율공장, Autonomous Factory]
generated: {by: ai-assisted-ingest, at: 2026-10-12}
evidence: mixed
---

# Autonomous Factory (자율공장)

## Compiled Truth

### 정의 [confirmed]

Autonomous Factory는 **AI가 공장을 대신 운영하는 기술이 아니라, 공정에 대한 지식을 데이터와 모델로 표현하고, 이를 안전하고 검증 가능한 행동으로 전환하며, 실행 결과를 통해 지식과 행동을 지속적으로 갱신하는 시스템**이다. 자율화의 수준은 "사람이 얼마나 빠졌는가"가 아니라 "공정을 얼마나 명시적으로 이해하고, 그 이해로 행동하며, 결과로 교정할 수 있는가"로 본다. (CSP 드라이브 문서, 2026-10-12)

### 핵심 요소 [confirmed]

같은 문서가 밝힌 내용이다.

- **공정 지식**은 매뉴얼의 순서보다 넓다. "이 조건에서 왜 속도를 낮추는가", "어떤 신호가 보이면 불량을 의심하는가", "어디까지 조정해도 안전한가"처럼 현장 판단을 떠받치는 원인·조건·제약의 지식이다. 데이터는 관측 근거, 모델은 조건과 결과의 관계를 표현한다.
- **검증 가능한 행동**은 조정값 제안으로 끝나지 않는다. 왜 그 행동인지, 무엇을 예상하는지, 어느 범위에서 실행할 수 있는지, 실패하면 어떻게 복구하는지가 함께 정의되고, 실행 뒤 예상과 실제의 차이로 지식과 모델을 고친다.
- **다섯 단계 운영체계**: ① 지식의 명시화 → ② 데이터·모델 표현 → ③ 행동 설계 → ④ 검증·실행 → ⑤ 결과 학습.
- **자율성**: 주어진 조건과 권한 안에서 판단·행동하고, 판단이 틀렸을 때 멈추거나 도움을 요청하고 수정할 수 있는 능력.
- **인재육성 함의**: 교육의 중심은 현장의 암묵지를 꺼내고, 모델로 표현하고, 실험으로 검증해, 운영에 연결하는 능력이다. 로봇·AI·디지털트윈은 그 능력의 수단이다.

### 같은 프로그램 [confirmed]

이 문서의 AF(Autonomous Factory)는 `projects/physical-ai-talent` 의 AI Factory 기술전문가 육성(1기 30명), 그리고 AF 오퍼레이션 메타모델(10-08 v0.3 초안, 관찰 중)과 사실상 같은 대상으로 해석한다. (CSP 확인 2026-10-13)

### 해석과 연결 [inferred]

- 자동화가 사람의 손을 빼는 일이라면, 이 정의의 자율화는 사람의 판단 근거를 꺼내 놓는 일이다.
- 멈출 줄 아는 능력을 자율성에 넣은 점은 [[self-determination-theory]]의 자율성이 "통제의 부재"가 아니라 "스스로 승인한 행동"이라는 점과 닮았다.
- 이 인재상은 [[k-smart-model]]의 스마트팩토리 인재론과 [[fde-talent-model]]의 현장 배치형 엔지니어 상이 만나는 지점이다. 같은 "지식을 행동 가능한 단위로 명시화한다"는 논리를 조직 지식에 적용한 것이 [[knowledge-capitalization]]이다.

### 아직 모르는 것 [unknown]

- 이 정의가 사내 공식 정의인지, CSP 개인의 정리인지.
- 다섯 단계 각각에 대응하는 교육 과정이나 평가 기준이 이미 있는지.

---

## Timeline

### 2026-10-12

- Drive 「Autonomous Factory — 공정 지식을 검증 가능한 행동으로 전환하는 시스템」(10-12 생성)에서 신규 편입. 정의 2단(기본 정의 → 학습 순환 포함 정의), 다섯 단계 운영체계, 인재육성 함의, 자율성 정의.
- 연결: [[k-smart-model]] · [[fde-talent-model]] · [[knowledge-capitalization]] · [[self-determination-theory]] · `projects/physical-ai-talent`.

### 2026-10-13 — 인식 상태 표시 적용

- 드라이브 원문이 밝힌 정의·요소·함의는 [confirmed], 비유·이론 연결·프로그램 동일시는 [inferred], 정의의 공식성과 단계별 과정 유무는 [unknown]으로 나눴다. 내용은 삭제하지 않았다.
- 확인 요청: 'AF = AI Factory 육성 프로그램' 동일시가 맞으면 CSP 확인 한 줄로 승격한다.
- CSP 확인 2026-10-13: AF = AI Factory 육성 프로그램 = AF 오퍼레이션 메타모델의 대상 — "사실상 동일하게 해석해도 됨". [inferred] → [confirmed] 승격.
