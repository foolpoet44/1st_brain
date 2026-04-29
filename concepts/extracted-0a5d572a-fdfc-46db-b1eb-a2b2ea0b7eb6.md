# Extracted Knowledge from Conv: 0a5d572a-fdfc-46db-b1eb-a2b2ea0b7eb6

**Date**: 2026-03-28T03:36:12.252839Z

### Extracted Code (bash)

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

### Extracted Code (bash)

```bash
# 프로젝트별 세션
tmux new -s escon        # ESCON Next.js 작업
tmux new -s ex-intel     # EX Intelligence 
tmux new -s ax-strategy  # AX 전략 문서
```
