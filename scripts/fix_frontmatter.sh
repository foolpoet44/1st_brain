#!/bin/bash
#
# Auto-fix Markdown files missing YAML frontmatter
#

VAULT_DIR="/Users/dkmac/Desktop/@26/dev"
FIXED_COUNT=0

echo "🔧 Fixing Markdown files without frontmatter..."
echo ""

while IFS= read -r -d '' file; do
    # Skip node_modules, .git, etc.
    if [[ "$file" == *"/node_modules/"* ]] || [[ "$file" == *"/.git/"* ]] || [[ "$file" == *"/Understand-Anything/"* ]]; then
        continue
    fi
    
    first_line=$(head -1 "$file" 2>/dev/null | tr -d '\r\n')
    
    if [ "$first_line" != "---" ]; then
        # Backup
        cp "$file" "${file}.bak"
        
        # Get content
        content=$(cat "$file")
        
        # Determine type from path
        if [[ "$file" == *"/outputs/daily-reflect/"* ]]; then
            type="Reflection"
        elif [[ "$file" == *"/outputs/"* ]]; then
            type="Note"
        elif [[ "$file" == *"/inbox/"* ]]; then
            type="Note"
        elif [[ "$file" == *"/wiki/"* ]]; then
            type="Note"
        else
            type="Note"
        fi
        
        # Write fixed content
        cat > "$file" << EOF
---
type: $type
status: Active
---

EOF
        echo "$content" >> "$file"
        
        # Remove backup
        rm "${file}.bak"
        
        echo "✅ Fixed: $file (type: $type)"
        FIXED_COUNT=$((FIXED_COUNT + 1))
    fi
done < <(find "$VAULT_DIR" -name "*.md" -type f -print0)

echo ""
echo "================================"
echo "Fixed $FIXED_COUNT files"
echo ""

if [ $FIXED_COUNT -gt 0 ]; then
    echo "Committing changes..."
    cd "$VAULT_DIR"
    git add -A
    git commit -m "fix: Add frontmatter to $FIXED_COUNT files (auto-fixed)"
    echo "✅ Done! Push to GitHub if needed."
fi
