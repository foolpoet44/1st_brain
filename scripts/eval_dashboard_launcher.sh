#!/bin/bash
#
# csp-brain Eval Dashboard Launcher
# - Eval 점수 계산 (full_vault_eval.py)
# - GitHub 배포 (git push)
# - Telegram 알림 (점수 < 60 점일 때만 경고)
#

set -e

# 설정
VAULT_DIR="/Users/dkmac/Desktop/@26/dev"
SCRIPTS_DIR="$VAULT_DIR/scripts"
LOG_DIR="$VAULT_DIR/_ops/logs"
LOG_FILE="$LOG_DIR/eval-dashboard.log"
TELEGRAM_LOG="$LOG_DIR/eval-telegram.log"

# 로그 디렉토리 생성
mkdir -p "$LOG_DIR"

# 로깅 함수
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

log "=== Eval Dashboard Update Started ==="

# 1. Eval 점수 계산
log "📊 Running full_vault_eval.py..."
cd "$VAULT_DIR"
python3 "$SCRIPTS_DIR/full_vault_eval.py" 2>&1 | tee -a "$LOG_FILE"

# 2. data.json 에서 점수 추출
if [ -f "$VAULT_DIR/data.json" ]; then
    EVAL_SCORE=$(python3 -c "import json; print(json.load(open('data.json')).get('eval_score', 0))" 2>/dev/null || echo "0")
    TOTAL_DOCS=$(python3 -c "import json; print(json.load(open('data.json')).get('total_docs', 0))" 2>/dev/null || echo "0")
    ORPHAN_RATE=$(python3 -c "import json; print(json.load(open('data.json')).get('orphan_rate', 0))" 2>/dev/null || echo "0")
    log "📈 Eval Score: $EVAL_SCORE/100, Total Docs: $TOTAL_DOCS, Orphan Rate: $ORPHAN_RATE%"
else
    log "❌ data.json not found!"
    EVAL_SCORE=0
fi

# 3. GitHub 배포
log "🚀 Pushing to GitHub..."
cd "$VAULT_DIR"

git add -A 2>&1 | tee -a "$LOG_FILE"

# 변경사항이 있을 때만 커밋
if ! git diff --cached --quiet; then
    git commit -m "chore: Eval Dashboard Auto-Update ($(date '+%Y-%m-%d %H:%M'))" 2>&1 | tee -a "$LOG_FILE"
fi

if git push origin main 2>&1 | tee -a "$LOG_FILE"; then
    log "✅ GitHub push successful"
    PUSH_STATUS="success"
else
    log "❌ GitHub push failed"
    PUSH_STATUS="failed"
fi

# 4. Telegram 알림 (점수 < 60 점일 때만 경고)
if (( $(echo "$EVAL_SCORE < 60" | bc -l) )); then
    log "⚠️ Eval Score ($EVAL_SCORE) below threshold (60) - Checking Telegram config..."
    
    # 환경 변수 확인
    if [ -n "$TELEGRAM_BOT_TOKEN" ] && [ -n "$TELEGRAM_CHAT_ID" ]; then
        log "📱 Sending Telegram alert..."
        
        # Telegram 메시지 구성
        MESSAGE="🚨 *csp-brain Eval 경고*

📊 *Eval Score*: $EVAL_SCORE/100
❌ *상태*: 임계치 (60 점) 미만

📈 *주요 지표*:
- Total Docs: $TOTAL_DOCS 개
- Orphan Rate: $ORPHAN_RATE%

🔗 *대시보드*: https://foolpoet44.github.io/1st_brain/

🔧 *조치 필요*:
1. Git 푸시 상태 확인 ($PUSH_STATUS)
2. 고립 문서 연결 강화
3. Type 문서 구조 정비"

        # Telegram API 호출
        curl -s -X POST "https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/sendMessage" \
            -d "chat_id=$TELEGRAM_CHAT_ID" \
            -d "text=$MESSAGE" \
            -d "parse_mode=Markdown" \
            >> "$TELEGRAM_LOG" 2>&1
        
        if [ $? -eq 0 ]; then
            log "✅ Telegram alert sent successfully"
        else
            log "❌ Telegram API call failed"
        fi
    else
        log "⚠️ TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID not set"
        log "📝 To enable Telegram alerts, add these to your shell profile:"
        log "   export TELEGRAM_BOT_TOKEN='your_bot_token'"
        log "   export TELEGRAM_CHAT_ID='your_chat_id'"
        echo "[$(date '+%Y-%m-%d %H:%M:%S')] Telegram skipped - Env vars not set. Score: $EVAL_SCORE" >> "$TELEGRAM_LOG"
    fi
else
    log "✅ Eval Score ($EVAL_SCORE) is healthy (≥60) - No alert needed"
fi

log "=== Eval Dashboard Update Completed ==="
log ""
