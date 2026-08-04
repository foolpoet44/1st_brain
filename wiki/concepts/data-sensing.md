---
title: Data Sensing (L1/L2/L3 Architecture)
created: 2026-04-14
updated: 2026-04-29
type: concept
status: growing
tags: [data, architecture, ex-intelligence, sensing]
aliases: [데이터 센싱, L1/L2/L3]
---

# Data Sensing (L1/L2/L3 Architecture)

## Compiled Truth

HR 인텔리전스 시스템에서 데이터의 신뢰도와 깊이를 확보하기 위해, 명시적 답변뿐만 아니라 행동과 맥락을 계층화하여 수집하는 방식입니다.

**L1 - Declarative Data (선언적 데이터)**

- 개인이 설문이나 인터페이스를 통해 직접 입력한 데이터
- 예시: 펄스 서베이 점수, 자기 신고형 역량 점수, 만족도 조사
- "나는 이렇게 생각한다"라는 주관적 의지를 포착하지만, 사회적 바람직성 편향이 발생할 수 있음

**L2 - Behavioral Data (행동 데이터)**

- 시스템이나 협업 도구에서 발생하는 활동 로그 데이터
- 예시: 슬랙 메시지 빈도, 코드 커밋 패턴, 도구 사용 로그, 목표 업데이트 주기
- "나는 실제로 이렇게 행동한다"를 보여주며, 선언적 데이터와의 간극을 포착하여 실제 문제를 발견함

**L3 - Contextual Data (맥락 데이터)**

- 비정형 텍스트나 비언어적 상황에서 추출되는 맥락
- 예시: 리더십 진단 내 정성 텍스트, 대화의 톤앤매너, 조직 내 감정적 분위기
- "왜 그런 행동이 발생했는가"에 대한 심층적 이유를 파악함. LLM 의 감정 분석 및 주제 추출 기술이 핵심적으로 활용됨

**적용 사례: EX Intelligence**

- L1: 주간 펄스 체크 점수
- L2: 협업 툴 (Slack, Outlook) 상의 의사소통 밀도
- L3: 심층 인터뷰 및 자유 기술형 피드백의 의미론적 분석

---

## Timeline

### 2026-04-29

- wiki 초기화와 함께 마이그레이션
- [[ex-intelligence|EX Intelligence]] 의 핵심 아키텍처로 설정됨

### 2026-04-14

- 3 단계 데이터 센싱 모델 정의 및 상세 이식
