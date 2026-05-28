#!/bin/bash
# CSP-Brain Dashboard Publisher
cd /Users/dkmac/Desktop/@26/dev

# Update Data
python3 /Users/dkmac/Desktop/@26/dev/_ops/scripts/update_dashboard.py

# Git sync
git add .gitignore _ops/web/index.html _ops/web/data.json KNOWLEDGE_PULSE.md _ops/scripts/update_dashboard.py _ops/scripts/publish_dashboard.sh
git commit -m "Dashboard Pulse: $(date '+%Y-%m-%d %H:%M:%S') [Automated]"
# Try pushing, but don't fail the whole script if it's an auth issue
git push origin main || echo "Git push failed. Please check your GitHub authentication (run 'gh auth login' or setup SSH keys)."
