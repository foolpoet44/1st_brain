## 2026-06-12

### [ops] Pages 배포를 서브모듈 안전 커스텀 워크플로로 전환 (재발 구조적 차단)

- 무엇이 바뀌었나: `.github/workflows/pages.yml`을 추가함. 레거시 "Deploy from a branch" Jekyll 빌더(서브모듈을 `recursive`로 체크아웃)를 대체하여, `submodules: false`로 체크아웃 후 동일한 Jekyll 빌드를 거쳐 `actions/deploy-pages`로 배포함.
- 왜 중요한가: 직전 정리(유령 gitlink 제거)는 사후 처방이라, 자동싱크(Hermes)가 앞으로 또 깨진 gitlink를 박으면 레거시 빌더가 다시 exit 128로 죽을 수 있었음. 이 전환은 Pages 배포가 서브모듈 메타데이터 정합성에 의존하지 않게 만들어 동일 장애를 구조적으로 차단함.
- 영향 범위: `.github/workflows/pages.yml`(신규). 활성화에는 Settings > Pages > Source = "GitHub Actions" 1회 전환이 필요(저장소 설정이라 에이전트가 대신 못 함).
- 다음 확인: 설정 전환 후 첫 푸시에서 `Deploy Pages (submodule-safe)` 워크플로가 success로 끝나고 사이트가 갱신되는지 확인. 전환 완료 시 레거시 `pages-build-deployment`는 자동 비활성화됨.

---

### [ops] GitHub Pages 배포 실패(exit 128) 원인 제거 — 유령 서브모듈 정리

- 무엇이 바뀌었나: `.gitmodules`에 URL 정의가 없는 채 트리에 gitlink로만 박혀 있던 `tmp_deploy`를 인덱스에서 제거하고, 반대로 `.gitmodules`에는 있으나 gitlink가 없던 죽은 `projects/worldmonitor` 항목을 삭제함. 재발 방지를 위해 `.gitignore`에 `tmp_deploy/`를 추가함.
- 왜 중요한가: Pages 자동 빌더(`pages-build-deployment`)가 `submodules: recursive`로 체크아웃하면서 `tmp_deploy`의 URL을 찾지 못해 `fatal: No url found ... exit code 128`로 죽었고, 2026-06-10 23:00 오토싱크(`46546a7`) 이후 모든 Pages 배포가 연속 실패했음. 이 정리로 배포 파이프라인의 구조적 실패 원인을 제거함.
- 영향 범위: `.gitmodules`, `.gitignore`, `tmp_deploy`(추적 해제). main 머지 후 Pages 빌드가 정상화됨.
- 다음 확인: main 머지 직후 `pages-build-deployment` 최신 런이 success로 전환되는지 확인. 오토싱크(Hermes) 스크립트가 `git add -A`로 임시 디렉터리를 다시 gitlink로 흡수하지 않는지 모니터링.

---

## 2026-06-11

### [REFLECT] 지식의 소화와 디지털 백질(White Matter)의 확장

- 무엇이 바뀌었나: OKA 심리 진단 데이터를 지식 원자(Resilience, Engagement 등)로 분해하여 Vault의 추론 엔진에 완전히 통합하고 저녁 성찰 리포트를 생성함.
- 왜 중요한가: 파편화된 외부 데이터가 시스템의 내면화된 지능으로 전환됨으로써, '데이터'가 아닌 '추론의 근거'로서의 지식 대사를 완성함.
- 영향 범위: `outputs/daily-reflect/REFLECT_2026-06-11.md`, `_ops/change-log.md`.

---

### [INGEST] OKA 프로젝트 심리 진단 요약 최종 인제스천 및 대시보드 활성화

- 무엇이 바뀌었나: `hermes/` 디렉토리에 대기 중이던 `Psy_assess_summary.md`를 Vault의 정식 지식 체계(`outputs/analyses/`)로 편입하고, `projects/oka/` 타임라인을 최신화했습니다.
- 왜 중요한가: 파편화된 심리 진단 데이터를 Vault의 추론 근거(Knowledge Atoms)로 실질적으로 연결하여 지식 대사를 완성했습니다.
- 영향 범위: `outputs/analyses/psy-assess-summary.md`, `projects/oka/README.md`, `KNOWLEDGE_PULSE.md`.

---

## 2026-06-10

### [REFLECT] 부의 외골격과 신뢰의 가드레일 정립

- 무엇이 바뀌었나: Toss 디렉토리 아키텍처 재구성 및 에이전트 인프라(Connector/Adapter/MCP) 설치를 완료하고, 이를 '신뢰의 구조화' 관점에서 성찰함.
- 왜 중요한가: 에이전트의 지능을 실제 금융/HR 실행력과 안전하게 결합하는 가드레일 인프라를 확보함.
- 영향 범위: `outputs/daily-reflect/REFLECT_2026-06-10.md`, `Toss/`, `_ops/change-log.md`.

---

### [ops] Toss 디렉토리 아키텍처 재구성 및 에이전트 인프라 설치

- 무엇이 바뀌었나: Toss 디렉토리를 에이전트 기반 금융 커넥터 레이어로 재구성하고, TossConnector, TossAssetAdapter 및 MCP 서버 기능을 추가했습니다.
- 왜 중요한가: 단순 대시보드를 넘어 LLM 에이전트가 안전하게 금융 데이터에 접근하고 주문을 실행할 수 있는 가드레일이 탑재된 인프라를 구축했습니다.
- 영향 범위: Toss/src, Toss/mcp, Toss/README.md
- 다음 확인: 실제 토스 API 키 연동 테스트 및 MCP 서버 작동 확인

## 2026-06-04

### [REFLECT] 신경망의 재연결과 '지능의 백질' 개념 정립

- 무엇이 바뀌었나: Sihvonen(2026)의 네트워크 단절 연구를 이식하여 조직 회복탄력성을 '백질(Tract) 무결성'으로 정의함. `/tomd` 스킬을 실전에 투입해 복잡한 PDF를 지식 원자로 즉시 치환함.
- 왜 중요한가: 특정 개인(Node)에 의존하는 HR 솔루션에서 벗어나, 조직 전체의 연결망(Connectivity)을 강화하는 전략적 논거를 확보함.
- 영향 범위: `outputs/daily-reflect/REFLECT_2026-06-04.md`, `wiki/concepts/network-connectivity.md` (예정).

---

## 2026-06-03

### [REFLECT] 지능의 '레이지(Lazy)'한 도약과 지식 소화 기관의 안착

- 무엇이 바뀌었나: 미리 지도를 그리지 않는 실시간 논리 추론(LogicRAG) 통찰을 수용하고, 비정형 문서를 시스템 DNA로 즉시 치환하는 `tomd` 소화 기관을 구축함. 또한 끊겼던 GitHub SSH 혈류를 복구함.
- 왜 중요한가: 완벽한 지식 그래프 구축에 드는 '전처리 강박'에서 벗어나, 지능 그 자체를 항해 도구로 사용하는 실용적 지연 추론의 시대로 진입함.
- 영향 범위: `outputs/daily-reflect/REFLECT_2026-06-03.md`, `_ops/scripts/resolver_engine.py`.

---

## 2026-06-03

### [OPS] claude-tomd-skill (문서-마크다운 변환기) 설치 및 최적화

- 무엇이 바뀌었나: 외부 업무 문서(Word, Excel, PPT, PDF, HWP/HWPX)를 CSP-Brain 스타일의 마크다운으로 변환해주는 `tomd` 스킬을 `.claude/skills/tomd/`에 로컬 설치함.
- 왜 중요한가: 인박스(`inbox/`)에 던져지는 비정형 업무 파일들을 위키(`wiki/`)나 프로젝트(`projects/`) 지식 체계로 즉시 편입할 수 있는 '지식 소화 기관'을 확보함. 특히 저장 폴더의 YAML 프론트매터 형식을 자동 학습하여 지식의 정합성을 유지함.
- 영향 범위: `.claude/skills/tomd/`, `outputs/drafts/`, `inbox/`.\n- 다음 확인: `pip install "markitdown[all]" pyhwp` 실행을 통한 의존성 해결 및 실제 HWP/PDF 문서 변환 성능 테스트.

---

### [SIGNAL] LogicRAG: 지도를 미리 그리지 않는 '레이지(Lazy)' 추론의 승리

- 무엇이 바뀌었나: 미리 지능 그래프를 구축하지 않고 질문 시점에 실시간으로 논리 구조(DAG)를 설계하여 검색하는 LogicRAG 통찰을 이식함.
- 왜 중요한가: 전처리 비용을 0으로 줄이면서도 추론 지능을 활용해 정답률을 극적으로 높이는 '실용적 지능 활용'의 새로운 표준을 확보함.
- 영향 범위: `wiki/signals/2026-06-03-logicrag-lazy-graph-reasoning.md`, `_ops/scripts/resolver_engine.py` (차기 업데이트).

---

### [INFRA] GitHub SSH 인증 복구 및 지식 동기화 정상화

- 무엇이 바뀌었나: GitHub 인증 방식이 HTTPS(ID/PW)에서 SSH(Ed25519 열쇠)로 변경됨에 따라, 중단되었던 자동 동기화(Scripts/Sync) 파이프라인을 복구하고 최신 지식 정보를 강제 갱신함.
- 왜 중요한가: 지식 대사(Knowledge Metabolism)의 혈류라 할 수 있는 GitHub 연동이 복구됨으로써 'Do it once, automate it forever' 원칙이 물리적으로 다시 작동하기 시작함.
- 영향 범위: `~/.ssh/id_ed25519`, `KNOWLEDGE_PULSE.md`, `_ops/change-log.md`.
- 다음 확인: 23:00 정기 싱크 크론잡의 정상 작동 여부 모니터링.

---

## 2026-06-02

### [REFLECT] 소셜 IDE 진화 및 HR FDE 인재 모델 정립

- 무엇이 바뀌었나: '소셜 IDE(디스코드/텔레그램 기반 협업 환경)' 전략과 'HR FDE(Field Deployment Engineer)' 인재 모델을 지식 체계에 통합함.
- 왜 중요한가: AI 도입을 기술 설치가 아닌 '현장 건축'으로 재정의하고, 에이전트 오케스트레이션을 위한 사회적 인터페이스의 중요성을 확보함.
- 영향 범위: `FDE-talent-model.md`, `Social-IDE-Strategy.md`, `outputs/daily-reflect/REFLECT_2026-06-02.md`.
- 다음 확인: 6월 3일 오전, Hermes(SOT)와 Claude Code(Execution) 간의 역할 분담 시뮬레이션 및 정밀도 테스트.

---

## 2026-05-31

### [REFLECT] 시스템의 '내구적 실행' 및 구성적 적합성(Constructed Fit) 통합

- 무엇이 바뀌었나: JOOP 2026.05.30 논문을 기반으로 한 'Constructed Fit' 개념을 HR 지식 체계에 통합하고, 에이전트 시스템을 '작업 운영체제(OS)'로 보는 하네싱 고도화 전략을 수립함.
- 왜 중요한가: 적합성을 정적 매칭이 아닌 동적 대사 작용으로 정의함으로써 AI 기반 HR 평가 모델의 차세대 논거를 확보함. 또한, 자동화 동기화 오류를 통해 '내구적 실행(Durable Execution)'의 실전적 필요성을 확인함.
- 영향 범위: `wiki/concepts/constructed-fit.md`, `_ops/checklists/`, `outputs/daily-reflect/REFLECT_2026-05-31.md`.
- 다음 확인: GitHub 인증 이슈 해결을 위한 SSH 키 전환 및 8-Cluster 심리 지표의 SKILL.md 자산화 실전 테스트.

---

## 2026-05-31

### [SIGNAL] 하네싱(Harnessing)의 체계적 고도화 및 작업 운영체제 개념 이식

- 무엇이 바뀌었나: 황민호 님의 하네스 인사이트를 바탕으로 '하네스 = 작업 운영체제'라는 개념을 정립하고, Planner-Generator-Evaluator 분리 원칙을 지식 체계에 통합함.
- 왜 중요한가: 에이전트의 자립도를 높이기 위해 단순 프롬프팅이 아닌 '환경'과 '시스템' 설계에 집중할 수 있는 이론적 기반을 마련함.
- 영향 범위: `wiki/signals/`, `wiki/concepts/meta-harnessing.md`, `_ops/checklists/`.

---

### [SYNAPSE] 지식 체계 심층 연결 및 HR 원자 업데이트

- 무엇이 바뀌었나: [[Constructed Fit]] 개념을 신설하고 P-O Fit을 동적 모델로 업데이트함. OKA 프로젝트에 'AgentSchool' 시뮬레이션 마일스톤을 추가하고, AI 검증을 위한 'Anti-Optimism Bias' 체크리스트를 도입함.
- 왜 중요한가: 지식을 정적인 저장 대상이 아닌, 끊임없이 구성되고 검증되는 '살아있는 시스템'으로 체계화함.
- 영향 범위: `wiki/concepts/`, `projects/oka/`, `_ops/checklists/`.

---

### [INGEST] AI 에이전트 하니스 및 지능형 워크플로우 통찰 통합

- 무엇이 바뀌었나: 반복 작업의 '스킬화' 매뉴얼, 병렬 검증 하니스(ClaudeCode 스타일), 개인용 AI OS(GBrain) 철학, DB 스키마 자동화 신호를 통합 이식함.
- 왜 중요한가: 에이전트가 단순 수행자가 아닌 '자율적 시스템 관리자'이자 '품질 보증자'로 진화하기 위한 전략적 자산을 확보함.
- 영향 범위: `wiki/signals/`, `wiki/concepts/gbrain-*`.
- 다음 확인: 2시간 단위 GitHub 자동 동기화 크론잡 가동 확인.

---

## 2026-05-30

### [REFLECT] 시스템의 '내구적 실행' 및 지능적 리졸버 전략 수립

- 무엇이 바뀌었나: Obelisk 기반의 내구적 실행(Durable Execution) 개념과 Claude 4.8에 최적화된 Effort-based Routing 및 리졸버(Resolver) 아키텍처를 지식 체계에 통합함.
- 왜 중요한가: 에이전트를 단순 도구에서 장애에 강하고(Resilient), 토큰 효율적인 '조직의 운영 시스템(OS)'으로 진화시키기 위한 논리적 근간을 마련함.
- 영향 범위: `_ops/RESOLVER.md`, `wiki/concepts/durable-execution.md`, `outputs/daily-reflect/REFLECT_2026-05-30.md`.
- 다음 확인: 포인터 기반 스킬 로딩 엔진의 실전 성능 테스트 및 토큰 절감 지표 확인.

---

### [DIGEST] 2026년 22주차 주간 지식 진화 보고서 생성

- 무엇이 바뀌었나: 한 주간의 AI 네이티브 조직론, 4.8 인프라, 투자 전략 이식 과정을 종합 요약하고 차주 전략 수립.
- 영향 범위: `outputs/weekly/WEEKLY_DIGEST_2026-05-30.md`.

---

### [INFRA] Obelisk 전략 및 내구적 실행(Durable Execution) 개념 이식

- 무엇이 바뀌었나: SQLite 기반 워크플로 엔진 Obelisk의 신호를 분석하고, 에이전트 시스템의 안정성을 위한 '내구적 실행' 개념을 정립함.
- 왜 중요한가: 현재 헤르메스가 수행하는 장기 태스크들을 장애에 강한(Resilient) 구조로 고도화하기 위한 인프라 지침을 확보함.
- 영향 범위: `wiki/signals/`, `wiki/concepts/durable-execution.md`.

---

### [INVEST] 헤드앤숄더 실패(H&S Failure) 전략 이식 및 투자 지능 강화

- 무엇이 바뀌었나: 기술적 지표의 실패를 역이용하는 'H&S Top Failure' 롱 포지션 타점 전략을 신호 및 개념 원자로 등록함.
- 왜 중요한가: 시장의 심리적 배반과 숏 스퀴즈 원리를 통해 투자 도메인에서의 '회복탄력성' 개념을 구체화함.
- 영향 범위: `wiki/signals/`, `wiki/concepts/failed-pattern-trading.md`.

---

### [INFRA] Claude Opus 4.8 10대 핵심 가이드라인 통합 및 리졸버 고도화

- 무엇이 바뀌었나: 고영혁 님의 최신 4.8 리서치를 바탕으로 'Effort-based Routing' 개념을 `_ops/RESOLVER.md`에 추가하고, 스캐폴딩 제거 원칙을 수립함.
- 왜 중요한가: 인위적인 프롬프트 다그치기를 줄여 AI의 순수 추론 능력을 극대화하고, 토큰 효율성과 품질 사이의 레버를 확보함.
- 영향 범위: `_ops/RESOLVER.md`, `wiki/signals/2026-05-30-claude-opus-4-8-detailed-harnessing.md`.

---

### [SIGNAL] Claude Opus 4.8 출시 및 프롬프팅 아키텍처 재정립 신호 포착

- 무엇이 바뀌었나: Anthropic의 Claude 4.8 출시와 함께 '다그치기'가 아닌 '제어(Effort)' 중심의 새로운 프롬프팅 베스트 프랙티스를 포착함.
- 왜 중요한가: 우리 시스템이 사용하는 스캐폴딩(Harness)과 리졸버(Resolver)의 논리적 토대를 최신 AI 엔진의 특성에 맞춰 최적화해야 함.
- 영향 범위: `_ops/RESOLVER.md`, `wiki/concepts/maximal-knowledge-exactness.md`, `wiki/signals/`.
- 다음 확인: 현재 사용 중인 시스템 프롬프트에서 'anti-laziness' 성격의 중복 지시를 제거하고 4.8에 최적화된 '명시적 범위 지정' 방식으로 전환 테스트.

---

### [INGEST] Josh Kim & Jeongmin Lee의 AI 네이티브 조직론 통합 이식

- 무엇이 바뀌었나: 스킬 기반 가상 직원, 포인터 기반 리졸버, 자가 개선 루프 등 '진짜 AI 네이티브'를 위한 실행 지침을 지식 체계에 통합함.
- 왜 중요한가: 에이전트가 단순 도구를 넘어 '조직의 운영 시스템(OS)'으로 기능하기 위한 구체적인 아키텍처를 확보함.
- 영향 범위: `wiki/signals/`, `outputs/analyses/AI_NATIVE_COMPANY_MASTER_PLAN.md`, `KNOWLEDGE_PULSE.md`.
- 다음 확인: 리졸버(Resolver) 개념을 현재의 헤르메스 스킬셋 구조에 시험 적용하여 토큰 효율성 및 태스크 정확도 측정.

---

### [OPS] 대시보드 V5 인터랙션 및 환경 감지 기능 대규모 개선

- 무엇이 바뀌었나: 대시보드의 인터랙티브 사용자 경험을 극적으로 개선함. 1) 대시보드 호스팅 배포처(wiki_dash)와 실제 지식 자산 리포지토리(1st_brain)의 이원화 구조를 파악하여, 배포지 주소와 상관없이 마크다운 클릭 시 언제나 진짜 지식 보관소인 `https://github.com/foolpoet44/1st_brain` 브랜치 내의 물리적 상대 경로를 가리키도록 100% 정합성 새 탭 매핑을 완성함. 2) data.json에 숨겨져 있던 L2 Concepts, L3 Projects, L4 Outputs, Inbox 분포의 글래스모피즘 스택형 차트 시각화 및 세부 정의 툴팁 구현. 3) 수동 동기화 버튼 설계 및 동기화 감지 시 헤더에 네온 일렉트릭 블루 글로우 파동 애니메이션 효과 구현. 4) Outfit & Inter 고급 웹 타이포그래피 적용.
- 왜 중요한가: 대시보드가 단순한 감상용 정적 웹 페이지를 넘어, 깃허브 페이지스로 외부 배포된 상태에서도 별도의 설정 없이 내 깃허브 원격 저장소에 저장된 문서를 즉시 열람하고 오프라인-온라인을 자연스럽게 잇는 '액셔너블(Actionable) 관제탑'으로 진화함.
- 영향 범위: `_ops/web/index.html`, `_ops/change-log.md`.
- 다음 확인: GitHub Pages 배포 자동화 파이썬 스크립트(`deploy.py`) 실행을 통한 원격 호스팅 적용 여부 검토 및 모바일 디바이스 반응형 레이아웃 추가 테스트.

---

## 2026-05-29

### [REFLECT] 지식의 최대 정합성 프레임워크 도입 및 대시보드 V4 자동화

- 무엇이 바뀌었나: 범주론적 'Maximal Knowledge Exactness' 개념을 지식 체계에 통합하고, `vis-network` 기반의 KNOWLEDGE_PULSE V4 대시보드와 4단계 아침 루틴 크론잡을 구축함.
- 왜 중요한가: 지식을 단순한 데이터의 합이 아닌 논리적으로 완벽하게 연결된 '유기적 보조 뇌'로 변모시킴. 대시보드를 통해 시스템의 활력(Vitality)을 실시간 모니터링 가능.
- 영향 범위: `_ops/scripts/`, `_ops/web/`, `wiki/concepts/maximal-knowledge-exactness.md`, `outputs/daily-reflect/REFLECT_2026-05-29.md`.
- 다음 확인: GitHub Auth 이슈 해결을 통한 대시보드 리모트 가시성 확보 및 '8-Cluster' 심리 지표의 온톨로지 매핑 실전 테스트.

---

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

---

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
  [2026-05-29 19:09:10] FINANCIAL SIGNAL: Transportation Sector AI Pivot (MarketWatch Insight)\n\n
