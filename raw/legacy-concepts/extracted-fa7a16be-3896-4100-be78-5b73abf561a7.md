# Extracted Knowledge from Conv: fa7a16be-3896-4100-be78-5b73abf561a7

**Date**: 2025-12-20T02:11:52.244223Z

### Extracted Code (bash)

```bash
# Claude Code에 추가 (가장 간단)
claude mcp add context7 -- npx -y @upstash/context7-mcp

# 또는 HTTP 방식
claude mcp add --transport http context7 https://mcp.context7.com/mcp
```

### Extracted Code (bash)

```bash
# 프롬프트에 "use context7" 추가
"use context7 to help me implement FastAPI authentication"

# 또는 자동 규칙 설정
"Always use context7 when I need code generation, setup or configuration steps, or library/API documentation"
```

### Extracted Code (bash)

```bash
# Claude Code에 Context7 추가
claude mcp add context7 -- npx -y @upstash/context7-mcp

# 설치 확인
claude mcp list
```

### Extracted Code (bash)

```bash
# 프로젝트 다운로드 후
cd fastapi-auth-demo
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Extracted Code (bash)

```bash
# Without Context7 (타이머 시작!)
claude "implement user registration"

# With Context7 (타이머 시작!)
claude "use context7 to implement user registration with latest FastAPI best practices"

# 시간 차이를 time_log.md에 기록!
```
