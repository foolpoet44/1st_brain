# Extracted Knowledge from Conv: 61e74eb1-8992-4b90-8b56-4e7d8bdbbce4

**Date**: 2026-01-08T05:14:14.593490Z

### Extracted Code (text)

```text
[Input Layer]
신년사 문서 (PDF/DOCX/MD)
    ↓
[Analysis Layer] 
Claude 기반 의미 추출 엔진
    ↓
[Ontology Layer]
전략-과제-액션 온톨로지
    ↓
[Planning Layer]
Obsidian 기반 실행계획
    ↓
[Execution Layer]
진척 모니터링 & 피드백
```

### Extracted Code (text)

```text
📁 Strategic-Planning-2025/
│
├── 📁 00-Inbox/              # 원본 문서 수집
│   ├── 신년사-회장-2025.pdf
│   ├── CEO-Letter-2025.md
│   └── 임원-지시사항-Q1.docx
│
├── 📁 01-Strategic-Messages/  # 구조화된 메시지
│   ├── 회장-핵심메시지.md
│   ├── CEO-전략방향.md
│   └── 임원-중점과제.md
│
├── 📁 02-Strategic-Themes/    # 전략 테마 추출
│   ├── DX-Transformation.md
│   ├── AX-Manufacturing.md
│   ├── People-Culture.md
│   └── Business-Innovation.md
│
├── 📁 03-Strategic-Objectives/ # 전략 목표
│   ├── SO-001-스마트팩토리고도화.md
│   ├── SO-002-AI기반자동화.md
│   └── SO-003-조직문화혁신.md
│
├── 📁 04-Key-Initiatives/     # 핵심 과제
│   ├── KI-001-HR-Ontology-System.md
│   ├── KI-002-Leadership-Assessment.md
│   └── KI-003-AX-Academy.md
│
├── 📁 05-Action-Plans/        # 실행계획
│   ├── AP-001-Q1-Plan.md
│   ├── AP-002-Q2-Plan.md
│   └── Weekly-Actions/
│
├── 📁 06-Progress-Tracking/   # 진척 관리
│   ├── Dashboard-2025.md
│   ├── Weekly-Review/
│   └── Monthly-Report/
│
├── 📁 Templates/              # 템플릿
│   ├── strategic-message.md
│   ├── strategic-objective.md
│   ├── key-initiative.md
│   └── action-plan.md
│
└── 📁 Scripts/               # 자동화 스크립트
    ├── extract-messages.py
    ├── generate-ontology.py
    └── sync-to-notion.js
```

### Extracted Code (yaml)

```yaml
---
type: strategic-message
source: CEO | 회장 | 임원
date: 2025-01-01
priority: critical | high | medium
themes: [DX, AX, People, Innovation]
keywords: []
raw-text: "원문 인용"
---
```

### Extracted Code (yaml)

```yaml
---
type: strategic-theme
name: DX Transformation
source-messages: [[CEO-전략방향]], [[회장-핵심메시지]]
objectives: [[SO-001]], [[SO-002]]
owner: DX본부
timeline: 2025-Q1~Q4
---
```

### Extracted Code (yaml)

```yaml
---
type: strategic-objective
id: SO-001
title: 스마트팩토리 고도화
theme: [[DX-Transformation]]
source: [[CEO-전략방향#DX혁신]]
kpis:
  - metric: 자동화율
    target: 95%
    baseline: 78%
initiatives: [[KI-001]], [[KI-002]]
owner: 생산기술팀
---
```

### Extracted Code (yaml)

```yaml
---
type: key-initiative
id: KI-001
title: HR Ontology 기반 자동화 시스템 구축
objective: [[SO-002]]
status: in-progress
priority: P0
timeline:
  start: 2025-01-15
  end: 2025-06-30
milestones:
  - 온톨로지 설계 완료
  - 프로토타입 개발
  - 파일럿 테스트
owner: CSP
team: [HR-DX팀, IT팀]
actions: [[AP-001]], [[AP-002]]
---
```

### Extracted Code (yaml)

```yaml
---
type: action-plan
id: AP-001
title: Q1 HR Ontology 시스템 설계
initiative: [[KI-001]]
quarter: 2025-Q1
status: not-started | in-progress | done | blocked
tasks:
  - [ ] 온톨로지 모델링
  - [ ] 데이터 스키마 설계
  - [ ] 기술 스택 선정
resources: []
blockers: []
---
```

### Extracted Code (python)

```python
# extract-messages.py
"""
신년사 문서에서 핵심 메시지 추출
"""

import anthropic
from pathlib import Path

def analyze_strategic_document(pdf_path):
    client = anthropic.Anthropic()
    
    prompt = """
    다음 신년사 문서를 분석하여 구조화된 전략 정보를 추출해주세요:
    
    1. 핵심 메시지 (3-5개)
    2. 전략 테마 분류 (DX/AX/People/Innovation 등)
    3. 구체적 목표/지표
    4. 추진 과제
    5. 타임라인
    
    출력 형식: YAML frontmatter + Markdown
    """
    
    # Claude API 호출로 문서 분석
    # Obsidian 노트 자동 생성
    pass
```

### Extracted Code (python)

```python
# generate-ontology.py
"""
전략 메시지 → 목표 → 과제 → 액션의 관계 매핑
"""

def build_strategic_ontology(messages_dir):
    # 1. 모든 strategic message 스캔
    # 2. 공통 테마 추출 (NLP/clustering)
    # 3. 계층 구조 생성
    # 4. 관계 링크 자동 생성
    pass
```

### Extracted Code (markdown)

```markdown
# Templates/action-plan.md

## Claude Prompt for Action Planning

당신은 전략 과제를 실행 가능한 액션플랜으로 변환하는 전문가입니다.

**입력**: Key Initiative 문서
**출력**: 분기별 실행계획

다음 구조로 계획을 수립하세요:
1. 목표 분해 (OKR 방식)
2. 주요 마일스톤
3. 주간 액션 아이템
4. 필요 리소스
5. 리스크 & 의존성
6. 성공 지표
```

### Extracted Code (bash)

```bash
# Morning Sync
$ python scripts/sync-progress.py
# → Notion에서 진척 현황 가져오기
# → Obsidian Dashboard 업데이트

# Evening Review
$ python scripts/daily-review.py
# → 오늘 완료된 액션 체크
# → 내일 우선순위 제안
```

### Extracted Code (bash)

```bash
# Weekly Planning (매주 월요일)
$ python scripts/weekly-planning.py
# → 전략 목표 대비 진척률 계산
# → 이번 주 핵심 액션 추출
# → Claude에게 우선순위 검토 요청

# Weekly Review (매주 금요일)
$ python scripts/weekly-review.py
# → 주간 성과 요약
# → 블로커 식별
# → 다음 주 계획 초안 생성
```

### Extracted Code (bash)

```bash
# Monthly Strategic Review
$ python scripts/monthly-review.py
# → 전략 목표별 KPI 현황
# → 신년사 메시지 대비 진척도
# → CEO/임원 보고서 자동 생성
```

### Extracted Code (dataview)

```dataview
TABLE status, priority, owner, progress
FROM "04-Key-Initiatives"
WHERE status != "done"
SORT priority ASC
```

### Extracted Code (javascript)

```javascript
// sync-to-notion.js
/**
 * Obsidian의 전략 데이터를 Notion DB로 동기화
 * 
 * Use Case:
 * - Obsidian: 개인 전략 수립 & 깊은 사고
 * - Notion: 팀 협업 & 진척 공유
 */

async function syncStrategicPlanning() {
  // 1. Obsidian에서 변경된 Strategic Objective 감지
  // 2. Notion DB 업데이트
  // 3. 팀원 알림
}
```

### Extracted Code (text)

```text
Strategic-Planning-2025/
├── 00-Inbox/              # 신년사 원본 수집
├── 01-Strategic-Messages/ # 구조화된 메시지
├── 02-Strategic-Themes/   # 전략 테마
├── 03-Strategic-Objectives/ # 전략 목표
├── 04-Key-Initiatives/    # 핵심 과제
├── 05-Action-Plans/       # 실행계획
├── 06-Progress-Tracking/  # 진척 관리
├── Templates/             # 8개 템플릿
└── Scripts/              # 자동화
```

### Extracted Code (text)

```text
strategic-planning-obsidian/
├── SKILL.md (핵심 가이드)
├── references/
│   ├── vault-structure.md
│   └── workflow-guide.md
├── assets/templates/
│   ├── strategic-message.md
│   ├── strategic-objective.md
│   ├── key-initiative.md
│   ├── action-plan.md
│   ├── weekly-review.md
│   ├── monthly-report.md
│   └── dashboard.md
└── scripts/
    └── setup-vault.sh
```

### Extracted Code (bash)

```bash
cd [다운로드한 폴더 경로]
   git remote add origin https://github.com/YOUR-USERNAME/Strategic-Planning-2025.git
   git push -u origin main
```

### Extracted Code (bash)

```bash
# 1. GitHub에서 먼저 새 리포 생성 (웹에서)
# https://github.com/new
# 이름: Strategic-Planning-2025
# README 초기화 체크 해제!

# 2. 아래 명령어 실행 (YOUR-USERNAME을 본인 GitHub 아이디로 변경)
cd Strategic-Planning-2025
git remote add origin https://github.com/YOUR-USERNAME/Strategic-Planning-2025.git
git push -u origin main
```
