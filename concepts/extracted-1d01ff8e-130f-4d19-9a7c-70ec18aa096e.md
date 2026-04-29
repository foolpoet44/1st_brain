# Extracted Knowledge from Conv: 1d01ff8e-130f-4d19-9a7c-70ec18aa096e

**Date**: 2026-02-15T22:53:02.669784Z

### Extracted Code (markdown)

```markdown
# CSP Global Claude Rules

## 나는 누구인가
- HR 도메인 전문가 + Vibe coder
- SW 공학 백그라운드 없음 → 설명은 항상 개념 먼저, 코드 나중
- 실용적 자동화 우선: 완벽한 코드보다 작동하는 코드

## 커뮤니케이션 규칙
- 한국어로 응답할 것
- 불렛 리스트보다 에세이형 설명 선호
- 철학적/심리학적 유추를 활용한 개념 설명 환영
- 코드 설명 시 "왜"를 반드시 포함할 것

## 코딩 스타일
- Python 우선, 필요시 JavaScript
- 함수는 단일 책임 원칙
- 복잡한 로직엔 반드시 주석 (한국어)
- 에러 처리는 생략하지 말 것

## 절대 하지 말 것
- 설명 없이 코드만 던지지 말 것
- 과도한 추상화 금지 (나중에 이해 못함)
- 라이브러리 남발 금지 → 가능하면 표준 라이브러리

## 선호하는 도구 스택
- 자동화: Python + n8n
- DB: Notion API, Supabase
- AI: Claude API, OpenAI API
- 버전관리: Git (커밋 메시지는 한국어 허용)

## 작업 원칙
"Do it once, automate it forever"
→ 반복 작업이 보이면 반드시 자동화 방법을 제안할 것
```

### Extracted Code (markdown)

```markdown
## 불확실할 때의 규칙
- 내 의도가 불명확하면 코드 작성 전에 먼저 질문할 것
- 여러 방법이 있을 때는 트레이드오프를 설명하고 선택을 물을 것
- 기존 코드를 크게 바꿔야 할 때는 반드시 먼저 알릴 것
```

### Extracted Code (markdown)

```markdown
# CSP Global Rules

## 컨텍스트 로딩 지시
- 프로젝트 워크스페이스에 CLAUDE.md 또는 AGENTS.md가 있으면 반드시 먼저 읽을 것
- 하위 폴더에도 CLAUDE.md가 있을 수 있으니 재귀적으로 탐색할 것
- 읽은 후 "CLAUDE.md 로드 완료" 메시지를 출력할 것

## 기본 규칙 (CLAUDE.md 없을 때 fallback)
- 한국어로 응답
- 에세이형 설명 선호
- 코드보다 "왜"를 먼저 설명
```

### Extracted Code (text)

```text
~/.gemini/antigravity/skills/
├── csp-communication/
│   └── SKILL.md          ← 응답 스타일 규칙
├── hr-ontology/
│   └── SKILL.md          ← HR 도메인 지식
└── python-automation/
    └── SKILL.md          ← 자동화 코딩 규칙
```

### Extracted Code (markdown)

```markdown
---
name: csp-communication
description: CSP의 커뮤니케이션 스타일로 응답해야 할 때. 
             한국어 응답, 에세이형 설명이 필요할 때 사용.
---

# CSP Communication Style

## 응답 원칙
- 반드시 한국어로 응답
- 불렛 포인트보다 에세이형 문단 선호
- 철학적/심리학적 유추로 개념 설명
- 코드 전에 반드시 "왜"를 먼저 설명

## 코딩 설명 방식
- SW 백그라운드 없는 HR 전문가 수준으로 설명
- 과도한 추상화 금지
- 표준 라이브러리 우선, 라이브러리 남발 금지
```

### Extracted Code (bash)

```bash
# 기존 CLAUDE.md를 공통 소스로
mkdir -p ~/.config/ai-rules
cp ~/.claude/CLAUDE.md ~/.config/ai-rules/GLOBAL.md

# 각 도구가 같은 파일을 바라보게
ln -sf ~/.config/ai-rules/GLOBAL.md ~/.claude/CLAUDE.md
ln -sf ~/.config/ai-rules/GLOBAL.md ~/.gemini/CLAUDE.md  
# GEMINI.md에서 CLAUDE.md를 읽도록 지시
```

### Extracted Code (markdown)

```markdown
# CSP Global Working Agreements

## 나는 누구인가
- HR 도메인 전문가 + Vibe coder (SW 공학 백그라운드 없음)
- 17년 LG PRI HR 경험 기반 자동화 시스템 구축자
- 철학: "Do it once, automate it forever"

## 커뮤니케이션 규칙
- 반드시 한국어로 응답
- 불렛 리스트보다 에세이형 문단 설명 선호
- 코드 전에 반드시 "왜"를 먼저 설명
- 철학적/심리학적 유추 활용 환영

## 코딩 원칙
- Python 우선, 표준 라이브러리 먼저
- 과도한 추상화 금지 (이해 불가능한 패턴 사용 금지)
- 복잡한 로직엔 한국어 주석 필수
- 에러 처리 생략 금지

## 불확실할 때의 규칙
- 의도가 불명확하면 코드 작성 전에 먼저 질문
- 여러 방법이 있으면 트레이드오프 설명 후 선택 요청
- 기존 코드를 크게 바꿀 때는 반드시 사전 고지

## 선호 도구 스택
- 자동화: Python, n8n
- DB: Notion API, Supabase
- AI: Claude API, OpenAI API
- 버전관리: Git
```

### Extracted Code (text)

```text
~/projects/hr-automation/
├── AGENTS.md              ← 프로젝트 전체 규칙
└── esco-api/
    └── AGENTS.md          ← 이 모듈만의 추가 규칙
```

### Extracted Code (markdown)

```markdown
# HR Automation Project Rules

## 도메인 컨텍스트
- LG PRI 역량 평가 자동화 시스템
- ESCO API 기반 디지털 스킬 온톨로지 연동
- Notion을 세컨브레인 + 데이터베이스로 동시 활용

## 코드 규칙
- Notion API 호출은 반드시 rate limit 처리 포함
- 역량 데이터는 skills_ontology.py 모듈을 통해서만 접근
- 테스트 실행: `python -m pytest tests/`

## 절대 하지 말 것
- 실제 직원 데이터를 로그에 출력하지 말 것
- Notion DB 스키마를 임의로 변경하지 말 것
```

### Extracted Code (bash)

```bash
# 임시 오버라이드 생성
echo "# Temp Override\n- Respond in English only" > ~/.codex/AGENTS.override.md

# 작업 완료 후 삭제
rm ~/.codex/AGENTS.override.md
```

### Extracted Code (bash)

```bash
# 전역 Skills 위치
~/.codex/skills/          ← Codex CLI 전역
~/.claude/skills/         ← Claude Code 전역

# 같은 내용을 공유하려면 심볼릭 링크
mkdir -p ~/.codex/skills
ln -sf ~/.claude/skills/csp-communication ~/.codex/skills/csp-communication
```

### Extracted Code (bash)

```bash
# 공통 소스 하나를 만들고
mkdir -p ~/.config/ai-rules
nano ~/.config/ai-rules/GLOBAL.md   ← 여기서만 편집

# 각 도구가 심볼릭 링크로 바라보게
ln -sf ~/.config/ai-rules/GLOBAL.md ~/.claude/CLAUDE.md
ln -sf ~/.config/ai-rules/GLOBAL.md ~/.codex/AGENTS.md

# Antigravity는 직접 로드 지원 안 하므로
# ~/.gemini/GEMINI.md에 "CLAUDE.md를 읽어라" 지시만 추가
```

### Extracted Code (powershell)

```powershell
# .gemini 폴더 생성
mkdir $env:USERPROFILE\.gemini

# 메모장으로 편집
notepad $env:USERPROFILE\.gemini\GEMINI.md
```

### Extracted Code (markdown)

```markdown
# CSP Global Rules

## 커뮤니케이션 규칙
- 반드시 한국어로 응답
- 불렛 리스트보다 에세이형 문단 설명 선호
- 코드 전에 반드시 "왜"를 먼저 설명
- 철학적/심리학적 유추 활용 환영

## 코딩 원칙
- Python 우선, 표준 라이브러리 먼저
- 과도한 추상화 금지
- 복잡한 로직엔 한국어 주석 필수
- 에러 처리 생략 금지

## 불확실할 때의 규칙
- 의도 불명확하면 코드 전에 먼저 질문
- 기존 코드 크게 바꿀 때 반드시 사전 고지

## 작업 원칙
"Do it once, automate it forever"
→ 반복 작업 보이면 반드시 자동화 방법 제안

## 프로젝트 컨텍스트 파일 로딩 지시
- 프로젝트 워크스페이스에 CLAUDE.md 또는 AGENTS.md가
  있으면 반드시 먼저 읽고 시작할 것
- 하위 폴더도 재귀적으로 탐색할 것
```

### Extracted Code (cmd)

```cmd
:: 공통 소스 폴더 생성
mkdir %USERPROFILE%\.config\ai-rules

:: GLOBAL.md 생성 (여기서만 편집)
notepad %USERPROFILE%\.config\ai-rules\GLOBAL.md

:: 각 도구가 하드링크로 바라보게 설정
:: (하드링크 = 심볼릭 링크보다 안정적, GEMINI.md 버그 우회)
mklink /H %USERPROFILE%\.claude\CLAUDE.md ^
          %USERPROFILE%\.config\ai-rules\GLOBAL.md

mklink /H %USERPROFILE%\.gemini\GEMINI.md ^
          %USERPROFILE%\.config\ai-rules\GLOBAL.md

mklink /H %USERPROFILE%\.codex\AGENTS.md ^
          %USERPROFILE%\.config\ai-rules\GLOBAL.md
```

### Extracted Code (text)

```text
C:\Users\사용자명\projects\hr-automation\
├── CLAUDE.md        ← Claude Code용
├── AGENTS.md        ← Codex CLI용 (내용 동일해도 됨)
└── .antigravity\
    └── rules.md     ← Antigravity 프로젝트 규칙
```

### Extracted Code (markdown)

```markdown
# CSP Gemini CLI Global Context

## 나는 누구인가
- HR 도메인 전문가 + Vibe coder
- SW 공학 백그라운드 없음
- 17년 LG PRI HR 경험 기반 자동화 구축자

## 커뮤니케이션 규칙
- 반드시 한국어로 응답
- 불렛 리스트보다 에세이형 설명 선호
- 코드 전에 "왜"를 먼저 설명
- 철학적/심리학적 유추 활용

## 코딩 원칙
- Python 우선, 표준 라이브러리 먼저
- 복잡한 로직엔 한국어 주석 필수
- 에러 처리 생략 금지
- 과도한 추상화 금지

## 불확실할 때
- 의도 불명확하면 먼저 질문
- 여러 방법 있으면 트레이드오프 설명 후 선택 요청

## 작업 원칙
"Do it once, automate it forever"
```

### Extracted Code (markdown)

```markdown
# CSP Global Context

## 도구 구분 안내
- `.gemini/antigravity/` 폴더와 `mcp_config.json`은 Antigravity IDE 전용
- Gemini CLI는 `extensions/` 디렉토리와 `settings.json` 사용
- 두 도구를 혼동하거나 동기화 시도하지 말 것

## (이하 나머지 규칙...)
```

### Extracted Code (markdown)

```markdown
# Global Context for Gemini Tools

## 공통 규칙 (CLI & Antigravity 공통)
- 한국어 응답
- 에세이형 설명 선호
- "Do it once, automate it forever"

---

## Gemini CLI 전용 규칙
<!-- Antigravity에서는 무시 -->
- 터미널 명령어 실행 시 항상 설명 먼저
- 파일 변경 전 diff 보여줄 것

---

## Antigravity IDE 전용 규칙
<!-- Gemini CLI에서는 무시 -->
- Agent Manager에서 작업 시 Plan 모드 우선
- Browser Artifacts 생성 시 스크린샷 포함
```

### Extracted Code (text)

```text
~/.gemini/GEMINI.md           ← 전역 (모든 프로젝트)
↓
프로젝트/GEMINI.md            ← 프로젝트 전용
↓
프로젝트/하위폴더/GEMINI.md   ← 모듈 전용
```

### Extracted Code (markdown)

```markdown
# HR Automation Project Context

## 프로젝트 정보
- LG PRI 역량 평가 자동화 시스템
- ESCO API 기반 온톨로지 연동
- Notion을 세컨브레인 + DB로 활용

## 프로젝트 규칙
- Notion API 호출 시 rate limit 처리 필수
- 역량 데이터는 skills_ontology.py만 통해 접근
- 실제 직원 데이터 로그 출력 금지
```

### Extracted Code (markdown)

```markdown
# ~/.gemini/GEMINI.md

## 프로젝트 컨텍스트 파일 로딩
- 프로젝트에 AGENTS.md 또는 CLAUDE.md가 있으면 먼저 읽을 것
- 이 파일들의 내용을 우선 컨텍스트로 활용할 것
- 하위 폴더도 재귀적으로 탐색할 것

## (이하 나머지 규칙...)
```

### Extracted Code (bash)

```bash
# 공통 소스 생성
mkdir -p ~/.config/ai-rules
nano ~/.config/ai-rules/GLOBAL.md

# 각 도구가 같은 파일 바라보게
ln -sf ~/.config/ai-rules/GLOBAL.md ~/.claude/CLAUDE.md
ln -sf ~/.config/ai-rules/GLOBAL.md ~/.codex/AGENTS.md
ln -sf ~/.config/ai-rules/GLOBAL.md ~/.gemini/GEMINI.md
```

### Extracted Code (cmd)

```cmd
mkdir %USERPROFILE%\.config\ai-rules
notepad %USERPROFILE%\.config\ai-rules\GLOBAL.md

:: 하드링크로 연결 (심볼릭 링크 버그 우회)
mklink /H %USERPROFILE%\.claude\CLAUDE.md ^
          %USERPROFILE%\.config\ai-rules\GLOBAL.md

mklink /H %USERPROFILE%\.codex\AGENTS.md ^
          %USERPROFILE%\.config\ai-rules\GLOBAL.md

mklink /H %USERPROFILE%\.gemini\GEMINI.md ^
          %USERPROFILE%\.config\ai-rules\GLOBAL.md
```

### Extracted Code (text)

```text
~/.config/ai-rules/
  └── GLOBAL.md              ← 단일 소스 (여기서만 편집)
       ↓ (하드링크)
~/.claude/CLAUDE.md          ← Claude Code
~/.codex/AGENTS.md           ← Codex CLI  
~/.gemini/GEMINI.md          ← Gemini CLI (+ Antigravity 전역)
       ↓
프로젝트/.antigravity/rules.md  ← Antigravity 프로젝트 전용
프로젝트/GEMINI.md               ← Gemini CLI 프로젝트 전용
```
