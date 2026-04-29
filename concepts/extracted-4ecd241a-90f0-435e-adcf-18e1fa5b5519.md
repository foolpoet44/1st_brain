# Extracted Knowledge from Conv: 4ecd241a-90f0-435e-adcf-18e1fa5b5519

**Date**: 2025-12-23T01:10:21.701874Z

### Extracted Code (sql)

```sql
-- 1. 직무 (Jobs)
CREATE TABLE jobs (
    id SERIAL PRIMARY KEY,
    code VARCHAR(50) UNIQUE NOT NULL,
    name VARCHAR(200) NOT NULL,
    category VARCHAR(100),
    description TEXT,
    metadata JSONB,  -- 유연한 추가 정보
    created_at TIMESTAMP DEFAULT NOW()
);

-- 2. 역량 프레임워크 (Competency Framework)
CREATE TABLE competencies (
    id SERIAL PRIMARY KEY,
    code VARCHAR(50) UNIQUE NOT NULL,
    name VARCHAR(200) NOT NULL,
    category VARCHAR(100),  -- behavioral, technical, leadership
    source VARCHAR(50),  -- SHL_UCF, custom 등
    definition JSONB,  -- 계층적 정의 (JSON으로 유연하게)
    level_criteria JSONB,  -- 레벨별 기준
    created_at TIMESTAMP DEFAULT NOW()
);

-- 3. 스킬 (Skills)
CREATE TABLE skills (
    id SERIAL PRIMARY KEY,
    code VARCHAR(50) UNIQUE NOT NULL,
    name VARCHAR(200) NOT NULL,
    skill_type VARCHAR(50),  -- technical, soft, digital
    industry VARCHAR(100),  -- smart_factory, manufacturing 등
    proficiency_levels JSONB,  -- 숙련도 레벨 정의
    related_tools JSONB,  -- 관련 도구/기술 목록
    created_at TIMESTAMP DEFAULT NOW()
);

-- 4. 직무-역량 매핑 (Job-Competency Mapping)
CREATE TABLE job_competencies (
    id SERIAL PRIMARY KEY,
    job_id INTEGER REFERENCES jobs(id),
    competency_id INTEGER REFERENCES competencies(id),
    importance_level INTEGER CHECK (importance_level BETWEEN 1 AND 5),
    required_level INTEGER,
    assessment_criteria JSONB,
    UNIQUE(job_id, competency_id)
);

-- 5. 역량-스킬 매핑 (Competency-Skill Mapping)
CREATE TABLE competency_skills (
    id SERIAL PRIMARY KEY,
    competency_id INTEGER REFERENCES competencies(id),
    skill_id INTEGER REFERENCES skills(id),
    weight DECIMAL(3,2),  -- 가중치
    context JSONB,  -- 적용 맥락
    UNIQUE(competency_id, skill_id)
);

-- 6. 평가 데이터 (Assessments)
CREATE TABLE assessments (
    id SERIAL PRIMARY KEY,
    person_id VARCHAR(100),
    job_id INTEGER REFERENCES jobs(id),
    assessed_at DATE,
    assessor VARCHAR(200),
    status VARCHAR(50),  -- draft, completed, verified
    results JSONB,  -- 평가 결과 (유연한 구조)
    gap_analysis JSONB,  -- 갭 분석 결과
    created_at TIMESTAMP DEFAULT NOW()
);
```

### Extracted Code (json)

```json
// competencies.definition 예시 (SHL UCF 기반)
{
  "ucf_code": "DEC",
  "ucf_name": "Deciding and Initiating Action",
  "levels": {
    "1": {
      "description": "기본 수준의 의사결정",
      "indicators": ["단순한 상황에서 결정", "지침 따름"],
      "smart_factory_context": "표준 작업 지시 이해 및 실행"
    },
    "2": {
      "description": "중급 수준의 의사결정",
      "indicators": ["복잡한 상황 분석", "대안 평가"],
      "smart_factory_context": "디지털 시스템 데이터 기반 판단"
    }
  }
}

// skills.proficiency_levels 예시
{
  "levels": [
    {
      "level": 1,
      "name": "Beginner",
      "criteria": "PLC 기본 개념 이해",
      "assessment_method": "객관식 시험"
    },
    {
      "level": 2,
      "name": "Intermediate",
      "criteria": "간단한 래더 로직 작성 가능",
      "assessment_method": "실습 과제"
    }
  ],
  "tools": ["Siemens TIA Portal", "Rockwell Studio 5000"]
}

// assessments.results 예시
{
  "competency_scores": {
    "DEC": {"score": 3.5, "evidence": ["프로젝트 리드 경험"]},
    "ANA": {"score": 4.0, "evidence": ["데이터 분석 인증"]}
  },
  "skill_scores": {
    "python_programming": {"level": 4, "verified_by": "certification"},
    "plc_programming": {"level": 2, "verified_by": "practical_test"}
  },
  "recommendations": [
    "PLC 고급 과정 수강 권장",
    "AI/ML 프로젝트 참여 추천"
  ]
}
```

### Extracted Code (bash)

```bash
# 현재 엑셀 구조를 JSON으로 변환
엑셀/
├── AX역량_스마트팩토리통합_v2.0.xlsx
│
변환 ↓
│
JSON/
├── jobs.json
├── competencies.json
├── skills.json
├── mappings.json
└── assessments.json
```

### Extracted Code (python)

```python
import pandas as pd
import json

# 엑셀 읽기
df = pd.read_excel('AX역량_스마트팩토리통합_v2.0.xlsx', sheet_name='직무정보')

# JSON 변환
jobs = df.to_dict('records')
with open('jobs.json', 'w', encoding='utf-8') as f:
    json.dump(jobs, f, ensure_ascii=False, indent=2)
```

### Extracted Code (python)

```python
import sqlite3
import json

# SQLite 생성 (PostgreSQL과 문법 거의 동일)
conn = sqlite3.connect('hr_competency.db')
cursor = conn.cursor()

# 테이블 생성 (위의 SQL 스키마 사용)
# JSON 컬럼은 TEXT로 저장 후 파싱
```

### Extracted Code (bash)

```bash
# Supabase 프로젝트 생성 (무료)
# https://supabase.com

# 자동으로 제공:
# - PostgreSQL 14+
# - REST API
# - 실시간 구독
# - 인증 시스템
# - 대시보드
```

### Extracted Code (python)

```python
from fastapi import FastAPI
from pydantic import BaseModel
import asyncpg  # PostgreSQL 비동기 클라이언트

app = FastAPI()

# JSON 응답 모델
class CompetencyResponse(BaseModel):
    code: str
    name: str
    definition: dict  # JSONB 컬럼
    levels: dict

@app.get("/api/competencies/{code}")
async def get_competency(code: str):
    # PostgreSQL JSONB 쿼리
    query = """
        SELECT code, name, definition, level_criteria as levels
        FROM competencies
        WHERE code = $1
    """
    # ... 구현
```

### Extracted Code (bash)

```bash
# 데이터베이스 확인
python3 test_db.py

# API 서버 실행
python3 api_server.py

# 브라우저에서 확인
http://localhost:8000/docs
```

### Extracted Code (bash)

```bash
# Python으로 쿼리
python3 << EOF
import sqlite3
conn = sqlite3.connect('output/competency.db')
cursor = conn.cursor()
cursor.execute("SELECT label, market_demand FROM [1역량마스터데이터] LIMIT 5")
print(cursor.fetchall())
EOF
```

### Extracted Code (text)

```text
fastapi           0.127.0    ✅
uvicorn           0.40.0     ✅
pandas            2.3.3      ✅
openpyxl          3.1.5      ✅
pydantic          2.12.5     ✅
numpy             2.4.0      ✅
```

### Extracted Code (text)

```text
fastapi==0.127.0        # API 프레임워크
uvicorn==0.40.0         # ASGI 웹서버
pandas==2.3.3           # 데이터 분석
openpyxl==3.1.5         # 엑셀 처리
pydantic==2.12.5        # 데이터 검증
numpy==2.4.0            # 수치 계산
```

### Extracted Code (bash)

```bash
# 1. 전체 목록 (테이블 형식)
pip list

# 2. requirements.txt용 (버전 고정)
pip freeze

# 3. 특정 패키지 상세 정보
pip show fastapi

# 4. 의존성 트리 (추천!)
pipdeptree

# 5. 업데이트 가능한 패키지
pip list --outdated
```

### Extracted Code (json)

```json
{
  "total_competencies": 66,
  "total_persons": 30,
  "total_proficiency_records": 394,
  "by_department": [
    {"department": "AI연구팀", "count": 6},
    {"department": "데이터팀", "count": 4}
  ],
  "by_competency_type": [
    {"type": "TechnicalSkill", "count": 32},
    {"type": "SoftSkill", "count": 10}
  ]
}
```

### Extracted Code (text)

```text
GET /competencies
    ?type=TechnicalSkill    # 타입 필터
    &min_demand=80          # 최소 수요
    &limit=20               # 개수 제한
```

### Extracted Code (bash)

```bash
# 모든 역량 조회
curl http://localhost:8000/competencies

# 고수요 기술 스킬만 조회
curl "http://localhost:8000/competencies?type=TechnicalSkill&min_demand=80"

# 상위 10개만
curl "http://localhost:8000/competencies?limit=10"
```

### Extracted Code (json)

```json
[
  {
    "competency_id": "LLM",
    "label": "대규모 언어 모델",
    "type": "TechnicalSkill",
    "category": "AI",
    "market_demand": 96.8,
    "short_description": "GPT, Claude 등 LLM 활용 능력"
  },
  {
    "competency_id": "PromptEngineering",
    "label": "프롬프트 엔지니어링",
    "type": "TechnicalSkill",
    "category": "AI",
    "market_demand": 94.2,
    "short_description": "효과적인 AI 프롬프트 작성 기술"
  }
]
```

### Extracted Code (json)

```json
{
  "competency": {
    "competency_id": "AIEthics",
    "label": "AI 윤리",
    "type": "DomainKnowledge",
    "category": "Business",
    "market_demand": 88.6,
    "description": "AI 시스템 개발 및 활용에서 윤리적 원칙과 책임 있는 AI 실천",
    "long_description": "AI 기술의 개발과 배포 과정에서 공정성, 투명성...",
    "keywords": "AI 윤리, DomainKnowledge, AI, Transformation",
    "related_tools": "Fairlearn,AI Fairness 360,What-If Tool"
  },
  "levels": [
    {
      "level": 1,
      "level_name": "Awareness",
      "level_description": "기본 개념과 용어를 이해하고 설명할 수 있음",
      "typical_experience": "입문"
    },
    {
      "level": 2,
      "level_name": "Basic",
      "level_description": "지도 하에 기본적인 작업을 수행할 수 있음",
      "typical_experience": "6+ 개월"
    },
    // ... levels 3, 4, 5
  ]
}
```

### Extracted Code (bash)

```bash
# 전체 인원 조회
curl http://localhost:8000/persons

# AI연구팀만 조회
curl "http://localhost:8000/persons?department=AI연구팀"
```

### Extracted Code (json)

```json
[
  {
    "person_id": "P001",
    "employee_id": "E2024001",
    "name": "김민준",
    "email": "minjun.kim@company.com",
    "department": "AI연구팀",
    "current_role_id": "ML Engineer",
    "hire_date": "2022-03-01",
    "total_experience_months": 36,
    "education_level": "석사",
    "major": "컴퓨터공학"
  }
]
```

### Extracted Code (json)

```json
{
  "person": {
    "person_id": "P001",
    "name": "김민준",
    "email": "minjun.kim@company.com",
    "department": "AI연구팀",
    "current_role_id": "ML Engineer"
  },
  "skills": [
    {
      "competency_id": "LLM",
      "label": "대규모 언어 모델",
      "type": "TechnicalSkill",
      "level": 4,
      "confidence_score": 0.92,
      "validated": true,
      "last_used_date": "2025-12-20"
    },
    {
      "competency_id": "Python",
      "label": "Python 프로그래밍",
      "type": "TechnicalSkill",
      "level": 5,
      "confidence_score": 0.95,
      "validated": true
    }
  ],
  "total_skills": 15
}
```

### Extracted Code (json)

```json
{
  "person": {
    "person_id": "P001",
    "name": "김민준",
    "current_role_id": "ML Engineer"
  },
  "role": "ML Engineer",
  "gaps": [
    {
      "competency_label": "MLOps",
      "competency_type": "TechnicalSkill",
      "target_level": 4,
      "current_level": 2,
      "gap": 2,
      "importance": "High",
      "market_demand": 89.5
    },
    {
      "competency_label": "Python 프로그래밍",
      "competency_type": "TechnicalSkill",
      "target_level": 5,
      "current_level": 5,
      "gap": 0,
      "importance": "Critical",
      "market_demand": 95.5
    },
    {
      "competency_label": "딥러닝 프레임워크",
      "competency_type": "TechnicalSkill",
      "target_level": 4,
      "current_level": 5,
      "gap": -1,
      "importance": "High",
      "market_demand": 92.3
    }
  ],
  "summary": {
    "total_skills": 20,
    "needs_improvement": 8,
    "meets_requirements": 9,
    "exceeds": 3
  }
}
```

### Extracted Code (json)

```json
{
  "role": "ML Engineer",
  "requirements": [
    {
      "competency_id": "LLM",
      "competency_label": "대규모 언어 모델",
      "competency_type": "TechnicalSkill",
      "required_level": 4,
      "importance": "Critical",
      "priority": "P0",
      "market_demand": 96.8,
      "short_description": "GPT, Claude 등 LLM 활용"
    },
    {
      "competency_id": "Python",
      "competency_label": "Python 프로그래밍",
      "competency_type": "TechnicalSkill",
      "required_level": 5,
      "importance": "Critical",
      "priority": "P0",
      "market_demand": 95.5
    }
  ],
  "total": 20
}
```

### Extracted Code (bash)

```bash
# 1. Data Scientist 역할의 필요 역량 조회
curl http://localhost:8000/roles/Data%20Scientist/requirements

# 2. 고수요 기술 스킬만 필터링
curl "http://localhost:8000/competencies?type=TechnicalSkill&min_demand=85"

# 3. 특정 역량의 레벨별 상세 기준 확인
curl http://localhost:8000/competency/MachineLearning
```

### Extracted Code (bash)

```bash
# 1. 직원의 현재 프로파일 확인
curl http://localhost:8000/person/P001/profile

# 2. 스킬 갭 분석
curl http://localhost:8000/skill-gap/P001

# 3. 부족한 역량의 상세 정보 및 학습 경로 확인
curl http://localhost:8000/competency/MLOps
```

### Extracted Code (bash)

```bash
# 1. 부서별 인원 확인
curl http://localhost:8000/stats

# 2. 특정 부서 직원 목록
curl "http://localhost:8000/persons?department=AI연구팀"

# 3. 각 직원의 스킬 갭 분석
for id in P001 P002 P003; do
  curl http://localhost:8000/skill-gap/$id
done
```

### Extracted Code (python)

```python
import requests

BASE_URL = "http://localhost:8000"

# 1. 고수요 역량 조회
response = requests.get(
    f"{BASE_URL}/competencies",
    params={
        "type": "TechnicalSkill",
        "min_demand": 90,
        "limit": 5
    }
)
top_skills = response.json()
print(f"Top {len(top_skills)} 고수요 스킬:")
for skill in top_skills:
    print(f"  - {skill['label']}: {skill['market_demand']}")

# 2. 개인 스킬 갭 분석
person_id = "P001"
gap_response = requests.get(f"{BASE_URL}/skill-gap/{person_id}")
gap_data = gap_response.json()

print(f"\n{gap_data['person']['name']}님의 스킬 갭:")
print(f"  향상 필요: {gap_data['summary']['needs_improvement']}개")
print(f"  충족: {gap_data['summary']['meets_requirements']}개")

# 향상이 필요한 스킬 출력
needs_work = [g for g in gap_data['gaps'] if g['gap'] > 0]
for gap in needs_work[:5]:
    print(f"  - {gap['competency_label']}: "
          f"현재 Lv.{gap['current_level']} → 목표 Lv.{gap['target_level']}")
```

### Extracted Code (json)

```json
{
  "person": {...},          // 메인 객체
  "skills": [...],          // 관련 데이터
  "total_skills": 15,       // 메타 정보
  "summary": {...}          // 요약/통계
}
```
