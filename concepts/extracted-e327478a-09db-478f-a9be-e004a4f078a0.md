# Extracted Knowledge from Conv: e327478a-09db-478f-a9be-e004a4f078a0

**Date**: 2026-02-17T23:24:23.344607Z

### Extracted Code (text)

```text
# 🎯 Mission: 로봇테크 for 스마트팩토리 — 스킬 온톨로지 데이터 재설계

## 배경
현재 ESCON 프로젝트(escon-nine.vercel.app)는 Physical AI 전반을 다루는 
1,640개+ 스킬 데이터를 보유하고 있다. 
오늘의 목표는 스코프를 "로봇테크 for 스마트팩토리"로 좁히고, 
해당 도메인의 스킬 온톨로지를 ESCO 기반으로 완벽하게 재설계하는 것이다.

## Step 1: 현재 데이터 구조 파악 (탐색 후 보고)

1-1. 프로젝트 루트에서 다음을 순서대로 실행하고 결과를 보고해라:
```

### Extracted Code (text)

```text
1-3. 전체 스킬 수, 도메인 수, 데이터 스키마(key 목록)를 요약 보고해라.
- 현재 데이터에 "robot", "robotics", "manufacturing", "automation" 관련 
  항목이 몇 개나 있는지 grep 또는 jq로 카운트해라.

---

## Step 2: 로봇테크 for 스마트팩토리 도메인 설계

Step 1 분석을 바탕으로, 아래 6개 도메인 구조로 새 데이터를 설계한다.

### 타겟 도메인 (6개)
1. 산업용 로봇 제어 (Industrial Robot Control)
2. 머신비전 & 센서 통합 (Machine Vision & Sensor Integration)  
3. 협동로봇 운용 (Collaborative Robot Operation)
4. 자율이동로봇 (AMR/AGV Systems)
5. 로봇 유지보수 & 진단 (Robot Maintenance & Diagnostics)
6. 디지털트윈 & 시뮬레이션 (Digital Twin & Simulation)

### 각 도메인별 스킬 구조 (ESCO 3층 모델)
각 도메인마다 아래 3층 구조로 스킬을 정의한다:
```

### Extracted Code (text)

```text
### 역할별 매핑 (3개 역할)
- Robot Operator: 장비 운용, 기본 트러블슈팅
- Robot Engineer: 프로그래밍, 시스템 통합, 최적화
- Robot Developer: 알고리즘 개발, 커스터마이징, 신기술 적용

---

## Step 3: 새 JSON 데이터 파일 생성

### 파일 경로
`public/data/robot-smartfactory.json`

### 스키마 설계 원칙
기존 ESCON JSON 스키마를 최대한 유지하되, 아래 필드를 반드시 포함해라:
```

### Extracted Code (text)

```text
### 데이터 요구사항
- 6개 도메인 × 최소 20개 스킬 = 최소 120개 스킬 정의
- 각 스킬마다 knowledge → skill → competence 계층 연결 필수
- 3개 역할(operator/engineer/developer)에 고르게 분포
- proficiency_level 1~4가 고르게 분포
- ESCO URI는 실제 ESCO API 패턴(http://data.europa.eu/esco/skill/...)을 
  따르되, 없으면 "CUSTOM-RSF-[번호]"로 표기

---

## Step 4: 데이터 검증 스크립트 작성 및 실행

`scripts/validate-robot-data.js` 파일을 만들고 아래를 검증해라:
```

### Extracted Code (text)

```text
---

## 주의사항
- 기존 파일은 절대 수정하지 말고, 새 파일만 생성한다
- ESCO 스킬명은 실제 ESCO 표준 용어를 최대한 반영한다
- 스마트팩토리 현장 맥락(smartfactory_context)은 제조업 실무자가 
  이해할 수 있는 구체적인 문장으로 작성한다
- 작업 중 판단이 필요한 부분은 임의로 결정하지 말고 질문해라
```
