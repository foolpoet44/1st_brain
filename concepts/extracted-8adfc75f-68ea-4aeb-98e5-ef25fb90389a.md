# Extracted Knowledge from Conv: 8adfc75f-68ea-4aeb-98e5-ef25fb90389a

**Date**: 2026-01-11T04:17:55.120329Z

### Extracted Code (python)

```python
# Power Automate Flow 구조 (의사코드)
Trigger: OneDrive에 새 파일 (경로: /회의록/)
Condition: 파일명에 "리더십" OR "DX" 포함
Action 1: 파일 내용 읽기 → GPT API로 요약
Action 2: Notion에 페이지 생성 (DB: 학습 노트, 태그: #업무연계)
Action 3: Google Drive에 복사 (폴더: Work Archive)
```

### Extracted Code (text)

```text
[OneDrive 워크스페이스]
         ↓ (변환 트리거)
   [변환 허브 (로컬 또는 클라우드)]
         ↓ (병렬 처리)
    ┌────┴────┬────────┐
    ↓         ↓        ↓
[Google   [Notion]  [GitHub]
 Drive]              (백업)
```

### Extracted Code (bash)

```bash
# 기본 변환
pandoc input.docx -o output.md --extract-media=./images

# HR 문서 최적화 변환
pandoc input.docx -o output.md \
  --extract-media=./images \
  --wrap=none \
  --markdown-headings=atx \
  --lua-filter=hr-template.lua
```

### Extracted Code (markdown)

```markdown
# 리더십 평가 - 홍길동 (2024 Q4)

## 평가 항목

| 역량 | 점수 | 피드백 |
|------|------|--------|
| 전략적 사고 | 4.2 | 중장기 로드맵 수립 우수 |
| 팀 개발 | 3.8 | 1:1 코칭 강화 필요 |

## 상세 피드백
> "분기별 목표 달성률 95% 이상 유지..."

## 다음 액션
- [ ] 코칭 스킬 교육 이수 (2025 Q1)
- [ ] 멘토링 프로그램 참여
```

### Extracted Code (python)

```python
import pandas as pd
from pathlib import Path

def excel_to_markdown(xlsx_path, output_path):
    # 모든 시트를 읽어서 각각 마크다운 테이블로
    excel_file = pd.ExcelFile(xlsx_path)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(f"# {Path(xlsx_path).stem}\n\n")
        
        for sheet_name in excel_file.sheet_names:
            df = pd.read_excel(xlsx_path, sheet_name=sheet_name)
            
            # 빈 행/열 제거
            df = df.dropna(how='all').dropna(axis=1, how='all')
            
            f.write(f"## {sheet_name}\n\n")
            f.write(df.to_markdown(index=False))
            f.write("\n\n")
            
            # 통계 자동 추가
            if df.select_dtypes(include='number').columns.any():
                f.write("### 요약 통계\n\n")
                f.write(df.describe().to_markdown())
                f.write("\n\n")

# 사용
excel_to_markdown("리더십평가_2024Q4.xlsx", "leadership_eval_2024q4.md")
```

### Extracted Code (python)

```python
from pptx import Presentation
from pathlib import Path

def pptx_to_markdown(pptx_path, output_path, extract_images=True):
    prs = Presentation(pptx_path)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(f"# {Path(pptx_path).stem}\n\n")
        f.write(f"**슬라이드 총 {len(prs.slides)}장**\n\n")
        f.write("---\n\n")
        
        for idx, slide in enumerate(prs.slides, 1):
            f.write(f"## 슬라이드 {idx}\n\n")
            
            # 텍스트 추출
            for shape in slide.shapes:
                if shape.has_text_frame:
                    text = shape.text.strip()
                    if text:
                        # 제목은 ### 로, 본문은 - 로
                        if shape.is_placeholder:
                            f.write(f"### {text}\n\n")
                        else:
                            f.write(f"- {text}\n")
            
            # 이미지 추출 (옵션)
            if extract_images:
                for shape in slide.shapes:
                    if shape.shape_type == 13:  # Picture
                        image = shape.image
                        image_path = f"images/slide_{idx}_{shape.shape_id}.png"
                        # 이미지 저장 로직...
                        f.write(f"\n![슬라이드 {idx} 이미지]({image_path})\n")
            
            f.write("\n---\n\n")

# 사용
pptx_to_markdown("DX교육_자료.pptx", "dx_training.md")
```

### Extracted Code (python)

```python
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
from pathlib import Path

class OfficeToMarkdownHandler(FileSystemEventHandler):
    def __init__(self, watch_folder, output_folder):
        self.watch_folder = Path(watch_folder)
        self.output_folder = Path(output_folder)
        self.output_folder.mkdir(exist_ok=True)
        
        # 변환 중인 파일 추적 (중복 방지)
        self.processing = set()
    
    def on_created(self, event):
        if event.is_directory:
            return
        
        file_path = Path(event.src_path)
        
        # Office 파일만 처리
        if file_path.suffix not in ['.docx', '.xlsx', '.pptx']:
            return
        
        # 임시 파일 무시
        if file_path.name.startswith('~$'):
            return
        
        # 중복 처리 방지
        if str(file_path) in self.processing:
            return
        
        self.processing.add(str(file_path))
        
        # 파일 쓰기 완료 대기 (OneDrive 동기화 고려)
        time.sleep(2)
        
        try:
            self.convert_file(file_path)
        finally:
            self.processing.discard(str(file_path))
    
    def convert_file(self, file_path):
        output_name = file_path.stem + '.md'
        output_path = self.output_folder / output_name
        
        print(f"🔄 변환 시작: {file_path.name}")
        
        if file_path.suffix == '.docx':
            # Pandoc 사용
            subprocess.run([
                'pandoc', str(file_path), 
                '-o', str(output_path),
                '--extract-media=./images',
                '--wrap=none'
            ])
        
        elif file_path.suffix == '.xlsx':
            excel_to_markdown(file_path, output_path)
        
        elif file_path.suffix == '.pptx':
            pptx_to_markdown(file_path, output_path)
        
        print(f"✅ 변환 완료: {output_path.name}")
        
        # Google Drive 업로드
        self.upload_to_google_drive(output_path)
        
        # Notion 동기화
        self.sync_to_notion(output_path, file_path)
    
    def upload_to_google_drive(self, md_path):
        # Google Drive API 또는 rclone 사용
        subprocess.run([
            'rclone', 'copy', 
            str(md_path), 
            'gdrive:MarkdownDocs/'
        ])
        print(f"☁️ Google Drive 업로드: {md_path.name}")
    
    def sync_to_notion(self, md_path, original_path):
        # Notion API로 페이지 생성
        with open(md_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 메타데이터 추출
        metadata = {
            '제목': md_path.stem,
            '원본 파일': original_path.name,
            '변환 일시': time.strftime('%Y-%m-%d %H:%M'),
            '타입': original_path.suffix[1:].upper()
        }
        
        # Notion API 호출 (CSP님의 기존 아카이빙 시스템 활용)
        # create_notion_page(content, metadata)
        print(f"📝 Notion 동기화: {md_path.name}")

# 실행
if __name__ == "__main__":
    watch_path = "C:/Users/CSP/OneDrive/MarkdownSync"
    output_path = "C:/Users/CSP/Documents/ConvertedMD"
    
    event_handler = OfficeToMarkdownHandler(watch_path, output_path)
    observer = Observer()
    observer.schedule(event_handler, watch_path, recursive=True)
    observer.start()
    
    print(f"👀 폴더 모니터링 시작: {watch_path}")
    print("종료하려면 Ctrl+C를 누르세요...")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
```

### Extracted Code (text)

```text
[트리거] OneDrive 폴더에 파일 생성
    ↓
[조건] 파일 확장자가 .docx/.xlsx/.pptx
    ↓
[액션 1] 로컬에 파일 다운로드
    ↓
[액션 2] Python 스크립트 실행
    Parameters: %FilePath% %OutputFolder%
    ↓
[액션 3] 생성된 .md 파일을 Google Drive에 업로드
    ↓
[액션 4] Notion API 호출 (페이지 생성)
    ↓
[액션 5] 원본 파일을 "아카이브" 폴더로 이동
```

### Extracted Code (yaml)

```yaml
name: Office to Markdown Converter

on:
  repository_dispatch:
    types: [onedrive-sync]
  # 또는 webhook으로 OneDrive 변경 감지

jobs:
  convert:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: |
          pip install pandoc openpyxl pandas python-pptx
          sudo apt-get install -y pandoc
      
      - name: Download from OneDrive
        env:
          ONEDRIVE_TOKEN: ${{ secrets.ONEDRIVE_TOKEN }}
        run: |
          python scripts/download_files.py
      
      - name: Convert to Markdown
        run: |
          python scripts/batch_convert.py
      
      - name: Upload to Google Drive
        env:
          GDRIVE_CREDENTIALS: ${{ secrets.GDRIVE_CREDENTIALS }}
        run: |
          python scripts/upload_to_gdrive.py
      
      - name: Sync to Notion
        env:
          NOTION_TOKEN: ${{ secrets.NOTION_TOKEN }}
        run: |
          python scripts/sync_notion.py
      
      - name: Commit changes
        run: |
          git config user.name "MD Converter Bot"
          git add .
          git commit -m "Auto-convert: $(date)"
          git push
```

### Extracted Code (markdown)

```markdown
---
title: "2024 Q4 리더십 평가 - 홍길동"
original_file: "리더십평가_홍길동_2024Q4.docx"
created_date: 2024-12-20
author: CSP
document_type: 평가서
tags:
  - 리더십
  - Q4
  - 평가
category: HR/평가
related_framework: LG_Leadership_Competency
ontology_class: PerformanceEvaluation
properties:
  evaluator: CSP
  evaluatee: 홍길동
  period: 2024-Q4
  overall_score: 4.1
synced_to:
  - notion: https://notion.so/abc123
  - gdrive: https://drive.google.com/xyz456
---

# 리더십 평가 - 홍길동 (2024 Q4)

## 평가 항목
...
```

### Extracted Code (python)

```python
# 변환 로그 자동 생성
conversion_log = {
    "timestamp": "2024-12-25 14:30:00",
    "source": "리더십평가_2024Q4.docx",
    "target": "leadership_eval_2024q4.md",
    "metrics": {
        "original_size": "245KB",
        "markdown_size": "23KB",
        "compression_ratio": "90.6%",
        "paragraphs": 45,
        "tables": 3,
        "images": 2,
        "processing_time": "1.2s"
    },
    "quality_checks": {
        "tables_preserved": True,
        "images_extracted": True,
        "formatting_intact": True,
        "korean_encoding": "UTF-8"
    },
    "destinations": [
        "Google Drive: /MarkdownDocs/HR/",
        "Notion: HR 문서 아카이브",
        "GitHub: docs/evaluations/"
    ]
}
```

### Extracted Code (bash)

```bash
# Markdown → Google Docs (Apps Script 활용)
# Markdown → Word
pandoc input.md -o output.docx --reference-doc=company_template.docx
```

### Extracted Code (bash)

```bash
# Python 3.11 이상 설치 확인
python --version

# 필수 라이브러리 설치
pip install python-pptx Pillow markdown2 python-docx

# 선택: Pandoc 설치 (고급 변환용)
# https://pandoc.org/installing.html 에서 다운로드
```

### Extracted Code (text)

```text
C:/Users/CSP/
├── PPTConverter/
│   ├── 📂 input/           # OneDrive 동기화 폴더
│   ├── 📂 output/          # 변환된 MD 파일
│   ├── 📂 images/          # 추출된 이미지
│   ├── 📂 archive/         # 원본 백업
│   ├── 📂 logs/            # 변환 로그
│   └── 📄 converter.py     # 메인 스크립트
```

### Extracted Code (python)

```python
"""
PowerPoint to Markdown Converter v1.0
CSP's HR Document Automation System
"""

import os
import re
from pathlib import Path
from datetime import datetime
from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE
from PIL import Image
import io
import json

class PPTXConverter:
    def __init__(self, input_folder, output_folder, images_folder, archive_folder):
        self.input_folder = Path(input_folder)
        self.output_folder = Path(output_folder)
        self.images_folder = Path(images_folder)
        self.archive_folder = Path(archive_folder)
        
        # 폴더 생성
        for folder in [self.output_folder, self.images_folder, self.archive_folder]:
            folder.mkdir(parents=True, exist_ok=True)
    
    def extract_metadata(self, prs):
        """PPT 메타데이터 추출"""
        try:
            core_props = prs.core_properties
            return {
                'title': core_props.title or '제목 없음',
                'author': core_props.author or 'Unknown',
                'created': core_props.created.strftime('%Y-%m-%d') if core_props.created else 'N/A',
                'modified': core_props.modified.strftime('%Y-%m-%d') if core_props.modified else 'N/A',
                'slide_count': len(prs.slides)
            }
        except:
            return {
                'title': '제목 없음',
                'author': 'Unknown',
                'created': 'N/A',
                'modified': 'N/A',
                'slide_count': len(prs.slides)
            }
    
    def extract_text_from_shape(self, shape):
        """도형에서 텍스트 추출 (재귀적)"""
        text_items = []
        
        if shape.has_text_frame:
            for paragraph in shape.text_frame.paragraphs:
                text = paragraph.text.strip()
                if text:
                    # 들여쓰기 레벨 감지
                    level = paragraph.level
                    indent = '  ' * level
                    text_items.append((level, f"{indent}- {text}"))
        
        # 그룹 도형 처리
        if shape.shape_type == MSO_SHAPE_TYPE.GROUP:
            for sub_shape in shape.shapes:
                text_items.extend(self.extract_text_from_shape(sub_shape))
        
        return text_items
    
    def extract_image(self, shape, slide_idx, image_counter, ppt_name):
        """이미지 추출 및 저장"""
        try:
            image = shape.image
            image_bytes = image.blob
            
            # 이미지 파일명 생성
            ext = image.ext
            filename = f"{ppt_name}_slide{slide_idx:02d}_img{image_counter:02d}.{ext}"
            image_path = self.images_folder / filename
            
            # 이미지 저장
            with open(image_path, 'wb') as f:
                f.write(image_bytes)
            
            # 상대 경로 반환
            return f"images/{filename}"
        except Exception as e:
            print(f"  ⚠️ 이미지 추출 실패: {e}")
            return None
    
    def extract_table(self, shape):
        """표 추출"""
        if not shape.has_table:
            return None
        
        table = shape.table
        md_table = []
        
        # 헤더 행
        header = []
        for cell in table.rows[0].cells:
            header.append(cell.text.strip())
        md_table.append("| " + " | ".join(header) + " |")
        md_table.append("| " + " | ".join(["---"] * len(header)) + " |")
        
        # 데이터 행
        for row in table.rows[1:]:
            row_data = []
            for cell in row.cells:
                row_data.append(cell.text.strip())
            md_table.append("| " + " | ".join(row_data) + " |")
        
        return "\n".join(md_table)
    
    def extract_notes(self, slide):
        """슬라이드 노트(발표자 메모) 추출"""
        try:
            if slide.has_notes_slide:
                notes_slide = slide.notes_slide
                text_frame = notes_slide.notes_text_frame
                notes = text_frame.text.strip()
                if notes:
                    return notes
        except:
            pass
        return None
    
    def convert_slide(self, slide, slide_idx, ppt_name):
        """단일 슬라이드 변환"""
        md_content = []
        image_counter = 1
        
        # 슬라이드 제목
        md_content.append(f"\n## 슬라이드 {slide_idx}\n")
        
        # 도형별 처리
        has_title = False
        bullet_items = []
        
        for shape in slide.shapes:
            # 제목 감지
            if shape.is_placeholder and shape.placeholder_format.type == 1:  # Title
                title = shape.text.strip()
                if title:
                    md_content.append(f"### {title}\n")
                    has_title = True
            
            # 텍스트 박스
            elif shape.has_text_frame:
                text_items = self.extract_text_from_shape(shape)
                for level, text in text_items:
                    bullet_items.append(text)
            
            # 표
            elif shape.has_table:
                table_md = self.extract_table(shape)
                if table_md:
                    md_content.append(f"\n{table_md}\n")
            
            # 이미지
            elif shape.shape_type == MSO_SHAPE_TYPE.PICTURE:
                image_path = self.extract_image(shape, slide_idx, image_counter, ppt_name)
                if image_path:
                    md_content.append(f"\n![슬라이드 {slide_idx} 이미지 {image_counter}]({image_path})\n")
                    image_counter += 1
            
            # 차트
            elif shape.has_chart:
                md_content.append(f"\n> 📊 **차트**: {shape.chart.chart_title.text_frame.text if shape.chart.has_title else '제목 없음'}\n")
        
        # 불렛 포인트 추가
        if bullet_items:
            md_content.append("\n" + "\n".join(bullet_items) + "\n")
        
        # 발표자 노트
        notes = self.extract_notes(slide)
        if notes:
            md_content.append(f"\n> **발표자 노트**: {notes}\n")
        
        return "".join(md_content)
    
    def generate_frontmatter(self, metadata, ppt_path):
        """YAML Frontmatter 생성"""
        frontmatter = f"""---
title: "{metadata['title']}"
author: "{metadata['author']}"
created_date: "{metadata['created']}"
modified_date: "{metadata['modified']}"
slide_count: {metadata['slide_count']}
original_file: "{ppt_path.name}"
converted_date: "{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
document_type: "Presentation"
tags:
  - ppt-converted
  - {ppt_path.stem.lower().replace(' ', '-')}
category: "HR/교육자료"
---

"""
        return frontmatter
    
    def convert_pptx(self, pptx_path):
        """메인 변환 함수"""
        print(f"\n{'='*60}")
        print(f"🔄 변환 시작: {pptx_path.name}")
        print(f"{'='*60}")
        
        try:
            # PPT 로드
            prs = Presentation(str(pptx_path))
            
            # 메타데이터 추출
            metadata = self.extract_metadata(prs)
            print(f"📊 슬라이드 수: {metadata['slide_count']}장")
            print(f"👤 작성자: {metadata['author']}")
            
            # Markdown 콘텐츠 생성
            md_content = []
            
            # Frontmatter 추가
            md_content.append(self.generate_frontmatter(metadata, pptx_path))
            
            # 문서 제목
            md_content.append(f"# {metadata['title']}\n")
            md_content.append(f"\n**총 {metadata['slide_count']}장의 슬라이드**\n")
            md_content.append("\n---\n")
            
            # 각 슬라이드 변환
            for idx, slide in enumerate(prs.slides, 1):
                print(f"  ✓ 슬라이드 {idx}/{metadata['slide_count']} 변환 중...")
                slide_md = self.convert_slide(slide, idx, pptx_path.stem)
                md_content.append(slide_md)
                md_content.append("\n---\n")
            
            # Markdown 파일 저장
            output_filename = f"{pptx_path.stem}.md"
            output_path = self.output_folder / output_filename
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write("".join(md_content))
            
            print(f"✅ 변환 완료: {output_path}")
            
            # 원본 파일 아카이브
            archive_path = self.archive_folder / f"{pptx_path.stem}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pptx"
            pptx_path.rename(archive_path)
            print(f"📦 원본 아카이브: {archive_path}")
            
            # 변환 로그 저장
            self.save_log(pptx_path.name, output_path, metadata)
            
            return True
            
        except Exception as e:
            print(f"❌ 변환 실패: {e}")
            import traceback
            traceback.print_exc()
            return False
    
    def save_log(self, source_file, output_path, metadata):
        """변환 로그 저장"""
        log_folder = self.input_folder.parent / "logs"
        log_folder.mkdir(exist_ok=True)
        
        log_file = log_folder / f"conversion_log_{datetime.now().strftime('%Y%m')}.json"
        
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'source_file': source_file,
            'output_file': output_path.name,
            'slide_count': metadata['slide_count'],
            'author': metadata['author'],
            'status': 'success'
        }
        
        # 기존 로그 읽기
        logs = []
        if log_file.exists():
            with open(log_file, 'r', encoding='utf-8') as f:
                logs = json.load(f)
        
        logs.append(log_entry)
        
        # 로그 저장
        with open(log_file, 'w', encoding='utf-8') as f:
            json.dump(logs, f, ensure_ascii=False, indent=2)
    
    def batch_convert(self):
        """폴더 내 모든 PPTX 파일 일괄 변환"""
        pptx_files = list(self.input_folder.glob("*.pptx"))
        
        # 임시 파일 제외
        pptx_files = [f for f in pptx_files if not f.name.startswith('~$')]
        
        if not pptx_files:
            print("📭 변환할 PPTX 파일이 없습니다.")
            return
        
        print(f"\n📚 총 {len(pptx_files)}개 파일 발견")
        
        success_count = 0
        for pptx_file in pptx_files:
            if self.convert_pptx(pptx_file):
                success_count += 1
        
        print(f"\n{'='*60}")
        print(f"🎉 변환 완료: {success_count}/{len(pptx_files)} 성공")
        print(f"{'='*60}\n")


# 메인 실행 코드
if __name__ == "__main__":
    print("""
    ╔══════════════════════════════════════════════════════╗
    ║   PowerPoint → Markdown Converter v1.0              ║
    ║   CSP's HR Document Automation System               ║
    ╚══════════════════════════════════════════════════════╝
    """)
    
    # 경로 설정
    BASE_DIR = Path(__file__).parent
    INPUT_DIR = BASE_DIR / "input"
    OUTPUT_DIR = BASE_DIR / "output"
    IMAGES_DIR = BASE_DIR / "images"
    ARCHIVE_DIR = BASE_DIR / "archive"
    
    # 변환기 생성 및 실행
    converter = PPTXConverter(INPUT_DIR, OUTPUT_DIR, IMAGES_DIR, ARCHIVE_DIR)
    converter.batch_convert()
    
    input("\n엔터를 눌러 종료하세요...")
```

### Extracted Code (batch)

```batch
@echo off
chcp 65001
echo ╔══════════════════════════════════════════════════════╗
echo ║   PowerPoint 변환기 실행 중...                       ║
echo ╚══════════════════════════════════════════════════════╝
echo.

cd /d "%~dp0"
python converter.py

pause
```

### Extracted Code (batch)

```batch
@echo off
chcp 65001

if "%~1"=="" (
    echo PPT 파일을 이 bat 파일로 드래그하세요!
    pause
    exit
)

echo 변환 중: %~nx1
python converter.py "%~1"
pause
```

### Extracted Code (python)

```python
# 스크립트 끝부분 수정
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        # 단일 파일 변환 모드
        pptx_path = Path(sys.argv[1])
        if pptx_path.suffix.lower() == '.pptx':
            converter = PPTXConverter(INPUT_DIR, OUTPUT_DIR, IMAGES_DIR, ARCHIVE_DIR)
            converter.convert_pptx(pptx_path)
    else:
        # 일괄 변환 모드
        converter.batch_convert()
```

### Extracted Code (markdown)

```markdown
## 변환 품질 점검표

### 필수 항목
- [ ] 모든 슬라이드 번호가 순서대로 변환되었는가?
- [ ] 제목이 정확히 추출되었는가?
- [ ] 불렛 포인트 계층 구조가 유지되는가?
- [ ] 한글이 깨지지 않았는가? (UTF-8 인코딩)

### 콘텐츠 항목
- [ ] 이미지가 images 폴더에 저장되었는가?
- [ ] 이미지 링크가 정상 작동하는가?
- [ ] 표가 마크다운 테이블로 변환되었는가?
- [ ] 발표자 노트가 추출되었는가?

### 메타데이터 항목
- [ ] YAML frontmatter에 작성자 정보가 있는가?
- [ ] 슬라이드 수가 정확한가?
- [ ] 변환 일시가 기록되었는가?

### 아카이브 항목
- [ ] 원본 PPT가 archive 폴더로 이동했는가?
- [ ] 로그 파일이 생성되었는가?
```

### Extracted Code (python)

```python
from pathlib import Path
import re

def check_markdown_quality(md_path):
    """Markdown 파일 품질 검사"""
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    issues = []
    
    # 빈 슬라이드 체크
    empty_slides = re.findall(r'## 슬라이드 \d+\n\n---', content)
    if empty_slides:
        issues.append(f"⚠️ 빈 슬라이드 {len(empty_slides)}개 발견")
    
    # 깨진 이미지 링크 체크
    broken_images = re.findall(r'!\[.*?\]\((images/.*?)\)', content)
    for img_path in broken_images:
        full_path = md_path.parent.parent / img_path
        if not full_path.exists():
            issues.append(f"⚠️ 이미지 없음: {img_path}")
    
    # frontmatter 체크
    if not content.startswith('---'):
        issues.append("⚠️ YAML frontmatter 없음")
    
    # 슬라이드 수 카운트
    slide_count = len(re.findall(r'## 슬라이드 \d+', content))
    
    print(f"\n{'='*50}")
    print(f"📄 파일: {md_path.name}")
    print(f"📊 슬라이드 수: {slide_count}")
    
    if issues:
        print(f"⚠️ 발견된 이슈:")
        for issue in issues:
            print(f"  {issue}")
    else:
        print("✅ 품질 검사 통과!")
    print(f"{'='*50}\n")

# 실행
output_folder = Path("output")
for md_file in output_folder.glob("*.md"):
    check_markdown_quality(md_file)
```

### Extracted Code (bash)

```bash
# rclone 설치
# Windows: https://rclone.org/downloads/ 에서 다운로드

# Google Drive 연동 설정
rclone config

# 대화형 설정
# n) New remote → gdrive
# Google Drive 선택
# 브라우저에서 인증
```

### Extracted Code (python)

```python
import subprocess

def upload_to_google_drive(self, md_path):
    """Google Drive 업로드"""
    try:
        # rclone으로 업로드
        result = subprocess.run([
            'rclone', 'copy',
            str(md_path),
            'gdrive:MarkdownDocs/PPT변환/',
            '--progress'
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"☁️ Google Drive 업로드 완료: {md_path.name}")
            return True
        else:
            print(f"⚠️ 업로드 실패: {result.stderr}")
            return False
    except FileNotFoundError:
        print("⚠️ rclone이 설치되지 않았습니다. 수동으로 업로드하세요.")
        return False

# convert_pptx 함수에서 호출
# 변환 완료 후:
self.upload_to_google_drive(output_path)
```

### Extracted Code (python)

```python
import requests

class NotionSync:
    def __init__(self, api_key, database_id):
        self.api_key = api_key
        self.database_id = database_id
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "Notion-Version": "2022-06-28"
        }
    
    def upload_markdown(self, md_path, metadata):
        """Markdown을 Notion 페이지로 업로드"""
        
        with open(md_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # frontmatter 제거
        content = re.sub(r'^---.*?---\n', '', content, flags=re.DOTALL)
        
        # Notion 페이지 생성
        url = "https://api.notion.com/v1/pages"
        
        data = {
            "parent": {"database_id": self.database_id},
            "properties": {
                "제목": {
                    "title": [
                        {
                            "text": {
                                "content": metadata['title']
                            }
                        }
                    ]
                },
                "주제": {
                    "select": {
                        "name": "교육/발표"
                    }
                },
                "중요도": {
                    "select": {
                        "name": "⭐⭐ 중요"
                    }
                },
                "상태": {
                    "select": {
                        "name": "✅ 완료"
                    }
                },
                "태그": {
                    "multi_select": [
                        {"name": "PPT변환"},
                        {"name": metadata['author']}
                    ]
                }
            },
            "children": self.markdown_to_blocks(content[:2000])  # Notion 블록 제한
        }
        
        response = requests.post(url, headers=self.headers, json=data)
        
        if response.status_code == 200:
            page_url = response.json()['url']
            print(f"📝 Notion 업로드 완료: {page_url}")
            return page_url
        else:
            print(f"⚠️ Notion 업로드 실패: {response.text}")
            return None
    
    def markdown_to_blocks(self, content):
        """Markdown을 Notion 블록으로 변환"""
        blocks = []
        
        lines = content.split('\n')
        for line in lines[:50]:  # 처음 50줄만
            line = line.strip()
            if not line:
                continue
            
            if line.startswith('# '):
                blocks.append({
                    "object": "block",
                    "type": "heading_1",
                    "heading_1": {
                        "rich_text": [{"type": "text", "text": {"content": line[2:]}}]
                    }
                })
            elif line.startswith('## '):
                blocks.append({
                    "object": "block",
                    "type": "heading_2",
                    "heading_2": {
                        "rich_text": [{"type": "text", "text": {"content": line[3:]}}]
                    }
                })
            else:
                blocks.append({
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {
                        "rich_text": [{"type": "text", "text": {"content": line[:2000]}}]
                    }
                })
        
        return blocks

# converter.py에서 사용
notion_sync = NotionSync(
    api_key="YOUR_NOTION_API_KEY",
    database_id="YOUR_DATABASE_ID"
)
notion_sync.upload_markdown(output_path, metadata)
```

### Extracted Code (python)

```python
def detect_competency_framework(self, content):
    """내용 기반 역량 프레임워크 자동 감지"""
    
    frameworks = {
        'Leadership': ['리더십', '전략', '비전', '코칭', '영향력'],
        'DX': ['디지털', '자동화', 'AI', '데이터', '혁신'],
        'Communication': ['소통', '협업', '피드백', '커뮤니케이션'],
        'Problem_Solving': ['문제해결', '분석', '의사결정', '논리적']
    }
    
    detected = []
    content_lower = content.lower()
    
    for framework, keywords in frameworks.items():
        if any(keyword in content_lower for keyword in keywords):
            detected.append(framework)
    
    return detected

# frontmatter에 추가
def generate_frontmatter(self, metadata, ppt_path, competencies):
    frontmatter = f"""---
title: "{metadata['title']}"
author: "{metadata['author']}"
created_date: "{metadata['created']}"
slide_count: {metadata['slide_count']}
original_file: "{ppt_path.name}"
document_type: "Presentation"
competency_frameworks: {competencies}
hr_category: "교육자료"
tags:
  - ppt-converted
  - {ppt_path.stem.lower().replace(' ', '-')}
---

"""
    return frontmatter
```

### Extracted Code (markdown)

```markdown
## Phase 1 완료 확인

### 기술 설정
- [ ] Python 환경 구축 완료
- [ ] 필수 라이브러리 설치 완료
- [ ] 폴더 구조 생성 완료
- [ ] OneDrive 동기화 폴더 연결

### 스크립트 구현
- [ ] converter.py 작성 완료
- [ ] 실행 bat 파일 생성
- [ ] 테스트 실행 성공

### 품질 검증
- [ ] 샘플 PPT 3개 변환 테스트
- [ ] 이미지 추출 확인
- [ ] 표 변환 확인
- [ ] 발표자 노트 추출 확인
- [ ] 한글 인코딩 정상

### 연동 설정 (선택)
- [ ] Google Drive rclone 설정
- [ ] Notion API 연동 (선택)
- [ ] 로그 시스템 작동 확인

### 문서화
- [ ] 사용 가이드 작성
- [ ] 트러블슈팅 가이드 작성
- [ ] 변환 품질 기준 문서화
```

### Extracted Code (bash)

```bash
# Python PATH 추가
# 시스템 환경 변수 → Path → Python 설치 경로 추가
# 예: C:\Users\CSP\AppData\Local\Programs\Python\Python311\
```

### Extracted Code (python)

```python
# converter.py 최상단에 추가
# -*- coding: utf-8 -*-
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
```
