---
type: Checklist
status: Active
category: AI-Ops
related_to: "[[Pulse-to-Action]], [[Agent Governance]]"
created: 2026-08-28
---

# Pulse-to-Action 완료 조건 — 3 단계 검증 체크리스트

> **핵심 원칙**: "Agent 가 처리했다"와 "업무가 제대로 끝났다"는 다르다.
> 
> 보고서 생성이나 시스템 등록이 끝난 시점과, 직원 경험이 달라진 시점을 혼동하지 않는다.

---

## 1 단계: 절차 완료 (Procedural Completion)

**질문**: 필수 근거와 검증 조건을 충족했는가?

### 체크리스트

- [ ] **필수 입력 데이터 존재**: 각 단계에 필요한 Pulse 데이터, 메타데이터, 컨텍스트가 모두 수집됨
- [ ] **생성 산출물 명세 준수**: 단계별 출력 (분석 리포트, 액션 추천, 승인 요청서) 이 정의된 포맷으로 생성됨
- [ ] **통과 조건 검증 로직 실행됨**: 
  - [ ] 최소 응답 기준 (예: n ≥ 30) 충족
  - [ ] 통계적 유의성 (예: p < 0.05) 확인
  - [ ] 데이터 품질 체크 (결측치, 이상치) 통과
- [ ] **실패 시 경로 명시**: 조건 미충족 시 대체 경로 또는 안전한 중단 절차가 정의됨

### Articul 프레임워크 적용

각 단계를 다음 4 칸으로 정의:

| 단계 | 필수 입력 | 생성 산출물 | 통과 조건 | 실패 시 경로 |
|------|-----------|-------------|-----------|--------------|
| 예시: Pulse 수집 | org_id, period | raw_responses | 응답률 ≥ 60% | 경고 로그 후 중단 |
| 예시: 분석 | cleaned_data | insights[] | 유의미한 패턴 ≥ 1 | "분석 불가" 메시지 출력 |
| 예시: 액션 추천 | insights[] | action_candidates[] | 우선순위 스코어 존재 | 수동 검토 큐로 이관 |

---

## 2 단계: 실행 완료 (Execution Completion)

**질문**: 승인한 조치가 중복 없이 실제 반영됐는가?

### 체크리스트

- [ ] **`action_id` 부여**: 모든 쓰기 작업에 고유 식별자가 할당됨
- [ ] **결과 미확정 상태 처리**: 타임아웃/응답 유실 시 `pending_verification` 상태로 전환
- [ ] **재조회 로직 구현**: 재시도 전 대상 시스템에서 기존 작업 성공 여부 먼저 확인
- [ ] **중복요청 처리 기능 확인**: 연결된 HRIS 가 idempotency 를 지원하는지 문서화됨

### AID-Guard 프로토콜 적용

```yaml
execution_flow:
  before_execute:
    - verify_approval_token
    - check_current_state
  on_timeout:
    - set_state: pending_verification
    - query_target_system: action_id
    - if exists: skip_retry
    - if not_exists: safe_retry
  after_execute:
    - record_action_id
    - log_execution_timestamp
```

### 중복 실행 리스크 시나리오

| 시나리오 | 방지 장치 |
|----------|-----------|
| 교육 신청 중복 등록 | `action_id` 기반 중복 체크 |
| 온보딩 계정 중복 생성 | 계정 존재 여부 선조회 |
| 안내메일 재발송 | 발송 이력 로그 확인 |

---

## 3 단계: 피드백 완료 (Feedback Completion)

**질문**: 직원에게 결과가 전달됐고, 후속 변화가 확인됐는가?

### 체크리스트

- [ ] **`직원에게 결과를 알린 날짜` 기록**: 액션 테이블에 필수 필드로 추가
- [ ] **소통 채널 명시**: 이메일, 공지, 팀 미팅 등 전달 수단 기록
- [ ] **후속 Mini Pulse 측정**: "지난 의견 수렴 이후 무엇이 바뀌었는지 알고 있다" 문항 포함
- [ ] **직급별 인식 차이 모니터링**: 익명성 확보된 집단에서만 비교 분석

### Employee Experience 지표

| 지표 | 측정 방법 | 목표값 |
|------|-----------|--------|
| 변화 인지율 | 후속 Pulse 문항 ("무엇이 바뀌었는가") | ≥ 50% |
| 소통 명확성 | "의사결정 소통이 명확했다" 응답률 | 임원 - 직원 격차 ≤ 15%p |
| 피드백 유효성 | "피드백이 의미 있는 변화로 이어졌다" 응답률 | ≥ 30% (Sogolytics Q1 2026 기준 10%) |

### 한계 인지

- 벤더 주도 자기보고 조사 (Sogolytics) 는 국내 조직 기준값으로 해석 불가
- 8 월 공개 자료는 Q1 2026 결과 (최근 일주일 변화 아님)
- 인과효과 주장에는 추가 실험 설계 필요

---

## 완료 상태 전이도

```
[절차 완료] → [실행 완료] → [피드백 완료] → [Closed]
      ↓              ↓              ↓
  [검증 실패]   [중복 감지]   [인지율 미달]
      ↓              ↓              ↓
  [수정 재실행]   [수동 확인]   [소통 강화]
```

---

## 관련 문서

- [[HR AI Research Brief 2026-08-28]]
- [[_ops/checklists/task-completion-contract.md]]
- [[Pulse-to-Action Workflow]]
- [[Agent Governance Framework]]

---

*본 체크리스트는 2026 년 8 월 28 일 HR AI 리서치 브리프의 3 건 연구를 기반으로 작성됨:*

1. *Purdue Univ (Artic): 자연어 지침 구조화 시 해결률 28%p 상승*
2. *Information Engineering Univ (AID-Guard): 승인 작업 중복 실행 방지 프로토콜*
3. *Sogolytics Q1 2026: 피드백 변화 인지율 10%, 임원 - 직원 격차 확인*
