# Extracted Knowledge from Conv: 376f0556-c72d-490c-a80b-7dbeb11dfc4a

**Date**: 2026-04-05T08:38:47.989196Z

### Extracted Code (text)

```text
┌─────────────────────────────────────────────────────┐
│              CSP 24/7 Code Factory                   │
├─────────────┬──────────────────┬────────────────────┤
│  LANE 1     │   LANE 2         │   LANE 3           │
│  Interactive│   Async Agent    │   Batch            │
│  (Pro 구독)  │   (API Key)      │   (Batch API -50%) │
│             │                  │                    │
│  실시간 응답  │  자율 루프 실행   │  비실시간 대량 처리  │
│  CSP 직접   │  밤새 빌드/테스트  │  코드리뷰, 문서화    │
│  대화하며   │  ESCON 자동화     │  Daily Radar 생성   │
│  코딩       │  CI/CD 파이프라인  │  Skill Ontology     │
└─────────────┴──────────────────┴────────────────────┘
```

### Extracted Code (bash)

```bash
# ~/.csp_interactive (Lane 1 - Pro 구독)
unset ANTHROPIC_API_KEY
alias csp-interactive="claude"

# ~/.csp_agent (Lane 2 - API Key)
export ANTHROPIC_API_KEY="sk-ant-..."
export CSP_LANE="agent"
alias csp-agent="claude -p --dangerously-skip-permissions"
```

### Extracted Code (python)

```python
# cost_watchdog.py
import anthropic, time, subprocess, os

client = anthropic.Anthropic()
DAILY_BUDGET_USD = 5.0  # CSP가 설정하는 일일 한도

def check_and_kill():
    # Anthropic Console API로 당일 사용량 조회
    # 한도 초과 시 agent 프로세스 SIGTERM
    pass

while True:
    check_and_kill()
    time.sleep(300)  # 5분마다 체크
```

### Extracted Code (python)

```python
# batch_runner.py - Batch API 호출
client.beta.messages.batches.create(
    requests=[
        {"custom_id": "daily-radar", "params": {...}},
        {"custom_id": "code-review-escon", "params": {...}},
    ]
)
```

### Extracted Code (text)

```text
ESCON 작업 성격별 분류

① 짧고 독립적인 작업 (세션당 1~2회 Claude 호출)
  - 특정 컴포넌트 버그 수정
  - 단일 API 엔드포인트 추가
  - Supabase 쿼리 최적화

② 긴 반복 작업 (세션을 오래 물고 있음 → quota 폭탄)
  - "전체 리팩터링 해줘"
  - "모든 컴포넌트 타입 체크해줘"
  - "테스트 다 짜줘"
```

### Extracted Code (text)

```text
escon-factory/
├── CLAUDE.md          # 에이전트 행동 규칙
├── task_queue.json    # 작업 큐 (수동 추가)
├── factory.sh         # 메인 실행 루프
├── quota_guard.sh     # quota 상태 감시
└── session_log/       # 실행 기록
```

### Extracted Code (bash)

```bash
#!/bin/bash
# ESCON Auto-Factory: quota-safe 자율 실행 루프

TASK_QUEUE="task_queue.json"
PROJECT_DIR="~/escon"
LOG_DIR="./session_log"

run_task() {
    local task="$1"
    local task_id="$2"
    
    echo "[$(date)] Starting task: $task_id" >> $LOG_DIR/run.log
    
    # 핵심: -p 플래그로 단일 세션, 작업 완료 후 즉시 종료
    # context를 최소화한 명시적 프롬프트 주입
    claude -p \
        --allowedTools "Edit,Write,Bash,Read" \
        --max-turns 10 \
        "ESCON 프로젝트 컨텍스트: Next.js + Supabase, GitHub: foolpoet44/escon
        
        작업: $task
        
        완료 조건을 충족하면 즉시 종료하세요. 불필요한 탐색 금지." \
        2>&1 | tee $LOG_DIR/${task_id}.log
    
    echo "[$(date)] Completed: $task_id" >> $LOG_DIR/run.log
}

# 큐에서 작업 하나씩 꺼내 실행
while true; do
    # quota 상태 확인
    STATUS=$(claude /status 2>/dev/null)
    if echo "$STATUS" | grep -q "limit reached"; then
        echo "[$(date)] Quota exhausted. Sleeping 30min..." >> $LOG_DIR/run.log
        sleep 1800  # 30분 대기 후 재확인
        continue
    fi
    
    # 다음 작업 꺼내기
    TASK=$(python3 -c "
import json
with open('$TASK_QUEUE') as f:
    q = json.load(f)
if q['pending']:
    task = q['pending'].pop(0)
    q['running'] = task
    with open('$TASK_QUEUE', 'w') as f:
        json.dump(q, f, indent=2)
    print(task['prompt'])
")
    
    if [ -z "$TASK" ]; then
        echo "[$(date)] Queue empty. Waiting..." >> $LOG_DIR/run.log
        sleep 300  # 5분 대기
        continue
    fi
    
    run_task "$TASK" "task_$(date +%s)"
    sleep 60  # 작업 간 1분 간격 (quota 안전 버퍼)
done
```

### Extracted Code (json)

```json
{
  "pending": [
    {
      "id": "escon-001",
      "priority": "high",
      "prompt": "src/components/SkillCard.tsx의 타입 에러를 수정하세요. valid_from/valid_to 컬럼 타입이 string | null인데 Date로 처리하는 부분 찾아서 고치기."
    },
    {
      "id": "escon-002", 
      "priority": "normal",
      "prompt": "Supabase의 skill_records 테이블 쿼리에서 N+1 문제가 있는 곳을 찾아 단일 쿼리로 최적화하세요."
    }
  ],
  "running": null,
  "completed": []
}
```

### Extracted Code (markdown)

```markdown
# ESCON Auto-Factory Rules

## 절대 규칙
- 주어진 작업 하나만 완료하고 종료
- 관련 없는 파일 탐색 금지
- 작업 완료 후 추가 개선 제안 금지 (quota 낭비)
- 불확실하면 TODO 주석 남기고 종료 (무한 탐색 금지)

## 프로젝트 컨텍스트
- Stack: Next.js 14, Supabase, TypeScript
- DB: skill_records (valid_from, valid_to: timestamp)
- 브랜치 규칙: feature/escon-[task-id]

## 완료 정의
- 코드 수정 완료 + 빌드 에러 없음 = 작업 종료
```

### Extracted Code (bash)

```bash
# 1. escon 프로젝트 디렉토리에서
cd ~/escon
mkdir -p escon-factory/session_log

# 2. Claude Code로 factory 파일들 생성
claude "escon-factory/ 디렉토리 구조와 위에서 설계한 
factory.sh, task_queue.json, CLAUDE.md를 생성해줘"

# 3. 첫 작업 추가하고 테스트 실행
chmod +x escon-factory/factory.sh
./escon-factory/factory.sh
```

### Extracted Code (text)

```text
~/.csp-factory/
├── bin/
│   └── csp                 # 단일 CLI 진입점
├── core/
│   ├── factory.sh          # 메인 실행 루프
│   ├── queue_manager.py    # 큐 CRUD
│   └── quota_guard.sh      # quota 감시
├── projects/
│   └── registry.json       # 등록된 프로젝트 목록
├── queue/
│   └── tasks.json          # 작업 큐 (pending/running/done)
├── logs/
│   └── YYYY-MM-DD/         # 날짜별 실행 로그
└── templates/
    └── CLAUDE.md.tmpl      # 범용 에이전트 행동 규범
```

### Extracted Code (bash)

```bash
# 프로젝트 등록
csp project add escon ~/escon "Next.js + Supabase, TKG 아키텍처"
csp project add pulse ~/pulse-check "React + Supabase, Magic Link"
csp project add ax-portal ~/ax-portal "HTML 포털, LG CHO 디자인 시스템"

# 작업 추가
csp add escon "SkillCard 타입 에러 수정, valid_from/valid_to 처리"
csp add pulse "Magic Link 이메일 템플릿 한국어 버전 추가"
csp add ax-portal "Y26 인증 프레임워크 Lv.3 섹션 컴포넌트 추가"

# 팩토리 제어
csp start          # 팩토리 데몬 시작
csp stop           # 팩토리 중단
csp status         # 현재 상태 확인
csp log            # 최근 실행 로그
csp queue          # 대기 중인 작업 목록
```

### Extracted Code (text)

```text
~/.csp-factory 디렉토리에 범용 Claude Code 자동화 팩토리를 구축해줘.

## 요구사항

### 1. CLI 진입점: ~/.csp-factory/bin/csp

다음 명령어를 지원하는 bash 스크립트:

csp project add <name> <path> <description>
  - ~/.csp-factory/projects/registry.json에 프로젝트 등록
  
csp add <project_name> <task_description>
  - registry에서 프로젝트 정보 조회
  - ~/.csp-factory/queue/tasks.json의 pending 배열에 추가
  - task_id는 <project>-<timestamp> 형식

csp start
  - ~/.csp-factory/core/factory.sh를 백그라운드 데몬으로 실행
  - PID를 ~/.csp-factory/factory.pid에 저장

csp stop  
  - factory.pid 읽어서 프로세스 종료

csp status
  - 현재 실행 중인 작업, quota 상태, 큐 대기 수 출력

csp queue
  - pending 작업 목록을 테이블 형식으로 출력

csp log
  - 최근 10개 작업 실행 결과 출력

### 2. 프로젝트 레지스트리: projects/registry.json
```

### Extracted Code (text)

```text
### 4. 메인 팩토리 루프: core/factory.sh

루프 로직:
1. quota 상태 확인 (`claude /status` 파싱)
2. quota 소진 시 → 30분 sleep 후 재확인
3. pending에서 첫 번째 작업 꺼내기
4. 프로젝트 registry에서 경로, description 조회
5. claude -p 실행:
   - --allowedTools "Edit,Write,Bash,Read"
   - --max-turns 15
   - working directory를 프로젝트 경로로 설정
   - 시스템 프롬프트에 프로젝트 description + 작업 주입
6. 완료 후 tasks.json에서 running → completed 이동
7. 로그를 logs/YYYY-MM-DD/<task_id>.log에 저장
8. 작업 간 60초 간격

claude -p 호출 형식:
```

### Extracted Code (text)

```text
### 5. quota 감시: core/quota_guard.sh

`claude /status` 출력에서 limit 관련 키워드 감지.
소진 감지 시 exit code 1 반환.

### 6. 범용 에이전트 규범: templates/CLAUDE.md.tmpl
```

### Extracted Code (text)

```text
### 7. 설치 스크립트: install.sh

- ~/.csp-factory/ 전체 구조 생성
- chmod +x bin/csp
- PATH에 ~/.csp-factory/bin 추가 (~/.<shell>rc에 export 추가)
- 설치 완료 메시지 출력

## 최종 확인
모든 파일 생성 후:
1. install.sh 실행
2. `csp project add escon ~/escon "Next.js + Supabase, TKG 아키텍처"` 테스트
3. `csp queue` 실행하여 정상 동작 확인
```

### Extracted Code (bash)

```bash
# Claude Code 실행
claude

# 위 프롬프트 붙여넣기 → 엔터
# Claude Code가 전체 구조 생성 + install.sh 실행까지 완료

# 이후 사용
source ~/.zshrc  # 또는 ~/.bashrc
csp project add escon ~/escon "Next.js + Supabase, TKG 아키텍처"
csp add escon "첫 번째 자동화 작업 내용"
csp start
csp status
```

### Extracted Code (text)

```text
Pro 구독 (Claude Sonnet 4.6)
    ↓ quota 소진
OpenRouter 무료 티어 (deepseek-r1:free, gemma-3 등)
    ↓ rate limit 도달
NVIDIA NIM 무료 (40 req/min, Kimi-K2.5)
    ↓ 한도 도달
Ollama 로컬 (완전 무료, 인터넷 불필요)
```

### Extracted Code (text)

```text
~/.csp-factory 디렉토리에 범용 Claude Code 자동화 팩토리를 구축해줘.
quota 소진 시 무료 모델로 자동 폴백하는 구조가 핵심이야.

## 전체 구조

~/.csp-factory/
├── bin/csp                    # CLI 진입점
├── core/
│   ├── factory.sh             # 메인 루프
│   ├── model_router.sh        # 폴백 엔진 (핵심)
│   └── quota_guard.sh         # quota 상태 감지
├── config/
│   ├── models.json            # 폴백 체인 설정
│   └── projects.json          # 프로젝트 레지스트리
├── queue/
│   └── tasks.json             # 작업 큐
├── logs/
│   └── .gitkeep
└── install.sh

---

## 1. config/models.json — 폴백 체인
```

### Extracted Code (text)

```text
---

## 6. install.sh 포함하여 전체 파일 생성 및 실행

모든 파일 생성 완료 후:
1. install.sh 실행 (chmod, PATH 설정)
2. ~/.zshrc에 OPENROUTER_API_KEY, NVIDIA_NIM_API_KEY 환경변수 추가 안내 출력
3. `csp project add escon ~/escon "Next.js + Supabase, TKG 아키텍처, valid_from/valid_to 타임스탬프 컬럼"` 테스트 실행
4. `csp status` 실행하여 tier 1 확인
```
