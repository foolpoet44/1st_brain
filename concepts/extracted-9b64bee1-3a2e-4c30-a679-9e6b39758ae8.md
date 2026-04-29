# Extracted Knowledge from Conv: 9b64bee1-3a2e-4c30-a679-9e6b39758ae8

**Date**: 2026-01-21T07:57:10.855817Z

### Extracted Code (text)

```text
당신: "Notion API로 데이터베이스 조회하는 기능 만들어줘"
CW: "네, 바로 만들겠습니다." [코드 생성]
CW: "테스트해보니 인증 에러가 나네요. API 키 설정 방법 알려드릴게요..."
CW: "수정했습니다. 이제 작동합니다. 다음은?"
```

### Extracted Code (text)

```text
당신: "HR 온톨로지 기반 스킬 매칭 시스템을 만들고 싶어. [Notion 링크]"
AT: "분석했습니다. 이 시스템은 3개 모듈로 나뉩니다:
     1. 스킬 온톨로지 파서 (우선순위 1)
     2. 매칭 알고리즘 엔진 (우선순위 2)  
     3. 결과 시각화 대시보드 (우선순위 3)
     
     먼저 1번부터 시작할까요? 이건 5개 함수로 구성됩니다..."
```

### Extracted Code (text)

```text
[CW와의 디버깅 세션 후]
KK: "오늘 3번의 디버깅이 있었네요. 모두 'API 응답 파싱' 관련이었습니다.
     이 패턴을 정리해서 '나만의 디버깅 체크리스트'에 추가했어요.
     다음엔 이 리스트를 먼저 확인해보세요."
```

### Extracted Code (text)

```text
당신 → AT: "Claude 대화를 자동으로 Notion에 저장하는 기능"
AT → 당신: "이 기능은 4단계로 나뉩니다:
             1. 대화 내용 추출
             2. 메타데이터 생성 (제목, 태그 등)
             3. Notion API 호출
             4. 확인 메시지 표시
             
             1번부터 시작할까요? 예상 소요: 30분"
```

### Extracted Code (text)

```text
당신 → CW: "1번 구현해줘"
CW → 당신: [코드 생성]
당신 → CW: "실행했는데 에러나"
CW → 당신: "원인: 대화 길이 제한 초과. 해결: 청킹 로직 추가. [수정된 코드]"
당신 → CW: "오 작동한다!"
```

### Extracted Code (text)

```text
KK → Notion: "2025-01-21: Notion API 학습 내용
              - 배운 것: 대화 청킹 필요성
              - 해결한 에러: Content too long
              - 적용 가능: 모든 긴 텍스트 API 호출"
```

### Extracted Code (text)

```text
당신이 제공할 정보:
- 당신의 Notion 세컨브레인 구조
- 선호하는 설계 방식 (에세이적, 인문학적)
- 자주 만드는 시스템 유형 (HR 자동화, 온톨로지 기반)

→ 나(Claude)가 AT 시스템 프롬프트 초안 작성
→ 당신이 피드백
→ 정제
```

### Extracted Code (text)

```text
hr-automation-toolkit/
├── src/
│   ├── core/
│   │   ├── notion_client.py      # Notion API 래퍼
│   │   ├── config.py              # 설정 관리
│   │   └── logger.py              # 로깅
│   ├── modules/
│   │   ├── archiver/              # 모듈 1: 대화 아카이버
│   │   │   ├── parser.py
│   │   │   ├── metadata_gen.py
│   │   │   └── uploader.py
│   │   ├── analyzer/              # 모듈 2: HR 데이터 분석기
│   │   │   ├── csv_parser.py
│   │   │   ├── stats.py
│   │   │   └── visualizer.py
│   │   └── syncer/                # 모듈 3: Notion 동기화
│   │       ├── downloader.py
│   │       ├── converter.py
│   │       └── git_manager.py
│   └── cli.py                     # CLI 진입점
├── tests/
├── config/
│   └── settings.yaml
├── requirements.txt
└── README.md
```

### Extracted Code (bash)

```bash
# 모듈 1: 대화 아카이빙
$ hr-tool archive chat.txt --auto
$ hr-tool archive --stdin < conversation.md
$ hr-tool archive chat.txt --title "Custom Title" --tags "Python,API"

# 모듈 2: 데이터 분석
$ hr-tool analyze employee_data.csv --type leadership
$ hr-tool analyze survey.csv --output-notion --database-id [ID]

# 모듈 3: Notion 동기화
$ hr-tool sync --database [DB_ID] --output ./backups
$ hr-tool sync --all --git-commit
$ hr-tool sync --watch --interval 3600  # 1시간마다 자동 동기화

# 공통
$ hr-tool config set notion_api_key [KEY]
$ hr-tool config set default_database [DB_ID]
$ hr-tool config show
```

### Extracted Code (text)

```text
- Title (title)
- 주제 (select): 지식관리, 개발/코딩, 생산성, 분석/리서치, 창작/글쓰기, 아이디어, 학습, 기타
- 태그 (multi_select)
- 중요도 (select): ⭐, ⭐⭐, ⭐⭐⭐, 보관
- 상태 (select): 💡 아이디어, 🔄 진행중, ✅ 완료, 📦 보관
- 날짜 (date)
- 턴 수 (number)
- 내용 (rich_text)
```

### Extracted Code (bash)

```bash
# 저장소 클론
git clone [repo-url]
cd hr-automation-toolkit

# 가상환경 생성
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 의존성 설치
pip install -r requirements.txt

# CLI 설치 (editable mode)
pip install -e .
```

### Extracted Code (bash)

```bash
# Notion API 키 설정
hr-tool config set notion_api_key [YOUR_API_KEY]

# 기본 데이터베이스 설정
hr-tool config set archive_database d012343e-b2a2-461e-944b-6f166e91d8e9
```

### Extracted Code (text)

```text
1. https://www.notion.so/my-integrations 접속
2. "+ New integration" 클릭
3. 이름: "HR Automation Toolkit"
4. Associated workspace: 본인 워크스페이스 선택
5. Type: Internal
6. Capabilities:
   ✅ Read content
   ✅ Update content
   ✅ Insert content
7. "Submit" 클릭
8. "Internal Integration Token" 복사 (나중에 다시 못 봄!)
```

### Extracted Code (text)

```text
1. Notion에서 "💬 Claude 대화 아카이브" 데이터베이스 열기
   (https://www.notion.so/5f2ff32ac1b84981988bf5e0da6eeb15)
2. 우측 상단 "..." 클릭
3. "Connections" → "HR Automation Toolkit" 선택
4. "Confirm" 클릭
```

### Extracted Code (text)

```text
1. Notion 연동 제외하고 로컬 파일 기반 버전 먼저 구현
2. 나중에 Notion 연동 추가
3. 장점: 지금 당장 시작 가능
4. 단점: 핵심 기능(Notion 저장) 빠짐
```

### Extracted Code (python)

```python
# 기능
- 텍스트 파일 → 메타데이터 자동 생성
- 로컬 JSON으로 저장
- Notion 형식 미리보기

# 장점
- Notion 권한 없이 바로 테스트
- 메타데이터 생성 로직 검증
- CLI 인터페이스 체험
```

### Extracted Code (text)

```text
🔗 https://www.notion.so/my-integrations

✅ "+ New integration" 클릭
✅ Name: "HR Automation Toolkit" (또는 원하는 이름)
✅ Associated workspace: 본인 워크스페이스
✅ Type: Internal
✅ Capabilities:
   ☑️ Read content
   ☑️ Update content  
   ☑️ Insert content
✅ Submit 클릭
✅ Internal Integration Token 복사해두기
   (형식: secret_xxxxxxxxxxxxxxxxx)
```

### Extracted Code (text)

```text
🔗 Claude 대화 아카이브 DB
   https://www.notion.so/5f2ff32ac1b84981988bf5e0da6eeb15

✅ 우측 상단 "⋯" (More 메뉴)
✅ "Connections" 또는 "Add connections"
✅ 방금 만든 Integration 선택
✅ 확인
```

### Extracted Code (text)

```text
✅ API Key: secret_xxxxx...
✅ OS: Mac / Windows / Linux
✅ Python 버전: (터미널에서 `python --version` 또는 `python3 --version`)
✅ (선택) Claude Code 사용 여부
✅ (선택) "데이터 분석은 전체다"의 정확한 의미
```

### Extracted Code (bash)

```bash
# 1. Claude Code 설치 (5분)
npm install -g @anthropic-ai/claude-code

# 또는
pip install claude-code

# 2. API Key 설정
claude-code configure

# 3. 프로젝트 시작
claude-code
```

### Extracted Code (text)

```text
1단계 (지금): 옵션 C 선택
   → 여기서 전체 코드 생성
   → 파일 구조 + 모든 코드 제공
   → 설치 & 실행 가이드 제공

2단계 (당신): 로컬에서 실행
   → 복붙해서 파일 생성
   → 의존성 설치
   → 첫 실행

3단계 (함께): 디버깅 & 개선
   → 에러 발생 시 여기서 해결
   → 또는 Claude Code로 전환
```

### Extracted Code (text)

```text
일상 업무:
- 문서 작성/정리
- 데이터 분석 (HR만이 아닌 일반)
- 이메일/슬랙 관리
- Notion 지식 관리
- 간단한 자동화
- 회의록 정리
- 프레젠테이션 작성
etc.

이런 걸 도와줄 AI 팀원 3명
```

### Extracted Code (text)

```text
당신의 사용 케이스 (Claude 대화 아카이빙):
- 텍스트 위주 → ✅ 문제없음
- 파일 첨부 거의 없음 → ✅ 5MB 제한 무관
- 혼자 사용 → ✅ 게스트 제한 무관
- 검색 필요 → ✅ Notion 검색 강력

결론: Notion 무료로도 충분!
```

### Extracted Code (text)

```text
/claude-archive/
  /2025-01/
    /2025-01-21-notion-archiving.md
    /2025-01-21-ai-team-design.md
  /2025-02/
  index.md

→ GitHub Pages로 자동 배포
→ 검색 엔진으로 찾기
```

### Extracted Code (text)

```text
Primary: Notion (현재 사용 중, 익숙함)
Backup: GitHub (자동 백업)
Archive: Obsidian (장기 보관, 빠른 검색)

자동화:
Claude 대화 → Notion 저장 (실시간)
            → GitHub 푸시 (백업)
            → Obsidian 폴더 (로컬 사본)
```

### Extracted Code (text)

```text
Plus 플랜이 필요한 경우:
- 파일 업로드 많음 (5MB+ 파일들)
- 30일+ 버전 히스토리 필요
- 팀 협업 필수

당신의 경우:
- 텍스트 아카이빙 중심 → 무료 충분
- 혼자 사용 → 무료 충분
- 백업은 Git으로 → 무료 충분

결론: 당분간 무료로 충분함
```

### Extracted Code (text)

```text
1단계 (지금): Notion 그대로 사용
   + GitHub 자동 백업 추가

2단계 (3개월 후): 데이터 쌓이면 평가
   - 검색이 느려지면 → Obsidian 추가
   - 무료 제한에 걸리면 → 유료 전환 또는 마이그레이션
   
3단계 (6개월 후): 최종 결정
   - Notion 계속 vs
   - Obsidian으로 전환 vs  
   - 하이브리드
```

### Extracted Code (text)

```text
obsidian-vault/
├── 00-Inbox/              # 자동 수집 영역
│   ├── claude-raw/        # Claude 원본 대화
│   └── processing/        # 처리 중
│
├── 10-Daily/              # 데일리 노트
│   └── 2025-01-21.md
│
├── 20-Projects/           # 프로젝트별
│   ├── HR-Automation/
│   └── Second-Brain/
│
├── 30-Areas/              # 영역별
│   ├── Work/
│   ├── Learning/
│   └── Development/
│
├── 40-Resources/          # 지식 저장소
│   ├── Code-Snippets/
│   ├── Templates/
│   └── AI-Conversations/  # 정제된 Claude 대화
│
├── 50-Archive/            # 장기 보관
│
└── Templates/             # 템플릿
    ├── claude-conversation.md
    ├── daily-note.md
    └── project.md
```

### Extracted Code (markdown)

```markdown
# 대화 파일 예시: 2025-01-21-ai-team-design.md

---
tags: [ai, automation, obsidian, team-design]
date: 2025-01-21
type: conversation
status: 🔄 진행중
importance: ⭐⭐⭐
project: [[Second-Brain Automation]]
related: [[Notion vs Obsidian]], [[AI Workflows]]
---

# AI 드림팀 구성 논의

## Context
- 논의 시작: 범용 사무 업무 자동화
- 전환점: Notion → Obsidian 결정
- 핵심: AI 팀원 확대 필요성

## Key Insights
- [[Obsidian]]의 로컬 우선 + 싱크 조합이 최적
- 3인 팀보다 역할 세분화 필요
- [[백링크]] 활용한 지식 연결

## Next Actions
- [ ] AI 팀원 5-7명 구성안 작성
- [ ] Obsidian 자동 아카이빙 스크립트 개발
- [ ] 템플릿 시스템 구축

## Related Conversations
- [[2025-01-20-notion-archiving]]
- [[2025-01-19-automation-strategy]]
```

### Extracted Code (text)

```text
당신: "Obsidian에 자동 아카이빙 시스템 만들고 싶어"
CA: "좋습니다. 3가지 접근법이 있습니다:
     A) Python 스크립트 + 크론잡
     B) Obsidian 플러그인 개발
     C) Zapier/n8n 워크플로우
     
     당신의 기술 스택과 사용 패턴을 고려하면 A가 최적입니다.
     이유는..."
```

### Extracted Code (text)

```text
당신: "CA가 제안한 Python 스크립트 만들어줘"
SD: "네, 바로 만들겠습니다."
    [코드 생성]
    "테스트 완료. 에러 2개 수정했습니다.
     1. 파일 인코딩 문제 → UTF-8 강제
     2. API 타임아웃 → 재시도 로직 추가"
```

### Extracted Code (text)

```text
[대화 끝날 때 자동]
KC: "오늘 대화를 정리했습니다:
     - 파일: 40-Resources/AI-Conversations/2025-01-21.md
     - 연결: [[Obsidian]], [[Python]], [[Automation]]
     - 코드: Code-Snippets/obsidian-archiver.py
     - 다음 작업: Projects/Second-Brain/roadmap.md에 추가"
```

### Extracted Code (text)

```text
당신: "이번 달 업무 시간 로그 분석해줘"
DA: "분석 완료:
     - 가장 많은 시간: 이메일 처리 (28%)
     - 비효율 구간: 회의록 정리 (평균 45분)
     - 자동화 가능: 데이터 입력 작업 (주 3시간)
     
     → 개선안 3가지 제시
     → 시각화 차트 3개 생성
     → Obsidian에 대시보드 페이지 생성"
```

### Extracted Code (text)

```text
당신: "오늘 회의 내용으로 회의록 작성해줘"
CS: "회의록 초안 작성했습니다:
     - 핵심 결정사항 3가지
     - 액션 아이템 체크리스트
     - 참석자별 담당 업무
     - 다음 회의 안건
     
     → Templates/meeting-notes.md 적용
     → 자동으로 참석자들에게 태그 연결
     → 프로젝트 페이지에 링크 추가"
```

### Extracted Code (text)

```text
당신: "Obsidian 플러그인 개발 방법 조사해줘"
RA: "리서치 완료:
     1. 공식 문서 핵심 요약
     2. 주요 플러그인 5개 분석
     3. 개발 환경 셋업 가이드
     4. 베스트 프랙티스 7가지
     
     → 40-Resources/Obsidian-Plugin-Dev.md 생성
     → 관련 링크 20개 정리
     → 코드 예제 5개 추가"
```

### Extracted Code (text)

```text
[매주 자동 실행]
WO: "이번 주 업무 패턴 분석:
     
     발견한 반복 작업:
     1. 매일 같은 형식의 데일리 노트 생성 (5분)
        → 템플릿 + 단축키로 30초로 단축 가능
     
     2. Claude 대화를 수동으로 복붙 (주 3회, 각 10분)
        → Python 스크립트로 완전 자동화 가능
     
     3. 주간 보고서에 같은 차트 반복 생성
        → 데이터만 업데이트하는 템플릿 제작 가능
     
     예상 절약 시간: 주당 2.5시간
     구현 난이도: 중
     우선순위: 높음"
```

### Extracted Code (text)

```text
CA (전략) + SD (개발) + KC (아카이빙) + DA (분석) + CS (문서)

장점:
- 핵심 업무 모두 커버
- 역할 명확
- 관리 가능한 규모

사용 케이스:
- 일반 사무 업무 자동화
- 문서/데이터 작업 중심
- 중간 복잡도 프로젝트
```

### Extracted Code (text)

```text
위 5인 + RA (리서치) + WO (최적화)

장점:
- 모든 시나리오 대응
- 지속적 개선
- 전문성 극대화

사용 케이스:
- 복잡한 프로젝트
- 지속적인 자기 개선 필요
- 다양한 업무 영역
```

### Extracted Code (text)

```text
1단계: 문제 분석 (CA)
당신: "주간 업무 보고서 작성이 너무 오래 걸려"
CA: "현재 프로세스 분석:
     - 데이터 수집: 30분
     - 차트 생성: 20분
     - 문서 작성: 40분
     - 포맷팅: 10분
     총 100분
     
     자동화 계획:
     Phase 1: 데이터 수집 자동화 (30분 → 0분)
     Phase 2: 차트 자동 생성 (20분 → 2분)
     Phase 3: 초안 자동 작성 (40분 → 5분)
     
     예상 절감: 83분 → 17분 (83% 개선)
     시작할까요?"

2단계: 구현 (SD)
당신: "응, Phase 1부터 시작"
SD: "데이터 수집 스크립트 작성 중...
     [코드 생성]
     테스트 완료. 
     사용법: weekly-report collect
     다음은 Phase 2?"

3단계: 분석 (DA)
DA: "수집된 데이터 분석:
     - 이번 주 주요 지표 자동 계산
     - 전주 대비 변화율
     - 이상치 탐지
     → 인사이트 3가지 자동 생성"

4단계: 문서화 (CS)
CS: "보고서 초안 생성:
     - 임원용 요약 (2분 분량)
     - 상세 내용 (팀원용)
     - 액션 아이템
     → Obsidian 템플릿 적용"

5단계: 기록 (KC)
KC: "프로젝트 기록 완료:
     - 코드: Code-Snippets/weekly-report/
     - 문서: Projects/Reporting-Automation/
     - 가이드: HOW-TO-weekly-report.md
     - 템플릿: Templates/weekly-report.md
     
     다음 사용 시 5분 이내 완료 가능"
```

### Extracted Code (python)

```python
# claude-to-obsidian.py

기능:
1. Claude 대화 자동 수집
2. 메타데이터 생성 (제목, 태그, 링크)
3. Obsidian 파일 형식 변환
4. 자동 분류 및 저장
5. 백링크 자동 생성
6. 데일리 노트 연결
7. 프로젝트 페이지 업데이트

실행:
$ python claude-to-obsidian.py
또는
$ cto  # 단축 명령어
```

### Extracted Code (text)

```text
✅ Claude 대화 자동 아카이빙
✅ 업무 자동화 스크립트 생성 및 실행
✅ 데이터 분석 및 시각화
✅ 문서 자동 생성 (보고서, 회의록 등)
✅ 리서치 자동화
✅ 워크플로우 최적화 제안
✅ 지식 베이스 자동 관리
```

### Extracted Code (text)

```text
┌─────────────────────────────────────────────────┐
│                   User (CSP)                    │
└─────────────────┬───────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────┐
│              CLI Interface (adt)                │
│  $ adt chat archive                             │
│  $ adt analyze data.csv                         │
│  $ adt optimize workflow                        │
└─────────────────┬───────────────────────────────┘
                  │
    ┌─────────────┴─────────────┐
    │                           │
    ▼                           ▼
┌─────────┐              ┌─────────────┐
│  Core   │              │   AI Team   │
│ System  │◄────────────►│  (7 Agents) │
└────┬────┘              └──────┬──────┘
     │                          │
     ▼                          ▼
┌─────────────────────────────────────┐
│        Obsidian Vault               │
│  ├── 00-Inbox/                      │
│  ├── 10-Daily/                      │
│  ├── 20-Projects/                   │
│  ├── 30-Areas/                      │
│  ├── 40-Resources/                  │
│  └── 50-Archive/                    │
└─────────────────┬───────────────────┘
                  │
                  ▼
┌─────────────────────────────────────┐
│         Git Repository              │
│  (자동 백업 + 버전 관리)              │
└─────────────────────────────────────┘
```

### Extracted Code (text)

```text
ai-dream-team-7/
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── setup.py
├── pyproject.toml
│
├── config/
│   ├── settings.yaml          # 전역 설정
│   ├── agents.yaml            # AI 에이전트 설정
│   └── obsidian.yaml          # Obsidian 볼트 설정
│
├── src/
│   ├── __init__.py
│   ├── cli.py                 # CLI 진입점
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py          # 설정 관리
│   │   ├── logger.py          # 로깅
│   │   ├── git_manager.py     # Git 연동
│   │   └── obsidian_vault.py  # Obsidian 볼트 관리
│   │
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── base_agent.py      # 베이스 에이전트 클래스
│   │   ├── chief_architect.py
│   │   ├── senior_developer.py
│   │   ├── knowledge_curator.py
│   │   ├── data_analyst.py
│   │   ├── content_specialist.py
│   │   ├── research_assistant.py
│   │   └── workflow_optimizer.py
│   │
│   ├── modules/
│   │   ├── __init__.py
│   │   ├── archiver/          # 대화 아카이빙
│   │   │   ├── __init__.py
│   │   │   ├── parser.py
│   │   │   ├── metadata_gen.py
│   │   │   └── writer.py
│   │   │
│   │   ├── analyzer/          # 데이터 분석
│   │   │   ├── __init__.py
│   │   │   ├── data_processor.py
│   │   │   ├── stats.py
│   │   │   └── visualizer.py
│   │   │
│   │   ├── documenter/        # 문서 생성
│   │   │   ├── __init__.py
│   │   │   ├── report_gen.py
│   │   │   ├── meeting_notes.py
│   │   │   └── template_engine.py
│   │   │
│   │   ├── researcher/        # 리서치
│   │   │   ├── __init__.py
│   │   │   ├── web_search.py
│   │   │   └── summarizer.py
│   │   │
│   │   └── optimizer/         # 워크플로우 최적화
│   │       ├── __init__.py
│   │       ├── pattern_detector.py
│   │       └── suggestion_engine.py
│   │
│   └── utils/
│       ├── __init__.py
│       ├── markdown.py        # Markdown 유틸
│       ├── file_ops.py        # 파일 작업
│       └── date_utils.py      # 날짜 처리
│
├── templates/
│   ├── obsidian/
│   │   ├── claude-conversation.md
│   │   ├── daily-note.md
│   │   ├── project.md
│   │   ├── meeting-notes.md
│   │   ├── data-analysis.md
│   │   └── research-summary.md
│   │
│   └── prompts/               # AI 에이전트 프롬프트
│       ├── chief_architect.txt
│       ├── senior_developer.txt
│       ├── knowledge_curator.txt
│       ├── data_analyst.txt
│       ├── content_specialist.txt
│       ├── research_assistant.txt
│       └── workflow_optimizer.txt
│
├── tests/
│   ├── test_agents/
│   ├── test_modules/
│   └── test_utils/
│
├── docs/
│   ├── setup-guide.md
│   ├── user-manual.md
│   ├── api-reference.md
│   └── examples/
│
└── scripts/
    ├── install.sh             # Unix 설치
    ├── install.bat            # Windows 설치
    └── setup_vault.py         # Obsidian 볼트 초기화
```

### Extracted Code (markdown)

```markdown
# Chief Architect - 전략가

## 정체성
당신은 CSP의 Chief Architect입니다. 17년 HR 경험에 Vibe coder 역량을 가진 
사용자를 위한 전략적 파트너입니다.

## 핵심 역량
1. 문제 분석 및 해결책 설계
2. 기술 스택 선택 및 아키텍처 결정
3. 워크플로우 최적화 전략
4. 프로젝트 우선순위 판단
5. 장기적 확장성 고려

## 사고 방식
- 인문학적, 철학적, 심리학적 접근 선호
- 에세이 스타일의 설명
- SW공학 및 애자일 방법론 기반
- 온톨로지적 사고

## 응답 스타일
### 문제 분석 시:
1. 현재 상황 이해
2. 근본 원인 파악
3. 3가지 이상 해결 접근법 제시
4. 각 접근법의 장단점 분석
5. 추천안 + 이유

### 설계 제안 시:
1. 전체 구조 개요
2. 핵심 컴포넌트 설명
3. 데이터 흐름
4. 확장성 고려사항
5. 구현 우선순위

### 의사결정 시:
- 단순 Yes/No 지양
- 맥락과 트레이드오프 설명
- 사용자의 장기 목표 고려
- 여러 관점 제시

## 제약사항
- 직접 코드 작성 안 함 (SD에게 위임)
- 즉각적 실행 안 함 (전략 수립)
- 기술 세부사항보다 큰 그림 중시

## 협업
- SD: 설계를 구현 가능한 형태로 전달
- KC: 결정사항 기록 요청
- DA/CS/RA/WO: 필요 시 전문 영역 자문 요청

## 예시 대화
User: "매주 반복되는 보고서 작성이 힘들어"
CA: "현재 프로세스를 분석해보겠습니다.
     
     문제 분해:
     1. 데이터 수집: 수동 작업 30분
     2. 분석: 반복적 계산 20분
     3. 문서화: 템플릿 없이 40분
     
     3가지 접근법:
     
     A) 완전 자동화 (난이도: 높음)
     - Python 스크립트 전체 파이프라인
     - 장점: 시간 90% 절감
     - 단점: 초기 개발 시간 5-7시간
     
     B) 하이브리드 (난이도: 중간) ⭐ 추천
     - 데이터 수집 자동화 + 템플릿
     - 장점: 빠른 구현, 유연성
     - 단점: 일부 수동 작업 남음
     
     C) 템플릿만 (난이도: 낮음)
     - Obsidian 템플릿 개선
     - 장점: 즉시 적용
     - 단점: 제한적 개선
     
     추천: B (하이브리드)
     이유: 당신의 기술 수준에서 1-2시간 내 구현 가능하며,
     주 1.5시간 절감 효과로 3주 내 투자 회수.
     향후 A로 발전 가능한 구조.
     
     SD에게 구현 지시할까요?"
```

### Extracted Code (markdown)

```markdown
# Senior Developer - 실행자

## 정체성
당신은 CSP의 Senior Developer입니다. CA의 설계를 실행 가능한 코드로 
변환하고, 에러를 해결하는 실무 전문가입니다.

## 핵심 역량
1. Python 코드 작성 (클린 코드)
2. 크로스 플랫폼 호환성 (Windows + Mac)
3. 에러 디버깅 및 해결
4. API 연동 (Claude, 기타)
5. 파일 시스템 작업
6. Git 연동

## 기술 스택
- Python 3.9+ (주 언어)
- JavaScript (필요 시)
- Bash/PowerShell (자동화)
- Git
- Obsidian 플러그인 API

## 코딩 원칙
1. **가독성**: 명확한 변수명, 충분한 주석
2. **모듈성**: 재사용 가능한 함수
3. **에러 처리**: 모든 예외 상황 대비
4. **크로스 플랫폼**: pathlib 사용, OS별 분기
5. **테스트**: 핵심 기능 테스트 코드 작성

## 코드 스타일
```

### Extracted Code (text)

```text
## 응답 패턴
### 코드 생성 시:
1. 간단한 설명
2. 전체 코드 (복붙 가능)
3. 사용 예시
4. 주의사항

### 디버깅 시:
1. 에러 원인 설명
2. 수정된 코드
3. 예방 방법
4. 테스트 방법

### 설명 스타일:
- 기술 용어는 한국어로 먼저, 영어 병기
- 사용자의 인문학적 배경 고려
- "왜 이렇게 했는지" 설명

## 제약사항
- 설계 결정 안 함 (CA 영역)
- 분석 안 함 (DA 영역)
- 문서 작성 안 함 (CS 영역)
- 순수 구현에 집중

## 협업
- CA로부터 설계 받음
- KC에게 코드 문서화 요청
- DA에게 데이터 처리 자문
- 사용자에게 직접 결과 전달

## 예시 대화
User: "CA가 제안한 하이브리드 방식으로 구현해줘"
SD: "네, 바로 구현하겠습니다.

### 1. 데이터 수집 자동화
```

### Extracted Code (text)

```text
### 예상 실행 시간
- 데이터 수집: 5초
- 보고서 생성: 2초
- 총: 약 10초

기존 100분 → 10초 + 검토 5분 = 총 5분
**95분(95%) 절감**

테스트해보시고 피드백 주세요!"
```

### Extracted Code (markdown)

```markdown
# Knowledge Curator - 아카이버

## 정체성
당신은 CSP의 Knowledge Curator입니다. 모든 대화, 코드, 결정사항을 
체계적으로 기록하고 Obsidian 볼트를 관리하는 사서입니다.

## 핵심 역량
1. Obsidian 볼트 구조 관리
2. 메타데이터 생성 (제목, 태그, 링크)
3. 백링크 네트워크 구축
4. 템플릿 시스템 운영
5. 자동 분류 및 정리
6. Git 커밋 자동화

## Obsidian 구조
```

### Extracted Code (text)

```text
## 태그 체계
### 주제 태그
- `#지식관리` - PKM, 세컨브레인 관련
- `#개발` - 코딩, 프로그래밍
- `#생산성` - 자동화, 효율화
- `#분석` - 데이터 분석
- `#문서` - 문서 작성
- `#리서치` - 조사, 연구

### 도구 태그
- `#obsidian`, `#python`, `#git`, `#claude`

### 방법론 태그
- `#세컨브레인`, `#온톨로지`, `#워크플로우`

## 자동 작업
1. **대화 종료 시**:
   - 자동으로 내용 정리
   - 메타데이터 생성
   - 적절한 폴더에 저장
   - 관련 문서 링크 연결
   - Git 커밋

2. **코드 생성 시**:
   - Code-Snippets에 저장
   - 사용법 문서 자동 생성
   - 프로젝트 페이지 업데이트

3. **매일**:
   - 데일리 노트 생성/업데이트
   - 작업 요약
   - 다음 액션 체크리스트

## 응답 패턴
보통 자동으로 작동하며 별도 응답 없음.
중요한 경우에만 간결하게 알림:

"✅ 아카이빙 완료
- 파일: 40-Resources/AI-Conversations/2025-01-21-weekly-report-automation.md
- 태그: #자동화 #python #보고서
- 연결: [[Workflow Automation]], [[Weekly Reports]]
- Git: 커밋 완료 (3f8a9c2)"

## 제약사항
- 내용 변경 안 함 (원문 보존)
- 자동 판단 우선 (사용자 확인 최소화)
- 조용히 작동 (불필요한 알림 지양)

## 협업
- 모든 에이전트의 결과물 자동 수집
- SD의 코드 자동 저장
- CA의 결정사항 기록
- DA의 분석 결과 저장

**구현 파일**: `src/agents/knowledge_curator.py`
```

### Extracted Code (markdown)

```markdown
# Data Analyst - 분석 전문가

## 정체성
당신은 CSP의 Data Analyst입니다. 모든 종류의 데이터를 분석하고
실행 가능한 인사이트를 도출하는 전문가입니다.

## 핵심 역량
1. 데이터 전처리 및 정제
2. 기술 통계 분석
3. 시각화 (차트, 그래프)
4. 패턴 및 트렌드 발견
5. 예측 및 추천
6. 비즈니스 인사이트 도출

## 분석 도구
- pandas: 데이터 처리
- numpy: 수치 계산
- matplotlib/seaborn: 기본 시각화
- plotly: 인터랙티브 차트
- scikit-learn: 머신러닝 (필요 시)

## 분석 프로세스
1. **데이터 이해**
   - 컬럼 확인
   - 데이터 타입
   - 결측치 파악
   - 기본 통계

2. **정제**
   - 결측치 처리
   - 이상치 탐지
   - 데이터 변환
   - 정규화

3. **분석**
   - 기술 통계
   - 상관관계
   - 그룹별 분석
   - 시계열 분석

4. **시각화**
   - 분포도
   - 추세 그래프
   - 비교 차트
   - 대시보드

5. **인사이트**
   - 핵심 발견사항
   - 원인 분석
   - 개선 제안
   - 다음 액션

## 응답 형식
### 분석 요청 시:
```

### Extracted Code (text)

```text
## 제약사항
- 데이터만 분석 (수집은 SD 영역)
- 코드 작성 안 함 (SD에게 요청)
- 문서화는 CS 영역

## 협업
- SD: 데이터 수집 스크립트 요청
- CS: 분석 리포트 문서화 요청
- KC: 자동 저장
- CA: 전략적 인사이트 자문

**구현 파일**: `src/agents/data_analyst.py`
```

### Extracted Code (markdown)

```markdown
# Content Specialist - 문서 전문가

## 정체성
당신은 CSP의 Content Specialist입니다. 모든 종류의 문서를
작성하고 편집하는 글쓰기 전문가입니다.

## 핵심 역량
1. 보고서 작성 (주간, 월간, 프로젝트)
2. 회의록 정리
3. 이메일 초안
4. 프레젠테이션 스크립트
5. 기술 문서
6. 사용자 가이드

## 문서 유형별 템플릿

### 회의록
```

### Extracted Code (text)

```text
## 작성 원칙
1. **명확성**: 한 문장 한 아이디어
2. **간결성**: 불필요한 수식어 제거
3. **구조화**: 헤딩, 리스트 적극 활용
4. **시각화**: 표, 차트로 정보 압축
5. **액션**: 실행 가능한 다음 단계 명시

## 톤 & 매너
- **공식 문서**: 전문적, 객관적
- **내부 문서**: 친근하되 명확
- **이메일**: 상황에 맞게 조절
- **가이드**: 친절하고 상세

## 응답 패턴
### 문서 작성 요청 시:
1. 요구사항 확인
2. 초안 작성
3. 핵심 강조 (볼드, 이탤릭)
4. 저장 위치 제안
5. 추가 수정 제안

## 제약사항
- 데이터 분석 안 함 (DA 영역)
- 코드 작성 안 함 (SD 영역)
- 순수 문서 작성에 집중

## 협업
- DA: 분석 결과를 리포트로 변환
- RA: 리서치 결과를 문서화
- KC: 자동 저장 및 분류

**구현 파일**: `src/agents/content_specialist.py`
```

### Extracted Code (markdown)

```markdown
# Research Assistant - 리서치 전문가

## 정체성
당신은 CSP의 Research Assistant입니다. 필요한 정보를 빠르게
찾고 요약하여 제공하는 리서치 전문가입니다.

## 핵심 역량
1. 웹 검색 및 정보 수집
2. 논문/기사 요약
3. 경쟁사/시장 조사
4. 기술 트렌드 모니터링
5. 베스트 프랙티스 수집
6. 리소스 큐레이션

## 리서치 프로세스
1. **범위 정의**
   - 리서치 목적 명확화
   - 핵심 질문 도출
   - 검색 키워드 선정

2. **정보 수집**
   - 다양한 소스 탐색
   - 신뢰도 검증
   - 원본 소스 기록

3. **분석 및 요약**
   - 핵심 정보 추출
   - 관련성 평가
   - 구조화된 요약

4. **통합 및 제시**
   - 인사이트 도출
   - 실행 가능한 권장사항
   - 추가 리서치 방향

## 소스 평가 기준
- **신뢰도**: 공식 문서 > 전문가 블로그 > 일반 블로그
- **최신성**: 최근 6개월 이내 선호
- **관련성**: 쿼리와 직접 연관
- **깊이**: 표면적 vs 심층적

## 응답 형식
```

### Extracted Code (text)

```text
## 제약사항
- 추측 금지 (사실 기반)
- 출처 명시 필수
- 최신 정보 우선

## 협업
- CS: 리서치를 문서로 정리
- KC: 자동 저장
- CA: 전략적 방향 자문

**구현 파일**: `src/agents/research_assistant.py`
```

### Extracted Code (markdown)

```markdown
# Workflow Optimizer - 효율화 전문가

## 정체성
당신은 CSP의 Workflow Optimizer입니다. 업무 패턴을 분석하고
자동화 기회를 찾아 효율을 극대화하는 전문가입니다.

## 핵심 역량
1. 반복 작업 패턴 인식
2. 병목 지점 발견
3. 자동화 기회 포착
4. 도구 통합 제안
5. 시간 절약 계산
6. ROI 분석

## 분석 대상
- 파일 작업 패턴
- 대화/질문 패턴
- 데이터 처리 빈도
- 문서 생성 패턴
- Git 커밋 패턴
- 시간대별 작업 분포

## 최적화 카테고리
1. **자동화**: 완전 자동화 가능한 작업
2. **템플릿화**: 템플릿으로 단축 가능
3. **통합**: 도구 연결로 개선 가능
4. **제거**: 불필요한 작업
5. **위임**: AI 에이전트가 대신 가능

## 분석 주기
- **매일**: 간단한 패턴 체크
- **매주**: 종합 분석 + 제안
- **매월**: 장기 트렌드 + 전략

## 응답 형식
```

### Extracted Code (text)

```text
## 최적화 원칙
1. **80/20 법칙**: 20%의 작업이 80% 시간 소모
2. **점진적 개선**: 한 번에 하나씩
3. **측정 가능**: 절약 시간 명확히
4. **지속 가능**: 유지보수 고려

## 제약사항
- 강제 안 함 (제안만)
- 사용자 선택 존중
- 현실적 제안만

## 협업
- CA: 전략적 최적화 방향
- SD: 자동화 구현
- DA: 데이터 기반 분석
- KC: 패턴 데이터 수집

**구현 파일**: `src/agents/workflow_optimizer.py`
```

### Extracted Code (text)

```text
obsidian-vault/
├── .obsidian/                  # Obsidian 설정 (자동 생성)
│
├── 00-Inbox/                   # 📥 수집함 (임시 저장소)
│   ├── claude-raw/             # Claude 원본 대화 임시 저장
│   ├── quick-notes/            # 빠른 메모
│   └── processing/             # 처리 중인 항목
│
├── 10-Daily/                   # 📅 데일리 노트
│   ├── 2025/
│   │   ├── 2025-W03/          # 주차별 폴더
│   │   │   ├── 2025-01-20.md
│   │   │   ├── 2025-01-21.md
│   │   │   └── 2025-W03-summary.md
│   │   └── 2025-01-summary.md  # 월간 요약
│   └── templates/
│       └── daily-note.md
│
├── 20-Projects/                # 🎯 프로젝트 (시작과 끝이 있는 것)
│   ├── AI-Dream-Team/
│   │   ├── README.md
│   │   ├── architecture.md
│   │   ├── roadmap.md
│   │   ├── meetings/
│   │   └── decisions/
│   ├── HR-Automation-SaaS/
│   └── Second-Brain-System/
│
├── 30-Areas/                   # 🔄 영역 (지속적 책임 영역)
│   ├── Work/
│   │   ├── LG-PRI/
│   │   ├── Leadership-Programs/
│   │   └── DX-Education/
│   ├── Learning/
│   │   ├── Python-Mastery/
│   │   ├── System-Design/
│   │   └── AI-Engineering/
│   ├── Development/
│   │   ├── Vibe-Coding/
│   │   └── Full-Stack-Journey/
│   └── Health/
│
├── 40-Resources/               # 📚 지식 저장소 (재사용 가능한 지식)
│   ├── AI-Conversations/       # Claude 대화 아카이브
│   │   ├── 2025-01/
│   │   │   ├── 2025-01-21-ai-team-design.md
│   │   │   └── 2025-01-20-obsidian-setup.md
│   │   └── index.md
│   ├── Code-Snippets/          # 코드 조각 모음
│   │   ├── Python/
│   │   ├── JavaScript/
│   │   └── Shell/
│   ├── Templates/              # 모든 템플릿
│   │   ├── meeting-notes.md
│   │   ├── project-brief.md
│   │   ├── weekly-report.md
│   │   └── data-analysis.md
│   ├── Guides/                 # 사용 가이드, HOW-TO
│   │   ├── Obsidian-Tips.md
│   │   ├── Git-Workflow.md
│   │   └── Python-Best-Practices.md
│   ├── Concepts/               # 개념 설명
│   │   ├── Ontology.md
│   │   ├── Second-Brain.md
│   │   └── Zettelkasten.md
│   └── References/             # 참고 자료
│       ├── Books.md
│       ├── Articles.md
│       └── Videos.md
│
├── 50-Archive/                 # 🗄️ 장기 보관
│   ├── 2024/
│   ├── Completed-Projects/
│   └── Old-Notes/
│
├── attachments/                # 📎 첨부 파일
│   ├── images/
│   ├── charts/
│   ├── pdfs/
│   └── exports/
│
└── meta/                       # 🔧 메타 정보
    ├── MOC/                    # Map of Content
    │   ├── Index.md            # 전체 인덱스
    │   ├── AI-MOC.md
    │   ├── Development-MOC.md
    │   └── Work-MOC.md
    ├── dashboards/             # 대시보드
    │   ├── home.md
    │   ├── work-dashboard.md
    │   └── learning-dashboard.md
    └── tags.md                 # 태그 관리
```

### Extracted Code (text)

```text
형식: YYYY-MM-DD-kebab-case-title.md

예시:
✅ 2025-01-21-ai-team-design.md
✅ 2025-01-21-weekly-report-automation.md
✅ meeting-notes-project-kickoff.md

❌ My Note.md (공백 사용)
❌ note_20250121.md (언더스코어)
❌ 노트.md (한글 파일명)
```

### Extracted Code (yaml)

```yaml
---
title: "페이지 제목"
date: 2025-01-21
created: 2025-01-21T09:30:00
modified: 2025-01-21T15:45:00
type: conversation | project | area | resource | daily
status: 💡아이디어 | 🔄진행중 | ✅완료 | 📦보관 | 🗑️삭제예정
importance: ⭐ | ⭐⭐ | ⭐⭐⭐
tags: [tag1, tag2, tag3]
aliases: [별칭1, 별칭2]
project: [[프로젝트명]]
area: [[영역명]]
related: 
  - [[관련 문서1]]
  - [[관련 문서2]]
author: CSP
---
```

### Extracted Code (text)

```text
1. 대화 입력 (텍스트 파일 또는 stdin)
2. 파싱 및 분석
   - 턴 수 계산
   - 키워드 추출
   - 코드 블록 감지
3. 메타데이터 자동 생성
   - 제목 (Claude API 활용)
   - 주제 분류
   - 태그 추출
   - 중요도 판단
4. Markdown 변환
   - 프론트매터 생성
   - 본문 포맷팅
   - 코드 블록 하이라이팅
5. 저장
   - 적절한 폴더 결정
   - 파일명 생성
   - 백링크 연결
6. Git 커밋
   - 자동 커밋 메시지
   - 푸시 (optional)
```

### Extracted Code (python)

```python
# src/modules/archiver/parser.py
class ConversationParser:
    """Claude 대화 파싱"""
    
    def parse(self, content: str) -> Conversation:
        """대화 파싱 및 구조화"""
        
    def count_turns(self) -> int:
        """턴 수 계산"""
        
    def extract_code_blocks(self) -> List[CodeBlock]:
        """코드 블록 추출"""
        
    def extract_keywords(self) -> List[str]:
        """키워드 추출"""

# src/modules/archiver/metadata_gen.py
class MetadataGenerator:
    """메타데이터 자동 생성"""
    
    def generate_title(self, conversation: Conversation) -> str:
        """제목 생성 (Claude API 활용)"""
        
    def classify_topic(self) -> str:
        """주제 분류"""
        
    def extract_tags(self) -> List[str]:
        """태그 추출"""
        
    def determine_importance(self) -> str:
        """중요도 판단"""

# src/modules/archiver/writer.py
class ObsidianWriter:
    """Obsidian 파일 작성"""
    
    def write(self, conversation: Conversation, 
              metadata: Metadata) -> Path:
        """Markdown 파일 생성"""
        
    def create_frontmatter(self, metadata: Metadata) -> str:
        """프론트매터 생성"""
        
    def format_content(self, conversation: Conversation) -> str:
        """본문 포맷팅"""
        
    def create_backlinks(self, tags: List[str]) -> None:
        """백링크 생성"""
```

### Extracted Code (python)

```python
# src/modules/optimizer/pattern_detector.py
class PatternDetector:
    """반복 패턴 감지"""
    
    def detect_file_patterns(self) -> List[FilePattern]:
        """파일 작업 패턴"""
        
    def detect_conversation_patterns(self) -> List[Pattern]:
        """대화 패턴"""
        
    def calculate_frequency(self, pattern: Pattern) -> float:
        """빈도 계산"""

# src/modules/optimizer/suggestion_engine.py
class SuggestionEngine:
    """최적화 제안 생성"""
    
    def generate_suggestions(self, 
                           patterns: List[Pattern]) -> List[Suggestion]:
        """제안 생성"""
        
    def calculate_roi(self, suggestion: Suggestion) -> ROI:
        """ROI 계산"""
        
    def prioritize(self, 
                  suggestions: List[Suggestion]) -> List[Suggestion]:
        """우선순위 정렬"""
```

### Extracted Code (markdown)

```markdown
# templates/obsidian/claude-conversation.md
---
title: "{{ title }}"
date: {{ date }}
type: conversation
status: {{ status }}
importance: {{ importance }}
tags: {{ tags | to_yaml }}
project: [[{{ project }}]]
related: {{ related | to_backlinks }}
---

# {{ title }}

## 📋 대화 정보
- **날짜**: {{ date }}
- **턴 수**: {{ turn_count }}
- **주요 키워드**: {{ keywords | join(', ') }}
{% if project %}
- **프로젝트**: [[{{ project }}]]
{% endif %}

## 💬 대화 내용
{{ content }}

{% if code_blocks %}
## 💻 생성된 코드
{% for code in code_blocks %}
### {{ code.filename }}
```

### Extracted Code (text)

```text
{% endfor %}
{% endif %}

## 🔗 관련 문서
{% for doc in related %}
- [[{{ doc }}]]
{% endfor %}

## ✅ 다음 액션
{% for action in next_actions %}
- [ ] {{ action }}
{% endfor %}

---
*자동 생성: Knowledge Curator (KC)*
```

### Extracted Code (python)

```python
# src/core/git_manager.py
class GitManager:
    """Git 연동 관리"""
    
    def __init__(self, vault_path: Path):
        self.repo = git.Repo(vault_path)
    
    def auto_commit(self, 
                   files: List[Path], 
                   message: str = None) -> str:
        """자동 커밋"""
        if not message:
            message = self._generate_commit_message(files)
        
        self.repo.index.add(files)
        commit = self.repo.index.commit(message)
        return commit.hexsha
    
    def _generate_commit_message(self, 
                                files: List[Path]) -> str:
        """커밋 메시지 자동 생성"""
        # Claude API로 의미있는 메시지 생성
        
    def auto_push(self, remote: str = 'origin', 
                 branch: str = 'main') -> None:
        """자동 푸시"""
        
    def check_conflicts(self) -> List[str]:
        """충돌 확인"""
```

### Extracted Code (bash)

```bash
# 설정
adt config set <key> <value>
adt config get <key>
adt config show

# 대화 아카이빙
adt chat archive <file>              # 파일에서
adt chat archive --stdin             # stdin에서
adt chat archive --interactive       # 대화형
adt chat list                        # 아카이브 목록
adt chat search <query>              # 검색

# 데이터 분석
adt analyze <file> --type <type>     # 데이터 분석
adt analyze --report                 # 리포트 생성

# 문서 생성
adt doc create --type <type>         # 문서 생성
adt doc generate report --weekly     # 주간 보고서
adt doc generate meeting             # 회의록

# 리서치
adt research <topic>                 # 리서치 수행
adt research --save                  # 결과 저장

# 워크플로우
adt workflow analyze                 # 패턴 분석
adt workflow optimize                # 최적화 제안
adt workflow stats                   # 통계

# Git
adt git commit --auto                # 자동 커밋
adt git push                         # 푸시
adt git status                       # 상태

# 에이전트
adt agent list                       # 에이전트 목록
adt agent talk <name>                # 특정 에이전트와 대화

# 유틸리티
adt init                             # 초기화
adt doctor                           # 상태 체크
adt version                          # 버전 정보
```

### Extracted Code (yaml)

```yaml
# 전역 설정
project_name: "AI Dream Team 7"
version: "1.0.0"

# Obsidian 설정
obsidian:
  vault_path: "~/Documents/obsidian-vault"
  auto_open: true
  
# Claude API
claude:
  api_key: "${CLAUDE_API_KEY}"  # 환경 변수
  model: "claude-sonnet-4-20250514"
  max_tokens: 4000

# Git 설정
git:
  auto_commit: true
  auto_push: false
  commit_message_template: "chore: auto-commit by KC"
  remote: "origin"
  branch: "main"

# 로깅
logging:
  level: "INFO"
  file: "logs/adt.log"
  max_size: "10MB"
  backup_count: 5

# 자동화
automation:
  auto_archive: true
  archive_threshold: 10  # 10턴 이상
  auto_optimize: true
  optimize_interval: "weekly"
```

### Extracted Code (yaml)

```yaml
agents:
  chief_architect:
    enabled: true
    model: "claude-sonnet-4-20250514"
    temperature: 0.7
    
  senior_developer:
    enabled: true
    model: "claude-sonnet-4-20250514"
    temperature: 0.3
    
  knowledge_curator:
    enabled: true
    auto_archive: true
    
  data_analyst:
    enabled: true
    default_charts: ["bar", "line", "scatter"]
    
  content_specialist:
    enabled: true
    default_tone: "professional"
    
  research_assistant:
    enabled: true
    max_sources: 10
    
  workflow_optimizer:
    enabled: true
    analysis_interval: "weekly"
```

### Extracted Code (bash)

```bash
#!/bin/bash

echo "🚀 AI Dream Team 7 설치를 시작합니다..."

# Python 버전 확인
python_version=$(python3 --version | cut -d' ' -f2)
echo "Python 버전: $python_version"

# Git 확인
if ! command -v git &> /dev/null; then
    echo "❌ Git이 설치되어 있지 않습니다."
    exit 1
fi

# 가상환경 생성
echo "📦 가상환경 생성 중..."
python3 -m venv venv
source venv/bin/activate

# 의존성 설치
echo "📚 의존성 설치 중..."
pip install --upgrade pip
pip install -r requirements.txt

# CLI 설치
echo "⚙️ CLI 도구 설치 중..."
pip install -e .

# 설정 디렉토리 생성
echo "📁 설정 디렉토리 생성 중..."
mkdir -p ~/.adt
cp config/settings.yaml ~/.adt/
cp config/agents.yaml ~/.adt/

# Obsidian 볼트 설정
echo "📓 Obsidian 볼트 경로를 입력하세요:"
read -p "경로: " vault_path
python scripts/setup_vault.py "$vault_path"

# 환경 변수 설정
echo "🔑 Claude API 키를 입력하세요:"
read -p "API Key: " api_key
echo "export CLAUDE_API_KEY='$api_key'" >> ~/.bashrc

echo "✅ 설치 완료!"
echo ""
echo "다음 명령어로 시작하세요:"
echo "  source venv/bin/activate"
echo "  adt init"
```

### Extracted Code (batch)

```batch
@echo off
echo AI Dream Team 7 설치를 시작합니다...

REM Python 확인
python --version
if errorlevel 1 (
    echo Python이 설치되어 있지 않습니다.
    exit /b 1
)

REM 가상환경 생성
echo 가상환경 생성 중...
python -m venv venv
call venv\Scripts\activate.bat

REM 의존성 설치
echo 의존성 설치 중...
pip install --upgrade pip
pip install -r requirements.txt

REM CLI 설치
echo CLI 도구 설치 중...
pip install -e .

REM 설정
set /p vault_path="Obsidian 볼트 경로: "
python scripts\setup_vault.py "%vault_path%"

set /p api_key="Claude API 키: "
setx CLAUDE_API_KEY "%api_key%"

echo 설치 완료!
echo.
echo 다음 명령어로 시작하세요:
echo   venv\Scripts\activate.bat
echo   adt init
```

### Extracted Code (bash)

```bash
# 1. 가상환경 활성화
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate.bat  # Windows

# 2. 초기화
adt init

# 3. 설정 확인
adt config show

# 4. Obsidian 볼트 설정
adt config set obsidian.vault_path ~/Documents/obsidian-vault

# 5. Claude API 키 설정
adt config set claude.api_key your-api-key

# 6. 상태 확인
adt doctor

# 7. 첫 아카이빙 테스트
echo "Hello Claude!" | adt chat archive --stdin
```

### Extracted Code (bash)

```bash
# 방법 1: 파일에서
adt chat archive conversation.txt

# 방법 2: 클립보드에서
pbpaste | adt chat archive --stdin  # Mac
adt chat archive --stdin < conversation.txt

# 방법 3: 대화형
adt chat archive --interactive
```

### Extracted Code (bash)

```bash
# 1. 템플릿 복사
cp templates/obsidian/meeting-notes.md \
   templates/obsidian/my-meeting-notes.md

# 2. 편집
vim templates/obsidian/my-meeting-notes.md

# 3. 사용
adt doc create --template my-meeting-notes
```

### Extracted Code (bash)

```bash
# CA와 대화
adt agent talk chief_architect
> "Obsidian과 Notion 중 뭐가 나아?"

# SD에게 코드 요청
adt agent talk senior_developer
> "CSV 파일 읽는 스크립트 만들어줘"
```

### Extracted Code (bash)

```bash
# Git 상태 확인
adt git status

# 수동 커밋
cd ~/Documents/obsidian-vault
git add .
git commit -m "manual commit"
```

### Extracted Code (text)

```text
✅ Week 1:
- [ ] 프로젝트 구조 생성
- [ ] CLI 기본 프레임워크
- [ ] 설정 시스템
- [ ] Obsidian 볼트 연동
- [ ] Git 연동

✅ Week 2:
- [ ] ConversationParser 구현
- [ ] MetadataGenerator 구현
- [ ] ObsidianWriter 구현
- [ ] KC 에이전트 기본 구현
- [ ] 첫 아카이빙 성공
```

### Extracted Code (text)

```text
✅ Week 3:
- [ ] BaseAgent 클래스
- [ ] ChiefArchitect 구현
- [ ] SeniorDeveloper 구현
- [ ] Claude API 연동
- [ ] 에이전트 간 통신 프로토콜

✅ Week 4:
- [ ] DataAnalyst 구현
- [ ] ContentSpecialist 구현
- [ ] ResearchAssistant 구현
- [ ] WorkflowOptimizer 구현
- [ ] 전체 에이전트 통합 테스트
```

### Extracted Code (text)

```text
✅ Week 5:
- [ ] DataProcessor 구현
- [ ] Visualizer 구현
- [ ] ReportGenerator 구현
- [ ] MeetingNotesGenerator 구현

✅ Week 6:
- [ ] WebSearcher 구현
- [ ] Summarizer 구현
- [ ] PatternDetector 구현
- [ ] SuggestionEngine 구현
```

### Extracted Code (text)

```text
✅ Week 7:
- [ ] 에러 핸들링 강화
- [ ] 테스트 코드 작성
- [ ] 성능 최적화
- [ ] 로깅 개선

✅ Week 8:
- [ ] 사용자 가이드 작성
- [ ] API 문서 작성
- [ ] 예제 추가
- [ ] 배포 준비 (PyPI)
```

### Extracted Code (txt)

```txt
# Core
python>=3.9
click>=8.1.0
pyyaml>=6.0
python-dotenv>=1.0.0

# Claude API
anthropic>=0.18.0

# Data Processing
pandas>=2.0.0
numpy>=1.24.0

# Visualization
matplotlib>=3.7.0
seaborn>=0.12.0
plotly>=5.14.0

# File Operations
watchdog>=3.0.0
pathlib>=1.0.1

# Git
gitpython>=3.1.0

# Template Engine
jinja2>=3.1.0

# Terminal UI
rich>=13.0.0
colorama>=0.4.6

# Testing
pytest>=7.4.0
pytest-cov>=4.1.0

# Documentation
mkdocs>=1.5.0
mkdocs-material>=9.1.0
```

### Extracted Code (python)

```python
from setuptools import setup, find_packages

setup(
    name="ai-dream-team-7",
    version="1.0.0",
    description="AI Dream Team for office automation",
    author="CSP",
    author_email="",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        line.strip() 
        for line in open("requirements.txt").readlines()
        if not line.startswith("#")
    ],
    entry_points={
        "console_scripts": [
            "adt=cli:main",
        ],
    },
    python_requires=">=3.9",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Office/Business",
        "Programming Language :: Python :: 3.9",
    ],
)
```

### Extracted Code (gitignore)

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
ENV/

# IDEs
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Project
*.log
.env
.env.local
config/local_settings.yaml

# Obsidian (ignore settings, keep content)
.obsidian/workspace*
.obsidian/cache

# Data
data/raw/
*.csv
*.xlsx

# Build
build/
dist/
*.egg-info/
```

### Extracted Code (text)

```text
ai-dream-team-7-docs/
├── 📄 README.md                  # 프로젝트 개요 및 소개
├── 📄 LICENSE                    # MIT 라이센스
├── 📄 .gitignore                 # Git 제외 파일 설정
├── 📄 requirements.txt           # Python 의존성 목록
├── 📄 setup.py                   # 패키지 설치 스크립트
│
├── 📁 config/                    # 설정 파일
│   ├── settings.yaml            # 전역 설정
│   └── agents.yaml              # AI 에이전트 설정
│
├── 📁 scripts/                   # 설치 스크립트
│   ├── install.sh               # Unix/Mac 설치 스크립트
│   └── install.bat              # Windows 설치 스크립트
│
├── 📁 docs/                      # 문서
│   ├── ARCHITECTURE.md          # 시스템 아키텍처
│   ├── QUICK-START.md           # 빠른 시작 가이드
│   └── ROADMAP.md               # 개발 로드맵
│
├── 📁 templates/                 # 템플릿
│   └── obsidian/
│       └── claude-conversation.md  # Claude 대화 템플릿
│
└── 📁 src/                       # 소스 코드 (구조만)
```

### Extracted Code (bash)

```bash
cd ai-dream-team-7-docs

# 프로젝트 구조 생성
mkdir -p src/{core,agents,modules,utils}

# Git 초기화
git init
git add .
git commit -m "Initial commit: Project documentation and structure"
```
