# Extracted Knowledge from Conv: dba915e1-a14e-4da7-881f-3f9c0f791286

**Date**: 2026-03-30T05:47:05.103510Z

### Extracted Code (markdown)

```markdown
---
name: weekly-report
description: EXG팀 주간업무 보고서 자동 생성. 업무명과 이번 주 핵심 내용을 받아 추진 업무 실적(bullet)과 상세 내용(산문) 두 컬럼을 LG 생산기술원 HR 보고서 문체로 작성한다.
triggers:
  - "주간보고서"
  - "주간 보고서"
  - "보고서 작성"
  - "weekly report"
---

# EXG팀 주간업무 보고서 작성 에이전트

## 역할
너는 LG 생산기술원 EXG팀 담당자 조대근의 주간업무 보고서를 대신 작성하는 HR 보좌 에이전트다.

## 실행 전 필수 작업
반드시 `.agent/skills/weekly-report/history.md` 파일을 읽어 각 업무의 이전 주차 맥락을 파악한 후 작성을 시작한다.

## 입력 형식
사용자가 다음 형식으로 입력한다:
```

### Extracted Code (text)

```text
### 상세 내용 (산문 형식)
3~5문장의 격식체 산문. 반드시 "이번 주에는", "~을 진행하고 있습니다", "~할 예정입니다" 패턴 사용.

## 문체 규칙
- 격식체 (~합니다, ~예정입니다, ~하고 있습니다)
- 이전 주차 완료 사항은 결과로 간략 언급
- 이번 주 신규 진행 사항 중심으로 작성
- LG 생산기술원 HR 보고서 수준 유지

## 출력 후 반드시 실행
보고서 생성 완료 후, 이번 주 추진 업무 실적을 `history.md`의 해당 업무 항목에 업데이트한다. (다음 주 연속성 유지용)

## 파일 저장
생성된 보고서를 `reports/[년도]-[월]-[주차].md` 파일로 저장한다.
```

### Extracted Code (markdown)

```markdown
# EXG팀 주간업무 히스토리
# 이 파일은 매주 보고서 생성 후 자동으로 업데이트됨

## AX 역량인증제 (모두의 AX제도변경)
- 최근 주차: 6일~10일
- 최근 실적:
  ● [AX] "모두의 AX" 인증제 운영
    - 생산기술원 관점의 최적 적용 운영안 검토 및 리뷰 준비(w/AX 커미티)
    - 신규 LV1 인증 절차 안내 및 운영
    - 각 레벨별 학습 내용 매칭 작업 진행

## AX기반의 Pulse Check 체계구축
- 최근 주차: 6일~10일
- 최근 실적:
  ● [AX] 조직 건강도 시스템 4월 MVP 범위 확정 및 모듈별 개발 착수
    - 4월 기준 MVP 구현 범위 결정
    - Pulse 화면 구성 / 구성원 Attraction / 진단 응답 모듈 개발 착수

## HR실 AX 역량 강화
- 최근 주차: 6일~10일
- 최근 실적:
  ● [AX] HR실 AX역량 강화교육 준비
    - LG화학 사내강사 초빙 협의 및 교육운영 일정(4/16, 목) 확정
    - 강의장 확보 / 구성원 참여율 제고를 위한 사전 안내 준비

## Physical AI 역량강화
- 최근 주차: 9일~14일
- 최근 실적:
  ● [AX] Physical AI Skill Inventory 구축 준비
    - Physical AI for Smart Factory 추진을 위한 스킬/역량의 체계적 가시화
    - WBS 검토 및 파일럿 대상 조직 선정 진행 중

## PRI 기술 전문가 커미티
- 최근 주차: 3일~6일
- 최근 실적:
  ● PRI 기술 전문가 커미티 개편 및 Kick off 준비
    - Kick off 일정 확정 및 커미티 멤버 안내 완료
```

### Extracted Code (yaml)

```yaml
---
name: generate-report
description: 주간보고서 생성 워크플로우. /generate-report 로 실행.
---

# 주간보고서 생성 워크플로우

## Step 1: 히스토리 로드
.agent/skills/weekly-report/history.md 파일을 읽는다.

## Step 2: 입력 수집
사용자에게 다음을 요청한다:
- 이번 주차 (예: 30일~4월3일)
- 작성할 업무 목록과 각 업무의 핵심 내용

## Step 3: 보고서 생성
weekly-report skill을 활성화해 각 업무의 추진실적과 상세내용을 작성한다.

## Step 4: 히스토리 업데이트 // turbo
history.md에 이번 주 실적을 반영한다.

## Step 5: 파일 저장 // turbo
reports/ 폴더에 마크다운 파일로 저장한다.
```

### Extracted Code (text)

```text
주차: 30일~4월3일

업무: AX 역량인증제
내용: LV2 시험 응시자 8명 결과 처리 완료, 다음 주 LV3 기준 AX 커미티 리뷰 예정

업무: Pulse Check
내용: MVP 로그인 화면 완성, Supabase 연동 테스트 중, 4월 데모 일정 확정
```

### Extracted Code (text)

```text
hr-workspace/
├── .agent/
│   ├── skills/
│   │   └── weekly-report/
│   │       ├── SKILL.md          ← 다운로드한 SKILL.md
│   │       └── history.md        ← 다운로드한 history.md
│   └── workflows/
│       └── generate-report.md    ← 다운로드한 generate-report.md
└── reports/                      ← 직접 생성 (보고서 자동 저장 폴더)
```
