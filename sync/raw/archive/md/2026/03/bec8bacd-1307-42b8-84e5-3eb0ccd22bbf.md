---
title: 엑셀 데이터 기반 개별 이메일 자동 생성
date: 2026-03-18
time: 00:16
uuid: bec8bacd-1307-42b8-84e5-3eb0ccd22bbf
type: conversation
tags: [archive, conversation]
---

# 엑셀 데이터 기반 개별 이메일 자동 생성

**날짜**: 2026-03-18 00:16

---

## Human (Message 1)

첨부 엑셀파일의 데이터를 근거로 개별 이메일을 작성할거야.
수신 : [PL] [직위]

하단 엑셀 리스트 [PL]열에 표시된 대상자의 이름으로 소팅한 엑셀값
개별 메일을 eml파일로 생성 후, 아웃룩에서 발송

최적 방안을 제안해줘

## Claude (Message 2)

```
This block is not supported on your current device yet.
```

```
This block is not supported on your current device yet.
```

```
This block is not supported on your current device yet.
```

```
This block is not supported on your current device yet.
```

```
This block is not supported on your current device yet.
```

```
This block is not supported on your current device yet.
```

```
This block is not supported on your current device yet.
```

데이터 구조를 완전히 파악했습니다. 이제 최적 방안을 제안하고 실제 eml 파일을 생성하는 Python 스크립트를 만들겠습니다.

```
This block is not supported on your current device yet.
```

```
This block is not supported on your current device yet.
```

```
This block is not supported on your current device yet.
```

완료했습니다. 결과와 아웃룩 발송 방법을 정리해 드립니다.

---

## 생성 결과

**65명 개별 eml 파일** + **발송 목록 엑셀** 생성 완료.

각 eml은 해당 PL이 담당한 과제 목록(년도, Project Code, 과제명, 총액)을 테이블로 포함하고, 제목은 `[회신요청] PM 역할 수행 현황 확인 요청 - {이름} {직위}님` 형식입니다.

---

## 아웃룩 발송 방법 (2가지)

### ✅ 방법 1 — 더블클릭 발송 (가장 빠름)

ZIP 압축 해제 후, eml 파일을 **더블클릭** → 아웃룩에서 자동 열림 → **보내기** 클릭.

65개를 하나씩 열어야 하므로 수량이 많을 경우 방법 2를 권장합니다.

### ✅ 방법 2 — VBA 매크로 일괄 발송

아웃룩에서 `Alt+F11` → VBA 편집기 열기 → 아래 코드 붙여넣기 → `F5` 실행:

```vb
Sub SendAllEML()
    Dim folderPath As String
    Dim fileName As String
    Dim olApp As Object
    Dim olMail As Object

    folderPath = "C:\Users\YourName\Downloads\eml_output\" ' ← 압축 해제 경로로 수정
    fileName = Dir(folderPath & "*.eml")

    Set olApp = CreateObject("Outlook.Application")

    Do While fileName <> ""
        Set olMail = olApp.CreateItemFromTemplate(folderPath & fileName)
        olMail.Send
        fileName = Dir()
    Loop

    MsgBox "발송 완료!"
End Sub
```

`folderPath`만 실제 압축 해제 경로로 수정하면 65개가 자동 일괄 발송됩니다.

---

## 주의사항

- **퇴직/이동** 처리된 PL은 자동으로 제외했습니다 (이메일 없는 대상 포함).
- `발송목록.xlsx`에 발송여부 컬럼을 추가해 뒀으니 관리용으로 활용하세요.
- VBA 발송 시 아웃룩 보안 경고가 뜰 수 있는데, IT 정책에 따라 관리자 허용이 필요할 수 있습니다.

## Human (Message 3)

첫줄 바꾸자
: 안녕하십니까?  생산기술Employee eXperience&Growth팀 조대근 입니다.

마직막 두줄은 아래와 같이
관련하여 문의 사항이 있으시다면 편하게 연락 주세요. 

감사합니다.

## Claude (Message 4)

```
This block is not supported on your current device yet.
```

```
This block is not supported on your current device yet.
```

```
This block is not supported on your current device yet.
```

수정 완료했습니다. 65개 전체 재생성됐고, 변경된 부분은 두 곳입니다.

- **첫 인사**: `안녕하십니까? 생산기술Employee eXperience&Growth팀 조대근 입니다.`
- **마지막**: `관련하여 문의 사항이 있으시다면 편하게 연락 주세요.` + `감사합니다.` (서명 블록 제거)

## Human (Message 5)

열어보니 메일 2개 생성되어 있고 그나마 한글도 깨져 있음., 제대로 한거 맞아?

## Claude (Message 6)

죄송합니다. eml 파일 생성 방식에 문제가 있었네요. 실제로 열어서 확인해 보겠습니다.

```
This block is not supported on your current device yet.
```

문제 파악했습니다. `Content-Transfer-Encoding: base64`로 인코딩되어 있어서 아웃룩에서 열면 한글이 깨지고, `multipart/alternative` 구조 때문에 메일이 2개처럼 보이는 겁니다. `quoted-printable` 인코딩 + `text/html` 단일 파트로 다시 만들겠습니다.

```
This block is not supported on your current device yet.
```

```
This block is not supported on your current device yet.
```

한글 정상 확인됐습니다. 패키징합니다.

```
This block is not supported on your current device yet.
```

```
This block is not supported on your current device yet.
```

이전 버전의 문제 원인과 수정 내용입니다.

**문제 원인 2가지**

- `multipart/alternative` 구조 → 아웃룩이 파트를 2개의 메일처럼 표시
- `Content-Transfer-Encoding: base64` → 본문 전체가 base64로 인코딩되어 한글 깨짐

**이번 수정**

- 단일 `text/html` 파트로 변경 (멀티파트 제거)
- 인코딩을 `quoted-printable`로 변경 → 한글이 `=EC=A1=B0...` 형태로 안전하게 처리되고 아웃룩이 정상 디코딩

압축 풀고 더블클릭 → 아웃룩 열리면 한글 정상 표시될 겁니다. 한 개 먼저 테스트해보시고 이상 있으면 말씀해주세요.

## Human (Message 7)

아래와 같이 확인 됨. 한글 생성 다시 보고, 윈도우 환경이야
발신자 : dk.cho@lge.com 으로 반영하고 : 

수신 : 조성환 선임�==97�구원님
안녕하십니까? 생�==B0기술Employee eXperience&Growth팀 조�==8C�근 입니다.
생산기술원은 프�==9C젝트 기반 조직으�==9C 프로젝트를 체계�==81으로 관리하고, 성과를 만들어낼 수 ==EC��는 프로젝트 관리 ==EC��량이 중요합니다.<=/p>
이에 프로젝트 �==80리 역량 강화 및 육�==84�체계 수립을 진행�==95�고 있습니다.
관련하여 PEOP 등록된 ==EA��제들에 대한 실제 ==ED��로젝트 관리 현황==EC�� 조사하고 있으며,= 아래 노란셀에 잠==EC��만 시간 내시어 회==EC�� 요청드립니다.<=/p>
[선임연구원님 �==B4당 과제 목록]
년�==84Project Code 과�==9C명총�==A1(억원)2025년=KR25P00009430[LGE] HS_�==8A�타일러 플라스틱 �==9B�가경쟁력 확보 기�==88� 개발2.10
[작성 기준]

1. 수주장비 분류 : 1)단==EB��장비 2)장비군 3)라�==B8설비/증설 4)신규공�==9E�/턴키수주
2. PM 역할 수행 여부 : �==B8인이 전체 장비 개�==9C~셋업까지 수행
3. PM 역할 수행 인원 : 2�==88에서 본인이 아니�==BC 상위 리더(PM)이 있었==EB��면 이름/소속 기입=
4. 프로젝트 투입된 �==8B�점(PM역할 기준) : 1)수�==A3�*투자정보 입수 2)수==EC��*컨셉설계 3) 수주\_�==B4워드 이후
5. 프로젝트 종결시�==A0� (PM역할기준): 1)설계�==9C작 2) 셋업/CS\_셋업/양산= 3)셋업/CS_CS
   관련하여 문의 사�==AD이 있으시다면 편�==98게 연락 주세요.
   감사합니다.

## Claude (Message 8)

문제 명확합니다. `quoted-printable`이 윈도우 아웃룩에서 깨지고 있습니다. **UTF-8 BOM + 8bit 인코딩**으로 완전히 바꾸겠습니다.

```
This block is not supported on your current device yet.
```

```
This block is not supported on your current device yet.
```

```
This block is not supported on your current device yet.
```

base64 본문 자체는 완벽합니다. 문제는 **줄바꿈이 `\r\n`(CRLF)이 아닌 `\n`(LF)**으로 저장되어 아웃룩이 헤더와 본문 경계를 못 찾는 겁니다. 윈도우 표준 CRLF로 다시 생성합니다.

```
This block is not supported on your current device yet.
```

```
This block is not supported on your current device yet.
```

```
This block is not supported on your current device yet.
```

이번엔 근본 원인까지 정확히 수정했습니다.

**이전 버전들의 문제 정리:**

- v1~v2: `multipart/alternative` 구조 → 아웃룩이 파트 2개로 인식
- v3: `quoted-printable` + `\n`(LF) 줄바꿈 → 윈도우 아웃룩이 헤더/본문 경계를 못 찾아 한글 깨짐

**이번 최종 버전 수정사항:**

- 본문: `base64` 인코딩 (한글 바이트 직접 노출 없음)
- 줄바꿈: `\r\n` CRLF (RFC 2822 / 윈도우 표준)
- 구조: 단일 `text/html` 파트 (multipart 제거)
- 발신자: `dk.cho@lge.com` 반영

압축 풀고 하나 더블클릭해서 아웃룩에서 확인 부탁드립니다.

## Human (Message 9)

이 메일의 목적은 노란색 음영에 필요한 정보를 기입하도록 요청하는데 있다는 점을 다시한번 확인하고 적절한지 검증해

## Claude (Message 10)

이미지를 보니 핵심이 명확합니다. 메일 본문에 **실제로 노란 셀이 있는 엑셀 테이블**이 포함되어야 수신자가 직접 기입할 수 있는 구조인데, 지금 생성된 eml은 **읽기 전용 HTML 테이블**만 있습니다.

현재 eml의 문제를 정확히 짚어보면:

```
This block is not supported on your current device yet.
```

진단이 나왔습니다. 현재 구조의 근본적인 문제를 짚겠습니다.

---

## 현재 eml의 구조적 결함

이미지를 보면 수신자가 **답장해야 하는 컬럼이 5개** 있습니다:

| 컬럼 | 내용                                                |
| ---- | --------------------------------------------------- |
| 1)   | 수주장비 분류                                       |
| 2)   | 본인 전체 관리 여부 (PM 직접 vs 상위 리더 있었는지) |
| 3)   | PM 역할 수행인원 (성명/조직)                        |
| 4)   | 프로젝트 투입(in) 시점                              |
| 5)   | 프로젝트 종결(out) 시점                             |

**현재 eml**: 년도/Project Code/과제명/총액 4컬럼만 있는 읽기 전용 테이블 → **수신자가 기입할 칸 자체가 없음**

**올바른 구조**: 과제별로 1)~5) 컬럼이 **빈 노란 셀**로 제공되어야 회신이 가능합니다.

---

## 해결 방향 선택

HTML 이메일에서 "노란 빈 칸"을 구현하는 방법이 두 가지입니다.

```
This block is not supported on your current device yet.
```

엑셀 첨부 방식으로 가겠습니다. 이게 실무적으로 가장 확실한 구조입니다.

**동작 방식:**

- 메일 본문: 과제 목록 + 안내 텍스트 (읽기용)
- 첨부파일: 해당 PL의 과제만 필터된 엑셀, 노란 셀(1)~5) 컬럼)에 기입 후 회신

지금 바로 만들겠습니다.

```
This block is not supported on your current device yet.
```

```
This block is not supported on your current device yet.
```

```
This block is not supported on your current device yet.
```

```
This block is not supported on your current device yet.
```

완전히 재설계했습니다. 이번 버전의 구조입니다.

---

**이전 버전과의 차이**

이전엔 메일 본문에 년도/과제명/총액 4컬럼짜리 읽기 전용 테이블만 있었습니다. 수신자가 기입할 칸 자체가 없었던 구조였습니다.

**이번 버전**은 두 레이어로 분리했습니다.

메일 본문은 과제 목록을 회색 테이블로 보여주는 읽기용 안내 역할을 하고, 첨부 엑셀(`PM역할확인_이름.xlsx`)에 실제 입력 구조가 담겨 있습니다. 엑셀 1번 시트에는 해당 PL의 과제 행마다 1)수주장비분류, 2)전체관리여부(Y/N), 3)PM역할수행인원, 4)투입시점, 5)종결시점 컬럼이 노란 셀로 비어 있고, 2번 시트(`작성기준`)에는 각 항목 설명이 정리되어 있습니다.

수신자는 엑셀 열고 → 노란 셀 채우고 → 파일 첨부해 회신하면 됩니다. 하나 열어서 테스트해보시고 알려주세요.

## Human (Message 11)

Q: 회신 방식을 어떻게 하실 건가요?
A: 메일 본문에 노란 빈 칸 테이블 포함 (수신자가 답장 메일에 직접 텍스트 입력)

## Claude (Message 12)

알겠습니다. 그러면 첨부파일 없이 메일 본문 자체에 수신자가 직접 타이핑할 수 있는 노란 빈 칸 테이블을 넣는 방식으로 만들겠습니다.

한 가지 중요한 현실적 제약을 먼저 말씀드리면, 아웃룩에서 답장할 때 HTML 테이블의 셀 안에 커서를 놓고 타이핑하는 것은 가능하지만 **노란 배경색은 유지**되고 **입력한 텍스트가 셀 안에** 들어가는 구조입니다. 수신자가 답장 버튼을 누르면 원본 메일이 인용되면서 테이블이 편집 가능 상태가 됩니다.

```
This block is not supported on your current device yet.
```

```
This block is not supported on your current device yet.
```

```
This block is not supported on your current device yet.
```

완성했습니다. 이번 버전의 테이블 구조입니다.

```
[고정 - 회색]                    [입력 - 노란색]
년도 | Project Code | 과제명 | 총액  |  1)수주장비  |  2)PM여부  |  3)수행인원  |  4)투입시점  |  5)종결시점
                                      분류         (Y/N)      (N일때만)
```

헤더를 2줄로 구성해서 고정 정보(회색)와 입력 영역(노란색)이 시각적으로 명확히 구분됩니다. 작성 기준도 테이블 바로 아래 한 줄 요약으로 붙였습니다.

수신자가 답장 누르면 이 테이블이 편집 가능 상태가 되고, 노란 셀에 직접 기입 후 발송하면 됩니다. 하나 열어서 확인해 보시겠어요.

## Human (Message 13)

일단 현재 상태에서 샘플을 문서화해서 출력해봐

## Claude (Message 14)

샘플 하나 디코딩해서 HTML로 시각화해 보겠습니다.

```
This block is not supported on your current device yet.
```

HTML 내용이 완벽하게 확인됩니다. 이제 실제 메일처럼 보이는 문서로 만들겠습니다.

```
This block is not supported on your current device yet.
```

```
This block is not supported on your current device yet.
```

```
This block is not supported on your current device yet.
```

아웃룩 창 형태로 시각화했습니다. 확인 포인트 정리드립니다.

**구조 검토**

- 상단 4컬럼(년도·Project Code·과제명·총액)은 **회색 고정** — 수신자가 건드릴 필요 없음
- 우측 5컬럼은 **노란 빈 셀** — 답장 후 직접 클릭해서 기입
- 테이블 바로 아래 **작성 기준 한 줄 요약** 배치

**현재 상태에서 검토 필요한 사항**

노란 셀이 현재 `&nbsp;`(공백)만 들어있어 시각적으로는 빈 칸처럼 보이지만, 아웃룩에서 답장할 때 수신자가 셀을 정확히 클릭해서 타이핑해야 합니다. 내용 확인 후 수정 필요한 부분 말씀해 주세요.

## Human (Message 15)

ok 현재 기준으로 eml 파일을 다운로드할 수 있게 해줘:
윈도우 아웃룩 기준으로 한글표시 문제없도록 검증하고

## Claude (Message 16)

윈도우 아웃룩 한글 호환성을 철저히 검증하고 생성하겠습니다.

```
This block is not supported on your current device yet.
```

5개 검증 모두 통과. 이제 전체 65개 생성합니다.

```
This block is not supported on your current device yet.
```

잠깐, HTML에서 한글을 HTML 엔티티(`&#49688;` 방식)로 하드코딩했는데 실제 PL명·직위는 동적으로 바뀌어야 합니다. 본문에 변수가 제대로 들어갔는지 확인합니다.

```
This block is not supported on your current device yet.
```

HTML 엔티티가 일부 깨졌습니다. 수동 엔티티 방식 대신 **UTF-8 → base64 직접 인코딩**으로 깔끔하게 처리합니다.

```
This block is not supported on your current device yet.
```

한글 완벽합니다. ZIP으로 패키징합니다.

```
This block is not supported on your current device yet.
```

```
This block is not supported on your current device yet.
```

**65개 eml, 검증 5항목 전체 통과** 완료입니다.

이전 버전들과 결정적으로 달라진 점은 HTML을 UTF-8로 작성한 뒤 **파일 전체를 base64로 변환**해 eml에 담은 겁니다. 이렇게 하면 eml 파일 자체는 순수 ASCII 바이트만 존재하고, 아웃룩이 열 때 base64를 디코딩해 UTF-8 한글을 그대로 렌더링합니다. 줄바꿈도 윈도우 표준인 CRLF(`\r\n`)로 고정했습니다.

압축 풀고 하나 더블클릭해서 한글 확인 부탁드립니다.

---

_Archived from: `bec8bacd-1307-42b8-84e5-3eb0ccd22bbf.json`_
