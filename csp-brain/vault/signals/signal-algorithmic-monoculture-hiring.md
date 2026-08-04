---
type: Signal
status: Active
created: 2026-08-03
related_to:
  - "[[agentic-recruitment-proxy]]"
  - "[[bp-signal-intelligence]]"
  - "[[human-gate-schema]]"
tags:
  - algorithmic-monoculture
  - vendor-concentration
  - hiring-bias
  - 2026-signal
---

# Signal: Algorithmic Monoculture in Hiring

## 핵심 통계

> **90% 채용 AI 시장 3 개 벤더 집중** (HireVue, Pymetrics, LinkedIn Insight)
> 
> **26% Black 지원자, 15% Asian 지원자** 시스템적 거부율 증가

## 데이터 소스

| 지표 | 값 | 연도 | 소스 |
|------|-----|------|------|
| Top 3 벤더 시장점유율 | 90% | 2026 | IDC HR Tech Market Analysis |
| Black 지원자 거부율 증가 | +26% | 2025-2026 | NIST Algorithmic Bias Audit |
| Asian 지원자 거부율 증가 | +15% | 2025-2026 | NIST Algorithmic Bias Audit |
| 시스템적 거부 (Systematic Rejection) | 10% | 2026 | csp-brain Bias Audit |

## 신호의 의미

### 1. 알고리즘 단일문화 (Monoculture)
- **정의**: 소수 벤더 알고리즘이 시장 지배 → 다양성 상실
- **결과**: 모든 기업이 **동일한 편향**을 증폭
- **비유**: 농업 단일작물 재배 → 병충해 취약

### 2. 인종별 차별적 영향
```
Black 지원자:   기준선 대비 26% 더 높은 거부율
Asian 지원자:   기준선 대비 15% 더 높은 거부율
White 지원자:   기준선 (통제군)
```

### 3. "시스템적 거부" 메커니즘
- **10% 지원자**는 자격과 무관하게 **자동 거부**
- **원인**: 학습 데이터 편향 → 알고리즘 결정 → 피드백 루프

## Human Gate 연결

### Gate #2: Bias Audit Gate

**트리거 조건**:
- Skin-Deep Bias ≥ 0.3 → **자동 발동**
- 현재 측정값: **0.42** (위험 수준)

**필요 조치**:
1. **즉시 감사**: HireVue, Pymetrics, LinkedIn Insight 3 벤더 대상
2. **결과 공개**: GitHub Pages 에 편향 감사 리포트 게시
3. **벤더 다각화**: 단일 벤더 의존도 50% 미만으로 축소

### Gate #4: Rollback Gate

**트리거 조건 충족**:
- ✅ Bias detected (Skin-Deep 0.42 > 0.3)
- ✅ Human complaint count ≥ 3 (2026 년 7 건 접수)

**권장 조치**:
- **즉시 중지**: 3 개 벤더 알고리즘 일시 정지
- **수동 전환**: 30 일간 인간 심사자로 복귀
- **재검증**: 편향 0.15 미만으로 개선 후 재가동

## 조직적 함의

### ✅ 기회
- **리스크 가시화**: 편향 수치화로 개선 목표 설정 가능
- **벤더 협상력**: 감사 결과 기반 SLA 재협상
- **다양성 이니셔티브**: 객관적 지표로 DEI 프로그램 효과 측정

### ⚠️ 위험
- **법적 리스크**: 인종 차별 소송 (EEOC 신고 증가)
- **평판 손상**: 편향 감사 결과 유출 시 브랜드 타격
- **인재 상실**: qualified candidate 10% 자동 거부

## 추천 액션

1. **비상 감사 위원회**: HR, Legal, DEI, Engineering 합동
2. **벤더 다각화**: 3 개 → 6 개 (신규: HireEZ, Paradox, Eightfold)
3. **Human-in-the-Loop**: 최종 결정 100% 인간 검토 (30 일)
4. **편향 모니터링**: 실시간 대시보드 (Eval 통합)

## 관련 신호

- [[signal-autonomous-agent-adoption-2026]] — 에이전트 채택
- [[signal-generative-ai-gender-bias-language]] — 언어 편향
- [[signal-human-algorithm-bias-amplification]] — 편향 증폭

## 변경 이력

- **2026-08-03**: 초기 작성 (Algorithmic Monoculture 신호 등록)
- **2026-08-03**: Human Gate #2, #4 연결 추가

