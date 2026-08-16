# .claude/CLAUDE.md — ex-analyzer 에이전트 협업 허브

type: Reflection
> **위치:** `/Users/dkmac/Desktop/@26/dev/.claude/CLAUDE.md`
> 
> **역할:** ex-analyzer 스킬이 실제 프로젝트 컨텍스트에서 실행될 때 따르는 워크플로우와 품질 기준
> 
> **인간 (CSP) 은 이 파일을 직접 수정하지 않습니다. 에이전트가 유지보수합니다.**

---

## 1. ex-analyzer 의 사명과 위치

**핵심 철학:** "조직은 데이터가 아니라 경험의 총합이다"

ex-analyzer 는 csp-brain Vault 의 HR 도메인에서 **구성원 경험 (EX) 데이터의 Single Source of Truth**를 확보하는 분석가입니다.

### 1.1 Vault 내 위치

```
csp-brain Vault
├── wiki/signals/          # ex-analyzer 출력 → Signal 노드로 INGEST
├── wiki/concepts/         # EX 관련 개념 (직무몰입, 회복탄력성, 심리적안전감)
├── outputs/briefings/     # HR Tech 브리핑 → ex-analyzer 입력
├── inbox/                 # 원본 EX 데이터 (설문, 피드백, 면담)
└── _ops/
    ├── change-log.md      # ex-analyzer 실행 이력 기록
    └── ingest-log.md      # INGEST 판정 이력 (NEW/MERGE/DUPLICATE)
```

### 1.2 관련 스킬

- **`ex-analyzer`** (hr-analytics 카테고리) — 본 스킬 (스키마, 파이프라인, 휴먼 게이트)
- **`knowledge-management`** (productivity 카테고리) — Evening Reflect, INGEST Protocol, Metabolism Reporting
- **`writing-plans`** (software-development 카테고리) — bite-sized tasks, TDD, frequent commits

---

## 2. 실행 워크플로우 (5-Stage Pipeline)

### Stage 1: 수집 (Ingest)

**명령:**
```bash
cd /Users/dkmac/Desktop/@26/dev
python3 .claude/pipelines/01_ingest.py --source survey_platform --date-range 2026-08-01:2026-08-15
```

**입력:**
- `inbox/surveys_202608*.csv` — 설문 플랫폼 원본
- `inbox/feedbacks_202608*.xlsx` — HR 팀 수기 관리 피드백
- `inbox/interviews/` — 면담 기록 (텍스트 파일)

**출력:**
- `data/raw/surveys_20260815.json`
- `data/raw/feedbacks_20260815.csv`
- `data/raw/interviews_20260815/`

**품질 기준:**
- ✅ 원본 데이터는 절대 수정하지 않음 (read-only)
- ✅ 수집 이력은 `_ops/ingest-log.md` 에 기록
- ✅ 실패 시 재시도 3 회 후 경고 (graceful degradation)

**Human Gate:** 원본 데이터의 익명화 처리 (employee_id 해시화) 는 인간이 검증

---

### Stage 2: 정규화 (Normalize)

**명령:**
```bash
python3 .claude/pipelines/02_normalize.py --input data/raw/ --output data/normalized/
```

**주요 작업:**
- 필드 매핑 (예: `Q1` → `job_engagement`)
- 타입 변환 (문자열 → 숫자, 날짜 포맷 통일)
- 익명화 처리 (employee_id 해시화)
- 결측치 마킹 (`null` 또는 `-999`)

**출력:**
- `data/normalized/ex_surveys.jsonl` (JSON Lines 형식)
- `data/normalized/ex_feedbacks.jsonl`
- `data/normalized/ex_interviews.jsonl`

**품질 기준:**
- ✅ 모든 레코드가 스키마 검증 통과 (`jsonschema` 라이브러리 사용)
- ✅ 매핑 규칙은 `references/ex-schemas.md` 에 명시
- ✅ 변환 이력은 로그로 기록 (원본 필드 → 변환 필드)

**Human Gate:** 필드 매핑 규칙 (예: Q1=job_engagement) 은 HR 전문가가 검증

---

### Stage 3: 검증 (Validate)

**명령:**
```bash
python3 .claude/pipelines/03_validate.py --input data/normalized/ --report reports/validation_20260815.md
```

**검항 항목:**
1. **필수 필드 검사:** `required` 필드가 모두 채워졌는가?
2. **타입 검증:** 숫자 필드에 문자열이 들어있지 않은가?
3. **범위 검증:** 리커트 척도가 1-5 점 범위인가?
4. **이상치 탐지:** tenure_years 가 50 년 초과인 레코드는 없는가?
5. **중복 검사:** response_id 가 중복되지 않았는가?

**출력:**
- `reports/validation_20260815.md` (검토 보고서)
- `data/normalized/valid_surveys.jsonl` (검증 통과 데이터)
- `data/normalized/invalid_surveys.jsonl` (검증 실패 데이터, 수동 검토용)

**품질 기준:**
- ✅ 검증 실패율 5% 미만 (초과 시 원본 데이터 소스 검토)
- ✅ 이상치는 자동으로 제거하지 않음 (HR 팀 검토 후 결정)
- ✅ 검증 규칙은 `references/ex-schemas.md` 에 명시

**Human Gate #3:** 검증 실패 레코드 중 5% 이상 시 원본 소스 검토 (AI 자동 제거 금지)

---

### Stage 4: 인사이트 (Enrich)

**명령:**
```bash
python3 .claude/pipelines/04_enrich.py --input data/normalized/valid_*.jsonl --output data/output/
```

**분석 항목:**
1. **집계 통계:** 부서별, 근속별 평균 점수
2. **상관 분석:** job_engagement ↔ resilience 상관관계
3. **트렌드:** 전월 대비 변화 (MoM), 전년 동기 대비 (YoY)
4. **세그먼트 분석:** high_performer vs struggling 그룹 비교
5. **텍스트 마이닝:** open_text, 피드백 키워드 추출 (TF-IDF, 토픽 모델링)

**출력:**
- `data/output/aggregates.json`
- `data/output/correlations.json`
- `data/output/trends.json`
- `data/output/keywords.json`

**품질 기준:**
- ✅ 모든 통계는 샘플 크기 (n) 함께 보고
- ✅ 상관관계는 p-value 함께 보고 (유의수준 0.05)
- ✅ 트렌드는 신뢰구간 함께 보고 (95% CI)

---

### Stage 5: 출력 (Export)

**명령:**
```bash
python3 .claude/pipelines/05_export.py --input data/output/ --format dashboard,json,csv
```

**출력 형식:**
1. **대시보드:** `index.html` + `data.json` (GitHub Pages 배포용)
2. **JSON:** API 제공용 (`/api/ex/metrics`)
3. **CSV:** HR 팀 Excel 분석용
4. **보고서:** `reports/EX_analysis_20260815.md` (에세이 형식)

**품질 기준:**
- ✅ 대시보드는 2 초 이내 로딩
- ✅ JSON 은 OpenAPI 명세 준수
- ✅ 보고서는 HR 전문가가 읽을 수 있는 수준 (통계 용어 설명 포함)

**Human Gate #4:** 감정 분석 점수 (sentiment_score) 가 -0.8 미만인 피드백은 인간이 직접 읽음

---

## 3. 휴먼 게이트 명세 (Human Gate Specification)

| 게이트 이름 | 설명 | 경험적 근거 | 실행 함의 |
|------------|------|------------|----------|
| **Human Gate #1: 몰입도 격차 검토** | 부서별 몰입도 격차가 1 점 초과일 때, 원인 분석을 인간이 검토 | Sales 부서 피드백 문화 부재 (면담 기록) | AI 자동 진단 금지, HR 팀 직접 인터뷰 |
| **Human Gate #2: 온버딩 버디 매칭** | 신규 입사자 버디 매칭은 인간이 수행 | "방치 기간" 인식 (신규 입사자 면담) | AI 자동 매칭 금지, 인간 관계성 고려 |
| **Human Gate #3: 이상치 레코드 검토** | 검증 실패 레코드 중 5% 이상 시 원본 소스 검토 | 데이터 수집 오류 가능성 (과거 이력) | AI 자동 제거 금지, HR 팀 수동 확인 |
| **Human Gate #4: 감정 분석 점수 검증** | sentiment_score 가 -0.8 미만인 피드백은 인간이 직접 읽음 | NLP 모델의 한국어 뉘앙스 오해 가능성 | AI 자동 분류 금지, HR 팀 직접 읽기 |

---

## 4. INGEST Protocol (Vault 통합)

**핵심 철학:** "브리핑은 자기가 무엇과 중복되는지 모른다"

ex-analyzer 의 출력 (보고서, 대시보드) 은 csp-brain Vault 의 **Signal 노드**로 INGEST 됩니다.

### 4.1 INGEST 판정 기준

- **NEW:** 새로운 EX 인사이트 (예: "Sales 부서 심리적 안전감 1 점 격차") → `wiki/signals/YYYY-MM-DD-ex-dept-gap.md`
- **MERGE:** 기존 신호의 업데이트 (예: "직무 몰입도 트렌드" 심화) → 기존 Signal 노드의 `## Timeline` 에 추가
- **DUPLICATE:** 동일한 브리핑 이미 처리됨 → `processed: true` 마킹만

**참조:** `knowledge-management` 스킬의 `references/ingest-duplicate-detection.md`

### 4.2 Evening Reflect 통합

ex-analyzer 실행 당일의 Evening Reflect (`outputs/daily-reflect/REFLECT_YYYY-MM-DD.md`) 에 반드시 통합:

1. **Knowledge Atoms:** 4 개 이하로 요약 (통계 → Vault 연결 → 핵심 통찰 → HR 실행 함의 → Human Gate)
2. **심리학적 성찰:** "데이터는 침묵한다. 경험은 말한다" — Guardian → Gardener 정체성 전환
3. **One Strategy:** 내일 아침 구체적인 실행 과제 3 가지

**참조:** `knowledge-management` 스킬의 `references/evening-reflect-protocol.md`

---

## 5. 품질 기준 (Quality Standards)

### 5.1 데이터 무결성

- ✅ **스키마 준수:** 모든 레코드가 JSON 스키마 검증 통과
- ✅ **익명화:** employee_id 는 SHA-256 해시 처리
- ✅ **이력 추적:** 원본 → 정규화 → 검증 이력 로그 기록

### 5.2 분석 신뢰성

- ✅ **샘플 크기 보고:** 모든 통계는 n= 함께 보고
- ✅ **유의수준:** 상관관계는 p-value 함께 보고 (0.05 기준)
- ✅ **신뢰구간:** 트렌드는 95% CI 함께 보고

### 5.3 보고서 품질

- ✅ **에세이 형식:** 불렛 리스트 나열 지양, 철학적 성찰 포함
- ✅ **한국어:** 명확하고 품격 있는 한국어 사용
- ✅ **One Strategy:** 내일 아침 실행 가능한 구체적 과제 3 가지
- ✅ **Human Gate:** AI 자동화 금지 영역 명시

### 5.4 대시보드 성능

- ✅ **로딩 속도:** 2 초 이내
- ✅ **반응형:** 모바일/태블릿 호환
- ✅ **실시간:** GitHub Pages 자동 sync (4 시간 주기)

---

## 6. Pitfalls 및 교훈

### 6.1 "양적 성장 = 건강" 착각

**문제:** 처리 레코드 수만 추적하고, 인사이트의 질을 무시함.
**교훈:** "처리 레코드 1,000 건보다 실행 가능한 인사이트 1 개가 귀하다."
**해결:** 보고서에 **실행 함의 (HR Execution Implication)** 섹션 필수 포함.

### 6.2 "스키마 준수 = 진실" 착각

**문제:** 스키마를 통과한 데이터만 신뢰하고, 이상치를 자동으로 제거함.
**교훈:** "이상치는 오류가 아니라, 다른 이야기를 하는 데이터일 수 있다."
**해결:** 이상치는 **Human Gate #3** 으로 전달, AI 자동 제거 금지.

### 6.3 "AI 분석 = 객관성" 착각

**문제:** 감정 분석 점수를 맹신하고, 인간이 읽지 않음.
**교훈:** "NLP 모델은 한국어 뉘앙스를 오해한다 (예: '죽인다' = 긍정/부정?)."
**해결:** **Human Gate #4** 구현, 극단적 점수는 인간이 직접 읽기.

### 6.4 "대시보드 = 완료" 착각

**문제:** 대시보드를 배포하면 작업이 끝났다고 착각함.
**교훈:** "대시보드는 질문을 생성해야지, 답을 주지 않는다."
**해결:** 보고서에 **One Strategy** 필수 포함 — 내일 아침 무엇을 할 것인가?

---

## 7. 실행 체크리스트

ex-analyzer 실행 전 다음을 확인하십시오:

- [ ] `ex-analyzer` 스킬 로드 (`skill_view(name='hr-analytics/ex-analyzer')`)
- [ ] 디렉토리 구조 생성 (`mkdir -p .claude/{pipelines,data/{raw,normalized,output},reports}`)
- [ ] 원본 데이터 수집 (01_ingest.py 실행)
- [ ] 정규화 실행 (02_normalize.py 실행)
- [ ] 유효성 검사 실행 (03_validate.py 실행)
- [ ] 인사이트 도출 (04_enrich.py 실행)
- [ ] 출력 생성 (05_export.py 실행)
- [ ] 보고서 작성 (에세이 형식, Human Gate 명세 포함)
- [ ] 대시보드 배포 (GitHub Pages)
- [ ] Evening Reflect 에 통합 (지식 원자로)
- [ ] INGEST 판정 (NEW/MERGE/DUPLICATE) 및 `_ops/ingest-log.md` 업데이트

---

## 8. 참고 문헌

- **ex-analyzer 스킬:** `hr-analytics/ex-analyzer` (스키마, 파이프라인 템플릿, 휴먼 게이트)
- **지식 관리:** `knowledge-management` (Evening Reflect, INGEST Protocol, Metabolism Reporting)
- **계획 작성:** `writing-plans` (bite-sized tasks, TDD, frequent commits)
- **Vault 구조:** `AGENTS.md` (Tolaria Vault 컨벤션)
- **HR 도메인:** [[bp-signal-intelligence]], [[hr-conceptual-atoms]], [[fde-talent-model]]

---

**마지막 성찰:** "이 스킬은 데이터를 분석하는 것이 아니라, 인간의 경험을 번역하는 도구입니다. 번역은 원본을 지우지 않습니다. 검열만이 지웁니다."
