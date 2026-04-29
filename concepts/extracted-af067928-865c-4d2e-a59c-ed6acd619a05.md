# Extracted Knowledge from Conv: af067928-865c-4d2e-a59c-ed6acd619a05

**Date**: 2026-02-08T23:41:14.166201Z

### Extracted Code (text)

```text
// 상위 조직이 제공하는 Context
interface CompanyOKR {
  objective: "디지털 전환 가속화"
  keyResults: ["AI 활용도 20% 증가"]
}

// 당신이 구현하는 Implementation  
class DepartmentOKR implements CompanyOKR {
  objective: "AX 내재화를 통한 생산성 향상"
  keyResults: [
    "구성원 성숙도 15% 향상",
    "Physical AI Leader 30명 육성",
    "업무 효율 10% 개선"
  ]
}
```

### Extracted Code (python)

```python
# OKR 데이터 모델 (Notion Database)
OKR_Database = {
    "Quarter": "Q1 2026",
    "Objective": "조직 AX 수용성 진단 및 Quick Win 입증",
    "Key_Results": [
        {
            "description": "Survey 완료 및 Pain Point 5개 식별",
            "target": 5,
            "current": 3,
            "progress": 0.6,
            "status": "진행중"
        },
        # ...
    ],
    "Owner": "CSP",
    "Last_Update": "2026-02-09",
    "Blockers": ["IT 리소스 부족", "예산 승인 지연"]
}
```

### Extracted Code (typescript)

```typescript
// OKR 엔티티 구조
interface OKR {
  id: string
  owner: Employee
  quarter: Quarter
  objective: string
  keyResults: KeyResult[]
  alignedTo: OKR[]  // 상위 OKR들
  supporting: OKR[] // 하위 OKR들
  visibility: 'public' | 'team' | 'private'
  status: 'draft' | 'active' | 'completed' | 'archived'
}

interface KeyResult {
  id: string
  description: string
  metric: string
  baseline: number
  target: number
  current: number
  progress: number // 0.0 - 1.0
  lastUpdated: Date
  confidence: 'low' | 'medium' | 'high' // 달성 자신감
  updates: ProgressUpdate[]
}

interface ProgressUpdate {
  date: Date
  value: number
  note: string
  mood: 'on-track' | 'at-risk' | 'blocked'
}
```

### Extracted Code (markdown)

```markdown
Properties:
- 이름 (title): "2026 Q1 - AX 파일럿 성공"
- 분기 (select): Q1 2026, Q2 2026, Q3 2026, Q4 2026
- 담당자 (person): CSP, 팀원A, 팀원B...
- Objective (text): "조직의 AX 수용성 진단 및 Quick Win 입증"
- 상태 (select): Draft, Active, Completed, Archived
- 공개범위 (select): 전사, 부서, 팀, 개인
- 상위OKR (relation → OKR Master): CEO OKR과 연결
- 전체 진척률 (formula): Average(KR 진척률들)
- 마지막 업데이트 (last edited time)
```

### Extracted Code (markdown)

```markdown
Properties:
- 이름 (title): "Survey 완료 및 Pain Point 5개 식별"
- 소속OKR (relation → OKR Master)
- 담당자 (person)
- 측정지표 (text): "식별된 Pain Point 개수"
- Baseline (number): 0
- Target (number): 5
- Current (number): 3
- Progress (formula): Current / Target (자동 계산)
- Confidence (select): 낮음, 보통, 높음
- Mood (select): 순조, 위험, 막힘
- 예상완료일 (date)
```

### Extracted Code (markdown)

```markdown
Properties:
- 제목 (title): "2026-02-09 주간 업데이트"
- KR (relation → Key Results)
- 날짜 (date): 2026-02-09
- 이전값 (number): 2
- 현재값 (number): 3
- 변화량 (formula): 현재값 - 이전값
- 노트 (text): "인터뷰 10건 완료, 공통 패턴 3개 발견"
- Mood (select): 순조, 위험, 막힘
- 블로커 (multi-select): IT리소스, 예산, 인력부족
```

### Extracted Code (python)

```python
# weekly_checkin.py

from notion_client import Client
import datetime

notion = Client(auth="your_token")

def send_weekly_checkin_reminder():
    """모든 Active OKR 담당자에게 업데이트 요청"""
    
    # Active OKR 조회
    okrs = notion.databases.query(
        database_id="OKR_DB_ID",
        filter={"property": "상태", "select": {"equals": "Active"}}
    )
    
    for okr in okrs['results']:
        owner = okr['properties']['담당자']['people'][0]
        
        # Slack 메시지 발송
        send_slack_dm(
            user=owner['id'],
            message=f"""
            📊 주간 OKR 체크인 시간입니다!
            
            OKR: {okr['properties']['Objective']['text']}
            
            5분만 투자해서 업데이트 해주세요:
            1. 각 KR의 현재값 입력
            2. Mood 태깅 (순조/위험/막힘)
            3. 이번 주 배운 점 한 줄
            
            👉 [업데이트 하러 가기]({okr['url']})
            """
        )

# 매주 금요일 오후 3시 실행
schedule.every().friday.at("15:00").do(send_weekly_checkin_reminder)
```

### Extracted Code (python)

```python
# okr_dashboard.py

def generate_team_dashboard(team_name, quarter):
    """팀 전체 OKR 현황 시각화"""
    
    # 해당 팀의 모든 OKR 조회
    okrs = get_team_okrs(team_name, quarter)
    
    dashboard = {
        "전체_진척률": calculate_average_progress(okrs),
        "위험_신호": count_at_risk_krs(okrs),
        "주요_블로커": aggregate_blockers(okrs),
        "이번주_하이라이트": extract_wins(okrs)
    }
    
    # Notion 페이지로 생성
    create_notion_page(
        parent_db="대시보드",
        title=f"{team_name} OKR Dashboard - {quarter}",
        content=render_dashboard(dashboard)
    )
    
    # 팀 Slack 채널에 요약 포스팅
    post_to_slack(
        channel=f"#{team_name}",
        message=f"""
        📈 이번 주 OKR 현황
        
        전체 진척: {dashboard['전체_진척률']:.1%}
        ⚠️ 위험 신호: {dashboard['위험_신호']}개 KR
        🚧 주요 블로커: {', '.join(dashboard['주요_블로커'][:3])}
        
        🎉 이번 주 성과:
        {dashboard['이번주_하이라이트']}
        
        자세히 보기 👉 [대시보드]
        """
    )
```

### Extracted Code (python)

```python
# one_on_one_prep.py

def prepare_1on1_agenda(manager, direct_report, date):
    """1:1 미팅 전 OKR 기반 아젠다 자동 생성"""
    
    # 직원의 현재 OKR 상태 분석
    okrs = get_person_okrs(direct_report)
    analysis = {
        "on_track": [],
        "at_risk": [],
        "blocked": [],
        "recent_wins": [],
        "questions_to_ask": []
    }
    
    for kr in okrs['key_results']:
        if kr['mood'] == '순조' and kr['progress'] > 0.7:
            analysis['on_track'].append(kr)
        elif kr['mood'] == '위험':
            analysis['at_risk'].append(kr)
            analysis['questions_to_ask'].append(
                f"'{kr['description']}'가 위험 신호인데, 무엇이 어려운가요?"
            )
        elif kr['mood'] == '막힘':
            analysis['blocked'].append(kr)
            analysis['questions_to_ask'].append(
                f"'{kr['description']}'의 블로커를 제가 도울 수 있을까요?"
            )
    
    # Notion 1:1 미팅 노트 템플릿 생성
    create_1on1_note(
        title=f"1:1 - {direct_report['name']} - {date}",
        content=f"""
        # OKR 체크인 (10분)
        
        ## 🎉 잘 되고 있는 것
        {format_list(analysis['on_track'])}
        
        ## ⚠️ 관심 필요
        {format_list(analysis['at_risk'])}
        
        ## 🚧 블로커
        {format_list(analysis['blocked'])}
        
        ## 💬 질문 가이드
        {format_list(analysis['questions_to_ask'])}
        
        ---
        
        # 코칭 & 개발 (15분)
        - [ ] 커리어 목표 확인
        - [ ] 스킬 개발 진행상황
        - [ ] 필요한 리소스/지원
        
        # 기타 (5분)
        - [ ] 팀 분위기/관계
        - [ ] 개인적 근황
        """
    )
```
