# Extracted Knowledge from Conv: 0d093a12-c224-4beb-bdbe-6d638aed9380

**Date**: 2026-01-30T05:51:58.568048Z

### Extracted Code (python)

```python
# 이 접근은 PPT의 모든 핵심 요소를 포착합니다
{
  "layout": {
    "shapes": [
      {
        "left": 100,    # 정확한 위치
        "top": 200,
        "width": 300,
        "height": 150,
        "type": "textbox",
        "content": "제조 AX 아카데미"
      }
    ]
  },
  "theme": {
    "colors": {
      "accent1": "#4472C4",
      "background": "#FFFFFF"
    }
  }
}
```

### Extracted Code (python)

```python
# ❌ 현재: 물리적 속성만
{
  "shape": {
    "left": 100,
    "top": 200,
    "text": "제조 AX 아카데미"
  }
}

# ✅ 개선: 의미론적 + 물리적
{
  "shape": {
    # 의미론적 정보
    "semantic_role": "heading",  # h1, h2, section, card
    "content_type": "title",
    "hierarchy_level": 1,
    
    # 디자인 의도
    "design_intent": "hero_title",  # CTA, caption, body
    
    # 물리적 속성
    "position": {"left": 100, "top": 200},
    "text": "제조 AX 아카데미"
  }
}
```

### Extracted Code (python)

```python
# ❌ 현재: 개별 shape만
[
  {"shape_id": 1, "left": 100, "text": "타이틀"},
  {"shape_id": 2, "left": 100, "text": "부제"}
]

# ✅ 개선: 관계성 포함
{
  "groups": [
    {
      "type": "title_block",
      "members": [1, 2],  # shape_id
      "relationship": "parent_child",
      "visual_grouping": "vertical_stack"
    }
  ]
}
```

### Extracted Code (python)

```python
# ❌ 절대 좌표만
{"left": 1200, "top": 300}  # 1920px 기준

# ✅ 상대 좌표 + 절대 좌표
{
  "absolute": {"left": 1200, "top": 300},
  "relative": {
    "horizontal": "right",  # left, center, right
    "vertical": "top",      # top, middle, bottom
    "offset_percent": {"x": 62.5, "y": 15.6}  # 슬라이드 크기 대비
  }
}
```

### Extracted Code (python)

```python
# ✅ Z-index 및 시각적 우선순위
{
  "visual_hierarchy": {
    "z_index": 10,
    "visual_weight": "primary",  # primary, secondary, accent
    "attention_score": 0.95  # 0-1, 폰트 크기/색상/위치 기반
  }
}
```

### Extracted Code (json)

```json
{
  "metadata": {
    "slide_size": {"width": 1920, "height": 1080},
    "theme": {
      "colors": {
        "primary": "#4472C4",
        "accent": "#E67E22",
        "background": "#FFFFFF"
      },
      "fonts": {
        "heading": "Noto Sans KR",
        "body": "Noto Sans KR"
      }
    }
  },
  
  "slides": [
    {
      "slide_id": 1,
      "layout_type": "title_slide",  // 레이아웃 템플릿 힌트
      
      "elements": [
        {
          "id": "elem_1",
          
          // 의미론적 정보
          "semantic": {
            "role": "heading",
            "level": 1,
            "content_type": "title"
          },
          
          // 디자인 의도
          "design": {
            "intent": "hero_title",
            "visual_weight": "primary"
          },
          
          // 물리적 속성
          "geometry": {
            "absolute": {"left": 100, "top": 200, "width": 800, "height": 100},
            "relative": {"h_align": "left", "v_align": "top"}
          },
          
          // 스타일
          "style": {
            "font": {"family": "Noto Sans KR", "size": 44, "weight": "bold"},
            "color": {"text": "#2C3E50", "background": null},
            "effects": {"shadow": true}
          },
          
          // 콘텐츠
          "content": {
            "text": "제조 AX 아카데미",
            "text_runs": [  // 부분 스타일링
              {"text": "제조 AX", "color": "#4472C4"}
            ]
          }
        }
      ],
      
      // 그룹 관계
      "groups": [
        {
          "type": "card",
          "members": ["elem_2", "elem_3"],
          "layout": "vertical_stack"
        }
      ]
    }
  ]
}
```

### Extracted Code (python)

```python
from pptx import Presentation
import json

def parse_ppt_basic(ppt_path):
    prs = Presentation(ppt_path)
    data = {
        "slides": []
    }
    
    for slide in prs.slides:
        slide_data = {
            "shapes": []
        }
        
        for shape in slide.shapes:
            shape_data = {
                "left": shape.left,
                "top": shape.top,
                "width": shape.width,
                "height": shape.height,
                "type": shape.shape_type.name
            }
            
            if hasattr(shape, "text"):
                shape_data["text"] = shape.text
                
            slide_data["shapes"].append(shape_data)
            
        data["slides"].append(slide_data)
    
    return data
```

### Extracted Code (python)

```python
def enrich_semantics(basic_data):
    """물리적 속성에서 의미 추론"""
    
    for slide in basic_data["slides"]:
        for shape in slide["shapes"]:
            # 크기·위치 기반 역할 추론
            if shape["width"] > slide_width * 0.6:
                shape["semantic_role"] = "heading"
            
            # 색상 기반 시각적 계층
            if is_theme_color(shape["color"]):
                shape["visual_weight"] = "primary"
            
            # 텍스트 분석
            if len(shape["text"]) < 50:
                shape["content_type"] = "title"
            else:
                shape["content_type"] = "body"
    
    return basic_data
```

### Extracted Code (python)

```python
def detect_groups(enriched_data):
    """공간적 근접성으로 그룹 탐지"""
    
    for slide in enriched_data["slides"]:
        shapes = slide["shapes"]
        
        # 수직 정렬된 텍스트 → 리스트
        vertical_groups = find_vertical_alignment(shapes)
        for group in vertical_groups:
            slide["groups"].append({
                "type": "list",
                "members": [s["id"] for s in group]
            })
        
        # 이미지 + 캡션 → figure
        image_text_pairs = find_adjacent_pairs(shapes, "image", "text")
        for pair in image_text_pairs:
            slide["groups"].append({
                "type": "figure",
                "members": pair
            })
    
    return enriched_data
```

### Extracted Code (html)

```html
<!-- 절대 위치로 PPT 복제 -->
<div style="position: absolute; left: 100px; top: 200px;">
  제조 AX 아카데미
</div>
```

### Extracted Code (json)

```json
{
  "output_modes": {
    "faithful": {
      // pixel-perfect, 절대 좌표 기반
      "use_case": "프레젠테이션 PDF 대체"
    },
    "semantic": {
      // HTML 시맨틱 구조
      "use_case": "웹사이트 랜딩페이지"
    },
    "responsive": {
      // 반응형 + 원본 디자인 유지
      "use_case": "현대적 웹 문서"
    }
  }
}
```

### Extracted Code (python)

```python
# 기존 JSON에 추가
shape["semantic_role"] = infer_role(shape)
shape["design_intent"] = infer_intent(shape)
```

### Extracted Code (text)

```text
"이 JSON은 PPT 슬라이드입니다.
- 각 요소의 semantic_role을 참고하여 적절한 HTML 태그로 변환하세요
- groups 정보를 활용해 section/article 구조를 만드세요
- 절대 좌표는 CSS Grid/Flexbox로 재현하세요"
```

### Extracted Code (markdown)

```markdown
# 나쁜 프롬프트
"이 JSON을 HTML로 변환해줘"

# 좋은 프롬프트
"이 JSON은 PPT 슬라이드의 구조화된 데이터입니다.
1. semantic_role을 기반으로 적절한 HTML5 태그 선택
2. design_intent에 따라 CSS 클래스 부여
3. groups의 type에 따라 section/article/figure 구조 생성
4. 절대 좌표는 CSS Grid의 grid-template-areas로 변환

목표: 시맨틱하고 반응형인 HTML 생성"
```

### Extracted Code (json)

```json
{
  "metadata": {
    "source_file": "presentation.pptx",
    "parsed_at": "2025-01-30T12:00:00Z",
    "slide_dimensions": {
      "width": 1920,
      "height": 1080,
      "unit": "emu"
    },
    "theme": {
      "name": "Office Theme",
      "colors": {
        "primary": "#4472C4",
        "accent1": "#ED7D31",
        "accent2": "#A5A5A5",
        "background": "#FFFFFF",
        "text_dark": "#000000",
        "text_light": "#FFFFFF"
      },
      "fonts": {
        "heading": {
          "latin": "Calibri Light",
          "east_asian": "맑은 고딕"
        },
        "body": {
          "latin": "Calibri",
          "east_asian": "맑은 고딕"
        }
      }
    }
  },
  
  "slides": [
    {
      "slide_number": 1,
      "layout_name": "Title Slide",
      "layout_pattern": "hero_centered",
      "background": {
        "type": "solid",
        "color": "#FFFFFF"
      },
      
      "elements": [],
      "groups": [],
      "layout_analysis": {}
    }
  ]
}
```

### Extracted Code (json)

```json
{
  "id": "elem_1_1",
  "type": "text_box",
  
  // === LAYER 1: Physical Properties ===
  "geometry": {
    "absolute": {
      "left": 914400,
      "top": 365760,
      "width": 6096000,
      "height": 1524000,
      "unit": "emu"
    },
    "relative": {
      "h_align": "center",
      "v_align": "top",
      "offset_percent": {
        "x": 50.0,
        "y": 20.0
      }
    },
    "z_index": 1
  },
  
  "style": {
    "font": {
      "family": "Noto Sans KR",
      "size": 4400,
      "weight": "bold",
      "italic": false,
      "underline": false,
      "color": "#2C3E50"
    },
    "fill": {
      "type": "solid",
      "color": null,
      "transparency": 0
    },
    "border": {
      "width": 0,
      "color": null,
      "style": "none"
    },
    "effects": {
      "shadow": {
        "enabled": true,
        "blur": 4,
        "angle": 45,
        "distance": 2,
        "color": "#00000040"
      },
      "reflection": false,
      "glow": false
    }
  },
  
  // === LAYER 2: Semantic Properties ===
  "semantic": {
    "role": "heading",
    "level": 1,
    "content_type": "title",
    "html_tag_suggestion": "h1"
  },
  
  "design": {
    "intent": "hero_title",
    "visual_weight": "primary",
    "attention_score": 0.95,
    "purpose": "main_message"
  },
  
  // === Content ===
  "content": {
    "raw_text": "제조 AX 아카데미",
    "text_runs": [
      {
        "text": "제조 ",
        "style_override": null
      },
      {
        "text": "AX",
        "style_override": {
          "color": "#E67E22",
          "weight": "bold"
        }
      },
      {
        "text": " 아카데미",
        "style_override": null
      }
    ],
    "has_hyperlink": false,
    "language": "ko"
  },
  
  // === LAYER 3: Relationships ===
  "relationships": {
    "parent_group": "group_1",
    "visual_proximity": {
      "nearest_above": null,
      "nearest_below": "elem_1_2",
      "distance_to_below": 50000
    }
  }
}
```

### Extracted Code (python)

```python
# 의사코드
def determine_semantic_role(element):
    """
    요소의 물리적 속성을 분석하여 의미론적 역할 결정
    """
    
    # 1. 크기 기반 판단
    if element.width > slide_width * 0.6:
        if element.font_size > 3600:  # 40pt 이상
            return "heading", 1
        elif element.font_size > 2800:  # 32pt 이상
            return "heading", 2
    
    # 2. 위치 기반 판단
    if element.top < slide_height * 0.2:
        if element.h_align == "center":
            return "heading", 1
    
    # 3. 색상 기반 판단
    if is_accent_color(element.color):
        return "emphasis", None
    
    # 4. 텍스트 길이 기반
    if len(element.text) < 50:
        return "label", None
    elif len(element.text) < 200:
        return "paragraph", None
    else:
        return "body_text", None
    
    # 5. 기본값
    return "text", None
```

### Extracted Code (python)

```python
def determine_design_intent(element, position_in_slide):
    """
    시각적 배치와 스타일로 디자인 의도 파악
    """
    
    intents = []
    
    # 1. 포지셔닝 기반
    if position_in_slide == "hero_area":  # 슬라이드 상단 1/3
        intents.append("hero_title")
    elif position_in_slide == "footer":
        intents.append("metadata")
    
    # 2. 스타일 기반
    if element.has_shadow or element.has_glow:
        intents.append("attention_grabber")
    
    if element.background_color is not None:
        intents.append("callout")
    
    # 3. 크기 기반
    if element.width > slide_width * 0.8:
        intents.append("full_width_banner")
    
    # 4. 색상 기반
    if element.color == theme.accent_color:
        intents.append("brand_emphasis")
    
    return intents[0] if intents else "neutral"
```

### Extracted Code (json)

```json
{
  "groups": [
    {
      "id": "group_1",
      "type": "vertical_stack",
      "members": ["elem_1_1", "elem_1_2"],
      "layout": {
        "direction": "vertical",
        "spacing": 20000,
        "alignment": "left"
      },
      "html_structure_suggestion": {
        "container": "div",
        "layout_method": "flex-column"
      }
    },
    {
      "id": "group_2",
      "type": "figure_with_caption",
      "members": ["elem_2_1", "elem_2_2"],
      "roles": {
        "elem_2_1": "image",
        "elem_2_2": "caption"
      },
      "html_structure_suggestion": {
        "container": "figure",
        "children": ["img", "figcaption"]
      }
    },
    {
      "id": "group_3",
      "type": "card_grid",
      "members": ["elem_3_1", "elem_3_2", "elem_3_3"],
      "layout": {
        "pattern": "3-column",
        "gap": 30000
      },
      "html_structure_suggestion": {
        "container": "section",
        "layout_method": "css-grid",
        "grid_template": "1fr 1fr 1fr"
      }
    }
  ]
}
```

### Extracted Code (python)

```python
def detect_vertical_stack(elements):
    """
    수직으로 정렬된 요소들을 탐지
    """
    aligned_groups = []
    
    for i, elem in enumerate(elements):
        for j, other in enumerate(elements[i+1:]):
            # 수평 위치가 유사한가?
            if abs(elem.left - other.left) < THRESHOLD:
                # 수직으로 인접한가?
                if abs(elem.bottom - other.top) < GAP_THRESHOLD:
                    aligned_groups.append([elem, other])
    
    return merge_chains(aligned_groups)
```

### Extracted Code (python)

```python
def detect_list_pattern(elements):
    """
    불릿/번호 리스트 패턴 탐지
    """
    list_candidates = []
    
    for elem in elements:
        # 불릿 심볼 체크
        if elem.text.startswith(('•', '-', '▪', '○')):
            list_candidates.append(elem)
        
        # 번호 패턴 체크
        if re.match(r'^\d+\.', elem.text):
            list_candidates.append(elem)
    
    # 수직 정렬 확인
    if is_vertically_aligned(list_candidates):
        return {
            "type": "bullet_list" if has_bullets else "ordered_list",
            "members": list_candidates
        }
```

### Extracted Code (python)

```python
def detect_figure_caption(elements):
    """
    이미지와 캡션 쌍 탐지
    """
    figures = []
    
    for elem in elements:
        if elem.type == "picture":
            # 하단에 텍스트가 있는가?
            caption = find_text_below(elem, threshold=50000)
            
            if caption and len(caption.text) < 100:
                figures.append({
                    "type": "figure_with_caption",
                    "image": elem.id,
                    "caption": caption.id
                })
    
    return figures
```

### Extracted Code (python)

```python
def detect_card_grid(elements):
    """
    카드 레이아웃 (박스 + 아이콘 + 텍스트) 탐지
    """
    # 배경이 있는 shape들 찾기
    boxes = [e for e in elements if e.has_background]
    
    if len(boxes) >= 2:
        # 수평 정렬 확인
        if is_horizontally_aligned(boxes):
            # 간격이 균일한가?
            if has_uniform_spacing(boxes):
                return {
                    "type": "card_grid",
                    "members": boxes,
                    "columns": len(boxes)
                }
```

### Extracted Code (json)

```json
{
  "layout_analysis": {
    "pattern": "hero_centered",
    "regions": {
      "hero": {
        "bounds": {"top": 0, "height": "33%"},
        "elements": ["elem_1_1"]
      },
      "main": {
        "bounds": {"top": "33%", "height": "60%"},
        "elements": ["group_1", "group_2"]
      },
      "footer": {
        "bounds": {"top": "93%", "height": "7%"},
        "elements": ["elem_5_1"]
      }
    },
    "grid": {
      "detected": true,
      "columns": 3,
      "rows": 2,
      "gutter": 30000
    }
  }
}
```

### Extracted Code (python)

```python
def calculate_attention_score(element):
    """
    시각적 주목도 점수 (0-1)
    """
    score = 0.0
    
    # 1. 크기 (30%)
    size_ratio = (element.width * element.height) / (slide_width * slide_height)
    score += min(size_ratio * 3, 0.3)
    
    # 2. 위치 (20%)
    if element.v_align == "top":
        score += 0.15
    elif element.v_align == "center":
        score += 0.20
    
    # 3. 색상 대비 (25%)
    if is_high_contrast(element.color, background_color):
        score += 0.25
    
    # 4. 폰트 크기 (15%)
    if element.font_size > 3600:
        score += 0.15
    elif element.font_size > 2800:
        score += 0.10
    
    # 5. 시각 효과 (10%)
    if element.has_shadow:
        score += 0.05
    if element.has_glow:
        score += 0.05
    
    return min(score, 1.0)
```

### Extracted Code (python)

```python
def classify_visual_weight(attention_score, color, position):
    """
    primary, secondary, tertiary 분류
    """
    if attention_score > 0.8:
        return "primary"
    elif attention_score > 0.5:
        return "secondary"
    elif is_accent_color(color):
        return "accent"
    else:
        return "tertiary"
```

### Extracted Code (python)

```python
from pptx import Presentation
from pptx.util import Pt, Emu
from pptx.enum.shapes import MSO_SHAPE_TYPE
import json
from datetime import datetime

class PPTSemanticParser:
    def __init__(self, ppt_path):
        self.prs = Presentation(ppt_path)
        self.slide_width = self.prs.slide_width
        self.slide_height = self.prs.slide_height
        
    def parse(self):
        """메인 파싱 함수"""
        result = {
            "metadata": self._extract_metadata(),
            "slides": []
        }
        
        for idx, slide in enumerate(self.prs.slides):
            slide_data = self._parse_slide(slide, idx + 1)
            result["slides"].append(slide_data)
        
        return result
    
    def _extract_metadata(self):
        """프레젠테이션 메타데이터 추출"""
        theme = self._extract_theme()
        
        return {
            "source_file": "uploaded_file.pptx",
            "parsed_at": datetime.now().isoformat(),
            "slide_dimensions": {
                "width": self.slide_width,
                "height": self.slide_height,
                "unit": "emu"
            },
            "theme": theme,
            "total_slides": len(self.prs.slides)
        }
    
    def _extract_theme(self):
        """테마 색상 및 폰트 추출"""
        # 테마 정보 접근
        try:
            theme_part = self.prs.part.package.part_related_by(
                "http://schemas.openxmlformats.org/officeDocument/2006/relationships/theme"
            )
            # XML 파싱하여 색상 스킴 추출
            # a:clrScheme 접근
            pass
        except:
            pass
        
        return {
            "colors": {
                "primary": "#4472C4",  # 기본값
                "accent1": "#ED7D31",
                "background": "#FFFFFF"
            },
            "fonts": {
                "heading": {"latin": "Calibri", "east_asian": "맑은 고딕"},
                "body": {"latin": "Calibri", "east_asian": "맑은 고딕"}
            }
        }
    
    def _parse_slide(self, slide, slide_number):
        """개별 슬라이드 파싱"""
        elements = []
        
        for shape in slide.shapes:
            element_data = self._parse_element(shape)
            if element_data:
                elements.append(element_data)
        
        # 그룹 탐지
        groups = self._detect_groups(elements)
        
        # 레이아웃 분석
        layout_analysis = self._analyze_layout(elements, groups)
        
        return {
            "slide_number": slide_number,
            "layout_name": slide.slide_layout.name,
            "elements": elements,
            "groups": groups,
            "layout_analysis": layout_analysis
        }
    
    def _parse_element(self, shape):
        """개별 요소 파싱 (3 Layer)"""
        elem_id = f"elem_{shape.shape_id}"
        
        # LAYER 1: Physical
        geometry = self._extract_geometry(shape)
        style = self._extract_style(shape)
        
        # LAYER 2: Semantic
        semantic = self._infer_semantic_role(shape, geometry, style)
        design = self._infer_design_intent(shape, geometry, semantic)
        
        # Content
        content = self._extract_content(shape)
        
        return {
            "id": elem_id,
            "type": self._get_shape_type(shape),
            "geometry": geometry,
            "style": style,
            "semantic": semantic,
            "design": design,
            "content": content
        }
    
    def _extract_geometry(self, shape):
        """위치/크기 추출"""
        abs_pos = {
            "left": shape.left,
            "top": shape.top,
            "width": shape.width,
            "height": shape.height,
            "unit": "emu"
        }
        
        # 상대 위치 계산
        rel_x = (shape.left / self.slide_width) * 100
        rel_y = (shape.top / self.slide_height) * 100
        
        # 정렬 추론
        h_align = "center" if 40 < rel_x < 60 else ("left" if rel_x < 40 else "right")
        v_align = "top" if rel_y < 33 else ("middle" if rel_y < 66 else "bottom")
        
        return {
            "absolute": abs_pos,
            "relative": {
                "h_align": h_align,
                "v_align": v_align,
                "offset_percent": {"x": rel_x, "y": rel_y}
            }
        }
    
    def _extract_style(self, shape):
        """스타일 추출"""
        style = {
            "font": None,
            "fill": None,
            "border": None,
            "effects": {}
        }
        
        # 텍스트 프레임이 있는 경우
        if hasattr(shape, "text_frame"):
            if shape.text_frame.paragraphs:
                para = shape.text_frame.paragraphs[0]
                if para.runs:
                    run = para.runs[0]
                    font = run.font
                    
                    style["font"] = {
                        "family": font.name or "Calibri",
                        "size": font.size.pt if font.size else 18,
                        "weight": "bold" if font.bold else "normal",
                        "italic": font.italic or False,
                        "color": self._get_color(font.color)
                    }
        
        # Fill
        if hasattr(shape, "fill"):
            style["fill"] = self._extract_fill(shape.fill)
        
        return style
    
    def _get_color(self, color_obj):
        """색상 객체를 hex로 변환"""
        try:
            if color_obj.type == 1:  # RGB
                rgb = color_obj.rgb
                return f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}".upper()
        except:
            pass
        return None
    
    def _extract_content(self, shape):
        """콘텐츠 추출"""
        content = {
            "raw_text": "",
            "text_runs": [],
            "has_hyperlink": False
        }
        
        if hasattr(shape, "text"):
            content["raw_text"] = shape.text
            
            # Run별 스타일 추출
            if hasattr(shape, "text_frame"):
                for para in shape.text_frame.paragraphs:
                    for run in para.runs:
                        content["text_runs"].append({
                            "text": run.text,
                            "style_override": self._get_run_style(run)
                        })
        
        return content
    
    def _infer_semantic_role(self, shape, geometry, style):
        """의미론적 역할 추론"""
        role = "text"
        level = None
        content_type = "body"
        
        # 크기 기반 판단
        width_ratio = geometry["absolute"]["width"] / self.slide_width
        
        if style.get("font"):
            font_size = style["font"]["size"]
            
            if width_ratio > 0.6 and font_size > 40:
                role = "heading"
                level = 1
                content_type = "title"
            elif font_size > 32:
                role = "heading"
                level = 2
                content_type = "subtitle"
            elif font_size > 24:
                role = "heading"
                level = 3
        
        # HTML 태그 제안
        html_tag = f"h{level}" if role == "heading" else "p"
        
        return {
            "role": role,
            "level": level,
            "content_type": content_type,
            "html_tag_suggestion": html_tag
        }
    
    def _infer_design_intent(self, shape, geometry, semantic):
        """디자인 의도 추론"""
        intent = "neutral"
        
        # 위치 기반
        v_align = geometry["relative"]["v_align"]
        h_align = geometry["relative"]["h_align"]
        
        if v_align == "top" and h_align == "center" and semantic["role"] == "heading":
            intent = "hero_title"
        elif v_align == "bottom":
            intent = "metadata"
        
        # 주목도 점수
        attention_score = self._calculate_attention_score(shape, geometry, semantic)
        
        return {
            "intent": intent,
            "visual_weight": "primary" if attention_score > 0.8 else "secondary",
            "attention_score": attention_score
        }
    
    def _calculate_attention_score(self, shape, geometry, semantic):
        """시각적 주목도 계산"""
        score = 0.0
        
        # 크기 (30%)
        size_ratio = (geometry["absolute"]["width"] * geometry["absolute"]["height"]) / \
                     (self.slide_width * self.slide_height)
        score += min(size_ratio * 3, 0.3)
        
        # 위치 (20%)
        if geometry["relative"]["v_align"] == "center":
            score += 0.2
        elif geometry["relative"]["v_align"] == "top":
            score += 0.15
        
        # 의미론적 역할 (50%)
        if semantic["role"] == "heading":
            score += 0.3 if semantic["level"] == 1 else 0.2
        
        return min(score, 1.0)
    
    def _detect_groups(self, elements):
        """그룹 탐지"""
        groups = []
        
        # 수직 정렬 탐지
        vertical_groups = self._detect_vertical_alignment(elements)
        groups.extend(vertical_groups)
        
        # 카드 그리드 탐지
        card_grids = self._detect_card_grids(elements)
        groups.extend(card_grids)
        
        return groups
    
    def _detect_vertical_alignment(self, elements):
        """수직 정렬 패턴 탐지"""
        # 구현 생략 (복잡도 관계)
        return []
    
    def _analyze_layout(self, elements, groups):
        """전체 레이아웃 분석"""
        # Hero 영역 탐지
        hero_elements = [e for e in elements 
                        if e["geometry"]["relative"]["v_align"] == "top"]
        
        return {
            "pattern": "hero_centered" if hero_elements else "standard",
            "grid": {
                "detected": False
            }
        }

# 사용 예시
if __name__ == "__main__":
    parser = PPTSemanticParser("/mnt/user-data/uploads/presentation.pptx")
    result = parser.parse()
    
    # JSON 저장
    with open("parsed_output.json", "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
```

### Extracted Code (markdown)

```markdown
You are a PPT Semantic Parser Agent specialized in analyzing PowerPoint presentations with THREE analytical layers:

1. **Physical Layer**: Extract exact positions, sizes, colors, fonts using python-pptx
2. **Semantic Layer**: Infer roles (heading/paragraph/list), content types, HTML tag suggestions
3. **Relational Layer**: Detect visual groups, layout patterns, spatial relationships

Your output MUST be a valid JSON following the schema provided in the context.

**Key Principles:**
- Be precise with measurements (use EMU units from python-pptx)
- Infer semantic meaning from physical attributes (size → heading level, position → intent)
- Detect visual patterns (vertical alignment → list, image+text → figure)
- Suggest HTML5 semantic tags based on content role
- Calculate attention scores based on size, position, color contrast
- Group related elements for better HTML structure

**Analysis Order:**
1. Extract all physical properties first
2. Then infer semantic roles from physics
3. Finally detect groups and relationships
4. Perform layout-level analysis

**Output Quality:**
- Complete JSON (no truncation)
- Korean text properly encoded (UTF-8)
- All measurements in EMU units
- RGB colors in #RRGGBB hex format
```

### Extracted Code (markdown)

```markdown
# Task: Parse PowerPoint Presentation

Analyze the uploaded PowerPoint file and generate a comprehensive JSON output with 3 analytical layers.

## File Information
- **File Path**: /mnt/user-data/uploads/CDP안내자료_생산기술원_제조AX아카데미_260130.pptx
- **Expected Slides**: ~10-15
- **Language**: Korean (한국어)
- **Theme**: Manufacturing AX Academy (제조 AX 아카데미)

## Required JSON Schema
```

### Extracted Code (text)

```text
## Step-by-Step Instructions

### Step 1: Extract Metadata
1. Open the PPTX file using python-pptx
2. Get slide dimensions (width, height in EMU)
3. Extract theme colors from `a:clrScheme` in theme XML
4. Extract font scheme from `a:fontScheme`
5. Record parsing timestamp

### Step 2: For Each Slide
1. Iterate through all slides
2. Extract slide layout name
3. Get background fill properties

### Step 3: For Each Element (Shape)
1. **Physical Layer:**
   - Position: `shape.left`, `shape.top`
   - Size: `shape.width`, `shape.height`
   - Font: `run.font.name`, `run.font.size`, `run.font.bold`, `run.font.color`
   - Fill: `shape.fill.type`, `shape.fill.fore_color.rgb`
   - Effects: Check for shadow, glow, reflection

2. **Semantic Layer:**
   - If font_size > 40pt AND width > 60% → role="heading", level=1
   - If font_size > 32pt → role="heading", level=2
   - If font_size > 24pt → role="heading", level=3
   - If text_length < 50 → content_type="label"
   - If text_length > 200 → content_type="body"

3. **Design Layer:**
   - If v_align="top" AND h_align="center" AND role="heading" → intent="hero_title"
   - If v_align="bottom" → intent="metadata"
   - Calculate attention_score:
     - size_ratio * 0.3
     - position_bonus * 0.2
     - role_bonus * 0.5

4. **Content Extraction:**
   - Full text: `shape.text`
   - Text runs with individual styles
   - Detect hyperlinks

### Step 4: Group Detection
1. Find vertically aligned elements (left position within 5% tolerance)
2. Find image + adjacent text (distance < 50,000 EMU)
3. Find horizontally aligned boxes (card grid pattern)
4. Suggest HTML structure for each group

### Step 5: Layout Analysis
1. Identify hero area (top 33% of slide)
2. Detect grid patterns (uniform spacing)
3. Classify overall layout pattern

## Special Handling for Korean Text
- Ensure all Korean characters are UTF-8 encoded
- Check for mixed Korean/English text runs
- Preserve Korean font family (usually "맑은 고딕" or "Noto Sans KR")

## Output Requirements
- **Format**: Valid JSON (no trailing commas, proper escaping)
- **Encoding**: UTF-8 with Korean support
- **Completeness**: All slides, all elements
- **Precision**: All measurements in exact EMU units
- **Suggestions**: Include html_tag_suggestion and html_structure_suggestion

## Error Handling
- If theme extraction fails, use default colors
- If font info missing, default to "Calibri"
- Skip decorative shapes (type == "line" with no text)
- Handle grouped shapes by ungrouping

## Final Checklist
- [ ] All slides parsed
- [ ] All text content extracted
- [ ] Semantic roles assigned
- [ ] Groups detected
- [ ] Layout patterns identified
- [ ] JSON is valid
- [ ] Korean text preserved

Now, please analyze the PowerPoint file and output the complete JSON.
```

### Extracted Code (json)

```json
{
  "metadata": {
    "source_file": "CDP안내자료_생산기술원_제조AX아카데미_260130.pptx",
    "parsed_at": "2025-01-30T15:30:00Z",
    "slide_dimensions": {
      "width": 9144000,
      "height": 6858000,
      "unit": "emu"
    },
    "theme": {
      "colors": {
        "primary": "#4472C4",
        "accent1": "#E67E22",
        "accent2": "#A5A5A5",
        "background": "#FFFFFF"
      },
      "fonts": {
        "heading": {
          "latin": "Calibri Light",
          "east_asian": "맑은 고딕"
        },
        "body": {
          "latin": "Calibri",
          "east_asian": "맑은 고딕"
        }
      }
    },
    "total_slides": 12
  },
  
  "slides": [
    {
      "slide_number": 1,
      "layout_name": "Title Slide",
      "layout_pattern": "hero_centered",
      "background": {
        "type": "solid",
        "color": "#FFFFFF"
      },
      
      "elements": [
        {
          "id": "elem_1_1",
          "type": "text_box",
          
          "geometry": {
            "absolute": {
              "left": 914400,
              "top": 1828800,
              "width": 7315200,
              "height": 1143000,
              "unit": "emu"
            },
            "relative": {
              "h_align": "center",
              "v_align": "top",
              "offset_percent": {
                "x": 50.0,
                "y": 26.7
              }
            },
            "z_index": 1
          },
          
          "style": {
            "font": {
              "family": "맑은 고딕",
              "size": 44,
              "weight": "bold",
              "italic": false,
              "underline": false,
              "color": "#2C3E50"
            },
            "fill": {
              "type": "none",
              "color": null,
              "transparency": 0
            },
            "border": {
              "width": 0,
              "color": null,
              "style": "none"
            },
            "effects": {
              "shadow": false,
              "reflection": false,
              "glow": false
            }
          },
          
          "semantic": {
            "role": "heading",
            "level": 1,
            "content_type": "title",
            "html_tag_suggestion": "h1"
          },
          
          "design": {
            "intent": "hero_title",
            "visual_weight": "primary",
            "attention_score": 0.95,
            "purpose": "main_message"
          },
          
          "content": {
            "raw_text": "제조 AX 아카데미",
            "text_runs": [
              {
                "text": "제조 ",
                "style_override": null
              },
              {
                "text": "AX",
                "style_override": {
                  "color": "#E67E22",
                  "weight": "bold"
                }
              },
              {
                "text": " 아카데미",
                "style_override": null
              }
            ],
            "has_hyperlink": false,
            "language": "ko"
          },
          
          "relationships": {
            "parent_group": null,
            "visual_proximity": {
              "nearest_below": "elem_1_2",
              "distance_to_below": 200000
            }
          }
        },
        
        {
          "id": "elem_1_2",
          "type": "text_box",
          
          "geometry": {
            "absolute": {
              "left": 914400,
              "top": 3171800,
              "width": 7315200,
              "height": 571500,
              "unit": "emu"
            },
            "relative": {
              "h_align": "center",
              "v_align": "middle",
              "offset_percent": {
                "x": 50.0,
                "y": 46.2
              }
            }
          },
          
          "style": {
            "font": {
              "family": "맑은 고딕",
              "size": 28,
              "weight": "normal",
              "color": "#7F8C8D"
            }
          },
          
          "semantic": {
            "role": "heading",
            "level": 2,
            "content_type": "subtitle",
            "html_tag_suggestion": "p class='subtitle'"
          },
          
          "design": {
            "intent": "subtitle",
            "visual_weight": "secondary",
            "attention_score": 0.65
          },
          
          "content": {
            "raw_text": "CDP 전문가 양성 프로그램",
            "text_runs": [
              {
                "text": "CDP 전문가 양성 프로그램",
                "style_override": null
              }
            ]
          }
        }
      ],
      
      "groups": [
        {
          "id": "group_1_1",
          "type": "vertical_stack",
          "members": ["elem_1_1", "elem_1_2"],
          "layout": {
            "direction": "vertical",
            "spacing": 200000,
            "alignment": "center"
          },
          "html_structure_suggestion": {
            "container": "header",
            "children": ["h1", "p.subtitle"],
            "layout_method": "flex-column"
          }
        }
      ],
      
      "layout_analysis": {
        "pattern": "hero_centered",
        "regions": {
          "hero": {
            "bounds": {"top": 0, "height": "50%"},
            "elements": ["group_1_1"]
          }
        },
        "grid": {
          "detected": false
        }
      }
    }
  ]
}
```

### Extracted Code (markdown)

```markdown
1. System Instruction: 역할 정의 + 핵심 원칙
2. User Prompt: 
   - Task 명확화
   - JSON 스키마 제시
   - Step-by-step 지시
   - 예시 제공
   - 체크리스트
```

### Extracted Code (bash)

```bash
# 1. python-pptx 설치
pip install python-pptx

# 2. 기본 파서 실행
python ppt_parser.py

# 3. JSON 검증
python -m json.tool parsed_output.json
```

### Extracted Code (python)

```python
import google.generativeai as genai

# API 설정
genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel("gemini-2.0-flash-exp")

# JSON을 컨텍스트로 전달
with open("parsed_output.json") as f:
    parsed_data = f.read()

response = model.generate_content([
    "이 JSON은 PPT 파싱 결과입니다.",
    parsed_data,
    "이를 HTML로 변환하되, semantic 정보를 활용하세요."
])

print(response.text)
```
