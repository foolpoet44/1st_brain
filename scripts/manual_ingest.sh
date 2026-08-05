#!/bin/bash
# 수동 INGEST 프로토콜 - inbox/ → wiki/signals/ 이동

INGEST_DIR="/Users/dkmac/Desktop/@26/dev/inbox"
TARGET_DIR="/Users/dkmac/Desktop/@26/dev/wiki/signals"

echo "📂 INGEST 시작: $INGEST_DIR → $TARGET_DIR"

# 파일 수 카운트
FILE_COUNT=$(ls -1 "$INGEST_DIR"/*.md 2>/dev/null | wc -l | tr -d ' ')
echo "📄 처리 대상: $FILE_COUNT 개 파일"

if [ "$FILE_COUNT" -eq 0 ]; then
    echo "✅ 처리할 파일 없음"
    exit 0
fi

# 파일 이동
for file in "$INGEST_DIR"/*.md; do
    if [ -f "$file" ]; then
        filename=$(basename "$file")
        mv "$file" "$TARGET_DIR/$filename"
        echo "  → $filename"
    fi
done

echo "✅ INGEST 완료: $FILE_COUNT 개 파일 이동"

# Git 커밋
cd /Users/dkmac/Desktop/@26/dev
git add -A
git commit -m "ingest: inbox/ → wiki/signals/ ($FILE_COUNT files)"
echo "✅ Git 커밋 완료"
