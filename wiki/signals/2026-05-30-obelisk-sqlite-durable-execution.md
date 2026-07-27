---
title: "[SIGNAL] Obelisk: SQLite 기반 내구적 워크플로 엔진의 부상"
created: 2026-05-30
updated: 2026-05-30
status: growing
type: signal
source: Anthropic / Tech Blogs (Obelisk)
date: 2026-05-30
tags:
  [
    "sqlite",
    "durable-execution",
    "workflow-engine",
    "obelisk",
    "agentic-systems",
  ]
---

# [SIGNAL] Obelisk: [[Understand-Anything/understand-anything-plugin/skills/understand/languages/sql.md|sql]]ite 기반 내구적 워크플로 엔진의 부상

## 💡 핵심 요약 (TL;DR)

- **로컬 지향 아키텍처**: 외부 DB 서비스 없이 단일 바이너리와 **SQLite**만으로 워크플로의 상태와 실행 로그를 보존.
- **Durable Execution (DE)**: 장애 발생 시 중단된 지점부터 자동으로 재개(`Replay`) 가능. 네트워크 지연이나 LLM 호출 오류에 취약한 에이전트 시스템에 최적화.

## 🚀 전략적 가치 (Strategic Value)

- **인프라 미니멀리즘**: 거창한 오케스트레이터(Temporal 등) 없이도 엔터프라이즈 수준의 안정성 확보.
- **에이전틱 시스템의 척추**: 비결정론적이고 비용이 비싼 LLM 호출 과정을 '내구적 단계'로 만들어 실패 비용을 최소화함.
- **백업의 단순화**: SQLite와 Litestream(S3 복제)만으로 고가용성 워크플로 시스템 구축 가능.

## 🧠 CSP-Brain 인프라 적용 아이디어

- **Hermes Long-[[Understand-Anything/understand-anything-plugin/skills/understand/locales/ru.md|ru]]nning Task 보존**: 현재 5분 이상 걸리는 복잡한 지식 대사 과정을 `Obelisk` 패턴으로 설계하여, 중단 시에도 처음부터 다시 하지 않고 이어서 수행하도록 개선.
- **SQLite as Truth**: 이미 `[[KNOWLEDGE_PULSE.md|KNOWLEDGE_PULSE]]`에서 SQLite를 활용 중이므로, 이를 단순 통계용이 아닌 '에이전트 상태 머신'의 저장소로 확장할 근거 확보.
