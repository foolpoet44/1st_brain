---
title: CSP Brain System
created: 2026-04-14
updated: 2026-04-29
type: concept
status: growing
tags: [brain, system, architecture, knowledge]
aliases: [CSP Brain, Brain System]
---

# CSP Brain System

## Compiled Truth

AI 에이전트와 인간이 함께 운영하는 **공유 메모리 시스템**입니다. Git 레포지토리를 기반으로 대화 간 컨텍스트를 유지하고, 지식을 축적하며, 의사결정을 추적합니다.

**핵심 구성 요소**

1. **Compiled Truth**: 현재 상태의 가장 정확한 요약. 새 정보 오면 섹션째 덮어씀. 빠른 컨텍스트 복원용 TL;DR.
2. **Timeline**: append-only 증거 기록. 절대 수정/삭제 금지. 모든 변화의 증거가 남음.
3. **Dream Cycle**: 매주 금요일 실행하는 주간 정리 루틴. inbox 비우기 → 상태 갱신 → weekly 파일 생성.
4. **Inbox 우선 원칙**: 분류가 애매할 때 `inbox/`에 먼저 투입. 마찰 없이 기록하는 것이 목표.

**왜 중요한가**

- AI 에이전트와 대화할 때 매번 컨텍스트를 처음부터 설명하지 않아도 됨. Brain 이 연속성을 보장.
- 모든 프로젝트·결정·인물 정보가 한 곳에 축적되어, 에이전트가 더 정확한 조언을 할 수 있게 됨.

**관련 개념**

| 개념 | 관계 |
|:-----|:-----|
| RAG (Retrieval-Augmented Generation) | Brain 은 구조화된 수동 RAG 에 가까움 |
| GTD (Getting Things Done) | inbox 우선 원칙의 철학적 유사성 |

---

## Timeline

### 2026-04-29
- wiki 초기화와 함께 마이그레이션
- [[Obsidian]] + [[Git]] 하이브리드 구조로 재정비

### 2026-04-14
- 개념 등록
- csp-brain 초기화와 함께 공식 정의됨
- Compiled Truth / Timeline 이중 구조 적용 형식으로 재정비
