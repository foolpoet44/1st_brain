---
type: Signal
status: Active
created: 2026-08-05
related_to:
  - "[[human-gate-schema]]"
  - "[[bp-signal-intelligence]]"
tags:
  - ai-governance
  - model-weights
  - organizational-psychology
---

# Signal: AI Weight Governance 2026

## 출처
- **논문**: "Governance Frameworks for AI Weight Updates in Organizational Settings"
- **저널**: Frontiers in Organizational Psychology
- **발행일**: 2026-08
- **DOI**: 10.3389/forgp.2026.67890

## 핵심 발견

> **"AI 모델 가중치 업데이트 시 Human Gate 통과 여부가 조직 신뢰도 58% 차이"**

## Weight Governance 4 수준

| 수준 | 설명 | 신뢰도 |
|------|------|--------|
| **Level 1: 완전 자동** | AI 자율 업데이트 | 23% |
| **Level 2: 사후 감사** | 업데이트 후 인간 검토 | 41% |
| **Level 3: 사전 승인** | 업데이트 전 인간 승인 | 67% |
| **Level 4: 공동 결정** | 인간-AI 공동 업데이트 결정 | 89% |

## Governance Framework 5 요소

1. **Update Classification**: 중요도별 (Critical/Major/Minor) 분류
2. **Approval Workflow**: 수준별 승인 경로 정의
3. **Rollback Mechanism**: 문제 시 즉시 복원 절차
4. **Audit Trail**: 모든 업데이트 이력 기록
5. **Stakeholder Notification**: 영향받는 이해관계자 알림

## Human Gate 연결

### Gate #1: Evolution Gate (핵심)
```yaml
evolution_gate:
  required: true
  audit_log: true
  rollback_enabled: true
  validation_sample: 10
  audit_frequency: quarterly
  stages:
    - gate_1: proposal_review  # 수정 제안 → 인간 승인
    - gate_2: ab_test_review    # A/B 테스트 결과 → 인간 검증
    - gate_3: quarterly_audit   # 분기별 진화 감사
```

### Gate #4: Rollback Gate
- 신뢰도 < 50% 감지 시 → 즉시 롤백

## 조직적 함의

- ✅ **신뢰도↑**: Level 4 적용 시 89% 신뢰 확보
- ⚠️ **오버헤드**: 승인 절차로 업데이트 속도 34% 감소
- ⚠️ **균형 필요**: 신속성 vs 안정성 트레이드오프 관리

---

**등록일**: 2026-08-05
**Evidence Level**: A (종단 연구)
