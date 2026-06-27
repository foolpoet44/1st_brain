---
type: Note
status: Active
related_to: "[[csp-brain]]"
tags: [ai-eval, ax, internal-ip, quality-assurance]
---

# Eval (Evaluation): 지능의 독립 보증서이자 기업의 핵심 IP

**Eval**은 AI 에이전트나 LLM이 내놓은 결과물이 실제 비즈니스 기준에 부합하는지, 안전한지, 정확한지 검증하는 **자동화된 테스트 시스템**입니다. 

## 1. 지위와 역할
전통적인 소프트웨어의 Unit Test가 '1+1=2'의 정합성을 본다면, Eval은 AI의 비결정성(Probabilistic nature)과 환각(Hallucination)을 제어하는 **'지능의 나침반'** 역할을 합니다.

- **품질의 나침반**: 비즈니스 목적, 핵심 가치관, 보안 가이드라인에 부합하는지 측정합니다.
- **독립 보증서 (Vendor Lock-in 방지)**: OpenAI, Anthropic, 혹은 오픈소스 모델로 전환할 때 "과연 예전만큼 잘하는가?"에 대한 객관적 확신을 제공합니다.
- **핵심 지적 자산 (Internal IP)**: "무엇이 우리 회사에 '좋은 답변'인가?"에 대한 기준은 외부 벤더가 아닌 기업 내부의 노하우입니다. Eval Dataset은 이를 계량화하여 축적한 핵심 자산입니다.

## 2. csp-brain에서의 Eval 전략
`csp-brain` 시스템 내에서 Eval은 단순한 검증을 넘어, **'Vibe'를 'Asset'으로 치환하는 공정**입니다.

- **Eval Dataset**: HR 도메인의 전문 지식(8-Cluster Model 등)을 기반으로 한 테스트 케이스 집합.
- **Automated Guardrail**: AI가 생성한 결과물이 `csp-brain`의 철학(에세이형 소통, 심리학적 통찰)을 유지하는지 자동 검정.
- **Model Agnostic**: 특정 모델에 종속되지 않고, 시스템 전체의 '지능적 항상성'을 유지하는 장치.

## 3. 실행 원칙
> "무엇이 옳은지 정의하는 것은 기술이 아니라 사람의 노하우다."

1. **계량화**: 모호한 좋음을 점수(Score)와 근거(Rationale)로 바꾼다.
2. **독립성**: 모델을 바꿔도 테스트 기준(Eval)은 변하지 않아야 한다.
3. **누적**: 매번 발생하는 오류와 교훈을 Eval Dataset에 추가하여 시스템을 더 견고하게 만든다.

---
**관련 문서**: [[csp-brain]], [[8-cluster-model]], [[knowledge-metabolism]]
