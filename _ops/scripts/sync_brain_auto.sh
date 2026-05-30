#!/bin/bash
# CSP-Brain Automated Git Sync Script
# Runs every 2 hours via cron

cd /Users/dkmac/Desktop/@26/dev

# 1. Update pulse data and dashboard
python3 /Users/dkmac/Desktop/@26/dev/scripts/know_grow_monitor.py
python3 /Users/dkmac/Desktop/@26/dev/_ops/scripts/update_dashboard.py

# 2. Git operations
git add .
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
git commit -m "Auto-Sync: $TIMESTAMP [Evolution Insight]"

# 3. Push to origin
# We use '|| echo' to prevent script failure if there are no changes to commit or network issues
git push origin main || echo "Sync completed (no changes or push suppressed)."
