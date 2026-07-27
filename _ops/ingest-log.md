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

| 처리 | 건수 | 내용 |
| :-- | :-: | :-- |
| 신규 생성 | 5 | [[fde-talent-model]], [[social-ide]], [[claude-code-skills]], [[rlm-forge]], [[poststroke-depression-network]] |
| Timeline 병합 | 4 | [[graph-rag]](BigQuery Graph), [[knowledge-capitalization]](셀피쉬클럽), [[agentic-engineering]](하네스 세션), [[claude-code-workflow]](Karpathy LLM=OS) |
| 처리 마킹(보류) | 7 | 일일 메모 4, 빈 파일 2, ADK 셋업 프롬프트 1 — 각 파일 frontmatter 의 processed_note 에 사유 기록 |

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
