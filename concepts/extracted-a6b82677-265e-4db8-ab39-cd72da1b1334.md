# Extracted Knowledge from Conv: a6b82677-265e-4db8-ab39-cd72da1b1334

**Date**: 2025-12-09T00:44:54.934246Z

### Extracted Code (text)

```text
/docs
  /decisions          # 아키텍처 결정 기록 (ADR)
  /workflows         # 반복 가능한 워크플로우
  /troubleshooting   # 문제 해결 사례
  /lessons-learned   # 교훈 및 베스트 프랙티스
```

### Extracted Code (bash)

```bash
# .claude/commands/record.md 예시
작업 완료 시:
1. git log를 분석하여 변경사항 요약
2. CHANGELOG.md 업데이트
3. 관련 문서(README, API docs) 업데이트
```

### Extracted Code (markdown)

```markdown
# .claude/commands/snapshot.md

정기적으로(주간/월간):
1. 프로젝트 상태 요약 생성
2. 주요 메트릭 수집 (코드 라인, 커버리지, 이슈)
3. 의존성 변경사항 기록
4. 팀 생산성 인사이트
```

### Extracted Code (bash)

```bash
# 1. 작업 시작
/branch feature-user-auth

# 2. 계획 수립 및 문서화
claude "인증 기능 구현 계획을 세우고 docs/decisions/에 ADR로 저장"

# 3. 구현
claude "계획대로 구현하되, 각 단계마다 테스트 작성"

# 4. 품질 검증
/review  # 커스텀 커맨드로 코드 리뷰

# 5. 문서화
/document  # 자동으로 README, 체인지로그 업데이트

# 6. 커밋 및 PR
claude "변경사항 커밋하고 PR 생성. PR 설명에 작업 요약 포함"

# 7. 지식 저장
/snapshot  # 이번 작업의 교훈 기록
```

### Extracted Code (turtle)

```turtle
@prefix ax: <http://example.org/ax-competency#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix dcterms: <http://purl.org/dc/terms/> .

# 최상위 클래스
ax:Competency a owl:Class ;
    rdfs:label "역량"@ko, "Competency"@en .

# 주요 하위 클래스
ax:TechnicalSkill rdfs:subClassOf ax:Competency ;
    rdfs:label "기술 스킬"@ko .

ax:SoftSkill rdfs:subClassOf ax:Competency ;
    rdfs:label "소프트 스킬"@ko .

ax:Tool rdfs:subClassOf ax:Competency ;
    rdfs:label "도구"@ko .

ax:Methodology rdfs:subClassOf ax:Competency ;
    rdfs:label "방법론"@ko .

ax:Capability rdfs:subClassOf ax:Competency ;
    rdfs:label "역량"@ko .

ax:Domain rdfs:subClassOf ax:Competency ;
    rdfs:label "도메인 지식"@ko .
```

### Extracted Code (turtle)

```turtle
# 데이터 속성
ax:proficiencyLevel a owl:DatatypeProperty ;
    rdfs:domain ax:Competency ;
    rdfs:range xsd:string ;
    skos:note "1-초급, 2-중급, 3-고급, 4-전문가, 5-마스터" .

ax:marketDemand a owl:DatatypeProperty ;
    rdfs:domain ax:Competency ;
    rdfs:range xsd:decimal ;
    rdfs:comment "노동시장 수요 지수 (0-100)" .

ax:emergingTrend a owl:DatatypeProperty ;
    rdfs:domain ax:Competency ;
    rdfs:range xsd:boolean .

ax:halfLife a owl:DatatypeProperty ;
    rdfs:domain ax:Competency ;
    rdfs:range xsd:duration ;
    rdfs:comment "스킬 반감기" .

# 객체 속성
ax:requiresPrerequisite a owl:ObjectProperty ;
    rdfs:domain ax:Competency ;
    rdfs:range ax:Competency .

ax:relatedTo a owl:ObjectProperty, owl:SymmetricProperty ;
    rdfs:domain ax:Competency ;
    rdfs:range ax:Competency .

ax:appliesTo a owl:ObjectProperty ;
    rdfs:domain ax:Competency ;
    rdfs:range ax:JobRole .

ax:supersededBy a owl:ObjectProperty ;
    rdfs:domain ax:Competency ;
    rdfs:range ax:Competency .
```

### Extracted Code (text)

```text
┌─────────────────────────────────────────────────────────┐
│           데이터 수집 레이어 (Data Ingestion)              │
├─────────────────────────────────────────────────────────┤
│ ▪ 구인공고 크롤러    ▪ 이력서 파서                          │
│ ▪ 학습 콘텐츠        ▪ 내부 HR 시스템                      │
│ ▪ 산업 보고서        ▪ 오픈 데이터셋                       │
└─────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────┐
│         NLP/ML 처리 레이어 (Processing)                    │
├─────────────────────────────────────────────────────────┤
│ ▪ Named Entity Recognition (스킬 추출)                    │
│ ▪ 관계 추출 (Relation Extraction)                        │
│ ▪ 의미 유사도 계산                                        │
│ ▪ 트렌드 분석                                            │
└─────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────┐
│         온톨로지 관리 레이어 (Ontology Management)          │
├─────────────────────────────────────────────────────────┤
│ ▪ Apache Jena / RDF4J (Triple Store)                    │
│ ▪ OWL 추론 엔진                                           │
│ ▪ 버전 관리 (시간에 따른 온톨로지 진화)                      │
│ ▪ 품질 검증 (일관성, 중복 제거)                            │
└─────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────┐
│         그래프 데이터베이스 (Graph Database)                 │
├─────────────────────────────────────────────────────────┤
│ ▪ Neo4j / Amazon Neptune / GraphDB                      │
│ ▪ 지식 그래프 저장소                                       │
│ ▪ SPARQL 쿼리 엔진                                        │
└─────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────┐
│         응용 서비스 레이어 (Application Services)           │
├─────────────────────────────────────────────────────────┤
│ ▪ 스킬 갭 분석        ▪ 커리어 패스 추천                    │
│ ▪ 학습 경로 설계      ▪ 인재 매칭                          │
│ ▪ 조직 역량 진단      ▪ 미래 스킬 예측                     │
└─────────────────────────────────────────────────────────┘
```

### Extracted Code (python)

```python
# requirements.txt
rdflib==7.0.0           # RDF 처리
owlready2==0.45         # OWL 온톨로지 조작
spacy==3.7.0            # NLP
transformers==4.35.0    # BERT 기반 임베딩
neo4j==5.15.0           # 그래프 DB
fastapi==0.108.0        # API 서버
pydantic==2.5.0         # 데이터 검증
celery==5.3.0           # 비동기 작업
```

### Extracted Code (python)

```python
from rdflib import Graph, Namespace, Literal, URIRef
from rdflib.namespace import RDF, RDFS, OWL, SKOS

class CompetencyOntology:
    def __init__(self):
        self.g = Graph()
        self.ax = Namespace("http://example.org/ax-competency#")
        self.g.bind("ax", self.ax)
        
    def create_core_classes(self):
        """핵심 클래스 생성"""
        # Competency 최상위 클래스
        self.g.add((self.ax.Competency, RDF.type, OWL.Class))
        self.g.add((self.ax.Competency, RDFS.label, 
                   Literal("역량", lang="ko")))
        
        # 하위 클래스들
        skill_types = [
            ("TechnicalSkill", "기술 스킬"),
            ("SoftSkill", "소프트 스킬"),
            ("Tool", "도구"),
            ("Methodology", "방법론"),
            ("Capability", "역량")
        ]
        
        for class_name, label_ko in skill_types:
            class_uri = self.ax[class_name]
            self.g.add((class_uri, RDF.type, OWL.Class))
            self.g.add((class_uri, RDFS.subClassOf, self.ax.Competency))
            self.g.add((class_uri, RDFS.label, Literal(label_ko, lang="ko")))
            
    def add_competency(self, skill_id, skill_name, skill_type, 
                       proficiency=None, market_demand=None):
        """개별 역량 추가"""
        skill_uri = self.ax[skill_id]
        self.g.add((skill_uri, RDF.type, self.ax[skill_type]))
        self.g.add((skill_uri, RDFS.label, Literal(skill_name, lang="ko")))
        
        if proficiency:
            self.g.add((skill_uri, self.ax.proficiencyLevel, 
                       Literal(proficiency)))
        if market_demand:
            self.g.add((skill_uri, self.ax.marketDemand, 
                       Literal(market_demand)))
```

### Extracted Code (python)

```python
import spacy
from transformers import AutoTokenizer, AutoModel
import torch

class SkillExtractor:
    def __init__(self):
        self.nlp = spacy.load("ko_core_news_lg")
        self.tokenizer = AutoTokenizer.from_pretrained(
            "klue/bert-base"
        )
        self.model = AutoModel.from_pretrained(
            "klue/bert-base"
        )
        
    def extract_skills_from_job_posting(self, text):
        """구인공고에서 스킬 추출"""
        doc = self.nlp(text)
        
        skills = []
        # NER 기반 추출
        for ent in doc.ents:
            if ent.label_ in ["SKILL", "TECH", "TOOL"]:
                skills.append({
                    "text": ent.text,
                    "type": ent.label_,
                    "context": ent.sent.text
                })
        
        # 패턴 기반 추출
        skill_patterns = [
            {"label": "TOOL", "pattern": [
                {"LOWER": {"IN": ["python", "java", "react"]}}
            ]},
            {"label": "METHODOLOGY", "pattern": [
                {"LOWER": "agile"}, {"IS_PUNCT": True, "OP": "?"}, 
                {"LOWER": {"IN": ["scrum", "kanban"]}}
            ]}
        ]
        
        matcher = self.nlp.add_pipe("entity_ruler", before="ner")
        matcher.add_patterns(skill_patterns)
        
        return skills
    
    def compute_skill_similarity(self, skill1, skill2):
        """스킬 간 유사도 계산"""
        inputs1 = self.tokenizer(skill1, return_tensors="pt")
        inputs2 = self.tokenizer(skill2, return_tensors="pt")
        
        with torch.no_grad():
            emb1 = self.model(**inputs1).last_hidden_state.mean(dim=1)
            emb2 = self.model(**inputs2).last_hidden_state.mean(dim=1)
            
        similarity = torch.cosine_similarity(emb1, emb2)
        return similarity.item()
```

### Extracted Code (python)

```python
from celery import Celery
from datetime import datetime, timedelta

app = Celery('ax_competency', broker='redis://localhost:6379')

class DynamicOntologyUpdater:
    def __init__(self, ontology):
        self.ontology = ontology
        self.trend_detector = TrendDetector()
        
    @app.task
    def update_market_demand(self):
        """주기적으로 시장 수요 업데이트"""
        # 구인공고 데이터 수집
        job_postings = self.scrape_job_postings()
        
        # 스킬별 등장 빈도 계산
        skill_counts = self.count_skill_mentions(job_postings)
        
        # 온톨로지 업데이트
        for skill_id, count in skill_counts.items():
            demand_score = self.calculate_demand_score(count)
            self.ontology.update_property(
                skill_id, 
                "marketDemand", 
                demand_score
            )
    
    @app.task
    def detect_emerging_skills(self):
        """신규 등장 스킬 탐지"""
        recent_data = self.get_recent_data(days=30)
        historical_data = self.get_historical_data(months=6)
        
        new_skills = self.trend_detector.find_new_patterns(
            recent_data, 
            historical_data
        )
        
        for skill in new_skills:
            if self.validate_skill(skill):
                self.ontology.add_competency(
                    skill_id=self.generate_id(skill),
                    skill_name=skill['name'],
                    skill_type=skill['type'],
                    emerging_trend=True
                )
    
    def calculate_skill_half_life(self, skill_id):
        """스킬 반감기 계산"""
        history = self.get_skill_demand_history(skill_id)
        
        # 최고점 대비 50% 하락까지의 시간
        peak_demand = max(history.values())
        for date, demand in sorted(history.items()):
            if demand <= peak_demand * 0.5:
                half_life = date - self.get_peak_date(history)
                return half_life
        
        return None  # 아직 반감기에 도달하지 않음
```

### Extracted Code (python)

```python
from rdflib.plugins.sparql import prepareQuery
import networkx as nx

class CompetencyInference:
    def __init__(self, ontology):
        self.ontology = ontology
        self.reasoner = self.setup_reasoner()
        
    def find_skill_gaps(self, current_skills, target_role):
        """스킬 갭 분석"""
        query = prepareQuery("""
            SELECT ?skill ?level
            WHERE {
                ?role ax:requiresSkill ?skill .
                ?skill ax:proficiencyLevel ?level .
                FILTER(?role = ?target)
                FILTER NOT EXISTS {
                    ?person ax:hasSkill ?skill .
                    FILTER(?person = ?current)
                }
            }
        """, initNs={"ax": self.ontology.ax})
        
        gaps = self.ontology.g.query(
            query, 
            initBindings={
                'target': target_role,
                'current': current_skills
            }
        )
        
        return list(gaps)
    
    def recommend_learning_path(self, current_skills, target_skill):
        """학습 경로 추천"""
        # 그래프 변환
        G = nx.DiGraph()
        
        # 선행 조건 관계를 그래프로 변환
        for s, p, o in self.ontology.g.triples(
            (None, self.ontology.ax.requiresPrerequisite, None)
        ):
            G.add_edge(str(s), str(o))
        
        # 현재 스킬에서 목표 스킬까지의 최단 경로
        paths = []
        for current in current_skills:
            try:
                path = nx.shortest_path(
                    G, 
                    source=str(current), 
                    target=str(target_skill)
                )
                paths.append(path)
            except nx.NetworkXNoPath:
                continue
        
        # 최적 경로 선택 (총 학습 시간 고려)
        return self.select_optimal_path(paths)
    
    def predict_future_skills(self, domain, horizon_months=12):
        """미래 스킬 예측"""
        query = """
            SELECT ?skill ?trend ?growth_rate
            WHERE {
                ?skill rdf:type ax:TechnicalSkill .
                ?skill ax:domain ?domain_val .
                ?skill ax:emergingTrend true .
                ?skill ax:growthRate ?growth_rate .
                FILTER(?domain_val = ?target_domain)
            }
            ORDER BY DESC(?growth_rate)
        """
        
        results = self.ontology.g.query(
            query,
            initBindings={'target_domain': domain}
        )
        
        # 트렌드 외삽
        predictions = []
        for row in results:
            projected_demand = self.extrapolate_trend(
                row.skill, 
                horizon_months
            )
            predictions.append({
                'skill': row.skill,
                'projected_demand': projected_demand,
                'confidence': self.calculate_confidence(row.skill)
            })
        
        return predictions
```

### Extracted Code (python)

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="AX Competency API")

class SkillProfile(BaseModel):
    person_id: str
    skills: List[dict]
    proficiency_levels: dict

class JobRequirement(BaseModel):
    job_id: str
    required_skills: List[dict]
    nice_to_have: Optional[List[dict]]

@app.post("/api/match/candidates")
async def match_candidates(job: JobRequirement):
    """후보자 매칭"""
    ontology = CompetencyOntology()
    inference = CompetencyInference(ontology)
    
    # 모든 후보자 검색
    candidates = get_all_candidates()
    
    matches = []
    for candidate in candidates:
        # 매칭 스코어 계산
        score = inference.calculate_match_score(
            candidate.skills,
            job.required_skills
        )
        
        # 스킬 갭 분석
        gaps = inference.find_skill_gaps(
            candidate.skills,
            job.job_id
        )
        
        if score > 0.7:  # 임계값
            matches.append({
                "candidate_id": candidate.person_id,
                "match_score": score,
                "skill_gaps": gaps,
                "learning_path": inference.recommend_learning_path(
                    candidate.skills,
                    gaps
                )
            })
    
    return sorted(matches, key=lambda x: x['match_score'], reverse=True)

@app.get("/api/skills/trending")
async def get_trending_skills(domain: str, limit: int = 10):
    """트렌딩 스킬 조회"""
    ontology = CompetencyOntology()
    
    query = """
        SELECT ?skill ?label ?demand ?growth
        WHERE {
            ?skill rdf:type ax:TechnicalSkill .
            ?skill rdfs:label ?label .
            ?skill ax:domain ?domain_val .
            ?skill ax:marketDemand ?demand .
            ?skill ax:growthRate ?growth .
            FILTER(?domain_val = ?target)
        }
        ORDER BY DESC(?growth)
        LIMIT ?limit
    """
    
    results = ontology.g.query(
        query,
        initBindings={'target': domain, 'limit': limit}
    )
    
    return [
        {
            "skill": str(row.skill),
            "name": str(row.label),
            "demand": float(row.demand),
            "growth_rate": float(row.growth)
        }
        for row in results
    ]
```

### Extracted Code (python)

```python
import plotly.graph_objects as go
import networkx as nx

class CompetencyVisualizer:
    def __init__(self, ontology):
        self.ontology = ontology
        
    def create_skill_network(self, center_skill, depth=2):
        """스킬 관계 네트워크 생성"""
        G = nx.Graph()
        
        # 중심 스킬과 관련된 스킬들 찾기
        related = self.find_related_skills(center_skill, depth)
        
        for skill, relation_type, target in related:
            G.add_edge(
                skill, 
                target, 
                relation=relation_type
            )
        
        # Plotly 시각화
        pos = nx.spring_layout(G)
        
        edge_trace = go.Scatter(
            x=[], y=[],
            line=dict(width=0.5, color='#888'),
            hoverinfo='none',
            mode='lines'
        )
        
        for edge in G.edges():
            x0, y0 = pos[edge[0]]
            x1, y1 = pos[edge[1]]
            edge_trace['x'] += (x0, x1, None)
            edge_trace['y'] += (y0, y1, None)
        
        node_trace = go.Scatter(
            x=[], y=[],
            mode='markers+text',
            hoverinfo='text',
            marker=dict(
                showscale=True,
                colorscale='YlGnBu',
                size=10,
                colorbar=dict(
                    thickness=15,
                    title='연결 수',
                    xanchor='left'
                )
            )
        )
        
        for node in G.nodes():
            x, y = pos[node]
            node_trace['x'] += (x,)
            node_trace['y'] += (y,)
        
        fig = go.Figure(
            data=[edge_trace, node_trace],
            layout=go.Layout(
                title=f'{center_skill} 스킬 네트워크',
                showlegend=False,
                hovermode='closest'
            )
        )
        
        return fig
    
    def create_skill_evolution_timeline(self, skill_id):
        """스킬 진화 타임라인"""
        history = self.get_skill_demand_history(skill_id)
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=list(history.keys()),
            y=list(history.values()),
            mode='lines+markers',
            name='수요 지수'
        ))
        
        # 반감기 표시
        half_life = self.calculate_skill_half_life(skill_id)
        if half_life:
            fig.add_vline(
                x=half_life,
                line_dash="dash",
                line_color="red",
                annotation_text="반감기"
            )
        
        fig.update_layout(
            title=f'{skill_id} 수요 변화 추이',
            xaxis_title='날짜',
            yaxis_title='수요 지수'
        )
        
        return fig
```

### Extracted Code (python)

```python
class OntologyValidator:
    def __init__(self, ontology):
        self.ontology = ontology
        
    def check_consistency(self):
        """일관성 검증"""
        inconsistencies = []
        
        # 순환 참조 확인
        G = self.build_dependency_graph()
        cycles = list(nx.simple_cycles(G))
        if cycles:
            inconsistencies.append({
                "type": "circular_dependency",
                "cycles": cycles
            })
        
        # 고아 노드 확인
        orphans = [
            node for node in self.ontology.g.subjects()
            if not list(self.ontology.g.predicate_objects(node))
        ]
        if orphans:
            inconsistencies.append({
                "type": "orphan_nodes",
                "nodes": orphans
            })
        
        return inconsistencies
    
    def detect_duplicates(self, threshold=0.9):
        """중복 스킬 탐지"""
        skills = list(self.ontology.get_all_skills())
        duplicates = []
        
        for i, skill1 in enumerate(skills):
            for skill2 in skills[i+1:]:
                similarity = self.compute_similarity(skill1, skill2)
                if similarity > threshold:
                    duplicates.append({
                        "skill1": skill1,
                        "skill2": skill2,
                        "similarity": similarity
                    })
        
        return duplicates
    
    def validate_data_quality(self):
        """데이터 품질 검증"""
        quality_report = {
            "completeness": self.check_completeness(),
            "accuracy": self.check_accuracy(),
            "timeliness": self.check_timeliness()
        }
        
        return quality_report
```

### Extracted Code (python)

```python
from datetime import datetime
import hashlib

class OntologyVersionControl:
    def __init__(self, ontology):
        self.ontology = ontology
        self.versions = []
        
    def create_snapshot(self, description=""):
        """온톨로지 스냅샷 생성"""
        snapshot = {
            "version": self.generate_version_id(),
            "timestamp": datetime.now(),
            "description": description,
            "ontology_hash": self.compute_hash(),
            "triple_count": len(self.ontology.g),
            "changes": self.compute_changes()
        }
        
        # 스냅샷 저장
        self.save_snapshot(snapshot)
        self.versions.append(snapshot)
        
        return snapshot['version']
    
    def rollback(self, version_id):
        """이전 버전으로 롤백"""
        snapshot = self.load_snapshot(version_id)
        self.ontology.g = snapshot['graph']
        
    def compare_versions(self, version1, version2):
        """버전 간 차이 비교"""
        g1 = self.load_snapshot(version1)['graph']
        g2 = self.load_snapshot(version2)['graph']
        
        added = g2 - g1
        removed = g1 - g2
        
        return {
            "added_triples": list(added),
            "removed_triples": list(removed),
            "modified_count": len(added) + len(removed)
        }
```

### Extracted Code (python)

```python
class OntologyMetrics:
    def calculate_coverage(self):
        """커버리지: 실제 직무의 몇 %를 커버하는가"""
        total_jobs = self.get_total_job_count()
        covered_jobs = self.get_covered_job_count()
        return covered_jobs / total_jobs
    
    def calculate_freshness(self):
        """최신성: 얼마나 최신 데이터인가"""
        avg_update_lag = self.get_average_update_lag()
        return 1 / (1 + avg_update_lag.days)
    
    def calculate_accuracy(self):
        """정확도: 스킬 추출/매칭의 정확도"""
        test_cases = self.get_test_cases()
        correct = sum(1 for tc in test_cases if self.is_correct(tc))
        return correct / len(test_cases)
```

### Extracted Code (python)

```python
from ax_ontology_manager import AITransformationOntology

# 1. 온톨로지 로드
ontology = AITransformationOntology("ax_ai_transformation_ontology.ttl")

# 2. 스킬 갭 분석
gap = ontology.analyze_skill_gap(
    current_skills=["Python", "SQL", "MachineLearningFundamentals"],
    target_role="MLEngineer"
)
print(f"완성도: {gap['completion_rate']:.1f}%")

# 3. 인재 매칭
matches = ontology.find_candidates_for_role("MLEngineer", candidates)

# 4. 시각화
from ax_visualizer import CompetencyVisualizer
visualizer = CompetencyVisualizer(ontology)
fig = visualizer.create_comprehensive_dashboard()
fig.show()
```
