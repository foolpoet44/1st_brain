# Extracted Knowledge from Conv: 30d8aa9a-d2c8-4f2a-9638-4f9241e09a3b

**Date**: 2026-03-24T10:16:48.574295Z

### Extracted Code (text)

```text
사용자 입력 (Intent)
      ↓
[ Dispatcher ]  ← 여기가 핵심
      ↓
┌─────────────────────────────┐
│  PulseCheck Agent           │
│  ESCON Agent                │
│  LeadershipEval Agent       │
│  GeneralQA Agent            │
└─────────────────────────────┘
```

### Extracted Code (python)

```python
# 각 Agent는 자기 책임 범위만 처리
class PulseCheckAgent:
    def handle(self, payload): ...

class ESCONAgent:
    def handle(self, payload): ...

# Dispatcher: 판단과 라우팅만 담당
class Dispatcher:
    def __init__(self):
        self.routes = {
            "pulse_check": PulseCheckAgent(),
            "escon":       ESCONAgent(),
        }

    def dispatch(self, intent: str, payload: dict):
        agent = self.routes.get(intent)
        if not agent:
            raise ValueError(f"No agent for intent: {intent}")
        return agent.handle(payload)

# 실행
dispatcher = Dispatcher()
result = dispatcher.dispatch("pulse_check", {"team": "EXG", "period": "2026-Q1"})
```

### Extracted Code (markdown)

```markdown
# CLAUDE.md (Orchestrator 역할)

## Dispatch Rules
- 사용자 요청에 "설문", "참여율", "Well-Being" 포함 → pulse_check_agent 호출
- 사용자 요청에 "스킬", "ESCO", "역량" 포함 → escon_agent 호출
- 사용자 요청에 "평가", "리더십", "360" 포함 → leadership_agent 호출
```
