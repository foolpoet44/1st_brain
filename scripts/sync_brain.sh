#!/bin/bash
# 이식성: 하드코딩된 로컬 경로(/Users/dkmac/...) 대신 스크립트 위치에서 레포 루트를 유도.
# 과거 하드코딩 경로는 머신 종속이었고, 부모 디렉토리에 sibling vault가 있으면
# `git add .`가 이를 통째로 빨아들이는 사고(2026-06-22 중복 스냅샷)의 단초였다.
#
# v2 (2026-08-04): 단일 [AUTOSYNC] 커밋 → CLAUDE.md 5절 커밋 분리 규칙에 따른 분류 커밋.
#   이 스크립트는 daily-knowledge-sync(매일 23:00)가 부르는 Vault 의 유일한 자동 커밋기다.
#   커밋 주체를 하나로 좁힌 대신, 그 하나가 의미별로 나눠 커밋할 책임을 진다.
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
VAULT_PATH="$( cd "$SCRIPT_DIR/.." && pwd )"
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
git add -A

# --- 안전장치: .gitmodules에 없는 우발적 gitlink(중첩 git 저장소) 언스테이징 ---
# tmp_deploy 같은 임시/중첩 저장소가 gitlink로 흡수되면 GitHub Pages 빌더가
# 'No url found ... exit code 128'로 죽는다. 선언되지 않은 gitlink는 커밋 전에 제거.
git ls-files --stage | awk '$1 == "160000" {print $4}' | while IFS= read -r gl; do
    if ! grep -qF "path = $gl" .gitmodules 2>/dev/null; then
        echo "⚠️  우발적 gitlink 제거(언스테이징): $gl"
        git rm --cached "$gl" >/dev/null 2>&1 || true
    fi
done

# gitlink 정리 결과를 반영한 뒤 스테이징을 풀고, 의미 그룹별로 다시 담는다.
git reset -q

# CLAUDE.md 5절 접두어: knowledge / project / ops / content / archive
# 대형 자동 산출물(manifest.json, data.json)은 지식 변경과 반드시 분리한다.
commit_group() {
    local prefix="$1"; shift
    local label="$1"; shift
    local paths=()
    for p in "$@"; do [ -e "$p" ] && paths+=("$p"); done
    [ ${#paths[@]} -eq 0 ] && return 0

    git add -- "${paths[@]}" 2>/dev/null
    git diff --cached --quiet && return 0

    local n
    n=$(git diff --cached --name-only | wc -l | tr -d ' ')
    git commit -q -m "${prefix}: ${label} (${TIMESTAMP}) — ${n}개 파일" \
        && echo "  ✓ ${prefix}: ${n}개"
}

echo "Committing by category..."
commit_group knowledge "위키 지식"     wiki/
commit_group project   "프로젝트"       projects/
commit_group ops       "운영 체계"      scripts/ _ops/ templates/ .claude/ CLAUDE.md AGENTS.md SOUL.md
commit_group content   "산출물"         outputs/ sharing/
commit_group archive   "원자료·인덱스"  raw/ inbox/ manifest.json data.json index.html knowledge.html

# 분류되지 않은 잔여는 chore 로 남긴다. 조용히 섞이면 분류 누락을 영영 모른다.
git add -A
if ! git diff --cached --quiet; then
    LEFT=$(git diff --cached --name-only | wc -l | tr -d ' ')
    git commit -q -m "chore: 미분류 변경 (${TIMESTAMP}) — ${LEFT}개 파일"
    echo "  ⚠️  미분류 ${LEFT}개 — 경로 그룹 재검토 필요"
fi

git pull --rebase origin main && git push origin main
echo "Knowledge evolution synced to GitHub at $TIMESTAMP"
