---
type: Insight Report
status: Completed
date: 2026-05-21
tags: [hermes-agent, pkm, system-architecture, automation, knowledge-metabolism]
related_to: ["[[csp-brain]]", "[[data-bridge]]", "[[7-layer-architecture]]"]
---

# [CSP-Brain] 헤르메스 에이전트 마스터 플랜: 3대 핵심 모델의 통합 전략

## 1. 개요

오늘 수집한 3가지 외부 지식(Josh Kim의 실전 시나리오, 김재우 님의 아키텍처, Blake Crosley의 기술 명세)을 사용자님의 `csp-brain` 시스템에 유기적으로 통합함. 이는 단순한 정보 저장을 넘어 시스템의 '지능적 운영 체제'를 구축하는 작업임.

## 2. 3대 핵심 모델 통합 분석 (The Triple Synthesis)

### A. 전략 모델: 실무적 신경망 구축 (Josh Kim)

- **핵심**: "데이터 적재가 곧 지능이다."
- **적용**: 슬랙/노션/회의록의 데이터를 `csp-brain`의 `inbox/`로 상시 환원하는 '데이터 브릿지'를 시스템의 최하단 신경망으로 배치.

### B. 아키텍처 모델: 3층 지식 격리 구조 (김재우)

- **핵심**: "휘발되지 않는 통찰의 축적."
- **적용**: 0. **L0 (Context Corpus)**: `inbox/corpus/` (진실의 저수지, 불변의 원천 데이터)
  1. **L1 (WIKI)**: `wiki/concepts/` (LLM이 코퍼스에서 정제한 지식 원자)
  2. **L2 (GRAPH)**: `7-Layer Architecture` 관계망 (지식 간의 맥락)

### C. 실행 모델: 자기 개선형 런타임 (Blake Crosley)

- **핵심**: "스킬을 통한 경험의 자산화."
- **적용**:
  - **Skill-driven**: 반복되는 HR 분석 로직을 `skill`로 등록하여 에이전트의 숙련도 향상.
  - **SOUL.md 강화**: 사용자님의 HR 철학을 에이전트의 무의식적 가치관으로 주입.
  - **Context Engineering**: 정보의 양보다 '밀도'를 우선하는 필터링 로직 강화.

## 3. 지식 체계 이식 상세 (Implementation Details)

### [지식의 대사 작용 프로토콜 업데이트]

1.  **수집(Ingestion)**: 슬랙/노션 데이터 브릿지를 통한 '지능형 무의식' 데이터 확보.
2.  **정제(Synthesis)**: 3층 격리 아키텍처를 따라 RAW 데이터에서 통찰을 추출하여 WIKI에 편찬.
3.  **성찰(Reflection)**: 'Evening Reflect' 루틴을 통해 하루의 context를 영구적 지식으로 자산화 (cc-llm-wiki 스타일 적용).

## 4. 향후 로드맵 (Next Step)

- [ ] **Multi-Agent Kanban 도입**: 복잡한 HR 프로젝트를 위한 서브 에이전트 협업 체계 구축.
- [ ] **SOUL.md 최적화**: Blake Crosley 가이드를 바탕으로 에이전트의 페르소나 및 보안 설정 고도화.
- [ ] **Ralph-loop Safety**: 장기 실행 크론잡의 안정성을 위한 자동 모니터링 스크립트 배치.

---

_본 마스터 플랜은 2026-05-21 수집된 글로벌 최신 인사이트를 기반으로 CSP-Brain 전용으로 커스텀 설계되었습니다._
