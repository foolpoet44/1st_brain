---
status: Inbox
type: Note
source: gdrive
original_title: "BP_Signal_Intelligence_개발명세서.md"
drive_id: 1DK-2gL6YeH6Vdfo5jPUob4bj90T76z9YBzX7qxCAj8o
pulled: 2026-07-18
processed: true
---

# BP Signal Intellig[[Understand-Anything/understand-anything-plugin/skills/understand/locales/en.md|en]]ce — 운영 시스템 개발 명세서

상태 기계(State Machine) × People Context Graph × [[CLAUDE.md|CLAUDE]] Code 멀티에이전트 EX Intelligence 아키텍처의 Relation Verification 층을 살아있는 파이프라인으로 전환하는 개발 하네스

## 0\. 문서 개요

### 0.1 목적

BP(Business Partner) 아카이브에 축적된 신호 데이터는 현재 **모든 레코드가** **접수** **상태에 정체**되어 있다. 신호를 받기만 하고 검증·분류·조치·종결로 흘려보내지 못하는 구조이며, 그 결과 BP Report는 설계 의도였던 *active signal verifier*가 아니라 여전히 *passive reporter*에 머물러 있다.

이 문서는 정적인 아카이브 테이블을 **신호가 반드시 흘러가는 파이프라인**으로 전환하고, 각 단계를 Claude Code 서브에이전트가 지키게 하는 개발 명세를 정의한다.

### 0.2 핵심 설계 원칙

1.  **status = work queue** — 신호의 현재 상태가 곧 '어느 에이전트를 깨울 것인가'를 결정한다. 별도 오케스트레이터 없이 상태 자체가 라우터다.
2.  **사람이 지키는 칸은 단 하나(조치)** — 자동화의 한계가 아니라 윤리. 사람에 대한 신호를 다루는 시스템에서 마지막 개입 판단까지 기계에 넘기면 EX Intelligence는 감시 도구로 변질된다.
3.  **모든 질적 판단은 감사 가능해야 한다** — 에이전트가 신뢰도를 매기고 클러스터를 코딩한 근거를 JSONL로 남긴다. 신뢰도를 매기는 시스템이 자기 판단의 근거를 남기지 않으면 모순이다.
4.  **do it once, automate it forever** — 일회성 정제가 아니라 입력 단계의 마찰 설계로 데이터 품질을 구조적으로 보장한다.

### 0.3 현재 데이터 진단 (49건 기준)

| 항목 | 상태 | 문제 |
| :-: | :-: | :-: |
| status | 49/49 전부 접수 | Actionable Intelligence 층 미작동 |
| opinions (BP 해석) | 17건 공란 + 다수 무의미값(".", "test222") | verifier 역할 미작동 |
| tags | 7/49만 채움, 통제어휘 없음 | EX 클러스터 태깅 미작동 |
| author | 동일 BP가 4종 표기로 분산 | 마스터 정규화 부재 |
| target | 자유텍스트 27종 | **개인 레벨 그래프 연결 불가** |
| 신뢰도 등급(A–D) | 스키마에 부재 | 설계–데이터 갭 |
| 심리 프레임워크 메타 | 스키마에 부재 | 설계–데이터 갭 |
| 테스트 더미 | 운영 데이터에 2건 혼입 | 환경 분리 부재 |

### 0.4 범위

  - **포함**: Supabase 스키마 마이그레이션, 상태 기계 정의, 5+1 서브에이전트 명세, 오케스트레이션, observability, 49건 정제 절차.
  - **제외**: Pulse Check·리더십 평가 등 Signal Generation 상류 소스(별도 문서), 프론트엔드 대시보드 UI(후속).

## 1\. 시스템 아키텍처

```
[Signal Generation]            (상류 — 본 문서 범위 밖)
        │
        ▼
┌─────────────────────────────────────────────────────────┐
│  1층 · 신호 생애주기 상태 기계                              │
│  접수 → 검증 → 분류 → 조치 → 종결  (status = work queue)   │
│   Ingest  Verifier Triage  사람   Graph·Digest            │
└─────────────────────────────────────────────────────────┘
        │ (종결 시 영구 노드화)
        ▼
┌─────────────────────────────────────────────────────────┐
│  2층 · People Context Graph                               │
│  persons ── signals ── orgs ── ex_clusters               │
│  동일 인물 누적 신호 → 약신호 증폭 감지(Ansoff)            │
└─────────────────────────────────────────────────────────┘
        ▲
        │ (각 상태 칸을 지키는 문지기)
┌─────────────────────────────────────────────────────────┐
│  3층 · Claude Code 멀티에이전트 런타임                     │
│  tmux 24/7 · status 폴링/webhook 트리거                   │
│  PostToolUse hook → JSONL → swim-lane 대시보드            │
└─────────────────────────────────────────────────────────┘
```

세 층은 독립 모듈이 아니라 하나의 회로다. 상태 기계가 **무엇을 할 차례인지**를 정의하고, 에이전트 런타임이 **그것을 실행**하며, People Context Graph가 **결과를 시간축에 누적**한다.

## 2\. 데이터 모델 & Supabase 마이그레이션

기존 bp_reports(OKA 아키텍처의 pgvector + FastAPI 토대 위) 를 확장하고, 마스터 테이블과 그래프 간선을 추가한다.

### 2.1 status enum 및 신뢰도/티어 타입

```sql
-- 신호 생애주기 상태
create type signal_status as enum (
  'received',   -- 접수: raw 기록 입력됨
  'verifying',  -- 검증: 신뢰도 평가 대기
  'rejected',   -- 반려: 신뢰도 D, 접수로 환류
  'triaged',    -- 분류: 클러스터·티어 부여됨
  'acting',     -- 조치: 사람 개입 할당됨
  'closed'      -- 종결: 그래프 귀속 완료
);

-- BP 신뢰도 등급 (Relation Verification 산출)
create type reliability_grade as enum ('A','B','C','D');

-- Actionable Intelligence 티어
create type action_tier as enum ('watch','alert','critical');
```

### 2.2 bp_reports 확장

```sql
alter table bp_reports
  add column status            signal_status     not null default 'received',
  add column reliability       reliability_grade,            -- verifier가 부여
  add column tier              action_tier,                  -- triage가 부여
  add column person_id         uuid references persons(id),  -- target 정규화 결과
  add column org_id            uuid references orgs(id),
  add column verified_by       text,                         -- 검증 BP
  add column verified_at       timestamptz,
  add column embedding         vector(1536);                 -- pgvector 의미 연결

-- 환경 분리: 운영 데이터에서 테스트 격리
alter table bp_reports
  add column is_test           boolean not null default false;
```

### 2.3 마스터 테이블 (정규화)

```sql
-- 인물: target 자유텍스트를 person_id로 정규화 → 개인 레벨 그래프의 노드
create table persons (
  id          uuid primary key default gen_random_uuid(),
  name        text not null,
  title       text,                 -- 직책(책임/선임/팀장 등)
  org_id      uuid references orgs(id),
  aliases     text[],               -- 표기 변형 흡수 ('JB 김진우 선임' 등)
  created_at  timestamptz default now()
);

-- 조직
create table orgs (
  id          uuid primary key default gen_random_uuid(),
  name        text not null,        -- 직속연구소/장비기술센터/생산혁신센터 등
  parent_id   uuid references orgs(id),
  created_at  timestamptz default now()
);

-- EX 8-클러스터 (통제어휘) — 3-레이어 구조
create table ex_clusters (
  id          uuid primary key default gen_random_uuid(),
  code        text unique not null, -- 'energy_survival_01' 등
  layer       text not null,        -- 'energy_survival' | 'direction_meaning' | 'relationship_trust'
  label       text not null,
  framework   text[]                -- ['JD-R','SDT'] 심리 프레임워크 메타
);
```

### 2.4 People Context Graph 간선

```sql
-- 인접 리스트: 신호 간/신호-노드 간 관계
create table signal_edges (
  id          uuid primary key default gen_random_uuid(),
  src_type    text not null,        -- 'signal' | 'person' | 'org' | 'cluster'
  src_id      uuid not null,
  dst_type    text not null,
  dst_id      uuid not null,
  relation    text not null,        -- 'about' | 'belongs_to' | 'tagged' | 'related_to' | 'causal'
  weight      real default 1.0,
  created_at  timestamptz default now()
);

create index on signal_edges (src_type, src_id);
create index on signal_edges (dst_type, dst_id);
```

### 2.5 상태 전이 로그 (time-to-action 측정)

```sql
create table status_transitions (
  id          uuid primary key default gen_random_uuid(),
  signal_id   uuid not null references bp_reports(id),
  from_status signal_status,
  to_status   signal_status not null,
  actor       text not null,        -- 'ingest_agent' | 'verifier_agent' | 'human:<id>' 등
  reason      text,                 -- 반려 사유 등
  at          timestamptz default now()
);

create index on status_transitions (signal_id, at);
```

**운영 KPI의 원천**: status_transitions에서 received → acting 경과 시간이 곧 **time-to-action**. 현재는 모두 received에 멈춰 측정조차 불가능하다. 이 테이블이 생기는 순간 시스템의 반응 속도가 관측 가능해진다.

## 3\. 신호 생애주기 상태 기계

### 3.1 상태 정의 및 담당

| 상태 | 의미 | 담당 | 산출 |
| :-: | :-: | :-: | :-: |
| received | raw 기록 입력 | **Ingest 에이전트** | 정규화·더미 제거 |
| verifying | 신뢰도 평가 | **Verifier 에이전트** | A–D 등급, verified_by |
| rejected | 신뢰도 D 환류 | Verifier → 접수 | 반려 사유 |
| triaged | 클러스터·티어 부여 | **Triage 에이전트** | EX 클러스터, watch/alert/critical |
| acting | 개입 할당·추적 | **사람(HR/리더십)** | 액션 항목 |
| closed | 그래프 귀속 | **Graph 에이전트** | 노드·간선, 증폭 스캔 |

### 3.2 전이 규칙 (가드 조건)

```
received  ──[Ingest 완료]──────────────▶ verifying
verifying ──[reliability ∈ {A,B,C}]────▶ triaged
verifying ──[reliability = D]──────────▶ rejected ──▶ received  (반려 루프)
triaged   ──[tier 부여 완료]───────────▶ acting
acting    ──[사람이 액션 종료 표기]─────▶ closed

# 가드(반드시 만족해야 전이):
- verifying → triaged : opinions 비공란 AND reliability 부여됨
- triaged  → acting   : ex_cluster 1개 이상 태깅 AND tier 부여됨
- critical 티어        : acting 단계를 건너뛸 수 없음 (fast-track이되 사람 개입 필수)
```

반려 루프(verifying → rejected → received)가 BP를 passive reporter에서 active verifier로 강제 전환시키는 핵심 장치다. 해석·근거 없는 단발 보고는 통과하지 못한다.

## 4\. Claude Code 멀티에이전트 명세

각 서브에이전트는 **하나의 상태 칸을 지키는 문지기**다. ~/.claude/[[AGENTS.md|AGENTS]]/ 하위에 정의하거나 프로젝트 CLAUDE.md의 프로토콜로 등록한다.

### 4.1 Ingest 에이전트

  - **트리거**: status = received
  - **책임**: author/target을 persons·orgs 마스터에 매칭(없으면 신규 노드 생성 후보 큐로), is_test 판별, 스키마 정규화.
  - **도구**: Supabase MCP(read/write), 인물 alias 매칭 로직.
  - **출력 전이**: received → verifying
  - **판단 골자**:

입력 레코드의 author·target 문자열에서 인물을 식별하라. persons.aliases와 대조해 동일 인물이면 person_id를 연결하고, 신규로 보이면 후보로 표시하되 자동 생성하지 마라(사람 승인 큐). 'test'·'테스트'·무의미 본문은 is_test=true로 격리하라.

### 4.2 Verifier 에이전트 (Relation Verification 핵심)

  - **트리거**: status = verifying
  - **책임**: opinions·source_desc 충실도와 교차검증 가능성을 근거로 A–D 신뢰도 부여.
  - **출력 전이**: A/B/C → triaged, D → rejected
  - **판단 골자**:

신호의 신뢰도를 평가하라. A=교차검증된 1차 관찰, B=단일 BP의 근거 있는 해석, C=정황·전언, D=해석·근거 없는 단발 보고. opinions가 공란이거나 무의미하면 D를 부여하고 반려 사유를 명시해 접수로 환류하라. **신뢰도 근거를 반드시 status_transitions.reason에 기록하라.**

### 4.3 Triage 에이전트

  - **트리거**: status = triaged_pending(verifying 통과 직후)
  - **책임**: summary·opinions 본문을 EX 8-클러스터(3-레이어)로 코딩하고 심리 프레임워크(SDT/LMX/POS/JD-R) 메타를 부착, watch/alert/critical 티어 결정.
  - **출력 전이**: triaged → acting
  - **판단 골자**:

신호 본문을 Energy&Survival / Direction&Meaning / Relationship&Trust 3-레이어 중 해당 클러스터로 코딩하라. '이탈'이라는 표면 현상이 생존(처우·과중)인지 의미(업무 침식)인지 관계(리더십·신뢰)인지 분리하라. JD-R·SDT 관점 메타를 부착하고, 신뢰도×조직 누적도를 반영해 티어를 정하라.

### 4.4 (사람) 조치 — 자동화하지 않는 칸

  - **트리거**: status = acting
  - **책임**: HR/리더십이 실제 개입을 할당·추적. 에이전트는 알림·맥락 브리핑만 제공하고 **판단은 하지 않는다.**
  - **출력 전이**: acting → closed (사람이 종료 표기)

### 4.5 Graph 에이전트

  - **트리거**: status = closed
  - **책임**: 종결 신호를 People Context Graph에 노드·간선으로 박고, 동일 person_id·org_id의 누적 신호를 스캔해 **약신호 증폭** 경보 생성.
  - **도구**: Supabase MCP, signal_edges write, pgvector 유사 신호 탐색.
  - **판단 골자**:

종결 신호를 그래프에 연결하라(about/belongs_to/tagged). 동일 인물에 critical·alert가 시간축으로 N건(기본 N=3) 누적되면 증폭 경보를 생성하라 — Ansoff Weak Signal: 개별로는 일회성 면담이나 누적되면 강신호다. pgvector로 의미 유사 신호를 related_to 간선으로 연결하라.

### 4.6 Digest 에이전트

  - **트리거**: cron(주기적, 예: 일 1회) 또는 critical 증폭 경보 발생 시
  - **책임**: 그래프 상태를 경영진 언어로 요약, hermes-telegram 파이프라인으로 전달.
  - **출력**: 조직×레이어 히트맵 요약, 신규 증폭 경보, time-to-action 추이.

## 5\. 오케스트레이션

### 5.1 status = work queue

중앙 오케스트레이터를 두지 않는다. 각 에이전트는 자신이 담당하는 status를 폴링하거나 webhook으로 트리거된다.

```
# tmux 24/7 Code Factory 레인 (개념)
lane:ingest    → watch status=received    → run ingest_agent
lane:verifier  → watch status=verifying   → run verifier_agent
lane:triage    → watch status=triaged_pending → run triage_agent
lane:graph     → watch status=closed      → run graph_agent
lane:digest    → cron daily               → run digest_agent
```

### 5.2 트리거 메커니즘 (택1 또는 병행)

  - **Webhook**: Supabase Database Webhook → status 변경 시 Claude Code 실행 엔드포인트 호출(즉시성).
  - **Polling**: tmux 세션에서 N초 주기 status 스캔(단순·견고). 초기에는 polling 권장, 안정화 후 webhook 전환.

## 6\. Observability

24/7 팩토리의 불투명성을 해소하고, 무엇보다 **에이전트의 질적 판단을 사후 감사 가능하게** 만든다.

### 6.1 PostToolUse Hook → JSONL

```json
// 각 에이전트 행동 1건 = JSONL 1줄
{
  "ts": "2026-06-15T09:12:03Z",
  "agent": "verifier_agent",
  "signal_id": "030b174d-…",
  "action": "assign_reliability",
  "input_excerpt": "구매 부서 인력 공백…실무 90%",
  "decision": "B",
  "rationale": "단일 BP의 근거 있는 1차 관찰, 교차검증 미실시",
  "from_status": "verifying",
  "to_status": "triaged"
}
```

### 6.2 Swim-lane 대시보드

  - 가로축: 시간. 세로 레인: 에이전트(ingest/verifier/triage/graph/digest).
  - 각 신호가 레인을 가로질러 흐르는 모습 → 어디서 정체되는지, 어떤 판단이 내려졌는지 한눈에.
  - JSONL 스트림을 소스로 하는 정적/준실시간 뷰.

## 7\. 데이터 마이그레이션 절차 (기존 49건)

```
Phase A · 격리      : 'test'/'테스트'/무의미 본문 → is_test=true
Phase B · 인물 정규화: author/target → persons 마스터 구축 + alias 흡수
                      (동일 BP 4종 표기 통합, target 27종 → person_id)
Phase C · 조직 정규화: org 5종 → orgs 마스터
Phase D · 사후 코딩  : Triage 에이전트로 49건 summary/opinions를
                      EX 8-클러스터 + 심리 프레임워크로 일괄 코딩
Phase E · 신뢰도 부여: Verifier 에이전트로 opinions 충실도 기반 A–D 부여
                      (공란 17건은 D 또는 보류)
Phase F · 그래프 적재: Graph 에이전트로 노드·간선 생성 + 증폭 스캔
                      (장비기술센터 critical 5건 등 핫스팟 자동 식별)
```

사후 코딩은 LLM 보조로 49건 기준 1일 내 완료 가능. 다만 **사람 승인 게이트**를 Phase B(신규 인물 생성)와 Phase E(신뢰도 확정)에 둔다.

## 8\. 운영 KPI

| 지표 | 정의 | 출처 |
| :-: | :-: | :-: |
| **time-to-action** | received → acting 평균 경과 | status_transitions |
| 반려율 | verifying → rejected 비율 | status_transitions |
| 신뢰도 분포 | A/B/C/D 구성 | bp_reports.reliability |
| 증폭 경보 수 | 인물 누적 강신호 건 | graph 스캔 |
| 클러스터 히트맵 | 조직×레이어 신호 밀도 | signal_edges 집계 |
| 종결율 | closed / 전체 | bp_reports.status |

## 9\. 구현 로드맵

```
Phase 0 (기반)   : 스키마 마이그레이션(§2) + status enum + transitions 로그
Phase 1 (정제)   : 49건 마이그레이션(§7 A–C) — 인물·조직 정규화
Phase 2 (에이전트): Ingest/Verifier/Triage 빌드 + 상태 전이 가드(§3,§4)
Phase 3 (그래프) : Graph/Digest 에이전트 + 증폭 감지 + hermes-telegram 연동
Phase 4 (관측)   : PostToolUse hook + JSONL + swim-lane 대시보드
```

EX Intelligence 전체 로드맵(Q2 foundation → Q3 connection → Q4 intelligence activation)과 정렬: Phase 0–1 = Q2, Phase 2–3 = Q3, Phase 4 = Q4.

## 10\. 디렉토리 구조 (제안)

```
bp-signal-intelligence/
├── CLAUDE.md                  # 에이전트 프로토콜·가드·통제어휘 정의
├── agents/
│   ├── ingest_agent.md
│   ├── verifier_agent.md
│   ├── triage_agent.md
│   ├── graph_agent.md
│   └── digest_agent.md
├── migrations/
│   ├── 001_status_enum.sql
│   ├── 002_extend_bp_reports.sql
│   ├── 003_master_tables.sql
│   └── 004_signal_edges.sql
├── seeds/
│   └── ex_clusters.sql        # 8-클러스터 통제어휘 시드
├── scripts/
│   └── migrate_49.py          # 기존 49건 정제(§7)
├── hooks/
│   └── post_tool_use.sh       # JSONL 로깅
└── observability/
    └── swimlane.html          # 대시보드
```

### 부록 · 설계 결정 요약

  - **③ 운영 설계 채택**: status를 work queue로 보는 관점이 운영 설계와 에이전트 설계를 하나로 통합.
  - **사람 칸 1개 유지**: 조치 단계는 의도적으로 자동화하지 않음(감시 아닌 돌봄).
  - **People Context Graph의 관문**: target → person_id 정규화가 개인 레벨 층 구조적 갭을 메우는 단일 결정점.
  - **감사 가능성**: 모든 신뢰도·클러스터 판단의 근거를 JSONL·transitions.reason에 기록.
