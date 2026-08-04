#!/bin/bash
# CSP-Brain Automated Git Sync Script
# Improved for portability across environments
#
# v2 (2026-08-04): 단일 "Auto-Sync" 커밋 → CLAUDE.md 커밋 분리 규칙에 따른 분류 커밋으로 전환.
#   변경 이유: Git 은 백업 수단이 아니라 '변화 이해 장치'다. 지식 변경과 대량 자동 산출물이
#   한 커밋에 뭉치면, 나중에 "무엇이 왜 바뀌었나"를 되짚을 수 없다. 규칙을 CLAUDE.md 문서에만
#   두면 사람만 읽고 커밋의 대다수를 만드는 자동화는 읽지 않으므로, 규칙을 스크립트에 각인한다.

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

# 스테이징을 일단 해제하고, 아래에서 의미 그룹별로 다시 담는다.
# (gitlink 정리 결과는 인덱스에 남아 있어야 하므로 순서가 중요하다)
git reset -q

TIMESTAMP=$(date '+%Y-%m-%d %H:%M')

# --- 분류 커밋 ---
# CLAUDE.md 5절의 접두어 규칙을 그대로 옮긴다.
#   knowledge: 지식 내용 / project: 프로젝트 상태 / ops: 운영 체계
#   content: 외부 공유물 / archive: 대량 원자료
# 대형 자동 산출물(manifest.json, data.json 등)은 반드시 지식 변경과 분리한다.
commit_group() {
    local prefix="$1"; shift
    local label="$1"; shift
    local paths=()
    for p in "$@"; do [ -e "$p" ] && paths+=("$p"); done
    [ ${#paths[@]} -eq 0 ] && return 0

    git add -- "${paths[@]}" 2>/dev/null
    if git diff --cached --quiet; then
        return 0
    fi
    local n
    n=$(git diff --cached --name-only | wc -l | tr -d ' ')
    git commit -q -m "${prefix}: ${label} 자동 동기화 (${TIMESTAMP}) — ${n}개 파일" \
        && echo "  ✓ ${prefix}: ${n}개 파일"
}

echo "Committing by category..."
commit_group knowledge "위키 지식"     wiki/
commit_group project   "프로젝트"       projects/
commit_group ops       "운영 체계"      scripts/ _ops/ templates/ .claude/ CLAUDE.md AGENTS.md SOUL.md
commit_group content   "산출물"         outputs/ sharing/
commit_group archive   "원자료·인덱스"  raw/ inbox/ manifest.json data.json index.html knowledge.html

# 위 그룹에 속하지 않은 잔여 변경 — 분류되지 않았음을 드러내기 위해 별도 커밋으로 남긴다.
git add -A
if ! git diff --cached --quiet; then
    LEFT=$(git diff --cached --name-only | wc -l | tr -d ' ')
    git commit -q -m "chore: 미분류 변경 (${TIMESTAMP}) — ${LEFT}개 파일"
    echo "  ⚠️  미분류 ${LEFT}개 — 경로 그룹 재검토 필요"
fi

echo "Pulling latest changes..."
git pull --rebase -Xtheirs origin main || echo "Pull failed, attempting to continue..."

# 3. Push to origin
echo "Pushing to origin..."
git push origin main || echo "Push failed."
