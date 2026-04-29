# Extracted Knowledge from Conv: 61b93d4d-001c-4776-a63c-76e85fe4ccff

**Date**: 2025-11-20T23:26:43.234586Z

### Extracted Code (text)

```text
Employee:
- hasEmployeeID: string
- hasName: string
- hasEmail: string
- hasYearsOfExperience: integer
- hasJoinDate: date

Skill:
- hasSkillName: string
- hasSkillDescription: string
- hasDifficultyLevel: integer (1-5)
- hasMarketDemand: float

SkillProficiency (스킬 숙련도):
- hasProficiencyLevel: integer (1-5)
  * 1: Beginner (초급)
  * 2: Elementary (초중급)
  * 3: Intermediate (중급)
  * 4: Advanced (고급)
  * 5: Expert (전문가)
- hasAcquiredDate: date
- hasLastUsedDate: date
- hasCertified: boolean
```

### Extracted Code (text)

```text
Employee와 Skill 관계:
- hasProficiency (직원이 스킬 숙련도를 가짐)
  Domain: Employee
  Range: SkillProficiency
  
- wantsToLearn (학습 희망 스킬)
  Domain: Employee
  Range: Skill

Job과 Skill 관계:
- requiresSkill (필수 스킬)
  Domain: Job
  Range: Skill
  
- prefersSkill (우대 스킬)
  Domain: Job
  Range: Skill

Skill 간 관계:
- isPrerequisiteOf (선수 스킬)
  예: Java isPrerequisiteOf Spring
  
- isRelatedTo (연관 스킬)
  예: React isRelatedTo JavaScript
  
- isAlternativeTo (대체 가능 스킬)
  예: MySQL isAlternativeTo PostgreSQL

Learning 관계:
- teachesSkill
  Domain: Course
  Range: Skill
  
- hasCompleted
  Domain: Employee
  Range: Course

Project 관계:
- usedSkillIn
  Domain: Employee
  Range: Project
  
- requiresSkillFor
  Domain: Project
  Range: Skill
```

### Extracted Code (text)

```text
# 스킬 인스턴스
Skill_Java:
  rdf:type TechnicalSkill, ProgrammingLanguage
  hasSkillName "Java"
  hasDifficultyLevel 3
  hasMarketDemand 0.85

Skill_Spring:
  rdf:type TechnicalSkill, Framework
  hasSkillName "Spring Framework"
  hasDifficultyLevel 4
  isPrerequisiteOf Skill_Java

# 직원 인스턴스
Employee_김철수:
  rdf:type Employee, Developer
  hasEmployeeID "EMP001"
  hasName "김철수"
  hasYearsOfExperience 5
  
  hasProficiency [
    a SkillProficiency;
    forSkill Skill_Java;
    hasProficiencyLevel 4;
    hasAcquiredDate "2020-03-15";
    hasCertified true
  ]
  
  hasProficiency [
    a SkillProficiency;
    forSkill Skill_Spring;
    hasProficiencyLevel 3;
    hasAcquiredDate "2021-06-20";
  ]
  
  wantsToLearn Skill_Kubernetes

# 직무 인스턴스
Job_SeniorBackendDev:
  rdf:type JobPosition
  hasJobTitle "Senior Backend Developer"
  
  requiresSkill Skill_Java [
    minimumLevel 4;
    yearsRequired 3
  ]
  
  requiresSkill Skill_Spring [
    minimumLevel 3;
    yearsRequired 2
  ]
  
  prefersSkill Skill_AWS
  prefersSkill Skill_Kubernetes

# 교육 과정 인스턴스
Course_SpringMaster:
  rdf:type Course
  hasCourseName "Spring Framework 마스터"
  hasDuration 40
  teachesSkill Skill_Spring
  improvesLevelBy 1
```

### Extracted Code (text)

```text
# 숙련도 진행 규칙
Rule 1: 스킬 레벨 순서
IF Employee hasProficiency Skill_A with level 4
AND Skill_B isPrerequisiteOf Skill_A
THEN Employee MUST have hasProficiency Skill_B with level >= 3

# 직무 매칭 규칙
Rule 2: 직무 적합성
IF Job requiresSkill Skill_X with minimumLevel N
AND Employee hasProficiency Skill_X with level >= N
THEN Employee isQualifiedFor Job (부분 적격)

Rule 3: 완전 매칭
IF Job requiresSkill {Skill_1, Skill_2, ..., Skill_n}
AND Employee hasProficiency ALL of {Skill_1, Skill_2, ..., Skill_n}
    with appropriate levels
THEN Employee isFullyQualifiedFor Job

# 학습 추천 규칙
Rule 4: 다음 학습 추천
IF Employee hasProficiency Skill_A with level >= 3
AND Skill_B isPrerequisiteOf Skill_A
AND Employee NOT hasProficiency Skill_C
AND Skill_A isPrerequisiteOf Skill_C
THEN RECOMMEND Skill_C to Employee

# 경력 개발 규칙
Rule 5: 경력 패스
IF Employee hasYearsOfExperience >= 5
AND Employee hasProficiency {Java:4, Spring:4, AWS:3}
AND JobRole_Architect requires {Java:4, Spring:4, AWS:3, Kubernetes:3}
THEN SUGGEST Course_Kubernetes to Employee
```

### Extracted Code (text)

```text
QUERY: 김철수가 "Senior Backend Developer" 포지션에 지원하려면 
       무엇이 부족한가?

온톨로지 추론:
1. Job_SeniorBackendDev requiresSkill:
   - Java (level 4, 3 years) ✓ 김철수: level 4, 5년 경력
   - Spring (level 3, 2 years) ✓ 김철수: level 3, 2년 경력
   
2. Job_SeniorBackendDev prefersSkill:
   - AWS ✗ 김철수: 보유하지 않음
   - Kubernetes ✗ 김철수: wantsToLearn 표시

결과: 필수 스킬은 만족하나, 우대 스킬 2개 부족
추천: AWS, Kubernetes 교육 과정 수강
```

### Extracted Code (text)

```text
QUERY: React 프로젝트에 적합한 팀원 찾기

온톨로지 추론:
1. React isPrerequisiteOf JavaScript
2. React isRelatedTo {HTML, CSS, Redux}

3. 직원 검색:
   - Employee hasProficiency JavaScript (level >= 3)
   - Employee hasProficiency React (level >= 2)
   
4. 보너스 점수:
   - Employee hasProficiency Redux (+10점)
   - Employee hasCompleted Course_ReactAdvanced (+5점)

결과: 자격을 갖춘 직원 목록 + 적합도 점수
```

### Extracted Code (text)

```text
QUERY: 초급 개발자가 클라우드 아키텍트가 되려면?

온톨로지 추론:
1. JobRole_CloudArchitect requiresSkill:
   - Java (4), Python (3), AWS (4), Docker (3), Kubernetes (4)

2. 선수 관계 추적:
   - Kubernetes isPrerequisiteOf Docker (3)
   - Docker isPrerequisiteOf Linux (2)
   - AWS_Advanced isPrerequisiteOf AWS_Basics (3)

3. 학습 경로 생성:
   Step 1: Linux Fundamentals (2개월)
   Step 2: Python Basics (2개월)
   Step 3: Docker Essentials (1개월)
   Step 4: AWS Basics (3개월)
   Step 5: Java Advanced (4개월)
   Step 6: AWS Advanced (3개월)
   Step 7: Kubernetes Mastery (4개월)
   
   총 예상 기간: 19개월
```

### Extracted Code (xml)

```xml
<owl:Class rdf:about="#Employee">
  <rdfs:subClassOf rdf:resource="#Person"/>
</owl:Class>

<owl:ObjectProperty rdf:about="#hasProficiency">
  <rdfs:domain rdf:resource="#Employee"/>
  <rdfs:range rdf:resource="#SkillProficiency"/>
</owl:ObjectProperty>

<owl:DatatypeProperty rdf:about="#hasProficiencyLevel">
  <rdfs:domain rdf:resource="#SkillProficiency"/>
  <rdfs:range rdf:resource="&xsd;integer"/>
  <owl:minInclusive rdf:datatype="&xsd;integer">1</owl:minInclusive>
  <owl:maxInclusive rdf:datatype="&xsd;integer">5</owl:maxInclusive>
</owl:DatatypeProperty>

<owl:TransitiveProperty rdf:about="#isPrerequisiteOf"/>
```

### Extracted Code (xml)

```xml
<?xml version="1.0"?>
<rdf:RDF xmlns="http://www.example.org/hr-skills#"
     xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
     xmlns:owl="http://www.w3.org/2002/07/owl#"
     xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#">
    
    <owl:Class rdf:about="#Employee">
        <rdfs:subClassOf rdf:resource="#Person"/>
        <rdfs:label>직원</rdfs:label>
    </owl:Class>
    
    <owl:ObjectProperty rdf:about="#hasProficiency">
        <rdfs:domain rdf:resource="#Employee"/>
        <rdfs:range rdf:resource="#SkillProficiency"/>
    </owl:ObjectProperty>
</rdf:RDF>
```

### Extracted Code (turtle)

```turtle
@prefix : <http://www.example.org/hr-skills#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Employee a owl:Class ;
    rdfs:subClassOf :Person ;
    rdfs:label "직원" .

:hasProficiency a owl:ObjectProperty ;
    rdfs:domain :Employee ;
    rdfs:range :SkillProficiency .

:김철수 a :Employee ;
    :hasEmployeeID "EMP001" ;
    :hasProficiency :김철수_Java숙련도 .
```

### Extracted Code (json)

```json
{
  "@context": {
    "@vocab": "http://www.example.org/hr-skills#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#"
  },
  "@graph": [
    {
      "@id": "Employee",
      "@type": "owl:Class",
      "rdfs:subClassOf": {"@id": "Person"},
      "rdfs:label": "직원"
    }
  ]
}
```

### Extracted Code (bash)

```bash
# https://protege.stanford.edu/ 에서 다운로드
# 윈도우: protege-X.X.X-win.zip
# 맥: protege-X.X.X-mac.zip
# 리눅스: protege-X.X.X-linux.zip
```

### Extracted Code (text)

```text
Thing
├── Person
│   ├── Employee
│   │   ├── Developer
│   │   └── Designer
│   └── Candidate
└── Skill
    ├── TechnicalSkill
    └── SoftSkill
```

### Extracted Code (python)

```python
# 설치
pip install owlready2

# 기본 사용법
from owlready2 import *

# 온톨로지 생성
onto = get_ontology("http://test.org/hr-skills.owl")

with onto:
    # 클래스 정의
    class Person(Thing):
        pass
    
    class Employee(Person):
        pass
    
    class Skill(Thing):
        pass
    
    # 속성 정의
    class hasProficiency(ObjectProperty):
        domain = [Employee]
        range = [Skill]
    
    class hasEmployeeID(DataProperty, FunctionalProperty):
        domain = [Employee]
        range = [str]
    
    class hasProficiencyLevel(DataProperty):
        domain = [Skill]
        range = [int]
    
    # 인스턴스 생성
    java = Skill("Java")
    
    김철수 = Employee("김철수")
    김철수.hasEmployeeID = ["EMP001"]
    김철수.hasProficiency = [java]
    
    # 규칙 정의
    class AdvancedDeveloper(Employee):
        equivalent_to = [Employee & 
                        hasProficiency.some(Skill & 
                        hasProficiencyLevel.value(5))]

# 추론 실행
sync_reasoner_pellet(infer_property_values=True)

# 결과 확인
print(list(AdvancedDeveloper.instances()))

# 저장
onto.save(file="hr_skills.owl", format="rdfxml")
```

### Extracted Code (python)

```python
from owlready2 import *

# 온톨로지 로드 또는 생성
onto = get_ontology("http://example.org/hr-skills.owl")

with onto:
    # === 클래스 정의 ===
    class Skill(Thing):
        pass
    
    class TechnicalSkill(Skill):
        pass
    
    class ProgrammingLanguage(TechnicalSkill):
        pass
    
    class Framework(TechnicalSkill):
        pass
    
    class Person(Thing):
        pass
    
    class Employee(Person):
        pass
    
    class Job(Thing):
        pass
    
    # === 속성 정의 ===
    class hasProficiency(ObjectProperty):
        domain = [Employee]
        range = [Skill]
    
    class requiresSkill(ObjectProperty):
        domain = [Job]
        range = [Skill]
    
    class isPrerequisiteOf(ObjectProperty, TransitiveProperty):
        domain = [Skill]
        range = [Skill]
    
    class hasSkillLevel(DataProperty, FunctionalProperty):
        domain = [Skill]
        range = [int]
    
    class hasYearsOfExperience(DataProperty):
        domain = [Employee]
        range = [int]
    
    # === 추론 규칙 ===
    class SeniorDeveloper(Employee):
        equivalent_to = [
            Employee & 
            hasYearsOfExperience.some(ConstrainedDatatype(int, min_inclusive=5)) &
            hasProficiency.min(3, Skill)
        ]
    
    # === 인스턴스 생성 ===
    # 스킬
    java = ProgrammingLanguage("Java")
    java.hasSkillLevel = 3
    
    spring = Framework("Spring")
    spring.hasSkillLevel = 4
    spring.isPrerequisiteOf = [java]  # Spring은 Java 선수지식 필요
    
    python = ProgrammingLanguage("Python")
    python.hasSkillLevel = 2
    
    # 직원
    emp1 = Employee("김철수")
    emp1.hasYearsOfExperience = 6
    emp1.hasProficiency = [java, spring, python]
    
    emp2 = Employee("이영희")
    emp2.hasYearsOfExperience = 3
    emp2.hasProficiency = [python]
    
    # 직무
    backend_job = Job("BackendDeveloper")
    backend_job.requiresSkill = [java, spring]

# === 쿼리 예제 ===

# 1. Spring을 다루는 직원 찾기
print("Spring 보유 직원:")
for emp in onto.search(type=Employee, hasProficiency=spring):
    print(f"  - {emp.name}")

# 2. 선수 지식이 있는 스킬 찾기 (추이적 속성 활용)
sync_reasoner_pellet(infer_property_values=True)
print(f"\nSpring의 모든 선수 스킬:")
for skill in spring.INDIRECT_isPrerequisiteOf:
    print(f"  - {skill.name}")

# 3. Senior Developer 자동 분류
print("\nSenior Developers:")
for dev in SeniorDeveloper.instances():
    print(f"  - {dev.name} ({dev.hasYearsOfExperience}년 경력)")

# 4. 특정 직무에 적합한 직원 찾기
print("\nBackend Developer 직무 적격자:")
required_skills = backend_job.requiresSkill
for emp in Employee.instances():
    emp_skills = set(emp.hasProficiency)
    if set(required_skills).issubset(emp_skills):
        print(f"  - {emp.name}")

# === SPARQL 쿼리 ===
graph = default_world.as_rdflib_graph()
query = """
    PREFIX hr: <http://example.org/hr-skills.owl#>
    
    SELECT ?employee ?skill
    WHERE {
        ?employee a hr:Employee .
        ?employee hr:hasProficiency ?skill .
        ?skill a hr:ProgrammingLanguage .
    }
"""
results = list(graph.query(query))
print("\n프로그래밍 언어를 보유한 직원:")
for row in results:
    print(f"  - {row[0].split('#')[1]}: {row[1].split('#')[1]}")

# 저장
onto.save(file="hr_skills.owl", format="rdfxml")
```

### Extracted Code (python)

```python
from rdflib import Graph, Namespace, RDF, RDFS, OWL, Literal, URIRef
from rdflib.namespace import XSD

# 그래프 생성
g = Graph()

# 네임스페이스 정의
HR = Namespace("http://example.org/hr-skills#")
g.bind("hr", HR)
g.bind("owl", OWL)

# 클래스 정의
g.add((HR.Employee, RDF.type, OWL.Class))
g.add((HR.Skill, RDF.type, OWL.Class))

# 속성 정의
g.add((HR.hasProficiency, RDF.type, OWL.ObjectProperty))
g.add((HR.hasProficiency, RDFS.domain, HR.Employee))
g.add((HR.hasProficiency, RDFS.range, HR.Skill))

# 인스턴스 생성
emp1 = HR.김철수
g.add((emp1, RDF.type, HR.Employee))
g.add((emp1, HR.hasEmployeeID, Literal("EMP001", datatype=XSD.string)))

java = HR.Java
g.add((java, RDF.type, HR.Skill))
g.add((emp1, HR.hasProficiency, java))

# SPARQL 쿼리
query = """
    SELECT ?emp ?skill
    WHERE {
        ?emp hr:hasProficiency ?skill .
    }
"""
results = g.query(query)
for row in results:
    print(f"{row.emp} has skill {row.skill}")

# 저장
g.serialize(destination="hr_skills.ttl", format="turtle")
g.serialize(destination="hr_skills.xml", format="xml")
g.serialize(destination="hr_skills.json", format="json-ld")
```

### Extracted Code (python)

```python
# hr_skills_manager.py
from owlready2 import *
import json

class HRSkillsOntology:
    def __init__(self, owl_file="hr_skills.owl"):
        self.onto = get_ontology(owl_file).load()
        
    def add_employee(self, emp_id, name, skills):
        """새 직원과 스킬 추가"""
        with self.onto:
            emp = self.onto.Employee(name)
            emp.hasEmployeeID = [emp_id]
            
            for skill_name in skills:
                skill = self.onto.search_one(iri=f"*{skill_name}")
                if skill:
                    emp.hasProficiency.append(skill)
        
        self.onto.save()
        
    def find_qualified_employees(self, job_title):
        """직무에 적합한 직원 찾기"""
        job = self.onto.search_one(iri=f"*{job_title}")
        if not job:
            return []
        
        required = set(job.requiresSkill)
        qualified = []
        
        for emp in self.onto.Employee.instances():
            emp_skills = set(emp.hasProficiency)
            if required.issubset(emp_skills):
                qualified.append({
                    'name': emp.name,
                    'id': emp.hasEmployeeID[0],
                    'skills': [s.name for s in emp.hasProficiency]
                })
        
        return qualified
    
    def recommend_learning_path(self, employee_name, target_job):
        """학습 경로 추천"""
        emp = self.onto.search_one(iri=f"*{employee_name}")
        job = self.onto.search_one(iri=f"*{target_job}")
        
        if not emp or not job:
            return None
        
        current = set(emp.hasProficiency)
        required = set(job.requiresSkill)
        gap = required - current
        
        # 선수 지식 고려한 학습 순서
        learning_path = []
        for skill in gap:
            prereqs = list(skill.INDIRECT_isPrerequisiteOf)
            learning_path.append({
                'skill': skill.name,
                'prerequisites': [p.name for p in prereqs]
            })
        
        return learning_path

# 사용 예시
manager = HRSkillsOntology()

# 직원 추가
manager.add_employee("EMP002", "박민수", ["Python", "Django"])

# 적격자 찾기
qualified = manager.find_qualified_employees("BackendDeveloper")
print(json.dumps(qualified, indent=2, ensure_ascii=False))

# 학습 경로 추천
path = manager.recommend_learning_path("박민수", "BackendDeveloper")
print(json.dumps(path, indent=2, ensure_ascii=False))
```

### Extracted Code (python)

```python
# 온톨로지 로드
from owlready2 import *
onto = get_ontology("ai_skills.owl").load()

# 스킬 조회
for skill in onto.Skill.instances():
    print(f"{skill.label[0]}: 난이도 {skill.difficultyLevel[0]}")

# 특정 스킬의 관계 확인
transformer = onto.search_one(iri="*Transformer*")
print(f"선수지식: {[s.label[0] for s in transformer.INDIRECT_isPrerequisiteOf]}")
```
