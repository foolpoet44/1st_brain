#!/bin/bash
VAULT_PATH="/Users/dkmac/Desktop/@26/dev"
MONITOR_SCRIPT="$VAULT_PATH/scripts/know_grow_monitor.py"
cd "$VAULT_PATH" || exit
if [ -f "$MONITOR_SCRIPT" ]; then
    python3 "$MONITOR_SCRIPT"
fi
if [[ -z $(git status -s) ]]; then
    echo "No changes to sync."
    exit 0
fi
TIMESTAMP=$(date +"%Y-%m-%d %H:%M")
git add .
git commit -m "[AUTOSYNC] Knowledge Metabolism Pulse: $TIMESTAMP"
git push origin main
echo "Knowledge evolution synced to GitHub at $TIMESTAMP"
