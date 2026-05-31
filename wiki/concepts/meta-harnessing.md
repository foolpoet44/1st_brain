---
title: 메타-하네스 (Meta-Harnessing)
created: 2026-05-26
type: concept
tags: [harness, automation, ai-agent, scale]
related_to: "[[harness-engineering-insight]], [[vibe-coding]]"
---

# 메타-하네스: 도구를 만드는 도구

## 개요

메타-하네스(Meta-Harnessing)는 에이전트의 작업 환경(Harness) 자체를 인공지능이 스스로 설계하고 구축하는 단계를 의미합니다. "Do it once, automate it forever" 원칙의 최고 단계입니다.

## 핵심 철학

- **구조의 복제**: 검증된 워크플로우(예: csp-brain의 5단계 루틴)를 템플릿화하여 새로운 프로젝트에 즉시 이식합니다.
- **에이전트 군단(Multi-Agent Team)**: 하나의 모델에 의존하지 않고, 특정 하네츠 내에서 협업하는 전문 에이전트들을 `/harness` 명령으로 소환합니다.
- **실행 표면(Execution Surface)**: 에이전트가 물리적 컴퓨터(Codex)와 브라우저를 자유롭게 조작할 수 있는 권한과 도구를 세팅해주는 과정입니다.

## CSP Brain에서의 구현 (v2.0)

1. **Scaffolding**: 새로운 HR 프로젝트 폴더를 생성할 때 `AGENTS.md`, `skills/`, `wiki/` 표준 구조를 자동 생성.
2. **Context Packaging**: 세션 종료 시 현재의 작업 맥락을 압축하여 다음 에이전트 세션에 '전달(Handoff)'하는 자동화.
3. **Always-on Agent**: 맥북의 시스템 설정을 조작하여 AI가 백그라운드에서 끊임없이 지식을 가공하게 만드는 환경 구축.

## 시사점

"AI 활용이 깊어질수록 중요한 것은 더 많이 시키는 것이 아니라, 더 안정적으로 잘 작동하는 환경을 만드는 것이다."

---

_참조: https://github.com/revfactory/harness-for-agy_

## 2. 하네싱의 고도화 (v2.0 Insight)
하네스는 인공지능의 '디지털 신경망'을 보호하고 강화하는 '강화복'과 같습니다.

### ❶ Planner-Generator-Evaluator 분리
- **Planner**: 작업 분해 및 선언적 계획 수립.
- **Generator**: 실제 코드 및 콘텐츠 생성.
- **Evaluator**: 생성물에 대한 비판적 검증 (Playwright, Unit Test, LLM-as-a-judge).

### ❷ 작업 인계 장치 (Hand-off Mechanism)
- 세션 간 컨텍스트 단절을 막기 위해 `progress.md`나 Git 히스토리를 '기억의 릴레이' 도구로 활용합니다.

### ❸ Sprint Contract
- 에이전트 작업의 "완료" 정의를 명확히 하고, 해당 계약 조건이 충족될 때까지 세션을 종료하지 않는 엄격한 완결성을 지향합니다.
