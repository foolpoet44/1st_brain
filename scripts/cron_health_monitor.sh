#!/bin/bash
# Cron Job Health Monitor for csp-brain
# Checks all cron jobs and alerts on failures

HERMES_HOME="$HOME/.hermes"
CRON_OUTPUT="$HERMES_HOME/cron/output"
LOG_FILE="$HERMES_HOME/cron/health-monitor.log"
MAX_AGE_HOURS=25

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

check_job_health() {
    local job_id="$1"
    local job_name="$2"
    local job_dir="$CRON_OUTPUT/$job_id"
    
    if [ ! -d "$job_dir" ]; then
        log "${RED}[FAIL]${NC} $job_name: Directory not found"
        return 1
    fi
    
    local latest_file=$(ls -t "$job_dir"/*.md 2>/dev/null | head -1)
    
    if [ -z "$latest_file" ]; then
        log "${RED}[FAIL]${NC} $job_name: No output files"
        return 1
    fi
    
    if grep -q "## Error" "$latest_file" 2>/dev/null; then
        log "${RED}[ERROR]${NC} $job_name: $(basename "$latest_file")"
        return 1
    fi
    
    if grep -q "\[SILENT\]" "$latest_file" 2>/dev/null; then
        log "${YELLOW}[SILENT]${NC} $job_name: No new content"
        return 0
    fi
    
    local file_age_hours=$(( ($(date +%s) - $(stat -f %m "$latest_file")) / 3600 ))
    
    if [ $file_age_hours -gt $MAX_AGE_HOURS ]; then
        log "${RED}[STALE]${NC} $job_name: Last run ${file_age_hours}h ago"
        return 1
    fi
    
    log "${GREEN}[OK]${NC} $job_name: $(basename "$latest_file") (${file_age_hours}h ago)"
    return 0
}

log "=========================================="
log "Cron Job Health Check"
log "=========================================="

failed=0
ok=0

# Job list (job_id|job_name)
jobs=(
    "b4525e1a3b93|Evening Reflect"
    "e4534f91ef78|Daily Knowledge Sync"
    "284cd7db0eae|Knowledge Metabolism"
    "9d956add06c2|Financial Flow"
    "dab74102bfb9|HR Tech Insight"
    "fc334c4eab75|Psychology Paper"
    "da9391461b1b|Auto Sync"
)

for job_entry in "${jobs[@]}"; do
    job_id="${job_entry%%|*}"
    job_name="${job_entry##*|}"
    if check_job_health "$job_id" "$job_name"; then
        ((ok++))
    else
        ((failed++))
    fi
done

log "=========================================="
log "Summary: OK=$ok | Failed=$failed"
log "=========================================="

if [ $failed -gt 0 ]; then
    log "🚨 $failed job(s) need attention!"
    exit 1
fi

log "✅ All jobs healthy."
exit 0
