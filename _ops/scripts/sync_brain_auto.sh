#!/bin/bash
# CSP-Brain Automated Git Sync Script
# Improved for portability across environments

# Get the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
# Assuming the script is in [REPO_ROOT]/_ops/scripts/
REPO_ROOT="$( cd "$SCRIPT_DIR/../../" && pwd )"

cd "$REPO_ROOT" || exit 1

echo "Syncing brain at $REPO_ROOT..."

# 1. Update pulse data and dashboard
echo "Running knowledge monitor..."
python3 "$REPO_ROOT/scripts/know_grow_monitor.py" || echo "Knowledge monitor failed."

echo "Updating dashboard..."
python3 "$REPO_ROOT/_ops/scripts/update_dashboard.py" || echo "Dashboard update failed."

# 2. Git operations
echo "Adding changes..."
git add .

# --- 안전장치: .gitmodules에 없는 우발적 gitlink(중첩 git 저장소) 언스테이징 ---
# tmp_deploy 같은 임시/중첩 저장소가 gitlink로 흡수되면 GitHub Pages 빌더가
# 'No url found ... exit code 128'로 죽는다. 선언되지 않은 gitlink는 커밋 전에 제거.
git ls-files --stage | awk '$1 == "160000" {print $4}' | while IFS= read -r gl; do
    if ! grep -qF "path = $gl" .gitmodules 2>/dev/null; then
        echo "⚠️  우발적 gitlink 제거(언스테이징): $gl"
        git rm --cached "$gl" >/dev/null 2>&1 || true
    fi
done

TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
echo "Committing changes..."
git commit -m "Auto-Sync: $TIMESTAMP [Evolution Insight]" || echo "Nothing to commit"

echo "Pulling latest changes..."
git pull --rebase -Xtheirs origin main || echo "Pull failed, attempting to continue..."

# 3. Push to origin
echo "Pushing to origin..."
git push origin main || echo "Push failed."
