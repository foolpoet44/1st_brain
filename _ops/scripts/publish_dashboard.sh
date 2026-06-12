#!/bin/bash
# CSP-Brain Dashboard Publisher
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VAULT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
cd "$VAULT_ROOT"

# Update Data
python3 "$VAULT_ROOT/_ops/scripts/update_dashboard.py"

# Git sync
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

git commit -m "Dashboard Pulse: $(date '+%Y-%m-%d %H:%M:%S') [Automated]" || echo "No changes to commit"

# Stash remaining unstaged changes temporarily to avoid pull conflicts
git stash

# Pull first to prevent merge rejection
git pull --rebase origin main

# Restore stashed changes
git stash pop || echo "No stashed changes to restore"

# Try pushing, but don't fail the whole script if it's an auth issue
git push origin main || echo "Git push failed. Please check your GitHub authentication (run 'gh auth login' or setup SSH keys)."
