## 2026-05-28

### [REFLECT] AI 네이티브 로드맵 통합 및 지식 그래프 내비게이션 전략 수립

- 무엇이 바뀌었나: 'AI 네이티브 컴퍼니 로드맵'을 수립하고, 단순 검색을 넘어선 '지식 그래프 맵'과 '맥락적 적재' 개념을 지식 체계에 통합함.
- 왜 중요한가: 에이전트가 조직의 모든 맥락을 실시간으로 학습하고, 인덱싱된 관계를 통해 토큰 비용을 혁신적으로 절감하며 판단의 설명 가능성을 확보함.
- 영향 범위: `projects/AI-Native-Company-Roadmap.md`, `wiki/concepts/knowledge-graph-as-map.md`, `outputs/daily-reflect/REFLECT_2026-05-28.md`.
- 다음 확인: 8-Cluster 심리 지표를 SKILL.md 자산으로 변환하여 지식 그래프 상의 '추론 노드'로 실전 배치 테스트.

---

## 2026-05-26

### [REFLECT] 디지털 외골격 개념 정립 및 메타-하네싱 전략 수립

- 무엇이 바뀌었나: AI agents를 단순 도구가 아닌 '디지털 외골격(Exoskeleton)'으로 정의하고, agy CLI 기반의 '메타-하네싱(Meta-Harnessing)'과 GraphRAG를 통한 '지식 맥박(Knowledge Pulse)' 로드맵을 수립함.
- 왜 중요한가: 기술적 FOMO를 주권적 효능감으로 전환하고, 에이전트 오케스트레이션의 근간(Spine)을 세움으로써 "Do it once, automate it forever"의 완성도를 높임.
- 영향 범위: `outputs/daily-reflect/REFLECT_2026-05-26.md`, `wiki/concepts/digital-exoskeleton.md`, `_ops/change-log.md`.
- 다음 확인: GraphRAG의 로컬 Vault 이식 가능성 검토 및 `agy` 스캐폴딩 스크립트(`harness_scaffold.py`)의 실전 적용 테스트.

---

## 2026-05-25

### [OPS] 토큰 최적화 도구 RTK(Rust Token Killer) 도입 및 Claude Code 연동

- 무엇이 바뀌었나: LLM 토큰 소비를 60-90% 절감하는 `rtk` 도구를 Homebrew로 설치하고, Claude Code의 PreToolUse Hook에 등록함. `~/.claude/RTK.md` 가이드를 생성하여 시스템 전반의 토큰 효율성을 확보함.
- 왜 중요한가: "Token Maxing" 전략의 실천적 도구를 확보함. 에이전트가 처리하는 데이터의 밀도를 높여 비용을 절감하고, 문맥 유지 능력을 극대화함.
- 영향 범위: 시스템 전반의 Bash 명령어 실행 환경, `/Users/dkmac/.claude/CLAUDE.md`, `~/.claude/settings.json`.
- 다음 확인: `rtk gain` 명령어를 통해 실제 토큰 절감 효과를 주기적으로 모니터링하고, `Protocol 3: LINT` 실행 시 토큰 효율성 지표 포함 검토.

### [INGEST] LinkedIn 에이전트 자동화 원칙 지식 이식 및 분석

- 무엇이 바뀌었나: 정승현 님의 '가재맨' 에이전트 사례를 분석하여 `agent-friendly-redesign`, `token-maxing` 개념을 정립하고 분석 리포트를 생성함.
- 왜 중요한가: 에이전트를 단순 도구가 아닌 '조직의 상태 관리자'로 보는 관점을 확보함. 특히 'Hermes'가 실전에서 언급된 사례를 통해 현재 시스템 방향성의 정당성을 확인.
- 영향 범위: `wiki/concepts/agent-friendly-redesign.md`, `wiki/concepts/token-maxing.md`, `outputs/analyses/linkedin-agent-automation-20260525.md`.
- 다음 확인: 현재 진행 중인 OKA 프로젝트의 '검증 단계'에 독립 에이전트 패턴(Principle 3) 적용 검토.

---

## 2026-05-24

### [OPS] 지식 체계 전반의 인덱싱 최적화 및 안정화

- 무엇이 바뀌었나: `wiki/concepts`, `wiki/people`, `wiki/tools`, `wiki/decisions` 등 4개 주요 카테고리의 인덱스 파일(`_index.md`)을 최신화하고, 최근 2주간 추가된 20여 개의 문서를 지식 그래프에 정식 편입함. 또한 `inbox/`의 백업 파일들을 정리하여 작업 환경을 정화함.
- 왜 중요한가: 지식의 개별 문서들이 파편화되지 않고 상위 인덱스에서 발견될 수 있도록 '연결성'을 확보함. 특히 최근의 '3층 아키텍처'와 'Hermes Pi' 철학이 인덱스에 반영되어 시스템의 현재 상태를 한눈에 파악 가능해짐.
- 영향 범위: `wiki/**/_index.md`, `inbox/`, `_ops/change-log.md`.
- 다음 확인: `lint` 프로토콜 정기 실행 및 `projects/` 타임라인의 주간 요약(W21) 준비.

---

### [INGEST] 인박스 파편 메모의 지식 체계 및 프로젝트 타임라인 통합

- 무엇이 바뀌었나: `inbox/`에 대기 중이던 5개의 메모를 분석하여, 실무 이슈는 `projects/ax-internalization` 타임라인에, 인터페이스 실험 데이터는 `wiki/concepts/execution-surface`에 각각 통합함.
- 왜 중요한가: 단순 테스트나 파편화된 메모를 방치하지 않고, '실행 표면'이라는 상위 개념의 증거(Evidence)로 전환함으로써 지식의 휘발을 방지함.
- 영향 범위: `projects/ax-internalization/README.md`, `wiki/concepts/execution-surface.md`, `_ops/ingest-log.md`.
- 다음 확인: 수집 완료된 `inbox/` 파일들의 물리적 정리 및 `wiki/concepts/memo-architecture.md` 설계 검토.

---

## 2026-05-23

### [REFLECT] 에이전틱 코딩 멘탈 모델 수립 및 조직 웰빙 기상도 파일럿

- 무엇이 바뀌었나: 'Thin Harness, Fat Skills' 원칙을 바탕으로 HR 전문가의 판단력을 자산화(Skill Assetization)하고, 외부 환경 데이터(날씨, 공휴일)를 HR 지식 원자와 결합한 '조직 웰빙 기상도' 모델을 설계함.
- 왜 중요한가: AI를 단순 도구가 아닌 '맥락 조력자(Contextual Champion)'로 진화시켜, HR의 역할을 '규정 관리'에서 '조직 분위기 설계(Vibe Coding)'로 확장함.
- 영향 범위: `outputs/daily-reflect/REFLECT_2026-05-23.md`, `hr-automation/org-wellbeing-monitor/SKILL.md`.
- 다음 확인: 거시 경제 지표(반도체 슈퍼사이클 등)를 웰빙 모델에 이식하여 조직 내 보상 및 성과 압박 시그널 탐지 체계 구축.

---

## 2026-05-22

### [REFLECT] FDE(Forward Deployed Engineer) 개념 정립 및 심리적 거울 효과 분석

- 무엇이 바뀌었나: jyoung105(Jeongmin Lee)의 인사이트를 바탕으로 FDE의 3대 워크플로우(Audit, Evals, Deployment)를 HR 도메인에 이식하고, AI 인터페이스가 심리적 안전감을 통해 데이터 정합성을 높이는 기제를 분석함.
- 왜 중요한가: 기술적 구현력(FDE)과 인간적 신뢰(Psychological Safety)가 결합될 때 진정한 AX(AI Transformation)가 가능하다는 전략적 토대를 마련함.
- 영향 범위: `outputs/daily-reflect/REFLECT_2026-05-22.md`, `_ops/change-log.md`.
- 다음 확인: 8-Cluster 심리 지표의 온톨로지 매핑(AOG)을 통한 추론 엔진 설계 착수.

---

## 2026-05-20

### [SIGNAL] Google I/O 2026 분석 및 지식 체계 이식

- 무엇이 바뀌었나: 2026년 구글 I/O의 주요 업데이트를 분석하여 '디지털 무의식([[digital-unconscious]])' 개념을 정립하고, 에이전틱 전환의 신호([[2026-05-20-google-io-sign-of-agentic-shift]])를 Vault에 반영함.
- 왜 중요한가: AI가 배경 조력자로 진화함에 따라 "Do it once, automate it forever" 원칙을 실현할 수 있는 기술적/철학적 토대를 지식 체계에 통합함.
- 영향 범위: `wiki/concepts/`, `wiki/signals/`, `260520.md`, `_ops/change-log.md`.
- 다음 확인: Gemini Spark 및 Information Agent 기능을 활용한 HR 채용 시장 자동 모니터링 워크플로우 설계 검토.

---

## 2026-05-18

### [INGEST] AOG(Automated Ontology Generation) 지식 원자 추출 및 이식 완료

- 무엇이 바뀌었나: 멀티 에이전트 기반 온톨로지 생성 방법론(`automated_ontology_generation.pdf`)을 분석하여 `wiki/concepts/`에 등록함.
- 왜 중요한가: HR 정책 및 규정을 논리적 '지식 그래프'로 전환하여, 향후 100% 신뢰 가능한 자동화 추론 엔진을 구축하기 위한 개념적 토대를 마련함.
- 영향 범위: `wiki/concepts/`, `_ops/change-log.md`.
- 다음 확인: 수집된 AOG 방법론을 OKA 프로젝트의 심리 지표(8-Cluster) 구조화에 시범 적용 검토.

---

## 2026-05-18

### [SIGNAL] AI 호황과 성과배분 이슈를 CSP 레이더에 추가

- 무엇이 바뀌었나: 오늘 주요이슈를 `260518.md` 일일 노트와 `wiki/signals/2026-05-18-ai-boom-labor-distribution.md` signal 문서로 정리하고, AX Internalization 및 EX Intelligence Timeline에 연결했다.
- 왜 중요한가: 삼성전자 노사 갈등은 단순 임금교섭이 아니라 AI 반도체 호황의 성과배분, 핵심인재 보상, 공급망 안정성, 조직 공정성 인식이 충돌한 약한 신호로 볼 수 있다.
- 영향 범위: `260518.md`, `wiki/signals/`, `wiki/concepts/ax-internalization.md`, `wiki/concepts/ex-intelligence.md`.
- 다음 확인: 2026-05-19 중앙노동위원회 조정 결과와 2026-05-21 파업 현실화 여부, AI 도입 조직의 ROI·구성원 경험·보상 공정성 후속 데이터.

---

## 2026-05-17

### [OPS] KBO 경기 결과 조회 자동화 스킬(kbo-results) 도입

- 무엇이 바뀌었나: 외부 커뮤니티 저장소(`NomaDamas/k-skill`)에서 `kbo-results` 스킬을 발굴하여 헤르메스 에이전트에 이식함. `kbo-game` npm 패키지를 활용한 실시간 스코어 및 경기 일정 조회 체계 구축.
- 왜 중요한가: "Do it once, automate it forever" 원칙에 따라 사용자의 반복적인 야구 경기 정보 조회를 자동화함. 검색 에이전트의 기능을 '스포츠 도메인'으로 확장함.
- 영향 범위: 헤르메스 에이전트 스킬셋, `_ops/` (향후 자동화 리포트 생성 시 활용).
- 다음 확인: 주간 다이제스트(`Protocol 4: DIGEST`) 생성 시 해당 스킬을 활용한 스포츠 신호 탐지 자동화 가능성 검토.

---

## 2026-05-17

### [INGEST] OKA 프로젝트 심리 진단(Psy_assess) 분석 및 저장 완료

- 무엇이 바뀌었나: `/Users/dkmac/Desktop/@26/hermes/` 경로에 `Psy_assess_summary.md` 산출물을 최종 생성하고, `csp-brain` Vault의 `outputs/analyses/` 및 `wiki/` 체계에 지식 원자(Atoms: Resilience, Engagement 등)를 통합함.
- 왜 중요한가: 파편화된 PDF 정보를 구조화된 지식 데이터로 전환하여 '자동 면접 질문 생성' 등 향후 자동화 업무의 추론 토대를 마련함.
- 영향 범위: `outputs/analyses/`, `wiki/concepts/`, `projects/oka/` (내부 데이터 정합성 강화).
- 다음 확인: 추출된 8-Cluster 모델을 기반으로 한 '맞춤형 채용 가이드' 생성 스크립트 설계.

---

- [2026-05-21] Josh Kim의 링크드인 인사이트 분석 및 '데이터 브릿지' 전략 리포트 생성 완료 (/outputs/analyses/INSIGHT_2026-05-21_Data_Bridge_Strategy.md)
- [2026-05-21] 헤르메스 마스터 플랜 수립: Josh Kim, 김재우, Blake Crosley의 인사이트를 통합한 3계층 아키텍처 및 자기 개선형 시스템 설계 (/outputs/analyses/MASTER_PLAN_2026-05-21_Hermes_CSP_Integration.md)
- [2026-05-21] 'Context Corpus' 개념을 시스템 지식 계층(L0)으로 공식 편입하고 마스터 플랜 업데이트 완료
[2026-05-27 16:03:55] NEW CONCEPT: skillopt.md (Self-Evolving AI Insight)
[2026-05-27 18:33:57] SIGNAL DETECTED: Agentic Recruitment Proxy (Harper Insight)
[2026-05-28 19:07:45] MISSION UPDATE: AI-Native Company Roadmap integrated.
