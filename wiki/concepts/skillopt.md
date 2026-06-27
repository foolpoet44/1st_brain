---
title: "SkillOpt (자기 진화형 기술 최적화)"
created: 2026-04-29
updated: 2026-04-29
type: concept
related_to: "[[agentic-engineering]]", "[[knowledge-metabolism]]"
status: Active
tags: [microsoft, optimization, self-evolution, ai-agent]
---

# SkillOpt (자기 진화형 기술 최적화)

> "에이전트의 지능은 고정된 파라미터가 아니라, 끊임없이 수정되는 '기술 문서(.md)'에서 나옵니다."

## 1. 핵심 메커니즘: Behavioral OS의 진화

SkillOpt는 Microsoft 연구진이 제안한 프레임워크로, LLM 자체를 튜닝하는 대신 에이전트에게 주어지는 **'기술 지침(Skill/Prompt)'**을 반복적으로 최적화합니다.

- **Trajectory Analysis**: 에이전트가 업무를 수행한 궤적을 분석합니다.
- **Optimizer Model**: 별도의 '감독관 모델'이 성공과 실패의 원인을 파악합니다.
- **Iterative Refinement**: 지침 문서에서 불필요한 문장은 삭제하고, 성공에 기여한 맥락은 보강합니다.

## 2. HR적 유추: '매뉴얼이 스스로 쓰여지는 조직'

전통적인 조직에서는 사람이 업무 매뉴얼을 업데이트하지만, SkillOpt 환경에서는 **'업무 성과 데이터'가 직접 매뉴얼을 수정**합니다.

- **포터블 역량**: 모델이 바뀌어도(예: GPT -> Claude) 최적화된 `.md` 기술은 그대로 사용 가능합니다. 이는 '핵심 인재의 노하우'를 시스템화하는 과정과 같습니다.

## 3. csp-brain으로의 이식 (Action Plan)

- **SKILL.md 최적화**: 헤르메스가 수행한 작업의 로그를 분석하여, `hermes-agent` 스킬이나 도메인 스킬을 스스로 패치(Patch)하는 워크플로우를 지향합니다.
- **Validation Gate**: 새로운 지침을 적용하기 전, 이전 성과와 비교 검증하는 프로세스를 `_ops/` 내에 구축합니다.
