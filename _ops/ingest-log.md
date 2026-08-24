## 2026-08-22 — INGEST 수행

- **신규 (NEW):** 0 개
- **병합 (MERGE):** 3 개
- **중복 종결 (DUPLICATE):** 0 개

### 병합 상세

- BRIEFING_MONEY-FLOW_2026-08-22.md -> BRIEFING_2026-08-03.md
- BRIEFING_IO-PSYCH_2026-08-22.md -> 2026-07-23-wadi-human-centric-design.md
- BRIEFING_MONEY-FLOW_2026-08-21.md -> 2026-05-30-harness-is-not-just-a-leash.md

### 판정 근거

- 통계 매칭 기준: 2 개 이상 일치 시 MERGE
- 3 개 브리핑 모두 기존 문서와 4-6 개 통계 일치로 MERGE 판정

---

## 2026-08-14

- **신규 (NEW)**: 0 건
- **병합 (MERGE)**: 2 건
  -  →  (의사결정 피로 재확인)
  -  →  (인종 편향 85.1%/100%/35% 신규 추가)
- **중복 종결 (DUPLICATE)**: 0 건
- **판정 근거**: 
  - IO-PSYCH: "의사결정 피로 10.5% 감소" 통계가 BRIEFING_2026-07-30_IO_PSYCHOLOGY.md 에 이미 편입되어 있음
  - HR-TECH: "52% 자율 에이전트", "26% 후보자 신뢰", "70% vs 8% 신뢰 격차" 등 핵심 통계가 2026-07-22-autonomous-hiring-paradox.md 에 이미 존재

---

---
type: Note
status: Active
---

## 2026-08-13 — INGEST 프로토콜 수행 (아침 브리핑 6 건)

**집계**:
- **신규 (NEW)**: 0 건
- **병합 (MERGE)**: 6 건
- **중복 종결 (DUPLICATE)**: 0 건

**판정 근거**:
- **HR-TECH 3 건** (08-10, 08-11, 08-12): 2026-07-22-autonomous-hiring-paradox.md 에 병합
  - 이유: 52% 에이전트 도입, 26% 편향, Eightfold FCRA, 70% vs 8% 신뢰 격차 — 모두 기존 문서에 있음
- **IO-PSYCH 1 건** (08-11): 2026-07-22-autonomous-hiring-paradox.md 에 병합
  - 이유: arXiv:2603.14963 (의미 보호 구역), arXiv:2605.28680 (Decency vs Meaningfulness) — HR 실행 함의 중복
- **MONEY-FLOW 2 건** (08-11, 08-12): 2026-08-10-capital-flow-market-neutral.md 에 병합
  - 이유: Fed 금리, 환율 1460 원, 5:5 자산배분 — 자본시장 신호 중복

**인용된 Human Gate**:
- Human Gate #1-4: 에이전트 조직 설계, DEI 벤더 심사, 의미 보호 구역, 도메인별 AI 영향 평가 (IO-PSYCH)
- Human Gate #1-4: 편향 감사, 법적 리스크 모니터링, 후보자 경험 심의회, 진화 게이트 (HR-TECH)
- Human Gate #1-3: Fed 금리 감시, 환율 임계치, 자산배분 심의 (MONEY-FLOW)

**후속 작업**:
- [ ] 2026-07-22-autonomous-hiring-paradox.md 의 Timeline 에 4 건 브리핑 내용 추가
- [ ] 2026-08-10-capital-flow-market-neutral.md 의 Timeline 에 2 건 브리핑 내용 추가
- [ ] _ops/change-log.md 에 [INGEST] 엔트리 추가
- [ ] wiki/signals/_index.md 에 링크 존재 확인

---


# Ingest Log

inbox/ 에서 wiki/ 로 자료가 수집된 기록입니다.

---

## 2026-05-24 Ingest (Claude Code)

- **대상**:
  - `inbox/notes/2026-04-29.md`
  - `inbox/notes/2026-05-02-Test-Capture.md`
  - `inbox/notes/2026-05-02-메모-인터페이스.md`
  - `inbox/notes/Invalid date.md`
  - `inbox/short_memo/2026-W18-short_memo.md`
- **처리 결과**:
  - `2026-04-29.md` → `projects/ax-internalization/README.md` 타임라인에 인사 실무 이슈로 기록.
  - `메모-인터페이스.md` & `Test-Capture.md` → `wiki/concepts/execution-surface.md`에 인터페이스 실험 사례로 통합.
  - `Invalid date.md` → 시스템 잔여물로 판단하여 정리 완료 (Processed).
  - `2026-W18-short_memo.md` → 테스트용 메모로 확인, `wiki/concepts/memo-architecture.md` (예정) 관점에서 참조 후 처리.
- **다음 확인**: `inbox/` 파일들의 물리적 삭제 또는 `processed: true` 플래그 추가.

---

## 2026-04-30 Dream Cycle

- 확인 대상: `inbox/notes/2026-04-29.md`, `inbox/notes/Invalid date.md`
- 처리 결과: wiki/project 승격 없음
- 이유: `2026-04-29.md`는 생산기술담당, 국내 출장, 근태 제도변경, 건설팀 해외출장 이슈 키워드를 담고 있으나 귀속 프로젝트와 결정 사항이 불명확하다. `Invalid date.md`는 깨진 daily 템플릿 잔여물로 판단된다.
- 다음 확인: 업무 이슈 메모를 HR 운영 프로젝트로 승격할지, 단순 daily note로 보관할지 CSP 판단 필요.

---

## 2026-07-02 — 성장 루프 첫 회전 (Issue #13)

대시보드 Action Queue 의 INGEST 카드로 발행된 일감. inbox 16건 전체 처리.

| 처리            | 건수 | 내용                                                                                                                                                     |
| :-------------- | :--: | :------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 신규 생성       |  5   | [[fde-talent-model]], [[social-ide]], [[claude-code-skills]], [[rlm-forge]], [[poststroke-depression-network]]                                           |
| Timeline 병합   |  4   | [[graph-rag]](BigQuery Graph), [[knowledge-capitalization]](셀피쉬클럽), [[agentic-engineering]](하네스 세션), [[claude-code-workflow]](Karpathy LLM=OS) |
| 처리 마킹(보류) |  7   | 일일 메모 4, 빈 파일 2, ADK 셋업 프롬프트 1 — 각 파일 frontmatter 의 processed_note 에 사유 기록                                                         |

모든 inbox 파일에 `processed: true` + `processed_date` + `processed_note` 마킹.

---

## 2026-07-18 Drive 설계문서 INGEST

Google Drive 유입 설계문서 14건 처리. EX Intelligence 하위 시스템 + Physical AI/스마트팩토리 인재육성 두 클러스터.

- `BP_Signal_Intelligence_개발명세서.md` → wiki/concepts/bp-signal-intelligence.md / **new**
- `EX_Insight_Mining_Pipeline_설계서.md` → wiki/concepts/ex-insight-mining-pipeline.md / **new**
- `ESCON_College_Level_Extension_Design.md` → projects/escon/README.md / **merge**
- `Physical_AI_Tech_Leader_Pool_조직설계.md` → projects/physical-ai-talent/README.md / **new**
- `Physical_AI_Tech_Leader_면접계획서.md` → projects/physical-ai-talent/README.md / **merge**
- `스마트팩토리-전문가-육성방안-보고서.md` → wiki/concepts/k-smart-model.md / **new**
- `직무역량_SF_Domain_매핑.md` → wiki/concepts/sf-domain-mapping.md / **new**
- `AI_Factory_기술전문가_육성체계_v2_2.md` → projects/physical-ai-talent/README.md / **merge**
- `Ax-internalization.md` → wiki/concepts/ax-internalization.md / **merge**
- `Opq-ucf-le.md` → wiki/concepts/opq-framework.md / **merge**
- `PRI_FDE_대화아카이브.md` → wiki/concepts/fde-talent-model.md / **merge**
- `ex-oi-integration-strategy.md` → projects/ex-intelligence/README.md / **merge**
- `EX-Intelligence-보고-3단계-실행-로드맵.md` → projects/ex-intelligence/README.md / **merge**
- `2026_AX_역량강화_업무계획.md` → projects/ax-internalization/README.md / **merge**

신규 5(bp-signal-intelligence, ex-insight-mining-pipeline, k-smart-model, sf-domain-mapping, projects/physical-ai-talent) / 병합 9 / 처리 inbox 14건 전부 `processed: true`.

---

## 2026-08-04 밀린 브리핑 일괄 INGEST

7/23 ~ 8/03 사이 inbox 에 적체된 브리핑 11 건 처리. 생산(매일 브리핑 자동 생성)은 돌아갔으나 소화(INGEST)가 멈춰 있던 구간을 해소.

**신규 3 건**

- `IO_PSYCHOLOGY_BRIEFING_2026-07-23.md` → wiki/signals/2026-07-23-wadi-human-centric-design.md / **new**
- `IO_PSYCHOLOGY_BRIEFING_2026-07-24.md` → wiki/signals/2026-07-24-cognitive-offloading-skill-decay.md / **new**
- `HR_Tech_Briefing_2026-07-26.md` → wiki/signals/2026-07-26-self-evolving-agents-evolution-gate.md / **new**

**병합 4 건**

- `HR_Tech_Briefing_2026-07-23.md` → wiki/signals/2026-07-22-autonomous-hiring-paradox.md / **merge**
- `HR_Tech_Briefing_2026-07-24.md` → wiki/signals/2026-07-22-autonomous-hiring-paradox.md / **merge**
- `HR_TECH_BRIEFING_2026-07-29.md` → wiki/signals/2026-07-26-self-evolving-agents-evolution-gate.md / **merge**
- (스키마 확장) → wiki/concepts/bp-signal-intelligence.md / **merge**

**중복 종결 4 건** — 이미 편입되었거나 신규 정보가 없어 마킹만 수행

- `BRIEFING_2026-07-30_IO_PSYCHOLOGY.md` — wiki/synapses/IO_PSYCHOLOGY_SYNAPSE_2026-07-30.md 에 기수록
- `BRIEFING_2026-08-01.md` / `BRIEFING_2026-08-03.md` — \_ops/change-log.md + csp-brain/vault/ 에 기편입
- `REFLECT_2026-08-01_SUMMARY.md` — 08-01 브리핑의 요약본
- `notes/2026-07-14.md` — 브리핑 아닌 스킬 작업 메모

**판단 근거**: 브리핑들이 반복 제안한 `signal-autonomous-hiring-economics`, `signal-trust-design-patterns`, `signal-skill-adjacency-matching` 3 개 노드는 **생성하지 않았다.** 세 주제의 핵심 수치(52% / 74% / $1,400 / 73% / 3-5 배 / 16%)가 이미 `2026-07-22-autonomous-hiring-paradox.md` 2 절에 전부 들어 있어, 분리 시 같은 사실이 두 곳에서 따로 낡아간다. 대신 두 브리핑이 실제로 더한 증분(조정 비용 역설 60%, 에이전트 3 세대 컨덕터 모델, SDT 3 축 훼손)만 해당 문서 Timeline 에 기록했다.

신규 3 / 병합 4 / 중복 종결 4 / inbox 11 건 전부 `processed: true`.

---

## 2026-08-05 — INGEST 프로토콜 수행

### 판정 요약

- **신규 생성**: 0 건
- **병합**: 1 건
  - `outputs/briefings/BRIEFING_HR-TECH_2026-08-05.md` → `wiki/signals/2026-07-22-autonomous-hiring-paradox.md` (Timeline 에 증분 기록)
- **중복 종결**: 4 건 (브리핑이 제안한 signal 노드 모두 기존 문서에 포함됨)
  - `signal-ai-trust-gap-2026` (기존: 2026-07-22 문서 2.2 절)
  - `signal-algorithmic-monoculture-2026` (기존: 2026-07-22 문서 2.3 절 + 2026-07-26 문서)
  - `signal-autonomous-agent-adoption-2026` (기존: 2026-07-22 문서 2.1 절)
  - `signal-skills-based-hiring-acceleration-2026` (기존: 2026-07-22 문서 2.4 절)

### 판정 근거

1. **중복 대조 완료**: `wiki/signals/` 에서 브리핑의 핵심 통계 (52% 자율 에이전트, 71-74% 후보자 불신, 26% 인종 편향) 검색.
2. **기존 문서 확인**: `2026-07-22-autonomous-hiring-paradox.md` 가 동일 주제를 포괄하며, 2026-07-26, 2026-07-29 브리핑이 이미 Timeline 에 병합됨.
3. **증분 추가**: 신뢰의 사다리 프레임, Stanford HAI 알고리즘 모노컬처 통계, Human Gate 4 종 명세를 Timeline 에 기록.
4. **신규 노드 생성 금지**: 브리핑이 제안한 4 개 signal 노드는 모두 기존 문서의 2.1~2.4 절이 이미 포함. 분리 시 백링크만 늘고 사실의 소유권이 흐려짐.

### 사람 판단 필요 항목

- **없음**. 모든 통계가 복수 출처 (Greenhouse, Stanford HAI, Perelson & Associates) 에 기반하며, 개인정보·생체정보·감시와 관련된 스키마 변경도 없음.

### 후속 조치

- [ ] Human Gate 4 종을 [[bp-signal-intelligence]] 의 `evolution_gate` 스키마에 명세화
- [ ] 알고리즘 모노컬처 통계 (Stanford HAI) 다음 브리핑에서 재확인 시 별도 신호 승격 검토

---

## 2026-08-06 18:30:54

- **신규**: 0건
- **병합**: 1건
- **중복 종결**: 0건

### 상세
병합: BRIEFING_MONEY-FLOW_2026-08-06.md → 2026-05-30-harness-is-not-just-a-leash.md (통계 중복: 2026)

## 2026-08-08 18:33:07

### 판정 요약

- **신규 생성 (NEW)**: 0 건
- **병합 (MERGE)**: 6 건
- **중복 종결 (DUPLICATE)**: 0 건

### 병합 상세

| 원본 파일 | 대상 wiki/signals/ 문서 | 추가된 증분 |
| :--- | :--- | :--- |
| BRIEFING_MONEY-FLOW_2026-08-07.md | 2026-05-30-harness-is-not-just-a-leash.md | 자본 중립화 신호 (Equity Market Neutral 29%) |
| BRIEFING_MONEY-FLOW_2026-08-08.md | 2026-05-30-harness-is-not-just-a-leash.md | Fed 금리/환율/해외투자 신호 |
| BRIEFING_HR-TECH_2026-08-07.md | 2026-07-22-autonomous-hiring-paradox.md | 10 전문에이전트, 자기진화 (MOSS), 88% AI 스크리닝 |
| BRIEFING_HR-TECH_2026-08-09.md | 2026-07-22-autonomous-hiring-paradox.md | 자율채용 경제성 (/hire), SHRM 2026, 알고리즘 모노컬처 |
| BRIEFING_IO-PSYCH_2026-08-07.md | 2026-07-24-cognitive-offloading-skill-decay.md | 알고리즘 관리 자율성 40% 감소, SDT 메타분석 |
| BRIEFING_IO-PSYCH_2026-08-08.md | 2026-07-26-self-evolving-agents-evolution-gate.md | SCAN 프레임워크, LLM 감정편향, 메타인지 프롬프트 |

### 판정 근거

1. **중복 대조 완료**:  에서 각 브리핑의 핵심 통계 검색 (grep).
2. **기존 문서 확인**: 모든 브리핑이 기존 signal 문서와 통계적 중복을 가짐.
3. **증분 추가**: 각 문서의  섹션에 2026-08-07/08/09 일자 증분 기록.
4. **신규 노드 생성 금지**: 브리핑이 제안한 signal 노드는 모두 기존 문서가 포괄. 분리는 백링크만 늘리고 사실의 소유권을 흐림.

### 사람 판단 필요 항목

- **없음**. 모든 통계가 복수 출처 (Barclays, SHRM, Stanford HAI, arXiv) 에 기반하며, 개인정보·생체정보·감시와 관련된 스키마 변경도 없음.

### 후속 조치

- [ ] 6 개 브리핑 파일 모두  마킹 완료
- [ ] change-log.md 에 CLAUDE.md 4 절 형식으로 기록 필요
- [ ] wiki/signals/_index.md 에 병합된 문서들의 링크 존재 확인

---

## 2026-08-10 — INGEST 프로토콜 수행 (아침 브리핑 5 건)

**집계**:
- **신규 (NEW)**: 1 건 — 2026-08-10-capital-flow-market-neutral.md (MONEY-FLOW 도메인 첫 신호)
- **병합 (MERGE)**: 4 건 — BRIEFING_IO-PSYCH_2026-08-10.md, BRIEFING_HR-TECH_2026-08-09.md, BRIEFING_MONEY-FLOW_2026-08-09.md, BRIEFING_MONEY-FLOW_2026-08-07_SUMMARY.md, BRIEFING_MONEY-FLOW_2026-08-10.md
- **중복 종결 (DUPLICATE)**: 0 건

**판정 근거**:
1. **BRIEFING_IO-PSYCH_2026-08-10.md** → MERGE to 2026-07-22-autonomous-hiring-paradox.md
   - 이유: 26% 편향 통계, agent-native 조직 개념이 기존 문서와 중복
2. **BRIEFING_HR-TECH_2026-08-09.md** → MERGE to 2026-07-22-autonomous-hiring-paradox.md
   - 이유: Trust Ladder, autonomous hiring, Human Gate 개념이 기존 문서와 중복
3. **BRIEFING_MONEY-FLOW_2026-08-09.md** → MERGE to 2026-08-10-capital-flow-market-neutral.md (신규 생성)
   - 이유: MONEY-FLOW 도메인의 자본시장 신호 — 기존 문서 없음
4. **BRIEFING_MONEY-FLOW_2026-08-07_SUMMARY.md** → MERGE to 2026-08-10-capital-flow-market-neutral.md
   - 이유: 동일 도메인 (MONEY-FLOW), 헤지펀드 중심 — 신규 문서에 통합
5. **BRIEFING_MONEY-FLOW_2026-08-10.md** → MERGE to 2026-08-10-capital-flow-market-neutral.md
   - 이유: 동일 도메인 (MONEY-FLOW), 시장 중립 전략 — 신규 문서에 통합

**인용된 Human Gate**:
- Human Gate #1: 에이전트 조직 설계 심의회 (IO-PSYCH)
- Human Gate #2: DEI 위원회 벤더 심사 (IO-PSYCH)
- Human Gate #3: 실무자 참여 AI 설계 심의 (IO-PSYCH)
- Human Gate #4: 직무 의미 재정의 심의회 (IO-PSYCH)
- Human Gate #1: 에이전트 조직 설계 심의회 (HR-TECH)
- Human Gate #2: 집중 한도 심의 (HR-TECH)
- Human Gate #3: 신뢰 점수 재검토 (HR-TECH)
- Human Gate #4: 3 단계 진화 게이트 (HR-TECH)
- Human Gate #1: 단일 자산 한도 심의 (MONEY-FLOW)
- Human Gate #2: 환율 임계치 돌파 자동매도 금지 (MONEY-FLOW)
- Human Gate #3: 인플레이션 헤지 20% 할당 심의 (MONEY-FLOW)

**후속 작업**:
- [ ] 2026-07-22-autonomous-hiring-paradox.md 의 Timeline 에 IO-PSYCH, HR-TECH 브리핑 내용 추가
- [ ] 2026-08-10-capital-flow-market-neutral.md 의 Timeline 에 MONEY-FLOW 브리핑 3 건 내용 추가
- [ ] _ops/change-log.md 에 [INGEST] 엔트리 추가

---

## 2026-08-15 — MONEY-FLOW 브리핑 INGEST

- **NEW**: 0 건
- **MERGE**: 2 건
  -  →  (Timeline append)
  -  →  (Timeline append)
- **DUPLICATE**: 1 건
  -  (이미 2026-08-06 에 처리됨, processed: true)

**판정 근거**:
- 2026-08-13 브리핑: 60/20/20 포트폴리오 제안은 기존 60/40 논의의 연장선 (MERGE)
- 2026-08-15 브리핑: 신뢰 사다리 프레임은 기존 Trust Ladder 개념의 심화 (MERGE)
- 2026-08-06 브리핑: 이미 processed 마킹 완료 (DUPLICATE)

**인출된 Human Gate**: 4 개
1. 안전자산 재정의 심의회 (AI automation prohibited)
2. 베타 제거 평가 위원회 (분기 1 회 배경 영향 감사)
3. 환율 레짐 시프트 수용 선언 (연 1 회 정책 재설계)
4. 골드 20% 할당론의 HR 번역 (반기 1 회 담론 테스트)

---

## 2026-08-20 — Cron INGEST Execution

- 신규: 0 건
- 병합: 7 건
- 중복 종결: 0 건

- 2026-08-20 18:32: MERGE BRIEFING_MONEY-FLOW_2026-08-17.md -> 2026-08-10-capital-flow-market-neutral.md (23개 통계 일치)
- 2026-08-20 18:32: MERGE BRIEFING_IO-PSYCH_2026-08-20.md -> 2026-07-22-autonomous-hiring-paradox.md (27개 통계 일치)
- 2026-08-20 18:32: MERGE BRIEFING_HR-TECH_2026-08-18.md -> 2026-07-22-autonomous-hiring-paradox.md (22개 통계 일치)
- 2026-08-20 18:32: MERGE BRIEFING_MONEY-FLOW_2026-08-16.md -> 2026-07-22-autonomous-hiring-paradox.md (18개 통계 일치)
- 2026-08-20 18:32: MERGE BRIEFING_HR-TECH_2026-08-20.md -> 2026-07-22-autonomous-hiring-paradox.md (26개 통계 일치)
- 2026-08-20 18:32: MERGE BRIEFING_MONEY-FLOW_2026-08-20.md -> 2026-07-22-autonomous-hiring-paradox.md (24개 통계 일치)
- 2026-08-20 18:32: MERGE BRIEFING_IO-PSYCH_2026-08-17.md -> 2026-07-22-autonomous-hiring-paradox.md (20개 통계 일치)

## 2026-08-24 18:32

- **신규**: 0 건
- **병합**: 3 건
- **중복 종결**: 0 건
- **총 처리**: 3 건

### 판정 내역

- **MERGE**: `BRIEFING_IO-PSYCH_2026-08-24.md` → `2026-07-22-autonomous-hiring-paradox.md` (2 개 통계 일치)
- **MERGE**: `BRIEFING_HR-TECH_2026-08-24.md` → `2026-07-22-autonomous-hiring-paradox.md` (5 개 통계 일치)
- **MERGE**: `BRIEFING_MONEY-FLOW_2026-08-24.md` → `2026-08-10-capital-flow-market-neutral.md` (4 개 통계 일치)

