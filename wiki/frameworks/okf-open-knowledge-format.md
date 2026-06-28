---
title: OKF (Open Knowledge Format)
created: 2026-06-28
updated: 2026-06-28
type: framework
status: growing
tags: [okf, knowledge-management, agent-architecture, folder-as-database, google]
aliases: [OKF, Open Knowledge Format, 오픈 지식 포맷, 폴더 지식 포맷]
---

# OKF (Open Knowledge Format)

## Compiled Truth

OKF는 **지식을 폴더로 표현하는 개방형 사양**이다. 벡터 데이터베이스 대신 서로 링크된 일반 텍스트
파일 폴더에 지식을 담는다. Google이 BigQuery 팀을 통해 공식화했지만, 지적 기원은
[[Karpathy LLM Wiki]] 아이디어다. 이 Vault — csp-brain — 는 바로 그 OKF를 자기 발행 형식으로
채택했고(`scripts/okf/`, PUBLISH 프로토콜), 그래서 OKF는 우리에게 외부 트렌드가 아니라 **자기
아키텍처를 설명하는 거울**이다.

**사양의 골격은 단순하다.** 번들은 폴더이고, 각 파일은 하나의 개념이며, 파일 경로가 곧 이름이다.
파일 간 링크가 그래프를 형성하고, 디렉터리마다 내용 목록(`index.md`)과 변경 로그(`log.md`)를 둔다.
유일하게 강제되는 규칙은 단 하나 — **모든 파일은 `type` 필드로 자신의 유형을 선언해야 한다.** 나머지는
관대하다: 알 수 없는 필드, 깨진 링크, 파싱 불가 파일조차 허용한다.

**왜 폴더가 [[RAG]]/벡터DB를 이기는가** — 세 가지다. (1) *작업 시점의 효율성*: RAG는 질문 시점마다
다시 생각하지만, OKF는 번들을 **구축할 때 한 번** 지식을 연결·요약·모순 표시한다. 비용을 선불로
한 번만 낸다. (2) *처리 가능성*: 각 폴더의 짧은 목차를 먼저 읽고 필요한 파일 하나만 펼쳐, 나머지
수천 개를 건너뛴다 — 모델의 제한된 컨텍스트를 낭비하지 않는다. (3) *단순 텍스트*: Git으로 diff·리뷰가
되고, 서버·API 키 없이 파일만 열면 읽힌다. 이는 [[Compiled Truth + Timeline]] 이중 구조가 추구하는
"해석 가능한 변화"와 정확히 같은 철학이다.

**그러나 OKF에는 세 가지 결함이 있고, 이 Vault는 각각에 의도적으로 응답한다.** 이것이 이 문서의
핵심이다 — 형식을 베끼는 것이 아니라 형식의 약점을 메우는 운영을 갖는 것.

| OKF의 결함 | 이 Vault의 응답 |
| :--- | :--- |
| ① **드리프트** — "타임스탬프 필드는 있지만 필드는 프로세스가 아니다." 공유 폴더는 한 달이면 부패. | LINT 프로토콜의 "6주 미갱신" 점검을 **conformance checker의 `stale-compiled-truth` 게이트로 코드화**. 필드가 아니라 측정되는 프로세스. [[Protocols]] · [[Dream Cycle]] |
| ② **지저분한 마크다운** — LLM이 서식·헤더·링크를 망치는데 Google은 사양을 관대하게 바꿔 회피만 함. | **작성본 비파괴 + ERROR-0 게이트 + malformed YAML 자동 수리.** 잘못은 발행 파이프(`scripts/okf/publish.py`)가 흡수하고, 작성본은 손대지 않는다. |
| ③ **컨테이너만 표준화** — `type`이 자유 형식이라 "테이블 vs 관계형 자산"처럼 팀마다 다른 언어. | **정본 type 어휘(controlled vocabulary)를 SPEC §5에 못박고** `derive_type`/`normalize_type`으로 강제. 의미의 합의를 사용자에게 미루지 않는다. |

글의 결론처럼 "두 폴더가 동일해 보여도 하나는 프로덕션에서 유지되고 다른 하나는 부패한다. 파일을
읽어서는 구별할 수 없다." 그 보이지 않는 차이 — 잠금/재작성 분리와 드리프트 방지 — 가 곧 이 Vault의
운영 규칙이다. OKF 형식 자체의 성패와 무관하게, **폴더가 기억의 그릇이 된다**는 근본 전환은 이미
되돌릴 수 없다.

---

## Timeline

### 2026-06-28

- OKF 분석 글(`inbox/articles/2026-06-28-okf-folders-vs-vectordb.md`)을 INGEST하며 본 문서 생성.
- 글의 두 축을 정리: ① 폴더 > 벡터DB 논지, ② 세 가지 결함(드리프트·지저분한 마크다운·컨테이너만
  표준화).
- 핵심 발견 — 이 Vault는 이미 OKF를 **구현**했으면서도 정작 OKF를 설명하는 위키가 없었다. 그 구멍을
  메우고, 세 결함에 대한 우리의 응답을 표로 명문화.
- 후속: 글의 ① 드리프트 비판을 conformance checker의 `stale-compiled-truth` 검사로 코드화하고,
  ③ 컨테이너 비판을 type 어휘 사양화 + type-conflict 정리로 잇는다.
