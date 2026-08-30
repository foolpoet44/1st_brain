# HR AI 리서치 브리프 — 2026 년 8 월 28 일

type: Task
> **이번 주 핵심**: "Agent 가 처리했다"와 "업무가 제대로 끝났다"를 구분하라
> 
> - ✅ 절차 준수
> - ✅ 중복 실행 방지
> - ✅ 직원이 체감하는 후속조치 확인

---

## 📊 3 건의 핵심 연구 요약

| # | 자료 | 핵심 발견 | HR 실무 적용 |
|---|------|-----------|-------------|
| 1 | **Purdue Univ (Artic)**<br>자연어 워크플로우 연구 | 단계별 입출력·검증 조건 명시 시<br>해결률 **28%p 상승** | Pulse 각 단계를 4 칸으로 정의:<br>필수 입력 / 생성 산출물 / 통과 조건 / 실패 시 경로 |
| 2 | **Information Engineering Univ (AID-Guard)**<br>승인 작업 재시도 연구 | 응답 유실 후 재시도 시<br>**중복 실행** 발생 가능 | 쓰기 작업에 `action_id` 부여,<br>타임아웃 시 재조회 로직 구현 |
| 3 | **Sogolytics Q1 2026**<br>Employee Experience 조사 | 피드백이 변화로 이어진다는 응답<br>**10%** (임원 51% vs 직원 21%) | 액션 테이블에 `결과 알림 날짜` 추가,<br>후속 Pulse 에서 변화 인지율 측정 |

---

## 🎯 CSP 설계에 대한 추론: 완료 조건 3 단계 분리

기존의 **단일 완료 상태**를 다음 세 가지로 분리해야 합니다:

### 1️⃣ 절차 완료 (Procedural Completion)
> **질문**: 필수 근거와 검증 조건을 충족했는가?

- [ ] 각 단계의 필수 입력 데이터 존재
- [ ] 생성 산출물이 명세대로 출력됨
- [ ] 통과 조건 검증 로직 실행됨
- [ ] 실패 시 경로가 명시됨

**체크리스트**: [`_ops/checklists/pulse-to-action-completion.md`](https://github.com/foolpoet44/1st_brain/blob/main/_ops/checklists/pulse-to-action-completion.md)

---

### 2️⃣ 실행 완료 (Execution Completion)
> **질문**: 승인한 조치가 중복 없이 실제 반영됐는가?

- [ ] `action_id` 가 부여됨
- [ ] 결과 미확정 상태 처리 로직 존재
- [ ] 타임아웃 시 재조회 로직 구현
- [ ] 대상 시스템의 중복요청 처리 기능 확인

**중복 실행 리스크**:
- 🚫 교육 신청 중복 등록
- 🚫 온보딩 계정 중복 생성
- 🚫 안내메일 재발송

---

### 3️⃣ 피드백 완료 (Feedback Completion)
> **질문**: 직원에게 결과가 전달됐고, 후속 변화가 확인됐는가?

- [ ] `직원에게 결과를 알린 날짜` 기록됨
- [ ] 후속 Mini Pulse 에서 변화 인지율 측정
- [ ] 직급별 인식 차이 모니터링 (익명성 확보 시)

**Employee Experience 지표**:
| 지표 | 현재값 (Sogolytics Q1 2026) | 목표 |
|------|---------------------------|------|
| 변화 인지율 | 10% | ≥ 50% |
| 소통 명확성 (직원) | 21% | 임원 격차 ≤ 15%p |

---

## 📁 생성된 문서

### 1. 리서치 브리프 원문
- **경로**: [`signals/hr-ai-research-brief-20260828.md`](https://github.com/foolpoet44/1st_brain/blob/main/signals/hr-ai-research-brief-20260828.md)
- **내용**: 3 건 연구의 상세 분석, 한계점, 관련 문서 링크

### 2. 실행 체크리스트
- **경로**: [`_ops/checklists/pulse-to-action-completion.md`](https://github.com/foolpoet44/1st_brain/blob/main/_ops/checklists/pulse-to-action-completion.md)
- **내용**: 
  - Artic 프레임워크 적용 (4 칸 정의)
  - AID-Guard 프로토콜 (실행 흐름 YAML)
  - Employee Experience 지표 테이블
  - 완료 상태 전이도

---

## 🔁 다음 행동 (Next Actions)

### 즉시 수행 (이번 주 최우선)
1. **기존 Pulse-to-Action 워크플로우 검토**: 단일 완료 상태를 3 단계로 분리하는 수정안 작성
2. **액션 테이블 스키마 변경**: `action_id`, `result_notification_date`, `status` 필드 추가
3. **Mini Pulse 문항 개발**: "지난 의견 수렴 이후 무엇이 바뀌었는지 알고 있다" 측정 문항 추가

### 검토 필요
- [ ] 국내 HRIS 시스템의 idempotency 지원 여부 확인
- [ ] 익명성 확보 가능한 직급 집단 식별
- [ ] 변화 인지율 기준값 설정 (조직 문화 고려)

---

## ⚠️ 한계 인지

본 브리프의 연구 결과들은 다음 한계를 가집니다:

1. **Artic**: 실제 HR 운영 실험 아님 (산업·의료 벤치마크)
2. **AID-Guard**: 제한된 시험 환경 프로토타입
3. **Sogolytics**: 
   - 8 월 공개 Q1 2026 자료 (최신 아님)
   - 벤더 주도 자기보고 조사
   - **국내 조직 기준값으로 해석 불가**

---

## 🔗 관련 문서

- [[Pulse-to-Action Workflow]]
- [[Agent Governance Framework]]
- [[Employee Experience Metrics]]
- [[HR AI Research Brief 2026-08-21]] (이전 브리프)

---

*본 브리프는 2026 년 8 월 28 일 GitHub 에 저장되었으며, csp-brain Vault 의 Signal 로 등록되었습니다.*

**저장소**: https://github.com/foolpoet44/1st_brain  
**커밋**: `ae83d11` (2026-08-28)
