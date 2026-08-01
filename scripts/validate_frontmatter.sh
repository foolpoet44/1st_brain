#!/bin/bash
#
# Validate all Markdown files have proper YAML frontmatter
#

VAULT_DIR="/Users/dkmac/Desktop/@26/dev"
INVALID_FILES=()

echo "🔍 Scanning for Markdown files without frontmatter..."
echo ""

while IFS= read -r -d '' file; do
    # Skip node_modules, .git, etc.
    if [[ "$file" == *"/node_modules/"* ]] || [[ "$file" == *"/.git/"* ]] || [[ "$file" == *"/Understand-Anything/"* ]]; then
        continue
    fi
    
    first_line=$(head -1 "$file" 2>/dev/null | tr -d '\r\n')
    
    if [ "$first_line" != "---" ]; then
        INVALID_FILES+=("$file")
        echo "❌ $file (first line: '$first_line')"
    fi
done < <(find "$VAULT_DIR" -name "*.md" -type f -print0)

echo ""
echo "================================"
if [ ${#INVALID_FILES[@]} -eq 0 ]; then
    echo "✅ All Markdown files have valid frontmatter!"
    exit 0
else
    echo "❌ Found ${#INVALID_FILES[@]} files without frontmatter"
    echo ""
    echo "To fix automatically, run:"
    echo "  scripts/fix_frontmatter.sh"
    exit 1
fi
