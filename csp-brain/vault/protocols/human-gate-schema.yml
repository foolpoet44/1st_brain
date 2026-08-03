---
type: Protocol
status: Active
version: 1.0.0
related_to:
  - "[[hr-identity-evolution]]"
  - "[[agentic-recruitment-proxy]]"
  - "[[bp-signal-intelligence]]"
  - "[[fde-talent-model]]"
---

# Human Gate 4 명세 (AI Prohibition Zones)

## 개요
Human Gate 는 AI 에이전트의 진화와 작동을 통제하는 **인간 승인 게이트웨이**입니다.
각 Gate 는 YAML 스키마로 정의되며, 위반 시 자동 롤백이 트리거됩니다.

---

## Gate #1: 에이전트 진화 감사 (Evolution Gate)

evolution_gate:
  enabled: true
  required: true  # AI 모델 수정 시 인간 승인 필수
  audit_log: true  # 진화 이력 기록
  rollback_enabled: true  # 인간이 롤백 권한 보유
  validation_sample: 10  # 자동 분류 후 무작위 10 개 샘플 인간 검증
  
  approval_workflow:
    - step: 1
      name: AI 제안
      actor: agent
      action: submit_modification
      description: "AI 가 모델/프롬프트/규칙 수정 제안"
    
    - step: 2
      name: 인간 검토
      actor: human
      action: review_and_approve
      timeout_hours: 24
      description: "인간이 24 시간 내 검토 및 승인/거부"
    
    - step: 3
      name: 적용 또는 롤백
      actor: human
      action: apply_or_rollback
      description: "승인 시 적용, 거부/타임아웃 시 롤백"
  
  trigger_conditions:
    - model_weights_changed: true
    - prompt_template_modified: true
    - classification_rules_updated: true
    - eval_score_change_gt: 5  # Eval 점수 5 점 이상 변동
  
  notification:
    telegram: true
    slack: false
    email: true

---

## Gate #2: 편향 감사 결과 공개 (Bias Audit Gate)

bias_audit_gate:
  enabled: true
  required: true
  disclosure_level: public  # internal | public
  audit_frequency: monthly  # weekly | monthly | quarterly
  
  metrics:
    - name: skin_deep_bias
      description: "AI 면접 아바타 인종/성별 불일치 편향"
      threshold: 0.3
      measurement: "아바타 불일치 시 편향 점수 증가율"
    
    - name: decision_fatigue
      description: "연속 의사결정 시 오류율 증가"
      threshold: 0.15
      measurement: "오류율 > 15% 시 게이트 발동"
    
    - name: ai_replacement_narrative
      description: "'AI 대체' 담론 vs 'AI 보강' 담론 비율"
      target: 0.7
      measurement: "보강 담론 비율 ≥ 70% 목표"
  
  publication_channel:
    telegram: true
    github_pages: true
    internal_dashboard: true
  
  escalation:
    - level: 1
      condition: "metric.threshold_exceeded"
      action: "telegram_alert"
    
    - level: 2
      condition: "threshold_exceeded_count >= 2"
      action: "gate_activation"
    
    - level: 3
      condition: "human_complaint_count >= 3"
      action: "immediate_rollback"

---

## Gate #3: 신뢰 사다리 교육 (Trust Ladder Gate)

trust_ladder_gate:
  enabled: true
  required: true
  curriculum_version: 1.0
  certification_valid_months: 12
  renewal_required: true
  
  stages:
    - stage: 1
      name: 이해 (Understanding)
      duration_hours: 4
      learning_objectives:
        - "AI 의 능력과 한계 정확히 이해"
        - "Skin-Deep Bias 개념 숙지"
        - "Decision Fatigue 메커니즘 이해"
      
      content:
        - type: lecture
          title: "AI 편향의 심리학"
          duration_minutes: 60
        
        - type: case_study
          title: "아바타 인종 불일치 사례"
          duration_minutes: 90
        
        - type: quiz
          questions: 20
          passing_score: 80
      
      assessment:
        type: quiz
        passing_score: 80
        requirements:
          - "퀴즈 점수 ≥ 80"
          - "케이스 분석 리포트 제출"
    
    - stage: 2
      name: 공감 (Empathy)
      duration_hours: 8
      learning_objectives:
        - "인간 의사결정 피로 공감"
        - "정체성 협상 과정 이해"
        - "'감시자 → 정원사' 프레임 전환"
      
      content:
        - type: role_play
          title: "의사결정 피로 체험"
          duration_minutes: 120
        
        - type: workshop
          title: "정원사 마인드셋"
          duration_minutes: 180
        
        - type: practice
          title: "신뢰 구축 대화"
          duration_minutes: 180
      
      assessment:
        type: role_play
        passing_score: 70
        requirements:
          - "역할극 관찰자 평가 ≥ 70"
          - "성찰 일지 제출 (500 자 이상)"
    
    - stage: 3
      name: 중개 (Mediation)
      duration_hours: 12
      learning_objectives:
        - "인간-AI 간 의미 중개 능력"
        - "'AI 보강' 담론 프레이밍"
        - "신뢰 사다리 완성"
      
      content:
        - type: project
          title: "실제 HR 업무 중개"
          duration_minutes: 360
        
        - type: mentoring
          title: "번역자 정체성 확립"
          duration_minutes: 180
        
        - type: presentation
          title: "신뢰 구축 전략"
          duration_minutes: 180
      
      assessment:
        type: project
        passing_score: 60
        requirements:
          - "프로젝트 결과물 ≥ 60"
          - "동료 평가 ≥ 70"
          - "최종 발표 ≥ 60"
  
  certification:
    issued_by: "csp-brain HR Authority"
    valid_months: 12
    renewal_required: true
    output_path: "outputs/certifications/trust-ladder-YYYY.md"

---

## Gate #4: 인간 롤백 권한 (Human Rollback Gate)

rollback_gate:
  enabled: true
  required: true
  auto_trigger: true
  
  trigger_conditions:
    - condition: eval_score_below
      threshold: 60
      description: "Eval 점수 60 점 미만"
    
    - condition: bias_detected
      threshold: true
      description: "편향 감사에서 임계치 초과"
    
    - condition: human_complaint_count
      threshold: 3
      description: "인간 불만 3 건 이상"
    
    - condition: gate_violation
      description: "Human Gate #1-3 위반 감지"
  
  rollback_scope:
    model_weights: true
    prompt_templates: true
    classification_rules: true
    agent_permissions: true
  
  notification:
    telegram: true
    email: true
    slack: false
    github_issue: true
  
  rollback_procedure:
    - step: 1
      action: "immediate_suspension"
      description: "에이전트 즉시 중지"
    
    - step: 2
      action: "snapshot_restore"
      description: "이전 안정 버전으로 롤백"
    
    - step: 3
      action: "incident_report"
      description: "사후 보고서 작성 (24 시간 내)"
    
    - step: 4
      action: "human_review"
      description: "인간 검토 후 재가동 승인"

---

## 모니터링 및 감사

monitoring:
  eval_integration: true  # Eval 대시보드와 연동
  audit_frequency: monthly
  public_dashboard: true
  github_pages_path: "https://foolpoet44.github.io/1st_brain/human-gates/"

audit_log:
  enabled: true
  storage_path: "_ops/human-gate-audits/"
  retention_months: 24
  format: markdown

---

## 버전 이력

- **1.0.0** (2026-08-01): 초기 버전
  - Human Gate 4 명세 정의
  - YAML 스키마 표준화
  - Eval 대시보드 연동 준비

