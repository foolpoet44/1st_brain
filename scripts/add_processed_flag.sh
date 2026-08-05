#!/bin/bash
# outputs/briefings/ 파일들에 processed: true 추가

BRIEFINGS_DIR="outputs/briefings"

echo "📝 processed: true 추가 시작..."

for file in "$BRIEFINGS_DIR"/*.md; do
    if [ -f "$file" ]; then
        if ! grep -q "processed: true" "$file" 2>/dev/null; then
            # frontmatter 에 processed: true 추가
            if head -1 "$file" | grep -q "^---$"; then
                # frontmatter 있음 - 세 번째 줄에 추가
                sed -i '' '4i\
processed: true\
processed_date: '\"$(date +%Y-%m-%d)'
' "$file"
                echo "  ✅ $file"
            else
                # frontmatter 없음 - 추가
                content=$(cat "$file")
                cat > "$file" << EOF
---
type: Briefing
status: Processed
processed: true
processed_date: $(date +%Y-%m-%d)
---

EOF
                echo "$content" >> "$file"
                echo "  ✅ $file (frontmatter added)"
            fi
        fi
    fi
done

echo "✅ 완료"
