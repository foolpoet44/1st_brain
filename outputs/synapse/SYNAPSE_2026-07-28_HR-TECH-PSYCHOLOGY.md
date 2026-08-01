---
type: Note
status: Active
---

# Synapse: HR Tech Psychology → Vault Integration
## 2026-07-28 Daily Briefing Connections

---

## 🧬 시냅스 1: Skin-Deep Bias → [[agentic-recruitment-proxy]]

**연결 개념**: AI 면접 아바타의 정체성 표현성이 공정성 인식에 미치는 영향

**기존 [[agentic-recruitment-proxy]] 지식**:
- AI 기반 채용 프록시 에이전트의 편향 감사 프로토콜
- 알고리즘 의사결정의 투명성 요구사항

**새로운 시냅스**:
```
Skin-Deep Bias (2026) → agentic-recruitment-proxy
- 아바타 디자인은 "UI"가 아닌 "사회적 정체성 단서"
- 공정성 감사 범위 확장: 알고리즘 편향 + 아바타 표현성
- 교차적 공정성 역설: 부분 일치 > 완전 불일치 (공정성 점수)
- 실행: DEI 위원회가 아바타 디자인 심사 (Human Gate #1)
```

**Vault 연결 제안**:
- `outputs/synapse/synapse_skin-deep-bias_agentic-recruitment.md` 생성
- [[agentic-recruitment-proxy]] 문서에 "아바타 디자인 감사" 섹션 추가

---

## 🧬 시냅스 2: Careers in AI Age → [[hr-conceptual-atoms]]

**연결 개념**: AI 노출도 모델 간 불확실성과 커리어 코칭 프로토콜

**기존 [[hr-conceptual-atoms]] 지식**:
- HR 개념 원자: 역량, 동기, 조직 몰입 등 핵심 구성개념

**새로운 시냅스**:
```
Careers in AI Age (2026) → hr-conceptual-atoms
- AI 노출도 7 개 모델 비교: 가정 (assumption) 이 결과 결정
- 2020+ 모델: AI 노출도 ↔ 급여·복잡도 정적 상관 (이전: 부정적/중립)
- 보강 프리미엄: complement > substitute (급여)
- 실행: 커리어 코칭 시 5 개 모델 평균 제시 (불확실성 완화)
- 국가별 AI 낙관주의: 불평등↑ → AI 낙관↑ (ρ=0.64)
```

**Vault 연결 제안**:
- `outputs/synapse/synapse_careers-ai_hr-conceptual-atoms.md` 생성
- [[hr-conceptual-atoms]] 에 "AI 시대 커리어 원자" 추가

---

## 🧬 시냅스 3: Decision Fatigue → [[bp-signal-intelligence]]

**연결 개념**: 의사결정 피로 10 가지 원인과 HR 운영 리듬 설계

**기존 [[bp-signal-intelligence]] 지식**:
- 비즈니스 프로세스 신호 감지 및 자동화 게이트 설계

**새로운 시냅스**:
```
Decision Fatigue (2026) → bp-signal-intelligence
- 10 가지 원인 (조직 6, 개인 3, 외부 1) → 3 범주
- 1 차 효과: 비효율적 결정, 보수화, 회피
- 2 차 효과: 직무 만족↓, 이직↑, 몰입↓
- 실행: 의사결정 감사 (Decision Audit) — 고위험 결정은 오전 배치
- 휴식 설계: 점심 전후 결정 패턴 모니터링
```

**Vault 연결 제안**:
- `outputs/synapse/synapse_decision-fatigue_bp-signal.md` 생성
- [[bp-signal-intelligence]] 에 "의사결정 리듬 게이트" 섹션 추가
- Evolution Gate YAML schema 에 `decision_audit` 항목 추가

---

## 🧬 시냅스 4: Cripping AI → [[fde-talent-model]]

**연결 개념**: 신경다양성 채용 시 정체성 확장 프레임

**기존 [[fde-talent-model]] 지식**:
- FDE 인재 모델: 역량 기반 인재 평가 프레임워크

**새로운 시냅스**:
```
Cripping AI (2026) → fde-talent-model
- 3 대 능력주의 전제 해체: 결함, 능력자 권위, 수동적 대상
- Cripping AI 3 원칙: 정치성 노출, cripistemologies 존중, crip labor 인정
- 실행: 신경다양성 채용 시 "정체성 확장" 프레임
  - "새로운 사람이 되어야 함" → "기존 역량 확장"
  - 유연한 커뮤니케이션 규범 (비동기 면접 옵션)
- AI 평가 도구 감사: "정상성" 기준이 능력자 중심인지 점검
```

**Vault 연결 제안**:
- `outputs/synapse/synapse_cripping-ai_fde-talent.md` 생성
- [[fde-talent-model]] 에 "신경다양성 정체성 확장" 섹션 추가
- Human Gate Specification 에 "신경다양성 채용 기준 공동 설계" 추가

---

## 🧬 시냅스 5: Decision Fatigue → [[OKA Project]]

**연결 개념**: 의사결정 감사 도구와 OKA 운영 리듬

**기존 [[OKA Project]] 지식**:
- OKA 프로젝트: 조직 지식 아키텍처 및 운영 프로토콜

**새로운 시냅스**:
```
Decision Fatigue (2026) → OKA Project
- 의사결정 감사 도구: 하루 결정 밀집 시간대 매핑
- 고위험 결정은 오전 배치 (인지 자원 최대)
- 휴식 설계: 점심 전후 결정 패턴 모니터링
- 실행: OKA 운영 리듬에 "의사결정 밀도" 메트릭 추가
```

**Vault 연결 제안**:
- `outputs/synapse/synapse_decision-fatigue_oka.md` 생성
- [[OKA Project]] 에 "의사결정 리듬 설계" 섹션 추가

---

## 📊 시냅스 메트릭

| 시냅스 | 원본 논문 | 대상 Vault 노드 | 인간 게이트 | Trust Level |
|--------|----------|----------------|-------------|-------------|
| 1 | Skin-Deep Bias | agentic-recruitment-proxy | 아바타 디자인 심사 | Medium |
| 2 | Careers in AI Age | hr-conceptual-atoms | 커리어 코칭 프로토콜 | High |
| 3 | Decision Fatigue | bp-signal-intelligence | 의사결정 감사 | High |
| 4 | Cripping AI | fde-talent-model | 신경다양성 채용 기준 | Medium |
| 5 | Decision Fatigue | OKA Project | 운영 리듬 설계 | High |

**총 시냅스**: 5 개
**인간 게이트 선언**: 5 개 영역
**Trust Level High**: 3 개, **Medium**: 2 개

---

*시냅스 생성: 2026 년 7 월 28 일 오전 9:10 | csp-brain Synapse Protocol v1.0*
