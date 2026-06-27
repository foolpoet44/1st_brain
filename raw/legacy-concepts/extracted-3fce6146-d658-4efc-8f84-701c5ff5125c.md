# Extracted Knowledge from Conv: 3fce6146-d658-4efc-8f84-701c5ff5125c

**Date**: 2026-04-04T03:57:26.080119Z

### Extracted Code (bash)

```bash
# 설치 여부 확인
ollama --version

# 미설치라면
# Mac: brew install ollama
# Linux: curl -fsSL https://ollama.com/install.sh | sh
```

### Extracted Code (bash)

```bash
# 원하는 모델 다운로드 (예시)
ollama pull llama3.2
ollama pull qwen2.5:7b      # 경량 + 한국어 준수
ollama pull gemma3:12b       # 성능 밸런스
```

### Extracted Code (bash)

```bash
curl http://localhost:11434/api/generate \
  -d '{"model": "qwen2.5:7b", "prompt": "안녕하세요", "stream": false}'
```

### Extracted Code (bash)

```bash
# 현재 11434 포트 사용 중인 프로세스 확인
lsof -i :11434

# 실행 중인 GUI 앱 목록
ls /Applications | grep -i -E "ollama|clo|lm|open"

# 혹은 Spotlight로 찾기
# Cmd + Space → "open" 또는 "clo" 검색
```

### Extracted Code (bash)

```bash
# 지금 바로 로컬 모델로 실행
ollama run qwen3.5:9b
ollama run qwen3-coder:latest    # 코딩 작업용
ollama run qwen2.5-coder:7b      # 경량 코딩용
```

### Extracted Code (bash)

```bash
# Open WebUI 실행 중인지 확인
docker ps | grep open-webui

# 또는 브라우저에서 접근 가능한지 확인
open http://localhost:3000
```

### Extracted Code (bash)

```bash
# 1. 기존 gateway 종료
openclaw gateway stop

# 2. 잠깐 대기
sleep 2

# 3. 새 모델로 재실행
ollama launch openclaw --model qwen3.5:9b
```

### Extracted Code (bash)

```bash
# 강제 종료
kill -9 42165

# 확인
sleep 1 && lsof -i :18789

# 재실행
ollama launch openclaw --model qwen3.5:9b
```
