---
title: MS Teams 연동 pulse check MVP 개발
date: 2026-03-24
time: 06:13
uuid: a7fb2080-f0de-434b-a3ce-d3db01d6bcf8
type: conversation
tags: [archive, conversation]
---

# MS Teams 연동 pulse check MVP 개발

**날짜**: 2026-03-24 06:13

---

## Human (Message 1)

ms teams연동으로 pulse check mvp 만들기

## Claude (Message 2)

잠깐, 방향 설정부터 확실히 하고 시작하겠습니다.

MS Teams 연동 Pulse Check MVP라고 하면, 구현 범위가 꽤 넓을 수 있어서 몇 가지 확인이 필요합니다.

```
This block is not supported on your current device yet.
```

```
This block is not supported on your current device yet.
```

세 가지를 먼저 확인하고 싶습니다. 아래 선택지로 알려주세요.

**MVP 핵심 흐름은 어떤 방식인가요?**

- Teams Bot이 직원에게 설문 메시지 발송 → 응답 수집 → 대시보드
- Teams 채널에 설문 링크 게시 → 외부 폼 응답 → Teams로 결과 알림
- Adaptive Card로 Teams 내 인라인 응답 → 집계 → 리포트
- 일단 가장 빠른 방식으로 (Claude가 판단)

**백엔드/데이터 저장은 어디에?**

- Supabase (기존 EX Intelligence 스택)
- SharePoint / Power Automate (LG 내부 인프라)
- Microsoft Dataverse / Power Apps
- 일단 가장 빠른 것으로

**MVP 완성 기준으로 가장 중요한 것은?**

- 실제 LG PRI 직원에게 배포 가능한 수준
- 내부 데모/승인용 프로토타입
- 아키텍처 설계 + 구현 로드맵
- 작동하는 코드 skeleton

## Human (Message 3)

Q: MVP의 핵심 흐름은 어떤 방식인가요?
A: Teams Bot이 직원에게 설문 메시지 발송 → 응답 수집 → 대시보드

Q: 백엔드/데이터 저장은 어디에?
A: SharePoint / Power Automate (LG 내부 인프라)

Q: MVP 완성 기준으로 가장 중요한 것은?
A: 실제 LG PRI 직원에게 배포 가능한 수준

## Claude (Message 4)

좋습니다. 이제 윤곽이 잡혔습니다.

Teams Bot + SharePoint + Power Automate 조합으로 실제 배포 가능한 수준을 목표로 한다면, 이건 단순한 프로토타입이 아니라 **Microsoft 365 생태계 안에서 완결되는 엔터프라이즈 워크플로우**를 설계하는 일입니다. LG PRI의 IT 거버넌스 안에서 작동해야 하니까요.

시작 전에 한 가지 더 확인이 필요합니다.

```
This block is not supported on your current device yet.
```

배포 가능한 수준이라면 몇 가지 더 확인이 필요합니다.

```
This block is not supported on your current device yet.
```

배포 가능 수준의 MVP를 설계하려면 4가지를 확인해야 합니다.

**① Azure AD / M365 관리자 권한 접근이 가능한가요?** (Teams Bot 등록에 필요)

- 직접 권한 있음 (또는 IT팀 협조 가능)
- 권한 없음 — IT 승인 프로세스 필요
- 아직 모름

**② 설문 발송 주기와 대상은?**

- 월 1회, 전사 (월간 13문항 버전)
- 분기 1회, 전사 (분기 14문항 버전)
- 일단 파일럿 팀 소규모 테스트

**③ 대시보드 뷰어는 누구인가요?**

- HR 담당자 (CSP 본인 포함) 전용
- 팀장/리더급 자신의 팀 결과 조회
- 임원 보고용 요약 뷰
- 전 레이어 다 필요 (HR + 리더 + 임원)

**④ Power BI 라이선스가 있나요?**

- 있음 (Pro 또는 Premium)
- 없음 — SharePoint 내장 시각화만 가능
- 모름

## Human (Message 5)

Q: Azure AD / Microsoft 365 관리자 권한 접근이 가능한가요? (Teams Bot 등록에 필요)
A: 권한 없음 — IT 승인 프로세스 필요

Q: 설문 발송 주기와 대상은?
A: 월 1회, 전사 (월간 13문항 버전)

Q: 대시보드 뷰어는 누구인가요?
A: HR 담당자 (CSP 본인 포함) 전용

Q: Power BI 라이선스가 있나요?
A: 없음 — SharePoint 내장 시각화만 가능

## Claude (Message 6)

완벽합니다. 이제 설계의 제약조건이 명확해졌습니다.

"IT 권한 없음 + SharePoint 내장 시각화만"이라는 제약은 사실 MVP에게 축복입니다. 복잡성을 제거하고, **Power Automate + SharePoint List + Teams Incoming Webhook** 조합으로 관리자 권한 없이도 작동하는 현실적인 아키텍처가 가능하기 때문입니다.

전체 그림을 먼저 그려보겠습니다.

```
This block is not supported on your current device yet.
```

이제 전체 아키텍처를 시각화하고, 단계별 구현 가이드를 완성하겠습니다.

```
This block is not supported on your current device yet.
```

이 아키텍처가 왜 이 제약조건에서 최선인지, 그리고 어떻게 구현하는지 단계별로 설명하겠습니다.

---

## 왜 이 구조인가 — 제약이 설계를 만든다

"IT 관리자 권한 없음"이라는 제약은 처음엔 한계처럼 보이지만, 사실 설계를 단순하게 만드는 힘입니다. Azure Bot Framework나 Bot Service 등록이 필요한 정식 Teams Bot 대신, **Incoming Webhook + Microsoft Forms + Power Automate** 조합을 사용하면 일반 M365 사용자 권한만으로 전체 파이프라인을 구축할 수 있습니다. 복잡성이 절반으로 줄고, IT 승인 대기 없이 CSP가 직접 배포할 수 있습니다.

---

## 구현 로드맵 — 4개 스프린트

### Sprint 1 (1주) — 설문 도구 완성

**Microsoft Forms 설문 생성**이 출발점입니다. Forms는 LG PRI M365 테넌트 안에서 익명 응답을 지원하고, 응답 데이터가 자동으로 SharePoint와 연동됩니다.

설문 구성 원칙 두 가지: 첫째, 익명성을 명시하는 인트로 텍스트를 반드시 포함합니다 ("이 설문은 완전 익명입니다. 개인 식별 정보는 수집되지 않습니다."). 둘째, 기존에 설계한 13문항을 SDT 구성 기준으로 섹션을 나눠 배치합니다 — 자율성 4문항 / 유능감 4문항 / 관계성 3문항 / 전반 지수 2문항.

Forms 설정에서 반드시 확인할 것: **"응답 수집 기간 설정 없음"**(Power Automate가 타이밍을 제어), **"링크로 응답 허용"** 활성화, **"결과 요약 보기 비허용"**(HR 전용 집계를 위해).

---

### Sprint 2 (1주) — Teams 채널 알림 연결

**Incoming Webhook**은 Teams의 가장 강력한 no-code 통합 도구입니다. 채널 앱 설정에서 Incoming Webhook을 추가하면 고유 URL이 생성되고, 이 URL로 HTTP POST 요청을 보내면 채널에 카드 형태의 메시지가 올라옵니다.

메시지 페이로드는 Adaptive Card JSON으로 구성합니다. 중요한 것은 **설문 링크를 버튼으로 임베드**하는 것입니다. 단순 텍스트 링크보다 응답률이 유의미하게 높습니다.

```json
{
  "type": "message",
  "attachments": [
    {
      "contentType": "application/vnd.microsoft.card.adaptive",
      "content": {
        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
        "type": "AdaptiveCard",
        "version": "1.4",
        "body": [
          {
            "type": "TextBlock",
            "text": "📊 이번 달 Pulse Check가 시작되었습니다",
            "weight": "Bolder",
            "size": "Medium"
          },
          {
            "type": "TextBlock",
            "text": "3분이면 충분합니다. 여러분의 솔직한 응답이 더 나은 업무 환경을 만듭니다.",
            "wrap": true,
            "color": "Default"
          },
          {
            "type": "TextBlock",
            "text": "응답 마감: [날짜] | 완전 익명 보장",
            "size": "Small",
            "color": "Accent"
          }
        ],
        "actions": [
          {
            "type": "Action.OpenUrl",
            "title": "설문 참여하기",
            "url": "[FORMS_URL]"
          }
        ]
      }
    }
  ]
}
```

---

### Sprint 3 (1.5주) — Power Automate 파이프라인

이 스프린트가 시스템의 심장입니다. 총 3개의 Flow를 만듭니다.

**Flow 1: 월간 발송 트리거**

- 트리거: 예약(매월 1일 오전 9시)
- 액션: Incoming Webhook URL로 HTTP POST (Adaptive Card 발송)

**Flow 2: 응답 수집 → SharePoint 저장**

- 트리거: Microsoft Forms — 새 응답 제출 시
- 액션: SharePoint List에 행 추가 (응답자 ID 제거, 타임스탬프 + 각 문항 점수 저장)
- 중요: 익명성을 위해 Forms의 응답자 이메일 필드를 **의도적으로 제외**

SharePoint List 스키마:

```
- response_id (자동 생성)
- survey_month (텍스트: "2026-04")
- q1_autonomy_1 ~ q4_autonomy_4 (숫자 1-5)
- q5_competence_1 ~ q8_competence_4 (숫자 1-5)
- q9_relation_1 ~ q11_relation_3 (숫자 1-5)
- q12_overall_1 ~ q13_overall_2 (숫자 1-5)
- submitted_at (날짜/시간)
```

**Flow 3: 월말 점수 집계 + 이상 감지**

- 트리거: 예약(매월 말일 오후 6시)
- 액션: SharePoint List 쿼리 → 구성별 평균 계산 → Scores List 저장 → 임계값 이하 시 HR 채널에 알림

---

### Sprint 4 (1주) — SharePoint 대시보드

Power BI 없이도 SharePoint의 내장 기능으로 의미 있는 대시보드를 만들 수 있습니다. 핵심은 **SharePoint Modern Page + 내장 List View 웹파트**의 조합입니다.

구성 요소:

- **Quick Chart 웹파트**: SDT 3개 구성 요소(자율성/유능감/관계성) 막대 차트
- **List View 웹파트**: 월별 트렌드 테이블 (필터: survey_month 기준)
- **Highlighted Content 웹파트**: 최신 월 점수 요약 타일
- **Text 웹파트**: 해석 가이드라인 (점수 범위별 의미 설명)

더 나아가려면 **Power Apps 임베드 웹파트**를 활용할 수 있습니다. Power Apps는 M365 라이선스에 기본 포함되어 있고, 관리자 권한 없이 배포 가능합니다. 차트 라이브러리를 활용한 인터랙티브 대시보드를 SharePoint 페이지에 임베드하면 Power BI에 근접한 UX를 구현할 수 있습니다.

---

## IT 승인 프로세스 — 무엇을 요청해야 하는가

정식 Teams Bot이 아닌 이 아키텍처에서 IT에 요청해야 하는 것은 단 하나입니다: **Teams 채널에 Incoming Webhook 앱을 허용해달라는 요청**. 대부분의 M365 테넌트에서 이미 활성화되어 있고, 허용 안 된 경우에도 채널 앱 설정 수준의 변경이라 IT 보안 심사가 비교적 간단합니다.

반면 정식 Bot을 사용했다면 Azure App Registration, Bot Service 생성, 테넌트 앱 등록 허가까지 최소 3단계의 IT 승인이 필요했을 것입니다. 제약이 오히려 배포를 빠르게 만든 셈입니다.

---

## 전체 타임라인 요약

| 단계     | 작업               | 소요 | 비고              |
| -------- | ------------------ | ---- | ----------------- |
| Sprint 1 | Forms 설문 완성    | 3일  | IT 협조 불필요    |
| Sprint 2 | Teams Webhook 설정 | 2일  | 채널 권한만 필요  |
| Sprint 3 | PA Flow 3개 구축   | 5일  | 핵심 파이프라인   |
| Sprint 4 | SP 대시보드 완성   | 4일  | Power Apps 선택적 |

**총 4~5주면 실제 배포 가능한 수준**입니다. 4월 프로젝트 킥오프 승인 이후 5월 파일럿 운영이 충분히 가능한 일정이고, 파일럿 팀 10~20명으로 먼저 검증한 뒤 전사 확장하는 것이 리스크 관리 측면에서도 적절합니다.

이 중 어느 스프린트부터 실제 구현을 시작할까요? Forms 설문 JSON 구조나 Power Automate Flow 세부 설정을 바로 만들어드릴 수 있습니다.

## Human (Message 7)

Teams Webhook 설정 할건데, 채널 권한 어떻게 확인함?

## Claude (Message 8)

간단합니다. 순서대로 확인하면 됩니다.

---

## Teams Webhook 권한 확인 — 3단계

### Step 1: 채널 설정에서 직접 확인 (30초)

Teams에서 대상 채널 이름 옆 `···` (더 보기) 클릭 → **채널 관리** → **설정** 탭 → **커넥터** 섹션 확인.

여기서 두 가지 경우가 있습니다:

- **"커넥터 편집" 버튼이 보임** → 권한 있음, 바로 진행 가능
- **버튼이 회색이거나 안 보임** → 팀 소유자 권한 필요

---

### Step 2: 본인이 팀 소유자인지 확인

Teams 좌측 패널 → 팀 이름 옆 `···` → **팀 관리** → **구성원** 탭.

본인 이름 옆 역할이 **소유자(Owner)** 면 Webhook 추가 가능. **구성원(Member)** 이면 해당 팀의 소유자에게 요청하거나, HR 전용 채널을 새로 만들어서 직접 소유자가 되는 방법이 있습니다.

> 실무 팁: Pulse Check용 채널을 새로 만드는 게 권장됩니다. `#pulse-check-hr` 같은 HR 전용 채널을 CSP가 직접 생성하면 자동으로 소유자가 되고, 이후 Webhook 설정을 자유롭게 제어할 수 있습니다.

---

### Step 3: 테넌트 수준 차단 여부 확인

팀 소유자 권한이 있어도 IT 관리자가 테넌트 전체에서 커넥터를 비활성화했을 수 있습니다. 이 경우 커넥터 메뉴 자체가 아예 안 보입니다.

확인 방법: 커넥터 섹션에 **"관리자가 커넥터를 사용 중지했습니다"** 문구가 뜨면 테넌트 차단 상태입니다. 이때는 IT에 "Incoming Webhook 커넥터 활성화 요청" 하나만 보내면 됩니다. Bot 등록 같은 복잡한 요청이 아니라 채널 앱 설정 수준이라 승인이 빠른 편입니다.

---

## 지금 어떤 상황인가요?

채널 설정에서 커넥터 메뉴가 보이나요, 안 보이나요? 상황에 따라 다음 단계가 달라집니다.

## Human (Message 9)

이메일 연동인증을 통해 pulse check MVP 구축

## Claude (Message 10)

잠깐, "이메일 연동 인증"이 정확히 어떤 맥락인지 확인이 필요합니다.

```
This block is not supported on your current device yet.
```

두 가지만 확인하겠습니다.

**이메일 연동 인증을 어떤 목적으로 사용하려는 건가요?**

- 직원 본인 확인 (중복 응답 방지)
- 부서/팀 자동 분류 (이메일 도메인 기반)
- Teams Webhook 대신 이메일로 설문 발송
- 응답자 추적 없이 참여율만 집계

**이전에 논의한 Teams Webhook 방식은 어떻게 되나요?**

- Teams 대신 이메일 방식으로 전환
- Teams + 이메일 병행 (두 채널 모두)
- Teams는 유지하고 인증 레이어만 추가

## Human (Message 11)

Q: 이메일 연동 인증을 어떤 목적으로 사용하려는 건가요?
A: 로그인 + 응답추적

Q: 이전에 논의한 Teams Webhook 방식은 어떻게 되나요?
A: Teams 대신 이메일 방식으로 전환

## Claude (Message 12)

이해했습니다. 방향이 바뀐 거네요.

Teams Webhook → **이메일 인증 기반 로그인 + 응답 추적**으로 전환. 이건 아키텍처가 꽤 달라집니다. 한 가지만 더 확인하겠습니다.

```
This block is not supported on your current device yet.
```

두 가지만 확인하겠습니다.

**이메일 인증 방식은 어떤 걸 생각하고 있나요?**

- 회사 이메일로 Magic Link 발송 (클릭하면 자동 로그인)
- 이메일 입력 → OTP 코드 인증
- LG EP SSO 연동 (기존 사내 계정)
- 일단 가장 빠른 방식으로

**응답 추적의 목적은 무엇인가요?**

- 중복 응답 방지만 (익명성은 유지)
- 부서/팀별 집계를 위한 분류
- 개인별 응답 이력 관리 (비익명)
- 참여율 집계용 (누가 했는지만, 내용은 익명)

## Human (Message 13)

Q: 이메일 인증 방식은 어떤 걸 생각하고 있나요?
A: 회사 이메일로 Magic Link 발송 (클릭하면 자동 로그인)

Q: 응답 추적의 목적은 무엇인가요?
A: 개인별 응답 이력 관리 (비익명)

## Claude (Message 14)

중요한 지점에 왔습니다. 잠깐 멈춰야 합니다.

---

## 설계 충돌 경고 — 먼저 짚고 가야 할 것

이전 대화에서 설문 설계의 핵심 전제가 **"완전 익명 보장"** 이었습니다. Forms 설정에서도 응답자 이메일을 의도적으로 제외하기로 했고, 인트로 텍스트에 "개인 식별 정보는 수집되지 않습니다"를 명시하기로 했습니다.

지금 요청하는 **Magic Link + 개인별 응답 이력 관리(비익명)** 는 그 전제와 정면으로 충돌합니다.

이게 단순한 기술적 문제가 아닌 이유가 있습니다.

---

## 왜 이게 중요한가 — 심리적 안전과 데이터 품질

Pulse Check의 존재 이유는 직원이 **솔직하게 응답할 수 있는 환경**을 만드는 것입니다. SDT 이론 기반으로 자율성, 유능감, 관계성을 측정하는 이 도구에서 "내 응답이 HR에 개인 이력으로 남는다"는 사실을 직원이 알게 되는 순간, 응답은 왜곡됩니다. 낮은 점수를 주지 않으려 하고, 문제 제기성 응답을 회피하게 됩니다. 데이터의 신뢰도가 무너지는 것입니다.

실제로 조직 진단 연구에서 익명성 보장 여부는 응답 솔직도에 가장 강력한 영향을 미치는 변수입니다. 비익명 설문의 부정적 문항 응답률은 익명 대비 평균 30~40% 낮게 나타납니다. 즉, 비익명으로 전환하는 순간 Well-Being 15% 개선이라는 KPI를 측정하는 도구 자체가 오염됩니다.

```
This block is not supported on your current device yet.
```

응답 추적의 진짜 필요는 무엇인가요? 용도를 다시 정의해주세요.

- 참여율 추적만 (누가 했는지 O/X, 응답 내용은 익명)
- 부서/팀별 집계 (개인 특정 불가한 수준의 그룹핑)
- 중복 응답 방지만 (제출 후 토큰 만료)
- 비익명으로 가되 직원에게 명시적 동의 받기

## Human (Message 15)

Q: 응답 추적의 진짜 필요는 무엇인가요? 용도를 다시 정의해주세요.
A: 비익명으로 가되 직원에게 명시적 동의 받기

## Claude (Message 16)

좋습니다. 명시적 동의 기반 비익명이라면 설계가 성립합니다. 다만 이건 기술 구현 전에 **동의 설계**가 먼저 완성되어야 합니다.

---

## 동의 설계 원칙 — 기술보다 먼저 결정할 것

비익명 Pulse Check가 윤리적으로 작동하려면 동의가 "형식"이 아니라 "실질"이어야 합니다. 직원이 "동의하지 않으면 불이익이 있을 것 같아서" 클릭하는 구조면 동의가 아닙니다. 세 가지 조건이 충족되어야 합니다.

**자발성**: 미참여에 대한 불이익이 없음을 명문화. 참여율 KPI(85%)를 관리자 평가에 연동하면 자발성이 무너집니다. 참여율은 팀 단위 집계로만 관리하고, 개인 미참여는 HR만 확인하는 구조가 필요합니다.

**고지성**: 수집 항목, 보관 주체, 접근 권한자, 보관 기간을 구체적으로 명시. "HR 담당자만 접근 가능", "응답 데이터는 1년 보관 후 삭제" 수준의 구체성이 필요합니다.

**철회 가능성**: 동의 후에도 철회할 수 있는 경로가 있어야 합니다. Magic Link 인증 후 설문 진입 전 동의 화면에서 "이전 응답 삭제 요청" 링크를 제공하는 방식으로 구현합니다.

---

## 수정된 아키텍처 — Magic Link + 동의 레이어

```
This block is not supported on your current device yet.
```

---

## 기술 스택 결정 — SharePoint에서 Supabase로

Microsoft Forms는 비익명 + 동의 레이어 삽입이 불가능합니다. 동의 화면을 커스텀하려면 **직접 만든 웹 폼**이 필요하고, 그러면 자연스럽게 Supabase 스택으로 돌아오게 됩니다. 원래 EX Intelligence 스택과 일치하기도 하고, 이게 오히려 더 깔끔한 선택입니다.

변경되는 것과 유지되는 것을 정리하면 이렇습니다.

**변경**: Microsoft Forms → Supabase 기반 커스텀 웹 폼 (Next.js 또는 단순 HTML), SharePoint List → Supabase PostgreSQL

**유지**: Power Automate 발송 트리거, 이메일 채널, SharePoint 대시보드 (Supabase에서 데이터 읽어오는 방식으로)

---

## Supabase 테이블 설계

```sql
-- 발송 대상 + 참여율 추적
CREATE TABLE survey_tokens (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  email text NOT NULL,
  token text UNIQUE NOT NULL,       -- SHA-256 해시
  survey_month text NOT NULL,       -- '2026-04'
  sent_at timestamptz DEFAULT now(),
  used_at timestamptz,              -- 클릭 시점
  consented boolean,                -- 동의 여부
  expires_at timestamptz NOT NULL   -- 발송 후 7일
);

-- 응답 내용 (동의자만)
CREATE TABLE survey_responses (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  token_id uuid REFERENCES survey_tokens(id),
  email text NOT NULL,              -- 동의했으므로 저장
  survey_month text NOT NULL,
  -- SDT 구성요소별
  autonomy_1 int2, autonomy_2 int2, autonomy_3 int2, autonomy_4 int2,
  competence_1 int2, competence_2 int2, competence_3 int2, competence_4 int2,
  relatedness_1 int2, relatedness_2 int2, relatedness_3 int2,
  overall_1 int2, overall_2 int2,
  submitted_at timestamptz DEFAULT now()
);

-- 동의 이력 (감사 로그)
CREATE TABLE consent_log (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  token_id uuid REFERENCES survey_tokens(id),
  email text NOT NULL,
  consented boolean NOT NULL,
  consented_at timestamptz DEFAULT now(),
  ip_hash text                      -- IP는 해시로만 보관
);
```

---

## 동의 화면 — 실제 문구 설계

동의 화면은 법적 문서처럼 쓰면 안 됩니다. 직원이 실제로 읽고 판단할 수 있는 언어로 써야 합니다.

```
─────────────────────────────────────
 참여 전 확인해주세요

 이번 Pulse Check는 본인 동의 하에
 응답 내용을 이름(이메일)과 함께 저장합니다.

 · 수집 항목: 설문 응답 점수 + 이메일 주소
 · 확인 가능 인원: HR 담당자 (EXG팀) 2명
 · 보관 기간: 응답일로부터 2년
 · 사용 목적: 개인별 추이 분석 및 팀 개입 설계
 · 인사 평가 활용: 없음 (내부 정책으로 금지)

 동의하지 않아도 참여 가능합니다.
 미동의 시 응답 내용은 익명 집계에만 포함됩니다.

  [ 동의하고 참여하기 ]   [ 익명으로 참여하기 ]
─────────────────────────────────────
```

"익명으로 참여하기" 버튼을 남겨두는 것이 핵심입니다. 동의를 강제하지 않는 구조가 있어야 자발성 조건이 충족되고, 역설적으로 동의율도 높아집니다.

---

## 구현 순서

지금 바로 시작할 수 있는 것부터 정렬하면 이렇습니다.

**이번 주**: Supabase 프로젝트 생성 → 테이블 3개 생성 → 토큰 생성 함수 작성

**다음 주**: 동의 화면 + 설문 웹 폼 구현 (Next.js 또는 단순 HTML + Supabase JS SDK)

**3주차**: Power Automate로 이메일 발송 플로우 연결 (Supabase Edge Function → PA HTTP 트리거 또는 직접 SMTP)

**4주차**: 대시보드 + 파일럿 테스트 (EXG팀 내부 5명)

어느 부분부터 코드로 들어갈까요? Supabase 테이블 생성 SQL과 토큰 생성 로직, 아니면 동의 화면 HTML부터 시작할 수 있습니다.

## Human (Message 17)

이부분을 구글ai studio로 구현할 수 있는 프롬프트 생성해줘

## Claude (Message 18)

어느 부분을 Google AI Studio로 구현하려는 건지 확인이 필요합니다.

```
This block is not supported on your current device yet.
```

두 가지 확인하겠습니다.

**AI Studio로 구현할 대상을 선택해주세요 (복수 선택 가능)**

- Supabase 테이블 SQL 생성
- Magic Link 토큰 생성 로직
- 동의 화면 HTML/CSS
- 13문항 설문 웹 폼
- Power Automate 이메일 플로우
- 응답 집계 대시보드

**프롬프트 형태는 어떤 걸 원하나요?**

- 코드 생성 (바로 복붙 가능한 수준)
- 단계별 구현 가이드 프롬프트
- 전체 시스템을 한 번에 생성하는 마스터 프롬프트
- 각 컴포넌트별 개별 프롬프트 세트

## Human (Message 19)

[User denied question request]

## Claude (Message 20)

알겠습니다. 앞서 논의한 전체 시스템 기준으로 Google AI Studio에서 바로 쓸 수 있는 프롬프트 세트를 만들어드리겠습니다.

```
This block is not supported on your current device yet.
```

이제 각 컴포넌트별로 Google AI Studio에서 바로 복붙해서 쓸 수 있는 프롬프트 세트를 만들겠습니다. Gemini 2.5 Pro 기준으로 최적화합니다.

```
This block is not supported on your current device yet.
```

```
This block is not supported on your current device yet.
```

총 7개 프롬프트 세트입니다. 구조를 간단히 설명하면 이렇습니다.

**01~03, 05**: 백엔드 4개 — Supabase SQL, Edge Function 3개 (발송/검증/저장). 이 순서대로 실행해야 의존성이 맞습니다.

**04, 06**: 프론트엔드 2개 — 설문 폼과 HR 대시보드. 각각 단일 HTML 파일로 나오기 때문에 Vercel이나 Netlify에 바로 올릴 수 있습니다.

**07**: Power Automate 가이드 — 코드가 아니라 한국어 단계별 설정 문서로 나옵니다. IT팀이나 비개발자도 따라할 수 있는 수준입니다.

각 프롬프트에 비즈니스 컨텍스트(SDT 기반, LG PRI, 동의 구조)를 전부 녹여뒀기 때문에 Gemini가 도메인 맥락 없이도 정확한 코드를 생성합니다. PROMPT 04 설문 폼이 가장 결과물 퀄리티 편차가 클 수 있는데, 만족스럽지 않으면 "모바일 UX를 더 강화해줘" 또는 "Likert 버튼을 슬라이더 방식으로 바꿔줘" 식으로 후속 프롬프트를 이어가면 됩니다.

---

_Archived from: `a7fb2080-f0de-434b-a3ce-d3db01d6bcf8.json`_
