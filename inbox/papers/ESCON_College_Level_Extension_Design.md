---
source: gdrive
original_title: "ESCON_College_Level_Extension_Design.md"
drive_id: 1b2TabyxDJyDFOy-FbzvQr0dy5RPMjOFoHLgTu0Rf8Ew
pulled: 2026-07-18
processed: false
---

# ESCON 데이터 모델 확장 설계서

## 칼리지·레벨 체계 통합 (College & Level Layer Extension)

**문서 목적**: ESCON의 기존 조직 → Enabler → Skill 3계층 온톨로지 위에, 스마트팩토리 칼리지 분류체계와 Lv1~Lv4 양성 레벨 체계를 비파괴적으로 얹기 위한 구현 설계서. **대상**: Claude Code (구현 실행자) **전제 원칙**: 기존 Enabler-Skill 데이터를 변경하지 않는다. 모든 확장은 신규 테이블 + 기존 테이블의 nullable 컬럼 추가로만 이뤄진다. **버전**: v1.0 (Design)

## 0\. TL;DR (Claude Code 작업 요약)

```
[ ] Task 1. 타입 정의      → app/lib/ontology/college-types.ts (신규)
[ ] Task 2. 시드 데이터    → public/data/college-mapping.json (신규)
[ ] Task 3. DB 마이그레이션 → database/migrations/00X_college_level.sql (신규)
[ ] Task 4. 매핑 변환 로직  → app/lib/ontology/college-resolver.ts (신규)
[ ] Task 5. 마이그레이션 스크립트 → scripts/migrate-college.js (신규)
[ ] Task 6. 타입 체크 + 무결성 검증
```

핵심 제약: **기존 파일 중 수정 대상은 단 두 곳** — database 스키마에 ALTER TABLE로 nullable 컬럼 2개 추가, 기존 Enabler 타입에 optional 필드 2개 추가. 그 외는 전부 신규 파일.

## 1\. 배경 및 목표

### 1.1 왜 확장하는가

ESCON은 현재 "어떤 스킬이 있고 어떻게 연결되는가"라는 **지식의 지도(Knowledge Map)**를 다룬다. 하지만 그 스킬들을 "누가, 어떤 순서로, 어떤 깊이까지 배우는가"라는 **사람의 여정(Learning Journey)**은 다루지 않는다.

칼리지·레벨 체계는 바로 이 여정 레이어다. 두 레이어가 결합되면 ESCON은 단순 스킬 시각화 도구를 넘어, 인재 양성 현황을 추적하는 플랫폼으로 진화한다.

### 1.2 무엇을 얻는가

  - **학습 경로 검증**: 기존 DRC 엔진을 재사용해 "이 사람의 이수 경로가 선수 관계 규칙을 위반하지 않는가"를 검증
  - **인재 Pool 커버리지**: 기존 커버리지 분석을 확장해 "Lv3 30명 목표 대비 현재 충원율"을 추적 (CSP 2026 KPI 직결)
  - **경로 시각화**: 기존 네트워크 그래프 위에 페르소나별 학습 경로를 오버레이

본 문서는 위 세 가지의 **공통 토대인 데이터 모델 확장**만 다룬다. 검증·커버리지·시각화는 후속 설계서에서 다룬다.

## 2\. 현재 구조 분석 (As-Is)

### 2.1 기존 3계층 온톨로지

```
조직 (Organization)
  └─ Enabler (직무 역량 단위)
       └─ Skill (ESCO 표준 매핑 스킬)
```

### 2.2 기존 5개 도메인 (로봇 중심)

ESCON은 Robotics Tech for Smart Factory 중심으로 설계되어, 다음 5개 도메인을 가진다.

| \# | 도메인 | 영문 | 성격 |
| :-: | :-: | :-: | :-: |
| 1 | 로봇기술 | Robot Tech Stack | 로봇 하드웨어·기구 |
| 2 | 제어 | Control | 모션 제어·PLC |
| 3 | 센싱/인지 | Sensing/Perception | 센서·비전 |
| 4 | 통합 | Integration | 시스템 통합 |
| 5 | 안전 | Safety | 협업 안전 |

### 2.3 관련 파일 (수정/참조 대상)

```
app/lib/ontology/        # 타입 정의 위치 (확장 대상)
public/data/             # 초기 JSON 데이터 (시드 추가 대상)
database/                # SQL 스키마 (마이그레이션 추가 대상)
scripts/migrate.js       # 기존 마이그레이션 (참조용)
app/api/coverage/        # 후속 Phase 확장 대상 (이번엔 미수정)
app/api/validate/        # 후속 Phase 확장 대상 (이번엔 미수정)
```

**확인 필요**: Claude Code는 구현 전 app/lib/ontology/의 실제 타입 정의 파일명과 public/data/의 실제 JSON 스키마를 먼저 읽고, 아래 설계의 필드명을 실제 코드에 맞게 정합화할 것.

## 3\. 확장 설계 (To-Be)

### 3.1 5계층 구조

```
College (4개 칼리지)              ← 신규
  └─ Level (Lv1~Lv4)             ← 신규
       └─ Enabler (기존)          ← college_id, level_tier 필드만 추가
            └─ Skill (기존)        ← 변경 없음
```

### 3.2 4개 칼리지 정의

| ID | 명칭 | 역할 | 허브 여부 |
| :-: | :-: | :-: | :-: |
| physical-ai | Physical AI & Robotics | 현장 작동 | - |
| data-intelligence | Data Intelligence | 데이터 허브 | **HUB** |
| agentic-ai | Agentic AI Manufacturing | 자율 판단 | - |
| digital-twin | Digital Twin & Simulation | 시뮬레이션 | - |

### 3.3 레벨 체계 정의

| Tier | 명칭 | 성격 |
| :-: | :-: | :-: |
| 1 | AX Starter | 입문·기초 조작 |
| 2 | AX Practitioner | 실무 운용·설계 |
| 3 | AX Specialist | 전문 심화 (Tech Leader Pool) |
| 4 | AX Expert | 융합 혁신 (Cross-College Capstone) |

### 3.4 TypeScript 타입 정의

**파일**: app/lib/ontology/college-types.ts (신규 생성)

```typescript
// ─────────────────────────────────────────────
// College & Level Ontology Extension
// 기존 Enabler-Skill 모델 위에 얹는 양성 체계 레이어
// ─────────────────────────────────────────────

/** 4개 칼리지 식별자 */
export type CollegeId =
  | 'physical-ai'
  | 'data-intelligence'   // HUB
  | 'agentic-ai'
  | 'digital-twin';

/** 레벨 등급 (1~4) */
export type LevelTier = 1 | 2 | 3 | 4;

/** 칼리지 */
export interface College {
  id: CollegeId;
  name: string;           // "Physical AI & Robotics"
  nameKo: string;         // "피지컬 AI 칼리지"
  role: string;           // "현장 작동"
  isHub: boolean;         // data-intelligence = true
  order: number;          // 표시 순서
}

/** 레벨 (칼리지 × Tier 조합) */
export interface Level {
  id: string;             // "physical-ai-lv2"
  collegeId: CollegeId;
  tier: LevelTier;
  name: string;           // "AX Practitioner"
  certification: string;  // "로봇 실무 자격"
  /** 선수 레벨 ID 배열 (HUB 선수 포함) */
  prerequisites: string[]; // ["physical-ai-lv1", "data-intelligence-lv1"]
}

/**
 * 기존 Enabler에 부착되는 칼리지·레벨 메타데이터.
 * 기존 Enabler 타입을 직접 수정하지 않고 별도 매핑으로 관리하거나,
 * 기존 타입에 optional 필드로 추가 (3.6 참조).
 */
export interface EnablerCollegeMeta {
  enablerId: string;      // 기존 Enabler ID 참조
  collegeId: CollegeId;
  levelTier: LevelTier;
  /** 부 칼리지 (도메인이 여러 칼리지에 걸칠 때) */
  secondaryColleges?: CollegeId[];
}

/** 학습 경로 (페르소나별 이수 시퀀스) — 후속 Phase 대비 정의만 */
export interface LearningPath {
  id: string;             // "agentic-ai-expert"
  personaName: string;    // "현장 담당자 → Agentic AI 전문가"
  steps: Array<{
    levelId: string;
    order: number;
    exemptible?: boolean; // 면제 가능 여부
  }>;
  targetTier: LevelTier;
}
```

### 3.5 DB 스키마 (Supabase / PostgreSQL)

**파일**: database/migrations/00X_college_level.sql (신규, 번호는 기존 마이그레이션 최신 번호 +1)

```sql
-- ═══════════════════════════════════════════════
-- College & Level Extension Migration
-- 비파괴적 확장: 신규 테이블 + 기존 테이블 nullable 컬럼
-- ═══════════════════════════════════════════════

-- 1. 칼리지 테이블
CREATE TABLE IF NOT EXISTS colleges (
  id            TEXT PRIMARY KEY,
  name          TEXT NOT NULL,
  name_ko       TEXT,
  role          TEXT,
  is_hub        BOOLEAN NOT NULL DEFAULT FALSE,
  display_order INTEGER NOT NULL DEFAULT 0,
  created_at    TIMESTAMPTZ DEFAULT now()
);

-- 2. 레벨 테이블
CREATE TABLE IF NOT EXISTS levels (
  id            TEXT PRIMARY KEY,
  college_id    TEXT NOT NULL REFERENCES colleges(id) ON DELETE CASCADE,
  tier          INTEGER NOT NULL CHECK (tier BETWEEN 1 AND 4),
  name          TEXT,
  certification TEXT,
  created_at    TIMESTAMPTZ DEFAULT now(),
  UNIQUE (college_id, tier)
);

-- 3. 레벨 선수관계 테이블 (다대다)
CREATE TABLE IF NOT EXISTS level_prerequisites (
  level_id              TEXT NOT NULL REFERENCES levels(id) ON DELETE CASCADE,
  prerequisite_level_id TEXT NOT NULL REFERENCES levels(id) ON DELETE CASCADE,
  PRIMARY KEY (level_id, prerequisite_level_id)
);

-- 4. 기존 enablers 테이블 비파괴적 확장 (nullable)
--    ※ 기존 테이블명이 'enablers'가 아닐 경우 실제 이름으로 교체
ALTER TABLE enablers
  ADD COLUMN IF NOT EXISTS college_id TEXT REFERENCES colleges(id);
ALTER TABLE enablers
  ADD COLUMN IF NOT EXISTS level_tier INTEGER CHECK (level_tier BETWEEN 1 AND 4);

-- 5. 조회 성능을 위한 인덱스
CREATE INDEX IF NOT EXISTS idx_enablers_college ON enablers(college_id);
CREATE INDEX IF NOT EXISTS idx_levels_college  ON levels(college_id);

-- 6. 롤백 스크립트 (별도 파일 00X_college_level_rollback.sql 권장)
-- DROP TABLE IF EXISTS level_prerequisites;
-- DROP TABLE IF EXISTS levels;
-- DROP TABLE IF EXISTS colleges;
-- ALTER TABLE enablers DROP COLUMN IF EXISTS college_id;
-- ALTER TABLE enablers DROP COLUMN IF EXISTS level_tier;
```

### 3.6 기존 Enabler 타입 확장 (선택지)

기존 Enabler 타입에 메타를 붙이는 방법은 두 가지다. Claude Code는 기존 코드 결합도를 보고 택일할 것.

**방식 A — 기존 타입에 optional 필드 추가 (간단, 권장)**

```typescript
// 기존 Enabler 인터페이스에 추가
interface Enabler {
  // ...기존 필드 유지
  collegeId?: CollegeId;     // optional → 기존 데이터 무영향
  levelTier?: LevelTier;     // optional
}
```

**방식 B — 별도 매핑 테이블로 분리 (결합도 0, 복잡)**

```typescript
// EnablerCollegeMeta[] 를 별도 관리, enablerId로 조인
```

기존 Enabler 데이터가 많고 안정적이면 **방식 A**가 마이그레이션 비용이 낮다. 기존 타입을 절대 못 건드리는 상황이면 방식 B.

## 4\. 도메인 → 칼리지 매핑

### 4.1 핵심 진단: ESCON은 로봇 칼리지에 편중되어 있다

ESCON의 기존 5개 도메인은 대부분 **Physical AI & Robotics 칼리지 하나의 세부 영역**에 해당한다. 나머지 3개 칼리지는 데이터가 거의 비어 있다. 따라서 매핑은 "1:1 재배치"가 아니라 "기존 도메인 재배치 + 신규 도메인 확장"의 형태가 된다.

### 4.2 매핑표 (기존 5도메인 → 4칼리지)

| ESCON 도메인 | 주(Primary) 칼리지 | 부(Secondary) 칼리지 | 매핑 근거 |
| :-: | :-: | :-: | :-: |
| 로봇기술 | physical-ai | - | 로봇 하드웨어 = 현장 작동 핵심 |
| 제어 | physical-ai | agentic-ai | PLC·모션 제어 → 작동 + 자율 판단 연계 |
| 센싱/인지 | physical-ai (비전) | data-intelligence (센서 데이터) | 비전 AI는 로봇, 센서 스트림은 데이터 허브 |
| 통합 | agentic-ai | data-intelligence | MES 통합 = 자율화 + 데이터 연계 |
| 안전 | physical-ai (협업 안전) | data-intelligence (OT 보안) | 물리 안전 + 사이버 보안 분리 |

### 4.3 갭 분석: 신규로 채워야 할 영역

| 칼리지 | 기존 커버리지 | 신규 확장 필요 |
| :-: | :-: | :-: |
| physical-ai | **높음** (5도메인 대부분) | 자율 로봇·휴머노이드 Lv3 보강 |
| data-intelligence | **부분** (센싱/통합/안전 일부) | 데이터 파이프라인·제조 분석·인텔리전스 신규 |
| agentic-ai | **낮음** (통합 일부) | AI 에이전트·멀티 에이전트·MES 자율화 대부분 신규 |
| digital-twin | **없음** | 시뮬레이션·가상 시운전·AI 융합 트윈 전체 신규 |

**시사점**: 이번 확장은 기존 데이터를 칼리지로 "태깅"하는 작업(Physical AI 중심) + 3개 칼리지의 신규 Enabler/Skill을 점진적으로 추가하는 작업으로 나뉜다. 후자는 ESCO API 재임포트가 필요할 수 있으며, 별도 데이터 작업 Phase로 분리 권장.

## 5\. 구현 가이드 (Claude Code 작업 지시)

### Task 1. 타입 정의 생성

  - **파일**: app/lib/ontology/college-types.ts
  - **작업**: 3.4의 타입 전체를 생성. 기존 ontology/ 내 타입 파일과 export 구조 정합화.
  - **검증**: tsc --noEmit 통과.

### Task 2. 시드 데이터 생성

  - **파일**: public/data/college-mapping.json
  - **작업**: 4개 칼리지, 16개 레벨(4칼리지 × 4tier), 레벨 선수관계, 도메인 매핑을 JSON으로 작성.

```json
{
  "colleges": [
    { "id": "physical-ai", "name": "Physical AI & Robotics", "nameKo": "피지컬 AI 칼리지", "role": "현장 작동", "isHub": false, "order": 1 },
    { "id": "data-intelligence", "name": "Data Intelligence", "nameKo": "데이터 인텔리전스 칼리지", "role": "데이터 허브", "isHub": true, "order": 2 },
    { "id": "agentic-ai", "name": "Agentic AI Manufacturing", "nameKo": "제조 Agentic AI 칼리지", "role": "자율 판단", "isHub": false, "order": 3 },
    { "id": "digital-twin", "name": "Digital Twin & Simulation", "nameKo": "디지털 트윈 칼리지", "role": "시뮬레이션", "isHub": false, "order": 4 }
  ],
  "levels": [
    { "id": "physical-ai-lv1", "collegeId": "physical-ai", "tier": 1, "name": "AX Starter", "certification": "현장 운전 자격", "prerequisites": [] },
    { "id": "physical-ai-lv2", "collegeId": "physical-ai", "tier": 2, "name": "AX Practitioner", "certification": "로봇 실무 자격", "prerequisites": ["physical-ai-lv1"] },
    { "id": "physical-ai-lv3", "collegeId": "physical-ai", "tier": 3, "name": "AX Specialist", "certification": "로봇 전문가 자격", "prerequisites": ["physical-ai-lv2", "data-intelligence-lv2"] },
    { "id": "data-intelligence-lv1", "collegeId": "data-intelligence", "tier": 1, "name": "AX Starter", "certification": "IIoT 운용 자격", "prerequisites": [] },
    { "id": "data-intelligence-lv2", "collegeId": "data-intelligence", "tier": 2, "name": "AX Practitioner", "certification": "데이터 실무 자격", "prerequisites": ["data-intelligence-lv1"] },
    { "id": "data-intelligence-lv3", "collegeId": "data-intelligence", "tier": 3, "name": "AX Specialist", "certification": "인텔리전스 자격", "prerequisites": ["data-intelligence-lv2"] },
    { "id": "agentic-ai-lv1", "collegeId": "agentic-ai", "tier": 1, "name": "AX Starter", "certification": "AI 활용 자격", "prerequisites": [] },
    { "id": "agentic-ai-lv2", "collegeId": "agentic-ai", "tier": 2, "name": "AX Practitioner", "certification": "에이전트 자격", "prerequisites": ["agentic-ai-lv1", "data-intelligence-lv1"] },
    { "id": "agentic-ai-lv3", "collegeId": "agentic-ai", "tier": 3, "name": "AX Specialist", "certification": "Agentic 전문 자격", "prerequisites": ["agentic-ai-lv2", "data-intelligence-lv2"] },
    { "id": "digital-twin-lv1", "collegeId": "digital-twin", "tier": 1, "name": "AX Starter", "certification": "DT 기초 자격", "prerequisites": [] },
    { "id": "digital-twin-lv2", "collegeId": "digital-twin", "tier": 2, "name": "AX Practitioner", "certification": "시뮬레이션 자격", "prerequisites": ["digital-twin-lv1", "data-intelligence-lv1"] },
    { "id": "digital-twin-lv3", "collegeId": "digital-twin", "tier": 3, "name": "AX Specialist", "certification": "DT 전문가 자격", "prerequisites": ["digital-twin-lv2", "data-intelligence-lv2"] }
  ],
  "domainMapping": {
    "robotics":   { "primary": "physical-ai",       "secondary": [] },
    "control":    { "primary": "physical-ai",       "secondary": ["agentic-ai"] },
    "sensing":    { "primary": "physical-ai",       "secondary": ["data-intelligence"] },
    "integration":{ "primary": "agentic-ai",        "secondary": ["data-intelligence"] },
    "safety":     { "primary": "physical-ai",       "secondary": ["data-intelligence"] }
  }
}
```

※ domainMapping의 키(robotics, control...)는 ESCON 실제 도메인 식별자에 맞게 Claude Code가 정합화할 것. Lv4는 Cross-College Capstone이므로 칼리지별 개별 레벨이 아닌 통합 레벨로 별도 정의 (후속).

### Task 3. DB 마이그레이션 실행

  - **파일**: database/migrations/00X_college_level.sql
  - **작업**: 3.5의 SQL 작성. 기존 마이그레이션 번호 확인 후 다음 번호 부여. 롤백 스크립트 동반 생성.
  - **주의**: ALTER TABLE enablers의 테이블명이 실제와 일치하는지 database/ 스키마 확인 후 실행.

### Task 4. 매핑 리졸버 생성

  - **파일**: app/lib/ontology/college-resolver.ts
  - **작업**: Enabler가 주어졌을 때 소속 칼리지·레벨을 반환하고, 레벨 선수관계를 조회하는 순수 함수 모음.

```typescript
import type { CollegeId, Level, College } from './college-types';

/** Enabler ID → 칼리지 매핑 (domainMapping 기반) */
export function resolveCollege(domainId: string, mapping): {
  primary: CollegeId;
  secondary: CollegeId[];
} { /* ... */ }

/** 특정 레벨의 모든 선수 레벨을 재귀적으로 수집 */
export function resolvePrerequisiteChain(
  levelId: string,
  levels: Level[]
): string[] { /* ... */ }

/** HUB(Data Intelligence) 선수 충족 여부 검사 — DRC 연결 대비 */
export function hasHubPrerequisite(
  levelId: string,
  completedLevels: string[],
  levels: Level[]
): boolean { /* ... */ }
```

### Task 5. 마이그레이션 스크립트

  - **파일**: scripts/migrate-college.js
  - **작업**: public/data/college-mapping.json을 읽어 colleges/levels/level_prerequisites 테이블에 삽입. 기존 scripts/migrate.js 패턴 참조.
  - **멱등성**: ON CONFLICT DO NOTHING 또는 upsert로 재실행 안전성 확보.

### Task 6. 검증

```sql
# 타입 체크
npx tsc --noEmit

# 데이터 무결성 (Supabase SQL Editor 또는 psql)
# 1) 모든 레벨의 선수가 실재하는가
SELECT lp.prerequisite_level_id
FROM level_prerequisites lp
LEFT JOIN levels l ON l.id = lp.prerequisite_level_id
WHERE l.id IS NULL;   -- 결과 0건이어야 정상

# 2) Lv2+ 비HUB 레벨이 HUB 선수를 갖는가 (설계 규칙 검증)
SELECT l.id FROM levels l
WHERE l.tier >= 2
  AND l.college_id != 'data-intelligence'
  AND NOT EXISTS (
    SELECT 1 FROM level_prerequisites lp
    JOIN levels pre ON pre.id = lp.prerequisite_level_id
    WHERE lp.level_id = l.id AND pre.college_id = 'data-intelligence'
  );  -- 결과 0건이어야 설계 규칙 충족
```

## 6\. 마이그레이션 전략

### 6.1 비파괴 원칙

  - 기존 enablers 테이블: 컬럼 **추가만** (nullable). 기존 행은 NULL로 유지되어 영향 없음.
  - 신규 테이블 3개: 완전 독립. 실패 시 DROP으로 깨끗한 롤백.
  - 기존 API (/api/validate, /api/coverage): **이번 단계에서 미수정**. 칼리지 메타가 NULL이어도 기존 로직 정상 동작.

### 6.2 단계별 롤아웃

```
1단계: 스키마 + 타입 + 시드 (Task 1~3, 5)  ← 데이터 구조만, 기능 영향 0
2단계: Physical AI 칼리지 기존 Enabler 태깅  ← UPDATE enablers SET college_id=...
3단계: 3개 신규 칼리지 Enabler/Skill 추가     ← 별도 데이터 작업 Phase (ESCO 재임포트)
4단계: 후속 — 커버리지/DRC/그래프 확장        ← 별도 설계서
```

### 6.3 기존 데이터 태깅 쿼리 예시 (2단계)

```sql
-- 로봇기술 도메인 Enabler를 Physical AI 칼리지로 태깅
UPDATE enablers SET college_id = 'physical-ai', level_tier = 2
WHERE domain_id = 'robotics';  -- 실제 도메인 식별 컬럼/값에 맞게 조정
```

## 7\. 리스크 및 주의사항

| 리스크 | 영향 | 완화 |
| :-: | :-: | :-: |
| 기존 테이블명/필드명 불일치 | 마이그레이션 실패 | 구현 전 database/ 스키마 실독 후 정합화 |
| Vercel 배포 블로커 (기존 이슈) | 빌드 실패 | 이번 변경은 빌드 무관(데이터 레이어), 단 타입 에러 주의 |
| 3개 칼리지 데이터 공백 | 커버리지 왜곡 | 갭을 명시적으로 노출(빈 칼리지 표시), 점진 채움 |
| Next.js deprecation 위험 (기존 이슈) | 후속 빌드 영향 | 이번 작업과 분리, 별도 추적 |
| 선수관계 순환 참조 | 무한 루프 | resolvePrerequisiteChain에 방문 노드 캐시 |

## 8\. 다음 단계 (후속 설계서 예고)

본 문서는 **데이터 모델 토대**만 다뤘다. 이 위에 올라갈 후속 작업:

1.  **인재 Pool 커버리지 API** — /api/coverage 확장, "Lv3 30명 목표 대비 충원율" 반환
2.  **학습 경로 DRC 규칙** — /api/validate 확장, 선수관계·HUB·FDE 진입 요건 검증
3.  **페르소나 경로 그래프 오버레이** — 기존 네트워크 그래프에 경로 하이라이트
4.  **FDE 양성 트랙 모델** — 5단계(선발→학습→동행→자립→인증) 진행 상태 추적

## 부록 A. 파일 변경 요약 (Claude Code 체크리스트)

| 파일 | 작업 | 기존/신규 |
| :-: | :-: | :-: |
| app/lib/ontology/college-types.ts | 타입 정의 | 신규 |
| app/lib/ontology/college-resolver.ts | 매핑 로직 | 신규 |
| public/data/college-mapping.json | 시드 데이터 | 신규 |
| database/migrations/00X_college_level.sql | 스키마 | 신규 |
| database/migrations/00X_college_level_rollback.sql | 롤백 | 신규 |
| scripts/migrate-college.js | 마이그레이션 실행 | 신규 |
| app/lib/ontology/\<기존 타입 파일\> | Enabler에 optional 필드 2개 | **수정(방식 A)** |
| database/\<기존 스키마\> | enablers 컬럼 2개 추가 | **수정** |

수정 대상은 단 2개. 나머지 6개는 신규. 비파괴 원칙 준수.

## 부록 B. 구현 전 필수 확인 사항

Claude Code는 첫 작업 전 다음을 실독하여 설계의 필드명을 실제 코드에 정합화할 것:

1.  app/lib/ontology/ 내 실제 타입 파일명과 Enabler/Skill 인터페이스 구조
2.  public/data/ 내 실제 JSON 스키마 (도메인 식별자, Enabler 필드명)
3.  database/ 내 실제 테이블명 (enablers가 맞는지) 및 도메인 식별 컬럼명
4.  기존 마이그레이션 파일 최신 번호 (00X의 X 결정)
5.  scripts/migrate.js의 DB 커넥션·삽입 패턴 (재사용)

*문서 끝. 본 설계는 ESCON v(현행)의 README 기준 작성되었으며, 실제 코드 구조와 차이가 있을 경우 부록 B의 실독 결과를 우선한다.*
