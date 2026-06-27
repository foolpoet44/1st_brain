# Extracted Knowledge from Conv: bef4ab3a-a2bb-4bd9-9344-809477eb1e10

**Date**: 2026-02-15T22:19:12.485435Z

### Extracted Code (bash)

```bash
# 현재 디렉토리 구조 확인
ls -la /Users/dkmac/Desktop/@26/camp/my-day1

# MCP 설정 내용 확인
cat ~/.claude.json | grep -A 5 "my-plugin"
```

### Extracted Code (bash)

```bash
# 기존 제거
claude mcp remove my-plugin

# 올바른 진입점으로 재등록
claude mcp add my-plugin node index.js
# 또는
claude mcp add my-plugin python main.py
```

### Extracted Code (bash)

```bash
# 플러그인 구조 확인
cat /Users/dkmac/Desktop/@26/camp/my-day1/.claude-plugin/manifest.json
# 또는
ls -la /Users/dkmac/Desktop/@26/camp/my-day1/.claude-plugin/
```

### Extracted Code (bash)

```bash
mkdir -p ~/.claude/skills/my-day1
ln -s ~/my-day1/skills/my-day1.md ~/.claude/skills/my-day1/SKILL.md
ln -s ~/my-day1/skills/references ~/.claude/skills/my-day1/references
```

### Extracted Code (text)

```text
~/my-day1/
├── .claude-plugin/
│   └── plugin.json          ✅ 올바른 형식
├── skills/
│   ├── my-day1.md           ✅ frontmatter 포함
│   └── references/          ✅ 15개 파일
└── README.md
```

### Extracted Code (text)

```text
~/.claude/skills/my-day1/
├── SKILL.md -> ~/my-day1/skills/my-day1.md
└── references -> ~/my-day1/skills/references/
```

### Extracted Code (bash)

```bash
# 1. 먼저 기존 MCP 등록 제거 (필요없음)
claude mcp remove my-plugin

# 2. skills 폴더 생성
mkdir -p ~/.claude/skills/my-day1

# 3. 심볼릭 링크 생성
ln -s /Users/dkmac/Desktop/@26/camp/my-day1/skills/my-day1.md ~/.claude/skills/my-day1/SKILL.md
ln -s /Users/dkmac/Desktop/@26/camp/my-day1/skills/references ~/.claude/skills/my-day1/references
```
