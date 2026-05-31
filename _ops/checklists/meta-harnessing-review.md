---
type: Checklist
category: AI-Ops
tags: ["validation", "verification", "harnessing", "optimization-bias"]
---

# Meta-Harnessing Review: Anti-Optimism Bias Checklist

> "AI는 본능적으로 '할 수 있다'고 말하지만, 인프라는 냉정하게 '되어야 한다'고 답해야 합니다."

## 1. 결과물 정합성 검증 (Self-Verification)

- [ ] 에이전트가 제시한 해결책이 기존 시스템의 다른 스킬과 충돌하지 않는가?
- [ ] "성공했습니다"라는 보고의 물리적 증거(파일 생성, API 응답 로그)가 확인되었는가?
- [ ] 예외 상황(Error Handling)에 대한 고려가 생략되지 않았는가?

## 2. 인지적 편향 제거

- [ ] **Anti-Optimism Check**: 가장 낙관적인 시나리오가 아닌, 최악의 시나리오에서도 시스템이 내구성을 갖는가?
- [ ] **Literal Interpretation**: 지시사항을 자의적으로 해석하여 빠뜨린 제약 조건은 없는가?

## 3. 효율성 점검

- [ ] 불필요하게 높은 Effort(토큰 낭비)가 투입되지는 않았는가?
- [ ] Resolver가 최적의 파일을 선택했는가?
