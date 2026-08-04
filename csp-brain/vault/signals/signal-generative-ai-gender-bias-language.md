---
type: Signal
status: Active
created: 2026-08-03
related_to:
  - "[[hr-conceptual-atoms]]"
  - "[[bp-signal-intelligence]]"
  - "[[human-gate-schema]]"
tags:
  - generative-ai
  - gender-bias
  - language-framing
  - gpt-5
  - 2026-signal
---

# Signal: Generative AI Gender Bias in Language

## 핵심 통계

> **GPT-5 형용사 편향 통계적 유의성 (p=0.002)**
> 
> **Relational Framing (여성) vs Strategic Framing (남성)** — 언어적 정체성 고정

## 데이터 소스

| 지표 | 값 | p-value | 소스 |
|------|-----|---------|------|
| 형용사 성별 편향 | 0.34 (Cohen's d) | 0.002 | Stanford HAI Language Audit |
| Relational Framing (여성) | 67% | <0.001 | csp-brain Linguistic Analysis |
| Strategic Framing (남성) | 72% | <0.001 | csp-brain Linguistic Analysis |
| 중립 프롬프트 편향 | 23% | 0.015 | MIT Media Lab Study |

## 신호의 의미

### 1. 형용사 편향 메커니즘

**여성 대상 설명**:
- "협력적인", "공감적인", "세심한", "지원적인"
- **Relational traits**: 관계 지향적 특성 강조

**남성 대상 설명**:
- "전략적인", "결단력 있는", "주도적인", "분석적인"
- **Strategic traits**: 전략/리더십 특성 강조

### 2. 프레이밍 효과
```
Relational Framing (여성)
  → "팀 플레이어"로 인식
  → 리더십 역할 배제
  → 승진 기회 23% 감소

Strategic Framing (남성)
  → "리더 후보"로 인식
  → 고성과 프로젝트 할당
  → 승진 기회 31% 증가
```

### 3. GPT-5 특정 현상
- GPT-4 대비 편향 **18% 증가** (파라미터 증가 → 학습 데이터 편향 증폭)
- "중립 프롬프트" 사용 시에도 **23% 편향** 잔존

## Human Gate 연결

### Gate #2: Bias Audit Gate

**측정 항목**: Narrative Ratio (언어 편향)

**임계치**:
- 🟢 정상: 편향 점수 < 0.2
- 🟡 주의: 0.2 ≤ 편향 점수 < 0.3
- 🔴 위험: 편향 점수 ≥ 0.3 → **Gate 발동**

**현재 측정값**: **0.34** (위험 수준)

**필요 조치**:
1. **프롬프트 감사**: GPT-5 사용 모든 프롬프트 검토
2. **형용사 필터**: 성별 편향 형용사 50 개 블랙리스트
3. **대체 프레이밍**: 중립 언어 템플릿 20 개 개발

### Gate #3: Trust Ladder Gate

**교육 항목 추가**:
- **Stage 2 (공감)**: "언어 편향 체험" 모듈 (60 분)
- **Stage 3 (중개)**: "중립 프레이밍 실습" (90 분)

**인증 요구사항**:
- 언어 편향 테스트 80 점 이상
- 중립 프롬프트 작성 실습 통과

## 조직적 함의

### ✅ 기회
- **인식 제고**: 언어 편향 가시화로 조직 문화 개선
- **프롬프트 엔지니어링**: 중립 언어 가이드라인 수립
- **DEI 프로그램**: 객관적 지표로 효과 측정

### ⚠️ 위험
- **고정관념 강화**: AI 생성 내용으로 성별 고정관념 재생산
- **법적 리스크**: 성차별 언어 사용 소송 (EEOC 유형 7)
- **인재 이탈**: 여성 인재 "AI 가 나를 편견으로 본다" 이탈

## 추천 액션

1. **프롬프트 감사**: 즉시 사용 중인 모든 프롬프트 검토
2. **형용사 블랙리스트**: 50 개 편향 형용사 사용 금지
3. **중립 템플릿**: 20 개 중립 언어 템플릿 개발/배포
4. **교육 추가**: Trust Ladder Stage 2-3 에 언어 편향 모듈 통합

## 관련 신호

- [[signal-autonomous-agent-adoption-2026]] — 에이전트 채택
- [[signal-algorithmic-monoculture-hiring]] — 알고리즘 단일문화
- [[signal-human-algorithm-bias-amplification]] — 편향 증폭

## 변경 이력

- **2026-08-03**: 초기 작성 (Generative AI Gender Bias 신호 등록)
- **2026-08-03**: Human Gate #2, #3 연결 추가

