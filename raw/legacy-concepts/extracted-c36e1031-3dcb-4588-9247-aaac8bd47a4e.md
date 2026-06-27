# Extracted Knowledge from Conv: c36e1031-3dcb-4588-9247-aaac8bd47a4e

**Date**: 2026-04-05T01:51:29.269455Z

### Extracted Code (json)

```json
// ~/.claude/settings.json
{
  "model": "claude-sonnet-4-6",
  "availableModels": ["claude-sonnet-4-6", "haiku"],
  "env": {
    "ANTHROPIC_DEFAULT_SONNET_MODEL": "claude-sonnet-4-6",
    "ANTHROPIC_DEFAULT_HAIKU_MODEL": "claude-haiku-4-5-20251001"
  }
}
```

### Extracted Code (bash)

```bash
OPENROUTER_API_KEY="sk-or-..."

# 평소 사용
MODEL_SONNET="open_router/openai/gpt-oss-120b:free"

# 한도 초과 시 Fallback
MODEL_HAIKU="open_router/stepfun/step-3.5-flash:free"
MODEL="open_router/stepfun/step-3.5-flash:free"  # 최종 Fallback
```
