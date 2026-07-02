---
title: "Claude Code Skills — 재사용 가능한 에이전트 역량 패키지"
created: 2026-07-02
updated: 2026-07-02
type: tool
status: growing
tags: [claude-code, skills, agent, packaging]
---

# Claude Code Skills

## Compiled Truth

Claude Code 의 `.claude/` 스킬 시스템은 **지시·워크플로우·도구 설정을 이식 가능한 폴더로 패키징**해, 어떤 에이전트 세션이든 집어들 수 있게 한다 (Avi Chawla 의 "16 powerful Agent skills" 정리). 대표 스킬군: Superpowers(구조화 개발), 계획 수립, 코드 리뷰, 문서 변환 등. 핵심 통찰은 개별 스킬이 아니라 **반복 작업의 스킬화 패턴** 자체다 — [[2026-05-30-automated-task-packaging]] 신호가 포착한 "자율형 태스크 패키징"의 구현체.

CSP 관점의 함의: csp-brain 의 프로토콜(INGEST/LINT/DIGEST)도 본질적으로 스킬이다. [[claude-code-workflow]]의 운영 구조 위에서, 반복되는 지식 대사를 스킬로 굳히는 것이 [[knowledge-capitalization]]의 실행 경로다.

---

## Timeline

### 2026-07-02

- inbox/articles/"16 powerful Agent skills for AI Engineers" 를 INGEST 로 편입 (Issue #13)
