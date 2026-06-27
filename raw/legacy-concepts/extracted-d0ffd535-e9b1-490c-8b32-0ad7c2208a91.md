# Extracted Knowledge from Conv: d0ffd535-e9b1-490c-8b32-0ad7c2208a91

**Date**: 2026-04-03T23:10:07.946481Z

### Extracted Code (bash)

```bash
# tool use 지원 모델로 교체
ollama pull llama3.1:8b      # 가볍고 tool 지원
ollama pull qwen2.5:14b      # tool 지원, 한국어 강함
ollama pull mistral-nemo     # tool 지원
```

### Extracted Code (bash)

```bash
# 클라우드 버전 (Ollama 서버에서 실행, 무료 tier 있음)
ollama pull glm-4.7:cloud
ollama launch claude --model glm-4.7:cloud
```

### Extracted Code (bash)

```bash
# ~/.zshrc에 추가
export ANTHROPIC_AUTH_TOKEN="ollama"
export ANTHROPIC_API_KEY=""
export ANTHROPIC_BASE_URL="http://localhost:11434"
```

### Extracted Code (bash)

```bash
export ANTHROPIC_AUTH_TOKEN="ollama"
export ANTHROPIC_API_KEY=""
export ANTHROPIC_BASE_URL="http://localhost:11434"
claude --model qwen2.5-coder:7b
```

### Extracted Code (bash)

```bash
echo 'export ANTHROPIC_AUTH_TOKEN="ollama"' >> ~/.zshrc
echo 'export ANTHROPIC_API_KEY=""' >> ~/.zshrc
echo 'export ANTHROPIC_BASE_URL="http://localhost:11434"' >> ~/.zshrc
source ~/.zshrc
```

### Extracted Code (bash)

```bash
# 클라우드
ollama launch claude --model qwen3.5:cloud
# 로컬 fallback
ollama launch claude --model qwen3.5:9b
```

### Extracted Code (text)

```text
복잡한 agentic 코딩  →  qwen3-coder-next:cloud (클라우드 quota 사용)
단순 파일 수정/확인  →  qwen3.5:9b (로컬, quota 무소비)
quota 소진 시 fallback  →  qwen2.5-coder:7b (로컬)
```
