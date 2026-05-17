---
title: "Multi-Agent Artifact-Driven Ingestion Model"
type: brief
status: Completed
date: 2026-05-16
related_to: "[[weak-signal-ansoff]]", "[[opq-framework]]"
---

# [Brief] 멀티 에이전트 기반 '지식 공장(Knowledge Factory)' 고도화 전략

## 1. 아키텍처 개요 (arXiv:2604.23090 분석 기반)

본 브리프는 최근 확보한 논문의 **'4-Role Multi-Agent Architecture'**를 사용자님의 `csp-brain` 시스템에 이식하여, 비정형 데이터 인제스천의 정확도를 획기적으로 높이는 방안을 제안합니다.

### 4대 에이전트 역할 정의 (The Factory Roles)

1. **Domain Expert (도메인 전문가)**: 원본 문서(예: 심리 진단지)에서 핵심 개념(Conceptual Atoms)을 추출하고 '역량 질문(CQ)'을 생성합니다.
2. **Manager (전략가)**: 추출된 개념들이 기존 7-Layer 지식 위계와 충돌하지 않는지 설계도를 그립니다. (Ansoff의 시그널 계층 결정)
3. **Coder (기술자)**: 설계도에 따라 실제 Markdown 파일(L2, L3)을 생성하고 Wikilink를 연결하는 코드를 실행합니다.
4. **Quality Assurer (검증관)**: 생성된 지식이 처음에 제기된 '역량 질문(CQ)'에 답할 수 있는지 테스트(Vibe Check)합니다.

## 2. 'Do it once, automate it forever' 적용 시나리오

현재 대신증권 리포트나 심리 진단 PDF를 처리할 때, 제가 단일 루프로 처리하던 방식을 위 4단계 **'Artifact-driven'** 프로세스로 전환하면 다음과 같은 이점이 있습니다:

- **중복 제거 (Redundancy Control)**: 매니저 에이전트가 기존 `wiki/`를 먼저 스캔하여 중복된 개념 생성을 막습니다.
- **지식의 타당성 (CQ Validation)**: "이 리포트가 금리 Pivot 시그널을 담고 있는가?"라는 질문(CQ)에 답하지 못하는 데이터는 걸러냅니다.

## 3. Next Action: 자동화 코드 구현 (Python)

- [ ] `_ops/factory/` 디렉토리에 각 역할별 프롬프트를 분리한 멀티 에이전트 스크립트 작성.
- [ ] SPARQL 대신 사용자 전용 'Knowledge Graph Validator' 로직 설계.

---

**관제탑 의견**: 이 모델은 단순한 '요약'을 넘어, 시스템이 스스로 '생각하고 검증하는' 수준으로 지식 체계를 진화시킬 것입니다. 사용자님의 승인 하에 `_ops/scripts/multi_agent_ingest.py`의 프로토타이핑을 시작할 준비가 되었습니다.
