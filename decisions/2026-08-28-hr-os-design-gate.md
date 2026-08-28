---
type: Decision
status: Approved
created: 2026-08-28
related_to: "[[HR OS — Product Definition v0.2]]"
tags:
  - design-gate
  - hr-os
  - baseline
---

# Design Gate 결정 기록 — HR OS v0.2

> **결정일**: 2026-08-28  
> **결정자**: DK CHO  
> **검토 게이트**: Design Gate → Implementation Gate

---

## 📋 확정된 10 가지 기준선

### 1. Primary User: HR 실무자
- **결정 사유**: 임원/경영진은 대시보드 뷰어로 충분, 주된 설계 대상은 HR 실무자의 업무 흐름
- **배제 항목**: 임원 대상 심층 보고 기능 (v0.2 범위 밖)

### 2. 핵심 철학: Workflow-centric
- **결정 사유**: Agent 는 도구일 뿐, HR 실무자의 업무 흐름이 중심
- **배제 항목**: Agent 자율성 과잉 설계 (Agent-centric ❌)

### 3. WorkTree: 참고 자료만
- **결정 사유**: 초기부터 '숫자 증명'의 함정 회피
- **제한**: 실제 절감 수치와 기계적으로 연결하지 않음
- **원리**: "Measure first, optimize later"

### 4. ROI 측정: 보류
- **결정 사유**: 11 번 수정사항 — HR OS 가 초기부터 '숫자 증명'의 함정에 빠지지 않도록 하는 안전장치
- **대신**: 업무 완결 시간 (Time-to-Completion) 과 인지적 오류율 감소에 집중

### 5. Pulse-to-Action 완료 조건: 3 단계 분리
- **절차 완료**: 필수 근거와 검증 조건 충족
- **실행 완료**: 승인한 조치가 중복 없이 실제 반영
- **피드백 완료**: 직원에게 결과가 전달되고 후속 변화 확인

### 6. Agent Governance: AID-Guard 프로토콜
- **결정 사유**: 승인된 작업도 재시도하면 두 번 실행될 수 있음
- **구현**: `action_id` 기반 중복 실행 방지, `pending_verification` 상태 처리

### 7. Employee Experience 지표: Sogolytics Q1 2026 기준
- **변화 인지율**: 10% → 목표 30%
- **소통 명확성 격차**: 임원 51% vs 직원 21% → 목표 ≤ 15%p

### 8. 데이터 센싱: 3 단계 (L1/L2/L3)
- **L1**: 주간 펄스 체크 점수 (Declarative)
- **L2**: 협업 툴 활동 로그 (Behavioral)
- **L3**: 정성 피드백 의미 분석 (Contextual)

### 9. 통합 전략: EX × OI
- **미시 신호 (EX)** 를 거시 사고력 (OI) 으로 전환
- **3 레이어 폐쇄 루프**: Experience → Semantic/Vibe → Intelligence

### 10. 운영 원칙: 5 대 원칙
- 짧고 빈번한 Pulse
- 저마찰 Magic Link
- 투명한 동의
- 최소 5 인 익명
- 2 주 내 공유

---

## 🔍 검토된 대안들

### 대안 1: ROI 측정 우선 (기각)
- **제안**: WorkTree 공수 데이터를 실제 절감 수치로 즉시 전환
- **기각 사유**: 초기 시스템이 '숫자 증명'의 함정에 빠질 위험
- **교훈**: "Measure first, optimize later" — 신뢰 구축이 우선

### 대안 2: Agent-centric 설계 (기각)
- **제안**: Agent 자율성을 극대화하여 HR 실무자 개입 최소화
- **기각 사유**: HR 업무는 신뢰와 책임이 핵심, Agent 는 도구일 뿐
- **교훈**: Workflow-centric 가 HR 도메인에 적합

### 대안 3: 단일 완료 상태 (기각)
- **제안**: "완료" 상태를 하나로 통합
- **기각 사유**: 보고서 생성과 직원 경험 변화를 혼동할 위험
- **교훈**: 3 단계 분리 (절차/실행/피드백) 가 신뢰성 확보

---

## 📊 근거 자료

1. **Purdue Univ (Artic)**: 자연어 지침 구조화 시 해결률 28%p 상승
2. **Information Engineering Univ (AID-Guard)**: 승인 작업 중복 실행 방지 프로토콜
3. **Sogolytics Q1 2026**: 피드백 변화 인지율 10%, 임원 - 직원 격차 확인

---

## 🔗 다음 게이트

**Implementation Gate (v0.3)**:
- 파일럿 설계 (3~5 팀, 100~200 명, 8 주)
- 실제 HRIS 연동 테스트
- 성공 기준 검증 계획

---

*본 결정 기록은 HR OS 의 Design Gate 통과 기준선으로, 향후 모든 설계 판단의 기준이 됩니다.*
