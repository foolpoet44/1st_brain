# Extracted Knowledge from Conv: 9f266d95-5c0c-4cfc-b1cc-6b03e7763fbe

**Date**: 2026-03-29T00:23:41.214105Z

### Extracted Code (text)

```text
[1] Intent Capture
    → Guide Mode 방식의 단계별 인터뷰 프롬프트
    → 청중 / 목적 / 데이터 소스 / 슬라이드 수 수집

[2] Research & Structure Agent  
    → Claude web_search로 필요한 데이터 수집
    → JSON 형태의 슬라이드 아웃라인 생성
    → 각 슬라이드: {title, key_points[], speaker_notes, chart_data}

[3] PPTX Rendering Agent
    → python-pptx로 기존 LG CHO 브랜드 템플릿에 콘텐츠 삽입
    → 차트 데이터는 python-pptx + matplotlib로 자동 생성
    → 기존 pptx 스킬 활용

[4] QA & Export
    → 팩트체크: 주요 클레임에 대한 웹 검색 검증
    → .pptx + .pdf 동시 내보내기
    → Notion 아카이빙 연동
```

### Extracted Code (text)

```text
# Slide Agent — Intent Capture

당신은 LG PRI EXG팀의 슬라이드 생성 에이전트입니다.
사용자의 요청을 받으면 다음을 순서대로 확인하세요:

1. 청중: 임원진 / 팀장급 / 실무팀 / 외부
2. 목적: 보고 / 공유 / 설득 / 교육
3. 핵심 메시지: 이 슬라이드로 청중이 무엇을 결정/느끼길 원하는가
4. 데이터 소스: 첨부 파일 / 수동 입력 / 웹 리서치 필요 여부
5. 슬라이드 수 및 구성 방식

확인 후 JSON 형태의 슬라이드 아웃라인을 생성하세요.
```

### Extracted Code (json)

```json
{
  "meta": {
    "title": "2026 Q1 Pulse Check 결과 보고",
    "audience": "임원진",
    "purpose": "보고",
    "slide_count": 8,
    "template": "lg_cho_master_v1.pptx"
  },
  "slides": [
    {
      "id": 1,
      "type": "title",
      "title": "2026 Q1 조직 건강도 진단 결과",
      "subtitle": "EX Intelligence Pulse Check",
      "speaker_notes": "..."
    },
    {
      "id": 2,
      "type": "data_chart",
      "title": "전사 Well-Being 지수 추이",
      "chart": {
        "type": "line",
        "data": {"Q4-25": 72, "Q1-26": 78},
        "highlight": "6pt 상승"
      },
      "key_message": "목표 대비 85% 달성",
      "speaker_notes": "..."
    }
  ]
}
```

### Extracted Code (text)

```text
hr-workspace/
└── slide-agent/
    ├── CLAUDE.md              # 에이전트 지시서
    ├── templates/
    │   └── lg_cho_master.pptx # 마스터 템플릿
    ├── src/
    │   ├── renderer.py        # 핵심 렌더링 엔진
    │   ├── chart_gen.py       # 차트 생성 모듈
    │   └── qa_agent.py        # 품질 검증
    ├── inputs/
    │   └── outline.json       # claude.ai에서 전달받은 JSON
    └── outputs/
        ├── *.pptx
        └── *.pdf
```

### Extracted Code (markdown)

```markdown
# Slide Agent — CLAUDE.md

## 역할
JSON outline을 받아 LG CHO 브랜드 .pptx 파일을 생성한다.

## 실행 순서
1. inputs/outline.json 읽기
2. renderer.py로 슬라이드 타입별 생성
3. chart_gen.py로 데이터 시각화 삽입
4. qa_agent.py로 레이아웃 검증
5. outputs/에 .pptx + .pdf 저장

## 브랜드 규칙
- Primary Red: #A50034
- Font: Malgun Gothic (제목), Arial (본문)
- 템플릿: templates/lg_cho_master.pptx의 슬라이드 레이아웃 인덱스를 반드시 유지

## 절대 하지 말 것
- 템플릿의 폰트/색상 임의 변경 금지
- 슬라이드 레이아웃 구조 임의 변경 금지
```

### Extracted Code (python)

```python
from pptx import Presentation
from pptx.util import Inches, Pt
import json

SLIDE_TYPE_MAP = {
    "title": render_title_slide,
    "data_chart": render_chart_slide,
    "text_only": render_text_slide,
    "comparison": render_comparison_slide,
    "framework": render_framework_slide,
}

def generate_presentation(outline_path: str):
    with open(outline_path) as f:
        outline = json.load(f)
    
    prs = Presentation("templates/lg_cho_master.pptx")
    
    for slide_data in outline["slides"]:
        render_fn = SLIDE_TYPE_MAP.get(slide_data["type"])
        if render_fn:
            render_fn(prs, slide_data)
    
    output_path = f"outputs/{outline['meta']['title']}.pptx"
    prs.save(output_path)
    return output_path
```
