# Extracted Knowledge from Conv: 66fa0aa4-d4ab-4a8e-8a47-db44dbbbfe22

**Date**: 2026-03-15T02:26:52.105627Z

### Extracted Code (yaml)

```yaml
# escon_context_shell.yaml
persona: |
  당신은 LG PRI의 Engineering Skill Competency Navigator입니다.
  17년 HR 경험과 Production Engineering 도메인 지식을 가진
  전문가의 판단 기준으로 작동합니다.

  핵심 판단 기준:
  - 스킬 레벨은 LV1(인지) → LV2(적용) → LV3(설계) → LV4(혁신)으로 정의됩니다
  - 갭 분석은 현재 수준과 목표 역할의 요구 수준 차이를 정량화합니다
  - 학습 경로 추천은 항상 실행 가능성(6개월 이내 달성 가능)을 기준으로 합니다

domain_glossary:
  "Physical AI Tech Leader": "물리 AI를 설계·운영할 수 있는 LV3 이상 엔지니어"
  "AX 내재화": "AI 도구를 일상 업무 워크플로우에 통합한 상태"
  "Skill Ontology": "직무별 필요 역량을 노드-엣지 구조로 표현한 지식 그래프"

constraints:
  - 스킬 추천은 반드시 Ontology에 존재하는 노드만 사용
  - 레벨 평가는 증거 기반(보유 자격증, 프로젝트 경험)으로만 수행
  - 불확실한 경우 추정이 아닌 추가 질문으로 대응
```

### Extracted Code (text)

```text
Step 1. 현재 역할과 목표 역할을 명확히 파악 (질문 생성)
Step 2. 각 역할의 필요 스킬 노드를 Ontology에서 조회
Step 3. 보유 스킬과 필요 스킬의 교집합/차집합 계산
Step 4. 갭의 우선순위를 비즈니스 임팩트 기준으로 정렬
Step 5. Output Contract 형식으로 결과 반환
```

### Extracted Code (typescript)

```typescript
// domain_membrane.ts
async function injectSkillContext(userQuery: string, db: SupabaseClient) {
  // 1. 쿼리에서 스킬 엔티티 추출 (LLM 호출)
  const entities = await extractSkillEntities(userQuery);
  
  // 2. Ontology에서 관련 노드 조회
  const skillNodes = await db
    .from('skill_nodes')
    .select('*, skill_edges(*)')
    .in('name', entities);
  
  // 3. 컨텍스트 문자열로 변환
  return formatOntologyContext(skillNodes);
  // → "Python(LV1-4): 데이터 처리, ML 파이프라인, API 개발에 필요.
  //    상위 노드: Software Engineering
  //    연결 스킬: SQL(필수), Docker(권장), FastAPI(선택)"
}
```

### Extracted Code (yaml)

```yaml
# escon_output_contract.yaml

gap_analysis_contract:
  required_fields:
    - current_level: integer (1-4)
    - target_level: integer (1-4)
    - gap_score: float (0.0-1.0)
    - priority_skills: array (max 3)
    - timeline_estimate: string ("3개월" | "6개월" | "12개월+")
  
  validation_rules:
    - gap_score > 0.7 → escalate_to_mentoring: true
    - timeline_estimate == "12개월+" → split_into_phases: true
    - priority_skills.length == 0 → status: "no_gap_found"
  
  dod_checklist:
    - [ ] 현재 레벨 근거 명시 (증거 기반)
    - [ ] 목표 역할 Ontology 노드와 매핑 완료
    - [ ] 우선순위 스킬 3개 이하로 집중
    - [ ] 타임라인이 실행 가능한 범위인지 검증

learning_path_contract:
  required_fields:
    - phases: array of phase objects
    - each_phase:
        - duration: string
        - skills: array
        - milestone: string (측정 가능한 성취 기준)
        - resources: array (최소 1개)
  
  dod_checklist:
    - [ ] 각 Phase의 마일스톤이 측정 가능한가
    - [ ] 리소스가 실제 접근 가능한가 (내부/외부 구분)
    - [ ] 전체 기간이 12개월 이내인가
```

### Extracted Code (yaml)

```yaml
gap_analysis_output:
  skill_node:
    id: string
    name: string
    current_level: 0-4  # 0=미보유
    required_level: 1-4
    gap: integer         # required - current
    evidence: string     # 보유 근거 (자격증, 프로젝트명)
  
  priority_ranking:
    basis: "business_impact | learning_efficiency | urgency"
    top_3: array[skill_node]
  
  timeline:
    estimate: "3mo | 6mo | 12mo+"
    confidence: "high | medium | low"
```

### Extracted Code (yaml)

```yaml
# escon_output_contract_v1.yaml
# =============================================
# CONTRACT A: Gap Analysis Output
# =============================================

gap_analysis:
  
  meta:
    contract_version: "1.0"
    generated_at: ISO8601
    target_role: string          # "Senior Production Engineer"
    requestor_level: integer     # 현재 레벨 (0-4)

  skill_gaps:
    type: array
    max_items: 10                # 집중도 유지를 위한 상한
    item_schema:
      skill_id: string           # Ontology 노드 ID (e.g., "PE-ML-001")
      skill_name: string
      cluster: string            # 상위 클러스터 (e.g., "Machine Learning")
      current_level: 0-4         # 0 = 미보유
      required_level: 1-4
      gap: integer               # required - current (1-4)
      evidence:
        type: string | null      # "자격증명 / 프로젝트명 / 자기평가"
        source: "certificate | project | self_assessment | manager_eval"
      prerequisite_met: boolean  # 선행 스킬 보유 여부
      learning_feasibility:
        timeline: "3mo | 6mo | 12mo+"
        confidence: "high | medium | low"

  priority_ranking:
    method: "business_impact × feasibility"
    top_3: array[skill_id]
    rationale: string            # 우선순위 선정 이유 (1-2문장)

  escalation_flags:
    needs_mentoring: boolean     # gap >= 2 시 true
    needs_phased_plan: boolean   # timeline "12mo+" 항목 존재 시 true
    missing_prerequisites: array[skill_id]

  summary:
    total_gap_count: integer
    critical_gaps: integer       # gap >= 2 인 항목 수
    quick_wins: integer          # gap == 1 AND timeline == "3mo" 인 항목 수
    overall_readiness: 0.0-1.0   # 목표 역할 대비 준비도 스코어
```

### Extracted Code (yaml)

```yaml
# =============================================
# CONTRACT B: Learning Path Output
# =============================================

learning_path:

  meta:
    contract_version: "1.0"
    total_duration: "3mo | 6mo | 12mo"
    target_skills: array[skill_id]  # 이 경로가 커버하는 스킬들

  phases:
    type: array
    min_items: 1
    max_items: 4
    item_schema:
      phase_number: integer
      duration: string             # "4주" / "2개월"
      focus_skills: array[skill_id]
      target_level: integer        # 이 Phase 완료 후 도달 레벨
      
      milestone:
        description: string        # 측정 가능한 성취 기준
        verification_method:
          type: "project | assessment | peer_review | certification"
          detail: string           # "사내 프로젝트에 실제 적용" 등
      
      resources:
        type: array
        min_items: 1
        max_items: 3
        item_schema:
          name: string
          type: "internal | external | on_the_job"
          access: string           # URL 또는 접근 방법
          estimated_hours: integer

  dependencies:
    prerequisite_phases: array     # 선행 Phase 없으면 빈 배열
    parallel_possible: boolean     # 병렬 진행 가능 여부
```

### Extracted Code (yaml)

```yaml
# =============================================
# CONTRACT C: Skill Discovery Output
# =============================================

skill_discovery:

  query_context: string            # 사용자 원본 질문 요약
  
  matched_skills:
    type: array
    max_items: 5
    item_schema:
      skill_id: string
      skill_name: string
      cluster: string
      relevance_score: 0.0-1.0
      level_descriptors:           # ← Skyhive에서 빌려온 핵심 개념
        lv1: string                # "개념과 용어를 인지한다"
        lv2: string                # "지도 하에 업무에 적용한다"
        lv3: string                # "독립적으로 설계하고 타인을 가르친다"
        lv4: string                # "조직 표준을 만들고 혁신한다"
      adjacent_skills: array[skill_id]   # 연결 스킬 (그래프 탐색)
      demand_signal: "high | medium | low"  # LG PRI 내부 수요

  ontology_path:
    from: skill_id | null
    to: skill_id
    hops: integer
    path_nodes: array[skill_id]
```

### Extracted Code (yaml)

```yaml
# =============================================
# DEFINITION OF DONE — ESCON v1.0
# =============================================

common_dod:
  # 모든 Contract에 공통 적용
  - id: C-01
    check: "모든 required 필드가 null이 아닌가"
    auto_validatable: true

  - id: C-02
    check: "skill_id가 Ontology DB에 존재하는 노드인가"
    auto_validatable: true
    on_fail: "존재하지 않는 노드는 제거 후 재추천"

  - id: C-03
    check: "레벨 값이 정의된 범위(0-4) 내인가"
    auto_validatable: true

  - id: C-04
    check: "결과물이 Contract JSON Schema를 통과하는가"
    auto_validatable: true

gap_analysis_dod:
  - id: GA-01
    check: "evidence.source가 'self_assessment' 단독인 경우, confidence는 'low'인가"
    rationale: "CSP 휴리스틱 — 자기평가만으로 높은 신뢰도 부여 금지"
    auto_validatable: true

  - id: GA-02
    check: "top_3 우선순위의 rationale이 1문장 이상인가"
    auto_validatable: false   # LLM judge 필요
    judge_prompt: "이 rationale이 비즈니스 임팩트와 실행 가능성을 근거로 하는가?"

  - id: GA-03
    check: "missing_prerequisites가 있을 경우, 해당 스킬이 top_3에 포함되지 않는가"
    rationale: "선행 스킬 없이 우선순위에 올리면 실행 불가"
    auto_validatable: true

  - id: GA-04
    check: "overall_readiness 계산이 gap 데이터와 수학적으로 일관되는가"
    auto_validatable: true

learning_path_dod:
  - id: LP-01
    check: "각 milestone의 verification_method.type이 명시되어 있는가"
    rationale: "측정 불가능한 마일스톤은 마일스톤이 아님"
    auto_validatable: true

  - id: LP-02
    check: "resources 중 internal 타입이 최소 1개 이상인가"
    rationale: "사내 자원 활용 없는 경로는 현실성 낮음"
    auto_validatable: true

  - id: LP-03
    check: "total_duration이 12개월을 초과하지 않는가"
    rationale: "초과 시 needs_phased_plan=true로 Gap Analysis로 에스컬레이션"
    auto_validatable: true

  - id: LP-04
    check: "각 Phase의 focus_skills가 이전 Phase의 target_level을 선행 조건으로 충족하는가"
    auto_validatable: true

skill_discovery_dod:
  - id: SD-01
    check: "level_descriptors 4개 레벨 모두 행동 동사로 시작하는가"
    rationale: "Bloom's Taxonomy 준수 — 명사형 설명은 측정 불가"
    auto_validatable: false
    judge_prompt: "각 descriptor가 행동 동사(인지한다, 적용한다, 설계한다 등)로 시작하는가?"

  - id: SD-02
    check: "adjacent_skills가 Ontology 엣지 기반인가 (추측이 아닌가)"
    auto_validatable: true

# =============================================
# ESCALATION RULES (DoD 실패 시 처리)
# =============================================

escalation:
  C-01_fail: "required 필드 채울 때까지 재생성 (max 3회)"
  C-02_fail: "존재하지 않는 노드 제거 → 유사 노드 추천 요청"
  GA-03_fail: "선행 스킬을 learning_path로 이동"
  LP-03_fail: "Gap Analysis Contract로 에스컬레이션"
  max_retry: 3
  on_max_retry: "partial_result_with_human_review_flag"
```

### Extracted Code (text)

```text
escon/
├── contracts/                          ← 오늘 만드는 것
│   ├── schemas/
│   │   ├── gap_analysis.schema.json    ← Contract A JSON Schema
│   │   ├── learning_path.schema.json   ← Contract B
│   │   └── skill_discovery.schema.json ← Contract C
│   ├── dod/
│   │   ├── common.dod.yaml             ← 공통 DoD
│   │   ├── gap_analysis.dod.yaml       ← Contract A DoD
│   │   ├── learning_path.dod.yaml      ← Contract B DoD
│   │   └── skill_discovery.dod.yaml    ← Contract C DoD
│   └── index.ts                        ← 런타임 검증 엔트리포인트
├── lib/
│   └── validator/
│       ├── ContractValidator.ts        ← DoD 체크 로직
│       └── DoDJudge.ts                 ← auto_validatable: false 처리
└── CLAUDE.md                           ← Claude Code용 컨텍스트
```

### Extracted Code (json)

```json
// contracts/schemas/gap_analysis.schema.json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "escon:gap_analysis:v1",
  "type": "object",
  "required": ["meta", "skill_gaps", "priority_ranking", "escalation_flags", "summary"],
  "properties": {
    "meta": {
      "type": "object",
      "required": ["contract_version", "generated_at", "target_role", "requestor_level"],
      "properties": {
        "contract_version": { "type": "string", "const": "1.0" },
        "generated_at":     { "type": "string", "format": "date-time" },
        "target_role":      { "type": "string", "minLength": 1 },
        "requestor_level":  { "type": "integer", "minimum": 0, "maximum": 4 }
      }
    },
    "skill_gaps": {
      "type": "array",
      "maxItems": 10,
      "items": {
        "type": "object",
        "required": ["skill_id", "skill_name", "cluster",
                     "current_level", "required_level", "gap",
                     "prerequisite_met", "learning_feasibility"],
        "properties": {
          "skill_id":         { "type": "string", "pattern": "^[A-Z]{2}-[A-Z]{2,4}-\\d{3}$" },
          "skill_name":       { "type": "string" },
          "cluster":          { "type": "string" },
          "current_level":    { "type": "integer", "minimum": 0, "maximum": 4 },
          "required_level":   { "type": "integer", "minimum": 1, "maximum": 4 },
          "gap":              { "type": "integer", "minimum": 1, "maximum": 4 },
          "evidence": {
            "type": "object",
            "properties": {
              "type":   { "type": ["string", "null"] },
              "source": { "enum": ["certificate", "project",
                                   "self_assessment", "manager_eval"] }
            }
          },
          "prerequisite_met": { "type": "boolean" },
          "learning_feasibility": {
            "type": "object",
            "required": ["timeline", "confidence"],
            "properties": {
              "timeline":   { "enum": ["3mo", "6mo", "12mo+"] },
              "confidence": { "enum": ["high", "medium", "low"] }
            }
          }
        }
      }
    },
    "priority_ranking": {
      "type": "object",
      "required": ["method", "top_3", "rationale"],
      "properties": {
        "method":    { "type": "string" },
        "top_3":     { "type": "array", "maxItems": 3, "items": { "type": "string" } },
        "rationale": { "type": "string", "minLength": 10 }
      }
    },
    "escalation_flags": {
      "type": "object",
      "required": ["needs_mentoring", "needs_phased_plan", "missing_prerequisites"],
      "properties": {
        "needs_mentoring":        { "type": "boolean" },
        "needs_phased_plan":      { "type": "boolean" },
        "missing_prerequisites":  { "type": "array", "items": { "type": "string" } }
      }
    },
    "summary": {
      "type": "object",
      "required": ["total_gap_count", "critical_gaps", "quick_wins", "overall_readiness"],
      "properties": {
        "total_gap_count":   { "type": "integer", "minimum": 0 },
        "critical_gaps":     { "type": "integer", "minimum": 0 },
        "quick_wins":        { "type": "integer", "minimum": 0 },
        "overall_readiness": { "type": "number",  "minimum": 0, "maximum": 1 }
      }
    }
  }
}
```

### Extracted Code (typescript)

```typescript
// lib/validator/ContractValidator.ts
import Ajv from 'ajv'
import addFormats from 'ajv-formats'
import gapSchema from '../../contracts/schemas/gap_analysis.schema.json'

const ajv = new Ajv({ allErrors: true })
addFormats(ajv)

export type ValidationResult = {
  passed: boolean
  errors: DoDError[]
  warnings: string[]
  requiresJudge: string[]   // auto_validatable: false 항목 ID
}

export type DoDError = {
  id: string
  message: string
  autoFixed?: boolean
}

export class ContractValidator {

  validateGapAnalysis(data: unknown): ValidationResult {
    const errors: DoDError[] = []
    const requiresJudge: string[] = []

    // C-01 ~ C-04: JSON Schema 검증 (자동)
    const validate = ajv.compile(gapSchema)
    if (!validate(data)) {
      validate.errors?.forEach(e => {
        errors.push({ id: 'C-01', message: e.message ?? 'Schema violation' })
      })
      return { passed: false, errors, warnings: [], requiresJudge }
    }

    const d = data as any

    // GA-01: self_assessment 단독 시 confidence는 'low'여야
    d.skill_gaps.forEach((gap: any) => {
      if (gap.evidence?.source === 'self_assessment' &&
          gap.learning_feasibility.confidence !== 'low') {
        errors.push({
          id: 'GA-01',
          message: `${gap.skill_id}: self_assessment 근거인데 confidence가 low가 아닙니다.`
        })
      }
    })

    // GA-03: missing_prerequisites가 top_3에 포함되면 안 됨
    const missingSet = new Set(d.escalation_flags.missing_prerequisites)
    d.priority_ranking.top_3.forEach((skillId: string) => {
      if (missingSet.has(skillId)) {
        errors.push({
          id: 'GA-03',
          message: `${skillId}: 선행 스킬 미충족인데 top_3에 포함되어 있습니다.`
        })
      }
    })

    // GA-04: overall_readiness 수학적 일관성
    const avgGap = d.skill_gaps.reduce((sum: number, g: any) => sum + g.gap, 0)
                   / (d.skill_gaps.length || 1)
    const expectedReadiness = Math.max(0, 1 - (avgGap / 4))
    if (Math.abs(d.summary.overall_readiness - expectedReadiness) > 0.15) {
      errors.push({
        id: 'GA-04',
        message: `overall_readiness(${d.summary.overall_readiness}) 값이 gap 데이터와 불일치합니다.`
      })
    }

    // GA-02: rationale 품질 → LLM judge 필요
    requiresJudge.push('GA-02')

    return {
      passed: errors.length === 0,
      errors,
      warnings: [],
      requiresJudge
    }
  }
}
```

### Extracted Code (typescript)

```typescript
// lib/validator/DoDJudge.ts
import Anthropic from '@anthropic-ai/sdk'

const client = new Anthropic()

export class DoDJudge {

  async judgeRationale(rationale: string): Promise<{
    passed: boolean
    reason: string
  }> {
    const response = await client.messages.create({
      model: 'claude-sonnet-4-6',
      max_tokens: 200,
      messages: [{
        role: 'user',
        content: `다음 우선순위 선정 rationale이 비즈니스 임팩트와 실행 가능성을 
근거로 하는지 판단하라. JSON으로만 응답: {"passed": true/false, "reason": "한 줄 이유"}

Rationale: "${rationale}"`
      }]
    })

    const text = response.content[0].type === 'text' ? response.content[0].text : ''
    return JSON.parse(text)
  }

  async judgeDescriptors(descriptors: Record<string, string>): Promise<{
    passed: boolean
    failed_levels: string[]
  }> {
    const response = await client.messages.create({
      model: 'claude-sonnet-4-6',
      max_tokens: 200,
      messages: [{
        role: 'user',
        content: `다음 스킬 레벨 descriptor들이 행동 동사로 시작하는지 확인하라.
JSON으로만 응답: {"passed": true/false, "failed_levels": ["lv1", ...]}

Descriptors: ${JSON.stringify(descriptors)}`
      }]
    })

    const text = response.content[0].type === 'text' ? response.content[0].text : ''
    return JSON.parse(text)
  }
}
```

### Extracted Code (markdown)

```markdown
<!-- CLAUDE.md 추가 섹션 -->

## Output Contract

ESCON의 모든 AI 응답은 반드시 `contracts/schemas/` 의 JSON Schema를 통과해야 한다.

### 핵심 규칙
- Gap Analysis 응답 → `gap_analysis.schema.json` 검증 필수
- skill_id 형식은 반드시 `PE-XX-000` 패턴 준수 (e.g., `PE-ML-001`)
- `ContractValidator.validateGapAnalysis()` 통과 후에만 사용자에게 반환
- DoD 실패 시 max 3회 재생성, 그래도 실패 시 `partial_result_with_human_review_flag` 설정

### DoD 체크 순서
1. JSON Schema 자동 검증 (C-01 ~ C-04)
2. 비즈니스 규칙 검증 (GA-01 ~ GA-04)
3. LLM Judge 검증 (GA-02: rationale 품질)
4. 모두 통과 시에만 반환

### 금지 사항
- Contract 검증 없이 AI 응답 직접 반환 금지
- skill_id를 임의 문자열로 생성 금지 (Ontology DB 조회 후 사용)
```

### Extracted Code (typescript)

```typescript
// app/api/gap-analysis/route.ts (Next.js App Router)
import { ContractValidator } from '@/lib/validator/ContractValidator'
import { DoDJudge } from '@/lib/validator/DoDJudge'

const validator = new ContractValidator()
const judge = new DoDJudge()

export async function POST(req: Request) {
  const { userId, targetRole } = await req.json()

  let result = null
  let attempts = 0
  const MAX_RETRY = 3

  while (attempts < MAX_RETRY) {
    // 1. LLM으로 Gap Analysis 생성
    result = await generateGapAnalysis(userId, targetRole)

    // 2. Contract 자동 검증
    const validation = validator.validateGapAnalysis(result)

    if (!validation.passed) {
      attempts++
      continue  // 재생성
    }

    // 3. LLM Judge 검증 (rationale 품질)
    const judgeResult = await judge.judgeRationale(
      result.priority_ranking.rationale
    )

    if (!judgeResult.passed) {
      attempts++
      continue
    }

    // 4. 모두 통과 → 반환
    return Response.json({ success: true, data: result })
  }

  // max retry 초과
  return Response.json({
    success: false,
    data: result,
    flag: 'partial_result_with_human_review_flag'
  }, { status: 206 })
}
```

### Extracted Code (text)

```text
사용자 요청
  → Intent Router (어떤 Contract인지 판단)
  → LLM 응답 생성 (Domain Membrane 컨텍스트 포함)
  → ContractValidator.validate() [C-01~C-04, GA-01~GA-04 자동 검증]
  → DoDJudge.judge() [GA-02 LLM judge]
  → 통과 시 반환 / 실패 시 재생성 (max 3회)
  → max retry 초과 시 human_review_flag
```

### Extracted Code (bash)

```bash
# 1. 레포 상태 확인
cd ~/your-path/escon
git status
git branch  # main 또는 develop 브랜치 확인

# 2. 의존성 설치 여부 확인
cat package.json | grep -E "ajv|anthropic"

# 3. 현재 폴더 구조 확인
ls -la
```

### Extracted Code (text)

```text
# ESCON Output Contract 구현 세션

## 이 세션의 목적
ESCON 프로젝트에 Output Contract + DoD 검증 시스템을 구축한다.
구현 대상: Gap Analysis Contract (v1.0) 우선

## 프로젝트 컨텍스트
- Stack: Next.js 14 (App Router), TypeScript, Supabase
- 레포: foolpoet44/escon
- 목표: AI 응답이 반드시 정의된 Contract를 통과한 후에만 사용자에게 반환되는 구조

## 구현 순서 (이 순서를 반드시 지킬 것)
1. contracts/ 디렉토리 구조 생성
2. gap_analysis.schema.json 작성
3. ContractValidator.ts 작성 (ajv 기반)
4. DoDJudge.ts 작성 (LLM self-validation)
5. CLAUDE.md 업데이트 (Contract 인지 주입)
6. API 라우트 연결 테스트

## DoD (이 세션의 완료 기준)
- [ ] contracts/schemas/gap_analysis.schema.json 존재
- [ ] ContractValidator가 유효한 데이터를 통과시키는 유닛 테스트 통과
- [ ] ContractValidator가 GA-01, GA-03, GA-04 위반 데이터를 잡아내는 테스트 통과
- [ ] CLAUDE.md에 Contract 섹션 추가됨
- [ ] git commit 완료

## 제약사항
- 기존 파일 수정 전 반드시 현재 내용 확인 후 진행
- 타입 에러 없이 tsc --noEmit 통과
- 테스트는 Jest 사용 (없으면 설치)
```

### Extracted Code (text)

```text
다음 파일 구조를 생성해줘:

contracts/
  schemas/
    gap_analysis.schema.json   ← 아래 스키마 사용
    learning_path.schema.json  ← 빈 파일 (stub)
    skill_discovery.schema.json ← 빈 파일 (stub)
  dod/
    common.dod.yaml
    gap_analysis.dod.yaml
  index.ts                     ← export 엔트리포인트

gap_analysis.schema.json 내용:
[아래 JSON을 그대로 붙여넣기]
```

### Extracted Code (json)

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "escon:gap_analysis:v1",
  "type": "object",
  "required": ["meta", "skill_gaps", "priority_ranking", "escalation_flags", "summary"],
  "properties": {
    "meta": {
      "type": "object",
      "required": ["contract_version", "generated_at", "target_role", "requestor_level"],
      "properties": {
        "contract_version": { "type": "string", "const": "1.0" },
        "generated_at":     { "type": "string", "format": "date-time" },
        "target_role":      { "type": "string", "minLength": 1 },
        "requestor_level":  { "type": "integer", "minimum": 0, "maximum": 4 }
      }
    },
    "skill_gaps": {
      "type": "array",
      "maxItems": 10,
      "items": {
        "type": "object",
        "required": ["skill_id","skill_name","cluster","current_level",
                     "required_level","gap","prerequisite_met","learning_feasibility"],
        "properties": {
          "skill_id":       { "type": "string", "pattern": "^[A-Z]{2}-[A-Z]{2,4}-\\d{3}$" },
          "skill_name":     { "type": "string" },
          "cluster":        { "type": "string" },
          "current_level":  { "type": "integer", "minimum": 0, "maximum": 4 },
          "required_level": { "type": "integer", "minimum": 1, "maximum": 4 },
          "gap":            { "type": "integer", "minimum": 1, "maximum": 4 },
          "evidence": {
            "type": "object",
            "properties": {
              "type":   { "type": ["string", "null"] },
              "source": { "enum": ["certificate","project","self_assessment","manager_eval"] }
            }
          },
          "prerequisite_met": { "type": "boolean" },
          "learning_feasibility": {
            "type": "object",
            "required": ["timeline", "confidence"],
            "properties": {
              "timeline":   { "enum": ["3mo","6mo","12mo+"] },
              "confidence": { "enum": ["high","medium","low"] }
            }
          }
        }
      }
    },
    "priority_ranking": {
      "type": "object",
      "required": ["method", "top_3", "rationale"],
      "properties": {
        "method":    { "type": "string" },
        "top_3":     { "type": "array", "maxItems": 3, "items": { "type": "string" } },
        "rationale": { "type": "string", "minLength": 10 }
      }
    },
    "escalation_flags": {
      "type": "object",
      "required": ["needs_mentoring","needs_phased_plan","missing_prerequisites"],
      "properties": {
        "needs_mentoring":       { "type": "boolean" },
        "needs_phased_plan":     { "type": "boolean" },
        "missing_prerequisites": { "type": "array", "items": { "type": "string" } }
      }
    },
    "summary": {
      "type": "object",
      "required": ["total_gap_count","critical_gaps","quick_wins","overall_readiness"],
      "properties": {
        "total_gap_count":   { "type": "integer", "minimum": 0 },
        "critical_gaps":     { "type": "integer", "minimum": 0 },
        "quick_wins":        { "type": "integer", "minimum": 0 },
        "overall_readiness": { "type": "number",  "minimum": 0, "maximum": 1 }
      }
    }
  }
}
```

### Extracted Code (text)

```text
lib/validator/ContractValidator.ts를 생성하고,
__tests__/ContractValidator.test.ts도 함께 만들어줘.

테스트 케이스는 4가지:
1. 유효한 데이터 → passed: true
2. GA-01 위반 (self_assessment인데 confidence가 high) → 에러 감지
3. GA-03 위반 (missing_prerequisites에 있는 skill_id가 top_3에 포함) → 에러 감지
4. GA-04 위반 (overall_readiness가 gap 데이터와 0.15 이상 차이) → 에러 감지

테스트 데이터는 skill_id 패턴 PE-ML-001 형식 사용
```

### Extracted Code (text)

```text
CLAUDE.md 파일을 열고 맨 아래에 다음 섹션을 추가해줘:

## Output Contract (필독)

모든 AI 응답은 contracts/schemas/ 의 JSON Schema를 통과해야 한다.

### 핵심 규칙
- Gap Analysis → gap_analysis.schema.json 검증 필수
- skill_id 형식: PE-XX-000 패턴 (예: PE-ML-001)
- ContractValidator.validateGapAnalysis() 통과 후에만 반환
- DoD 실패 시 최대 3회 재생성
- 3회 초과 실패 → partial_result_with_human_review_flag 반환

### DoD 체크 순서
1. JSON Schema 자동 검증 (C-01~C-04)
2. 비즈니스 규칙 검증 (GA-01~GA-04)
3. LLM Judge 검증 (GA-02: rationale 품질)

### 절대 금지
- 검증 없이 AI 응답 직접 반환
- skill_id 임의 생성 (반드시 Ontology DB 조회)
```

### Extracted Code (bash)

```bash
# Claude Code에게 순서대로 요청
npx tsc --noEmit          # 타입 에러 확인
npx jest ContractValidator # 테스트 실행

# 모두 통과하면
git add contracts/ lib/validator/ CLAUDE.md
git commit -m "feat: Add Output Contract v1.0 + ContractValidator (Gap Analysis)"
git push origin main
```

### Extracted Code (text)

```text
ajv를 ESM 방식으로 import하면 에러가 날 수 있어.
import Ajv from 'ajv' 대신 
const Ajv = require('ajv'); const ajv = new Ajv();
방식으로 바꿔줘.
```
