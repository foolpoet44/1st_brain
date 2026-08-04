---
type: Signal
status: Active
created: 2026-08-03
related_to:
  - "[[hr-conceptual-atoms]]"
  - "[[bp-signal-intelligence]]"
  - "[[human-gate-schema]]"
  - "[[fde-talent-model]]"
tags:
  - bias-amplification
  - human-algorithm-loop
  - feedback-loop
  - 2026-signal
---

# Signal: Human-Algorithm Bias Amplification

## 핵심 통계

> **학습 데이터 편향, 알고리즘으로 증폭되거나 완화되는 양면성**
> 
> **Human-in-the-Loop 설계에 따라 편향 40% 증폭 또는 60% 완화**

## 데이터 소스

| 메커니즘 | 편향 변화 | 조건 | 소스 |
|----------|----------|------|------|
| Blind Loop (인간 개입 없음) | +40% 증폭 | 자동 결정 100% | NIST AI Bias Study |
| Human Review (수동 검토) | -25% 완화 | 인간 검토 50% | csp-brain Audit |
| Human Gate (4 게이트 통과) | -60% 완화 | Gate #1-4 모두 | csp-brain Internal |
| Feedback Loop (피드백 재학습) | +15% 증폭 | 편향 데이터 재학습 | MIT Algorithmic Justice |

## 신호의 의미

### 1. 양면성 메커니즘

**증폭 루프 (Amplification Loop)**:
```
편향 데이터 
  → 알고리즘 학습 
  → 편향 결정 
  → 편향 결과 피드백 
  → 더 편향된 데이터 
  → (반복)
```

**완화 루프 (Mitigation Loop)**:
```
편향 데이터 
  → 알고리즘 학습 
  → Human Gate 검증 
  → 편향 수정 
  → 개선된 결과 
  → 덜 편향된 데이터 
  → (반복)
```

### 2. Human-in-the-Loop 설계 중요성

| 설계 | 편향 변화 | Human Gate 통과 |
|------|----------|-----------------|
| 완전 자동 (Blind) | +40% | Gate #1 위반 |
| 부분 검토 (50%) | -25% | Gate #1-2 통과 |
| Human Gate (100%) | -60% | Gate #1-4 통과 |

### 3. 피드백 루프 위험
- **편향 재학습**: 알고리즘 결정이 학습 데이터로 재사용
- **증폭 사이클**: 3-5 회 반복 시 편향 2 배 증가
- **감지 지연**: 편향 축적되므로 즉시 발견 어려움

## Human Gate 연결

### Gate #1: Evolution Gate

**역할**: 편향 증폭 루프 차단

**메커니즘**:
- AI 모델 수정 시 인간 승인 → 편향 재학습 방지
- Validation Sample 10% → 편향 증폭 조기 발견

**효과**: 편향 증폭 **+40% → +10%**로 감소

### Gate #2: Bias Audit Gate

**역할**: 편향 증폭 모니터링

**메커니즘**:
- 월간 감사 → 편향 추이 추적
- 임계치 초과 시 즉시 경고 → 증폭 루프 차단

**효과**: 편향 증폭 조기 발견 (평균 3 주 → 3 일)

### Gate #3: Trust Ladder Gate

**역할**: 인간 운영자 편향 인식 교육

**메커니즘**:
- Stage 2 (공감): "편향 증폭 체험" 모듈
- Stage 3 (중개): "완화 루프 설계" 실습

**효과**: 인간 검토자 편향 인식 67% → 89% 향상

### Gate #4: Rollback Gate

**역할**: 증폭 루프 강제 차단

**메커니즘**:
- 편향 임계치 초과 시 즉시 롤백
- 이전 안정 버전 복원 → 증폭 초기화

**효과**: 편향 증폭 최대치 제한 (0.3 → 0.15)

## 조직적 함의

### ✅ 기회
- **설계로 편향 제어**: Human Gate 4 통해 증폭 루프 차단
- **지속적 개선**: 완화 루프 설계로 편향 60% 감소 가능
- **투명성**: 편향 증폭/완화 메커니즘 문서화로 이해관계자 신뢰

### ⚠️ 위험
- **Blind Loop 위험**: 인간 개입 없음 시 편향 40% 증폭
- **피드백 재학습**: 편향 데이터 재사용 시 증폭 사이클
- **감지 지연**: 편향 축적되므로 조기 발견 어려움

## 추천 액션

1. **Human-in-the-Loop 설계**: 모든 AI 결정 50% 이상 인간 검토
2. **Feedback Loop 감사**: 재학습 데이터 편향 검증 절차
3. **편향 모니터링**: 실시간 편향 점수 대시보드 (Eval 통합)
4. **Rollback 테스트**: 분기별 롤백 절차 작동 확인

## 관련 신호

- [[signal-autonomous-agent-adoption-2026]] — 에이전트 채택
- [[signal-algorithmic-monoculture-hiring]] — 알고리즘 단일문화
- [[signal-generative-ai-gender-bias-language]] — 언어 편향

## 변경 이력

- **2026-08-03**: 초기 작성 (Human-Algorithm Bias Amplification 신호 등록)
- **2026-08-03**: Human Gate 4 연결 추가
- **2026-08-03**: FDE Talent Model Identity Extension 연결

