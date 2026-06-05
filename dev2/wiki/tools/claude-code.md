---
title: Claude Code
created: 2026-04-29
updated: 2026-04-29
type: tool
status: seed
tags: [ai, tool, coding]
aliases: []
---

# Claude Code

## Compiled Truth

Anthropic 의 Claude 모델과 연동된 CLI 기반 코딩 에이전트.

**주요 기능:**

- 터미널에서 직접 코드 읽기/쓰기/실행
- Git 연동 (커밋, PR 생성)
- 프로젝트 구조 이해 및 수정
- 테스트 실행 및 디버깅

**CSP 활용 맥락:**

- csp-brain Vault 의 지식 운영 에이전트
- INGEST, LINT, DIGEST, BRIDGE 프로토콜 실행
- [[Vibe Coding]] 의 주요 도구

**핵심 명령어 Top 10:**

1. `claude` — 세션 시작
2. `claude -c` — 이전 대화 이어가기
3. `claude -p "query"` — 자동화 파이프라인
4. `/compact` — 컨텍스트 윈도우 관리
5. `/clear` — 깨끗한 상태에서 새 작업
6. `/model` — 모델 전환 (Sonnet/Haiku/Opus)
7. `Shift+Tab` — 퍼미션 모드 사이클링
8. `claude mcp add` — MCP 서버 연결
9. `/cost` — 비용 추적
10. `claude -r "session-name"` — 이름으로 세션 복원

---

## Timeline

### 2026-04-29

- wiki 초기화와 함께 등록
- Claude Code 필수 명령어 Top 10 수집 및 통합
