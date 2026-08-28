---
type: Project
status: Active
created: 2026-08-28
related_to: "[[EX Intelligence]], [[Pulse-to-Action]], [[Agent Governance]]"
tags:
  - hr-os
  - product-definition
  - design-gate
  - workflow-centric
---

# HR OS — Product Definition v0.2 (Design Gate 통과)

> **Design Gate 확정일**: 2026-08-28  
> **버전**: v0.2 (Design Gate 통과)  
> **다음 게이트**: Implementation Gate (v0.3)

---

## 📋 Design Gate 확정사항 (10 가지 기준선)

사용자 검토를 거쳐 확정된 10 가지 설계 기준선입니다. 향후 모든 설계 판단의 기준이 됩니다.

### 1. Primary User
- **확정 내용**: HR 실무자
- **배제 사용자**: 임원/경영진 (대시보드 뷰어는 제공하되, 주된 설계 대상 아님)

### 2. 핵심 철학
- **Agent-centric ❌ → Workflow-centric ✅**
- Agent 는 도구일 뿐, HR 실무자의 업무 흐름이 중심

### 3. WorkTree
- **역할**: 공수 추정 및 우선순위 판단의 **참고 자료**
- **제한**: 실제 절감 수치와 기계적으로 연결하지 않음
- **원리**: "Measure first, optimize later" — 초기부터 '숫자 증명'의 함정 회피

### 4. ROI 측정
- **v0.2 범위**: 보류 (11 번 수정사항)
- **대신**: 업무 완결 시간 (Time-to-Completion) 과 인지적 오류율 감소에 집중

### 5. Pulse-to-Action 완료 조건
- **3 단계 분리**:
  1. 절차 완료 (Procedural Completion)
  2. 실행 완료 (Execution Completion)
  3. 피드백 완료 (Feedback Completion)

### 6. Agent Governance
- **승인 프로토콜**: AID-Guard 기반 (중복 실행 방지)
- **실행 상태**: `pending_verification` 상태 처리

### 7. Employee Experience 지표
- **변화 인지율**: 후속 Pulse 문항으로 측정
- **소통 명확성**: 임원 - 직원 격차 ≤ 15%p 목표

### 8. 데이터 센싱
- **3 단계**: L1(Declarative) → L2(Behavioral) → L3(Contextual)
- **약한 신호 이론**: L1~L2 단계에서 선제적 개입

### 9. 통합 전략
- **EX × OI**: 미시 신호 (EX) 를 거시 사고력 (OI) 으로 전환
- **3 레이어 폐쇄 루프**: Experience → Semantic/Vibe → Intelligence

### 10. 운영 원칙
- 짧고 빈번한 Pulse
- 저마찰 Magic Link
- 투명한 동의
- 최소 5 인 익명
- 2 주 내 공유

---

## 🎯 Product Vision

**HR 실무자가 "의견 수렴 → 액션 실행 → 변화 확인"의 전 과정을 신뢰할 수 있게 완결하는 Workflow OS**

### 핵심 가치
1. **신뢰**: "Agent 가 처리했다"와 "업무가 제대로 끝났다"를 구분
2. **투명성**: 모든 실행 단계가 검증 가능
3. **연속성**: 보고서 생성과 직원 경험 변화를 하나의 흐름으로 연결

---

## 🏗️ 아키텍처 개요

```
┌─────────────────────────────────────────────────────────────┐
│                    HR OS — Workflow Layer                   │
├─────────────────────────────────────────────────────────────┤
│  [Pulse 수집] → [분석] → [액션 추천] → [승인] → [실행] → [피드백]  │
│      ↓           ↓           ↓           ↓         ↓          │
│  (절차완료)  (절차완료)  (절차완료)  (실행완료)  (피드백완료)   │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│              Employee Experience Intelligence               │
│  - 변화 인지율 측정                                         │
│  - 임원 - 직원 격차 모니터링                                  │
│  - 후속 Mini Pulse 자동 생성                                │
└─────────────────────────────────────────────────────────────┘
```

---

## 📊 성공 기준 (v0.2 파일럿)

| 지표 | 측정 방법 | 목표값 |
|------|-----------|--------|
| 참여율 | Pulse 응답률 | ≥ 70% |
| 리더 액션 완료율 | 3 단계 완료 조건 충족률 | ≥ 60% |
| 변화 인지율 | "무엇이 바뀌었는가" 응답률 | ≥ 30% |
| 소통 명확성 격차 | 임원 - 직원 응답 차이 | ≤ 15%p |
| 중복 실행 제로 | `action_id` 기반 중복 감지 | 0 건 |

---

## 🔗 관련 문서

- [[_ops/checklists/pulse-to-action-completion]] — 3 단계 완료 체크리스트
- [[signals/hr-ai-research-brief-20260828]] — Design Gate 근거 자료
- [[projects/ex-intelligence/README]] — EX Intelligence 아키텍처
- [[Type/Project]] — 프로젝트 타입 정의

---

## 📝 변경 이력

| 버전 | 날짜 | 변경 내용 |
|------|------|-----------|
| v0.2 | 2026-08-28 | Design Gate 통과 (10 가지 기준선 확정, ROI 측정 보류) |
| v0.1 | 2026-08-21 | 초안 작성 |

---

*본 문서는 HR OS 의 Design Gate 통과 기준선으로, 향후 모든 설계 판단의 기준이 됩니다.*
