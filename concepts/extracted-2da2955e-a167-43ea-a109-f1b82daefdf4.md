# Extracted Knowledge from Conv: 2da2955e-a167-43ea-a109-f1b82daefdf4

**Date**: 2026-04-04T00:35:54.181540Z

### Extracted Code (bash)

```bash
# Claude Code settings.json에 추가
export ANTHROPIC_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
export ANTHROPIC_API_KEY=sk-your-dashscope-key

# 또는 claude code 실행 시
claude --model qwen3-coder-480b-a35b-instruct
```

### Extracted Code (text)

```text
방법 A. OpenRouter 직접 연결 (가장 단순, 5분 설정)
방법 B. LiteLLM 프록시 경유 (안정적, 권장)
방법 C. Claude Code Router (고급, 멀티모델 라우팅)
```

### Extracted Code (bash)

```bash
# ~/.zshrc 또는 ~/.bashrc에 추가
export ANTHROPIC_BASE_URL="https://openrouter.ai/api"
export ANTHROPIC_AUTH_TOKEN="sk-or-your-openrouter-key"
export ANTHROPIC_MODEL="qwen/qwen3-coder:free"
export ANTHROPIC_SMALL_FAST_MODEL="qwen/qwen3-coder:free"

# 적용
source ~/.zshrc
```

### Extracted Code (yaml)

```yaml
# ~/litellm/config.yaml
model_list:
  - model_name: "anthropic/*"
    litellm_params:
      model: "openrouter/qwen/qwen3-coder:free"
      max_tokens: 65536
      repetition_penalty: 1.05
      temperature: 0.7
      top_k: 20
      top_p: 0.8
```

### Extracted Code (yaml)

```yaml
# ~/litellm/docker-compose.yml
services:
  litellm:
    image: ghcr.io/berriai/litellm:main-latest
    ports:
      - "4000:4000"
    volumes:
      - ./config.yaml:/app/config.yaml
    environment:
      - OPENROUTER_API_KEY=${OPENROUTER_API_KEY}
    command: --config /app/config.yaml --port 4000
```

### Extracted Code (bash)

```bash
# ~/.zshrc에 추가
export ANTHROPIC_AUTH_TOKEN="sk-1234"   # 임의 값 OK
export ANTHROPIC_BASE_URL="http://localhost:4000"
export ANTHROPIC_MODEL="openrouter/qwen/qwen3-coder"
export ANTHROPIC_SMALL_FAST_MODEL="openrouter/qwen/qwen3-coder"
export CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1  # 텔레메트리 비활성화

source ~/.zshrc && claude
```

### Extracted Code (bash)

```bash
# ~/.zshrc
alias qlaude='ANTHROPIC_AUTH_TOKEN=sk-1234 \
  ANTHROPIC_BASE_URL=http://localhost:4000 \
  ANTHROPIC_MODEL=openrouter/qwen/qwen3-coder \
  claude'
```

### Extracted Code (bash)

```bash
# 설치
npm install -g @musistudio/claude-code-router

# config.json 설정 (~/.claude-code-router/config.json)
```

### Extracted Code (json)

```json
{
  "Providers": [
    {
      "name": "openrouter",
      "api_base_url": "https://openrouter.ai/api/v1/chat/completions",
      "api_key": "${OPENROUTER_API_KEY}",
      "models": [
        "qwen/qwen3-coder:free",
        "qwen/qwen3-coder-next"
      ],
      "transformer": { "use": ["openrouter"] }
    }
  ]
}
```

### Extracted Code (bash)

```bash
echo 'export ANTHROPIC_API_KEY="sk-or-여기에키"' >> ~/.zshrc
echo 'export ANTHROPIC_BASE_URL="https://openrouter.ai/api/v1"' >> ~/.zshrc
echo 'export ANTHROPIC_MODEL="qwen/qwen3-coder:free"' >> ~/.zshrc
source ~/.zshrc
```

### Extracted Code (bash)

```bash
# Ollama 방식 (CSP가 원하는 구조)
ollama pull qwen3-coder
ollama run qwen3-coder

# 현실적 최단거리 (환경변수 1회 설정 후)
source ~/.zshrc   # ← 이게 사실상 "pull" 역할
claude            # ← 이게 "run" 역할
```

### Extracted Code (bash)

```bash
# ~/.zshrc에 추가
alias claude-qwen='ANTHROPIC_MODEL="qwen/qwen3-coder:free" claude'
alias claude-free='ANTHROPIC_MODEL="qwen/qwen3-coder-next" claude'
alias claude-pro='unset ANTHROPIC_MODEL && unset ANTHROPIC_BASE_URL && claude'
```

### Extracted Code (bash)

```bash
claude-qwen   # Qwen3-Coder 480B 무료
claude-free   # Qwen3-Coder-Next
claude-pro    # 원래 Claude (Anthropic)
```

### Extracted Code (bash)

```bash
# 현재 세션에서 즉시 제거
unset ANTHROPIC_API_KEY

# .zshrc에서도 제거 (중복 방지)
# ANTHROPIC_API_KEY 라인을 삭제하고 아래처럼 재설정
```

### Extracted Code (bash)

```bash
# 기존 잘못된 라인 제거 후 아래로 교체
export ANTHROPIC_BASE_URL="https://openrouter.ai/api/v1"
export ANTHROPIC_AUTH_TOKEN="sk-or-여기에OpenRouter키"  # ← API_KEY 아님!
export ANTHROPIC_MODEL="qwen/qwen3-coder:free"

# ANTHROPIC_API_KEY 는 설정하지 않음
```

### Extracted Code (bash)

```bash
# 현재 충돌하는 변수 확인
echo $ANTHROPIC_API_KEY
echo $ANTHROPIC_AUTH_TOKEN
echo $ANTHROPIC_BASE_URL

# 충돌 변수 정리
unset ANTHROPIC_API_KEY
export ANTHROPIC_AUTH_TOKEN="sk-or-여기에키"
export ANTHROPIC_BASE_URL="https://openrouter.ai/api/v1"
export ANTHROPIC_MODEL="qwen/qwen3-coder:free"

# 재실행
claude
```

### Extracted Code (bash)

```bash
# ─── OpenRouter / Qwen3-Coder Free ───
export ANTHROPIC_BASE_URL="https://openrouter.ai/api/v1"
export ANTHROPIC_AUTH_TOKEN="sk-or-여기에OpenRouter키"
export ANTHROPIC_MODEL="qwen/qwen3-coder:free"
# ANTHROPIC_API_KEY 는 절대 설정하지 않음
```

### Extracted Code (bash)

```bash
source ~/.zshrc

# 변수 확인
echo $ANTHROPIC_BASE_URL    # https://openrouter.ai/api/v1
echo $ANTHROPIC_AUTH_TOKEN  # sk-or-...
echo $ANTHROPIC_MODEL       # qwen/qwen3-coder:free
echo $ANTHROPIC_API_KEY     # 아무것도 안 나와야 정상
```

### Extracted Code (bash)

```bash
# ~/.zshrc 맨 아래에 추가
alias claude-qwen='ANTHROPIC_MODEL="qwen/qwen3-coder:free" claude'
alias claude-ori='unset ANTHROPIC_BASE_URL ANTHROPIC_AUTH_TOKEN ANTHROPIC_MODEL && claude'
```

### Extracted Code (bash)

```bash
# 1. 충돌 변수 모두 제거
unset ANTHROPIC_BASE_URL
unset ANTHROPIC_AUTH_TOKEN
unset ANTHROPIC_MODEL
unset ANTHROPIC_API_KEY

# 2. 확인 (모두 빈칸이어야 함)
echo $ANTHROPIC_BASE_URL
echo $ANTHROPIC_AUTH_TOKEN

# 3. Claude 재실행
claude
```

### Extracted Code (bash)

```bash
# 이 라인들 삭제
export ANTHROPIC_BASE_URL="https://openrouter.ai/api/v1"
export ANTHROPIC_AUTH_TOKEN="sk-or-..."
export ANTHROPIC_MODEL="qwen/qwen3-coder:free"
```

### Extracted Code (bash)

```bash
# Claude Code 모드 전환
alias claude-qwen='ANTHROPIC_BASE_URL="https://openrouter.ai/api/v1" ANTHROPIC_AUTH_TOKEN="sk-or-여기에키" ANTHROPIC_MODEL="qwen/qwen3-coder:free" claude'
alias claude-ori='claude'
```

### Extracted Code (bash)

```bash
# 현재 세션 강제 정리
unset ANTHROPIC_BASE_URL
unset ANTHROPIC_AUTH_TOKEN  
unset ANTHROPIC_MODEL
unset ANTHROPIC_API_KEY

# 변수 상태 확인 (모두 빈칸이어야 함)
echo "BASE_URL: '$ANTHROPIC_BASE_URL'"
echo "AUTH_TOKEN: '$ANTHROPIC_AUTH_TOKEN'"
echo "MODEL: '$ANTHROPIC_MODEL'"
echo "API_KEY: '$ANTHROPIC_API_KEY'"
```
