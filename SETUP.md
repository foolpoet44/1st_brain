# CSP-Brain Setup Guide

> MacBook Air M5에서 처음부터 세팅하는 가이드

---

## Step 1: 옵시디언 설치 & Vault 열기

```bash
# 1. Obsidian 설치 (이미 설치되어 있다면 스킵)
# https://obsidian.md 에서 다운로드

# 2. csp-brain 폴더를 다운로드한 위치 확인
# (claude.ai에서 다운로드한 zip을 풀어서)
# 추천 위치: ~/csp-brain

# 3. Obsidian 실행 → "Open folder as vault" → ~/csp-brain 선택
```

## Step 2: 커뮤니티 플러그인 설치

옵시디언 설정 → Community Plugins → Turn on → Browse

**필수 플러그인 6개** (순서대로 설치):

| 플러그인 | 역할 | 설정 포인트 |
|:---|:---|:---|
| **Dataview** | wiki/ 문서 쿼리, 대시보드 | 설치만 하면 됨 |
| **Templater** | 문서 생성 자동화 | Template folder: `_templates` |
| **Obsidian Git** | 자동 Git 커밋/푸시 | Auto pull: 5min, Auto push: 매뉴얼 |
| **Shell Commands** | Claude Code 터미널 연동 | 아래 Step 4 참고 |
| **Kanban** | 프로젝트 보드 뷰 (선택) | — |
| **Calendar** | 일별/주별 타임라인 (선택) | — |

### Templater 설정

```
Settings → Templater
  → Template folder location: _templates
  → Trigger on new file creation: ON
```

### Obsidian Git 설정

```
Settings → Obsidian Git
  → Auto pull interval: 5 (minutes)
  → Auto push: OFF (수동 push — Dream Cycle 때만)
  → Auto commit: OFF (Claude Code가 직접 커밋)
```

## Step 3: GitHub 레포 연결

```bash
# 터미널에서 실행
cd ~/csp-brain

# Git 초기화
git init
git add .
git commit -m "init: csp-brain v2.0 — obsidian hybrid"

# GitHub에서 private repo 생성 (웹 브라우저에서)
# https://github.com/new
# 이름: csp-brain
# Visibility: Private
# README 초기화 체크 해제!

# 리모트 연결 & 푸시
git remote add origin https://github.com/[YOUR-USERNAME]/csp-brain.git
git branch -M main
git push -u origin main
```

## Step 4: Shell Commands 플러그인 설정 (Claude Code 연동)

```
Settings → Shell Commands → New Command

명령어 1: "Claude Code 세션 시작"
  Command: cd ~/csp-brain && claude
  Shell: Terminal (external)

명령어 2: "Git Status"
  Command: cd ~/csp-brain && git status
  Output: Notification

명령어 3: "Dream Cycle 커밋"
  Command: cd ~/csp-brain && git add . && git status
  Output: Notification
```

## Step 5: 첫 Claude Code 세션

```bash
cd ~/csp-brain
claude

# 첫 프롬프트:
> CLAUDE.md를 읽고, 현재 vault 상태를 파악해줘. 
> wiki/에 몇 개의 문서가 있고, 어떤 프로젝트가 추적되고 있는지 status 보고.
```

## Step 6: 일상 워크플로우

### 매일
```
1. 흥미로운 자료 발견 → inbox/에 드래그 앤 드롭
2. 떠오르는 생각 → inbox/notes/에 빠른 메모
3. Claude Code에서 질문 → `query` 프로토콜 자동 실행
```

### 매주 금요일 (Dream Cycle)
```bash
cd ~/csp-brain
claude

> dream
# → INGEST → LINT → DIGEST → BRIDGE → Git commit 순서로 실행
```

### 월 1회
```bash
> lint
# → 전체 위키 점검. 고립 문서, 오래된 Compiled Truth 경고
```

---

## iPad 동기화 (선택)

Working Copy 앱 사용:
1. Working Copy 설치 (App Store)
2. GitHub 계정 연결
3. csp-brain 레포 클론
4. Obsidian Mobile에서 Working Copy 폴더를 Vault로 열기

---

## 트러블슈팅

**Q: 옵시디언에서 .obsidian 폴더가 안 보여요**
A: 숨김 파일입니다. Finder에서 Cmd+Shift+. 로 표시

**Q: Git push가 안 돼요**
A: GitHub Personal Access Token 필요. Settings → Developer settings → Tokens

**Q: Claude Code가 CLAUDE.md를 못 읽어요**
A: `cd ~/csp-brain` 후 `claude` 실행 확인. 반드시 Vault 루트에서 시작

---

*v2.0 — 2026-04-29*
