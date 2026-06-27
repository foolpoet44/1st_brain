# Extracted Knowledge from Conv: 927ddeeb-55dd-4b10-8fa3-3276e0966e26

**Date**: 2025-11-29T20:41:43.161447Z

### Extracted Code (bash)

```bash
git clone https://github.com/serithemage/claude-code-infrastructure-showcase.git
cd claude-code-infrastructure-showcase
```

### Extracted Code (bash)

```bash
# 프로젝트 루트로 이동
cd /your/project/path

# .claude 디렉토리 생성
mkdir -p .claude/hooks

# 필수 Hook 복사
cp /path/to/showcase/.claude/hooks/skill-activation-prompt.* .claude/hooks/
cp /path/to/showcase/.claude/hooks/post-tool-use-tracker.sh .claude/hooks/
```

### Extracted Code (json)

```json
{
  "skills": [
    {
      "name": "backend-dev-guidelines",
      "triggers": {
        "paths": ["**/src/**/*.ts", "**/controllers/**", "**/services/**"],
        "keywords": ["api", "endpoint", "route", "controller", "service"],
        "intents": ["create api", "build endpoint", "implement route"]
      }
    },
    {
      "name": "frontend-dev-guidelines",
      "triggers": {
        "paths": ["**/components/**", "**/pages/**", "**/*.tsx", "**/*.jsx"],
        "keywords": ["component", "react", "ui", "frontend"],
        "intents": ["create component", "build ui", "implement frontend"]
      }
    }
  ]
}
```

### Extracted Code (bash)

```bash
# Claude Code 설정 디렉토리로 이동 (macOS/Linux)
cd ~/.config/claude-code/

# 백업
cp settings.json settings.json.backup
```

### Extracted Code (json)

```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "path": ".claude/hooks/skill-activation-prompt.ts",
        "enabled": true
      }
    ],
    "PostToolUse": [
      {
        "path": ".claude/hooks/post-tool-use-tracker.sh",
        "enabled": true
      }
    ]
  }
}
```

### Extracted Code (bash)

```bash
mkdir -p .claude/agents

# 필요한 Agent 복사
cp /path/to/showcase/.claude/agents/code-architecture-reviewer.md .claude/agents/
cp /path/to/showcase/.claude/agents/refactor-planner.md .claude/agents/
```

### Extracted Code (bash)

```bash
mkdir -p dev/active

# Commands 복사
mkdir -p .claude/commands
cp /path/to/showcase/.claude/commands/dev-docs.md .claude/commands/
```

### Extracted Code (bash)

```bash
# 본인의 포크를 클론
git clone https://github.com/본인계정/claude-code-infrastructure-showcase.git

# 디렉토리 이동
cd claude-code-infrastructure-showcase

# 원본 저장소를 upstream으로 추가 (나중에 업데이트 받기 위해)
git remote add upstream https://github.com/serithemage/claude-code-infrastructure-showcase.git

# 확인
git remote -v
```

### Extracted Code (text)

```text
origin    https://github.com/본인계정/claude-code-infrastructure-showcase.git (fetch)
origin    https://github.com/본인계정/claude-code-infrastructure-showcase.git (push)
upstream  https://github.com/serithemage/claude-code-infrastructure-showcase.git (fetch)
upstream  https://github.com/serithemage/claude-code-infrastructure-showcase.git (push)
```

### Extracted Code (bash)

```bash
# upstream에서 최신 변경사항 가져오기
git fetch upstream

# main 브랜치로 이동
git checkout main

# upstream의 변경사항을 현재 브랜치에 병합
git merge upstream/main

# 본인 포크에 푸시
git push origin main
```

### Extracted Code (bash)

```bash
# 새 브랜치 생성
git checkout -b customize-for-my-project

# 파일 수정 (예: skill-rules.json, SKILL.md 등)
# ... 편집 ...

# 변경사항 커밋
git add .
git commit -m "프로젝트에 맞게 스킬 설정 커스터마이징"

# 본인 저장소에 푸시
git push origin customize-for-my-project
```

### Extracted Code (text)

```text
원본 저장소 (친구 집)
    📦 claude-code-infrastructure-showcase
    👤 serithemage가 만듦
         |
         | [Fork 버튼 클릭] = 복사하기
         ↓
내 저장소 (내 집)
    📦 claude-code-infrastructure-showcase
    👤 내가 소유함
    ✏️ 내 마음대로 수정 가능!
```
