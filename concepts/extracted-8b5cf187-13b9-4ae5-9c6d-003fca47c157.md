# Extracted Knowledge from Conv: 8b5cf187-13b9-4ae5-9c6d-003fca47c157

**Date**: 2026-03-07T23:04:16.054072Z

### Extracted Code (text)

```text
[Google Forms] 
    ↓ 응답 수집 (자동)
[Google Sheets - 원본 데이터] 
    ↓ Apps Script 트리거 (자동)
[Google Sheets - 분석 시트] 
    ↓ Zapier / Make (자동)
[monday.com - 대시보드]
    ↓ 자동 알림
[팀장 / HR 담당자]
```

### Extracted Code (text)

```text
[섹션 0] 안내 및 동의 (1페이지)
[섹션 1] EX Touchpoints — 리더십·인프라·협업·AX (12문항)
[섹션 2] 조직 지원 인식 — POS (8문항)
[섹션 3] 기본 심리 욕구 — SDT (9문항)
[섹션 4] 직무 몰입 — UWES (9문항)
[섹션 5] 마무리 (개방형 1문항 + 제출)
```

### Extracted Code (text)

```text
안녕하세요.

이번 Pulse Check는 여러분의 업무 경험과 조직 환경을 
이해하기 위한 분기 설문입니다.

• 소요 시간: 약 8~10분
• 응답 방식: 완전 익명 처리
• 결과 활용: 팀/조직 단위 집계 후 개선 활동에 반영
  (개인 응답은 HR 외 누구에게도 공유되지 않습니다)

솔직한 응답이 가장 정확한 진단을 만듭니다.
감사합니다.
```

### Extracted Code (javascript)

```javascript
// 트리거: 폼 응답 제출 시 자동 실행
function onFormSubmit(e) {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const rawSheet = ss.getSheetByName('원본응답');
  const scoreSheet = ss.getSheetByName('점수집계');
  
  // 열 인덱스 정의 (Forms 순서에 맞게 조정)
  const COL = {
    timestamp: 0,
    // EX Touchpoints: 열 1~12
    ex_start: 1, ex_end: 12,
    // POS: 열 13~20
    pos_start: 13, pos_end: 20,
    // SDT: 열 21~29 (자율성 21~23, 유능감 24~26, 관계성 27~29)
    sdt_auto_start: 21, sdt_auto_end: 23,
    sdt_comp_start: 24, sdt_comp_end: 26,
    sdt_rel_start: 27, sdt_rel_end: 29,
    // UWES: 열 30~38 (활력 30~32, 헌신 33~35, 몰두 36~38)
    uwes_vig_start: 30, uwes_vig_end: 32,
    uwes_ded_start: 33, uwes_ded_end: 35,
    uwes_abs_start: 36, uwes_abs_end: 38,
  };

  const lastRow = rawSheet.getLastRow();
  const response = rawSheet.getRange(lastRow, 1, 1, 39).getValues()[0];

  // 섹션별 평균 계산
  function avg(start, end) {
    const vals = response.slice(start, end + 1).map(Number);
    return vals.reduce((a, b) => a + b, 0) / vals.length;
  }

  const scores = {
    timestamp: response[COL.timestamp],
    ex_leadership: avg(1, 3),
    ex_infra: avg(4, 6),
    ex_collab: avg(7, 9),
    ex_ax: avg(10, 12),
    ex_total: avg(COL.ex_start, COL.ex_end),
    pos_total: avg(COL.pos_start, COL.pos_end),
    sdt_autonomy: avg(COL.sdt_auto_start, COL.sdt_auto_end),
    sdt_competence: avg(COL.sdt_comp_start, COL.sdt_comp_end),
    sdt_relatedness: avg(COL.sdt_rel_start, COL.sdt_rel_end),
    sdt_total: avg(COL.sdt_auto_start, COL.sdt_rel_end),
    uwes_vigor: avg(COL.uwes_vig_start, COL.uwes_vig_end),
    uwes_dedication: avg(COL.uwes_ded_start, COL.uwes_ded_end),
    uwes_absorption: avg(COL.uwes_abs_start, COL.uwes_abs_end),
    uwes_total: avg(COL.uwes_vig_start, COL.uwes_abs_end),
  };

  // 점수집계 시트에 행 추가
  scoreSheet.appendRow([
    scores.timestamp,
    scores.ex_leadership, scores.ex_infra, 
    scores.ex_collab, scores.ex_ax, scores.ex_total,
    scores.pos_total,
    scores.sdt_autonomy, scores.sdt_competence, 
    scores.sdt_relatedness, scores.sdt_total,
    scores.uwes_vigor, scores.uwes_dedication, 
    scores.uwes_absorption, scores.uwes_total
  ]);
}
```

### Extracted Code (javascript)

```javascript
// 트리거: 매일 오전 9시 실행
function checkResponseRate() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const rawSheet = ss.getSheetByName('원본응답');
  
  const totalResponses = rawSheet.getLastRow() - 1; // 헤더 제외
  const TARGET_PARTICIPANTS = 50; // 파일럿 대상 인원으로 수정
  const responseRate = totalResponses / TARGET_PARTICIPANTS;
  
  const surveyDeadline = new Date('2026-03-19');
  const today = new Date();
  const daysLeft = Math.ceil((surveyDeadline - today) / (1000 * 60 * 60 * 24));
  
  if (responseRate < 0.7 && daysLeft <= 3) {
    GmailApp.sendEmail(
      'your-email@lg.com', // HR 담당자 이메일
      '[Pulse Check] 응답률 알림 — 마감 ' + daysLeft + '일 전',
      `현재 응답률: ${Math.round(responseRate * 100)}% (${totalResponses}명/${TARGET_PARTICIPANTS}명)\n` +
      `마감일: 2026-03-19\n\n` +
      `응답률이 70% 미달입니다. 팀장에게 리마인드를 요청해주세요.`
    );
  }
}
```

### Extracted Code (text)

```text
[트리거] Google Sheets — 새 행 추가 감지 (점수집계 시트)
    ↓
[필터] 총 응답 수 >= 5 (소수 응답 시 노이즈 방지)
    ↓
[액션 1] monday.com — 아이템 업데이트
         보드: "Pulse Check 대시보드"
         컬럼: EX/POS/SDT/UWES 각 점수 업데이트
    ↓
[액션 2] 조건 분기
         IF UWES 총점 < 3.5 (7점 기준)
         → monday.com 알림 생성 "⚠️ 몰입도 주의 구간"
         IF AX 체감도 < 3.0 (5점 기준)  
         → monday.com 알림 생성 "⚠️ AX 체감도 낮음"
```

### Extracted Code (text)

```text
[MS Forms]           ← Google Forms 대체
    ↓ 자동 연동
[Excel Online / SharePoint]  ← Google Sheets 대체
    ↓ Power Automate 트리거
[Power BI 대시보드]   ← Looker Studio 대체
    ↓
[monday.com or Teams 알림]
```

### Extracted Code (text)

```text
[monday WorkForms]   ← 설문 수집
    ↓ 자동 (내장)
[monday 보드]        ← 데이터 집계
    ↓ 자동화 레시피
[대시보드 뷰]        ← 실시간 시각화
    ↓ 알림 자동화
[팀장 / HR]
```

### Extracted Code (text)

```text
[Tally.so]           ← 설문 수집 (Notion 최적 연동)
    ↓ Zapier/Make
[Notion 데이터베이스] ← 응답 자동 적재
    ↓ 수식/집계
[Notion 대시보드]    ← 팀별 현황 시각화
```

### Extracted Code (text)

```text
[MS Forms]
    ↓ 자동 연동 (네이티브)
[SharePoint / Excel Online]
    ↓ Power Automate 플로우
[Power BI 대시보드]
    ↓ Teams 알림 자동화
[팀장 / HR 담당자]
```

### Extracted Code (text)

```text
[섹션 1] 안내 및 시작
[섹션 2] EX Touchpoints (12문항)
[섹션 3] POS + SDT (17문항)
[섹션 4] UWES (9문항)
[섹션 5] 자유 응답 + 제출
```

### Extracted Code (text)

```text
[원본응답 시트]     ← Forms가 자동으로 채움 (손대지 않음)
[점수집계 시트]     ← Power Automate가 자동으로 채움
[대시보드 시트]     ← Power BI가 읽어가는 소스
```

### Extracted Code (text)

```text
① [트리거] MS Forms — 새 응답 제출됨
    ↓
② [액션] MS Forms — 응답 세부 정보 가져오기
    (각 문항 응답값 추출)
    ↓
③ [액션] 변수 초기화 — 섹션별 점수 계산
    ex_leadership = (Q1 + Q2 + Q3) / 3
    ex_infra = (Q4 + Q5 + Q6) / 3
    ex_collab = (Q7 + Q8 + Q9) / 3
    ex_ax = (Q10 + Q11 + Q12) / 3
    pos_total = (Q13~Q20) / 8
    sdt_total = (Q21~Q29) / 9
    uwes_total = (Q30~Q38) / 9
    ↓
④ [액션] Excel Online — 행 추가
    (점수집계 시트에 계산된 값 삽입)
    ↓
⑤ [조건] UWES 종합 < 3.5 (7점 기준) OR AX 체감 < 3.0
    YES → 플로우 2 트리거 (알림 발송)
    NO  → 종료
```

### Extracted Code (text)

```text
① [트리거] 매일 오전 9:00 예약 실행
    ↓
② [액션] Excel Online — 행 수 가져오기
    (원본응답 시트의 총 행 수 = 응답 수)
    ↓
③ [액션] 변수 계산
    응답률 = 응답수 / 파일럿대상인원(50)
    마감까지_남은일 = 3월19일 - 오늘
    ↓
④ [조건] 응답률 < 0.7 AND 남은일 <= 3
    YES →
    ⑤ [액션] Teams — 채널 메시지 게시
       "⚠️ Pulse Check 응답률 알림
        현재: XX% (XX명/50명)
        마감: 3월 19일 (D-N)
        → 팀장 리마인드 필요"
    NO  → 종료
```

### Extracted Code (text)

```text
① [트리거] SharePoint 특정 파일 업데이트 감지
    (HR이 "분석완료" 체크박스 클릭 시)
    ↓
② [액션] Excel — 팀별 데이터 읽기
    ↓
③ [루프] 각 팀장에게 반복
    ④ [액션] Outlook — 개인화 이메일 발송
       제목: "[Pulse Check] 우리 팀 결과 공유"
       내용: 팀별 점수 + 전체 평균 비교 자동 삽입
```

### Extracted Code (text)

```text
1월    2월    3월    4월    5월    6월
월간(13)  ●      ●      ●      ●      ●      ●
분기(25)  ●                    ●
                                              
전체(38)  ●      ○      ○      ●      ○      ○

● = 전체 or 분기 운영  ○ = 월간만 운영
```
