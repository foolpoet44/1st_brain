---
type: Signal
date: 2026-06-03
source: LinkedIn (Soojeong Bae/Kiwoong Yeom)
tags: [RAG, LogicRAG, GraphRAG, Resolver, Efficiency, AI-Strategy]
status: 🟢 INGESTED
---

# [SIGNAL] LogicRAG: 지도를 미리 그리지 않는 '레이지(Lazy)' 추론의 승리

## 1. 핵심 통찰 (The Core Insight)

기존의 GraphRAG가 수만 권의 문서를 미리 읽어 거대한 지식 지도를 그려놓는 '부지런한 사서'의 방식이라면, **LogicRAG**는 질문이 들어오는 순간 필요한 논리 구조(DAG)를 설계하고 경로를 개척하는 '기민한 탐정'의 방식을 제안한다.

### 🧠 심리학적 유추: 고정 관념 vs 맥락적 사고

- **고정 관념(Pre-rendered Graph)**: 모든 상황에 대비해 미리 판단을 내려두는 것. 변화에 취약하고 유지비가 높다.
- **맥락적 사고(LogicRAG)**: 편견 없이 대기하다가, 질문(자극)이 주어지면 그 순간 가장 적합한 논리적 연결을 수행하는 것.

## 2. 주요 기술적 원자 (Technical Atoms)

1. **즉석 논리 설계 (Real-time DAG Sketching)**: 질문을 쪼개어 "무엇을 알아야 다음 단계를 풀 수 있는가"에 대한 순서도를 실시간으로 생성.
2. **위상 정렬(Topological Sort)**: 꼬여 있는 하위 질문들을 단방향 순서로 정렬하여 검색 효능감을 극대화.
3. **롤링 메모리(Rolling Memory)**: 검색된 풍부한 원본 데이터에서 핵심만 추출(Distillation)하고 나머지는 버림으로써 오직 '지능의 정수'만 컨텍스트 창에 유지.

## 3. csp-brain에의 적용점 (Actionable Strategy)

- **리졸버(Resolver)의 진화**: 현재의 `resolver_engine.py`가 단순히 파일을 찾는 수준을 넘어, 파일 간의 논리적 우선순위를 결정하여 **'순차적 사고(Chain of Thought for Files)'**를 수행하도록 고도화할 근거가 됨.
- **가성비의 미학**: gpt-4o-mini 수준의 모델로도 구조적 설계만 뒷받침된다면 64.7%의 압도적 정확도(benchmarked)를 달성할 수 있음을 확인. 이는 FDE(Field Deployment Engineer)가 가져야 할 '실용적 지능 활용'의 모범 사례임.

## 4. 리졸버의 한마디 (Navigator's Note)

"지도를 그리느라 시간을 보내지 마십시오. 이미 모델은 지도를 그릴 수 있는 지능을 충분히 가지고 있습니다. 우리는 그 지능이 움직일 '궤도(Logic)'만 실시간으로 깔아주면 됩니다."
