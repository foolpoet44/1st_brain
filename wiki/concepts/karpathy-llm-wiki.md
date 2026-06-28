---
title: Karpathy LLM Wiki
created: 2026-06-28
updated: 2026-06-28
type: concept
status: seed
tags: [karpathy, llm-wiki, knowledge-management, agent-architecture, vibe-coding]
aliases: [LLM Wiki, LLM 위키, 카파시 위키, Karpathy Wiki]
---

# Karpathy LLM Wiki

## Compiled Truth

LLM Wiki는 Andrej Karpathy(OpenAI 공동 창립자, 前 Tesla AI 총괄)가 제안한 아이디어로,
[[OKF (Open Knowledge Format)]]와 폴더 기반 지식 관리의 **지적 기원**이다. 핵심 전환은 이렇다 —
모델이 질문 시점에 모든 것을 다시 파악하는 [[RAG]] 방식 대신, **지식을 한 번 구축해 서로 링크된 일반
텍스트 파일 폴더로 만든다.** 그 폴더는 모델이 코드베이스를 읽는 개발자처럼 읽을 수 있는, 살아있는
백과사전이 된다.

가장 자주 인용되는 Karpathy의 비유가 이 구조를 압축한다:

> **"Obsidian은 IDE, LLM은 프로그래머, 위키는 코드베이스."**

여기서 결정적 통찰은 **위키를 쓰는 주체가 사람이 아니라 AI**라는 점이다. 사람은 새 자료를 던지고
좋은 질문을 할 뿐, 요약·상호 참조·파일링 같은 유지보수는 AI가 사서(librarian)처럼 처리한다. 폴더는
사용자가 소유하는 부분이고, 모델은 그것을 유지보수하는 작업자다. 이 분담이야말로 csp-brain의 운영
규칙 그 자체다 — `inbox/`는 인간의 영역, `wiki/`는 AI의 영역(CLAUDE.md 읽기/쓰기 규칙).

이 아이디어는 [[Vibe Coding]]과 같은 뿌리에서 자란다. Vibe Coding이 "인간은 방향, AI는 구현"이라면,
LLM Wiki는 "인간은 자료·질문, AI는 정리·유지보수"다. 둘 다 인간을 **편집자/방향 제시자**로, AI를
**실행자/사서**로 두는 동일한 노동 분업이다. 또한 [[Agentic Engineering]]이 말하는 "지시에서 교육으로,
`.sh`에서 `.md`로"의 전환과도 직결된다 — 지식을 의미(`.md`) 단위로 전수한다는 점에서.

단, Google이 OKF로 표준화하면서 **Karpathy의 AI 유지보수 지침은 제외하고 폴더 구조만** 가져갔다는
점이 중요하다. 즉 "누가 어떻게 폴더를 살아있게 유지하는가"라는 프로세스는 표준에서 빠졌고, 그 빈
자리를 각자가 채워야 한다. csp-brain은 그 자리를 LINT·DIGEST·Dream Cycle 같은 프로토콜로 메운다.

---

## Timeline

### 2026-06-28

- OKF 분석 글 INGEST 과정에서 OKF의 지적 기원으로 Karpathy LLM Wiki를 별도 개념화.
- "Obsidian=IDE, LLM=프로그래머, 위키=코드베이스" 비유와 "AI가 위키를 쓴다"는 핵심 전환 정리.
- [[Vibe Coding]]·[[Agentic Engineering]]·[[RAG]]·[[OKF (Open Knowledge Format)]]와 교차 링크 —
  인간=방향/AI=실행이라는 csp-brain 공통 분업으로 연결.
