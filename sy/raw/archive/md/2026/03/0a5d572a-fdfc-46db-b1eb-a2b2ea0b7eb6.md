---
title: tmux와 cmux의 차이점
date: 2026-03-28
time: 03:36
uuid: 0a5d572a-fdfc-46db-b1eb-a2b2ea0b7eb6
type: conversation
tags: [archive, conversation]
---

# tmux와 cmux의 차이점

**날짜**: 2026-03-28 03:36

---

## Human (Message 1)

tmux, cmux ??

## Claude (Message 2)

tmux와 cmux, 둘 다 터미널 멀티플렉서 계열인데 성격이 다릅니다.

**tmux**는 terminal multiplexer의 고전입니다. 하나의 터미널 세션 안에서 여러 창(window)과 패널(pane)을 분할해서 쓸 수 있고, 세션을 detach했다가 나중에 다시 attach할 수 있어서 — SSH 끊겨도 작업이 살아있는 그 기능 — 서버 작업이나 Claude Code 같은 장시간 에이전트 실행에 특히 유용합니다. CSP가 hr-workspace 아키텍처 운영할 때 쓰면 딱 맞는 도구죠.

**cmux**는 두 가지로 불립니다. 하나는 Ruby 생태계의 `tmuxinator` 류처럼 tmux 세션을 YAML로 미리 정의해두고 한 번에 띄우는 **tmux session manager** 개념의 도구고, 다른 하나는 gRPC 레이어에서 HTTP/2 연결을 멀티플렉싱하는 **cmux (Go 라이브러리)** 입니다. 어떤 맥락에서 보셨나요?

사용 맥락을 알면 더 정확히 연결해 드릴 수 있습니다 — Claude Code 워크플로우용인지, 서버 인프라용인지, 아니면 다른 문서에서 보신 건지요.

## Human (Message 3)

Cc 워크플로우

## Claude (Message 4)

Claude Code 워크플로우 맥락이라면 **tmux가 핵심**입니다.

---

## tmux가 CC 워크플로우에서 중요한 이유

Claude Code는 기본적으로 장시간 실행되는 에이전트 프로세스입니다. 터미널을 닫거나 SSH가 끊기면 작업이 날아가는데, tmux는 그 프로세스를 백그라운드 세션으로 보존합니다.

핵심 패턴은 이렇습니다.

```bash
# 세션 생성
tmux new -s hr-workspace

# 안에서 Claude Code 실행
claude

# 세션 detach (작업은 계속 돌아감)
Ctrl+b, d

# 나중에 다시 붙기
tmux attach -t hr-workspace
```

---

## CSP 워크플로우에 맞는 구성

hr-workspace 4-layer 구조에 맞춰 세션을 분리하면 됩니다.

```bash
# 프로젝트별 세션
tmux new -s escon        # ESCON Next.js 작업
tmux new -s ex-intel     # EX Intelligence
tmux new -s ax-strategy  # AX 전략 문서
```

하나의 세션 안에서 창을 분할할 수도 있습니다.

```
[window 1] claude (에이전트 실행)
[window 2] git / 파일 탐색
[window 3] 로그 모니터링
```

---

## cmux와의 관계

**tmuxinator** (흔히 cmux처럼 불리는 것)를 쓰면 이 세션 구성을 YAML로 저장해두고 `tmuxinator start hr-workspace` 한 줄로 전체 환경을 복원할 수 있습니다. CLAUDE.md처럼 워크스페이스 컨텍스트를 코드로 관리하는 개념과 동일선상입니다.

모바일 → 데스크탑 Dispatch 패턴으로 원격 제어할 때도 tmux 세션이 브릿지 역할을 합니다.

어떤 부분을 더 깊이 볼까요?

---

_Archived from: `0a5d572a-fdfc-46db-b1eb-a2b2ea0b7eb6.json`_
