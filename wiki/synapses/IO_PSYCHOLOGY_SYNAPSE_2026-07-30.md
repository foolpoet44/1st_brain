# 시냅스 제안: I/O Psychology 4 편 논문 연결 (2026-07-30)

**생성일:** 2026-07-30  
**출처:** `inbox/BRIEFING_2026-07-30_IO_PSYCHOLOGY.md`  
**유형:** Knowledge Synapse (학술 브리핑 → Vault 연결)

---

## 1. Decision Fatigue → [[bp-signal-intelligence]]

**연결 개요:**
의사결정 피로 연구 (Frontiers in Cognition, 2026) 는 **10 가지 원인** (조직 6, 개인 3, 외부 1) 과 **4 가지 효과** (비효과적 결정, 보수화, 오류, 회피) 를 규명했다. 이는 [[bp-signal-intelligence]] 의 **Human Gate 설계**와 직접 연결된다.

**시냅스 노드 제안:**
```yaml
# wiki/synapses/decision-fatigue-human-gate.md
source: "Frontiers in Cognition (2026) - Decision Fatigue Framework"
statistic: "의사결정 피로가 수술 확률 10.5% 감소"
vault_connection: "[[bp-signal-intelligence]] — Human Gate 설계"
core_insight: "**의사결정 피로는 개인의 자제력 실패가 아니라 조직 설계의 실패다.**"
human_gate:
  - gate_id: "DF-GATE-01"
    description: "조직 문화 컨텍스트에서 Operations Lead 가 판단"
    trigger: "연속 의사결정 3 시간 초과 또는 오후 3 시 이후 중대 결정"
    action: "의사결정 세션 중단 → 휴식 15 분 → 추천 중심 보고 (추천/근거/리스크)"
  - gate_id: "DF-GATE-02"
    description: "의사결정 '차선' 매핑"
    trigger: "새 의사결정 유형 등장"
    action: "어떤 결정이 어디에 속하는지 명시 (Executive / Manager / Team / Individual)"
```

**양방향 링크:**
- `[[bp-signal-intelligence]]` → `[[wiki/synapses/decision-fatigue-human-gate]]`
- `[[hr-conceptual-atoms]]` → `[[wiki/synapses/decision-fatigue-human-gate]]` (조직 설계 실패 프레임)

---

## 2. Cultural Bias → [[agentic-recruitment-proxy]]

**연결 개요:**
LLM 기반 채용 평가 연구 (arXiv:2508.16673) 는 **인도 출신 기록이 영국 출신보다 낮음** (p < 0.001) 을 발견했다. 리전 변수가 통제 후에도 유의한 예측 인자 (β = 0.444) 였다. 이는 [[agentic-recruitment-proxy]] 의 **AI 편향 필터**와 연결된다.

**시냅스 노드 제안:**
```yaml
# wiki/synapses/cultural-bias-llm-hiring.md
source: "arXiv:2508.16673 (2025) - Invisible Filters: Cultural Bias in LLM Hiring"
statistic: "인도 기록이 영국보다 낮음 (p < 0.001), 리전 β = 0.444"
vault_connection: "[[agentic-recruitment-proxy]] — AI 편향의 '보이지 않는 필터'"
core_insight: "**공정성은 '알고리즘적 객관성'이 아니라 관계적 정체성 협상 (relational identity negotiation) 이다.**"
human_gate:
  - gate_id: "CB-GATE-01"
    description: "DEI 위원회가 아바타/평가 디자인 심사"
    trigger: "AI 평가 도구 도입 또는 업데이트"
    action: "교차문화 검증 (서구 vs 비서구 샘플) → 편향 점수 공개 → AI 자동화 금지 영역 명시"
  - gate_id: "CB-GATE-02"
    description: "'읽기 쉬운 언어' 역설 인식"
    trigger: "LLM 평가 점수 생성"
    action: "Flesch Reading Ease 점수와 평가 점수 상관관계 모니터링 (β = -0.016, p < 0.001)"
```

**양방향 링크:**
- `[[agentic-recruitment-proxy]]` → `[[wiki/synapses/cultural-bias-llm-hiring]]`
- `[[hr-conceptual-atoms]]` → `[[wiki/synapses/cultural-bias-llm-hiring]]` (공정성의 관계적 협상 프레임)

---

## 3. Fairness in AI Recruitment → [[bp-signal-intelligence]]

**연결 개요:**
AI 기반 채용 공정성 연구 (arXiv:2405.19699v3) 는 **88% 조직이 AI 실험**, **71% 가 AI 최종 결정 반대**임을 보고했다. EEOC 의 **4/5 (80%) 규칙**과 NYC Local Law 144 (2023) 를 준수해야 한다. 이는 [[bp-signal-intelligence]] 의 **Evolution Gate YAML 스키마**와 연결된다.

**시냅스 노드 제안:**
```yaml
# wiki/synapses/fairness-ai-recruitment-gate.md
source: "arXiv:2405.19699v3 (2024) - Fairness in AI-Driven Recruitment"
statistic: "88% 조직 AI 실험, 71% AI 최종 결정 반대, 4/5 규칙 (80% threshold)"
vault_connection: "[[bp-signal-intelligence]] — Evolution Gate YAML 스키마"
core_insight: "**AI 편향은 기술적 결함이 아니라 권력 관계의 증폭이다.**"
human_gate:
  - gate_id: "FR-GATE-01"
    description: "분기별 진화 감사"
    trigger: "에이전트 모델 수정 제안"
    action: "evolution_gate.required: true → 인간 승인 필수, audit_log: true, rollback_enabled: true"
  - gate_id: "FR-GATE-02"
    description: "4 단계 파이프라인 편향 감사"
    trigger: "채용 시즌 시작"
    action: "소싱 → 스크리닝 → 면접 → 선정 각 단계별 CDP 점수 측정 (0.8 미만 시 Post-AI Oversight)"
  - gate_id: "FR-GATE-03"
    description: "NYC Local Law 144 준수"
    trigger: "자동화 도구 사용"
    action: "편향 감사 결과 공개 + 투명성 보고서 제출"
```

**양방향 링크:**
- `[[bp-signal-intelligence]]` → `[[wiki/synapses/fairness-ai-recruitment-gate]]`
- `[[sf-domain-mapping]]` → `[[wiki/synapses/fairness-ai-recruitment-gate]]` (Trust Level Disclosure)

---

## 4. AI Adoption Gap → [[fde-talent-model]]

**연결 개요:**
Irrational Labs 연구 (2025) 는 **자신의 직장 8% 우려 vs 동료 14% vs 다른 산업 29%**라는 인식 격차를 발견했다. **관리자 지지**가 79% 사용률을 견인한다. 이는 [[fde-talent-model]] 의 **Identity Extension 프레임**과 연결된다.

**시냅스 노드 제안:**
```yaml
# wiki/synapses/ai-adoption-identity-extension.md
source: "Irrational Labs (2025) - The AI Workplace: Employee AI Adoption"
statistic: "자신의 직장 8% 우려 vs 동료 14% vs 다른 산업 29%, 관리자 지지 시 79% 사용"
vault_connection: "[[fde-talent-model]] — Identity Extension 프레임"
core_insight: "**리더는 기술이 아니라 심리적 장벽을 해체해야 한다 — '낙관 편향'과 '평균 이상 효과'를 인식하라.**"
human_gate:
  - gate_id: "AA-GATE-01"
    description: "인간 HR + 신경다양성 이해관계자 공동 설계"
    trigger: "AI 채택 프로그램 설계"
    action: "'정체성 확장' 프레임 사용 — '새 사람이 되어라'가 아닌 '기존 역량 확장하라'"
  - gate_id: "AA-GATE-02"
    description: "AI 사용 가시화"
    trigger: "조직 내 AI 채택률 50% 미만"
    action: "성공 사례 올핸즈 공유, Slack 채널 생성, 리더 사용 시연"
  - gate_id: "AA-GATE-03"
    description: "Yerkes-Dodson Law 적용"
    trigger: "직원 불안 설문"
    action: "불안 수준 측정 → 너무 낮으면 동기 부여, 너무 높으면 마비 → 최적 존 설계"
```

**양방향 링크:**
- `[[fde-talent-model]]` → `[[wiki/synapses/ai-adoption-identity-extension]]`
- `[[hr-conceptual-atoms]]` → `[[wiki/synapses/ai-adoption-identity-extension]]` (Guardian → Gardener 전환)

---

## 5. 종합 통찰: "감시자 → 정원사" 정체성 전환

**테마:**  
4 편 논문은 하나의 질문을 던진다: **"HR 은 누구인가?"**

- **Decision Fatigue**: HR 은 개인의 인내력을 요구하는 감시자가 아니라, 의사결정 부하를 분산시키는 **정원사**다.
- **Cultural Bias**: HR 은 알고리즘의 객관성을 맹신하는 감시자가 아니라, 문화적 맥락을 번역하는 **정원사**다.
- **Fairness Metrics**: HR 은 AI 의 결정을 집행하는 감시자가 아니라, 권력 관계를 감시하는 **정원사**다.
- **AI Adoption**: HR 은 기술을 강제하는 감시자가 아니라, 심리적 장벽을 해체하는 **정원사**다.

**시냅스 노드 제안:**
```yaml
# wiki/synapses/guardian-to-gardener-identity.md
theme: "HR 의 정체성 전환: 감시자 → 정원사"
papers:
  - "Decision Fatigue (Frontiers in Cognition, 2026)"
  - "Cultural Bias (arXiv:2508.16673)"
  - "Fairness in AI Recruitment (arXiv:2405.19699v3)"
  - "AI Adoption Gap (Irrational Labs, 2025)"
core_insight: "**HR 은 AI 의 결정을 집행하는 감시자가 아니라, 인간과 AI 의 협력을 경작하는 정원사다.**"
philosophical_anchor:
  - "Kant's enlightenment: 스스로 설계하는 용기"
  - "SDT theory: 자율성, 유능감, 관계성 보호"
  - "Translation vs Censorship: 번역은 원본을 지우지 않는다. 검열은 지운다."
```

---

**다음 액션:**
1. 위 5 개 시냅스 노드를 `wiki/synapses/` 에 실제 파일로 생성 (각 15 분 × 5 = 75 분)
2. 각 소스 문서 ([[bp-signal-intelligence]], [[agentic-recruitment-proxy]], [[fde-talent-model]], [[hr-conceptual-atoms]]) 에 양방향 링크 추가
3. KNOWLEDGE_PULSE.md 에 "Recent Synapses" 섹션에 5 개 노드 기록
4. 대시보드 (http://localhost:8080) 에서 시냅스 가시성 확인

---

*이 시냅스는 csp-brain Vault 의 지식 대사 프로토콜에 따라 생성되었습니다. 지식은 연결될 때 비로소 지능이 됩니다.*
