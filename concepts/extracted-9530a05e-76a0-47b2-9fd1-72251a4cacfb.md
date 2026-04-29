# Extracted Knowledge from Conv: 9530a05e-76a0-47b2-9fd1-72251a4cacfb

**Date**: 2025-12-22T05:20:45.484508Z

### Extracted Code (bash)

```bash
# HTTP 전송 방식 (권장)
claude mcp add --transport http context7 https://mcp.context7.com/mcp --header "CONTEXT7_API_KEY: YOUR_API_KEY"

# 또는 stdio 방식
claude mcp add context7 -- npx -y @upstash/context7-mcp --api-key YOUR_API_KEY
```

### Extracted Code (text)

```text
코드 생성, 설정 단계, 라이브러리/API 문서가 필요할 때 항상 context7을 사용하세요. 
명시적으로 요청하지 않아도 Context7 MCP 도구를 자동으로 사용하여 라이브러리 ID를 확인하고 문서를 가져오세요.
```

### Extracted Code (bash)

```bash
# Next.js 14 프로젝트 시작
claude "Next.js 14 앱 생성 with App Router, TypeScript, Tailwind
/nextjs/next.js, /shadcn/ui 참조"

# 인증 시스템 구현
claude "NextAuth v5로 완벽한 인증 시스템 구현
/nextauth/next-auth 최신 문서 참조"

# 결제 통합
claude "Stripe 결제 통합, webhook 처리 포함
/stripe/stripe-node 참조"
```

### Extracted Code (bash)

```bash
# 1. 스크립트 다운로드 후
chmod +x setup-context7-workflow.sh

# 2. 실행
./setup-context7-workflow.sh

# 3. 헬퍼 명령어 로드
source .claude/claude-helpers.sh

# 4. 바로 시작!
claude-feature "첫 번째 기능 구현"
```
