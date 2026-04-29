# Extracted Knowledge from Conv: 9e84b0dc-72ca-4ff8-84e5-f3ccf250da0a

**Date**: 2026-01-28T09:17:54.060074Z

### Extracted Code (text)

```text
Physical AI 역량 체계
├── Core Technical Skills
│   ├── Robotics & Manipulation
│   ├── Computer Vision & Perception
│   ├── Motion Planning & Control
│   └── Sensor Integration
│
├── Domain Knowledge
│   ├── Physics & Dynamics
│   ├── Hardware Systems
│   ├── AI/ML Foundations
│   └── Safety & Ethics
│
└── Applied Competences
    ├── System Integration
    ├── Real-world Problem Solving
    ├── Human-Robot Interaction
    └── Adaptive Learning
```

### Extracted Code (sql)

```sql
-- 핵심 테이블 구조
CREATE TABLE esco_skills (
    skill_id TEXT PRIMARY KEY,
    skill_uri TEXT UNIQUE,
    preferred_label TEXT,
    alt_labels TEXT[],
    description TEXT,
    skill_type TEXT CHECK(skill_type IN ('skill', 'knowledge', 'competence')),
    esco_level INTEGER, -- 1-8 (EQF levels)
    physical_ai_relevance FLOAT, -- 0-1 relevance score
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE skill_hierarchies (
    parent_skill_id TEXT REFERENCES esco_skills(skill_id),
    child_skill_id TEXT REFERENCES esco_skills(skill_id),
    relationship_type TEXT, -- 'broader', 'narrower', 'related'
    PRIMARY KEY (parent_skill_id, child_skill_id)
);

CREATE TABLE skill_clusters (
    cluster_id TEXT PRIMARY KEY,
    cluster_name TEXT,
    description TEXT,
    physical_ai_domain TEXT -- 'manipulation', 'perception', 'locomotion', etc.
);

CREATE TABLE skill_to_cluster (
    skill_id TEXT REFERENCES esco_skills(skill_id),
    cluster_id TEXT REFERENCES skill_clusters(cluster_id),
    centrality_score FLOAT, -- 중심성 점수
    PRIMARY KEY (skill_id, cluster_id)
);

CREATE TABLE learning_pathways (
    pathway_id TEXT PRIMARY KEY,
    pathway_name TEXT,
    skill_sequence TEXT[], -- skill_ids in order
    estimated_duration INTEGER, -- in hours
    prerequisite_pathways TEXT[]
);
```

### Extracted Code (sql)

```sql
-- Physical AI 특화 속성
CREATE TABLE physical_ai_extensions (
    skill_id TEXT PRIMARY KEY REFERENCES esco_skills(skill_id),
    
    -- Hardware Requirements
    requires_physical_robot BOOLEAN DEFAULT FALSE,
    simulation_capable BOOLEAN DEFAULT TRUE,
    hardware_platforms TEXT[], -- ['UR5', 'Franka Emika', 'Boston Dynamics Spot']
    
    -- Interaction Modalities
    sensory_modalities TEXT[], -- ['vision', 'force', 'tactile', 'audio']
    actuation_types TEXT[], -- ['manipulation', 'locomotion', 'grasping']
    
    -- Complexity Metrics
    real_time_requirement BOOLEAN DEFAULT FALSE,
    safety_critical BOOLEAN DEFAULT FALSE,
    multi_modal_integration BOOLEAN DEFAULT FALSE,
    
    -- Learning Characteristics
    sample_efficiency_rating INTEGER, -- 1-5
    sim_to_real_transferability INTEGER, -- 1-5
    human_demo_required BOOLEAN DEFAULT FALSE
);
```

### Extracted Code (python)

```python
import sqlite3
from pathlib import Path

class PhysicalAISkillDB:
    def __init__(self, db_path="physical_ai_skills.db"):
        self.conn = sqlite3.connect(db_path)
        self.create_schema()
    
    def create_schema(self):
        # 위 SQL 스키마 실행
        pass
    
    def import_esco_skills(self, esco_csv_path):
        """ESCO CSV를 Physical AI 관점으로 필터링하여 import"""
        # Physical AI 관련 키워드로 필터링
        keywords = [
            'robot', 'vision', 'sensor', 'control',
            'manipulation', 'perception', 'actuator',
            'machine learning', 'computer vision'
        ]
        pass
    
    def add_physical_ai_extensions(self, skill_id, **kwargs):
        """Physical AI 특화 속성 추가"""
        pass
```

### Extracted Code (python)

```python
from sqlalchemy import create_engine
from pgvector.sqlalchemy import Vector

class AdvancedPhysicalAIDB:
    def __init__(self, connection_string):
        self.engine = create_engine(connection_string)
        self.setup_vector_search()
    
    def setup_vector_search(self):
        """임베딩 기반 시맨틱 검색 설정"""
        # CREATE EXTENSION vector;
        # ALTER TABLE esco_skills ADD COLUMN embedding vector(768);
        pass
    
    def semantic_skill_search(self, query, top_k=10):
        """자연어 쿼리로 관련 스킬 검색"""
        # OpenAI embedding + cosine similarity
        pass
```

### Extracted Code (cypher)

```cypher
// Neo4j 그래프 모델
(s:Skill {id: "robot_manipulation", label: "로봇 매니퓰레이션"})
-[:REQUIRES]->
(k:Knowledge {id: "kinematics", label: "기구학"})

(s)-[:BROADER_THAN]->(s2:Skill {id: "pick_and_place"})
(s)-[:RELATED_TO {strength: 0.8}]->(s3:Skill {id: "computer_vision"})
```

### Extracted Code (text)

```text
Phase 1: SQLite + Manual Curation (1-2주)
↓
Phase 2: PostgreSQL Migration + 자동화 (1개월)
↓
Phase 3: Neo4j Integration (필요시)
```

### Extracted Code (bash)

```bash
# 1. ESCO 데이터 다운로드
wget https://esco.ec.europa.eu/en/use-esco/download

# 2. Physical AI 관련 스킬 필터링
python filter_esco_for_physical_ai.py

# 3. SQLite DB 초기화
python init_database.py
```

### Extracted Code (python)

```python
# Physical AI 도메인 전문가 지식 추가
domains = [
    "Robotic Manipulation",
    "Mobile Robotics",
    "Human-Robot Interaction",
    "Vision-based Control",
    "Force Control",
    "Learning from Demonstration"
]

for domain in domains:
    enrich_domain_skills(domain)
```

### Extracted Code (json)

```json
{
  "skill_id": "phys_ai_001",
  "esco_uri": "http://data.europa.eu/esco/skill/...",
  "label": "6-DOF Manipulator Control",
  "type": "skill",
  "description": "능동적으로 6자유도 로봇 팔의 관절을 제어하여...",
  "prerequisites": ["kinematics", "inverse_kinematics", "trajectory_planning"],
  "related_occupations": ["robotics_engineer", "automation_specialist"],
  "physical_ai_specific": {
    "hardware": ["UR5", "Franka Emika Panda"],
    "sensors": ["joint_encoders", "force_torque_sensor"],
    "real_time": true,
    "safety_critical": true
  },
  "learning_path": {
    "theory_hours": 20,
    "simulation_hours": 40,
    "hardware_hours": 20,
    "total": 80
  }
}
```

### Extracted Code (text)

```text
ESCO 데이터베이스에서 산업용 로봇 관련 역량을 추출하고 Physical AI에 특화된 
SQLite 데이터베이스를 구축해줘.

[필수 요구사항]
1. ESCO Skills API 또는 CSV 데이터 다운로드
2. 산업용 로봇 관련 키워드로 필터링:
   - 핵심: robot, robotics, automation, manipulator, industrial robot
   - 기술: welding robot, assembly robot, pick and place, palletizing
   - 지식: kinematics, dynamics, PLC, motion control, safety standards
   - 센서: vision system, force sensor, encoder, proximity sensor
   - 제어: PID control, trajectory planning, inverse kinematics
   - 프로그래밍: robot programming, teach pendant, offline programming

3. 필터링 기준:
   - ESCO 스킬 중 relevance score > 0.6 이상
   - 제조업, 자동화, 로봇공학 occupation과 연결된 스킬
   - ISO 표준(ISO 10218, ISO/TS 15066) 관련 안전 역량 포함

[출력물]
- physical_ai_skills.db (SQLite)
- data_statistics.json (수집된 데이터 통계)
- filtering_log.txt (필터링 과정 로그)
```

### Extracted Code (text)

```text
다음 스키마로 SQLite 데이터베이스를 생성해줘:

-- 테이블 1: 핵심 스킬 테이블
CREATE TABLE esco_skills (
    skill_id TEXT PRIMARY KEY,
    skill_uri TEXT UNIQUE,
    preferred_label TEXT NOT NULL,
    alt_labels TEXT, -- JSON array format
    description TEXT,
    skill_type TEXT CHECK(skill_type IN ('skill', 'knowledge', 'competence')),
    esco_level INTEGER CHECK(esco_level BETWEEN 1 AND 8),
    industrial_robot_relevance FLOAT CHECK(industrial_robot_relevance BETWEEN 0 AND 1),
    source TEXT DEFAULT 'ESCO',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 테이블 2: 스킬 계층 구조
CREATE TABLE skill_hierarchies (
    hierarchy_id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_skill_id TEXT NOT NULL,
    child_skill_id TEXT NOT NULL,
    relationship_type TEXT CHECK(relationship_type IN ('broader', 'narrower', 'related', 'prerequisite')),
    strength FLOAT DEFAULT 1.0,
    FOREIGN KEY (parent_skill_id) REFERENCES esco_skills(skill_id),
    FOREIGN KEY (child_skill_id) REFERENCES esco_skills(skill_id),
    UNIQUE(parent_skill_id, child_skill_id, relationship_type)
);

-- 테이블 3: 산업용 로봇 도메인 클러스터
CREATE TABLE domain_clusters (
    cluster_id TEXT PRIMARY KEY,
    cluster_name TEXT NOT NULL,
    description TEXT,
    parent_cluster_id TEXT,
    robot_application_area TEXT, -- welding, assembly, material_handling, etc.
    FOREIGN KEY (parent_cluster_id) REFERENCES domain_clusters(cluster_id)
);

-- 테이블 4: 스킬-클러스터 매핑
CREATE TABLE skill_cluster_mapping (
    mapping_id INTEGER PRIMARY KEY AUTOINCREMENT,
    skill_id TEXT NOT NULL,
    cluster_id TEXT NOT NULL,
    centrality_score FLOAT DEFAULT 0.5,
    is_core_skill BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (skill_id) REFERENCES esco_skills(skill_id),
    FOREIGN KEY (cluster_id) REFERENCES domain_clusters(cluster_id),
    UNIQUE(skill_id, cluster_id)
);

-- 테이블 5: Physical AI 특화 확장 속성
CREATE TABLE industrial_robot_extensions (
    skill_id TEXT PRIMARY KEY,
    
    -- 하드웨어 요구사항
    requires_physical_robot BOOLEAN DEFAULT FALSE,
    simulation_capable BOOLEAN DEFAULT TRUE,
    robot_brands TEXT, -- JSON: ["ABB", "FANUC", "KUKA", "Yaskawa"]
    robot_types TEXT, -- JSON: ["6-axis", "SCARA", "Delta", "Collaborative"]
    
    -- 상호작용 특성
    primary_sensors TEXT, -- JSON: ["vision", "force_torque", "tactile"]
    actuation_category TEXT, -- manipulation, material_handling, welding, etc.
    workspace_type TEXT CHECK(workspace_type IN ('fixed', 'mobile', 'collaborative')),
    
    -- 복잡도 및 안전성
    real_time_critical BOOLEAN DEFAULT FALSE,
    safety_critical BOOLEAN DEFAULT FALSE,
    iso_standard_required TEXT, -- JSON: ["ISO 10218-1", "ISO/TS 15066"]
    risk_assessment_level TEXT CHECK(risk_assessment_level IN ('low', 'medium', 'high', 'critical')),
    
    -- 학습 특성
    typical_training_hours INTEGER,
    hands_on_practice_required BOOLEAN DEFAULT TRUE,
    certification_available BOOLEAN DEFAULT FALSE,
    prerequisite_skills TEXT, -- JSON array of skill_ids
    
    -- 직무 연관성
    hr_job_families TEXT, -- JSON: ["Manufacturing Engineer", "Automation Technician"]
    seniority_level TEXT CHECK(seniority_level IN ('entry', 'intermediate', 'advanced', 'expert')),
    
    FOREIGN KEY (skill_id) REFERENCES esco_skills(skill_id)
);

-- 테이블 6: 학습 경로
CREATE TABLE learning_pathways (
    pathway_id TEXT PRIMARY KEY,
    pathway_name TEXT NOT NULL,
    pathway_description TEXT,
    target_role TEXT, -- "Robot Programmer", "Automation Engineer", etc.
    difficulty_level TEXT CHECK(difficulty_level IN ('beginner', 'intermediate', 'advanced')),
    estimated_total_hours INTEGER,
    sequence_order TEXT, -- JSON array: [{skill_id, order, estimated_hours}]
    prerequisites TEXT, -- JSON array of pathway_ids
    industry_certifications TEXT, -- JSON: 관련 산업 자격증
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 테이블 7: 직업-스킬 매핑 (HR용)
CREATE TABLE occupation_skill_requirements (
    requirement_id INTEGER PRIMARY KEY AUTOINCREMENT,
    occupation_code TEXT NOT NULL, -- ISCO-08 or O*NET code
    occupation_title TEXT NOT NULL,
    skill_id TEXT NOT NULL,
    proficiency_level TEXT CHECK(proficiency_level IN ('basic', 'intermediate', 'advanced', 'expert')),
    importance_rating INTEGER CHECK(importance_rating BETWEEN 1 AND 5),
    is_mandatory BOOLEAN DEFAULT FALSE,
    typical_years_experience INTEGER,
    FOREIGN KEY (skill_id) REFERENCES esco_skills(skill_id)
);

-- 테이블 8: 기업별 로봇 플랫폼 매핑
CREATE TABLE robot_platforms (
    platform_id TEXT PRIMARY KEY,
    manufacturer TEXT NOT NULL, -- ABB, FANUC, KUKA, etc.
    model_series TEXT,
    robot_type TEXT,
    payload_kg FLOAT,
    reach_mm INTEGER,
    programming_language TEXT, -- RAPID, Karel, KRL, etc.
    common_applications TEXT, -- JSON array
    market_share_percent FLOAT,
    documentation_url TEXT
);

-- 테이블 9: 스킬-플랫폼 호환성
CREATE TABLE skill_platform_compatibility (
    compatibility_id INTEGER PRIMARY KEY AUTOINCREMENT,
    skill_id TEXT NOT NULL,
    platform_id TEXT NOT NULL,
    compatibility_score FLOAT CHECK(compatibility_score BETWEEN 0 AND 1),
    notes TEXT,
    FOREIGN KEY (skill_id) REFERENCES esco_skills(skill_id),
    FOREIGN KEY (platform_id) REFERENCES robot_platforms(platform_id),
    UNIQUE(skill_id, platform_id)
);

-- 인덱스 생성
CREATE INDEX idx_skill_type ON esco_skills(skill_type);
CREATE INDEX idx_relevance ON esco_skills(industrial_robot_relevance);
CREATE INDEX idx_safety_critical ON industrial_robot_extensions(safety_critical);
CREATE INDEX idx_cluster_mapping ON skill_cluster_mapping(cluster_id);
CREATE INDEX idx_occupation ON occupation_skill_requirements(occupation_code);

[추가 지시사항]
- 각 테이블에 샘플 데이터 5-10개씩 삽입
- 외래 키 제약조건 활성화: PRAGMA foreign_keys = ON;
- 데이터 무결성 검증 쿼리 작성
```

### Extracted Code (text)

```text
다음 산업용 로봇 도메인 클러스터를 domain_clusters 테이블에 삽입해줘:

[1단계 클러스터 - 로봇 응용 분야]
1. Material Handling (자재 운반)
   - Pick and Place
   - Palletizing/Depalletizing
   - Machine Tending
   - Packaging

2. Welding and Joining (용접 및 접합)
   - Arc Welding
   - Spot Welding
   - Laser Welding
   - Adhesive Dispensing

3. Assembly Operations (조립 작업)
   - Precision Assembly
   - Screw Driving
   - Press Fitting
   - Component Insertion

4. Surface Treatment (표면 처리)
   - Painting and Coating
   - Polishing and Grinding
   - Deburring
   - Surface Inspection

5. Quality Control (품질 관리)
   - Vision Inspection
   - Dimensional Measurement
   - Defect Detection
   - Testing and Validation

[2단계 클러스터 - 기술 역량]
A. Robot Programming
   - Teach Pendant Programming
   - Offline Programming
   - Simulation and Virtual Commissioning

B. Sensor Integration
   - Vision Systems
   - Force/Torque Sensing
   - Proximity and Safety Sensors

C. Motion Control
   - Trajectory Planning
   - Path Optimization
   - Collision Avoidance

D. Safety and Standards
   - Risk Assessment
   - Safety System Design
   - ISO Standard Compliance

[데이터 형식 예시]
INSERT INTO domain_clusters VALUES (
    'mat_handling',
    'Material Handling',
    'Robot applications for moving, placing, and organizing materials',
    NULL,
    'material_handling'
);

INSERT INTO domain_clusters VALUES (
    'pick_place',
    'Pick and Place',
    'High-speed picking and precise placement operations',
    'mat_handling',
    'material_handling'
);

각 클러스터마다 관련 스킬들을 skill_cluster_mapping에 연결해줘.
```

### Extracted Code (text)

```text
ESCO API 또는 데이터셋에서 산업용 로봇 관련 스킬을 추출해줘.

[데이터 소스]
Option 1: ESCO API 사용
- Endpoint: https://esco.ec.europa.eu/api/
- 필요시 requests 라이브러리로 호출

Option 2: ESCO CSV 다운로드
- URL: https://esco.ec.europa.eu/en/use-esco/download
- skills_en.csv 파일 파싱

[필터링 로직]
import re
import json

CORE_KEYWORDS = [
    # 로봇 관련
    'robot', 'robotic', 'robotics', 'manipulator', 'industrial automation',
    
    # 제조 공정
    'welding', 'assembly', 'pick and place', 'palletizing', 'material handling',
    'machine tending', 'painting', 'coating', 'grinding', 'polishing',
    
    # 제어 기술
    'motion control', 'trajectory', 'kinematics', 'inverse kinematics',
    'PID control', 'servo', 'actuator', 'controller',
    
    # 센서 기술
    'vision system', 'computer vision', 'force sensor', 'torque sensor',
    'encoder', 'proximity sensor', 'laser scanner', '3D vision',
    
    # 프로그래밍
    'robot programming', 'teach pendant', 'offline programming', 
    'simulation', 'PLC programming', 'ladder logic',
    
    # 안전 및 표준
    'safety system', 'risk assessment', 'collaborative robot', 'cobot',
    'ISO 10218', 'ISO/TS 15066', 'safety standard',
    
    # 특정 브랜드/기술
    'ABB', 'FANUC', 'KUKA', 'Yaskawa', 'Universal Robots',
    'RAPID', 'Karel', 'KRL', 'RobotStudio', 'ROBOGUIDE'
]

def calculate_relevance_score(skill_label, skill_description):
    """
    스킬의 산업용 로봇 관련성 점수 계산 (0-1)
    """
    text = (skill_label + ' ' + skill_description).lower()
    
    matches = 0
    for keyword in CORE_KEYWORDS:
        if keyword.lower() in text:
            matches += 1
    
    # 정규화
    score = min(matches / 5.0, 1.0)
    
    # 가중치 적용
    if 'industrial robot' in text:
        score *= 1.2
    if 'automation' in text and 'manufacturing' in text:
        score *= 1.15
    
    return min(score, 1.0)

[실행 단계]
1. ESCO 데이터 로드
2. 각 스킬에 대해 relevance_score 계산
3. score > 0.6인 스킬만 esco_skills 테이블에 삽입
4. 스킬 간 계층 관계도 함께 추출하여 skill_hierarchies에 저장
5. 필터링 통계 출력:
   - 전체 ESCO 스킬 수
   - 필터링된 스킬 수
   - 상위 20개 키워드별 매칭 수
```

### Extracted Code (text)

```text
필터링된 각 스킬에 대해 industrial_robot_extensions 속성을 자동으로 추론하여 삽입해줘.

[추론 규칙]
def infer_robot_extensions(skill_label, skill_description, skill_type):
    extensions = {
        'skill_id': skill_id,
        'requires_physical_robot': False,
        'simulation_capable': True,
        'robot_brands': [],
        'robot_types': [],
        'primary_sensors': [],
        'actuation_category': None,
        'workspace_type': 'fixed',
        'real_time_critical': False,
        'safety_critical': False,
        'iso_standard_required': [],
        'risk_assessment_level': 'low',
        'typical_training_hours': 20,
        'hands_on_practice_required': False,
        'certification_available': False,
        'prerequisite_skills': [],
        'hr_job_families': [],
        'seniority_level': 'intermediate'
    }
    
    text = (skill_label + ' ' + skill_description).lower()
    
    # 하드웨어 요구사항
    if any(k in text for k in ['welding', 'assembly', 'painting', 'grinding']):
        extensions['requires_physical_robot'] = True
        extensions['hands_on_practice_required'] = True
    
    # 로봇 브랜드
    brands = ['ABB', 'FANUC', 'KUKA', 'Yaskawa', 'Universal Robots', 'Staubli']
    extensions['robot_brands'] = [b for b in brands if b.lower() in text]
    
    # 로봇 타입
    if '6-axis' in text or 'articulated' in text:
        extensions['robot_types'].append('6-axis')
    if 'scara' in text:
        extensions['robot_types'].append('SCARA')
    if 'collaborative' in text or 'cobot' in text:
        extensions['robot_types'].append('Collaborative')
        extensions['workspace_type'] = 'collaborative'
    
    # 센서
    if 'vision' in text or 'camera' in text:
        extensions['primary_sensors'].append('vision')
    if 'force' in text or 'torque' in text:
        extensions['primary_sensors'].append('force_torque')
    if 'tactile' in text or 'touch' in text:
        extensions['primary_sensors'].append('tactile')
    
    # 작업 카테고리
    if 'welding' in text:
        extensions['actuation_category'] = 'welding'
    elif 'pick' in text or 'place' in text:
        extensions['actuation_category'] = 'material_handling'
    elif 'assembly' in text:
        extensions['actuation_category'] = 'assembly'
    elif 'painting' in text or 'coating' in text:
        extensions['actuation_category'] = 'surface_treatment'
    
    # 실시간 및 안전
    if 'real-time' in text or 'real time' in text:
        extensions['real_time_critical'] = True
    
    if any(k in text for k in ['safety', 'hazard', 'risk', 'collision']):
        extensions['safety_critical'] = True
        extensions['risk_assessment_level'] = 'high'
    
    # ISO 표준
    if 'ISO 10218' in text or 'iso 10218' in text:
        extensions['iso_standard_required'].append('ISO 10218-1')
        extensions['iso_standard_required'].append('ISO 10218-2')
    if 'ISO/TS 15066' in text or 'ts 15066' in text:
        extensions['iso_standard_required'].append('ISO/TS 15066')
    
    # 교육 시간 추정
    if skill_type == 'knowledge':
        extensions['typical_training_hours'] = 10
    elif skill_type == 'competence':
        extensions['typical_training_hours'] = 40
    else:  # skill
        extensions['typical_training_hours'] = 20
    
    # 직무 매칭
    if 'programming' in text:
        extensions['hr_job_families'].append('Robot Programmer')
    if 'maintenance' in text:
        extensions['hr_job_families'].append('Maintenance Technician')
    if 'engineer' in text:
        extensions['hr_job_families'].append('Automation Engineer')
    
    # 숙련도
    if any(k in text for k in ['advanced', 'expert', 'senior']):
        extensions['seniority_level'] = 'advanced'
    elif any(k in text for k in ['basic', 'fundamental', 'introduction']):
        extensions['seniority_level'] = 'entry'
    
    return extensions

[실행]
- 모든 esco_skills에 대해 위 함수 실행
- industrial_robot_extensions 테이블에 삽입
- JSON 필드는 json.dumps()로 직렬화
```

### Extracted Code (text)

```text
주요 산업용 로봇 제조사 및 플랫폼 정보를 robot_platforms 테이블에 삽입해줘.

[입력 데이터]
1. ABB
   - IRB 1200 (5kg payload, 900mm reach, RAPID)
   - IRB 2600 (20kg, 1650mm, RAPID)
   - IRB 6700 (150-300kg, 2600-3200mm, RAPID)
   - YuMi (Collaborative, 0.5kg, 559mm, RAPID)

2. FANUC
   - M-10iA (12kg, 1420mm, Karel)
   - M-20iA (20kg, 1811mm, Karel)
   - R-2000iC (210-270kg, 2655-3095mm, Karel)
   - CR-15iA (Collaborative, 15kg, 1630mm, Karel)

3. KUKA
   - KR 3 AGILUS (3kg, 540mm, KRL)
   - KR 10 R1100 (10kg, 1100mm, KRL)
   - KR 210 R2700 (210kg, 2700mm, KRL)
   - LBR iiwa (Collaborative, 7-14kg, 820mm, Sunrise)

4. Yaskawa (Motoman)
   - GP7 (7kg, 927mm, INFORM)
   - GP12 (12kg, 1440mm, INFORM)
   - GP180 (180kg, 2700mm, INFORM)
   - HC10DT (Collaborative, 10kg, 1200mm, INFORM)

5. Universal Robots
   - UR3e (Collaborative, 3kg, 500mm, URScript)
   - UR5e (Collaborative, 5kg, 850mm, URScript)
   - UR10e (Collaborative, 10kg, 1300mm, URScript)
   - UR16e (Collaborative, 16kg, 900mm, URScript)

[데이터 형식]
INSERT INTO robot_platforms (
    platform_id, manufacturer, model_series, robot_type,
    payload_kg, reach_mm, programming_language, 
    common_applications, market_share_percent, documentation_url
) VALUES (
    'abb_irb1200',
    'ABB',
    'IRB 1200',
    '6-axis',
    5.0,
    900,
    'RAPID',
    '["assembly", "material_handling", "machine_tending"]',
    NULL,  -- 시장 점유율 데이터는 선택사항
    'https://new.abb.com/products/robotics/industrial-robots/irb-1200'
);

모든 주요 플랫폼 삽입 후, skill_platform_compatibility를 추론하여 삽입:
- 예: "RAPID programming" 스킬 → ABB 로봇들과 compatibility_score = 1.0
- 예: "Collaborative robot operation" → 모든 Cobot과 compatibility_score = 0.9
```

### Extracted Code (text)

```text
주요 직무별 학습 경로를 learning_pathways 테이블에 생성해줘.

[경로 1: Robot Operator (초급)]
- Target: 로봇 조작 및 기본 티칭
- Duration: 40시간
- Sequence:
  1. Industrial robot safety (8h)
  2. Robot coordinate systems (4h)
  3. Teach pendant operation (8h)
  4. Basic point teaching (12h)
  5. Emergency procedures (4h)
  6. Routine maintenance (4h)

[경로 2: Robot Programmer (중급)]
- Target: 로봇 프로그래밍 전문가
- Duration: 120시간
- Prerequisites: Robot Operator
- Sequence:
  1. Kinematics fundamentals (16h)
  2. RAPID/Karel/KRL programming (40h)
  3. I/O configuration (12h)
  4. Sensor integration (20h)
  5. Offline programming software (20h)
  6. Program optimization (12h)

[경로 3: Automation Engineer (고급)]
- Target: 자동화 시스템 설계
- Duration: 200시간
- Prerequisites: Robot Programmer
- Sequence:
  1. PLC programming (40h)
  2. Vision system integration (30h)
  3. Safety system design (30h)
  4. Multi-robot coordination (25h)
  5. System commissioning (35h)
  6. Troubleshooting (20h)
  7. ROI analysis (20h)

[데이터 형식]
INSERT INTO learning_pathways VALUES (
    'path_robot_operator',
    'Industrial Robot Operator',
    'Entry-level training for operating and teaching industrial robots',
    'Robot Operator',
    'beginner',
    40,
    '[
        {"skill_id": "safety_001", "order": 1, "estimated_hours": 8},
        {"skill_id": "coord_001", "order": 2, "estimated_hours": 4},
        {"skill_id": "teach_001", "order": 3, "estimated_hours": 8}
    ]',
    '[]',
    '["Certified Robot Operator (CRO)"]',
    CURRENT_TIMESTAMP
);
```

### Extracted Code (text)

```text
주요 로봇 관련 직업에 필요한 스킬을 occupation_skill_requirements에 매핑해줘.

[직업 목록]
1. Industrial Robot Operator (ISCO: 8159)
   - 필수: Safety procedures, Teach pendant, Basic maintenance
   - 중요도: 5
   - 숙련도: Basic-Intermediate
   - 경력: 0-2년

2. Robot Programmer (ISCO: 2512)
   - 필수: RAPID/Karel/KRL, Kinematics, Offline programming
   - 중요도: 5
   - 숙련도: Intermediate-Advanced
   - 경력: 2-5년

3. Robotics Technician (ISCO: 3119)
   - 필수: Troubleshooting, PLC, Sensor integration
   - 중요도: 4-5
   - 숙련도: Intermediate
   - 경력: 1-4년

4. Automation Engineer (ISCO: 2144)
   - 필수: System design, Multi-robot coordination, Vision systems
   - 중요도: 5
   - 숙련도: Advanced-Expert
   - 경력: 5-10년

5. Robot Maintenance Technician (ISCO: 7233)
   - 필수: Mechanical maintenance, Electrical systems, Diagnostics
   - 중요도: 4-5
   - 숙련도: Intermediate-Advanced
   - 경력: 2-6년

[데이터 형식]
INSERT INTO occupation_skill_requirements (
    occupation_code, occupation_title, skill_id,
    proficiency_level, importance_rating, is_mandatory, typical_years_experience
) VALUES (
    '8159', 'Industrial Robot Operator', 'safety_iso10218',
    'intermediate', 5, TRUE, 1
);

각 직업당 10-20개의 핵심 스킬을 매핑해줘.
```

### Extracted Code (text)

```text
데이터베이스 검증 및 HR/엔지니어용 분석 쿼리를 작성해줘.

[검증 쿼리]
-- 1. 전체 데이터 통계
SELECT 
    'Total Skills' as metric,
    COUNT(*) as count
FROM esco_skills
UNION ALL
SELECT 
    'By Type: ' || skill_type,
    COUNT(*)
FROM esco_skills
GROUP BY skill_type
UNION ALL
SELECT
    'Safety Critical',
    COUNT(*)
FROM industrial_robot_extensions
WHERE safety_critical = TRUE;

-- 2. 고립된 스킬 찾기 (클러스터 미매핑)
SELECT s.skill_id, s.preferred_label
FROM esco_skills s
LEFT JOIN skill_cluster_mapping scm ON s.skill_id = scm.skill_id
WHERE scm.skill_id IS NULL
LIMIT 10;

-- 3. 순환 참조 검증
WITH RECURSIVE hierarchy_check AS (
    SELECT parent_skill_id, child_skill_id, 1 as depth
    FROM skill_hierarchies
    UNION ALL
    SELECT h.parent_skill_id, sh.child_skill_id, h.depth + 1
    FROM hierarchy_check h
    JOIN skill_hierarchies sh ON h.child_skill_id = sh.parent_skill_id
    WHERE h.depth < 10
)
SELECT DISTINCT parent_skill_id, child_skill_id
FROM hierarchy_check
WHERE parent_skill_id = child_skill_id;

[HR용 분석 쿼리]
-- Q1. 특정 직무에 필요한 모든 스킬 조회
SELECT 
    s.preferred_label as skill_name,
    osr.proficiency_level,
    osr.importance_rating,
    osr.is_mandatory,
    ire.typical_training_hours,
    ire.certification_available
FROM occupation_skill_requirements osr
JOIN esco_skills s ON osr.skill_id = s.skill_id
JOIN industrial_robot_extensions ire ON s.skill_id = ire.skill_id
WHERE osr.occupation_code = '2512'  -- Robot Programmer
ORDER BY osr.importance_rating DESC, osr.is_mandatory DESC;

-- Q2. 학습 경로 추천 (초급 → 고급)
SELECT 
    pathway_name,
    target_role,
    difficulty_level,
    estimated_total_hours,
    json_extract(prerequisites, '$') as prerequisites
FROM learning_pathways
ORDER BY 
    CASE difficulty_level
        WHEN 'beginner' THEN 1
        WHEN 'intermediate' THEN 2
        WHEN 'advanced' THEN 3
    END;

-- Q3. 안전 필수 스킬 목록
SELECT 
    s.preferred_label,
    s.description,
    ire.iso_standard_required,
    ire.risk_assessment_level
FROM esco_skills s
JOIN industrial_robot_extensions ire ON s.skill_id = ire.skill_id
WHERE ire.safety_critical = TRUE
ORDER BY 
    CASE ire.risk_assessment_level
        WHEN 'critical' THEN 1
        WHEN 'high' THEN 2
        WHEN 'medium' THEN 3
        WHEN 'low' THEN 4
    END;

[엔지니어용 분석 쿼리]
-- Q4. 특정 로봇 플랫폼에 필요한 스킬
SELECT 
    s.preferred_label as skill_name,
    s.skill_type,
    spc.compatibility_score,
    ire.typical_training_hours
FROM robot_platforms rp
JOIN skill_platform_compatibility spc ON rp.platform_id = spc.platform_id
JOIN esco_skills s ON spc.skill_id = s.skill_id
JOIN industrial_robot_extensions ire ON s.skill_id = ire.skill_id
WHERE rp.manufacturer = 'ABB' AND rp.model_series LIKE 'IRB%'
ORDER BY spc.compatibility_score DESC
LIMIT 20;

-- Q5. 특정 응용 분야의 스킬 클러스터
SELECT 
    dc.cluster_name,
    COUNT(DISTINCT scm.skill_id) as skill_count,
    GROUP_CONCAT(DISTINCT s.preferred_label, ' | ') as sample_skills
FROM domain_clusters dc
JOIN skill_cluster_mapping scm ON dc.cluster_id = scm.cluster_id
JOIN esco_skills s ON scm.skill_id = s.skill_id
WHERE dc.robot_application_area = 'welding'
GROUP BY dc.cluster_id, dc.cluster_name
ORDER BY skill_count DESC;

-- Q6. 센서별 필요 역량
SELECT 
    json_each.value as sensor_type,
    COUNT(DISTINCT s.skill_id) as related_skills,
    AVG(ire.typical_training_hours) as avg_training_hours
FROM industrial_robot_extensions ire
JOIN esco_skills s ON ire.skill_id = s.skill_id
CROSS JOIN json_each(ire.primary_sensors)
GROUP BY sensor_type
ORDER BY related_skills DESC;

모든 쿼리를 validation_queries.sql 파일로 저장하고,
각 쿼리 실행 결과를 validation_results.json에 저장해줘.
```

### Extracted Code (text)

```text
다음 파일들을 생성하고 정리해줘:

1. physical_ai_skills.db
   - 완성된 SQLite 데이터베이스

2. README.md
   - 데이터베이스 개요
   - 테이블 스키마 설명
   - 사용 예시 (Python/SQL)
   - HR 및 엔지니어를 위한 가이드

3. data_dictionary.json
   {
       "tables": {
           "esco_skills": {
               "description": "...",
               "row_count": 1234,
               "columns": {...}
           }
       }
   }

4. statistics_report.md
   - 수집된 스킬 통계
   - 도메인별 분포
   - 제조사별 플랫폼 수
   - 학습 경로 요약

5. sample_queries.sql
   - HR용 쿼리 10개
   - 엔지니어용 쿼리 10개
   - 주석 포함

6. quick_start_guide.md
   - 5분 만에 시작하기
   - Python 연결 예제
   - 주요 쿼리 실행 가이드

7. hr_dashboard_queries.sql
   - 채용 공고 작성용 쿼리
   - 역량 갭 분석 쿼리
   - 교육 계획 수립 쿼리

[최종 검증 체크리스트]
□ 모든 외래 키 제약조건 통과
□ 중복 데이터 없음
□ 모든 JSON 필드 유효성 검증
□ 샘플 쿼리 실행 성공
□ 문서화 완료
□ 백업 파일 생성

최종 작업 완료 후 다음 메시지 출력:
"✅ Physical AI 역량 DB 구축 완료!
  - 데이터베이스: physical_ai_skills.db
  - 총 스킬 수: [N]개
  - 로봇 플랫폼: [M]개
  - 학습 경로: [K]개
  
📊 다음 명령으로 데이터 탐색:
  sqlite3 physical_ai_skills.db
  .tables
  .schema esco_skills
  
📖 상세 가이드: README.md 참조"
```
