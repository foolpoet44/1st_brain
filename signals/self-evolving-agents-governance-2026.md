---
type: Signal
status: Active
created: 2026-08-05
related_to:
  - "[[human-gate-schema]]"
  - "[[agentic-recruitment-proxy]]"
tags:
  - self-evolving-agents
  - ai-governance
  - arxiv-2507-21046
---

# Signal: Self-Evolving Agents Governance 2026

## 출처
- 논문: Governance Frameworks for Self-Evolving AI Agents in Organizations
- arXiv: 2507.21046
- 발행일: 2025-07 (2026 년 업데이트)
- 저널: AI Safety and Governance Journal

## 핵심 발견

Self-Evolving Agent 의 분기별 Human Gate 감사가 catastrophic failure 94 percent 방지

## Self-Evolution 3 수준

| 수준 | 설명 | 위험도 | Human Gate 필요성 |
|------|------|--------|-----------------|
| Level 1: Parameter Tuning | 하이퍼파라미터 자동 조정 | 낮음 | Gate 1 (승인) |
| Level 2: Architecture Search | 모델 구조 자동 탐색 | 중간 | Gate 1-2 (승인+검증) |
| Level 3: Goal Rewriting | 목적 함수 자동 수정 | 높음 | Gate 1-4 (전체) |

## Governance Framework 6 요소

1. Evolution Boundary: 자기진화 허용 범위 명시
2. Pre-Commitment Review: 진화 전 인간 승인 (Gate 1)
3. A/B Testing: 진화 후 A/B 테스트 (Gate 2)
4. Quarterly Audit: 분기별 종합 감사 (Gate 3)
5. Emergency Rollback: 즉시 롤백 권한 (Gate 4)
6. Evolution Log: 모든 진화 이력 기록

## Human Gate 4 명세

evolution_gate:
  required: true
  audit_log: true
  rollback_enabled: true
  validation_sample: 10
  audit_frequency: quarterly
  stages:
    - gate_1: proposal_review
    - gate_2: ab_test_review
    - gate_3: quarterly_audit

## 조직적 함의

- 재난 방지: catastrophic failure 94 percent 감소
- 오버헤드: 분기별 감사로 운영 비용 12 percent 증가
- 균형: 혁신 속도 vs 안전성 트레이드오프 관리

등록일: 2026-08-05
Evidence Level: A (시뮬레이션 + 사례 연구)
