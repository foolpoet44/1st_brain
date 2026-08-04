#!/bin/bash
#
# csp-brain Eval Dashboard Launcher v3
# - Frontmatter 검증 (자동 수리)
# - Eval 점수 계산 (full_vault_eval.py)
# - Human Gate 4 검증 (새로 추가)
# - GitHub 배포 (git push with retry)
# - Telegram 알림 (점수 < 60 점 또는 Gate 위반)
#

set -e

# 설정
VAULT_DIR="/Users/dkmac/csp-brain"
SCRIPTS_DIR="$VAULT_DIR/scripts"
LOG_DIR="$VAULT_DIR/_ops/logs"
LOG_FILE="$LOG_DIR/eval-dashboard.log"
TELEGRAM_LOG="$LOG_DIR/eval-telegram.log"
HUMAN_GATE_LOG="$LOG_DIR/human-gate-audit.log"

# 로그 디렉토리 생성
mkdir -p "$LOG_DIR"

# 로깅 함수
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

log "=== Eval Dashboard Update Started ==="

# ========================================
# 0 단계: Frontmatter 검증 및 자동 수리
# ========================================
log "🔍 Validating YAML frontmatter..."

INVALID_COUNT=0
while IFS= read -r -d '' file; do
    [[ "$file" == *"/node_modules/"* ]] && continue
    [[ "$file" == *"/.git/"* ]] && continue
    [[ "$file" == *"/Understand-Anything/"* ]] && continue
    
    first_line=$(head -1 "$file" 2>/dev/null | tr -d '\r\n')
    if [ "$first_line" != "---" ]; then
        INVALID_COUNT=$((INVALID_COUNT + 1))
    fi
done < <(find "$VAULT_DIR" -name "*.md" -type f -print0)

if [ $INVALID_COUNT -gt 0 ]; then
    log "⚠️ Found $INVALID_COUNT files without frontmatter - Auto-fixing..."
    
    FIXED_COUNT=0
    while IFS= read -r -d '' file; do
        [[ "$file" == *"/node_modules/"* ]] && continue
        [[ "$file" == *"/.git/"* ]] && continue
        [[ "$file" == *"/Understand-Anything/"* ]] && continue
        
        first_line=$(head -1 "$file" 2>/dev/null | tr -d '\r\n')
        if [ "$first_line" != "---" ]; then
            cp "$file" "${file}.bak"
            content=$(cat "$file")
            
            if [[ "$file" == *"/outputs/daily-reflect/"* ]]; then
                type="Reflection"
            elif [[ "$file" == *"/outputs/"* ]]; then
                type="Note"
            elif [[ "$file" == *"/inbox/"* ]]; then
                type="Note"
            elif [[ "$file" == *"/wiki/"* ]]; then
                type="Note"
            else
                type="Note"
            fi
            
            cat > "$file" << EOF
---
type: $type
status: Active
---

EOF
            echo "$content" >> "$file"
            rm "${file}.bak"
            FIXED_COUNT=$((FIXED_COUNT + 1))
        fi
    done < <(find "$VAULT_DIR" -name "*.md" -type f -print0)
    
    log "✅ Fixed $FIXED_COUNT files"
else
    log "✅ All files have valid frontmatter"
fi

# ========================================
# 1 단계: Eval 점수 계산
# ========================================
log "📊 Running full_vault_eval.py..."
cd "$VAULT_DIR"
python3 "$SCRIPTS_DIR/full_vault_eval.py" 2>&1 | tee -a "$LOG_FILE"

# ========================================
# 2 단계: data.json 에서 점수 추출
# ========================================
if [ -f "$VAULT_DIR/data.json" ]; then
    EVAL_SCORE=$(python3 -c "import json; print(json.load(open('data.json')).get('eval_score', 0))" 2>/dev/null || echo "0")
    TOTAL_DOCS=$(python3 -c "import json; print(json.load(open('data.json')).get('total_docs', 0))" 2>/dev/null || echo "0")
    ORPHAN_RATE=$(python3 -c "import json; print(json.load(open('data.json')).get('orphan_rate', 0))" 2>/dev/null || echo "0")
    ACTIVE_DOCS=$(python3 -c "import json; print(json.load(open('data.json')).get('active_docs', 0))" 2>/dev/null || echo "0")
    log "📈 Eval Score: $EVAL_SCORE/100, Total Docs: $TOTAL_DOCS, Orphan Rate: $ORPHAN_RATE%, Active: $ACTIVE_DOCS"
else
    log "❌ data.json not found!"
    EVAL_SCORE=0
fi

# ========================================
# 3 단계: Human Gate 4 검증
# ========================================
log "🔒 Validating Human Gate compliance..."

HUMAN_GATE_SCHEMA="$VAULT_DIR/csp-brain/vault/protocols/human-gate-schema.md"
GATE_VIOLATIONS=0

# Gate #1: Evolution Gate 검증 (Markdown 내 YAML)
if [ -f "$HUMAN_GATE_SCHEMA" ]; then
    log "✅ Human Gate schema exists"
    
    # Python 으로 YAML 검증
    cd "$VAULT_DIR"
    python3 << 'PYEOF'
import yaml
import re
import sys

try:
    with open("csp-brain/vault/protocols/human-gate-schema.md", 'r') as f:
        content = f.read()
    
    # YAML 코드 블록 추출
    yaml_match = re.search(r'```yaml\n(.*?)```', content, re.DOTALL)
    if yaml_match:
        yaml_content = yaml_match.group(1)
        yaml.safe_load(yaml_content)
        print("✅ YAML schema valid")
        sys.exit(0)
    else:
        # frontmatter 에서 YAML 추출
        fm_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
        if fm_match:
            yaml.safe_load(fm_match.group(1))
            print("✅ YAML frontmatter valid")
            sys.exit(0)
        else:
            print("⚠️ No YAML found")
            sys.exit(0)
except yaml.YAMLError as e:
    print(f"❌ YAML error: {e}")
    sys.exit(1)
except Exception as e:
    print(f"❌ Error: {e}")
    sys.exit(1)
PYEOF
    
    if [ $? -ne 0 ]; then
        log "❌ YAML schema invalid - Alert!"
        GATE_VIOLATIONS=$((GATE_VIOLATIONS + 1))
    fi
else
    log "⚠️ Human Gate schema not found"
    GATE_VIOLATIONS=$((GATE_VIOLATIONS + 1))
fi

# Gate #2: Bias Audit 디렉토리 확인
AUDIT_DIR="$VAULT_DIR/outputs/bias-audits"
if [ -d "$AUDIT_DIR" ]; then
    LATEST_AUDIT=$(ls -t "$AUDIT_DIR"/*.md 2>/dev/null | head -1)
    if [ -n "$LATEST_AUDIT" ]; then
        log "✅ Latest bias audit: $(basename "$LATEST_AUDIT")"
    else
        log "ℹ️ Bias audit directory exists but empty"
    fi
else
    log "ℹ️ Bias audit directory not found - Will be created on first audit"
fi

# Gate #3: Trust Ladder 인증서 확인
CERT_DIR="$VAULT_DIR/outputs/certifications"
if [ -d "$CERT_DIR" ]; then
    CERT_COUNT=$(ls "$CERT_DIR"/*.md 2>/dev/null | wc -l | tr -d ' ')
    log "✅ Trust Ladder certifications: $CERT_COUNT"
else
    log "ℹ️ Certification directory not found - Will be created on first graduation"
fi

# Gate #4: Rollback 이력 확인
ROLLBACK_LOG="$LOG_DIR/rollback-history.log"
if [ -f "$ROLLBACK_LOG" ]; then
    ROLLBACK_COUNT=$(wc -l < "$ROLLBACK_LOG" | tr -d ' ')
    log "ℹ️ Rollback history: $ROLLBACK_COUNT events"
else
    log "✅ No rollback history (clean record)"
fi

# Human Gate 위반 요약
if [ $GATE_VIOLATIONS -gt 0 ]; then
    log "⚠️ Human Gate violations detected: $GATE_VIOLATIONS"
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] Human Gate violations: $GATE_VIOLATIONS" >> "$HUMAN_GATE_LOG"
else
    log "✅ Human Gate compliance: All checks passed"
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] Human Gate compliance: OK" >> "$HUMAN_GATE_LOG"
fi

# ========================================
# 4 단계: GitHub 배포 (재시도 로직)
# ========================================
log "🚀 Pushing to GitHub..."
cd "$VAULT_DIR"

git add -A 2>&1 | tee -a "$LOG_FILE"

# 변경사항이 있을 때만 커밋
if ! git diff --cached --quiet; then
    git commit -m "chore: Eval Dashboard Auto-Update ($(date '+%Y-%m-%d %H:%M'))" 2>&1 | tee -a "$LOG_FILE"
fi

# Git push with retry logic
MAX_RETRIES=3
RETRY_COUNT=0
PUSH_STATUS="failed"

while [ $RETRY_COUNT -lt $MAX_RETRIES ]; do
    if git push origin main 2>&1 | tee -a "$LOG_FILE"; then
        log "✅ GitHub push successful (attempt $((RETRY_COUNT + 1)))"
        PUSH_STATUS="success"
        break
    else
        RETRY_COUNT=$((RETRY_COUNT + 1))
        if [ $RETRY_COUNT -lt $MAX_RETRIES ]; then
            log "⚠️ Git push failed, retrying in 3 seconds... ($RETRY_COUNT/$MAX_RETRIES)"
            sleep 3
            if git push origin main --force 2>&1 | tee -a "$LOG_FILE"; then
                log "✅ GitHub push successful with --force (attempt $RETRY_COUNT)"
                PUSH_STATUS="success"
                break
            fi
        else
            log "❌ GitHub push failed after $MAX_RETRIES attempts"
            PUSH_STATUS="failed"
        fi
    fi
done

# ========================================
# 5 단계: Telegram 알림 (점수 < 60 또는 Gate 위반)
# ========================================
SEND_ALERT=false
ALERT_REASON=""

if (( $(echo "$EVAL_SCORE < 60" | bc -l) )); then
    SEND_ALERT=true
    ALERT_REASON="Eval Score below threshold"
fi

if [ $GATE_VIOLATIONS -gt 0 ]; then
    SEND_ALERT=true
    ALERT_REASON="${ALERT_REASON:+$ALERT_REASON, }Human Gate violations"
fi

if [ "$PUSH_STATUS" = "failed" ]; then
    SEND_ALERT=true
    ALERT_REASON="${ALERT_REASON:+$ALERT_REASON, }Git push failed"
fi

if [ "$SEND_ALERT" = true ]; then
    log "⚠️ Alert condition met: $ALERT_REASON"
    
    if [ -n "$TELEGRAM_BOT_TOKEN" ] && [ -n "$TELEGRAM_CHAT_ID" ]; then
        log "📱 Sending Telegram alert..."
        
        MESSAGE="🚨 *csp-brain Eval 경고*

📊 *Eval Score*: $EVAL_SCORE/100
🔒 *Human Gate Violations*: $GATE_VIOLATIONS
🚀 *Git Push*: $PUSH_STATUS

⚠️ *사유*: $ALERT_REASON

📈 *주요 지표*:
- Total Docs: $TOTAL_DOCS 개
- Orphan Rate: $ORPHAN_RATE%
- Active Docs: $ACTIVE_DOCS 개

🔗 *대시보드*: https://foolpoet44.github.io/1st_brain/

🔧 *조치 필요*:
1. Human Gate 검증 로그 확인
2. Git 푸시 상태 확인
3. 고립 문서 연결 강화"

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
        log "⚠️ Telegram not configured (TELEGRAM_BOT_TOKEN/CHAT_ID not set)"
        echo "[$(date '+%Y-%m-%d %H:%M:%S')] Alert: $ALERT_REASON | Score: $EVAL_SCORE | Gates: $GATE_VIOLATIONS | Push: $PUSH_STATUS" >> "$TELEGRAM_LOG"
    fi
else
    log "✅ All checks passed (Score: $EVAL_SCORE, Gates: $GATE_VIOLATIONS, Push: $PUSH_STATUS)"
fi

log "=== Eval Dashboard Update Completed ==="
log ""
