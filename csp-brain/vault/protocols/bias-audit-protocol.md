---
type: Protocol
status: Active
version: 1.0.0
related_to:
  - "[[human-gate-schema]]"
  - "[[hr-identity-evolution]]"
  - "[[agentic-recruitment-proxy]]"
---

# 편향 감사 결과 공개 프로토콜

## 개요

이 프로토콜은 **Human Gate #2 (Bias Audit Gate)**의 구현 명세입니다.
AI 시스템의 편향을 정기적으로 감사하고, 그 결과를 투명하게 공개합니다.

---

## 감사 주기

| 감사 유형 | 주기 | 담당자 | 결과 공개 |
|----------|------|--------|----------|
| **정기 감사** | 매월 1 회 | AI Agent + Human Reviewer | GitHub Pages |
| **임시 감사** | Human Gate 트리거 시 | AI Agent | Telegram 알림 |
| **연간 종합** | 연 1 회 (12 월) | Human Committee | 전체 리포트 |

---

## 감사 항목

### 1. Skin-Deep Bias (외피 편향)

**정의**: AI 면접 아바타의 인종/성별 불일치 시 발생하는 편향

**측정 방법**:
```python
bias_score = (불일치_시_합격률 - 일치_시_합격률) / 일치_시_합격률
```

**임계치**:
- 🟢 정상: `bias_score < 0.1`
- 🟡 주의: `0.1 ≤ bias_score < 0.3`
- 🔴 위험: `bias_score ≥ 0.3` → **Gate #2 발동**

**데이터 소스**:
- `outputs/bias-audits/skin-deep-YYYY-MM.md`
- Eval 대시보드 `bias_metrics.skin_deep_bias`

**근거 논문**:
- Skin-Deep Bias (2026): AI 면접 아바타 인종 불일치 편향 인식 상승

---

### 2. Decision Fatigue (의사결정 피로)

**정의**: 연속 의사결정 시 오류율 증가 현상

**측정 방법**:
```python
fatigue_index = (오후_오류율 - 오전_오류율) / 오전_오류율
```

**임계치**:
- 🟢 정상: `fatigue_index < 0.1`
- 🟡 주의: `0.1 ≤ fatigue_index < 0.15`
- 🔴 위험: `fatigue_index ≥ 0.15` → **Gate #2 발동**

**데이터 소스**:
- `outputs/bias-audits/decision-fatigue-YYYY-MM.md`
- Eval 대시보드 `bias_metrics.decision_fatigue`

**근거 논문**:
- Decision Fatigue (2026): 의사결정 피로로 수술 확률 10.5% 감소

---

### 3. AI Replacement Narrative (대체 담론 편향)

**정의**: "AI 가 인간을 대체한다"는 담론 vs "AI 가 인간을 보강한다"는 담론 비율

**측정 방법**:
```python
narrative_ratio = (보강_담론_빈도) / (대체_담론_빈도 + 보강_담론_빈도)
```

**목표**:
- 🎯 목표: `narrative_ratio ≥ 0.7` (보강 담론 70% 이상)
- 🟡 주의: `0.5 ≤ narrative_ratio < 0.7`
- 🔴 위험: `narrative_ratio < 0.5` → **Gate #2 발동**

**데이터 소스**:
- `outputs/bias-audits/narrative-analysis-YYYY-MM.md`
- Eval 대시보드 `bias_metrics.narrative_ratio`

**근거 논문**:
- Careers in AI Age (2026+): AI 노출도 ↔ 급여 정적 상관

---

## 감사 워크플로우

```
1. 데이터 수집 (매월 25 일)
   ↓
2. 편향 점수 계산 (매월 26 일)
   ↓
3. 임계치 판정 (매월 27 일)
   ↓
4. 결과 공개 (매월 28 일)
   ↓
5. Gate 발동 (필요시)
```

---

## 결과 공개 채널

### 1. Telegram 알림 (실시간)

**트리거**: 편향 점수 임계치 초과

**메시지 형식**:
```markdown
🚨 **편향 감사 경고**

📊 **Skin-Deep Bias**: 0.35 (임계치 0.3 초과)
⚠️ **상태**: Gate #2 발동

🔗 **상세 리포트**: https://foolpoet44.github.io/1st_brain/bias-audits/

🔧 **조치 필요**:
1. AI 면접 아바타 설정 검토
2. 인간 검토자 승인 대기
3. 필요시 롤백
```

### 2. GitHub Pages (월간 리포트)

**URL**: `https://foolpoet44.github.io/1st_brain/bias-audits/`

**포함 내용**:
- 월간 편향 점수 추이
- 항목별 상세 분석
- 개선 권고사항
- Human Gate 발동 이력

### 3. 내부 대시보드 (실시간 모니터링)

**URL**: `http://localhost:8080/bias-metrics`

**기능**:
- 실시간 편향 점수 표시
- 임계치 초과 시 경고
- 역사적 추이 그래프

---

## 에스컬레이션 프로세스

### Level 1: 경고 (Warning)

**조건**: 편향 점수 임계치 초과 (1 항목)

**조치**:
- Telegram 알림 발송
- GitHub 리포트 생성
- Human Gate #2 활성화 (승인 대기)

### Level 2: 게이트 발동 (Gate Activation)

**조건**: 편향 점수 임계치 초과 (2 항목 이상) 또는 2 개월 연속

**조치**:
- AI 에이전트 권한 제한
- 인간 검토자 승인 필수
- Rollback Gate #4 대기 상태

### Level 3: 즉시 롤백 (Immediate Rollback)

**조건**:
- 인간 불만 3 건 이상
- 편향 점수 0.5 이상 (심각)
- Gate 위반 감지

**조치**:
- **즉시 AI 에이전트 중지**
- 이전 안정 버전으로 롤백
- 사후 보고서 작성 (24 시간 내)
- Human Committee 검토

---

## 감사 리포트 템플릿

```markdown
---
type: BiasAudit
status: Published
audit_month: YYYY-MM
---

# 편향 감사 리포트 (YYYY 년 MM 월)

## 요약

- **Skin-Deep Bias**: 0.XX (🟢/🟡/🔴)
- **Decision Fatigue**: 0.XX (🟢/🟡/🔴)
- **Narrative Ratio**: 0.XX (🟢/🟡/🔴)
- **Human Gate 발동**: X 회

## 상세 분석

### 1. Skin-Deep Bias
[상세 분석 내용]

### 2. Decision Fatigue
[상세 분석 내용]

### 3. Narrative Ratio
[상세 분석 내용]

## 개선 권고사항

1. [권고사항 1]
2. [권고사항 2]

## Human Gate 이력

| 날짜 | Gate | 사유 | 조치 |
|------|------|------|------|
| YYYY-MM-DD | #2 | Skin-Deep Bias 0.35 | 승인 대기 |

---

**감사자**: AI Agent + Human Reviewer
**공개일**: YYYY-MM-DD
**다음 감사**: YYYY-MM-DD
```

---

## 관련 문서

- [[human-gate-schema]] — Human Gate 4 명세
- [[hr-identity-evolution]] — HR 정체성 진화 프레임
- [[agentic-recruitment-proxy]] — 에이전트 채용 프록시

---

## 변경 이력

- **2026-08-01**: 초기 작성 (Bias Audit Protocol v1.0.0)
- **2026-08-01**: Human Gate #2 연동 명세 추가


---

## Evolution Gate YAML Schema 연동

Bias Audit 는 **Human Gate #1 (Evolution Gate)** YAML 스키마와 연동됩니다.

### YAML 스키마 위치

```
csp-brain/vault/protocols/human-gate-schema.md
```

### 연동 메커니즘

```yaml
bias_audit_gate:
  enabled: true
  audit_frequency: monthly
  metrics:
    - skin_deep_bias: 0.3
    - decision_fatigue: 0.15
    - narrative_ratio: 0.7
  
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
```

### 자동화 플로우

1. **Eval 런처**가 `human-gate-schema.md` YAML 검증
2. **편향 감사** 결과 YAML 임계치와 비교
3. **임계치 초과** 시 Telegram 알림 + Gate 발동
4. **Gate #4 (Rollback)** 트리거 시 즉시 중지

