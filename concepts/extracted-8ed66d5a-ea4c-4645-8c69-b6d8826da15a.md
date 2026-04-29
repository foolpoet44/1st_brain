# Extracted Knowledge from Conv: 8ed66d5a-ea4c-4645-8c69-b6d8826da15a

**Date**: 2026-03-05T00:52:06.963101Z

### Extracted Code (text)

```text
Layer 0 측정 (EX Touchpoints) → 원인 변수
  - 공정성: 절차적/분배적/대인적 공정성 (3문항)
  - 상사지원: PSS(Perceived Supervisor Support) (2문항)
  - HR 관행: 자율성·훈련 재량적 제공 경험 (2문항)

Layer 1 측정 (Psychology) → 매개 변수
  - POS 지수: "조직이 나의 기여를 가치있게 여긴다" (3문항)
  - SDT 욕구충족: 자율성·유능감·관계성 각 1문항 (3문항)

Layer 2 측정 (Engagement) → 핵심 결과
  - UWES-9 단축형: Vigor 3 / Dedication 3 / Absorption 3 (9문항)
  - Job Engagement vs Org. Engagement 구분

Layer 3 측정 (Outcomes) → 선행 지표
  - 이직 의도 (1문항)
  - OCB 자기보고 (1문항)
  - 성과 자신감 (1문항)
```

### Extracted Code (text)

```text
진단 패턴 유형:

Type A: L0↑ L1↑ L2↑ → 건강한 조직 (유지 전략)
Type B: L0↓ L1↓ L2↓ → 전면 위기 (긴급 개입)
Type C: L0↑ L1↓ L2↓ → POS 형성 실패 (의미 전달 문제)
Type D: L0↑ L1↑ L2↓ → Engagement 전환 실패 (직무 설계 문제)
Type E: L0↓ L1↑ L2↑ → 과거 자산 소진 중 (예방적 개입 필요)
```

### Extracted Code (text)

```text
[데이터 수집 레이어]
Google Forms / Typeform
  ↓ Webhook
[오케스트레이션 레이어]
monday.com (응답률 모니터링 + 알림 자동화)
  ↓
[분석 레이어]
Google Sheets (원시 데이터) → Python/Claude API (패턴 분석)
  ↓
[인사이트 레이어]
Notion (대시보드 + 리포트) + Claude (자연어 해석)
  ↓
[액션 레이어]
HR 개입 솔루션 트리거 (자동 추천)
```

### Extracted Code (text)

```text
- 컬럼: 부서 / 대상자 수 / 응답자 수 / 응답률 / 마감일 / 상태
- 자동화: 응답률 70% 미만 시 리마인더 자동 발송
- 자동화: 마감 D-2 알림 → 담당자에게 Slack 메시지
```

### Extracted Code (text)

```text
- 컬럼: 부서 / Layer별 점수 / 진단 유형(A~E) / 권장 액션 / 개입 상태
- 자동화: 특정 점수 임계값 하회 시 → HR 담당자에게 알림
- 자동화: Type B/E 감지 시 → 즉각 개입 워크플로우 트리거
```

### Extracted Code (python)

```python
# Pulse Analysis Agent 핵심 프롬프트 구조

system_prompt = """
당신은 LG PRI의 조직심리 분석 전문가입니다.
입력: 부서별 4-Layer Pulse 점수 데이터
출력: 
1. 사슬 절단점 유형 판정 (Type A~E)
2. 핵심 발견사항 (3줄 요약)
3. 우선순위 개입 영역 (1~3순위)
4. 부서별 맞춤 솔루션 추천
5. 다음 측정 주기 집중 모니터링 지표
"""
```

### Extracted Code (text)

```text
수집 → 정제 → 분석 → 시각화 → 배포

1. 수집: Google Forms 제출 → Google Sheets 자동 적재
2. 정제: Apps Script → 역산 문항 처리, 결측값 처리
3. 분석: Python(pandas) → Layer별 평균, 진단 유형 분류
4. 시각화: Radar Chart (4-Layer), Heatmap (부서 비교)
5. 배포: Notion 자동 업데이트 + PDF 리포트 생성
```

### Extracted Code (text)

```text
형식: 1페이지 대시보드
내용: 
  - 전사 Engagement Index (단일 숫자)
  - 위험 신호 부서 Top 3
  - 분기 대비 변화 방향 (↑↓→)
  - 권장 조직 차원 개입 1~2개
핵심 언어: "비즈니스 성과와의 연결고리"
```

### Extracted Code (text)

```text
형식: 부서 전용 리포트 (3~5페이지)
내용:
  - 소속 부서 Layer별 프로파일
  - 전사 평균 대비 강점/약점
  - 구체적 행동 권고사항 (What to do next week)
  - FAQ: "이 데이터를 어떻게 해석하나요?"
핵심 언어: "내 팀에게 무엇을 해야 하는가"
```

### Extracted Code (text)

```text
형식: 자동 발송 개인 피드백 (2~3분 분량)
내용:
  - "당신의 응답이 반영되었습니다" 확인
  - 전체 집계 결과 공유 (익명성 보장 범위 내)
  - 조직이 취할 액션 예고
핵심 언어: "측정이 변화를 만든다"
```

### Extracted Code (text)

```text
Type C (POS 형성 실패) 처방:
  → 상사지원 행동 강화 워크숍
  → 조직 기여 가시화 커뮤니케이션 (사내 성과 스토리 공유)
  → 리더십 코칭: "PSS → POS 매개" 행동 목록 제공

Type D (Engagement 전환 실패) 처방:
  → 직무 재설계 대화 (Job Crafting 워크숍)
  → SDT 욕구(자율성·유능감·관계성) 진단 심화
  → 역할 명확화 + 성장 경로 가시화

Type E (자산 소진 진행중) 처방:
  → 즉각 Well-Being 개입 (번아웃 예방 프로그램)
  → 공정성 인식 회복을 위한 리더 행동 교정
  → 단기 인정·보상 강화
```

### Extracted Code (text)

```text
① 응답 → 액션 사이클을 30일 이내로 가시화
   "지난 번 여러분이 말한 것 → 우리가 한 것" 루프 공개

② 심리적 안전 설계
   - 부서 인원 5명 미만 결과는 집계에서 제외 (비공개)
   - 경영진도 익명성 보장 범위 명시

③ 간편성 설계
   - 모바일 최적화 (5분 이내 완료)
   - QR코드 접근 + 리마인더 1회만 (스팸 방지)

④ 의미 부여
   - 측정 전: "이 조사가 어떻게 사용되는지" 사전 브리핑
   - 측정 후: 결과 공유 날짜를 미리 약속
```

### Extracted Code (text)

```text
Q1 (3월):  Full Survey (24문항) → 분기 리포트 → 부서장 공유
4월:        Mini Pulse (5문항, L0 중심)
Q2 (6월):  Full Survey + 반기 Outcome 측정 → 상반기 리뷰
7월:        Mini Pulse
Q3 (9월):  Full Survey → 부서별 1:1 피드백 세션
10월:       Mini Pulse
Q4 (12월): Full Survey + 연간 Well-Being 종합 평가 → 연간 리포트
```

### Extracted Code (text)

```text
① 측정  
   Google Forms 기반 24문항 설문
   모바일 최적화 / 응답 5분 이내
   분기 Full + 월간 Mini Pulse 이원화

② 분석  
   Layer별 자동 집계 → 진단 유형 분류
   부서 비교 / 전기 대비 변화 추적
   AI 보조 해석 (이상 신호 자동 플래깅)

③ 운영  
   monday.com 응답률 모니터링
   미달 부서 자동 리마인더 발송
   결과 → 액션 30일 내 피드백 루프
```

### Extracted Code (text)

```text
✅ 측정 문항 설계 완료 (24문항, 4-Layer 구조)
✅ 진단 알고리즘 설계 완료 (5가지 유형 분류)
✅ 운영 도구 선정 완료 (기존 도구 활용)
✅ 파일럿 설계 완료 (1개 부서, 1분기)
⬜ 경영진 보고 및 승인
⬜ 전사 런칭
```

### Extracted Code (text)

```text
경영진  ────────────  분기 1회
"조직 건강도 Executive Dashboard"
전사 Engagement Index + 위험 신호 부서
→ 경영 의사결정 연동 가능한 언어로 번역

부서장  ────────────  분기 1회  
"내 팀 진단 리포트"
전사 평균 대비 강점/약점 + 다음 주 행동 권고
→ 리더가 팀원과 직접 대화할 수 있는 수준

구성원  ────────────  측정 직후
"여러분의 목소리가 반영되었습니다"
집계 결과 공유 + 조직이 취할 액션 예고
→ 참여율 유지의 핵심 장치
```

### Extracted Code (text)

```text
측정 결과  →  진단 유형 분류  →  처방 솔루션 매칭

공정성 저하   →  Type C  →  리더 행동 코칭
몰입 전환 실패 →  Type D  →  직무 재설계 대화
자산 소진 징후 →  Type E  →  Well-Being 즉각 개입
```
