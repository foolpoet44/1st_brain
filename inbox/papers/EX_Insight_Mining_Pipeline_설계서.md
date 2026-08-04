---
status: Inbox
type: Note
source: gdrive
original_title: "EX_Insight_Mining_Pipeline_설계서.md"
drive_id: 1hFYpt9O7M0CjNw-ULfRV-1CrFNWnyaoZeg9F_w5tmIg
pulled: 2026-07-18
processed: true
---

# EX Insight Mining Pipeline — 설계서

귀납적 의미 클러스터링 × 연역적 프레임워크 평정의 교차 분석 BP Signal Intellig[[Understand-Anything/understand-anything-plugin/skills/understand/locales/en.md|en]]ce의 **Triage 모듈**로 끼워지는 텍스트 인사이트 발굴 엔진

## 0\. 이 문서의 자리

### 0.1 목적

BP 신호의 자연어(summary·opinions)에서 risk_level이라는 단일 축으로는 보이지 않는 의미·구조·인과를 길어 올린다. 단어를 세는 빈도 분석이 아니라, 직원의 언어 속에 응결된 경험을 다시 살아있는 의미로 풀어내는 것이 목표다.

### 0.2 상위 시스템과의 관계

이 파이프라인은 독립 산출물이 아니라, BP*Signal_Intelligence*개발명세서.md의 **Triage 에이전트(§4.3)가 호출하는 분석 엔진**이다. 상태 기계에서 신호가 verifying → triaged로 넘어갈 때, Triage 에이전트는 이 파이프라인을 돌려 클러스터·티어·프레임워크 메타·인과 간선을 산출한다.

```
[Verifier 통과] → Triage 에이전트
                     └─ EX Insight Mining Pipeline 호출
                          ① 의미 임베딩 & 귀납 클러스터링
                          ② 연역 프레임워크 평정
                          ③ 교차 매핑 (귀납 × 연역)
                          ④ 인과 사슬 추출
                          ⑤ 약신호 신규성 탐지
                          ⑥ positive deviance 대조
                     └─ ex_cluster · tier · framework_meta · causal_edges 기록
              → [triaged → acting]
```

### 0.3 설계 철학 (3개의 인식론적 기둥)

1.  **현상학적 귀납 (Husserl의 epoché)** — 분석자의 이론적 선입견을 괄호 치고, 의미 구조가 데이터 자신의 중력으로 떠오르게 한다. 임베딩 공간의 코사인 거리가 epoché의 전산화다.
2.  **귀납–연역 교차 검증** — 데이터가 발견한 클러스터(귀납)와 조직심리 이론이 제공한 격자(연역)를 겹쳐, 발견이 해석을 만나고 해석이 발견을 검증하게 한다.
3.  **약신호 우선 (Ansoff)** — 빈도 분석은 과거를 본다(자주 나온 것=중요). 약신호는 정반대다. 드물지만 의미적으로 새로운 신호가 미래의 강신호 후보다.

### 0.4 표본 크기에 대한 정직한 전제

현재 49건은 통계적 토픽 모델링(LDA, 대규모 공출현 네트워크)에는 작다. 따라서 **현 단계 주력은 LLM 질적 코딩 + 임베딩 이웃 탐색**이고, 데이터가 수백 건으로 쌓이면 BERTopic·시계열 담론 진화 분석이 합류한다(§7). 지금은 파이프라인을 PoC로 깔아두고 데이터가 차오를수록 기법이 깊어지는 구조다.

## 1\. 아키텍처 개요

```
원천 텍스트 (summary + opinions + details)
        │
        ▼
┌─[전처리]──────────────────────────────────────────┐
│ 정제 · 화자 분리 · 길이 정규화 · is_test 제외        │
└───────────────────────────────────────────────────┘
        │
        ├─────────────────┬──────────────────┐
        ▼                 ▼                  ▼
  ① 귀납 클러스터링   ② 연역 평정        ④ 인과 추출
  embedding→UMAP      LLM 차원 평정       LLM 관계 추출
  →HDBSCAN            SDT/LMX/POS/JD-R    → causal edges
        │                 │                  │
        └────────┬────────┘                  │
                 ▼                            │
        ③ 교차 매핑 (귀납 클러스터 × 연역 격자)│
                 │                            │
        ┌────────┴───────────┬───────────────┘
        ▼                    ▼
  ⑤ 약신호 신규성 탐지   ⑥ positive deviance 대조
  novelty/outlier        건강군 vs 위험군 언어 대조
        │                    │
        └──────────┬─────────┘
                   ▼
        산출물: ex_cluster · framework_meta · tier
                · causal_edges · novelty_flag · pd_marker
```

여섯 단계는 따로 노는 기법이 아니라 하나의 하강이다 — 표면의 빈도에서 의미로, 의미에서 구조로, 구조에서 시간과 대조로.

## 2\. 단계별 상세 설계

### 2.1 전처리

- **화자 분리**: opinions는 BP의 해석층, summary는 현장 진술. 둘을 구분해 임베딩(해석과 진술을 섞으면 의미가 흐려진다).
- **격리**: is_test=true 제외, 무의미값(".", "test222") 제거.
- **단위**: 신호 1건 = 분석 단위 1개. 단, 한 신호에 복수 주제가 섞이면 문장군 단위로 분할(splitting) 후 재귀속.

### 2.2 ① 귀납적 의미 클러스터링

이론을 씌우지 않고 의미 구조가 스스로 떠오르게 하는 단계.

```python
# 의사코드 — 임베딩 → 차원축소 → 밀도 기반 클러스터링
emb = embed(texts)                      # pgvector / OpenAI·E5 등 (1536d)
reduced = umap.fit_transform(emb,       # 고차원 → 5~10차원
            n_neighbors=10, min_dist=0.0, metric='cosine')
labels = hdbscan.fit_predict(reduced,   # 밀도 기반: 클러스터 수 미지정
            min_cluster_size=3, metric='euclidean')
# 노이즈(-1)는 약신호 후보로 ⑤에 전달
```

- **왜 HDBSCAN인가**: k-means처럼 클러스터 수를 미리 정하지 않는다. '몇 개로 나눌까'라는 분석자의 선입견 자체를 제거한다(epoché). 어디에도 안 속한 점(노이즈)을 강제로 묶지 않고 약신호 후보로 남긴다.
- **소표본 대응**: 49건에서는 클러스터가 불안정할 수 있으므로 min_cluster_size를 낮게(3) 두고, 결과를 LLM 라벨링으로 해석 보강. 클러스터 경계는 확정이 아니라 가설로 다룬다.
- **산출**: 잠정 클러스터 + 각 클러스터의 대표 신호(centroid 최근접).

### 2.3 ② 연역적 프레임워크 평정

같은 신호를 이번엔 조직심리 이론의 차원에서 정량 평정. 귀납이 발견한 구조에 이름을 붙일 좌표계를 제공한다.

```json
// LLM 평정 출력 스키마 (신호 1건당)
{
  "signal_id": "030b174d-…",
  "sdt": { "autonomy": 0.8, "competence": 0.6, "relatedness": 0.3 }, // 자기결정이론
  "ldx": { "leader_member_exchange": 0.4 }, // 리더-구성원 교환
  "pos": { "perceived_org_support": 0.2 }, // 지각된 조직지원
  "jdr": { "demand": 0.9, "resource": 0.2, "burnout_risk": 0.85 }, // 직무요구-자원
  "evidence": "실무 비중 90% 급증 · 충원 난항",
  "rationale": "자율성보다 직무요구 과부하가 지배적"
}
```

- **평정 원칙**: 각 차원은 0~1 연속값. LLM은 반드시 evidence(본문 근거)와 rationale을 함께 출력 → 감사 가능성(상위 명세서의 JSONL 로깅과 정합).
- **신뢰도 가중**: Verifier가 부여한 A–D 등급을 평정 신뢰구간에 반영(D 신호의 평정은 약하게).

### 2.4 ③ 교차 매핑 — 이 파이프라인의 핵심

각 신호가 **두 좌표**를 갖게 된다: 귀납 클러스터 좌표(①)와 연역 프레임워크 격자 좌표(②). 이 둘을 겹친다.

- **방법**: 클러스터별로 소속 신호들의 프레임워크 점수를 집계(평균·분산) → 각 귀납 클러스터를 프레임워크 프로파일로 해석.
- **발견의 예시 형태**:

귀납적으로 떠오른 클러스터 C2는 JD-R의 demand(평균 0.88)와 SDT의 competence 박탈(0.71)이 합쳐진 자리 → '소진형 이탈'로 명명. 표면 단어는 '퇴사'지만 의미 구조는 과부하다.

- **EX 8-클러스터 확정**: 이 교차 매핑이 안정화되면, 데이터에서 귀납된 클러스터에 3-레이어 구조로 통제어휘를 부여한다.

|        레이어        |   성격    | 귀납 클러스터가 안착하는 자리(예시 후보) |
| :------------------: | :-------: | :--------------------------------------: |
|  Energy & Survival   | 생존·자원 |    과부하/소진, 처우·보상, 충원 공백     |
| Direction & Meaning  | 방향·의미 |   본연 업무 침식, 성장 정체, 역할 모호   |
| Relationship & Trust | 관계·신뢰 |   리더십 신뢰, 팀 결속, 조직지원 체감    |

8개 클러스터의 최종 라벨은 분석자가 선험적으로 정하지 않는다. 데이터가 귀납적으로 떠올린 것을 위 3-레이어에 귀속시키며 확정한다 — 이것이 top-down 보편 온톨로지가 아닌 bottom-up 현상학적 귀납.

### 2.5 ④ 인과 사슬 추출

개별 신호를 넘어 메커니즘의 지도를 그린다. CRITICAL 건의 언어는 이미 인과의 결을 품는다("인력 공백 → 실무 90% → 소진 → 이탈").

```json
// LLM 인과 추출 → People Context Graph causal 간선
{
  "chain": ["인력 공백", "실무 비중 급증", "소진", "이탈"],
  "edges": [
    {
      "src": "인력 공백",
      "dst": "실무 비중 급증",
      "relation": "causal",
      "weight": 0.9
    },
    {
      "src": "실무 비중 급증",
      "dst": "소진",
      "relation": "causal",
      "weight": 0.8
    },
    { "src": "소진", "dst": "이탈", "relation": "causal", "weight": 0.85 }
  ]
}
```

- **상위 스키마 연결**: 추출된 간선은 signal_edges(relation='causal')에 적재 → People Context Graph가 '무엇이 일어났나'에서 '무엇이 무엇을 일으키나'로 도약.
- **반복 구조 탐지**: 여러 조직에서 동일 인과 구조가 반복되면(충원난항→과중→이탈 고리의 조직 간 공명) 개별 사건이 아니라 **시스템 병리**로 격상. 개입 지점이 달라진다(개인 면담이 아니라 충원 정책).

### 2.6 ⑤ 약신호 신규성 탐지

Ansoff Weak Signal의 진짜 전산화. 드물지만 의미적으로 새로운 신호를 조기에 건진다.

```python
# 기존 신호 분포에서 동떨어진 점 = 신규성 후보
novelty = []
for s in new_signals:
    d = min(cosine_dist(emb[s], emb[h]) for h in history)  # 최근접 거리
    if d > NOVELTY_THRESHOLD:        # 기존 어느 신호와도 멀다
        novelty.append(s)
# ① 단계의 HDBSCAN 노이즈(-1)도 신규성 후보로 합류
```

- **시간축 결합**: 동일 person_id·org_id에 의미적으로 새로운 신호가 반복되기 시작하는 순간 = 임계 돌파 직전의 떨림 → 증폭 경보(상위 명세서 Graph 에이전트와 연동).
- **빈도의 함정 회피**: 한두 건뿐이라 빈도로는 묻힐 신호를 의미 거리로 구제한다.

### 2.7 ⑥ Positive Deviance 대조 분석

위험만 보면 시스템은 경보기로 전락한다. 건강한 조직의 언어를 분석해 처방의 마커를 찾는다.

- **대조군 설정**: positive deviance 신호(예: "면담 조직 중 가장 좋은 조직문화") vs 위험군 신호.
- **방법**: 두 군의 임베딩 중심 차이 벡터, 변별 어휘·구문·정서 추출(LLM 대조 요약). 무엇이 부족한가가 아니라 **무엇이 작동하는가**를 언어에서 읽는다.
- **산출**: pd_marker — 건강 조직 언어의 특징(학회 공동참여·역할 명확성·결속 어휘 등) → 다른 조직 이식 가설.
- **효과**: EX Intelligence를 감시에서 돌봄으로, 경보에서 이식으로 끌어올림.

## 3\. 산출물 (Triage 에이전트가 기록하는 것)

|      산출      |            적재 위치            |             비고              |
| :------------: | :-----------------------------: | :---------------------------: |
|   ex_cluster   |    bp_reports / ex_clusters     | 귀납 클러스터 + 3-레이어 귀속 |
| framework_meta |        bp_reports(jsonb)        |     SDT/LMX/POS/JD-R 평정     |
|      tier      |         bp_reports.tier         |     watch/alert/critical      |
|  causal_edges  | signal_edges(relation='causal') |           인과 사슬           |
|  novelty_flag  |     bp_reports(bool) + 경보     |          약신호 후보          |
|   pd_marker    |      별도 인사이트 테이블       |           처방 가설           |

## 4\. 데이터 스키마 보강 (상위 명세서에 추가)

```sql
alter table bp_reports
  add column framework_meta  jsonb,      -- ② 평정 결과
  add column novelty_score   real,       -- ⑤ 신규성 거리
  add column cluster_label   text;       -- ① 귀납 클러스터 잠정 라벨

-- positive deviance / 처방 가설 저장
create table ex_insights (
  id          uuid primary key default gen_random_uuid(),
  kind        text not null,             -- 'pd_marker' | 'causal_pattern' | 'novelty'
  scope       text,                      -- org_id 또는 'cross-org'
  payload     jsonb not null,
  confidence  real,
  created_at  timestamptz default now()
);
```

## 5\. Triage 에이전트 통합 (상위 명세서 §4.3 확장)

```
# [[AGENTS.md|AGENTS]]/triage_agent.md (발췌)
- 트리거: status = triaged_pending
- 호출: EX Insight Mining Pipeline (단계 ①~⑥)
- 판단 골자:
  1) ② 프레임워크 평정으로 신호의 지배 차원 식별
  2) ③ 교차 매핑으로 귀납 클러스터에 귀속 + 3-레이어 태깅
  3) 신뢰도(A–D) × 조직 누적도 반영해 tier 결정
  4) ④ 인과 간선·⑤ 신규성·⑥ PD 마커를 ex_insights/signal_edges에 적재
  5) 모든 판단 근거(evidence·rationale)를 JSONL에 기록 (감사 가능성)
- 출력 전이: triaged → acting
```

## 6\. 기술 스택

|          단계           |              라이브러리 / 도구              |
| :---------------------: | :-----------------------------------------: | ----------------------------------- |
|         임베딩          |   pgvector + (E5 / OpenAI text-embedding)   |
|        차원축소         |              UMAP (umap-learn)              |
|       클러스터링        |              HDBSCAN (hdbscan)              |
| 프레임워크 평정·인과·PD |           LLM (구조화 JSON 출력)            |
|          적재           | Supabase (jsonb, signal_edges, ex_insights) |
|          실행           |                 [[CLAUDE.md                 | CLAUDE]] Code 서브에이전트 (Triage) |

## 7\. 표본 규모별 진화 로드맵

```
~50건 (현재)  : LLM 질적 코딩 + 임베딩 이웃/노이즈 탐색 주력.
              클러스터는 '확정' 아닌 '가설'. 사람 검토 게이트 필수.
~수백 건      : BERTopic(임베딩 기반 토픽 모델링) 합류,
              교차 매핑 안정화 → EX 8-클러스터 통제어휘 확정.
~수천 건      : 시계열 담론 진화 분석(토픽 드리프트),
              조직 간 인과 구조 비교, novelty 자동 임계 학습.
```

현재의 조직 이니셔티브를 미래 SaaS의 proof-of-concept로 다루는 방식 그대로 — 파이프라인을 먼저 깔고, 데이터가 차오를수록 기법이 함께 깊어진다.

## 8\. 구현 단계

```
Step 1 : 전처리 + ① 임베딩·UMAP·HDBSCAN (49건 잠정 클러스터)
Step 2 : ② LLM 프레임워크 평정 (구조화 출력 + evidence/rationale)
Step 3 : ③ 교차 매핑 → 3-레이어 귀속 가설 + 사람 검토
Step 4 : ④ 인과 추출 → signal_edges(causal) 적재
Step 5 : ⑤ 신규성 탐지 + ⑥ PD 대조 → ex_insights 적재
Step 6 : Triage 에이전트에 ①~⑥ 모듈 결선 + JSONL 로깅
```

### 부록 · 한 줄 요약

이 파이프라인의 진짜 목적은 단어를 세는 것이 아니라, 직원의 언어 속에 굳어 있는 경험을 다시 살아있는 의미로 풀어내는 것이다. 귀납이 의미를 발견하고, 연역이 그것에 이름을 주고, 인과가 구조를 그리고, 신규성이 미래를 당기고, 대조가 처방을 비춘다 — 심리학이 코드가 되는 자리.
