---
title: RAG & 벡터 데이터베이스
created: 2026-06-28
updated: 2026-06-28
type: concept
status: seed
tags: [rag, vector-database, embedding, retrieval, ai-memory]
aliases: [RAG, Retrieval-Augmented Generation, 벡터 데이터베이스, 벡터DB, 임베딩 검색]
---

# RAG & 벡터 데이터베이스

## Compiled Truth

RAG(Retrieval-Augmented Generation)는 지난 2년간 **AI에 기억을 부여하는 표준 방식**이었다. 절차는
정형화돼 있다 — 문서를 수천 개의 조각(chunk)으로 나누고, 각 조각을 의미를 담은 숫자의 긴 목록
(임베딩)으로 변환해 벡터 데이터베이스에 저장한다. 질문이 들어오면 시스템은 질문과 가장 유사한
조각들을 끌어와 모델에게 건넨다.

이 방식이 복잡해진 이유는 **정보가 흩어져 있었기 때문**이다. 메트릭 정의는 데이터베이스에, 로직은
파이프라인에, 변경 이력은 오래된 풀 리퀘스트에, 나머지는 퇴사한 엔지니어의 머릿속에 있었다. RAG는
이 파편을 질문 시점에 다시 그러모으는 장치였다.

**그러나 RAG의 근본 한계는 '기억하지 못한다'는 점이다.** 모든 쿼리가 처음부터 시작된다. 모델은
매번 새로운 조각 더미를 받아 이전과 똑같은 연결을 다시 파악해야 한다. 같은 추론을 반복해서 사들이는
셈이다. 이 지점이 [[OKF (Open Knowledge Format)]]가 뒤집은 핵심이다 — OKF는 질문 시점이 아니라
**구축 시점에 한 번만** 연결·요약을 끝내 두고, 이후엔 완성된 답을 읽는다. 비싼 인프라(벡터DB·임베딩
서버·API)를 걷어내고 그저 **폴더와 텍스트 파일**로 더 나은 성능을 낸 것이, [[Karpathy LLM Wiki]]에서
시작해 OKF로 표준화된 전환의 요체다.

CSP 관점에서 이 대비는 [[Compiled Truth + Timeline]] 철학과 맞닿는다. RAG가 "매번 다시 검색"이라면,
Compiled Truth는 "한 번 정리해 덮어쓰고, 다음엔 그 요약을 읽는다." 둘 다 같은 질문에 답한다 —
지식을 어디서, 언제 한 번 비용 지불할 것인가.

---

## Timeline

### 2026-06-28

- OKF 분석 글 INGEST 과정에서 RAG/벡터DB의 한계를 별도 개념으로 분리 생성.
- 핵심 대비 정리: RAG = 질문 시점 재검색(매번 처음부터), OKF/폴더 = 구축 시점 일회 비용 + 이후 읽기.
- [[OKF (Open Knowledge Format)]]·[[Karpathy LLM Wiki]]와 교차 링크.
