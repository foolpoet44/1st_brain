# Extracted Knowledge from Conv: 86ebbc3d-efc9-4c0c-bed4-035a66de3cf4

**Date**: 2026-01-04T02:01:13.295611Z

### Extracted Code (text)

```text
CSP-Learning-OS/
├── 📚 knowledge-base/
│   ├── hr-leadership/          # HR 도메인
│   ├── psychology-insights/    # 심리학 통찰
│   ├── data-analytics/         # 분석 기법
│   ├── code-snippets/          # 코드 스니펫
│   └── cross-domain/           # 융합 지식
│
├── 🧠 daily-learning/
│   └── 2025/
│       ├── 01-Jan/
│       │   ├── 2025-01-04.md  # 일일 학습 로그
│       │   └── week-01-review.md
│       └── learning-stats.json # 자동 집계
│
├── 🎓 courses-resources/
│   ├── online-courses/         # 강의 노트
│   ├── books/                  # 독서 노트
│   ├── articles/               # 아티클 큐레이션
│   └── videos/                 # 영상 요약
│
├── 💡 projects/
│   ├── hr-automation/          # HR 자동화 프로젝트
│   ├── ontology-system/        # 온톨로지 시스템
│   └── experiments/            # 실험적 프로젝트
│
├── 🔗 connections/
│   ├── concept-map.md          # 개념 연결 지도
│   ├── skill-ontology.yaml     # 스킬 온톨로지
│   └── learning-graph.json     # 학습 관계 그래프
│
├── 📊 analytics/
│   ├── skill-progress.json     # 스킬 진척도
│   ├── learning-velocity.json  # 학습 속도 추적
│   └── visualizations/         # 대시보드 차트
│
└── 🤖 automation/
    ├── collectors/             # 자동 수집 스크립트
    ├── processors/             # 자동 분류/태깅
    ├── analyzers/              # 학습 패턴 분석
    └── workflows/              # GitHub Actions
```

### Extracted Code (yaml)

```yaml
# .github/workflows/collect-learning.yml
name: Daily Learning Collection

on:
  schedule:
    - cron: '0 21 * * *'  # 매일 밤 9시
  workflow_dispatch:

jobs:
  collect:
    runs-on: ubuntu-latest
    steps:
      # Claude 대화에서 학습 내용 추출
      - name: Fetch Claude Conversations
        run: python automation/collectors/claude_sync.py
      
      # Notion에서 학습 로그 가져오기
      - name: Sync Notion Learning Log
        run: python automation/collectors/notion_sync.py
      
      # 브라우저 북마크에서 읽기 자료 수집
      - name: Collect Reading List
        run: python automation/collectors/bookmark_sync.py
      
      # 자동 분류 및 태깅
      - name: Auto Classify & Tag
        run: python automation/processors/auto_tagger.py
      
      # 스킬 온톨로지 업데이트
      - name: Update Skill Graph
        run: python automation/analyzers/skill_mapper.py
      
      # 일일 리포트 생성
      - name: Generate Daily Report
        run: python automation/analyzers/daily_report.py
      
      # Notion 대시보드 업데이트
      - name: Update Notion Dashboard
        run: python automation/collectors/update_notion.py
```

### Extracted Code (markdown)

```markdown
# 2025-01-04 Learning Log

## 📥 Today's Input
- [ ] Claude 대화 3건 (자동 링크)
- [ ] 아티클 2건 읽음
- [ ] YouTube 강의 1건 시청

## 🧠 Key Insights
### HR Domain
- 리더십 평가 데이터 분석 패턴 발견

### Technical
- Python 자동화 스크립트 최적화 기법

### Cross-Domain
- HR 데이터 + 통계분석의 결합 포인트

## 💻 Code Created
```

### Extracted Code (text)

```text
## 🔗 Connections Made
- 기존 개념: "온톨로지 시스템" ↔ 신규 학습: "지식 그래프 DB"
- 스킬 연결: [Python] + [통계] → [데이터 분석 자동화]

## 📊 Skill Progress
- Python: ████████░░ 80% (+2%)
- HR Analytics: ███████░░░ 70% (+5%)
- 온톨로지: ██████░░░░ 60% (+3%)

## 🎯 Tomorrow's Focus
- [ ] Notion MCP 고급 활용법 탐구
- [ ] 리더십 평가 자동화 스크립트 v2 개발
```

### Extracted Code (yaml)

```yaml
# connections/skill-ontology.yaml
skills:
  hr_domain:
    - name: Leadership Assessment
      level: expert
      linked_to: [psychology, statistics]
      projects: [leadership-evaluation-2025]
      
  technical:
    - name: Python Automation
      level: advanced
      linked_to: [hr_domain, analytics]
      tools: [pandas, notion-sdk]
      
  analytics:
    - name: Statistical Analysis
      level: intermediate
      linked_to: [hr_domain, technical]
      
connections:
  - from: Python Automation
    to: HR Analytics
    type: enables
    strength: 0.9
    
  - from: Psychology
    to: Leadership Assessment
    type: foundation
    strength: 1.0
```

### Extracted Code (python)

```python
# automation/analyzers/learning_graph.py
import networkx as nx
import matplotlib.pyplot as plt

def generate_learning_graph():
    """학습한 개념들의 관계를 자동으로 시각화"""
    G = nx.Graph()
    
    # 일일 로그에서 자동 추출
    concepts = extract_concepts_from_daily_logs()
    
    for concept in concepts:
        G.add_node(concept['name'], 
                   domain=concept['domain'],
                   strength=concept['mastery'])
    
    # 개념 간 연결 자동 감지
    connections = detect_connections(concepts)
    for conn in connections:
        G.add_edge(conn['from'], conn['to'], 
                   weight=conn['strength'])
    
    # 시각화 저장
    visualize_graph(G, 'analytics/visualizations/learning-graph.png')
```

### Extracted Code (markdown)

```markdown
# Weekly Progress Report (Auto-generated)

## 📈 This Week's Stats (2025 W1)
- Total Learning Hours: 12.5h
- Concepts Learned: 8
- Code Written: 450 lines
- Articles Read: 15
- Claude Conversations: 7

## 🚀 Skill Velocity
```

### Extracted Code (text)

```text
## 🎯 Learning Trajectory
Current Path: HR Automation SaaS
Next Milestone: Ontology-based System MVP
Estimated: 3 weeks

## 💡 Cross-Domain Insights
- Discovered: Psychology + Python = HR Prediction Models
- Applied: Statistical Analysis to Leadership Data
- Created: Automated Feedback Generation System
```

### Extracted Code (python)

```python
# automation/analyzers/learning_recommender.py

class LearningRecommender:
    def recommend_next(self, current_skills, goals):
        """
        현재 스킬과 목표를 기반으로 다음 학습 자료 추천
        """
        # 스킬 갭 분석
        gaps = self.analyze_skill_gaps(current_skills, goals)
        
        # GitHub Stars, HN, Reddit에서 관련 자료 수집
        resources = self.collect_resources(gaps)
        
        # 학습 우선순위 자동 계산
        prioritized = self.prioritize_by_impact(resources, gaps)
        
        # Notion '학습 대기열'에 자동 추가
        self.add_to_notion_queue(prioritized)
```

### Extracted Code (bash)

```bash
# 1. Repository 생성 및 구조 설정
gh repo create CSP-Learning-OS --public
cd CSP-Learning-OS
mkdir -p {knowledge-base,daily-learning,courses-resources,projects,connections,analytics,automation}/{hr-leadership,psychology-insights,data-analytics,code-snippets}

# 2. 기본 자동화 스크립트 작성
# - Claude 대화 동기화
# - Notion 연동
# - 일일 템플릿 생성기

# 3. GitHub Actions 워크플로우 설정
```

### Extracted Code (yaml)

```yaml
# HR 도메인 특화 지식 체계
hr_concepts:
  - Leadership Competencies
  - Organizational Development
  - Talent Analytics
  
tech_enablers:
  - Python Automation
  - Statistical Modeling
  - Data Visualization
  
value_creation:
  - Automated Assessment
  - Predictive HR
  - Decision Support Systems
```

### Extracted Code (python)

```python
# 서로 다른 도메인의 융합 포인트 자동 감지
synergy_detector.find_intersections([
    "HR Leadership",
    "Python Automation", 
    "Statistical Analysis"
])
# → "Automated Leadership Assessment System"
```

### Extracted Code (bash)

```bash
# Day 1-2: Repository 구조 + 기본 스크립트
# Day 3-4: Notion 연동 + Claude 동기화
# Day 5-6: GitHub Actions 워크플로우
# Day 7: 첫 주간 리포트 자동 생성 확인
```

### Extracted Code (markdown)

```markdown
# Issue 템플릿: Daily Learning Log

**Title Format**: 📚 2025-01-04 학습 로그

## Labels (자동 추가)
- `daily-log`
- `hr` / `coding` / `analytics` / `psychology`

## 모바일에서 빠른 입력
### 오늘 배운 것
- Claude와 Notion MCP 연동 방법 학습
- Python asyncio 개념 이해

### 코드 스니펫
```

### Extracted Code (markdown)

```markdown
# Category 구조
📂 Knowledge Areas
  ├── HR & Leadership
  ├── Python & Automation
  ├── Data Analytics
  └── Psychology Insights

📂 Projects
  ├── HR Automation SaaS
  └── Ontology System

📂 Ideas
  └── 브레인스토밍
```

### Extracted Code (yaml)

```yaml
# .github/workflows/discussion-to-knowledge.yml
name: Discussion to Knowledge Base

on:
  discussion:
    types: [created, edited]

jobs:
  archive:
    runs-on: ubuntu-latest
    steps:
      - name: Extract Discussion Content
        run: |
          # Discussion 내용을 해당 카테고리 폴더에 저장
          python automation/processors/discussion_parser.py
      
      - name: Update Knowledge Graph
        run: |
          # 개념 연결 자동 업데이트
          python automation/analyzers/concept_linker.py
```

### Extracted Code (text)

```text
📥 To Learn    🔄 Learning    ✅ Learned    📦 Archived
──────────────────────────────────────────────────────
[Issue]        [Issue]        [Issue]       [Issue]
Python         Notion MCP     React         Django
고급 기법        통합 방법        Hooks         ORM

[Issue]        
Ontology
설계 패턴
```

### Extracted Code (text)

```text
🔰 Beginner    💪 Intermediate    🚀 Advanced    ⭐ Expert
────────────────────────────────────────────────────────
Ontology       Python            HR Analytics   Psychology
Design         Automation        

Git Actions                      Statistics
```

### Extracted Code (yaml)

```yaml
# Projects 이벤트를 감지하여 자동 업데이트
on:
  project_card:
    types: [moved]

jobs:
  update-stats:
    runs-on: ubuntu-latest
    steps:
      - name: Update Skill Progress JSON
        run: python automation/analyzers/update_skill_stats.py
      
      - name: Sync to Notion
        run: python automation/collectors/update_notion_dashboard.py
```

### Extracted Code (text)

```text
1. GitHub Mobile 앱 열기
2. "New Issue" → 템플릿 선택: "Daily Plan"
3. 오늘 학습 목표 3가지 작성
4. Label 선택 (hr/coding/analytics)
5. Submit

→ 자동으로 Projects Board에 추가됨
→ Notion에 오늘의 TODO로 싱크됨
```

### Extracted Code (text)

```text
1. 읽은 아티클 발견
2. "New Discussion" → Category: Knowledge Areas
3. 제목: "Notion API 고급 활용법"
4. 핵심 내용 + 링크 붙여넣기
5. Post

→ 자동으로 knowledge-base/articles/에 저장
→ Notion 읽기 목록에 추가
```

### Extracted Code (text)

```text
1. 오늘 작성한 코드가 있다면
2. "New Issue" → 템플릿: "Code Snippet"
3. 코드 + 간단한 설명 작성
4. Label: python/automation
5. Submit

→ 자동으로 code-snippets/ 폴더에 저장
→ 태그 기반 분류
```

### Extracted Code (text)

```text
1. 오늘 Issue 확인
2. "Close Issue" (완료 표시)

→ GitHub Actions가 자동으로:
   - daily-learning/2025/01/에 마크다운 생성
   - Notion 아카이브
   - 주간 통계 업데이트
```

### Extracted Code (yaml)

```yaml
# .github/workflows/issue-to-markdown.yml
name: Daily Log to Markdown

on:
  issues:
    types: [closed]

jobs:
  archive:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Convert Issue to Markdown
        run: |
          python automation/processors/issue_parser.py \
            --issue-number ${{ github.event.issue.number }} \
            --output daily-learning/$(date +%Y/%m)
      
      - name: Extract Code Snippets
        run: |
          python automation/processors/code_extractor.py \
            --issue-number ${{ github.event.issue.number }}
      
      - name: Update Learning Graph
        run: |
          python automation/analyzers/update_graph.py
      
      - name: Commit Changes
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          git add .
          git commit -m "📚 Archive: Issue #${{ github.event.issue.number }}"
          git push
      
      - name: Sync to Notion
        env:
          NOTION_TOKEN: ${{ secrets.NOTION_TOKEN }}
        run: python automation/collectors/notion_sync.py
```

### Extracted Code (python)

```python
# automation/processors/auto_tagger.py
import re
from github import Github

class AutoTagger:
    DOMAIN_KEYWORDS = {
        'hr': ['리더십', '평가', '조직', '인사', 'leadership', 'assessment'],
        'coding': ['python', 'code', '코드', '개발', 'script'],
        'analytics': ['분석', '통계', 'data', 'visualization', '시각화'],
        'psychology': ['심리', '행동', 'psychology', 'behavior']
    }
    
    def detect_labels(self, issue_body):
        """Issue 내용 기반 자동 라벨링"""
        labels = []
        for domain, keywords in self.DOMAIN_KEYWORDS.items():
            if any(kw in issue_body.lower() for kw in keywords):
                labels.append(domain)
        return labels
    
    def extract_code_blocks(self, issue_body):
        """코드 블록 자동 추출"""
        code_pattern = r'
```

### Extracted Code (text)

```text
**모바일에서 보기:**
- 간단한 리스트 뷰로 현재 학습 중인 것 확인
- 카드 클릭 → 상세 내용 확인
- 드래그로 상태 변경

---

## 🎯 Issue/Discussion 템플릿

### Issue 템플릿 1: 일일 학습 로그
```

### Extracted Code (markdown)

```markdown
# 🧠 CSP Learning OS

> **Learning Operating System**: GitHub Mobile 기반 개인 지식관리 시스템

[![GitHub issues](https://img.shields.io/github/issues/yourusername/CSP-Learning-OS)](https://github.com/yourusername/CSP-Learning-OS/issues)
[![GitHub stars](https://img.shields.io/github/stars/yourusername/CSP-Learning-OS)](https://github.com/yourusername/CSP-Learning-OS/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🎯 개념

**"입력은 쉽게, 정리는 자동으로"**

이동 중에도 학습 내용을 30초 만에 기록하면, 자동화가 체계적으로 정리해주는 지식관리 시스템입니다.

### 나는 누구?

**Creative Solution Provider (CSP)**
- 🏢 LG PRI Production Technology HR
- 🧩 HR(17년) × Psychology × Analytics × Full-stack Coding
- 🚀 Vibe Coder: 빠른 프로토타입, 실용적 자동화
- 🎓 목표: HR 자동화 SaaS 창업

### 왜 만들었나?
```

### Extracted Code (text)

```text
---

## ✨ 주요 특징

### 📱 Mobile-First
- GitHub Mobile 앱에서 **30초 만에** 학습 로그 작성
- Issues로 일일 기록, Discussions로 주제별 정리
- Projects Board로 학습 현황 한눈에 파악

### 🤖 자동화 시스템
- Issue 닫으면 → 자동으로 마크다운 파일 생성
- 코드 블록 감지 → 자동 분류 및 태깅
- Notion 대시보드 자동 동기화
- 주간/월간 리포트 자동 생성

### 🧠 지능형 연결
- 개념 간 자동 링크 생성
- 스킬 온톨로지 기반 지식 그래프
- 도메인 간 시너지 자동 감지 (HR × Coding × Analytics)

### 📊 진척도 추적
- 실시간 스킬 레벨 시각화
- 학습 속도(velocity) 자동 계산
- 주간/월간 통계 대시보드

---

## 🏗️ 시스템 아키텍처
```

### Extracted Code (text)

```text
### 2. GitHub Mobile 앱 설치

- [iOS](https://apps.apple.com/app/github/id1477376905)
- [Android](https://play.google.com/store/apps/details?id=com.github.android)

### 3. 첫 학습 로그 작성

1. GitHub Mobile 열기
2. 하단 `+` 버튼 → `New Issue`
3. Template 선택: `Daily Learning Log`
4. 오늘 배운 것 간단히 작성
5. Label 추가: `hr` / `coding` / `analytics` / `psychology`
6. `Submit Issue`

### 4. Projects Board 확인

1. Repository → `Projects` 탭
2. `Learning Pipeline` 보드 열기
3. 방금 만든 Issue가 자동으로 추가됨 ✅

**축하합니다! 🎉 첫 학습 로그가 기록되었습니다.**

---

## 📖 사용 가이드

### 일일 루틴

#### 아침 (출근길)
```

### Extracted Code (text)

```text
### 주간 루틴

**일요일 저녁**
- Projects Board에서 이번 주 학습 리뷰
- 완료된 카드 확인
- 다음 주 학습 목표 Issue 생성

---

## 🗂️ 폴더 구조
```

### Extracted Code (text)

```text
**Custom Fields:**
- `Domain`: HR / Coding / Analytics / Psychology
- `Priority`: 🔥 High / ⭐ Medium / 💤 Low
- `Effort`: 1h / 3h / 1d / 1w
- `Progress`: 0% ~ 100%

### Skill Progress Tracker
```

### Extracted Code (text)

```text
---

## 🔌 Notion 연동 (선택)

### 설정 방법

1. **Notion Integration 생성**
   - [Notion Integrations](https://www.notion.so/my-integrations)
   - `New Integration` 클릭
   - Token 복사

2. **GitHub Secrets 등록**
```

### Extracted Code (text)

```text
3. **Notion 데이터베이스 공유**
   - 아카이브 데이터베이스 생성
   - Integration에 접근 권한 부여

### 동기화 내용
- ✅ 일일 학습 로그
- ✅ 코드 스니펫
- ✅ 주간/월간 통계
- ✅ 스킬 진척도

---

## 📊 대시보드 예시

### 주간 리포트 (자동 생성)
```

### Extracted Code (text)

```text
### 자동화 규칙 조정

`.github/workflows/` 폴더의 YAML 파일 수정

---

## 🗺️ 로드맵

### Phase 1: Foundation ✅
- [x] Repository 구조 설계
- [x] Issue/Discussion 템플릿
- [x] Projects Board 설정
- [x] 기본 README

### Phase 2: Automation (진행 중)
- [ ] Issue → Markdown 자동 변환
- [ ] 코드 스니펫 자동 분류
- [ ] Notion 동기화 스크립트
- [ ] 주간 리포트 자동 생성

### Phase 3: Intelligence (계획)
- [ ] 개념 연결 자동 감지
- [ ] 스킬 온톨로지 시각화
- [ ] AI 기반 학습 자료 추천
- [ ] 학습 패턴 분석

### Phase 4: Integration (미래)
- [ ] Claude 대화 자동 아카이빙
- [ ] Obsidian 연동
- [ ] 학습 그래프 3D 시각화
- [ ] 개인 AI 어시스턴트 학습

---

## 💡 사용 팁

### 모바일 최적화
- Issue 제목은 짧게 (30자 이내)
- 코드 블록은 언어 명시 필수
- Label은 최대 3개까지만 사용
- Comment로 추가 생각 기록

### 검색 활용
```

### Extracted Code (text)

```text
### Projects Board 활용
- 드래그 앤 드롭으로 진행 상황 업데이트
- Milestone으로 중장기 목표 설정
- Filter로 도메인별/우선순위별 보기

---

## 🤝 기여

개인 프로젝트이지만, 아이디어나 개선 사항은 언제든 환영합니다!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자유롭게 사용하세요!

---

## 🙏 감사의 말

- **GitHub**: Mobile-first 플랫폼 제공
- **Notion**: 강력한 데이터베이스와 API
- **Claude**: 지식 정리의 든든한 파트너

---

## 📞 연락처

**CSP (Creative Solution Provider)**
- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com
- Blog: your-blog.com

---

## 🎯 한 줄 요약

> **GitHub Mobile로 30초 입력, 자동화로 평생 자산**

---

<div align="center">

**⭐ 이 프로젝트가 도움이 되셨다면 Star를 눌러주세요!**

Made with ❤️ by CSP | Last Updated: 2025-01-04

</div>
```

### Extracted Code (yaml)

```yaml
blank_issues_enabled: false
contact_links:
  - name: 💬 Discussion
    url: https://github.com/yourusername/CSP-Learning-OS/discussions
    about: 아이디어나 질문은 Discussions에서!
```

### Extracted Code (markdown)

```markdown
# 기여 가이드

## 개발 환경 설정
1. Python 3.9+ 설치
2. `pip install -r requirements.txt`
3. `.env` 파일 생성

## 코딩 스타일
- Black 포매터 사용
- Docstring 필수
- Type hints 권장
```

### Extracted Code (bash)

```bash
# 압축 해제
tar -xzf CSP-Learning-OS.tar.gz

# GitHub Repository 생성
# https://github.com/new

# 업로드
cd CSP-Learning-OS
git init
git add .
git commit -m "🎉 Initial setup"
git remote add origin https://github.com/yourusername/CSP-Learning-OS.git
git push -u origin main
```
