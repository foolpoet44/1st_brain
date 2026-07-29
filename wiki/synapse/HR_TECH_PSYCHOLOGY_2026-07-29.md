# Knowledge Synapse — HR Tech Psychology 2026-07-29

**생성일:** 2026-07-29 09:10 KST  
**출처:** `BRIEFING_2026-07-29_HR_TECH_PSYCHOLOGY.md`  
**유형:** `[[hr-tech-briefing]]` → `[[agentic-recruitment-proxy]]`, `[[fde-talent-model]]`, `[[bp-signal-intelligence]]`, `[[hr-conceptual-atoms]]`

---

## 시냅스 1: Human-AI Hybrid Fairness → [[agentic-recruitment-proxy]]

**핵심 연결:**  
arXiv:2603.06240 의 실증 데이터 (CDP 0.699 → 0.854) 는 [[agentic-recruitment-proxy]] 의 **Human Gate 설계**에 다음과 같은 실증적 근거를 제공합니다:

```yaml
# [[bp-signal-intelligence]] 에 추가할 Evolution Gate 스키마
evolution_gate:
  required: true  # AI 모델 수정 시 인간 승인 필수
  audit_log: true  # 진화 이력 기록
  rollback_enabled: true  # 인간이 롤백할 수 있는 권한
  validation_sample: 10  # 자동 분류 후 무작위 10 개 샘플 인간 검증 (권장)
  cdp_threshold: 0.80  # Conditional Demographic Parity 임계값 (미만 시 인간 재검토 필수)
  post_ai_oversight: true  # AI 추천 후 수동 검색 의무화 (CDP 0.876 달성)
```

**실행 액션:**  
- [[agentic-recruitment-proxy]] 의 **Trust Ladder 3 단계** (Collaboration) 를 기본 프로세스로 설계
- "AI 추천 → 인간 검증 (CDP 체크) → Post-AI Oversight 수동 검색" 파이프라인 구현
- 분기별 **진화 감사 (Evolution Audit)** 에서 CDP 추이 모니터링

---

## 시냅스 2: Bullshit Tasks → [[fde-talent-model]] Identity Extension

**핵심 연결:**  
arXiv:2606.12430 의 발견 ("근로자는 무의미 업무를 AI 에게 자발적 양도") 은 [[fde-talent-model]] 의 **Identity Extension** 프레임을 실증적으로 뒷받침합니다:

> "AI 는 대체자가 아니라 **역량 확장 도구**다. 당신은 '새로운 사람' 이 되는 것이 아니라, **기존 역량을 AI 로 확장**하는 것이다."

**실행 액션:**  
- 직무 재설계 워크숍에서 **Bullshit Task 분류 세션** 도입 (근로자 참여)
- **AI Delegation List** (위임 권장) vs **Human Retention List** (유지 필수) 명시적 문서화
- FDE Bootcamp 커리큘럼에 "Meaningful Work Design" 모듈 추가

---

## 시냅스 3: AI Signaling & Self-Efficacy → [[sf-domain-mapping]] Trust Level Disclosure

**핵심 연결:**  
Behavioral Sciences 2026 의 조절 효과 ("AI 자기효능감이 낮은 집단에는 AI 신호 효과 감소") 는 [[sf-domain-mapping]] 의 **Trust Level Disclosure** 와 연결됩니다:

| 구직자 유형 | AI 자기효능감 | 신뢰 수준 | 게이트 설계 |
|------------|--------------|----------|------------|
| Type A (High) | 높음 | High | AI 신호 즉시 노출, 빠른 지원 경로 |
| Type B (Low) | 낮음 | Medium | **AI 교육 기회 선제공개**, 지원 전 오리엔테이션 필수 |
| Type C (Anxious) | 매우 낮음 | Low | **인간 HR 우선 상담**, AI 는 보조 도구로만 소개 |

**실행 액션:**  
- 채용 공고에 **AI 자기효능감 진단 체크리스트** 링크 추가
- Type B/C 구직자를 위한 **AI 리터러시 부트캠프** 선제공개
- "AI 보조" 어조 사용 (예: "AI 가 서류를 **보조**하여 검토합니다" vs "AI 가 서류를 **자동 심사**합니다")

---

## 시냅스 4: Decision Making Ecology → [[bp-signal-intelligence]] Evolution Gate

**핵심 연결:**  
Frontiers in Psychology 2025 의 "의사결정은 환경 상호작용" 이라는 통찰은 [[bp-signal-intelligence]] 의 **Evolution Gate** 에 **의사결정 피로도 체크** 항목을 추가해야 함을 시사합니다:

```yaml
# Evolution Gate 에 추가할 Decision Fatigue 체크
decision_fatigue_mitigation:
  preferred_time_slot: "morning"  # 중요 인사 결정은 오전에 배치
  max_decisions_per_day: 5  # 하루 최대 의사결정 수 제한
  checklist_required: true  # 체크리스트/휴리스틱 도구 필수 사용
  cooldown_minutes: 30  # 결정 간 최소 30 분 쿨다운
```

**실행 액션:**  
- 승진/해고/채용 결정 회의는 **오전 10 시~12 시**로 고정
- **의사결정 체크리스트** 템플릿 배포 (휴리스틱 도구 포함)
- 분기별 **Decision Fatigue Audit** 실시 (결정 품질 vs 피로도 상관관계 분석)

---

## 종합: "감시자 → 정원사" 정체성 전환

4 개의 시냅스가 관통하는 주제는 **HR 의 정체성 재정의**입니다:

| 기존 정체성 (Guardian) | 새로운 정체성 (Gardener) |
|----------------------|------------------------|
| AI 편향을 **차단**한다 | AI 편향을 **감시하고 번안**한다 |
| Bullshit 업무를 **방어**한다 | Bullshit 업무를 **자발적 양도**한다 |
| AI 신호를 **은폐**한다 | AI 신호를 **가시화하고 교육**한다 |
| 의사결정을 **계산**한다 | 의사결정 환경을 **설계**한다 |

**핵심 통찰:**  
**"인지 능력의 생존 전략"** — AI 시대 HR 의 생존 전략은 **방어 (Guardian)** 가 아니라 **경작 (Gardener)** 입니다. AI 는 대체자가 아니라 **정원사의 도구**이며, HR 은 **확장 가능한 정체성**을 경작하는 역할로 전환해야 합니다.

---

**시냅스 파일 경로:** `wiki/synapse/HR_TECH_PSYCHOLOGY_2026-07-29.md`  
**연결된 노드:** [[agentic-recruitment-proxy]], [[fde-talent-model]], [[bp-signal-intelligence]], [[hr-conceptual-atoms]], [[hr-tech-briefing-2026-07-29]]  
**대시보드:** http://localhost:8080
