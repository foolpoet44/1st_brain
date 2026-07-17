---
title: EX Intelligence
created: 2026-04-14
updated: 2026-07-18
type: project
status: growing
tags: [project, hr, saas, ex, intelligence]
---

# EX Intelligence

## Compiled Truth

Employee Experience Intelligence — 구성원 경험 데이터 플랫폼.

**핵심 아키텍처**: [[Data Sensing (L1/L2/L3 Architecture)|3 단계 데이터 센싱]]

- L1: 주간 펄스 체크 점수 (Declarative)
- L2: 협업 툴 활동 로그 (Behavioral)
- L3: 정성 피드백 의미 분석 (Contextual)

**필터링 원리**: [[Weak Signal Theory (Ansoff)|약한 신호 이론]] — L1~L2 단계에서 선제적 개입

### EX × OI 통합 전략 (v1.0, 2026-04-28)

개별 구성원 경험(EX, 미시 신호)을 조직 지능(OI, 거시 사고력)으로 전환하는 실행 로드맵. 계기판(Pulse·LDS 360·Data Sensing·EX Full Inventory 12클러스터)들을 하나의 통합 진단 시스템으로 묶는다. **3레이어 폐쇄 루프**: L1 Experience(비침습 수집) → L2 Semantic/Vibe(LLM이 숫자 이면의 이야기·SDT/LMX/POS/JD-R 4렌즈로 의미화) → L3 Intelligence(actionable insight). 상향만이 아니라 **하향 흐름**(OI 우선순위가 수집 초점·빈도를 재조정)이 대시보드와 지능체를 가른다. 세 통합 전략: ① [[escon]] 진화(개인 스킬 → 조직 Skill Balance Sheet, 역량 감가상각) ② Workplace Jarvis(개인 Second Brain → 조직 Collective Brain, Supabase pgvector RAG) ③ Pulse Check → Early Warning System(명시 응답 + 암묵 행동, Watch/Alert/Critical). 통합 로드맵 Q2 기반구축 → Q3 연결 → Q4 지능화. 윤리 원칙: 집계 데이터만·투명성·Opt-out(감시 아닌 돌봄).

### 3단계 보고 로드맵 (경영 승인 트랙)

Working Backwards 역산으로 개념 승인→파일럿까지 세 번의 보고가 하나의 시스템을 만든다. **1보고(2026.03 완료)** "왜 해야 하는가" — Hidden Risk Zone(조직은 갑자기 무너지지 않는다, 신호 선행), 리더–직원 26%p 인식 격차, CIA Need-to-Know. **2보고(2026.05)** "무엇을 측정할 것인가" — 현실 이슈 Full Inventory 8클러스터(I01 번아웃~I08 프로세스), 측정방식 매트릭스(펄스/심층/행동/정성), 현상 카테고리 5종 + 임계치 액션 프로토콜(점수 방어 독해 → 문제해결자 모드 언어 전환). **3보고(2026.06)** "어떻게 운영할 것인가" — 5대 운영 원칙(짧고 빈번/저마찰 Magic Link/투명 동의/최소 5인 익명/2주 내 공유), 수요자별 3뷰(리더·경영진·HR 알림)+전사 대시보드, 파일럿(3~5팀·100~200명·8주·2회 측정). 성공 기준: 참여율 70%↑·리더 액션 60%↑·"말해도 바뀐다" 10%p↑. → Q4 전사 확대, AX maturity 연동.

**연결**: [[bp-signal-intelligence]](신호 상태 기계) · [[ex-insight-mining-pipeline]](Triage 분석) · [[opq-framework]](Disposition 선행) · [[pulse-check]] · projects/physical-ai-talent

---

## Timeline

### 2026-07-18 — Drive 설계문서 2건 편입

- **EX Intelligence × OI 통합 전략 v1.0**(2026-04-28): 3레이어 폐쇄 루프(Experience→Semantic/Vibe→Intelligence), 하향 흐름이 핵심. 3전략(ESCON Skill Balance Sheet / Workplace Jarvis RAG / Early Warning System). Supabase 단일 허브. 8개 클러스터 미시 신호를 8-클러스터 통제어휘로 잇는 상위 프레임.
- **EX Intelligence 보고 3단계 실행 로드맵**(2026.04): 1보고(왜)·2보고(무엇)·3보고(어떻게)의 경영 승인 트랙. 8 이슈 클러스터, 현상 카테고리 액션 프로토콜, 파일럿 계획(8주·100~200명). 파일럿 2026.07~08.
- 하위 시스템 [[bp-signal-intelligence]]·[[ex-insight-mining-pipeline]]·[[opq-framework]] 신설 문서와 그래프 연결.

### 2026-04-29

- wiki 초기화와 함께 아키텍처 문서 연결
- [[Data Sensing]], [[Weak Signal Theory]] 핵심 원리로 설정

### 2026-04-14

- 데이터 센싱 설계 완료
- 4 월 킥오프 대기
