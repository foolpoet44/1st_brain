# Extracted Knowledge from Conv: 2a2d8f0e-d1bb-478c-9091-a153e0b77a72

**Date**: 2025-12-24T19:54:58.572131Z

### Extracted Code (text)

```text
Claude 대화 
  ↓
Notion 페이지 자동 생성 (notion-knowledge-capture 스킬)
  ↓
Notion API → Obsidian 동기화
  ↓
Obsidian Vault (세컨 브레인)
```

### Extracted Code (text)

```text
📁 Obsidian Vault/
├── 📁 Claude Conversations/
│   ├── 📁 2024-12/
│   │   └── 2024-12-25_옵시디언_세컨브레인_구축.md
│   └── 📁 Topics/
│       ├── 개발.md
│       └── 지식관리.md
├── 📁 MOC (Map of Content)/
│   └── Claude_대화_인덱스.md
└── 📁 Templates/
    └── conversation_template.md
```

### Extracted Code (markdown)

```markdown
---
date: {{date}}
tags: [claude, conversation, {{topic}}]
aliases: []
---

# {{title}}

## 메타데이터
- 날짜: {{date}}
- 주제: {{topic}}
- 키워드: {{keywords}}

## 대화 요약
{{summary}}

## 주요 내용
{{main_content}}

## 관련 링크
- [[관련노트1]]
- [[관련노트2]]

## 다음 액션
- [ ] 항목1
- [ ] 항목2
```

### Extracted Code (text)

```text
1. Notion API Key 입력
2. Database ID 입력 (Notion URL의 일부)
3. Sync Folder 지정: "Claude Conversations/"
4. Auto-sync 활성화: 매 1시간
5. Bidirectional sync 설정 (선택)
```

### Extracted Code (python)

```python
# notion_to_obsidian_sync.py

from notion_client import Client
import os
from datetime import datetime

# 설정
NOTION_TOKEN = "your_token_here"
OBSIDIAN_VAULT = "/Users/yourname/Obsidian Vault"
DATABASE_ID = "your_database_id"

# Notion에서 페이지 가져오기
notion = Client(auth=NOTION_TOKEN)

# 마크다운으로 변환
# Obsidian에 저장
# 자동 태그 및 링크 생성
```
