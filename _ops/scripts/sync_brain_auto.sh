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

TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
echo "Committing changes..."
git commit -m "Auto-Sync: $TIMESTAMP [Evolution Insight]" || echo "Nothing to commit"

echo "Pulling latest changes..."
git pull --rebase -Xtheirs origin main || echo "Pull failed, attempting to continue..."

# 3. Push to origin
echo "Pushing to origin..."
git push origin main || echo "Push failed."
