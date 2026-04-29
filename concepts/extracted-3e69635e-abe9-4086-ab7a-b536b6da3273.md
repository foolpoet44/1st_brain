# Extracted Knowledge from Conv: 3e69635e-abe9-4086-ab7a-b536b6da3273

**Date**: 2026-02-06T23:01:33.206996Z

### Extracted Code (text)

```text
현재 feature/new-api 브랜치에서 작업 중
→ 긴급 버그 발생 (main 브랜치)
→ 변경사항 stash 또는 commit
→ main 브랜치로 checkout
→ 버그 수정
→ 다시 feature/new-api로 돌아와서 stash pop
→ 컨텍스트 스위칭 비용 발생
```

### Extracted Code (text)

```text
project/
├── main/          (main 브랜치 작업 공간)
├── feature-api/   (feature/new-api 작업 공간)
└── hotfix/        (긴급 수정용 작업 공간)

→ 각 디렉토리에서 독립적으로 작업
→ IDE 창만 전환하면 됨
→ stash 불필요, 컨텍스트 유지
```

### Extracted Code (bash)

```bash
# 새 브랜치와 함께 worktree 생성
git worktree add ../feature-login feature/login

# 기존 브랜치로 worktree 생성
git worktree add ../hotfix-bug hotfix/urgent-bug

# main 브랜치로 임시 worktree 생성
git worktree add ../main-review main
```

### Extracted Code (bash)

```bash
git worktree list

# 출력 예시:
# /Users/csp/project              abc123 [main]
# /Users/csp/feature-login        def456 [feature/login]
# /Users/csp/hotfix-bug           ghi789 [hotfix/urgent-bug]
```

### Extracted Code (bash)

```bash
# 프로젝트 구조
hr-automation/
├── main/                    # 운영 환경 (안정 버전)
├── dev/                     # 일반 개발
├── feature-notion-sync/     # Notion 동기화 기능
├── feature-email-auto/      # 이메일 자동화
└── experimental-ai/         # AI 실험적 기능
```

### Extracted Code (bash)

```bash
# 자동화 스크립트
#!/bin/bash
# ~/scripts/new-automation.sh

AUTOMATION_NAME=$1
cd ~/projects/hr-automation

# 자동으로 새 worktree와 브랜치 생성
git worktree add ../${AUTOMATION_NAME} -b feature/${AUTOMATION_NAME}

# IDE에서 새 창으로 열기
code ../${AUTOMATION_NAME}

echo "✅ 새 자동화 작업 공간 생성: ${AUTOMATION_NAME}"
```

### Extracted Code (bash)

```bash
learning/
├── main/              # 실제 프로젝트
├── tutorial-python/   # Python 학습
├── tutorial-react/    # React 실험
└── sandbox/           # 빠른 테스트
```

### Extracted Code (bash)

```bash
# 동료 코드 리뷰를 위한 worktree
git worktree add ../review-pr-123 pull/123/head

# 내 작업은 계속
# IDE에서 두 창을 나란히 띄워 비교
```

### Extracted Code (bash)

```bash
testing/
├── v1.0-stable/       # 안정 버전 (고객 데모용)
├── v2.0-beta/         # 베타 테스트
└── v3.0-experimental/ # 차기 버전 개발
```

### Extracted Code (text)

```text
일반적인 브랜치 전환:
Mental State A → Disruption → Mental State B

Worktree 사용:
Mental State A (유지)
Mental State B (새로 생성)
→ 두 상태 모두 보존
```

### Extracted Code (bash)

```bash
# 아침: 깊은 사고가 필요한 아키텍처 설계
cd ~/projects/main

# 오후: 에너지가 낮을 때 단순 작업
cd ~/projects/feature-ui-polish

# 저녁: 창의적 실험
cd ~/projects/experimental
```

### Extracted Code (bash)

```bash
# 초기 설정
cd ~/hr-automation
git worktree add ../production main
git worktree add ../dev-report feature/leadership-report
git worktree add ../hotfix -b hotfix/current

# 일상 작업
# Terminal 1: 리포트 개발
cd ~/dev-report
npm run dev

# Terminal 2: 운영 모니터링
cd ~/production
tail -f logs/production.log

# 긴급 상황 발생
cd ~/hotfix
# 빠른 수정 후 배포
git commit -am "Fix urgent email template"
git push origin hotfix/current
```

### Extracted Code (bash)

```bash
# 프로젝트 구조
~/ontology-skills/
├── main/              # 운영 중인 온톨로지 시스템
├── dev-esco-api/      # ESCO API 통합 개발
├── research-palantir/ # Palantir 방식 연구
└── docs/              # 문서화 작업

# 학습과 적용의 순환
# 1. research에서 개념 학습
cd ~/ontology-skills/research-palantir
# Palantir 온톨로지 구조 분석

# 2. dev에서 구현
cd ~/ontology-skills/dev-esco-api
# 학습한 내용을 실제 코드로 적용

# 3. main에서 검증
cd ~/ontology-skills/main
# 기존 시스템과 호환성 테스트
```

### Extracted Code (bash)

```bash
# 대화 아카이빙 시스템 개발
~/notion-automation/
├── main/                    # 안정 버전
├── feature-claude-archive/  # Claude 대화 자동 저장
├── feature-tag-extraction/  # 태그 자동 추출
└── test/                    # 통합 테스트

# 각 기능을 독립적으로 개발하면서
# main에서는 계속 기존 아카이빙 사용
```

### Extracted Code (bash)

```bash
# settings.json
{
  "window.newWindowDimensions": "inherit",
  "workbench.editor.enablePreview": false
}

# 각 worktree를 독립 창으로
code ~/projects/main &
code ~/projects/feature-api &
code ~/projects/hotfix &
```

### Extracted Code (bash)

```bash
# tmux로 여러 worktree 관리
tmux new-session -s work
tmux split-window -h
tmux send-keys "cd ~/projects/main" C-m
tmux split-window -v
tmux send-keys "cd ~/projects/feature-api" C-m
```

### Extracted Code (bash)

```bash
# ~/scripts/clean-worktrees.sh
#!/bin/bash
# 병합된 브랜치의 worktree 자동 정리

git worktree list | while read -r line; do
  path=$(echo $line | awk '{print $1}')
  branch=$(echo $line | grep -oP '\[\K[^\]]+')
  
  if git branch --merged main | grep -q "$branch"; then
    echo "Removing merged worktree: $path"
    git worktree remove "$path"
  fi
done
```

### Extracted Code (text)

```text
작업 중인데 긴급한 일이 생기면?

1. 지금 작업 stash로 저장
2. 다른 브랜치로 이동
3. 긴급 업무 처리
4. 다시 원래 브랜치로 돌아옴
5. stash 복구
→ 귀찮고 집중력 깨짐
```

### Extracted Code (text)

```text
hr-automation/
├── main/           → main 브랜치 (운영용)
├── feature-A/      → 기능A 개발 중
└── hotfix/         → 긴급 수정용

→ 각 폴더를 그냥 열면 됨
→ 창만 바꾸면 됨
```

### Extracted Code (bash)

```bash
# 1. 지금 feature-email 작업 중
cd ~/my-project

# 2. 긴급 버그 수정 필요!
git worktree add ../hotfix hotfix/bug-123

# 3. hotfix 폴더에서 수정
cd ../hotfix
# 여기서 버그 수정, 커밋, 푸시

# 4. 다시 원래 작업으로
cd ~/my-project
# 내 작업은 그대로 남아있음!
```

### Extracted Code (text)

```text
Main (메인)
└─ 1장: 인사
└─ 2장: 본론
└─ 3장: 결론

Feature 브랜치 (실험용)
└─ 1장: 인사
└─ 2장: 본론 (여기를 고쳐보는 중...)
└─ 3장: 결론
└─ 4장: 추가 내용 (새로 써보는 중...)
```

### Extracted Code (text)

```text
😰 상황:
책상에 서류 펼쳐놓고 작업 중
→ 갑자기 다른 급한 일이 생김
→ 근데 지금 서류를 정리할 시간도 없음

📦 Stash = 임시 서랍
→ 펼쳐놓은 서류를 급하게 서랍에 쓸어담음
→ 급한 일 처리
→ 다시 서랍에서 꺼내서 펼침
```

### Extracted Code (text)

```text
현재 상태: feature 브랜치에서 코드 작성 중
파일 3개 수정했는데 아직 커밋 안 함

😱 "Main에서 긴급 버그 수정해야 함!"

❌ 문제:
- 지금 수정한 것들을 커밋하기는 애매함 (아직 덜 됨)
- 그냥 브랜치 바꾸면 수정 내용이 사라짐

✅ 해결: Stash 사용
1. git stash          → 임시 저장
2. main으로 이동      → 버그 수정
3. 다시 feature로     → 원래 작업 복구
4. git stash pop      → 임시 저장 꺼내기
```

### Extracted Code (text)

```text
1. Main에서 시작 (안정 버전)
   ├─ report.py (완성됨)
   └─ email.py (완성됨)

2. 새 기능 개발 시작
   git branch feature/excel-export  (브랜치 생성)
   git checkout feature/excel-export (브랜치로 이동)

3. 작업 중...
   ├─ report.py (수정 중...)
   ├─ email.py
   └─ excel.py (새로 만드는 중...)
   
   (아직 커밋 안 함 - 덜 완성됨)

4. 😱 긴급! Main에서 email.py 버그 발견!
   
   git stash  (현재 작업 임시 저장)
   → "서류를 서랍에 넣음"

5. Main으로 이동
   git checkout main
   
   Main 상태:
   ├─ report.py (깨끗한 버전)
   └─ email.py (깨끗한 버전)

6. 버그 수정
   email.py 고침
   git commit -m "버그 수정"

7. 다시 내 작업으로
   git checkout feature/excel-export
   git stash pop  (임시 저장 꺼냄)
   
   다시 작업 중이던 상태로:
   ├─ report.py (수정 중이던 거 그대로)
   ├─ email.py
   └─ excel.py (만들던 거 그대로)
```

### Extracted Code (text)

```text
Main: 현재 사용 중인 리포트 자동화
      → 매일 아침 실행되고 있음
      → 절대 고장나면 안 됨

Feature 브랜치: 엑셀 내보내기 기능 추가 시도
                → 실험하다 망가져도 OK
                → Main은 계속 돌아감
                → 성공하면 Main에 합침
```

### Extracted Code (bash)

```bash
# 브랜치 관련
git branch                    # 브랜치 목록 보기
git branch 이름               # 새 브랜치 만들기
git checkout 이름             # 브랜치 이동
git checkout -b 이름          # 만들면서 바로 이동

# Stash 관련
git stash                     # 현재 작업 임시 저장
git stash list               # 임시 저장 목록
git stash pop                # 임시 저장 꺼내기
git stash drop               # 임시 저장 버리기
```

### Extracted Code (text)

```text
기존 방식:
- 브랜치 이동할 때마다 파일들이 바뀜
- Stash로 임시 저장 필요

Worktree:
- 각 브랜치가 별도 폴더
- 이동이 아니라 그냥 다른 폴더 열면 됨
- Stash 필요 없음
```

### Extracted Code (text)

```text
┌─────────────────────────────────────────────┐
│  내 컴퓨터 (Local)                           │
├─────────────────────────────────────────────┤
│                                             │
│  📂 Working Directory (작업 폴더)            │
│  ├─ report.py (수정 중...)                  │
│  ├─ email.py                                │
│  └─ config.txt                              │
│           ↓ git add                         │
│                                             │
│  📦 Staging Area (무대 뒤 대기실)            │
│  ├─ report.py ✓ (커밋 준비됨)                │
│           ↓ git commit                      │
│                                             │
│  💾 Repository (.git 폴더)                  │
│  ├─ 커밋1: "초기 버전"                       │
│  ├─ 커밋2: "이메일 기능 추가"                │
│  └─ 커밋3: "리포트 수정" ← 최신              │
│                                             │
└─────────────────────────────────────────────┘
```

### Extracted Code (text)

```text
Main (줄기)
                │
    ┌───────────┼───────────┐
    │           │           │
  커밋1       커밋2       커밋3
    │           │           │
    o ────────> o ────────> o  (안정 버전)
                │
                └──────> o ────> o
                      feature   개발 중
                      (가지)
```

### Extracted Code (text)

```text
Main 브랜치 (줄기 = 공식 버전):
o ──> o ──> o ──> o
v1.0  v1.1  v1.2  v1.3
                   │
                   │ 여기서 가지치기!
                   │
                   └──> o ──> o ──> o
                      feature/excel
                      (실험 버전)
                      
                   └──> o ──> o
                      feature/email
                      (다른 실험)
```

### Extracted Code (text)

```text
시간 흐름 ──────────────────────────────>

Main:
o────────o────────o────────────o
v1.0     v1.1     v1.2         v2.0
"완성"   "버그수정" "안정"      "새기능반영"
                    │            ↑
                    │            │ Merge!
                    │            │
Feature/Excel:      └──> o ──> o
                        "개발" "완성"
                        
                         (여기서 실험)
```

### Extracted Code (text)

```text
1️⃣ Main에서 시작
   Main: o (v1.0 - 기본 리포트 기능)

2️⃣ 새 기능 개발하고 싶다
   git branch feature/excel  (가지 만들기)
   
   Main:          o
                  │
   feature/excel: └──> (여기서 작업 시작)

3️⃣ 각자 진행
   Main:          o ──> o (버그 수정)
                  │
   feature/excel: └──> o ──> o (엑셀 기능 개발)

4️⃣ 개발 완료! Main에 합치기
   Main:          o ──> o ──> o (새 기능 반영!)
                              ↑
                              │ Merge
   feature/excel: o ──> o ────┘
```

### Extracted Code (text)

```text
┌─────────────────────┐         ┌─────────────────────┐
│   내 컴퓨터 (Local)   │         │  GitHub (Remote)    │
├─────────────────────┤         ├─────────────────────┤
│                     │         │                     │
│  Main:              │         │  Main:              │
│  o ──> o ──> o      │  push   │  o ──> o ──> o      │
│            ↑        │ ──────> │            ↑        │
│          여기까지   │         │          동일하게    │
│                     │         │                     │
│  feature/excel:     │         │  feature/excel:     │
│  o ──> o            │  push   │  o ──> o            │
│                     │ ──────> │                     │
│                     │         │                     │
│                     │  pull   │                     │
│                     │ <────── │  (다른 사람이 올린  │
│                     │         │   코드 받아오기)    │
└─────────────────────┘         └─────────────────────┘
```

### Extracted Code (bash)

```bash
# GitHub에 올리기
git push origin main              # Main 브랜치 업로드
git push origin feature/excel     # Feature 브랜치 업로드

# GitHub에서 받기
git pull origin main              # Main 최신 버전 받기
git clone https://github.com/...  # 처음 전체 복사
```

### Extracted Code (text)

```text
상황: feature/excel 브랜치에서 작업 중

┌─────────────────────────────────┐
│ Working Directory               │
│ ├─ report.py (수정 중 50%)      │
│ └─ excel.py (새로 만드는 중)     │
│                                 │
│ 😱 긴급! Main으로 가야 함!       │
│    근데 이거 커밋하기는 애매...   │
└─────────────────────────────────┘
              ↓ git stash
              
┌─────────────────────────────────┐
│ 📦 Stash (임시 보관함)           │
│ [작업내용 임시 저장됨]            │
└─────────────────────────────────┘

┌─────────────────────────────────┐
│ Working Directory               │
│ (깨끗해짐)                       │
│                                 │
│ → Main으로 이동 가능!            │
│ → 긴급 작업 처리                │
└─────────────────────────────────┘
              ↓ git stash pop
              
┌─────────────────────────────────┐
│ Working Directory               │
│ ├─ report.py (수정 중 50%) 복구  │
│ └─ excel.py (새로 만드는 중) 복구 │
│                                 │
│ 다시 원래 작업 계속!              │
└─────────────────────────────────┘
```

### Extracted Code (text)

```text
시작
  ↓
┌─────────────────────────────────────────┐
│ 1. GitHub에서 프로젝트 복사              │
│    git clone https://github.com/...     │
└─────────────────────────────────────────┘
  ↓
┌─────────────────────────────────────────┐
│ 2. 내 컴퓨터에 생김                      │
│    📁 hr-automation/                    │
│    ├─ .git/ (버전 관리 정보)            │
│    ├─ report.py                         │
│    └─ email.py                          │
└─────────────────────────────────────────┘
  ↓
┌─────────────────────────────────────────┐
│ 3. 새 기능 개발 시작                     │
│    git branch feature/excel             │
│    git checkout feature/excel           │
└─────────────────────────────────────────┘
  ↓
┌─────────────────────────────────────────┐
│ 4. 코딩 작업                            │
│    excel.py 파일 생성, 코딩...          │
└─────────────────────────────────────────┘
  ↓
┌─────────────────────────────────────────┐
│ 5. 중간 저장 (커밋)                      │
│    git add excel.py                     │
│    git commit -m "엑셀 기능 추가"        │
└─────────────────────────────────────────┘
  ↓
┌─────────────────────────────────────────┐
│ 6. GitHub에 백업                        │
│    git push origin feature/excel        │
└─────────────────────────────────────────┘
  ↓
┌─────────────────────────────────────────┐
│ 7. 완성! Main에 합치기                   │
│    git checkout main                    │
│    git merge feature/excel              │
│    git push origin main                 │
└─────────────────────────────────────────┘
```

### Extracted Code (text)

```text
📚 책 쓰기로 비유:

Main = 출판된 책 (공식 버전)
Branch = 초안 노트 (이것저것 시도)
Commit = 원고 저장 (버전마다)
Push = 출판사에 보내기
Pull = 편집자 수정본 받기
Merge = 초안을 정식 책에 반영
Stash = 급하게 서랍에 넣기
```
