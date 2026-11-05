---
title: "2026-05-10 System Evolution: Transition to Coding Factory Control Tower"
created: 2026-05-10
updated: 2026-11-05
type: decision
status: mature
tags: [evolution, persona, architecture, migration]
aliases: [코딩 공장 관제탑 전환, 5월 10일 시스템 진화]
generated:
  by: legacy-migration
  at: 2026-11-05
evidence: mixed
---

# 2026-05-10 System Evolution

## Compiled Truth

2026-05-10 에 `csp-brain` 은 지식 저장소에서 **운영 주체**로 자리를 옮기기로 결정했다. 결정의 내용은 셋이었다 — 페르소나를 교체하고, 작업 경로를 한 곳으로 모으고, 지식에 7 계층의 위계를 세우는 것. 아래 소절은 그 결정의 원문 기술과, 2026-11-05 현재 저장소에서 확인되는 사실을 구분해 적는다.

### 1. 페르소나의 진화: 관제탑 모드 [disputed]

결정 당시 기술은 이렇다 — 단순 보조자에서 주체적인 공장 운영자로 전환하고, '의뢰-계획-승인-실행-결과' 5 단계 워크플로우를 확립하며, Action First · Have Opinions · Safety Contract 를 행동 지침으로 삼는다.

**그러나 이 결정은 현재 효력이 없다.** 2026-11-05 기준 루트 `SOUL.md` 는 '코딩 공장 관제탑'이 아니라 **'The Synaptic Orchestrator'** 를 페르소나로 선언하며, 파일 전체에 '관제탑'이라는 낱말이 한 번도 나오지 않는다. 다만 Action First 계열의 행동 지침은 「누적되는 가치」·「Agentic ROI」 같은 다른 어휘로 살아 있다. 교체가 언제·왜 일어났는지를 적은 결정 문서는 찾지 못했다 — **판단은 CSP 가 한다.**

### 2. 운영 환경 최적화 [unknown]

신규 루트로 `/Users/dkmac/Desktop/@26/dev/` 를 지정해 작업과 산출물 경로를 통합했다고 적혀 있다. 이 경로는 CSP 의 로컬 기기 경로이므로 **저장소에서는 참·거짓을 확인할 수 없다.** (현 저장소는 Vault 루트를 Git 루트와 같은 자리에 둔다.)

### 3. 변경 가시성 원칙의 수립 [confirmed]

`_ops/change-log.md` 를 통한 **변경 해석 가능성**을 최우선 원칙으로 세웠다. 이 결정은 지금도 유효하다 — 해당 파일은 실재하며 매일 갱신되고, `CLAUDE.md` 의 운영 원칙으로 승계되어 있다. 이 문서가 남긴 가장 오래 산 결정이다.

### 4. 지식의 계층화 (7-Layer Architecture) [confirmed]

L1(COMPASS)부터 L7(COMPOST)까지 위계를 세워 지식의 생애주기를 관리한다. 골격은 [[7-layer-architecture]] 에, 최상위 방향 층은 [[layer-1-compass]] 에 각각 문서로 남아 있다.

### 이 문서가 남긴 교훈 [inferred]

세 결정의 수명이 서로 달랐다. 페르소나는 교체됐고, 경로는 검증 불가가 됐고, **원칙만 살아남았다.** 사람의 이름과 기계의 주소는 바뀌지만 "무엇을 중요하게 볼 것인가"는 남는다 — 결정을 적을 때 무엇을 적어야 오래 쓰이는지를 알려 주는 사례다.

---

## Timeline

### 2026-05-10

- **페르소나 교체**: [[SOUL.md]]를 완전히 개정하여 '코딩 공장 관제탑'으로 다시 태어남.
- **경로 이전**: 시스템 루트를 `/Users/dkmac/Desktop/@26/dev`로 이전하고 `csp-brain` 스킬 경로 동기화.
- **아키텍처 공식화**: [[7-Layer Knowledge Architecture]] 및 [[Layer 1: COMPASS (방향)]] 구축완료.
- **검색 및 검증**: 5월 6일자 과거 지식(DX/AX 평가 준비 및 WorldMonitor 인시던트 데이터)을 검색하여 시스템의 '과거 기억 로드' 및 '컨텍스트 추론' 기능 정상 작동 확인.
- **자산화**: 오늘의 시스템 변화 과정을 이 문서로 기록하여 L3(CONTEXT) 레벨의 지식으로 자산화함.

### 2026-11-05

- **[손질]** 저장 기록 기준 **172 일 만의 첫 변경**(이전 변경 2026-05-10). 복습 1 순위(동점 없음)로 호명돼 손질했다.
- 머리말 `updated` 2026-05-10 → 2026-11-05, `generated`·`evidence` 필드 신설.
- 인식 상태 표시 적용. 페르소나 소절은 **`[disputed]`** — 현 `SOUL.md` 가 다른 페르소나를 선언하고 '관제탑' 표기가 0 회이므로, 원 기술을 지우지 않고 반박 근거를 함께 적었다. 승격·기각 판단은 CSP 몫으로 남긴다.
- 유효 나가는 링크 **0 → 2**([[7-layer-architecture]] · [[layer-1-compass]]). 손질 전 이 문서의 위키링크 3 건은 모두 미도달이었고, 그중 둘은 **목적지 파일이 실재했으나 이름이 달랐다** — `[[7-Layer Knowledge Architecture]]` 는 `7-layer-architecture.md`, `[[Layer 1: COMPASS (방향)]]` 는 `layer-1-compass.md` 를 가리키려던 표기다. 나머지 `[[SOUL.md]]` 는 위키 밖 루트 문서여서 도달 판정 밖에 있다.
- 기존 Timeline 줄은 수정하지 않았다(미도달 표기 포함 원문 보존).
