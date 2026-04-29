# Extracted Knowledge from Conv: a7fb2080-f0de-434b-a3ce-d3db01d6bcf8

**Date**: 2026-03-24T06:13:58.896890Z

### Extracted Code (json)

```json
{
  "type": "message",
  "attachments": [{
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
      "actions": [{
        "type": "Action.OpenUrl",
        "title": "설문 참여하기",
        "url": "[FORMS_URL]"
      }]
    }
  }]
}
```

### Extracted Code (text)

```text
- response_id (자동 생성)
- survey_month (텍스트: "2026-04")
- q1_autonomy_1 ~ q4_autonomy_4 (숫자 1-5)
- q5_competence_1 ~ q8_competence_4 (숫자 1-5)
- q9_relation_1 ~ q11_relation_3 (숫자 1-5)
- q12_overall_1 ~ q13_overall_2 (숫자 1-5)
- submitted_at (날짜/시간)
```

### Extracted Code (sql)

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

### Extracted Code (text)

```text
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
