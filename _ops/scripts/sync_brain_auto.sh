#!/bin/bash
# CSP-Brain Automated Git Sync Script
# Runs every 2 hours via cron

cd /Users/dkmac/Desktop/@26/dev

# 2. Git operations
git pull --rebase origin main || echo "Pull failed, attempting to continue..."

# 1. Update pulse data and dashboard
python3 /Users/dkmac/Desktop/@26/dev/scripts/know_grow_monitor.py
python3 /Users/dkmac/Desktop/@26/dev/_ops/scripts/update_dashboard.py

git add .
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
git commit -m "Auto-Sync: $TIMESTAMP [Evolution Insight]" || echo "Nothing to commit"

# 3. Push to origin
git push origin main || echo "Push failed."
