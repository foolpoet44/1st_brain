# Extracted Knowledge from Conv: f4b6e95d-fcb5-4b6b-a217-f33c0a13f806

**Date**: 2026-01-17T04:48:14.318811Z

### Extracted Code (text)

```text
Layer 1: 최소 동작 버전 (MVP)
└─ 핵심 기능만 스크립트로 구현
└─ 목표: 작동만 하면 OK
└─ 예: Excel → 분석 → PPT (파이썬 스크립트)

Layer 2: 모듈화 버전
└─ 재사용 가능한 함수/클래스로 분리
└─ 목표: 다른 프로젝트에서도 쓸 수 있게
└─ 예: hr_analyzer.py, report_generator.py

Layer 3: 서비스화 버전
└─ API, 데이터베이스, UI 추가
└─ 목표: 남도 쓸 수 있게
└─ 예: FastAPI + Streamlit 대시보드
```

### Extracted Code (python)

```python
# 당신이 자주 하는 작업들을 템플릿화
my_hr_toolkit/
├── data_loader.py      # Excel, DB, API에서 데이터 읽기
├── analyzer.py         # 통계, 시각화
├── report_maker.py     # PPT, PDF 생성
├── email_sender.py     # 자동 메일 발송
└── templates/          # 재사용 가능한 템플릿들
```

### Extracted Code (python)

```python
# 이런 식으로 추상화
from my_hr_toolkit import HRAnalyzer, ReportGenerator

analyzer = HRAnalyzer("leadership_data.xlsx")
results = analyzer.run_standard_analysis()
report = ReportGenerator(template="leadership_feedback")
report.generate(results, output="report.pptx")
```

### Extracted Code (text)

```text
1. 당신: "리더십 평가 점수를 5점 척도로 정규화하고, 
         팀별 평균을 계산해서 막대 그래프로 보여줘"
2. Claude Code: 구현 코드 생성
3. 당신: 결과 확인 → 도메인 관점에서 검증
4. 피드백 → 개선 반복
```

### Extracted Code (text)

```text
제약 1: Python + pandas + 기본 라이브러리만
제약 2: 복잡한 프레임워크 금지 (Django X, Flask도 고민)
제약 3: 데이터베이스보다 Excel/CSV 우선
제약 4: 클라우드 배포보다 로컬 실행 우선
```

### Extracted Code (python)

```python
# 당신의 가장 자주 하는 작업 3가지를 함수로 만들기
# 예시:
def load_leadership_data(file_path):
    """리더십 평가 데이터 로드 - 표준 포맷"""
    pass

def calculate_team_scores(df):
    """팀별 점수 집계"""
    pass

def generate_feedback_report(scores, template="default"):
    """피드백 리포트 PPT 생성"""
    pass
```

### Extracted Code (text)

```text
1970년대: Waterfall (완성도 우선)
         └─ "완벽한 설계 문서 먼저"
         
2000년대: Agile (가능성 우선)
         └─ "작동하는 소프트웨어가 문서보다 중요"
         
2010년대: Lean Startup (가능성 검증)
         └─ "Build - Measure - Learn"
         
2020년대: AI 시대 (초고속 프로토타이핑)
         └─ "Claude Code로 30분 만에 MVP"
```

### Extracted Code (text)

```text
가능성 확인 단계:
├─ Vibe Coder: 빠른 프로토타입
├─ Psychology: "이게 사용자에게 의미 있을까?" 직관
└─ Analytics: 데이터로 빠르게 검증

완성도 향상 단계:
├─ HR Experiences: 도메인 깊이 추가
├─ Full-stack: 시스템 통합
└─ 17년 노하우: 엣지 케이스 커버
```

### Extracted Code (markdown)

```markdown
## 가능성 검증 (1주 이내)
- [ ] 핵심 기능 1개가 작동하는가?
- [ ] 데이터 입출력이 가능한가?
- [ ] 성능이 견딜 만한가?
- [ ] 내가 이해할 수 있는 코드인가?

✓ 4개 중 3개 통과 → 계속 진행
✗ 2개 이하 → 방향 재검토
```

### Extracted Code (text)

```text
Level 0: 작동 증명 (PoC)
└─ 한 번 돌려보면 됨, 코드 지저분해도 OK

Level 1: 반복 사용 가능
└─ 일주일에 한 번씩 쓸 수 있음

Level 2: 남에게 줄 수 있음
└─ 동료가 README 보고 실행 가능

Level 3: 제품 수준
└─ 고객에게 판매 가능
```

### Extracted Code (python)

```python
# 가능성 확인용 프롬프트
"이 HR 평가 로직을 Python으로 최대한 빠르게 구현해줘.
 지저분해도 상관없어. 일단 작동만 하면 돼."

# 완성도 향상용 프롬프트  
"이 코드를 프로덕션 레벨로 리팩토링해줘.
 - 에러 처리 추가
 - 주석 작성
 - 테스트 케이스 추가
 - 성능 최적화"
```

### Extracted Code (text)

```text
리더십 평가 시스템 구축:
1. 파일럿 프로그램 (가능성)
   └─ 소규모 팀에서 먼저 테스트
2. 피드백 수집 및 개선
3. 전사 확대 (완성도)
   └─ 프로세스 표준화, 매뉴얼 작성
```

### Extracted Code (text)

```text
작은 승리 1: 프로토타입 작동 ✓
└─→ 심리적 에너지 충전
    └─→ 작은 승리 2: 모듈화 완료 ✓
        └─→ 자신감 증가
            └─→ 작은 승리 3: 실전 적용 ✓
```

### Extracted Code (text)

```text
1주차: 프로토타입 작동
└─→ "나 Python으로 이거 만들 수 있네!" (효능감 ↑)
    └─→ 다음 프로젝트에 대한 두려움 감소
        └─→ 더 어려운 도전 시도
```

### Extracted Code (text)

```text
매일/매주 눈에 보이는 진전:
- "오늘 이 함수 완성했어" ✓
- "이번 주 PPT 자동화 작동했어" ✓
- "다음 주는 메일 발송까지 추가해보자"

vs.

3개월 동안 진전 없음:
- "완벽한 아키텍처 설계 중..."
- 눈에 보이는 결과물 없음
- 동기 고갈 → 프로젝트 포기
```

### Extracted Code (text)

```text
Fixed Mindset (고정 마인드셋):
"나는 원래 코딩 재능이 없어"
└─→ 실패 = 능력 부족의 증거
    └─→ 어려운 도전 회피

Growth Mindset (성장 마인드셋):
"코딩은 연습하면 늘어"
└─→ 실패 = 학습의 기회
    └─→ 어려운 도전 환영
```

### Extracted Code (text)

```text
프로토타입 실패:
└─ Fixed: "역시 나는 개발자가 아니야"
└─ Growth: "이 방법은 안 되는구나. 다른 방법 시도해보자"
           └─→ Claude Code 활용
           └─→ 다른 라이브러리 시도
           └─→ 간단한 버전으로 축소
```

### Extracted Code (text)

```text
완성도 우선 (목표가 멀음):
[0%─────────────────100%] ← 11개월 후
└─ "아직 멀었어..." (동기 저하)

가능성 우선 (목표가 가까움):
[0%─50%] ← 1주
└─ "거의 다 왔어!" (가속)
   [50%─70%] ← 2주
   └─ "조금만 더!" (더 가속)
```

### Extracted Code (text)

```text
┌─────────────────────────────────────────┐
│  가능성 우선 (1-2주)                      │
├─────────────────────────────────────────┤
│ Small Wins: 작은 승리 달성              │
│ Self-Efficacy: "나 할 수 있어!" 확인    │
│ Progress: 눈에 보이는 진전               │
│ Goal-Gradient: 목표가 가까워 속도 빠름  │
│ Growth: 실패해도 빠르게 배움            │
└─────────────────────────────────────────┘
         ↓ 심리적 에너지 충전
┌─────────────────────────────────────────┐
│  완성도 향상 (반복)                       │
├─────────────────────────────────────────┤
│ Self-Efficacy: 축적된 자신감으로 도전   │
│ Progress: 계속된 진전이 동기 유지        │
│ Growth: 과정 중심으로 개선              │
│ Small Wins: 각 개선이 또 하나의 승리    │
└─────────────────────────────────────────┘
```

### Extracted Code (text)

```text
자율성: 
└─ "이 방법으로 만들어볼까?" (스스로 결정)
  └─ vs. "회사 표준 프레임워크 써야 해" (강제)

유능감:
└─ 프로토타입 작동 → "나 이거 만들 수 있어!" ✓
  └─ vs. 3개월 후에야 결과 → "내가 잘하고 있는 건가?"

관계성:
└─ Claude Code와 협업, Notion 커뮤니티 공유
  └─ vs. 혼자 끙끙대며 코딩
```
