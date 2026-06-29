---
title: Open Knowledge Format (OKF)
created: 2026-06-29
updated: 2026-06-29
type: concept
status: growing
tags: [okf, google, rag, llm-wiki, knowledge-management, vector-db]
aliases: [OKF, Google OKF]
---

# Open Knowledge Format (OKF)

## Compiled Truth

Google이 2026년 공식 발표한 AI 지식 관리 표준. 벡터 데이터베이스 기반 RAG를 대체하는 폴더 구조 기반 지식 번들 형식이다. 핵심 아이디어는 Andrej Karpathy(OpenAI 공동 창립자)의 "LLM Wiki" 제안에서 비롯되었다.

### RAG vs OKF: 근본적 차이

기존 RAG는 **질문 시점**에 지식을 조립한다. 문서를 청크로 나누고, 임베딩으로 변환하고, 벡터 DB에 저장한 뒤, 질문이 올 때마다 유사도 검색으로 조각을 가져온다. 매 쿼리마다 처음부터 연결을 재파악하는 구조다.

OKF는 **번들 구축 시점**에 지식을 한 번 연결한다. 이후 에이전트는 완성된 지식 그래프를 읽기만 한다. 비용을 한 번 치르고, 결과는 계속 재사용한다.

### OKF의 세 가지 실용적 장점

**첫째, 네비게이션 효율성.** 각 폴더에 목차(`_index.md`)가 있어 에이전트가 전체 파일을 스캔하지 않고 필요한 파일 하나만 선택한다. 수천 개 파일 중 관련 파일만 읽는 선택적 독해가 가능해진다.

**둘째, 구축 시점 통합.** 모순 표시, 교차 링크, 요약 작업을 번들 생성 시 한 번만 수행한다. 질문 시점에 이 비용을 반복 지불하지 않는다.

**셋째, 인프라 무의존성.** Git으로 관리 가능한 텍스트 파일이다. 데이터베이스, 서버, API 키가 필요없다. 파일을 열 수 있으면 접근할 수 있다.

### OKF 사양의 최소 규칙

- 번들 = 폴더
- 각 파일 = 하나의 개념(테이블, 메트릭, 플레이북 등)
- 파일 경로 = 파일의 이름(식별자)
- 파일 간 링크 = 그래프 형성
- 폴더 목차와 변경 로그를 위한 특수 파일명 존재
- **유일한 필수 규칙**: 모든 파일이 자신의 타입을 선언하는 필드를 가져야 한다

설계 철학은 "가능한 많은 것을 용서하라"이다. 알 수 없는 필드, 깨진 링크, 파싱 불가 파일도 허용한다.

### OKF의 한계

OKF는 형식이지 프로세스가 아니다. 타임스탬프 필드는 있지만, 필드 자체가 업데이트를 강제하지는 않는다. 한 사람이 관리할 때는 잘 작동하지만, 공유 팀 환경에서는 한 달 안에 오래된 정보가 쌓이기 시작한다.

또한 에이전트가 완벽한 마크다운 사서라는 가정에 기반하지만, 실제 LLM은 대규모 문서 관리에서 서식 오류, 잘못된 링크를 만들어낸다. Google의 해결책은 "모든 독자가 혼란을 용서하도록 사양을 변경하는 것"이었다—이는 표준이라기보다 손상 통제에 가깝다.

가장 깊은 한계는 형식이 **컨테이너를 표준화**하지 **의미를 표준화**하지 않는다는 점이다. 타입 필드가 자유 형식이기 때문에 팀마다 다른 표현을 쓸 수 있다.

### Google의 전략적 맥락

OKF는 Google AI 연구소가 아닌 BigQuery 팀에서 나왔다. 참조 도구는 Gemini에서 실행되고, 번들 저장소는 Google 자체 지식 제품으로 연결된다. 기술 표준이자 생태계 유입 전략이다.

### CSP-Brain과의 관계

CSP-Brain은 OKF의 철학을 선행하고 있었다. 폴더 구조, 에이전트 유지보수 위키, Git 기반 변경 추적은 이미 구현되어 있었다. 2026-06-29, OKF 원칙을 공식 정렬하면서 `wiki/_index.md` 번들 루트를 추가하고 폴더별 `_index.md` 목차를 체계화했다.

---

## Timeline

### 2026-06-29

- OKF 개념 INGEST: "Google OKF: 폴더가 벡터 데이터베이스보다 뛰어난 이유" 기사 분석
- CSP-Brain 구조가 OKF 철학과 일치함을 확인
- `wiki/_index.md` 번들 루트 생성으로 공식 OKF 정렬 완료
- 폴더별 `_index.md` 목차 갱신 계획 수립 및 실행

## 관련 개념

- [[csp-brain-system|CSP Brain System]] — OKF를 실제 구현한 시스템
- [[graph-rag|Graph RAG]] — OKF와 비교되는 RAG 고도화 방식
- [[knowledge-capitalization|Knowledge Capitalization]] — 지식 자산화 철학
- [[gbrain-personal-ai-os|gBrain Personal AI OS]] — 유사한 개인 AI OS 패러다임
- [[context-corpus|Context Corpus]] — OKF 번들의 CSP 버전 개념
