# Extracted Knowledge from Conv: cfa60510-9eef-4846-adfa-6d084dff88b0

**Date**: 2026-03-21T23:58:50.147196Z

### Extracted Code (bash)

```bash
# SSH 키 생성
ssh-keygen -t ed25519 -C "your_email@example.com"

# 공개키 확인 (이걸 GitHub에 등록)
cat ~/.ssh/id_ed25519.pub

# SSH agent에 키 추가
ssh-add ~/.ssh/id_ed25519

# GitHub 연결 테스트
ssh -T git@github.com
```

### Extracted Code (bash)

```bash
# marketplace 설정 파일 위치 확인
cat ~/.claude/plugins/marketplaces/claude-plugins-official.json
# 또는
ls ~/.claude/
```

### Extracted Code (bash)

```bash
# 플러그인 파일 구조 확인
ls ~/.claude/plugins/installed/telegram*/

# skill 정의 파일이 있는지 확인
find ~/.claude/plugins -name "*.skill*" -o -name "skills*" 2>/dev/null
```

### Extracted Code (bash)

```bash
# 1. Claude 설정 디렉토리 전체 구조 확인
ls -la ~/.claude/

# 2. marketplace 관련 파일/폴더 확인
ls -la ~/.claude/plugins/marketplaces/
```

### Extracted Code (bash)

```bash
# marketplace 설정 파일 내용 확인
cat ~/.claude/plugins/marketplaces/claude-plugins-official.json
# 또는 .yaml / .toml 형식일 수도 있음
ls ~/.claude/plugins/marketplaces/
```

### Extracted Code (bash)

```bash
# jq로 깔끔하게 수정 (jq 없으면 아래 sed 방법 사용)
cat ~/.claude/plugins/marketplaces/claude-plugins-official.json \
  | jq '.url = "https://github.com/anthropics/claude-plugins.git"' \
  > /tmp/marketplace_tmp.json \
  && mv /tmp/marketplace_tmp.json \
     ~/.claude/plugins/marketplaces/claude-plugins-official.json

# jq 없을 경우 sed로 대체
sed -i '' 's|git@github.com:|https://github.com/|g' \
  ~/.claude/plugins/marketplaces/claude-plugins-official.json

# 수정 결과 확인
cat ~/.claude/plugins/marketplaces/claude-plugins-official.json
```

### Extracted Code (bash)

```bash
# 기존 marketplace 제거
/plugin marketplace remove claude-plugins-official

# HTTPS URL로 재등록
/plugin marketplace add claude-plugins-official \
  https://github.com/anthropics/claude-plugins.git
```

### Extracted Code (bash)

```bash
# marketplace 업데이트 재시도
/plugin marketplace update claude-plugins-official

# 성공하면 telegram 재설치
/plugin install telegram@claude-plugins-official
```

### Extracted Code (bash)

```bash
# 방법 1: URL만 입력
/plugin marketplace add https://github.com/anthropics/claude-plugins.git

# 방법 2: name을 별도 플래그로
/plugin marketplace add --name claude-plugins-official https://github.com/anthropics/claude-plugins.git

# 방법 3: 순서 바꾸기
/plugin marketplace add https://github.com/anthropics/claude-plugins.git claude-plugins-official
```

### Extracted Code (bash)

```bash
# curl로 레포 존재 여부 확인
curl -s -o /dev/null -w "%{http_code}" \
  https://api.github.com/repos/anthropics/claude-plugins
```

### Extracted Code (bash)

```bash
# 실제 설치된 telegram 플러그인 내부 확인
find ~/.claude/plugins -name "*telegram*" -type f
cat ~/.claude/plugins/installed/telegram*/plugin.json
# 또는
ls -la ~/.claude/plugins/installed/telegram*/
```

### Extracted Code (json)

```json
{
  "mcpServers": {
    "telegram": {
      "env": {
        "TELEGRAM_BOT_TOKEN": "여기에_새로발급받은_토큰"
      }
    }
  }
}
```

### Extracted Code (bash)

```bash
# 플러그인 문서 직접 읽기
cat ~/.claude/plugins/installed/telegram*/README.md
cat ~/.claude/plugins/installed/telegram*/CLAUDE.md
```

### Extracted Code (bash)

```bash
# plugin.json 또는 config 파일 내용 보기
cat $(find ~/.claude/plugins -name "plugin.json" | xargs grep -l telegram 2>/dev/null)

# 또는 telegram 폴더 전체 구조
ls -la ~/.claude/plugins/installed/telegram*/
```

### Extracted Code (json)

```json
{
  "mcpServers": {
    "telegram": {
      "env": {
        "TELEGRAM_BOT_TOKEN": "새로_발급받은_토큰"
      }
    }
  }
}
```

### Extracted Code (bash)

```bash
find ~/.claude/plugins/installed -path "*telegram*" \
  \( -name "*.json" -o -name "*.md" -o -name "*.yaml" \) \
  | xargs ls -la
```
