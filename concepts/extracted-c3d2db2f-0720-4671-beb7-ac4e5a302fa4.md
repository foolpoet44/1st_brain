# Extracted Knowledge from Conv: c3d2db2f-0720-4671-beb7-ac4e5a302fa4

**Date**: 2025-12-11T01:03:38.494103Z

### Extracted Code (sql)

```sql
SELECT cust_id, COUNT(*) 
FROM CUST_TXN
WHERE prod_cat_cd IN (스마트폰 관련 코드들)
  AND txn_dt BETWEEN '2024-01-01' AND '2024-12-31'
GROUP BY cust_id
ORDER BY COUNT(*) DESC
```

### Extracted Code (text)

```text
000 컴퓨터과학
  ├─ 005 프로그래밍
  │   ├─ 005.1 프로그래밍 언어
  │   │   ├─ Python
  │   │   └─ Java
  │   └─ 005.7 데이터 관리
  │       └─ SQL
  └─ 006 특수 컴퓨터 방법
      └─ 006.3 인공지능
          └─ 머신러닝
```

### Extracted Code (text)

```text
기술 스킬
├─ 소프트웨어 개발
│   ├─ 프로그래밍 언어
│   │   ├─ Python
│   │   │   ├─ 기초 (변수, 조건문, 반복문)
│   │   │   ├─ 중급 (OOP, 모듈, 패키지)
│   │   │   └─ 고급 (데코레이터, 제너레이터, 멀티스레딩)
│   │   └─ JavaScript
│   │       ├─ ES6+
│   │       └─ TypeScript
│   ├─ 프레임워크
│   │   ├─ Django (requires: Python-중급 이상)
│   │   └─ React (requires: JavaScript-ES6+)
│   └─ 데이터베이스
│       ├─ SQL
│       └─ NoSQL
│
└─ 데이터 분석
    ├─ 통계학
    ├─ 데이터 시각화
    │   └─ Tableau (requires: 통계학-기초)
    └─ 머신러닝
        └─ (requires: Python-중급, 통계학-중급)
```

### Extracted Code (text)

```text
머신러닝 --[requires]--> Python (중급 이상)
머신러닝 --[requires]--> 통계학 (기초 이상)
Django --[requires]--> Python (중급 이상)
```

### Extracted Code (text)

```text
Python --[used_in]--> 데이터 분석
Python --[used_in]--> 웹 개발
Python --[used_in]--> 자동화
SQL --[used_in]--> 데이터 분석
```

### Extracted Code (text)

```text
직원 테이블 (EMPLOYEES)
- emp_id: E001
- name: 김철수
- skills_raw: "파이썬, SQL, 엑셀"

교육 이력 (TRAINING_HISTORY)
- emp_id: E001
- course_name: "Python 기초 과정"
- completion_date: 2023-05-15
- score: 85

프로젝트 참여 (PROJECT_PARTICIPATION)
- emp_id: E001
- project_name: "고객 데이터 분석"
- role: "데이터 분석가"
- tech_stack: "Python, Pandas, SQL"
```

### Extracted Code (text)

```text
개념: 김철수의 Python 스킬

증거 소스:
1. skills_raw에 "파이썬" 명시
2. "Python 기초 과정" 85점으로 수료 (2023년)
3. 프로젝트에서 Python 사용 (2023-2024)

→ 시맨틱 추론:
- 스킬: Python
- 레벨: 중급 (교육 수료 + 실무 프로젝트 경험)
- 신뢰도: 높음 (다중 소스 확인)
- 최종 검증일: 2024-03
```

### Extracted Code (text)

```text
입력 데이터의 다양한 표현:
- "파이썬", "Python", "python", "py"
- "기계학습", "머신러닝", "Machine Learning", "ML"
- "자바스크립트", "JavaScript", "JS", "ECMAScript"

시맨틱 레이어의 정규화:
모두 → "Python" (표준 개념)
모두 → "Machine Learning" (표준 개념)
모두 → "JavaScript" (표준 개념)
```

### Extracted Code (text)

```text
직원 데이터: "Django 프로젝트 6개월 수행"

시맨틱 레이어 추론:
Django --[requires]--> Python (중급)
→ 이 직원은 Python 중급 이상 스킬 보유 (추론됨)
→ 이 직원은 웹 개발 스킬 보유 (추론됨)
→ 이 직원은 OOP 개념 이해 (추론됨)
```

### Extracted Code (text)

```text
질문: "머신러닝을 배우고 싶은데 어디서 시작?"

직원 현재 상태: Python 초급

시맨틱 레이어 추론:
머신러닝 --[requires]--> Python (중급)
머신러닝 --[requires]--> 통계학 (기초)

→ 학습 경로 생성:
1. Python 중급 과정 (선행)
2. 통계학 기초 과정 (선행)
3. 머신러닝 입문 과정
```

### Extracted Code (text)

```text
목표 직무: "데이터 사이언티스트"

직무 요구 스킬 (온톨로지 정의):
- Python (고급)
- SQL (중급)
- 통계학 (고급)
- 머신러닝 (중급)
- 데이터 시각화 (중급)

직원 보유 스킬:
- Python (중급) ← GAP
- SQL (중급) ✓
- 통계학 (기초) ← GAP
- 머신러닝 (없음) ← GAP
- 데이터 시각화 (없음) ← GAP

시맨틱 레이어 추천:
1순위: Python 고급 과정 (기존 기반 확장)
2순위: 통계학 중급 과정 (머신러닝 선행 스킬)
3순위: 데이터 시각화 기초 과정
4순위: 머신러닝 입문 과정
```

### Extracted Code (text)

```text
맥락 1: 웹 개발자 채용
→ Python + Django/Flask 프레임워크 경험 중요
→ 비동기 프로그래밍, API 설계 경험 가산점

맥락 2: 데이터 분석가 채용
→ Python + Pandas/NumPy 경험 중요
→ 통계 라이브러리, Jupyter 사용 경험 가산점

맥락 3: 자동화 엔지니어 채용
→ Python + 스크립팅 경험 중요
→ OS 자동화, DevOps 도구 연동 경험 가산점

시맨틱 레이어가 같은 스킬도 맥락에 맞게 가중치를 조정
```

### Extracted Code (text)

```text
AI 프로젝트 수행 가능
   --[requires]--> 머신러닝 (기초 이상)
   --[requires]--> Python (중급 이상)
   --[beneficial]--> 통계학
   --[beneficial]--> 클라우드 (AWS/GCP)
```

### Extracted Code (text)

```text
직접 매칭: "머신러닝" 스킬 보유자 검색
   
   간접 추론:
   - TensorFlow 사용자 → 딥러닝 → AI 가능
   - scikit-learn 사용자 → 머신러닝 → AI 가능
   - 데이터 과학 프로젝트 경험 → AI 관련 가능성 높음
```

### Extracted Code (text)

```text
1. 박지훈 (머신러닝 고급, 3개 AI 프로젝트 경험) - 매칭도 95%
   2. 이민정 (Python 고급, 통계학 석사, ML 프로젝트 1개) - 매칭도 85%
   3. 최서연 (데이터 분석 2년, scikit-learn 사용) - 매칭도 70%
```

### Extracted Code (text)

```text
풀스택 개발자 (온톨로지 정의)
   ├─ 프론트엔드
   │   ├─ HTML/CSS (필수)
   │   ├─ JavaScript (필수)
   │   └─ React/Vue (선택)
   ├─ 백엔드
   │   ├─ Node.js 또는 Python/Django (필수)
   │   ├─ RESTful API (필수)
   │   └─ 인증/보안 (필수)
   ├─ 데이터베이스
   │   ├─ SQL (필수)
   │   └─ NoSQL (선택)
   └─ DevOps
       ├─ Git (필수)
       ├─ Docker (권장)
       └─ CI/CD (권장)
```

### Extracted Code (text)

```text
보유 스킬:
   - JavaScript (중급)
   - HTML/CSS (기초)
   - Git (기초)
   
   부족 스킬:
   - React/Vue (없음)
   - 백엔드 언어 (없음)
   - 데이터베이스 (없음)
   - API 설계 (없음)
```

### Extracted Code (text)

```text
Phase 1 (병렬 가능):
   - HTML/CSS 중급 과정 (현재 기초 → 중급)
   - JavaScript ES6+ 고급 과정 (현재 중급 → 고급)
   - Git 실전 과정 (현재 기초 → 중급)
   
   Phase 2 (Phase 1 선행 필요):
   - React 기초 과정 (requires: JavaScript 고급)
   - Node.js 백엔드 과정 (requires: JavaScript 고급)
   
   Phase 3 (Phase 2 선행 필요):
   - RESTful API 설계 (requires: 백엔드 기초)
   - SQL 데이터베이스 (독립 학습 가능)
   
   Phase 4 (통합):
   - 풀스택 프로젝트 실습 (모든 스킬 통합)
```

### Extracted Code (text)

```text
"JavaScript 고급으로 올리면 React와 Node.js를 
   동시에 배울 수 있는 기반이 됩니다. 
   여기서 시작하는 걸 추천합니다!"
   
   예상 완료 기간: 8-12개월
   추천 학습 강도: 주 10시간
```

### Extracted Code (text)

```text
프로젝트 스킬 요구 (온톨로지 기반 분석):
   
   핵심 스킬 (Critical):
   - 머신러닝 (고급) - 1명 이상
   - Python (고급) - 2명 이상
   - 데이터 전처리 (중급) - 2명 이상
   
   필수 스킬 (Required):
   - SQL/데이터베이스 (중급) - 1명 이상
   - 통계학 (중급) - 1명 이상
   - 클라우드 (AWS/GCP) (기초) - 1명 이상
   
   선호 스킬 (Preferred):
   - MLOps (기초)
   - API 개발 (중급)
   - 데이터 시각화 (중급)
```

### Extracted Code (text)

```text
후보 A: 박지훈
   - 머신러닝 (고급) ✓✓
   - Python (고급) ✓
   - 통계학 (고급) ✓
   - 팀 리더 경험 (보너스)
   
   후보 B: 김서영  
   - Python (중급) ✓
   - 데이터 전처리 (고급) ✓✓
   - SQL (고급) ✓✓
   - 도메인 지식 (유통업) (보너스)
   
   후보 C: 이준호
   - Python (중급) ✓
   - AWS (중급) ✓✓
   - API 개발 (고급) ✓✓
   - DevOps (중급) (보너스)
   
   시맨틱 분석:
   - 팀 커버리지: 95% (모든 필수 스킬 충족)
   - 스킬 중복도: 적정 (백업 가능)
   - 학습 시너지: 높음 (상호 보완적)
   - 추천: 이 조합 채택
```

### Extracted Code (text)

```text
시스템 모니터링:
- 채용 공고에서 "Rust" 언어가 3개월간 10회 출현
- 기술 블로그에서 "Rust" 언급 증가 추세
- 직원 2명이 자발적으로 "Rust" 학습 기록

시맨틱 레이어 제안:
"Rust를 온톨로지에 추가할까요?"
→ 제안된 위치: 프로그래밍 언어 > 시스템 프로그래밍
→ 유사 스킬: C++, Go
→ 적용 분야: 시스템 프로그래밍, 임베디드, 블록체인
```

### Extracted Code (text)

```text
초기 정의:
React --[similar_to]--> Vue.js (전환 난이도: 중간)

실제 데이터 관찰 (6개월):
- React 개발자 20명 중 15명이 Vue.js를 2주 내 습득
- 평균 학습 시간: 30시간
- 성공률: 75%

시맨틱 레이어 업데이트 제안:
React --[similar_to]--> Vue.js (전환 난이도: 낮음)
신뢰도: 75% (데이터 기반)
```

### Extracted Code (text)

```text
2024년 트렌드 분석:
- "LLM Fine-tuning" 스킬 수요 300% 증가
- "Prompt Engineering" 신규 스킬 부상
- "RAG (Retrieval-Augmented Generation)" 주목

온톨로지 업데이트:
AI/머신러닝
└─ 생성형 AI (신규 카테고리)
    ├─ LLM 활용
    │   ├─ Prompt Engineering (신규)
    │   └─ LLM Fine-tuning (신규)
    └─ RAG 시스템 구축 (신규)
        --[requires]--> 벡터 데이터베이스
        --[requires]--> LLM API 활용
```

### Extracted Code (text)

```text
첫 버전 범위:
- 핵심 직무 3-5개만 집중
- 주요 스킬 50-100개로 시작
- 기본 관계 (선행, 유사) 위주

점진적 확장:
3개월 → 직무 10개, 스킬 200개
6개월 → 직무 20개, 스킬 500개
1년 → 전사 확대
```

### Extracted Code (text)

```text
GIGO (Garbage In, Garbage Out)

좋은 입력:
- "Python (Django 프레임워크 사용, 3년 실무 경험)"
- "머신러닝 (scikit-learn, TensorFlow 활용, 5개 프로젝트)"

나쁜 입력:
- "컴퓨터 잘함"
- "코딩 가능"
```

### Extracted Code (text)

```text
┌─────────────────────────────────────────┐
│     FOUNDRY ONTOLOGY LAYER              │
├─────────────────────────────────────────┤
│                                          │
│  ┌──────────┐      ┌──────────┐         │
│  │ Person   │◄────►│  Skill   │         │
│  │ (직원)   │      │ (스킬)   │         │
│  └──────────┘      └──────────┘         │
│       │                  │               │
│       │                  │               │
│       ▼                  ▼               │
│  ┌──────────┐      ┌──────────┐         │
│  │  Role    │◄────►│ Learning │         │
│  │ (직무)   │      │  Path    │         │
│  └──────────┘      └──────────┘         │
│       │                  │               │
│       │                  │               │
│       ▼                  ▼               │
│  ┌──────────┐      ┌──────────┐         │
│  │ Project  │◄────►│  Course  │         │
│  │(프로젝트)│      │ (교육)   │         │
│  └──────────┘      └──────────┘         │
│                                          │
└─────────────────────────────────────────┘
```

### Extracted Code (typescript)

```typescript
Object Type: Person
Primary Key: employeeId

Properties:
├─ employeeId: String (고유 ID)
├─ name: String
├─ email: String
├─ department: String
├─ level: Enum [Junior, Mid, Senior, Lead, Principal]
├─ joinDate: Date
├─ location: GeoPoint
└─ employmentStatus: Enum [Active, OnLeave, Exited]

Computed Properties (런타임 계산):
├─ skillCount: Integer (보유 스킨 개수)
├─ avgSkillLevel: Double (평균 스킬 레벨)
├─ learningVelocity: Double (학습 속도 지표)
├─ skillDiversity: Double (스킬 다양성 점수)
└─ marketValue: Double (시장 가치 추정)

Links (관계):
├─ possesses → SkillProficiency (여러 개)
├─ enrolledIn → Course (여러 개)
├─ worksOn → Project (여러 개)
├─ reportsTo → Person (1명)
├─ manages → Person (여러 명)
└─ recommendedFor → LearningPath (여러 개)
```

### Extracted Code (typescript)

```typescript
Object Type: Skill
Primary Key: skillId

Properties:
├─ skillId: String (예: "SKILL_PYTHON_001")
├─ name: String (예: "Python")
├─ canonicalName: String (정규화된 이름)
├─ category: Enum [Technical, Business, Soft]
├─ domain: String (예: "Programming Languages")
├─ description: Text
├─ difficultyLevel: Enum [Beginner, Intermediate, Advanced, Expert]
├─ marketDemand: Double (0-100, 외부 API에서 수집)
├─ internalDemand: Integer (사내 채용공고 언급 횟수)
├─ emergingTrend: Boolean (신기술 여부)
├─ deprecationRisk: Double (0-1, 기술 노후화 위험도)
└─ validationMethod: Enum [Certification, Project, Assessment, Peer]

Metadata:
├─ createdAt: Timestamp
├─ updatedAt: Timestamp
├─ dataSource: Array[String] (데이터 출처)
└─ confidence: Double (데이터 신뢰도 0-1)

Computed Properties:
├─ totalProficientEmployees: Integer
├─ avgProficiencyLevel: Double
├─ growthRate: Double (6개월 증가율)
├─ retentionRate: Double (스킬 보유자 이직률)
└─ ROI: Double (교육 투자 대비 효과)

Links:
├─ prerequisiteFor → Skill (여러 개)
├─ requires → Skill (여러 개)
├─ similarTo → Skill (여러 개, weighted)
├─ usedIn → Project (여러 개)
├─ taughtIn → Course (여러 개)
└─ requiredBy → Role (여러 개)
```

### Extracted Code (typescript)

```typescript
Object Type: SkillProficiency
Primary Key: proficiencyId

Properties:
├─ proficiencyId: String
├─ level: Enum [1-Awareness, 2-Novice, 3-Intermediate, 
│              4-Advanced, 5-Expert, 6-Authority]
├─ acquiredDate: Date (스킬 획득 시점)
├─ lastUsedDate: Date (마지막 사용)
├─ lastValidatedDate: Date (마지막 검증)
├─ hoursOfExperience: Integer
├─ projectCount: Integer (이 스킬로 수행한 프로젝트 수)
├─ selfAssessed: Boolean
└─ validationStatus: Enum [Unvalidated, PeerValidated, 
                           ManagerValidated, CertificationValidated]

Evidence (증거 체인):
├─ certifications: Array[Certification]
├─ projectParticipations: Array[Project]
├─ courseCompletions: Array[Course]
├─ assessmentScores: Array[Assessment]
└─ peerEndorsements: Array[Endorsement]

Decay Model (시간 경과에 따른 감쇠):
├─ decayRate: Double (사용하지 않을 때 감쇠율)
├─ halfLife: Integer (숙련도 반감기, 일 단위)
└─ currentProficiency: Double (감쇠 적용된 현재 숙련도)

Links:
├─ person → Person (1명)
├─ skill → Skill (1개)
├─ evidencedBy → Project/Course/Certification (여러 개)
└─ endorsedBy → Person (여러 명)
```

### Extracted Code (typescript)

```typescript
Object Type: Role
Primary Key: roleId

Properties:
├─ roleId: String
├─ title: String (예: "Data Scientist")
├─ level: Enum [Junior, Mid, Senior, Lead, Principal]
├─ family: String (예: "Engineering", "Data", "Product")
├─ description: Text
├─ responsibilities: Array[String]
└─ careerPath: Array[Role] (승진 경로)

Skill Requirements (필수 스킬 매트릭스):
├─ mandatorySkills: Map<Skill, MinLevel>
│   예: {
│     "Python": 4-Advanced,
│     "Machine Learning": 3-Intermediate,
│     "SQL": 3-Intermediate
│   }
├─ preferredSkills: Map<Skill, MinLevel>
└─ niceToHaveSkills: Array[Skill]

Computed Properties:
├─ supplyDemand: Double (공급/수요 비율)
├─ timeToFill: Integer (평균 채용 소요 일수)
├─ candidatePool: Integer (현재 적격 후보 수)
└─ skillGapSize: Double (전체 스킬 갭 크기)

Links:
├─ requires → Skill (여러 개, weighted)
├─ filledBy → Person (여러 명)
├─ progressionTo → Role (여러 개)
├─ similarTo → Role (여러 개)
└─ demandsKnowledgeOf → Domain (여러 개)
```

### Extracted Code (typescript)

```typescript
Object Type: Project
Primary Key: projectId

Properties:
├─ projectId: String
├─ name: String
├─ description: Text
├─ status: Enum [Planning, Active, Completed, OnHold, Cancelled]
├─ startDate: Date
├─ endDate: Date
├─ domain: String (예: "Healthcare", "Finance")
├─ complexity: Enum [Low, Medium, High, Critical]
└─ businessValue: Double

Technical Stack (기술 스택):
├─ requiredSkills: Map<Skill, Importance>
│   예: {
│     "Python": 0.9,  // 0-1 중요도
│     "AWS": 0.7,
│     "React": 0.6
│   }
└─ skillUtilizationHours: Map<Skill, Hours>

Computed Properties:
├─ skillCoverage: Double (팀의 스킬 커버리지 %)
├─ teamFitScore: Double (팀 적합도 점수)
├─ riskScore: Double (스킬 부족 리스크)
└─ learningOpportunity: Array[Skill] (학습 기회)

Links:
├─ usesSkill → Skill (여러 개, weighted)
├─ staffedBy → Person (여러 명, role-specific)
├─ requiresRole → Role (여러 개)
└─ createsLearningFor → Person (여러 명)
```

### Extracted Code (typescript)

```typescript
Object Type: LearningPath
Primary Key: pathId

Properties:
├─ pathId: String
├─ name: String (예: "Beginner to Data Scientist")
├─ targetRole: Role
├─ difficulty: Enum
├─ estimatedDuration: Integer (주 단위)
├─ estimatedEffort: Integer (시간/주)
└─ successRate: Double (완주율)

Curriculum (커리큘럼):
├─ stages: Array[LearningStage]
│   Stage {
│     order: Integer,
│     name: String,
│     skills: Array[Skill],
│     courses: Array[Course],
│     projects: Array[Project],
│     assessments: Array[Assessment],
│     prerequisite: Stage,
│     estimatedDuration: Integer
│   }

Personalization (개인화):
├─ adaptiveRules: Array[Rule]
│   예: "IF Python >= Advanced THEN skip Python-Intro"
└─ fastTrackConditions: Array[Condition]

Computed Properties:
├─ currentEnrollment: Integer
├─ completionRate: Double
├─ avgTimeToComplete: Integer
├─ skillAcquisitionRate: Double
└─ careerProgressionRate: Double (경로 완주 후 승진율)

Links:
├─ targetsRole → Role (1개)
├─ develops → Skill (여러 개)
├─ includes → Course (여러 개, sequenced)
├─ enrolls → Person (여러 명)
└─ prerequisite → LearningPath (0-여러 개)
```

### Extracted Code (typescript)

```typescript
Link Type: Requires (선행 관계)

Properties:
├─ strength: Double (0-1, 얼마나 필수적인가)
├─ minLevel: Integer (최소 요구 레벨)
├─ validatedBy: Array[DataSource]
└─ confidence: Double (관계의 신뢰도)

Example:
Machine Learning --[requires]--> Python
{
  strength: 0.95,
  minLevel: 4,  // Advanced
  validatedBy: ["job_postings", "curriculum_analysis", "expert_input"],
  confidence: 0.92
}

Machine Learning --[requires]--> Statistics
{
  strength: 0.85,
  minLevel: 3,  // Intermediate
  validatedBy: ["curriculum_analysis", "expert_input"],
  confidence: 0.88
}
```

### Extracted Code (typescript)

```typescript
Link Type: SimilarTo (유사 관계)

Properties:
├─ similarityScore: Double (0-1)
├─ transferabilityEase: Enum [Easy, Medium, Hard]
├─ avgTransitionTime: Integer (시간 단위)
├─ commonConcepts: Array[String]
└─ keyDifferences: Array[String]

Example:
React --[similarTo]--> Vue.js
{
  similarityScore: 0.82,
  transferabilityEase: "Easy",
  avgTransitionTime: 40,  // hours
  commonConcepts: ["Component-based", "Virtual DOM", "State Management"],
  keyDifferences: ["Template syntax", "Reactivity model"],
  bidirectional: true
}
```

### Extracted Code (typescript)

```typescript
Link Type: ComplementsWith (보완 관계)

Properties:
├─ synergyScore: Double (0-1, 함께 사용 시 시너지)
├─ coOccurrenceRate: Double (동시 사용 빈도)
├─ rolesThatUseBoth: Array[Role]
└─ typicalCombinations: Array[SkillSet]

Example:
Frontend Development --[complementsWith]--> Backend Development
{
  synergyScore: 0.88,
  coOccurrenceRate: 0.65,
  rolesThatUseBoth: ["Full Stack Developer", "Tech Lead"],
  typicalCombinations: [
    ["React", "Node.js", "MongoDB"],
    ["Vue.js", "Django", "PostgreSQL"]
  ]
}
```

### Extracted Code (python)

```python
# Foundry Pipeline 구조

Pipeline: HR_Data_Integration

├─ Source 1: HRIS (Workday/SAP)
│   ├─ Raw Dataset: employees_raw
│   ├─ Transform: normalize_employee_data
│   └─ Output: Person Objects
│
├─ Source 2: Learning Management System (LMS)
│   ├─ Raw Dataset: course_completions_raw
│   ├─ Transform: extract_skill_evidence
│   └─ Output: SkillProficiency Objects + Course Objects
│
├─ Source 3: Project Management (Jira/Monday)
│   ├─ Raw Dataset: project_assignments_raw
│   ├─ Transform: infer_skills_from_projects
│   └─ Output: Project Objects + SkillProficiency Evidence
│
├─ Source 4: Performance Reviews
│   ├─ Raw Dataset: review_data_raw
│   ├─ Transform: extract_skill_assessments
│   └─ Output: SkillProficiency Validations
│
├─ Source 5: External APIs
│   ├─ LinkedIn Skill Insights API
│   ├─ GitHub Contributions API
│   ├─ Stack Overflow Developer Survey
│   └─ Job Market APIs (Indeed, Glassdoor)
│
└─ Source 6: User Input
    ├─ Self-Assessment Forms
    ├─ Skill Endorsements
    └─ Career Aspirations
```

### Extracted Code (python)

```python
# Palantir Code Repository에서 실행되는 변환

@transform(
    input_dataset=employees_raw,
    output_ontology=Person
)
def create_person_objects(ctx, input_df):
    """
    HRIS 원시 데이터를 Person Object로 변환
    """
    return input_df.transform(
        lambda row: Person(
            employeeId=row['emp_id'],
            name=row['full_name'],
            email=row['email'],
            department=row['dept'],
            level=normalize_level(row['job_level']),
            joinDate=parse_date(row['hire_date']),
            location=geocode(row['office_location']),
            employmentStatus=row['status']
        )
    )


@transform(
    input_datasets=[course_completions_raw, employees_raw],
    output_ontology=[SkillProficiency, Skill]
)
def extract_skills_from_courses(ctx, completions, employees):
    """
    LMS 수료 데이터에서 스킬 증거 추출
    """
    # 강의 이름에서 스킬 추론
    skill_mappings = ctx.ontology.get_reference_data('course_skill_mapping')
    
    results = []
    for completion in completions.iter_rows():
        course_name = completion['course_title']
        employee_id = completion['learner_id']
        
        # NLP를 사용해 강의명에서 스킬 추출
        detected_skills = skill_extractor.extract(course_name)
        
        for skill in detected_skills:
            # Skill Object가 없으면 생성
            skill_obj = ctx.ontology.get_or_create(
                Skill,
                canonicalName=skill.normalized_name
            )
            
            # SkillProficiency 관계 생성
            proficiency = SkillProficiency(
                person=employee_id,
                skill=skill_obj.skillId,
                level=estimate_level_from_course(completion),
                acquiredDate=completion['completion_date'],
                evidencedBy=[completion['course_id']],
                validationStatus='CertificationValidated'
            )
            
            results.append(proficiency)
    
    return results


@transform(
    input_dataset=project_assignments_raw,
    output_ontology=[Project, SkillProficiency]
)
def infer_skills_from_projects(ctx, projects):
    """
    프로젝트 참여에서 스킬 사용 추론
    """
    results = []
    
    for project in projects.iter_rows():
        # 프로젝트 설명/기술스택에서 스킬 추출
        tech_stack = parse_tech_stack(project['description'])
        
        project_obj = Project(
            projectId=project['id'],
            name=project['name'],
            startDate=project['start'],
            endDate=project['end'],
            requiredSkills=tech_stack
        )
        
        # 프로젝트 참여자들의 스킬 숙련도 업데이트
        for member in project['team_members']:
            for skill, importance in tech_stack.items():
                # 기존 SkillProficiency 찾기 또는 생성
                proficiency = ctx.ontology.get_or_create(
                    SkillProficiency,
                    person=member,
                    skill=skill
                )
                
                # 프로젝트 경험 추가
                proficiency.projectCount += 1
                proficiency.hoursOfExperience += estimate_hours(
                    project['start'], 
                    project['end'],
                    member['allocation']
                )
                proficiency.lastUsedDate = max(
                    proficiency.lastUsedDate,
                    project['end']
                )
                
                # 레벨 상향 판단
                if should_level_up(proficiency):
                    proficiency.level = increase_level(proficiency.level)
                
                results.append(proficiency)
    
    return results
```

### Extracted Code (python)

```python
# Foundry Stream Processing

@streaming_transform(
    source=kafka_topic('hr_events'),
    output_ontology=SkillProficiency
)
def process_skill_updates_realtime(ctx, event_stream):
    """
    실시간 스킬 업데이트 처리
    """
    for event in event_stream:
        if event.type == 'CERTIFICATION_EARNED':
            # 즉시 SkillProficiency 업데이트
            update_proficiency(
                person=event.employee_id,
                skill=event.skill_id,
                level='CertificationValidated',
                evidence=event.certification_id
            )
            
            # 관련 추천 재계산 트리거
            ctx.trigger_recomputation(
                'learning_path_recommendations',
                person=event.employee_id
            )
        
        elif event.type == 'PROJECT_STARTED':
            # 프로젝트 시작 시 스킬 사용 추적 시작
            track_skill_usage(
                person=event.employee_id,
                project=event.project_id,
                skills=event.required_skills
            )
```

### Extracted Code (python)

```python
# Person Object의 Computed Property 정의

@computed_property(object_type=Person)
def skill_diversity(person: Person) -> float:
    """
    스킬 다양성 점수 계산
    0: 한 분야만 / 1: 매우 다양한 스킬
    """
    proficiencies = person.possesses  # Link를 통해 SkillProficiency 가져옴
    
    if not proficiencies:
        return 0.0
    
    # 스킬 카테고리별 분포
    categories = {}
    for prof in proficiencies:
        skill = prof.skill
        cat = skill.category
        categories[cat] = categories.get(cat, 0) + 1
    
    # Shannon Entropy로 다양성 측정
    total = len(proficiencies)
    entropy = 0
    for count in categories.values():
        p = count / total
        entropy -= p * math.log2(p)
    
    # 정규화 (0-1)
    max_entropy = math.log2(len(SkillCategory))
    return entropy / max_entropy if max_entropy > 0 else 0


@computed_property(object_type=Person)
def learning_velocity(person: Person) -> float:
    """
    학습 속도: 최근 6개월간 획득한 스킬 숙련도 증가율
    """
    six_months_ago = datetime.now() - timedelta(days=180)
    
    recent_proficiencies = [
        prof for prof in person.possesses
        if prof.acquiredDate >= six_months_ago
        or prof.lastValidatedDate >= six_months_ago
    ]
    
    total_level_gain = sum(
        prof.level for prof in recent_proficiencies
    )
    
    # 시간 가중 평균
    return total_level_gain / 6.0  # 월평균


@computed_property(object_type=Person)
def market_value(person: Person) -> float:
    """
    예상 시장 가치 (상대적 점수)
    """
    # 보유 스킬의 시장 수요 가중합
    proficiencies = person.possesses
    
    value = 0
    for prof in proficiencies:
        skill = prof.skill
        skill_value = (
            skill.marketDemand *  # 시장 수요
            (prof.level / 6) *  # 숙련도 (1-6)
            (1 if prof.validationStatus == 'CertificationValidated' else 0.7)
        )
        value += skill_value
    
    # 스킬 다양성 보너스
    value *= (1 + person.skill_diversity * 0.2)
    
    # 희소 스킬 보너스
    rare_skills = [
        prof for prof in proficiencies
        if prof.skill.totalProficientEmployees < 10
    ]
    value *= (1 + len(rare_skills) * 0.1)
    
    return value


@computed_property(object_type=Skill)
def growth_rate(skill: Skill) -> float:
    """
    스킬 성장률: 6개월 전 대비 숙련자 증가율
    """
    six_months_ago = datetime.now() - timedelta(days=180)
    
    current_count = skill.totalProficientEmployees
    
    # 6개월 전 스냅샷 (타임 시리즈 데이터)
    historical = ctx.time_series.get(
        object=skill,
        property='totalProficientEmployees',
        timestamp=six_months_ago
    )
    
    if historical == 0:
        return float('inf') if current_count > 0 else 0
    
    return (current_count - historical) / historical


@computed_property(object_type=Role)
def candidate_pool(role: Role) -> int:
    """
    현재 이 역할에 적합한 후보 수
    """
    mandatory = role.mandatorySkills
    preferred = role.preferredSkills
    
    # 모든 직원 검색
    candidates = 0
    for person in ctx.ontology.get_all(Person):
        if person.employmentStatus != 'Active':
            continue
        
        # 필수 스킬 체크
        has_all_mandatory = all(
            person.has_skill(skill, min_level)
            for skill, min_level in mandatory.items()
        )
        
        if has_all_mandatory:
            # 선호 스킬 몇 개 있는지 체크
            preferred_count = sum(
                1 for skill in preferred
                if person.has_skill(skill)
            )
            
            # 선호 스킬 50% 이상이면 후보로 인정
            if preferred_count >= len(preferred) * 0.5:
                candidates += 1
    
    return candidates
```

### Extracted Code (typescript)

```typescript
// Action 정의

Action: RecommendLearningPath
Applies to: Person
Triggers when: skill_gap_detected OR career_aspiration_set

Implementation:
function recommendLearningPath(person: Person, targetRole?: Role) {
    // 1. 목표 설정
    let goal: Role;
    if (targetRole) {
        goal = targetRole;
    } else {
        // 자동으로 다음 커리어 단계 추천
        goal = inferNextCareerStep(person);
    }
    
    // 2. 현재 상태 분석
    const currentSkills = person.possesses.map(p => ({
        skill: p.skill,
        level: p.level
    }));
    
    // 3. 스킬 갭 분석
    const gaps = analyzeSkillGap(currentSkills, goal.mandatorySkills);
    
    // 4. 학습 경로 생성
    const path = generateOptimalPath(
        currentState: currentSkills,
        targetState: goal.mandatorySkills,
        constraints: {
            maxDuration: person.preferredLearningDuration,
            learningStyle: person.learningStyle,
            availableTime: person.availableHoursPerWeek
        }
    );
    
    // 5. 개인화
    path.personalize({
        skipKnownContent: true,
        preferredFormat: person.preferredLearningFormat,
        budgetConstraint: person.department.trainingBudget
    });
    
    // 6. 예측
    const prediction = predictOutcome(person, path);
    
    return {
        path: path,
        estimatedDuration: prediction.duration,
        successProbability: prediction.probability,
        expectedRoleReadiness: prediction.readiness,
        investment: path.totalCost,
        roi: calculateROI(path, goal)
    };
}


Action: OptimizeTeamComposition
Applies to: Project
Triggers when: project_created OR team_member_added/removed

Implementation:
function optimizeTeam(project: Project, constraints: Constraints) {
    // 1. 프로젝트 스킬 요구사항 분석
    const requiredSkills = project.requiredSkills;  // Map<Skill, Importance>
    
    // 2. 후보자 풀 생성
    const availablePeople = ctx.ontology.query(Person)
        .filter(p => p.employmentStatus === 'Active')
        .filter(p => p.availableCapacity > 0);
    
    // 3. 각 후보의 적합도 계산
    const scoredCandidates = availablePeople.map(person => ({
        person: person,
        skillMatch: calculateSkillMatch(person, requiredSkills),
        availability: person.availableCapacity,
        learningOpportunity: calculateLearning Opportunity(person, project),
        teamDiversity: calculateDiversityImpact(person, currentTeam),
        riskScore: calculateRiskScore(person, project)
    }));
    
    // 4. 조합 최적화 (정수 계획법)
    const optimalTeam = solve_ILP({
        candidates: scoredCandidates,
        constraints: {
            minTeamSize: constraints.minSize,
            maxTeamSize: constraints.maxSize,
            budgetLimit: constraints.budget,
            requiredSkillCoverage: 0.95,  // 95% 스킬 커버리지
            diversityMinimum: 0.6  // 팀 다양성 최소 기준
        },
        objective: 'maximize_team_effectiveness'
    });
    
    // 5. 추천과 함께 인사이트 제공
    return {
        recommendedTeam: optimalTeam.members,
        skillCoverage: optimalTeam.coverage,
        estimatedEffectiveness: optimalTeam.score,
        gaps: optimalTeam.remainingGaps,
        alternatives: optimalTeam.alternativeTeams.slice(0, 3),
        risks: identifyRisks(optimalTeam),
        mitigations: suggestMitigations(optimalTeam.gaps)
    };
}


Action: DetectSkillDecay
Applies to: SkillProficiency
Triggers when: skill_not_used_threshold_days

Implementation:
function detectAndAlertSkillDecay(proficiency: SkillProficiency) {
    const skill = proficiency.skill;
    const person = proficiency.person;
    const daysSinceLastUse = (Date.now() - proficiency.lastUsedDate) / (1000*60*60*24);
    
    // 스킬별 감쇠 모델 적용
    const decayModel = skill.decayModel || DEFAULT_DECAY_MODEL;
    const halfLife = decayModel.halfLife;
    
    // 현재 예상 숙련도
    const decayFactor = Math.pow(0.5, daysSinceLastUse / halfLife);
    const currentEffectiveProficiency = proficiency.level * decayFactor;
    
    // 임계값 이하로 떨어졌으면 알림
    if (currentEffectiveProficiency < 3 && proficiency.level >= 4) {
        return {
            alert: true,
            message: `${person.name}님의 ${skill.name} 스킬이 미사용으로 인해 감소했을 수 있습니다.`,
            recommendation: [
                `리프레셔 코스: ${findRefresherCourse(skill)}`,
                `관련 프로젝트: ${findProjectOpportunities(skill)}`,
                `멘토링 제안: 후배에게 가르치면서 복습하기`
            ],
            urgency: calculateUrgency(skill, person)
        };
    }
    
    return { alert: false };
}


Action: IdentifyEmergingSkills
Applies to: Organization
Triggers when: scheduled_monthly

Implementation:
function identifyEmergingSkills() {
    // 1. 외부 시장 데이터 수집
    const marketTrends = fetchMarketData([
        'linkedin_skill_insights',
        'stackoverflow_survey',
        'github_trending',
        'job_postings_analysis'
    ]);
    
    // 2. 내부 데이터 분석
    const internalSignals = analyzeInternalData([
        'employee_self_learning',  // 직원들이 자발적으로 배우는 것
        'hiring_requisitions',     // 채용 공고
        'project_proposals',       // 제안된 프로젝트
        'tech_blog_mentions'       // 기술 블로그 언급
    ]);
    
    // 3. 신호 통합
    const emergingSkills = mergeAndRank(marketTrends, internalSignals);
    
    // 4. 각 신규 스킬에 대해
    for (const skill of emergingSkills) {
        // 이미 온톨로지에 있는지 확인
        let skillObj = ctx.ontology.find(Skill, { name: skill.name });
        
        if (!skillObj) {
            // 새 스킬 객체 제안
            skillObj = proposeNewSkill({
                name: skill.name,
                category: inferCategory(skill),
                domain: inferDomain(skill),
                marketDemand: skill.demandScore,
                emergingTrend: true,
                relatedSkills: findRelatedSkills(skill),
                suggestedCourses: findRelevantCourses(skill)
            });
        } else {
            // 기존 스킬의 수요 업데이트
            skillObj.marketDemand = updateDemand(skillObj, skill.demandScore);
            skillObj.emergingTrend = true;
        }
        
        // 5. 관련 있는 직원들에게 알림
        const relevantPeople = findRelevantPeople(skillObj);
        for (const person of relevantPeople) {
            notify(person, {
                type: 'EMERGING_SKILL_OPPORTUNITY',
                skill: skillObj,
                reason: explainRelevance(person, skillObj),
                resources: curateResources(skillObj)
            });
        }
    }
    
    return emergingSkills;
}
```

### Extracted Code (typescript)

```typescript
// Workshop 애플리케이션 구조

Dashboard: "Skill Intelligence Hub"

├─ Panel 1: Organization Overview
│   ├─ Total Skills Count (Card)
│   ├─ Skill Distribution by Category (Pie Chart)
│   ├─ Top 10 Most Common Skills (Bar Chart)
│   ├─ Emerging Skills Alert (Alert Cards)
│   └─ Skill Gap Heatmap by Department (Heatmap)
│
├─ Panel 2: Individual Profile
│   ├─ Skill Radar Chart (다차원 분석)
│   ├─ Proficiency Timeline (시간 경과)
│   ├─ Recommended Learning Paths (Cards)
│   ├─ Skill Decay Alerts (Warning Icons)
│   └─ Market Value Indicator (Gauge)
│
├─ Panel 3: Team Composition
│   ├─ Project-Skill Matrix (Heatmap)
│   ├─ Team Skill Coverage (Stacked Bar)
│   ├─ Suggested Team Members (Ranked List)
│   └─ Collaboration Network (Graph)
│
└─ Panel 4: Strategic Planning
    ├─ Supply-Demand Analysis (Scatter Plot)
    ├─ Future Skill Needs Projection (Time Series)
    ├─ Training ROI Calculator (Interactive Form)
    └─ Succession Planning Matrix (Grid)
```

### Extracted Code (typescript)

```typescript
// Object Explorer: 자연어 같은 쿼리

Query 1: "Python 고급 스킬을 가진 데이터팀 직원 중 
         머신러닝 프로젝트 경험이 없는 사람"

Translation:
SELECT p FROM Person p
WHERE p.department = 'Data'
  AND EXISTS (
    SELECT sp FROM p.possesses sp
    WHERE sp.skill.name = 'Python'
      AND sp.level >= 4
  )
  AND NOT EXISTS (
    SELECT pr FROM p.worksOn pr
    WHERE pr.requiredSkills CONTAINS 'Machine Learning'
  )

Result: [김민수, 박서연, 이준호]

Action Suggestion:
"이 3명에게 머신러닝 프로젝트 참여 기회를 제공하면 
 스킬 활용도를 높일 수 있습니다."


Query 2: "다음 분기 데이터 사이언티스트 역할을 
         수행할 수 있는 내부 후보"

Translation:
SELECT p, 
       skill_match_score(p, 'Data Scientist') as match,
       estimated_readiness_time(p, 'Data Scientist') as time
FROM Person p
WHERE p.employmentStatus = 'Active'
  AND skill_match_score(p, 'Data Scientist') >= 0.7
ORDER BY match DESC, time ASC

Result with Insights:
┌─────────┬───────┬──────────┬─────────────┐
│ Name    │ Match │ Ready In │ Gap         │
├─────────┼───────┼──────────┼─────────────┤
│ 이민정  │ 0.92  │ 4 weeks  │ MLOps (중급)│
│ 박지훈  │ 0.85  │ 8 weeks  │ 통계(고급)  │
│ 최서연  │ 0.78  │ 12 weeks │ Python(고급)│
└─────────┴───────┴──────────┴─────────────┘

Action: 각 후보에게 맞춤 학습 경로 자동 생성


Query 3: "AI 프로젝트를 위한 최적 팀 구성 (5명)"

Algorithm:
1. Required skills extraction from "AI Project" template
2. Constraint satisfaction problem solving
3. Multi-objective optimization:
   - Maximize skill coverage
   - Maximize team diversity
   - Minimize skill redundancy
   - Maximize learning opportunities
   - Balance workload

Result:
Team Composition:
- 박지훈 (ML Expert) - Team Lead
- 김서영 (Data Engineering) - Data Pipeline
- 이준호 (Cloud/DevOps) - Infrastructure
- 최민지 (Frontend) - User Interface
- 정수현 (Product) - Product Management

Team Stats:
- Skill Coverage: 96%
- Diversity Score: 0.82
- Estimated Success: 87%
- Knowledge Gaps: [MLOps-Advanced, A/B Testing]
- Recommended Support: External MLOps consultant
```

### Extracted Code (typescript)

```typescript
// Skill Network Visualization

Graph View: "Python Skill Ecosystem"

Nodes:
- Python (center, size ∝ # proficient people)
- Related Skills (connected, distance ∝ similarity)
- People (colored by proficiency level)
- Projects (shaped differently)
- Courses (another shape)

Edges:
- requires (directed, weighted)
- similarTo (undirected, weighted)
- usedIn (Person → Skill, thickness ∝ hours)
- develops (Course → Skill, color ∝ effectiveness)

Interactive Features:
- Click Python → highlight all connections
- Filter by proficiency level
- Time slider → see evolution
- "Find path" → shortest learning path between skills
- Clustering → auto-group related skills
```

### Extracted Code (python)

```python
# 모든 데이터의 출처 추적

Skill: "Python" (SKILL_PYTHON_001)
└─ Created: 2023-01-15
   └─ Source: Initial Ontology Setup
   
Person: 김철수 (EMP_001)
└─ SkillProficiency: Python (Level 4)
    └─ Evidence Chain:
        ├─ [1] Course Completion: "Python Advanced" (2023-03-20)
        │   └─ Source: LMS (Udemy API)
        │   └─ Confidence: 0.95
        ├─ [2] Project Participation: "Customer Analytics" (2023-04-01 - 2023-09-30)
        │   └─ Source: Jira API
        │   └─ Inferred Skill Usage: 400 hours
        │   └─ Confidence: 0.85
        ├─ [3] Peer Endorsement: 박지훈 (2023-10-15)
        │   └─ Source: Internal Platform
        │   └─ Confidence: 0.70
        └─ [4] Self-Assessment (2024-01-10)
            └─ Source: User Input
            └─ Confidence: 0.60
    
    Final Assessment:
    - Aggregated Level: 4 (Advanced)
    - Confidence: 0.88 (weighted average)
    - Last Validated: 2024-01-10
    - Validation Method: Multi-source
```

### Extracted Code (yaml)

```yaml
# Role-Based Access Control (RBAC)

Roles:
  - Employee:
      can_view:
        - own Person object (all properties)
        - own SkillProficiency objects
        - public Skill objects
        - public Course objects
      can_edit:
        - own self-assessment
        - own career aspirations
      can_action:
        - enroll in courses
        - request skill validation
  
  - Manager:
      can_view:
        - direct reports' Person objects
        - direct reports' SkillProficiency
        - team-level aggregations
      can_edit:
        - validate team members' skills
        - assign to projects
      can_action:
        - recommend learning paths
        - nominate for roles
  
  - HR Admin:
      can_view:
        - all Person objects (except salary)
        - all SkillProficiency objects
        - organization-wide analytics
      can_edit:
        - Person employment data
        - Role definitions
        - Learning Path templates
      can_action:
        - run talent analytics
        - export reports (anonymized)
  
  - System Admin:
      can_view:
        - all objects
        - all metadata
        - data lineage
      can_edit:
        - ontology schema
        - data pipelines
        - access controls
      can_action:
        - all actions

Data Masking:
  - PII fields auto-masked for non-authorized users
  - Aggregations automatically anonymized when < 5 people
  - Audit log for all sensitive data access
```

### Extracted Code (python)

```python
# Continuous Data Quality Checks

@data_quality_check(
    applies_to=SkillProficiency,
    frequency='daily'
)
def validate_skill_proficiency_integrity():
    violations = []
    
    # Check 1: 증거 없는 고숙련도
    high_level_without_evidence = query(
        "SkillProficiency WHERE level >= 4 AND evidence.count == 0"
    )
    if high_level_without_evidence:
        violations.append({
            'rule': 'HIGH_LEVEL_NEEDS_EVIDENCE',
            'severity': 'WARNING',
            'count': len(high_level_without_evidence),
            'action': 'Request validation'
        })
    
    # Check 2: 오래된 검증
    stale_validations = query(
        "SkillProficiency WHERE lastValidatedDate < NOW() - 365 days"
    )
    if stale_validations:
        violations.append({
            'rule': 'VALIDATION_STALE',
            'severity': 'INFO',
            'count': len(stale_validations),
            'action': 'Trigger re-validation'
        })
    
    # Check 3: 선행 스킬 위반
    for prof in query("SkillProficiency"):
        skill = prof.skill
        prerequisites = skill.requires
        
        for prereq, min_level in prerequisites:
            person_prereq = prof.person.get_skill(prereq)
            if not person_prereq or person_prereq.level < min_level:
                violations.append({
                    'rule': 'PREREQUISITE_VIOLATION',
                    'severity': 'ERROR',
                    'detail': f"{prof.person.name} has {skill.name} "
                             f"but insufficient {prereq.name}",
                    'action': 'Review or downgrade proficiency'
                })
    
    # Check 4: 감쇠 모델 적용
    decayed_skills = []
    for prof in query("SkillProficiency"):
        days_unused = (Date.now() - prof.lastUsedDate).days
        if days_unused > prof.skill.halfLife * 2:  # 2 half-lives
            decayed_skills.append(prof)
    
    if decayed_skills:
        violations.append({
            'rule': 'SKILL_DECAY_DETECTED',
            'severity': 'WARNING',
            'count': len(decayed_skills),
            'action': 'Alert person and suggest refresher'
        })
    
    return violations


@data_quality_check(
    applies_to=Skill,
    frequency='weekly'
)
def validate_skill_ontology_coherence():
    violations = []
    
    # Check 1: 고아 스킬 (관계 없음)
    orphan_skills = query(
        "Skill WHERE incoming_links.count == 0 AND outgoing_links.count == 0"
    )
    
    # Check 2: 순환 참조
    circular_dependencies = find_cycles_in_requires_graph()
    
    # Check 3: 시장 수요 데이터 누락
    missing_market_data = query(
        "Skill WHERE marketDemand IS NULL AND createdAt < NOW() - 30 days"
    )
    
    return violations
```

### Extracted Code (python)

```python
# Machine Learning Models in Foundry

@ml_model(
    name='skill_recommendation_model',
    framework='pytorch',
    retraining_frequency='weekly'
)
class SkillRecommender:
    """
    협업 필터링 + 그래프 신경망 하이브리드 모델
    """
    
    def __init__(self):
        self.embedding_dim = 128
        self.gnn = GraphNeuralNetwork(
            node_types=['Person', 'Skill', 'Role', 'Project'],
            edge_types=['possesses', 'requires', 'usedIn'],
            hidden_dims=[256, 128, 64]
        )
        self.collaborative_filter = MatrixFactorization(
            n_factors=64
        )
    
    def train(self, training_data):
        """
        학습 데이터:
        - 과거 스킬 학습 이력
        - 프로젝트 참여 패턴
        - 커리어 진행 경로
        - 유사 프로필 사람들의 선택
        """
        # 1. 온톨로지 그래프를 GNN 입력으로 변환
        graph = construct_heterogeneous_graph(
            ontology=ctx.ontology,
            include_temporal=True
        )
        
        # 2. 노드 임베딩 학습
        node_embeddings = self.gnn.forward(graph)
        
        # 3. Person-Skill 매트릭스 분해
        interaction_matrix = build_interaction_matrix(
            people=training_data.people,
            skills=training_data.skills,
            interactions=training_data.proficiencies
        )
        
        self.collaborative_filter.fit(interaction_matrix)
        
        # 4. 하이브리드 결합
        # GNN: 구조적 관계 / CF: 행동 패턴
        return combined_loss(gnn_loss, cf_loss)
    
    def recommend(self, person: Person, n: int = 10):
        """
        개인화 스킬 추천
        """
        # 1. GNN으로 구조적 추천
        person_embedding = self.gnn.get_embedding(person)
        all_skill_embeddings = self.gnn.get_embeddings(Skill)
        
        structural_scores = cosine_similarity(
            person_embedding,
            all_skill_embeddings
        )
        
        # 2. 협업 필터링으로 행동 기반 추천
        behavioral_scores = self.collaborative_filter.predict(
            person_id=person.employeeId
        )
        
        # 3. 컨텍스트 기반 조정
        context = extract_context(person)
        context_weights = {
            'career_goal': 0.4,      # 커리어 목표와 정렬
            'market_trend': 0.2,     # 시장 트렌드
            'team_need': 0.2,        # 팀 니즈
            'learning_style': 0.1,   # 학습 스타일 적합성
            'time_to_learn': 0.1     # 학습 시간 제약
        }
        
        # 4. 하이브리드 스코어 계산
        final_scores = (
            structural_scores * 0.4 +
            behavioral_scores * 0.4 +
            context_score(person, context_weights) * 0.2
        )
        
        # 5. 필터링
        # - 이미 보유한 스킬 제외
        # - 선행 스킬 미충족 스킬 제외 또는 낮은 순위
        # - 감쇠 위험 높은 기존 스킬 복습 우선순위 상향
        
        recommendations = []
        for skill, score in sorted(final_scores.items(), reverse=True):
            if len(recommendations) >= n:
                break
            
            if person.has_skill(skill):
                continue
            
            prereqs = skill.requires
            prereq_status = check_prerequisites(person, prereqs)
            
            if prereq_status.all_met:
                recommendations.append({
                    'skill': skill,
                    'score': score,
                    'reason': explain_recommendation(person, skill),
                    'learning_path': generate_path(person, skill),
                    'estimated_time': estimate_time(person, skill),
                    'value_add': estimate_value(person, skill)
                })
            elif prereq_status.mostly_met:
                # 선행 스킬이 거의 충족되면 패키지로 추천
                recommendations.append({
                    'skill': skill,
                    'score': score * 0.8,
                    'reason': "선행 스킬 보완 후 추천",
                    'prerequisites': prereq_status.missing,
                    'bundled_path': create_bundled_path(
                        person, 
                        prereq_status.missing + [skill]
                    )
                })
        
        return recommendations


@ml_model(
    name='skill_level_predictor',
    framework='xgboost'
)
class SkillLevelPredictor:
    """
    다양한 증거로부터 실제 스킬 레벨 예측
    """
    
    features = [
        'course_completion_count',
        'course_avg_score',
        'project_count',
        'total_hours_used',
        'recency_days',
        'peer_endorsement_count',
        'certification_exists',
        'self_assessed_level',
        'years_experience',
        'similar_skill_levels'  # 유사 스킬의 평균 레벨
    ]
    
    def predict_true_level(self, proficiency: SkillProficiency):
        """
        Self-assessment는 과대/과소 평가 가능성
        실제 증거 기반으로 진짜 레벨 예측
        """
        X = extract_features(proficiency, self.features)
        predicted_level = self.model.predict(X)
        confidence = self.model.predict_proba(X).max()
        
        return {
            'predicted_level': round(predicted_level),
            'confidence': confidence,
            'self_assessed': proficiency.level,
            'discrepancy': abs(predicted_level - proficiency.level),
            'recommendation': 'validation_needed' if discrepancy > 1 else 'ok'
        }
```

### Extracted Code (python)

```python
@ml_model(
    name='skill_extraction_nlp',
    framework='transformers'
)
class SkillExtractor:
    """
    자유 텍스트에서 스킬 추출
    - 이력서
    - 자기소개서
    - 프로젝트 설명
    - 채용 공고
    """
    
    def __init__(self):
        # Fine-tuned BERT for Named Entity Recognition
        self.model = AutoModelForTokenClassification.from_pretrained(
            'bert-base-uncased',
            num_labels=len(SKILL_TAGS)
        )
        self.tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
        
        # 온톨로지와 연결
        self.skill_ontology = ctx.ontology
    
    def extract(self, text: str):
        """
        텍스트에서 스킬 추출 및 정규화
        """
        # 1. NER로 스킬 후보 추출
        tokens = self.tokenizer(text, return_tensors='pt')
        outputs = self.model(**tokens)
        predictions = outputs.logits.argmax(dim=-1)
        
        skill_spans = extract_skill_spans(tokens, predictions)
        
        # 2. 온톨로지와 매칭
        normalized_skills = []
        for span in skill_spans:
            raw_skill = text[span.start:span.end]
            
            # 퍼지 매칭으로 온톨로지 스킬 찾기
            matches = self.skill_ontology.fuzzy_match(
                Skill,
                field='name',
                query=raw_skill,
                threshold=0.85
            )
            
            if matches:
                # 가장 유사한 것 선택
                best_match = matches[0]
                normalized_skills.append({
                    'raw': raw_skill,
                    'normalized': best_match.canonicalName,
                    'skill_id': best_match.skillId,
                    'confidence': matches[0].score
                })
            else:
                # 온톨로지에 없는 새 스킬 제안
                normalized_skills.append({
                    'raw': raw_skill,
                    'normalized': None,
                    'suggestion': 'add_to_ontology',
                    'confidence': 0.6
                })
        
        return normalized_skills
    
    def extract_with_context(self, text: str):
        """
        컨텍스트와 함께 스킬 추출 (레벨 추론)
        """
        skills = self.extract(text)
        
        # 주변 문맥에서 숙련도 단서 찾기
        for skill in skills:
            context = extract_context_window(text, skill.span, window=50)
            
            # "expert in Python", "basic knowledge of Java" 같은 패턴
            level_indicators = {
                'expert|advanced|proficient': 5,
                'intermediate|working knowledge': 3,
                'basic|beginner|familiar': 2
            }
            
            for pattern, level in level_indicators.items():
                if re.search(pattern, context, re.IGNORECASE):
                    skill['inferred_level'] = level
                    break
        
        return skills
```

### Extracted Code (python)

```python
# External API Integrations

@external_integration(
    name='linkedin_skills_api',
    refresh_frequency='weekly'
)
def sync_market_skill_trends():
    """
    LinkedIn, GitHub, Stack Overflow에서 
    스킬 트렌드 데이터 수집
    """
    # LinkedIn Talent Insights API
    linkedin_data = linkedin_api.get_skill_trends(
        regions=['US', 'Europe', 'Asia'],
        industries=['Technology', 'Finance', 'Healthcare']
    )
    
    # GitHub Octoverse
    github_data = github_api.get_trending_technologies()
    
    # Stack Overflow Developer Survey
    stackoverflow_data = fetch_stackoverflow_survey_data()
    
    # 온톨로지 스킬과 매칭 및 업데이트
    for skill in ctx.ontology.get_all(Skill):
        external_demand = aggregate_external_demand(
            skill,
            [linkedin_data, github_data, stackoverflow_data]
        )
        
        skill.marketDemand = external_demand.score
        skill.trendDirection = external_demand.direction
        skill.metadata['external_sources'] = external_demand.sources


@external_integration(
    name='course_marketplace_api',
    refresh_frequency='daily'
)
def discover_learning_resources():
    """
    Coursera, Udemy, Pluralsight 등에서
    최신 코스 정보 수집
    """
    platforms = [
        CourseeraAPI(),
        UdemyAPI(),
        PluralsightAPI(),
        LinkedInLearningAPI()
    ]
    
    for skill in ctx.ontology.get_all(Skill):
        courses = []
        for platform in platforms:
            results = platform.search_courses(skill.name)
            courses.extend(results)
        
        # 코스 큐레이션
        curated = rank_and_filter_courses(
            courses,
            criteria={
                'rating_min': 4.0,
                'students_min': 1000,
                'updated_within_months': 12,
                'price_max': skill.recommended_budget
            }
        )
        
        # Course 객체 생성 또는 업데이트
        for course_data in curated:
            course = ctx.ontology.get_or_create(
                Course,
                externalId=course_data.id,
                platform=course_data.platform
            )
            
            course.update({
                'title': course_data.title,
                'provider': course_data.instructor,
                'rating': course_data.rating,
                'duration': course_data.duration,
                'url': course_data.url,
                'price': course_data.price
            })
            
            # Skill-Course 관계 생성
            ctx.ontology.create_link(
                'taughtIn',
                from_obj=skill,
                to_obj=course,
                properties={'effectiveness': estimate_effectiveness(course)}
            )
```

### Extracted Code (python)

```python
@predictive_model(
    name='succession_planning',
    horizon='2_years'
)
def predict_succession_needs():
    """
    향후 2년간 각 핵심 역할의 공석 예측 및 후보 식별
    """
    critical_roles = ctx.ontology.query(Role).filter(
        criticality='High'
    )
    
    predictions = []
    for role in critical_roles:
        current_holders = role.filledBy
        
        for person in current_holders:
            # 이탈 위험 예측
            attrition_risk = predict_attrition_risk(person)
            
            # 승진 가능성 예측
            promotion_prob = predict_promotion_probability(person)
            
            # 퇴직 예정
            retirement_date = predict_retirement(person)
            
            vacancy_risk = max(
                attrition_risk,
                promotion_prob,
                1.0 if retirement_date < 730 else 0  # 2 years
            )
            
            if vacancy_risk > 0.3:
                # 후보 찾기
                candidates = find_succession_candidates(role)
                
                predictions.append({
                    'role': role,
                    'current_holder': person,
                    'vacancy_risk': vacancy_risk,
                    'estimated_vacancy_date': estimate_date(vacancy_risk),
                    'ready_now': [c for c in candidates if c.readiness >= 0.9],
                    'ready_soon': [c for c in candidates if 0.7 <= c.readiness < 0.9],
                    'need_development': [c for c in candidates if c.readiness < 0.7],
                    'action_plan': generate_succession_plan(role, candidates)
                })
    
    return predictions


@predictive_model(
    name='skill_demand_forecasting',
    horizon='1_year'
)
def forecast_skill_demand():
    """
    향후 1년간 스킬별 수요 예측
    - 사업 계획
    - 시장 트렌드
    - 기술 발전
    """
    # 입력 데이터
    business_plans = fetch_business_roadmap()
    market_trends = get_market_forecasts()
    tech_evolution = get_technology_forecast()
    
    forecasts = {}
    for skill in ctx.ontology.get_all(Skill):
        # 시계열 예측 모델 (SARIMA)
        historical_demand = skill.get_timeseries('internalDemand', period='2_years')
        
        # 외부 요인 반영
        external_signals = {
            'market_growth': market_trends.get(skill.domain, 1.0),
            'tech_adoption': tech_evolution.get(skill.name, 1.0),
            'planned_projects': count_planned_projects_needing(skill)
        }
        
        forecast = sarima_predict(
            historical=historical_demand,
            exogenous=external_signals,
            periods=12  # months
        )
        
        # 공급 예측
        current_supply = skill.totalProficientEmployees
        natural_attrition = current_supply * 0.15  # 15% annual
        training_pipeline = count_in_training(skill)
        projected_supply = current_supply - natural_attrition + training_pipeline
        
        gap = forecast.demand - projected_supply
        
        forecasts[skill] = {
            'skill': skill,
            'current_supply': current_supply,
            'forecast_demand': forecast.demand,
            'projected_supply': projected_supply,
            'gap': gap,
            'gap_severity': 'critical' if gap > current_supply * 0.3 else
                           'moderate' if gap > 0 else 'surplus',
            'recommendation': generate_workforce_plan(skill, gap)
        }
    
    return forecasts
```

### Extracted Code (bash)

```bash
# 1. 패키지 설치 (5분)
pip install -r requirements.txt

# 2. 데이터 로드 (5분)
python data_loader.py

# 3. 쿼리 테스트 (5분)
python semantic_layer.py

# 4. 대시보드 실행 (15분)
streamlit run dashboard.py
```

### Extracted Code (python)

```python
# ✅ 학습 경로 찾기
path = semantic.find_learning_path('머신러닝 기초', '대규모 언어 모델')
# → 머신러닝 기초 → 딥러닝 → 대규모 언어 모델 (8주)

# ✅ 역할 요구사항 조회
reqs = semantic.get_role_requirements_detail('AI Architect', priority='High')

# ✅ 역할 비교
comparison = semantic.compare_roles('AI Engineer', 'ML Engineer')
# → 유사도 100%

# ✅ 허브 스킬 Top 10
hubs = semantic.get_hub_skills(10)
# → ROI 산정, A/B 테스팅, AI 규제...
```

### Extracted Code (python)

```python
# 정적 객체 - 한 번 로드하면 끝
competencies = loader.load_competencies()

# 수동 함수 호출
hubs = semantic.get_hub_skills(10)

# 단순 조회만 가능
path = semantic.find_learning_path(start, end)
```

### Extracted Code (python)

```python
# 살아있는 객체 - 실시간 계산
python = ontology.get(Competency, 'Python')
print(python.total_proficient_people)  # 자동 계산
print(python.growth_rate)  # 자동 계산

# Actions로 실행
python_skill.update_market_demand()  # 버튼 클릭으로 실행 가능

# 데이터 계보 추적
print(python.lineage)  # 어디서 왔는지 자동 추적
```

### Extracted Code (text)

```text
Python skill:
- Total proficient people: 2 ← 자동 계산
- Average level: 4.50 ← 자동 계산  
- Growth rate: 25.0% ← 자동 계산
- Hub score: 0.00 ← 자동 계산

Jane's profile:
- Skill count: 2 ← 자동 계산
- Market value: 129.2 ← 자동 계산
- Readiness for Data Scientist: 67% ← 자동 계산
```

### Extracted Code (text)

```text
🎯 Generating learning path for Jane Kim → Data Scientist
   Current readiness: 67%
   Skills to learn: 1
   ✅ Learning path created: 4 weeks
[AUDIT] jane@company.com executed action
```

### Extracted Code (python)

```python
# ✅ Computed Properties 완전 구현
class Person(OntologyObject):
    @computed_property(ttl=3600)
    def skill_count(self):
        return len(self.possesses)  # 자동 계산!

# ✅ Transform Pipeline
@transform(input=CourseCompletion, output=SkillProficiency)
def extract_skills_from_courses(ctx, completions):
    # 버전관리, 재실행, lineage 자동 기록
    return proficiencies
```

### Extracted Code (python)

```python
# ✅ Actions 완전 구현
@action(applies_to=Person)
def enroll_in_learning_path(person, target_role):
    # UI 버튼으로 실행
    # 객체 생성/수정
    # 알림 자동 전송
    # 감사 로그 자동 기록
    
# ✅ Data Lineage
print(proficiency.lineage)
# → Course "Python Advanced" (2023-03-20, confidence: 0.95)
# → Project "Data Analytics" (2023-04, confidence: 0.85)
```

### Extracted Code (text)

```text
Week 1-2:  MVP (32% Foundry) ✅ 완료!
Week 3-6:  Phase 1 (60% Foundry) ← Computed Properties
Week 7-14: Phase 2 (90% Foundry) ← Actions + Lineage
```
