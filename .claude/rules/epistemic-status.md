# 인식 상태 표시 규칙 — 확인된 것과 해석한 것을 나눠 쓴다

> 2026-10-13 CSP 결정 (CSP_Taste_OKF v1 의 confirmed/inferred/unknown 구분을 위키 전체에 적용하는 1단계).
> wiki/ 와 projects/ 의 문서를 **새로 만들거나 Compiled Truth 를 고칠 때** 적용한다. 기존 문서를 일괄 소급하지 않는다.

## 왜 필요한가

Compiled Truth는 "현재 알고 있는 최선의 요약"이다. 그런데 지금은 그 안에서 CSP가 직접 말한 것, 원문 출처에 적힌 것, AI가 연결하고 해석한 것이 같은 목소리로 섞여 있다. 그래서 읽는 사람은 어디까지가 사실이고 어디부터가 가설인지 알 수 없다. AI의 해석이 확정처럼 적히면 시간이 지나면서 그것이 사실로 굳는다. 이 규칙은 해석을 금지하지 않는다. 해석에 이름표를 붙인다.

## 세 가지 표시

| 표시 | 뜻 | 예 |
| :-- | :-- | :-- |
| `[confirmed]` | CSP가 직접 말하거나 쓴 것, 또는 원문 출처에서 그대로 확인되는 사실 | CSP의 드라이브 문서에 적힌 정의, 외부 기사에 적힌 수치 |
| `[inferred]` | AI가 연결·해석·요약·추정한 것 | 두 개념의 유비, "~를 증명했다"는 평가, AI 대화가 제안한 어휘 |
| `[unknown]` | 근거가 부족해서 단정하지 않는 것 | 출처를 찾을 수 없는 주장, 검증하지 않은 일반화 |

표시는 Compiled Truth의 소절 제목 끝(`### 정의 [confirmed]`)에 붙이거나, 섞인 단락에서는 문장 끝에 붙인다. 소절 하나에 성격이 다른 주장이 섞이면 소절을 나눈다.

## 출처별 기본값

| 출처 | 기본 표시 |
| :-- | :-- |
| CSP가 직접 쓴 문서·메모·발언 (inbox/notes, 드라이브의 CSP 작성 문서) | confirmed |
| 외부 원문(기사·논문·보고서)에 적힌 사실과 수치 | confirmed (출처를 Timeline에 남김) |
| AI 대화 기록에서 AI가 답한 내용 | inferred |
| AI가 문서 사이를 연결하거나 이론에 빗댄 것 | inferred |
| 출처가 남아 있지 않은 과거 이관 문서의 주장 | unknown (출처를 찾으면 갱신) |
| 저장소에서 확인할 수 없는 파일·스크립트·결과에 대한 주장 | unknown |

## 승격 규칙

- `inferred` → `confirmed`로 바꾸려면 Timeline에 **`CSP 확인 YYYY-MM-DD: …`** 한 줄이 먼저 있어야 한다. AI가 혼자 승격하지 않는다.
- `unknown` → `confirmed`는 출처를 Timeline에 남기면 된다.
- `confirmed`를 반박하는 새 근거가 나오면 지우지 않고 `[disputed]`를 덧붙인 뒤 Timeline에 근거를 적는다. 판단은 CSP가 한다.

## frontmatter 추가 필드

```yaml
generated:
  by: ai-assisted-ingest | csp | legacy-migration | unknown
  at: YYYY-MM-DD
evidence: confirmed | mixed | inferred   # 문서 전체의 성격. 하나라도 섞이면 mixed
```

## 하지 않는 것

- 근거를 확인하지 않고 표시만 일괄로 붙이지 않는다. 근거 없는 표시는 표시가 없는 것보다 나쁘다.
- 단일 사례로 일반화한 문장에 confirmed를 붙이지 않는다.
- 표시 때문에 해석을 지우지 않는다. 해석은 위키의 가치다. 이름표만 정직하게 단다.
