---
title: "내구적 실행 (Durable Execution)"
created: 2026-04-29
updated: 2026-04-29
status: growing
type: concept
domain: Infrastructure
tags: ["engineering", "reliability", "statebase", "deterministic-workflow"]
---

# 내구적 실행 (Durable Execution)

> "성공하는 워크플로는 장애를 피하는 것이 아니라, 장애 이후 아무 일도 없었다는 듯 다시 시작하는 힘을 가진 것입니다."

## 1. 개요

분산 시스템이나 복잡한 비즈니스 로직에서 각 단계의 실행 상태를 영구 저장소에 기록하여, 시스템 중단 시 마지막 성공 지점부터 재개할 수 있게 하는 아키텍처 패턴입니다.

## 2. 핵심 메커니즘

- **Execution Log**: 모든 입력, 출력, 결정을 [[Understand-Anything/understand-anything-plu[[Understand-Anything/understand-anything-plugin/skills/understand/frameworks/gin.md|gin]]/skills/understand/languages/sql.md|sql]]ite 등 데이터베이스에 타임스탬프와 함께 기록.
- **Replay**: 상태를 복구하기 위해 이전 로그를 다시 읽어 현재의 인메모리 상태를 재구축.
- **Idempot[[Understand-Anything/understand-anything-plugin/skills/understand/locales/en.md|en]]cy (멱등성)**: 동일한 단계를 여러 번 실행해도 결과가 같음을 보장하여 재실행 부작용 방지.

## 3. 에이전트 시대의 중요성

에이전트가 수행하는 '브라우징', '코딩', '분석'은 모두 긴 시간이 소요되며 에러 확률이 높습니다. `Durable Execution`은 에이전트에게 '끈기'와 '안정성'을 부여하는 물리적 토대입니다.

---

_Reference: Obelisk Engine & DBOS Whitepaper_
