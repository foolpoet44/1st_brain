#!/bin/bash

# CSP-Brain Change Status
# 오늘 확인해야 할 변화와 위키 현황을 함께 보여줍니다.

set -u

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT_DIR" || exit 1

count_md() {
    local dir="$1"
    if [ -d "$dir" ]; then
        find "$dir" -name '*.md' -type f | wc -l | xargs
    else
        echo "0"
    fi
}

latest_file() {
    local dir="$1"
    if [ -d "$dir" ]; then
        find "$dir" -name '*.md' -type f -print0 \
            | xargs -0 ls -t 2>/dev/null \
            | head -n 1
    fi
}

echo "=== CSP-Brain Change Briefing ==="
echo ""

echo "1. 지금 주의할 변화"
echo "-------------------"
git_status="$(git status --short 2>/dev/null || true)"
if [ -n "$git_status" ]; then
    echo "$git_status" | sed -n '1,10p'
else
    echo "작업트리 변경 없음"
fi
echo ""

echo "2. 최근 커밋"
echo "------------"
git log --oneline -5 2>/dev/null || echo "Git 기록 없음"
echo ""

echo "3. 최근 수정된 핵심 문서"
echo "-----------------------"
for dir in _ops wiki projects outputs weekly templates scripts; do
    file="$(latest_file "$dir")"
    if [ -n "${file:-}" ]; then
        printf "%-10s %s\n" "$dir" "$file"
    fi
done
echo ""

echo "4. 운영 로그 상태"
echo "----------------"
for log in _ops/change-log.md _ops/ingest-log.md _ops/lint-log.md _ops/question-log.md _ops/bridge-log.md; do
    if [ ! -f "$log" ]; then
        printf "%-24s 없음\n" "$log"
        continue
    fi

    body_lines="$(sed '1,/^---$/d' "$log" | sed '/^[[:space:]]*$/d' | wc -l | xargs)"
    if [ "$body_lines" -le 2 ]; then
        printf "%-24s 비어 있음\n" "$log"
    else
        printf "%-24s 기록 있음\n" "$log"
    fi
done
echo ""

echo "5. 주간 다이제스트 상태"
echo "----------------------"
latest_weekly="$(latest_file outputs/weekly)"
if [ -n "${latest_weekly:-}" ]; then
    echo "최신 outputs/weekly: $latest_weekly"
else
    echo "outputs/weekly에 다이제스트 없음"
fi

latest_legacy_weekly="$(latest_file weekly)"
if [ -n "${latest_legacy_weekly:-}" ]; then
    echo "최신 weekly:         $latest_legacy_weekly"
fi
echo ""

echo "6. 문서 현황"
echo "-----------"
echo "wiki/concepts:      $(count_md wiki/concepts) 개"
echo "wiki/frameworks:    $(count_md wiki/frameworks) 개"
echo "wiki/tools:         $(count_md wiki/tools) 개"
echo "wiki/projects:      $(count_md wiki/projects) 개"
echo "wiki/decisions:     $(count_md wiki/decisions) 개"
echo "wiki/signals:       $(count_md wiki/signals) 개"
echo "총 wiki 문서:       $(count_md wiki) 개"
echo "inbox/:             $(count_md inbox) 개"
echo "projects/:          $(count_md projects) 개"
echo "outputs/:           $(count_md outputs) 개"
echo ""

echo "7. 고립 문서 후보"
echo "----------------"
found_orphan=0
while IFS= read -r file; do
    link_count="$(grep -o '\[\[[^]]*\]\]' "$file" 2>/dev/null | wc -l | xargs)"
    if [ "$link_count" -eq 0 ] && [[ ! "$file" =~ _index\.md$ ]]; then
        echo "  - $file"
        found_orphan=1
    fi
done < <(find wiki -name '*.md' -type f 2>/dev/null)

if [ "$found_orphan" -eq 0 ]; then
    echo "  없음"
fi
echo ""

echo "=== End of Briefing ==="
