import os
import sys
import json
import re
from datetime import datetime

# Root path configuration
ROOT = "/Users/dkmac/Desktop/@26/dev"

def read_md_content(rel_path):
    full_path = os.path.join(ROOT, rel_path)
    if not os.path.exists(full_path):
        return None
    with open(full_path, 'r', encoding='utf-8') as f:
        content = f.read()
        # Remove frontmatter for cleaner analysis
        content = re.sub(r'---.*?---', '', content, flags=re.DOTALL)
        return content.strip()

def generate_synapse_note(file1, file2, connection_insight):
    """
    두 지식의 연결고리를 실제 wiki/concepts/ 에 새로운 문서로 생성합니다.
    """
    name1 = os.path.basename(file1).replace(".md", "")
    name2 = os.path.basename(file2).replace(".md", "")

    # 새로운 문서 제목 생성 (예: synapse-concept1-concept2)
    synapse_title = f"synapse-{name1}-{name2}"
    target_path = os.path.join(ROOT, "wiki/concepts", f"{synapse_title}.md")

    today = datetime.now().strftime("%Y-%m-%d")

    frontmatter = f"""---
title: "Synapse: {name1} × {name2}"
created: {today}
updated: {today}
type: concept
status: seed
tags: ["synapse", "insight", "cross-domain"]
aliases: ["{name1}-{name2}-bridge"]
---

# [SYNAPSE] {name1} 와 {name2} 의 교차점

## Compiled Truth

{connection_insight}

---

## Timeline

### {today}
- [[{name1}]] 와 [[{name2}]] 의 데이터 충돌을 통해 생성된 자동화 통찰.
"""
    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(frontmatter)

    return target_path

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 generate_synapse.py <rel_path1> <rel_path2>")
        sys.exit(1)

    f1 = sys.argv[1]
    f2 = sys.argv[2]

    c1 = read_md_content(f1)
    c2 = read_md_content(f2)

    if not c1 or not c2:
        print("Error: Could not read one of the files.")
        sys.exit(1)

    # 이 부분은 실제로 에이전트(Claude)가 이 스크립트의 출력을 보고
    # 통찰 내용을 생성하여 다시 이 스크립트를 호출하거나 노트를 직접 쓰게 됩니다.
    print(f"--- CONTENT 1: {f1} ---")
    print(c1[:500] + "...")
    print(f"\n--- CONTENT 2: {f2} ---")
    print(c2[:500] + "...")
