# Extracted Knowledge from Conv: f2b906d8-d111-46d2-acdf-da7a7d0d01e2

**Date**: 2026-04-05T07:39:16.666169Z

### Extracted Code (text)

```text
┌─────────────────────────────────────────────────────┐
│              Orchestrator (Node.js / Python)         │
│                                                      │
│  ┌──────────┐    limit    ┌───────────────────────┐  │
│  │ Claude   │ ──detected──▶  Model Router          │  │
│  │  Code    │             │  (Fallback Manager)   │  │
│  │ (Primary)│             └───────────┬───────────┘  │
│  └──────────┘                         │              │
│                          ┌────────────▼────────────┐ │
│                          │  Free / Alt Models      │ │
│                          │  - Gemini 2.0 Flash     │ │
│                          │  - Ollama (local)       │ │
│                          │  - Groq (free tier)     │ │
│                          └─────────────────────────┘ │
└─────────────────────────────────────────────────────┘
```

### Extracted Code (bash)

```bash
# ~/.config/claude/model-fallback.sh

#!/bin/bash

PRIMARY_MODEL="claude-opus-4-5"
FALLBACK_MODEL="claude-haiku-4-5-20251001"  # 저렴한 tier
FREE_FALLBACK="gemini-2.0-flash"            # Google AI Studio 무료

run_with_fallback() {
  local prompt="$1"
  
  # Primary 시도
  result=$(claude --model $PRIMARY_MODEL -p "$prompt" 2>&1)
  exit_code=$?
  
  # Rate limit 감지 (exit code 또는 stderr 패턴)
  if echo "$result" | grep -q "rate_limit\|usage_limit\|529\|overloaded"; then
    echo "[FALLBACK] Switching to $FALLBACK_MODEL..."
    result=$(claude --model $FALLBACK_MODEL -p "$prompt" 2>&1)
    exit_code=$?
  fi
  
  # 완전 소진 시 외부 무료 모델
  if [ $exit_code -ne 0 ]; then
    echo "[FREE_FALLBACK] Switching to Gemini Flash..."
    result=$(call_gemini_flash "$prompt")
  fi
  
  echo "$result"
}
```

### Extracted Code (javascript)

```javascript
// model-router.js

import Anthropic from '@anthropic-ai/sdk';
import { GoogleGenerativeAI } from '@google/generative-ai';

const MODEL_PRIORITY = [
  { provider: 'anthropic', model: 'claude-opus-4-5', tier: 'primary' },
  { provider: 'anthropic', model: 'claude-haiku-4-5-20251001', tier: 'budget' },
  { provider: 'google', model: 'gemini-2.0-flash', tier: 'free' },
  { provider: 'groq', model: 'llama-3.3-70b', tier: 'free' },
  { provider: 'ollama', model: 'qwen2.5-coder', tier: 'local' },
];

class ModelRouter {
  constructor() {
    this.currentIndex = 0;
    this.cooldowns = new Map(); // 모델별 쿨다운 추적
  }

  async complete(prompt, systemPrompt = '') {
    for (let i = this.currentIndex; i < MODEL_PRIORITY.length; i++) {
      const modelConfig = MODEL_PRIORITY[i];
      
      if (this.isInCooldown(modelConfig.model)) continue;
      
      try {
        const result = await this.callModel(modelConfig, prompt, systemPrompt);
        this.currentIndex = i; // 성공한 모델 기억
        return result;
      } catch (err) {
        if (this.isRateLimitError(err)) {
          // 쿨다운 설정 (Anthropic: 60초, 등)
          this.setCooldown(modelConfig.model, this.getCooldownDuration(err));
          console.log(`[Router] ${modelConfig.model} rate limited, trying next...`);
          continue;
        }
        throw err; // 다른 에러는 상위로
      }
    }
    throw new Error('All models exhausted');
  }

  isRateLimitError(err) {
    return err.status === 429 || 
           err.status === 529 ||
           err.message?.includes('rate_limit') ||
           err.message?.includes('overloaded');
  }

  getCooldownDuration(err) {
    // retry-after 헤더 파싱
    const retryAfter = err.headers?.['retry-after'];
    return retryAfter ? parseInt(retryAfter) * 1000 : 60000;
  }

  async callModel(config, prompt, system) {
    switch(config.provider) {
      case 'anthropic':
        return this.callAnthropic(config.model, prompt, system);
      case 'google':
        return this.callGemini(config.model, prompt, system);
      case 'groq':
        return this.callGroq(config.model, prompt, system);
      case 'ollama':
        return this.callOllama(config.model, prompt, system);
    }
  }
}
```

### Extracted Code (bash)

```bash
# tmux 기반 세션 관리 + 자동 재시작

#!/bin/bash
# claude-watchdog.sh

SESSION="csp-agent"
LOG="/tmp/claude-usage.log"

start_claude() {
  local model="${1:-claude-opus-4-5}"
  tmux send-keys -t $SESSION \
    "claude --model $model" Enter
}

monitor_usage() {
  while true; do
    # Claude Code 로그에서 limit 신호 감지
    if tail -n 5 $LOG | grep -q "Claude AI usage limit reached"; then
      echo "[$(date)] Usage limit detected, switching model..."
      
      # 현재 세션 정리
      tmux send-keys -t $SESSION "/model claude-haiku-4-5-20251001" Enter
      sleep 2
      
      # 그래도 안되면 세션 재시작 with 대체 모델
      if tail -n 2 $LOG | grep -q "limit"; then
        tmux send-keys -t $SESSION "exit" Enter
        sleep 1
        start_claude "claude-haiku-4-5-20251001"
      fi
    fi
    sleep 30
  done
}
```

### Extracted Code (text)

```text
Primary:   Claude Sonnet/Opus  (Claude Code MAX 세션)
Budget:    Claude Haiku         (API 직접 호출, 저렴)  
Free Alt:  Gemini 2.0 Flash    (Google AI Studio 무료 키)
Local:     Ollama + Qwen2.5    (완전 오프라인 fallback)
```

### Extracted Code (bash)

```bash
# Step 1: Bifrost 실행 (npx 한 줄)
GEMINI_API_KEY=your_key npx -y @maximhq/bifrost

# Step 2: Claude Code를 Bifrost로 연결
ANTHROPIC_BASE_URL=http://localhost:8080/anthropic claude

# Step 3: 세션 내에서 실시간 모델 전환
/model gemini/gemini-2.0-flash
/model gemini/gemini-2.5-pro
/model anthropic/claude-sonnet-4-5-20250929  # Claude로 복귀
```

### Extracted Code (bash)

```bash
# 설치
pip install litellm

# config.yaml 작성
cat > litellm_config.yaml << EOF
model_list:
  - model_name: gemini-2.0-flash
    litellm_params:
      model: gemini/gemini-2.0-flash
      api_key: os.environ/GEMINI_API_KEY
  - model_name: gemini-2.5-pro
    litellm_params:
      model: gemini/gemini-2.5-pro
      api_key: os.environ/GEMINI_API_KEY
EOF

# 프록시 서버 시작
export GEMINI_API_KEY=your_key
export LITELLM_MASTER_KEY=sk-1234   # 임의 설정
litellm --config litellm_config.yaml

# Claude Code 연결
ANTHROPIC_BASE_URL=http://localhost:4000 \
ANTHROPIC_API_KEY=sk-1234 \
claude --model gemini-2.0-flash
```

### Extracted Code (bash)

```bash
# Docker 방식
cat > .env << EOF
GEMINI_API_KEY=your_gemini_key
OPENAI_API_KEY=fallback_key   # fallback용
PREFERRED_PROVIDER=google
BIG_MODEL=gemini-2.5-pro
SMALL_MODEL=gemini-2.0-flash
EOF

docker run -p 8082:8082 --env-file .env \
  ghcr.io/1rgs/claude-code-proxy:latest

# Claude Code 연결
ANTHROPIC_BASE_URL=http://localhost:8082 claude
```

### Extracted Code (bash)

```bash
# ~/.zshrc에 추가해두면 항상 적용
export GEMINI_API_KEY="your_google_ai_studio_key"

# alias 등록
alias claude-gemini='ANTHROPIC_BASE_URL=http://localhost:8080/anthropic claude'
alias bifrost='GEMINI_API_KEY=$GEMINI_API_KEY npx -y @maximhq/bifrost &'
```

### Extracted Code (bash)

```bash
# ─── Gemini / Claude Code Proxy ───────────────────────────
export GEMINI_API_KEY="your_google_ai_studio_key_here"
export ANTHROPIC_API_KEY="your_anthropic_key_here"

# Bifrost 백그라운드 실행 함수
bifrost-start() {
  if pgrep -f "maximhq/bifrost" > /dev/null; then
    echo "✅ Bifrost already running"
  else
    GEMINI_API_KEY=$GEMINI_API_KEY npx -y @maximhq/bifrost &
    echo "🚀 Bifrost started (port 8080)"
    sleep 2
  fi
}

# Claude → Gemini 모드
alias claude-gemini='bifrost-start && ANTHROPIC_BASE_URL=http://localhost:8080/anthropic claude'

# 일반 Claude (Anthropic 직접)
alias claude-direct='ANTHROPIC_BASE_URL="" claude'

# Bifrost 종료
alias bifrost-stop='pkill -f "maximhq/bifrost" && echo "🛑 Bifrost stopped"'
# ───────────────────────────────────────────────────────────
```

### Extracted Code (bash)

```bash
# Gemini로 Claude Code 실행
claude-gemini

# 세션 안에서 모델 전환
/model gemini/gemini-2.0-flash
/model gemini/gemini-2.5-pro
/model anthropic/claude-sonnet-4-5-20250929

# 원래 Claude로
claude-direct
```

### Extracted Code (bash)

```bash
# ~/.zshrc
# 계정 로그인 상태면 실제 API Key 불필요
# Bifrost 연결 시 더미값으로 에러 우회
alias claude-gemini='bifrost-start && \
  ANTHROPIC_BASE_URL=http://localhost:8080/anthropic \
  ANTHROPIC_API_KEY=dummy \
  claude'
```

### Extracted Code (bash)

```bash
# ─── Claude Code + Gemini Fallback ────────────────────────

export GEMINI_API_KEY="여기에_구글_AI_스튜디오_키_붙여넣기"

# Bifrost 시작 함수
bifrost-start() {
  if pgrep -f "maximhq/bifrost" > /dev/null; then
    echo "✅ Bifrost already running"
  else
    GEMINI_API_KEY=$GEMINI_API_KEY npx -y @maximhq/bifrost > /tmp/bifrost.log 2>&1 &
    echo "🚀 Bifrost starting..."
    sleep 3
  fi
}

# Gemini 모드 (계정 토큰 사용 + Gemini 라우팅)
alias claude-gemini='bifrost-start && ANTHROPIC_BASE_URL=http://localhost:8080/anthropic ANTHROPIC_API_KEY=dummy claude'

# 일반 모드 (계정 토큰 직접 사용)
alias claude-normal='ANTHROPIC_BASE_URL="" claude'

# Bifrost 종료
alias bifrost-stop='pkill -f "maximhq/bifrost" && echo "🛑 Bifrost stopped"'

# 상태 확인
alias bifrost-status='pgrep -f "maximhq/bifrost" > /dev/null && echo "✅ Running" || echo "❌ Stopped"'

# ──────────────────────────────────────────────────────────
```

### Extracted Code (bash)

```bash
# 일반 Claude (계정 토큰)
claude-normal

# Gemini 모드
claude-gemini
# → 세션 내에서 /model gemini/gemini-2.0-flash 입력

# Bifrost 상태 확인
bifrost-status
```

### Extracted Code (bash)

```bash
# ─── Claude Code + Gemini Fallback ────────────────────────

export GEMINI_API_KEY="AIza로_시작하는_키_여기에_붙여넣기"

# Bifrost 시작 함수
bifrost-start() {
  if pgrep -f "maximhq/bifrost" > /dev/null; then
    echo "✅ Bifrost already running"
  else
    GEMINI_API_KEY=$GEMINI_API_KEY npx -y @maximhq/bifrost > /tmp/bifrost.log 2>&1 &
    echo "🚀 Bifrost starting..."
    sleep 3
  fi
}

# Gemini 모드
alias claude-gemini='bifrost-start && ANTHROPIC_BASE_URL=http://localhost:8080/anthropic ANTHROPIC_API_KEY=dummy claude'

# 일반 모드 (Claude Pro 계정 토큰)
alias claude-normal='ANTHROPIC_BASE_URL="" claude'

# 유틸
alias bifrost-stop='pkill -f "maximhq/bifrost" && echo "🛑 Bifrost stopped"'
alias bifrost-status='pgrep -f "maximhq/bifrost" > /dev/null && echo "✅ Running" || echo "❌ Stopped"'
alias bifrost-log='tail -f /tmp/bifrost.log'

# ──────────────────────────────────────────────────────────
```

### Extracted Code (bash)

```bash
# config 디렉토리 생성
mkdir -p ~/.bifrost

# config 파일 작성
cat > ~/.bifrost/config.toml << EOF
[providers]
  [providers.gemini]
    api_key = "$GEMINI_API_KEY"
EOF
```

### Extracted Code (bash)

```bash
# 기존 종료
bifrost-stop

# 새 터미널에서 config 지정하여 재시작
GEMINI_API_KEY=$GEMINI_API_KEY npx -y @maximhq/bifrost --config ~/.bifrost/config.toml > /tmp/bifrost.log 2>&1 &
sleep 3

# Claude Gemini 모드 실행
claude-gemini
```

### Extracted Code (bash)

```bash
bifrost-start() {
  if pgrep -f "maximhq/bifrost" > /dev/null; then
    echo "✅ Bifrost already running"
  else
    GEMINI_API_KEY=$GEMINI_API_KEY npx -y @maximhq/bifrost \
      --config ~/.bifrost/config.toml \
      > /tmp/bifrost.log 2>&1 &
    echo "🚀 Bifrost starting..."
    sleep 3
  fi
}
```

### Extracted Code (bash)

```bash
alias claude-gemini='bifrost-start && ANTHROPIC_BASE_URL=http://localhost:8080/anthropic ANTHROPIC_API_KEY=dummy claude'
```

### Extracted Code (bash)

```bash
# 터미널 1: Bifrost 직접 실행
GEMINI_API_KEY="AIza로시작하는실제키" npx -y @maximhq/bifrost

# 터미널 2: Claude 연결
ANTHROPIC_BASE_URL=http://localhost:8080/anthropic claude
```

### Extracted Code (bash)

```bash
# Bifrost 전체 종료
pkill -f bifrost
pkill -f maximhq

# 혹시 zshrc에 ANTHROPIC_API_KEY 설정되어 있으면 확인
grep -n "ANTHROPIC_API_KEY" ~/.zshrc
```

### Extracted Code (bash)

```bash
# 디렉토리 생성
mkdir -p ~/.config/bifrost

# config.json 작성 (실제 키 그대로 사용)
cat > ~/.config/bifrost/config.json << 'EOF'
{
  "providers": {
    "gemini": {
      "api_key": "AIzaSyCTlQhikRrYqgJG_YjgFY3QDlvNld0xb34"
    }
  }
}
EOF
```

### Extracted Code (bash)

```bash
cat > ~/.config/bifrost/config.json << 'EOF'
{
  "providers": [
    {
      "provider_key": "gemini",
      "api_key": "AIzaSyCTlQhikRrYqgJG_YjgFY3QDlvNld0xb34"
    }
  ]
}
EOF
```

### Extracted Code (bash)

```bash
cat > ~/.config/bifrost/config.json << 'EOF'
{
  "$schema": "https://www.getbifrost.ai/schema",
  "providers": {
    "gemini": {
      "api_key": "AIzaSyCTlQhikRrYqgJG_YjgFY3QDlvNld0xb34"
    }
  }
}
EOF
```

### Extracted Code (bash)

```bash
cat > ~/.config/bifrost/config.json << 'EOF'
{
  "$schema": "https://www.getbifrost.ai/schema",
  "providers": {
    "gemini": {
      "keys": [
        {
          "value": "AIzaSyCTlQhikRrYqgJG_YjgFY3QDlvNld0xb34"
        }
      ]
    }
  }
}
EOF
```

### Extracted Code (bash)

```bash
curl -X POST http://localhost:8080/api/providers \
  -H "Content-Type: application/json" \
  -d '{
    "provider": "gemini",
    "keys": ["AIzaSyCTlQhikRrYqgJG_YjgFY3QDlvNld0xb34"]
  }'
```

### Extracted Code (bash)

```bash
# 설치
pip install litellm

# 실행 (한 줄)
GEMINI_API_KEY="AIzaSyCTlQhikRrYqgJG_YjgFY3QDlvNld0xb34" \
litellm --model gemini/gemini-2.0-flash --port 8080
```

### Extracted Code (bash)

```bash
curl -X POST http://localhost:8080/api/providers \
  -H "Content-Type: application/json" \
  -d '{
    "provider": "gemini",
    "keys": [{"value": "AIzaSyCTlQhikRrYqgJG_YjgFY3QDlvNld0xb34"}]
  }'
```

### Extracted Code (bash)

```bash
curl -X POST http://localhost:8080/api/providers/gemini/keys \
  -H "Content-Type: application/json" \
  -d '{"value": "AIzaSyCTlQhikRrYqgJG_YjgFY3QDlvNld0xb34"}'
```

### Extracted Code (bash)

```bash
# Bifrost 종료
pkill -f bifrost
lsof -ti:8080 | xargs kill -9

# DB 초기화 (기존 잘못된 설정 제거)
rm -rf ~/.config/bifrost/
rm -rf ~/Library/Caches/bifrost/

# config 새로 작성
mkdir -p ~/.config/bifrost
cat > ~/.config/bifrost/config.json << 'EOF'
{
  "$schema": "https://www.getbifrost.ai/schema",
  "providers": {
    "gemini": {
      "keys": [
        {
          "value": "AIzaSyCTlQhikRrYqgJG_YjgFY3QDlvNld0xb34"
        }
      ]
    }
  }
}
EOF

# 재시작
npx -y @maximhq/bifrost
```

### Extracted Code (bash)

```bash
pip install 'litellm[proxy]'

GEMINI_API_KEY="AIzaSyCTlQhikRrYqgJG_YjgFY3QDlvNld0xb34" \
litellm --model gemini/gemini-2.0-flash --port 4000
```

### Extracted Code (bash)

```bash
# Bifrost 종료
pkill -f bifrost
lsof -ti:8080 | xargs kill -9

# LiteLLM 설치
pip install 'litellm[proxy]'

# 실행
GEMINI_API_KEY="AIzaSyCTlQhikRrYqgJG_YjgFY3QDlvNld0xb34" \
litellm --model gemini/gemini-2.0-flash --port 4000
```

### Extracted Code (bash)

```bash
# ─── Claude Code + Gemini (LiteLLM) ──────────────────────
export GEMINI_API_KEY="AIzaSyCTlQhikRrYqgJG_YjgFY3QDlvNld0xb34"

litellm-start() {
  if pgrep -f "litellm" > /dev/null; then
    echo "✅ LiteLLM already running"
  else
    GEMINI_API_KEY=$GEMINI_API_KEY litellm \
      --model gemini/gemini-2.0-flash \
      --port 4000 > /tmp/litellm.log 2>&1 &
    echo "🚀 LiteLLM starting..."
    sleep 4
  fi
}

alias claude-gemini='litellm-start && ANTHROPIC_BASE_URL=http://localhost:4000 claude'
alias claude-normal='ANTHROPIC_BASE_URL="" claude'
alias litellm-stop='pkill -f litellm && echo "🛑 LiteLLM stopped"'
alias litellm-log='tail -f /tmp/litellm.log'
# ──────────────────────────────────────────────────────────
```
