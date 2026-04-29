# Extracted Knowledge from Conv: d696de87-58ac-4ec2-91a0-5a63fc4eeddc

**Date**: 2026-03-24T00:33:00.577154Z

### Extracted Code (python)

```python
from markitdown import MarkItDown

md = MarkItDown(enable_plugins=False)
result = md.convert("report.pptx")
print(result.text_content)
```

### Extracted Code (python)

```python
from markitdown import MarkItDown
from openai import OpenAI

client = OpenAI()
md = MarkItDown(llm_client=client, llm_model="gpt-4o")
result = md.convert("slide_with_images.pptx")
```

### Extracted Code (bash)

```bash
# 1. 가상환경 생성 (프로젝트 폴더 안에서)
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
# .venv\Scripts\activate    # Windows

# 2. MarkItDown 설치 (전체 기능 포함)
pip install 'markitdown[all]'

# 3. 즉시 사용
markitdown 파일명.pdf > 결과.md
markitdown 파일명.pptx -o 결과.md
```

### Extracted Code (json)

```json
{
  "mcpServers": {
    "markitdown": {
      "command": "/절대경로/.venv/bin/python",
      "args": ["-m", "markitdown_mcp"]
    }
  }
}
```
