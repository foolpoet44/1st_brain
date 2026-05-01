# Conversation Archive

## 구조

```
raw/archive/
├── conversations/    ← 원본 JSON 파일 (483 개, 114MB)
├── md/               ← 변환된 Markdown 파일 (483 개)
│   ├── 2024/         ← 2024 년 대화
│   ├── 2025/         ← 2025 년 대화
│   └── 2026/         ← 2026 년 대화
└── CONVERSATION_MAP.md ← JSON 파일 인덱스
```

## 변환 정보

- **변환일**: 2026-04-29
- **도구**: `scripts/parse_conversations.py`
- **포맷**: JSON → Markdown (frontmatter 포함)

## Markdown 문서 구조

각 Markdown 파일은 다음 구조를 가집니다:

```yaml
---
title: [대화 제목]
date: YYYY-MM-DD
time: HH:MM
uuid: [고유 ID]
type: conversation
tags: [archive, conversation]
---

# [대화 제목]

**날짜**: YYYY-MM-DD HH:MM

---

## Human (Message 1)
[내용]

## Claude (Message 2)
[내용]

---

*Archived from: [원본 JSON 파일명]*
```

## 활용 방법

### 특정 날짜의 대화 검색

```bash
# 2026 년 4 월 대화 검색
find raw/archive/md/2026/04 -name "*.md" -exec grep "검색어" {} \;
```

### 특정 UUID 의 대화 읽기

```bash
# CONVERSATION_MAP.md 에서 UUID 확인 후
cat raw/archive/md/[연도]/[월]/[UUID].md
```

---

_원본 데이터: `D:\obsi\sync\raw\archive\conversations\`_
