#!/bin/bash
# 이식성: 하드코딩된 로컬 경로(/Users/dkmac/...) 대신 스크립트 위치에서 레포 루트를 유도.
# 과거 하드코딩 경로는 머신 종속이었고, 부모 디렉토리에 sibling vault가 있으면
# `git add .`가 이를 통째로 빨아들이는 사고(2026-06-22 중복 스냅샷)의 단초였다.
#
# v2 (2026-08-04): 단일 [AUTOSYNC] 커밋 → CLAUDE.md 5절 커밋 분리 규칙에 따른 분류 커밋.
#   이 스크립트는 daily-knowledge-sync(매일 23:00)가 부르는 Vault 의 유일한 자동 커밋기다.
#   커밋 주체를 하나로 좁힌 대신, 그 하나가 의미별로 나눠 커밋할 책임을 진다.
#
# v3 (2026-10-08): 「완료」를 보고할 자격을 push 검증 뒤로 옮겼다.
#   09-23~09-30 사이 두 가지 경로로 지식이 GitHub 에 도착하지 못했다.
#   (a) 에이전트가 이 스크립트 대신 다른 폴더(~/.hermes/csp-brain, remote 없음)에서 커밋하고 「완료」를 보고했다.
#   (b) 작업 트리가 깨끗하면 "No changes" 로 끝나, 수동 커밋 6개가 push 되지 않은 채 쌓였다.
#   그래서 이제 ① 시작 시 이 저장소가 1st_brain 의 정본인지 확인하고, ② 트리가 깨끗해도 밀린 커밋은 push 하며,
#   ③ 마지막 줄에 SYNC_OK <해시> 또는 SYNC_FAILED <사유> 중 하나만 출력한다. 호출자는 이 줄만 믿는다.
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
VAULT_PATH="$( cd "$SCRIPT_DIR/.." && pwd )"
MONITOR_SCRIPT="$VAULT_PATH/scripts/know_grow_monitor.py"
cd "$VAULT_PATH" || { echo "SYNC_FAILED cannot-cd $VAULT_PATH"; exit 2; }

fail() { echo "SYNC_FAILED $*"; exit 2; }

# ① 정체 확인: remote 가 없거나 다른 저장소면 커밋 전에 멈춘다(사본 저장소 사고 재발 방지).
ORIGIN_URL=$(git remote get-url origin 2>/dev/null)
case "$ORIGIN_URL" in
    *foolpoet44/1st_brain*) ;;
    *) fail "wrong-repo path=$VAULT_PATH origin='${ORIGIN_URL:-none}'" ;;
esac
if [ -d .git/rebase-merge ] || [ -d .git/rebase-apply ]; then
    fail "rebase-in-progress — 사람이 먼저 정리해야 함"
fi
echo "SYNC_VAULT $VAULT_PATH ($ORIGIN_URL)"

if [ -f "$MONITOR_SCRIPT" ]; then
    python3 "$MONITOR_SCRIPT"
fi
TIMESTAMP=$(date +"%Y-%m-%d %H:%M")

# ② 트리가 깨끗해도 바로 끝내지 않는다 — 밀린 커밋이 있으면 아래 push 단계로 간다.
if [[ -z $(git status -s) ]]; then
    echo "No working-tree changes; checking for unpushed commits."
else
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
fi  # 작업 트리 변경이 있을 때만 커밋 단계 실행

# ③ 원격과 합치고 올린 뒤, 원격이 실제로 우리 HEAD 를 가졌는지 확인한다.
git fetch -q origin main || fail "fetch-failed"
AHEAD=$(git rev-list --count origin/main..HEAD)
if [ "$AHEAD" -eq 0 ]; then
    echo "SYNC_OK $(git rev-parse --short HEAD) nothing-to-push"
    exit 0
fi
echo "Unpushed commits: $AHEAD"
if ! git pull -q --rebase origin main; then
    git rebase --abort >/dev/null 2>&1
    fail "rebase-conflict — 로컬 커밋 ${AHEAD}개 보존됨, 수동 병합 필요"
fi
git push -q origin main || fail "push-rejected"
git fetch -q origin main || fail "verify-fetch-failed"
LOCAL=$(git rev-parse HEAD); REMOTE=$(git rev-parse origin/main)
[ "$LOCAL" = "$REMOTE" ] || fail "verify-mismatch local=${LOCAL:0:7} remote=${REMOTE:0:7}"
echo "Knowledge evolution synced to GitHub at $TIMESTAMP"
echo "SYNC_OK ${LOCAL:0:7} pushed=$AHEAD"
