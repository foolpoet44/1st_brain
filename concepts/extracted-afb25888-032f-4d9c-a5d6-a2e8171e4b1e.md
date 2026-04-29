# Extracted Knowledge from Conv: afb25888-032f-4d9c-a5d6-a2e8171e4b1e

**Date**: 2025-10-22T00:56:13.105147Z

### Extracted Code (html)

```html
<!-- Step 1: CSS 변수로 디자인 시스템 정의 -->
<style>
:root {
  --primary-color: #2E86AB;
  --text-color: #333333;
  --heading-font: 'Arial', sans-serif;
  --body-font: 'Helvetica', sans-serif;
}
</style>

<!-- Step 2: HTML로 슬라이드 구조 작성 -->
<body style="width: 960px; height: 540px;">
  <div class="row">
    <div class="col">
      <h1>분기별 매출 현황</h1>
      <p>2025년 3분기 실적 보고</p>
    </div>
  </div>
  <div class="placeholder">
    <!-- 차트가 들어갈 자리 -->
  </div>
</body>
```

### Extracted Code (javascript)

```javascript
// Step 3: JavaScript로 PowerPoint 생성
const pptxgen = require("pptxgenjs");
const { html2pptx } = require("@ant/html2pptx");

const pptx = new pptxgen();
pptx.layout = "LAYOUT_16x9";

// HTML 슬라이드를 PowerPoint로 변환
const { slide, placeholders } = await html2pptx("slide1.html", pptx);

// placeholder에 차트 추가
slide.addChart(pptx.charts.BAR, [
  { name: "Q1", labels: ["매출"], values: [120] },
  { name: "Q2", labels: ["매출"], values: [150] },
], placeholders[0]);

await pptx.writeFile("output.pptx");
```

### Extracted Code (bash)

```bash
# Step 1: 압축 해제
python ooxml/scripts/unpack.py presentation.pptx unpacked/

# Step 2: 파일 구조 확인
unpacked/
├── ppt/
│   ├── slides/
│   │   ├── slide1.xml      # 첫 번째 슬라이드
│   │   ├── slide2.xml      # 두 번째 슬라이드
│   ├── notesSlides/
│   │   └── notesSlide1.xml # 발표자 노트
│   └── presentation.xml     # 메타데이터
```

### Extracted Code (bash)

```bash
# Step 3: 편집 후 즉시 검증 (매우 중요!)
python ooxml/scripts/validate.py unpacked/ --original presentation.pptx

# Step 4: 다시 압축
python ooxml/scripts/pack.py unpacked/ new_presentation.pptx
```

### Extracted Code (bash)

```bash
# 텍스트 추출
python -m markitdown template.pptx > template-content.md

# 시각적 썸네일 생성
python scripts/thumbnail.py template.pptx
```

### Extracted Code (markdown)

```markdown
# Template Inventory Analysis

**Total Slides: 10**
**슬라이드는 0부터 시작 (첫 슬라이드 = 0)**

## 인트로 슬라이드
- Slide 0: Title Slide - 메인 제목, 부제목, 로고
- Slide 1: Section Divider - 섹션 구분용

## 콘텐츠 슬라이드  
- Slide 2: Two Column - 왼쪽 텍스트, 오른쪽 이미지
- Slide 3: Bullet Points - 제목 + 3개 불릿
- Slide 4: Chart Layout - 차트용 레이아웃
```

### Extracted Code (json)

```json
{
  "slide-0": {
    "shape-0": {
      "type": "TEXT_BOX",
      "text": "기존 제목",
      "default_font_size": 44.0,
      "placeholder_type": "TITLE"
    },
    "shape-1": {
      "type": "TEXT_BOX", 
      "text": "부제목",
      "default_font_size": 24.0
    }
  }
}
```

### Extracted Code (json)

```json
{
  "slide-0": {
    "shape-0": {
      "paragraphs": [
        {
          "text": "2025년 사업 계획",
          "alignment": "CENTER",
          "bold": true
        }
      ]
    },
    "shape-1": {
      "paragraphs": [
        {
          "text": "혁신과 성장을 위한 로드맵"
        }
      ]
    }
  },
  "slide-1": {
    "shape-0": {
      "paragraphs": [
        {
          "text": "주요 목표",
          "bold": true
        },
        {
          "text": "매출 30% 증가",
          "bullet": true,
          "level": 0
        },
        {
          "text": "신규 시장 진출",
          "bullet": true,
          "level": 0
        }
      ]
    }
  }
}
```

### Extracted Code (javascript)

```javascript
const chartData = [
  {
    name: "실제",
    labels: ["1월", "2월", "3월"],
    values: [10, 20, 15]
  },
  {
    name: "목표",
    labels: ["1월", "2월", "3월"],
    values: [12, 18, 20]
  }
];

slide.addChart(pptx.charts.LINE, chartData, {
  x: 1, y: 2, w: 8, h: 4
});
```

### Extracted Code (html)

```html
<!-- HTML 방식 -->
<div style="background-image: url('chart.png'); 
            width: 500px; height: 300px;">
</div>
```
