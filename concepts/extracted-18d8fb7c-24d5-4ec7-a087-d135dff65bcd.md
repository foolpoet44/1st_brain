# Extracted Knowledge from Conv: 18d8fb7c-24d5-4ec7-a087-d135dff65bcd

**Date**: 2026-01-01T10:06:52.803715Z

### Extracted Code (javascript)

```javascript
// ❌ 잘못된 예시
messages: [
  { role: "user", content: "안녕" },
  { role: "assistant", content: "안녕하세요" },
  { 
    role: "user", 
    content: [
      { type: "tool_result", tool_use_id: "toolu_xxx", content: "..." }
    ]
  }  // ← tool_use 없이 tool_result만 있음!
]

// ✅ 올바른 예시
messages: [
  { role: "user", content: "안녕" },
  { 
    role: "assistant", 
    content: [
      { type: "text", text: "검색하겠습니다" },
      { type: "tool_use", id: "toolu_xxx", name: "web_search", input: {...} }
    ]
  },
  { 
    role: "user", 
    content: [
      { type: "tool_result", tool_use_id: "toolu_xxx", content: "..." }
    ]
  }
]
```

### Extracted Code (javascript)

```javascript
// 문제가 있는 메시지를 제거하고 새로 시작
const cleanMessages = messages.filter((msg, index) => {
  // 34번 메시지 근처를 확인하고 문제 있는 부분 제거
  return index < 33; // 문제 발생 전까지만 유지
});
```

### Extracted Code (javascript)

```javascript
function validateMessages(messages) {
  const toolUseIds = new Set();
  
  for (let i = 0; i < messages.length; i++) {
    const msg = messages[i];
    
    if (msg.role === "assistant") {
      // tool_use 수집
      const toolUses = msg.content.filter(c => c.type === "tool_use");
      toolUses.forEach(tu => toolUseIds.add(tu.id));
    }
    
    if (msg.role === "user") {
      // tool_result 검증
      const toolResults = msg.content.filter(c => c.type === "tool_result");
      toolResults.forEach(tr => {
        if (!toolUseIds.has(tr.tool_use_id)) {
          console.error(`Orphan tool_result: ${tr.tool_use_id} at message ${i}`);
        }
      });
    }
  }
}
```

### Extracted Code (javascript)

```javascript
// 현재 대화를 포기하고 새로 시작
const response = await fetch("https://api.anthropic.com/v1/messages", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    model: "claude-sonnet-4-20250514",
    max_tokens: 1000,
    messages: [
      { 
        role: "user", 
        content: "새로운 대화 시작" 
      }
    ]
  })
});
```
