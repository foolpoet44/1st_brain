#!/bin/bash
# csp-brain Type 문서 자동 분류 스크립트
# 사용법: ./auto-classify-types.sh [limit]

VAULT_PATH="/Users/dkmac/Desktop/@26/dev"
LIMIT=${1:-100}

echo "🔍 csp-brain Vault 스캔 시작..."
echo "   경로: $VAULT_PATH"
echo "   배치 제한: $LIMIT 개 문서"
echo ""

# type 이 없는 문서 목록 추출
echo "📋 미분류 문서 검색 중..."
UNCLASSIFIED=$(find "$VAULT_PATH" -name "*.md" -type f ! -path "*/node_modules/*" ! -path "*/.git/*" ! -path "*/Type/*" -exec grep -L "^type:" {} \; | head -$LIMIT)

COUNT=$(echo "$UNCLASSIFIED" | grep -c "\.md" || echo 0)
echo "   발견된 미분류 문서: $COUNT 개"
echo ""

# 분류 함수
classify_file() {
    local file="$1"
    local content=$(head -50 "$file")
    local h1=$(grep "^# " "$file" | head -1 | tr '[:upper:]' '[:lower:]')
    
    # 분류 규칙
    if echo "$h1 $content" | grep -qiE "meeting|sync|standup|retro|agenda"; then
        echo "Meeting"
    elif echo "$h1 $content" | grep -qiE "reflect|retro|learning|insight|lesson|grow"; then
        echo "Reflection"
    elif echo "$h1 $content" | grep -qiE "project|initiative|roadmap|milestone|onboarding"; then
        echo "Project"
    elif echo "$h1 $content" | grep -qiE "person|profile|이정민|tony|lee"; then
        echo "Person"
    elif echo "$h1 $content" | grep -qiE "concept|model|framework|theory|principle|pattern"; then
        echo "Concept"
    elif echo "$h1 $content" | grep -qiE "url|link|resource|reference|article|doc"; then
        echo "Resource"
    elif echo "$h1 $content" | grep -qiE "task|action|todo|checklist|assign"; then
        echo "Task"
    elif echo "$h1 $content" | grep -qiE "idea|brainstorm|feature|opportunity|improve"; then
        echo "Idea"
    elif echo "$h1 $content" | grep -qiE "decision|decide|choice|select"; then
        echo "Decision"
    else
        echo "Note"
    fi
}

# 분류 진행
echo "📊 분류 진행:"
CLASSIFIED=0
for file in $UNCLASSIFIED; do
    if [ -f "$file" ]; then
        type=$(classify_file "$file")
        
        # frontmatter 에 type 추가
        if grep -q "^---" "$file"; then
            # frontmatter 가 있는 경우
            sed -i.bak "3i\\
type: $type
" "$file" && rm -f "${file}.bak"
        else
            # frontmatter 가 없는 경우
            echo "---
type: $type
---
$(cat "$file")" > "$file"
        fi
        
        echo "   ✅ $(basename "$file") → $type"
        CLASSIFIED=$((CLASSIFIED + 1))
    fi
done

echo ""
echo "🎯 분류 완료: $CLASSIFIED 개 문서"
echo ""

# 결과 요약
echo "📈 현재 상태:"
echo "   총 Type 문서: $(find "$VAULT_PATH/Type" -name '*.md' -type f | wc -l | tr -d ' ')"
echo "   type 할당됨: $(find "$VAULT_PATH" -name '*.md' -type f ! -path '*/node_modules/*' -exec grep -l '^type:' {} \; | wc -l | tr -d ' ')"
echo "   미분류: $(find "$VAULT_PATH" -name '*.md' -type f ! -path '*/node_modules/*' -exec grep -L '^type:' {} \; | wc -l | tr -d ' ')"
