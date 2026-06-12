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

# --- 안전장치: .gitmodules에 없는 우발적 gitlink(중첩 git 저장소) 언스테이징 ---
# tmp_deploy 같은 임시/중첩 저장소가 gitlink로 흡수되면 GitHub Pages 빌더가
# 'No url found ... exit code 128'로 죽는다. 선언되지 않은 gitlink는 커밋 전에 제거.
git ls-files --stage | awk '$1 == "160000" {print $4}' | while IFS= read -r gl; do
    if ! grep -qF "path = $gl" .gitmodules 2>/dev/null; then
        echo "⚠️  우발적 gitlink 제거(언스테이징): $gl"
        git rm --cached "$gl" >/dev/null 2>&1 || true
    fi
done

git commit -m "[AUTOSYNC] Knowledge Metabolism Pulse: $TIMESTAMP"
git pull --rebase origin main && git push origin main
echo "Knowledge evolution synced to GitHub at $TIMESTAMP"
