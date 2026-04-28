#!/bin/bash

# CSP-Brain Wiki Status
# 위키 전체 현황을 통계로 보여줍니다.

echo "=== CSP-Brain Wiki Status ==="
echo ""

# 문서 수 카운트
echo "📊 문서 현황"
echo "------------"
echo "wiki/concepts:      $(find wiki/concepts -name '*.md' | wc -l | xargs) 개"
echo "wiki/frameworks:    $(find wiki/frameworks -name '*.md' | wc -l | xargs) 개"
echo "wiki/tools:         $(find wiki/tools -name '*.md' | wc -l | xargs) 개"
echo "wiki/projects:      $(find wiki/projects -name '*.md' | wc -l | xargs) 개"
echo "wiki/decisions:     $(find wiki/decisions -name '*.md' | wc -l | xargs) 개"
echo "wiki/signals:       $(find wiki/signals -name '*.md' | wc -l | xargs) 개"
echo ""

TOTAL=$(find wiki -name '*.md' | wc -l | xargs)
echo "총 wiki 문서:       $TOTAL 개"
echo ""

# 성장 단계 판단
if [ "$TOTAL" -lt 5 ]; then
    echo "🌱 성장 단계: 씨앗 (5 개 미만)"
elif [ "$TOTAL" -lt 15 ]; then
    echo "🌱 성장 단계: 씨앗 (5~15 개)"
elif [ "$TOTAL" -lt 40 ]; then
    echo "🌿 성장 단계: 새싹 (15~40 개)"
elif [ "$TOTAL" -lt 80 ]; then
    echo "🌳 성장 단계: 성장 (40~80 개)"
else
    echo "🌲 성장 단계: 숲 (80 개 이상)"
fi

echo ""
echo "📁 기타 현황"
echo "------------"
echo "inbox/:           $(find inbox -name '*.md' | wc -l | xargs) 개"
echo "projects/:        $(find projects -name '*.md' | wc -l | xargs) 개"
echo "outputs/:         $(find outputs -name '*.md' | wc -l | xargs) 개"
echo ""

# 고립 문서 찾기 (백링크 0 개)
echo "⚠️  고립 문서 (백링크 0 개)"
echo "-------------------------"
for file in $(find wiki -name '*.md' -type f); do
    # 파일 내용에서 [[링크]] 개수 카운트
    link_count=$(grep -o '\[\[[^]]*\]\]' "$file" 2>/dev/null | wc -l)
    if [ "$link_count" -eq 0 ]; then
        # _index.md 는 제외
        if [[ ! "$file" =~ _index\.md$ ]]; then
            echo "  - $file"
        fi
    fi
done

echo ""
echo "=== End of Status ==="
