---
type: Note
status: Active
---

# Synapse Proposal — HR Tech Psychology 2026-07-31

**생성일:** 2026-07-31  
**출처:** Daily HR Tech Psychology Briefing  
**연결 대상:** [[hr-conceptual-atoms]], [[agentic-recruitment-proxy]], [[bp-signal-intelligence]], [[fde-talent-model]], [[OKA Project]]

---

## 🧠 새로운 시냅스 연결 제안

### Synapse #1: AI Augmentation vs Automation 함정
- **Source:** arXiv:2607.13839 (AI-Augmented HRM, German companies)
- **Target:** [[agentic-recruitment-proxy]]
- **Link Type:** Warning Pattern
- **Content:** "AI 도입 시 'augmentation' 선언과 실제 'automation' 운용 사이의 괴리. HR Tech 도입 심사 시 '상호작용 시간 증감' 지표를 1 차 질문으로 명문화할 것."
- **Human Gate:** #1 (AI 도입 심사)

### Synapse #2: Cripping AI — 신경다양성 채용 프레임
- **Source:** arXiv:2605.02080 (Cripping AI)
- **Target:** [[fde-talent-model]]
- **Link Type:** Identity Extension Pattern
- **Content:** "신경다양성 채용은 '기존 역량 확장' 프레임으로 설계. '새로운 사람이 되라'가 아닌 '당신의 인지 방식을 조직이 학습한다'는 메시지."
- **Human Gate:** #2 (신경다양성 채용 설계)

### Synapse #3: Decision Fatigue — 조직 설계 실패
- **Source:** Front. Cognit. 2026 (Decision Fatigue integrative review)
- **Target:** [[bp-signal-intelligence]]
- **Link Type:** Organizational Design Pattern
- **Content:** "DF 는 개인의 자제력 실패가 아닌 조직 설계 실패. 오후 3 시 이후 high-stakes 의사결정 금지 또는 2 인 이상 합의제 필수."
- **Human Gate:** #3 (의사결정 시간 설계)

### Synapse #4: Cognitive Agency Surrender — 의도적 마찰
- **Source:** arXiv:2603.21735 (Cognitive Agency Surrender)
- **Target:** [[agentic-recruitment-proxy]]
- **Link Type:** Epistemic Sovereignty Pattern
- **Content:** "AI 평가 도구는 '반대 근거 입력' 필드를 필수로 활성화. 인간 결정자는 AI 판단에 동의하더라도 1 개 이상의 검증 근거를 입력해야 최종 결정 승인."
- **Human Gate:** #4 (AI 평가 검증 강제)

---

## 🔗 기존 지식 원자와의 연결

### [[hr-conceptual-atoms]] 확장
- **추가될 Atom:**
  - "HR 의 AI 리터러시는 'AI 를 쓰는 능력'이 아니라, 'AI 의 판단을 조직의 언어로 번역하는 능력'이다."
  - "번역은 원본을 지우지 않는다. 검열은 지운다."
  - "정체성 전환: Guardian(감시자) → Gardener(정원사) → Translator(번역가)"

### [[bp-signal-intelligence]] Evolution Gate YAML 추가
```yaml
evolution_gate:
  required: true  # 에이전트 모델 수정 시 인간 승인 필수 여부
  audit_log: true  # 진화 이력 기록 여부
  rollback_enabled: true  # 인간이 롤백할 수 있는 권한 부여 여부
  validation_sample: 10  # 자동 분류/처리 후 무작위 N 개 샘플 인간 검증 (권장: 10)
  human_gates:
    - gate_1_ai_adoption:
        question: "이 도구가 인간의 상호작용 시간을 늘리는가, 줄이는가?"
        threshold: "해방된 시간의 50% 이상은 인간 상호작용에 재할당"
    - gate_2_neurodiversity_design:
        requirement: "신경다양성 커뮤니티 심의 통과"
        panel_size: 3
    - gate_3_decision_timing:
        rule: "오후 3 시 이후 high-stakes 의사결정 금지"
        exception: "2 인 이상 합의 또는 다음 날 오전 자동 연기"
    - gate_4_ai_verification:
        requirement: "AI 평가 동의 시 1 개 이상 반대 근거 입력 필수"
        enforcement: "시스템이 최종 결정 승인 거부"
```

### [[OKA Project]] — Meaning Protection Zone 선언
```yaml
meaning_protection_zone:
  roles:
    - Digital Twin Designer
    - Physical AI Tech Leader Pool
    - Neurodiversity Hiring Committee
  principle: "AI full-automation prohibited — AI is assistant, human is principal"
  empirical_basis: "arXiv:2603.14963 — AI-exposed work is most strongly correlated with creativity/novelty, autonomy/freedom, and positive affect/happiness"
```

---

## 📊 지식 대사 보고 (Metabolism Summary)

- **새로운 Signal Node:** 4 개 (HR_TECH_PSYCHOLOGY_2026-07-31)
- **연결된 Vault Nodes:** 5 개 ([[hr-conceptual-atoms]], [[agentic-recruitment-proxy]], [[bp-signal-intelligence]], [[fde-talent-model]], [[OKA Project]])
- **Human Gate 선언:** 4 개 (AI 도입 심사, 신경다양성 채용 설계, 의사결정 시간 설계, AI 평가 검증 강제)
- **핵심 키워드:** Translation vs Censorship, Guardian→Gardener→Translator, Scaffolded Friction, Decision Fatigue, Cripping AI

**대시보드:** http://localhost:8080
