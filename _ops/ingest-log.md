---
type: Note
status: Active
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
