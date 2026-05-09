# Extracted Knowledge from Conv: 62efbf26-3afc-4d47-a919-64bf93b43bc4

**Date**: 2026-02-10T02:41:00.640772Z

### Extracted Code (bash)

```bash
npm uninstall -g @anthropic-ai/claude-code
rm ~/.claude.json
rm -rf ~/.claude/
npm cache clean --force
npm install -g @anthropic-ai/claude-code
```

### Extracted Code (bash)

```bash
# 현재 버전 확인
claude --version

# 업데이트 (npm 설치인 경우)
npm update -g @anthropic-ai/claude-code

# 또는 공식 권장 방식
claude update
```

### Extracted Code (bash)

```bash
# zsh인 경우
nano ~/.zshrc   # ANTHROPIC_MODEL 관련 줄 삭제
source ~/.zshrc

# bash인 경우
nano ~/.bashrc
source ~/.bashrc
```

### Extracted Code (bash)

```bash
# 기본 Sonnet 4.5 (가장 안정적)
claude --model claude-sonnet-4-5-20250929

# Opus 4.6 (Max 플랜 또는 extra usage 필요)
claude --model claude-opus-4-6

# Sonnet 4
claude --model claude-sonnet-4-20250514
```

### Extracted Code (bash)

```bash
npm uninstall -g @anthropic-ai/claude-code
rm -f ~/.claude.json
rm -rf ~/.claude/
npm cache clean --force
npm install -g @anthropic-ai/claude-code
claude
```
