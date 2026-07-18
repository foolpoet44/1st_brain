## 2026-07-18

### [REFLECT] 저녁 성찰: 번역이라는 노동

- 무엇이 바뀌었나: 오늘 같은 배치로 INGEST된 [[ax-internalization]](3대 기둥+애자일 3 Phase), [[sf-domain-mapping]](44개 직무역량↔4대 도메인 번역), [[fde-talent-model]](Palantir FDE 벤치마크·정체성 확장), [[ex-insight-mining-pipeline]](현상학적 귀납×연역 교차 분석) 네 지식 원자를 엮어 `outputs/daily-reflect/REFLECT_2026-07-18.md`를 새로 작성함(기존 파일은 아래 [OPS] 항목 참조). 네 문서 모두 "번역"이라는 같은 동작을 하고 있으며, 원본(기존 언어·정체성·습관)을 지우지 않아야 번역이 검열로 전락하지 않는다는 공통 설계 원칙을 짚음.
- 왜 중요한가: 오전 편입분(bp-signal-intelligence 등)이 이미 다룬 "감시 대 돌봄" 축과 별개로, 같은 날 도착한 나머지 네 문서가 "번역 대 검열"이라는 두 번째 축을 이루고 있음을 드러냄. AX 내재화 실행 계층(전략→도메인 매핑→인재 트랙→인사이트 파이프라인) 전체가 오늘 하루에 갖춰졌다는 것을 보여주는 지표.
- 영향 범위: `outputs/daily-reflect/REFLECT_2026-07-18.md`, `_ops/change-log.md`. wiki 원본 문서는 무변경(읽기만 함).
- 다음 확인: FDE 부트캠프 및 SF Domain 매핑을 실제 커리큘럼/선발 프로세스에 반영할 때, 이 반성에서 도출한 "원본을 지우지 않는 번역" 원칙(신뢰도 등급 공개, 정체성 확장 언어 사용 등)이 실제로 지켜지는지 확인.

### [OPS] Hermes 자동화가 저녁 성찰 아카이브를 덮어씀 — 데이터 무결성 점검 필요

- 무엇이 바뀌었나: 오늘 17:00 KST 커밋(`48ee3cf`, author: Hermes Agent)이 오전 INGEST 지식(bp-signal-intelligence 등, 바로 아래 원래 [REFLECT] 항목이 기록하고 있던 그 에세이)을 다룬 `REFLECT_2026-07-18.md`를 "크론잡 모델 폐기 사태"라는 무관한 서사로 완전히 덮어썼고, 이전에 존재하지 않았던 `REFLECT_2026-07-15.md`~`07-17.md`도 같은 서사로 새로 생성함. 해당 사건의 근거는 change-log/ingest-log 등 볼트 어디에도 없음. 이번 저녁 실행에서 실제 지식 기반 에세이로 재작성해 복구함.
- 왜 중요한가: 이 프로토콜과 Hermes 자동화가 `outputs/daily-reflect/` 같은 경로에 각자 쓰기 작업을 하면서, 한쪽이 다른 쪽의 실제 지식 종합 결과를 조용히 지운 사례. "무엇이 어떻게 바뀌고 있는지 잘 모르겠다"는 CSP의 핵심 페인포인트가 자동화 간 충돌로 재발할 위험을 보여줌. `scripts/cron_health_monitor.sh`도 같은 커밋으로 신규 생성됨(Hermes 소유 추정, 검토 필요).
- 영향 범위: `outputs/daily-reflect/REFLECT_2026-07-15.md`~`18.md`, `scripts/cron_health_monitor.sh`(신규), `KNOWLEDGE_PULSE.md`.
- 다음 확인: CSP가 Hermes와 이 프로토콜의 쓰기 경로를 분리할지(예: `outputs/daily-reflect/` 소유권 단일화, 파일명에 소스 태그 추가) 판단 필요. 다음 실행 전 `git log --author="Hermes Agent"`로 유사 덮어쓰기가 반복되는지 확인 권장.

- 무엇이 바뀌었나: 오늘 INGEST된 [[bp-signal-intelligence]](신호 상태 기계), [[opq-framework]](UCF×Leader Edge 그림자 점등 규칙), [[k-smart-model]](3국 스마트팩토리 벤치마크) 세 지식 원자를 엮어 `outputs/daily-reflect/REFLECT_2026-07-18.md`를 생성함. 세 시스템 모두 "사람에 대한 신호를 감지하는 시스템은 감시로 흐르기 쉽다"는 동일한 위험 앞에서, 인간 개입 게이트를 명시적으로 남기는 같은 설계 답을 내놓고 있음을 짚음.
- 왜 중요한가: 개별 프로젝트 문서만 보면 각자의 스펙으로 흩어져 있던 설계 결정("조치 칸만 사람이 지킨다", "판결이 아닌 가설로만 말한다", "노사 상생 협정이 우선")이 사실은 하나의 원칙 — 감지 능력과 그 절제는 별개의 설계 축이라는 것 — 임을 드러냄. 앞으로 새 신호/평가 파이프라인 설계 시 참조할 기준선이 됨.
- 영향 범위: `outputs/daily-reflect/REFLECT_2026-07-18.md`, `_ops/change-log.md`. wiki 원본 문서는 무변경(읽기만 함).
- 다음 확인: EX Signal Intelligence Phase 0-1(스키마·49건 정제) 착수 시, 이 반성에서 도출한 "인간 게이트 명시" 원칙을 설계 문서에 실제로 반영하는지 확인.

### [OPS] 위키 대시보드 스크롤 불능 수리 및 사용성 개선

- 무엇이 바뀌었나: `index.html`의 높이 제약 사슬이 끊겨(grid 아이템의 `min-height:auto` 기본값) 데스크톱에서 오른쪽 컬럼 하단 카드(Knowledge Gaps 등)가 잘린 채 스크롤로도 접근 불가능하던 문제를 `min-h-0` + 컬럼 `overflow-y-auto`로 수리함. 함께 10초마다 전체 innerHTML 재렌더링이 목록 스크롤 위치와 그래프 시점을 리셋하던 문제를 "데이터 변경 시에만 갱신 + 90초 주기"로 바꾸고, 그래프 물리엔진을 안정화 후 동결, 터치 기기에서 캔버스의 팬/줌이 페이지 스크롤을 삼키지 않도록 비활성화, 1024px 미디어쿼리 경계 충돌 해소, vis-network 버전 고정(@10.1.0), 헤더에 지식 인덱스 링크 추가.
- 왜 중요한가: 관제판의 존재 이유는 "변경 가시성"인데, 정작 화면의 40% 분량(1366×768 기준)이 존재하지만 영원히 볼 수 없는 상태였음. 이제 모든 해상도에서 전체 카드에 도달 가능하고, 보던 화면이 10초마다 리셋되지 않음.
- 영향 범위: `index.html`, `_ops/change-log.md`. 데이터 파이프라인·빌드 스크립트는 무변경.
- 다음 확인: Pages 배포 후 실제 기기(모바일 터치 스크롤, 노트북 해상도)에서 스크롤 동작 확인. 남은 개선 후보: Tailwind Play CDN → 정적 CSS 컴파일, 8~9px 저대비 텍스트 가독성, 목록 항목 키보드 접근성.

## 2026-07-11

### [SYNAPSE] OKA 심리 진단 분석 결과 최종 적용 및 지식 대사 완결

- 무엇이 바뀌었나: `hermes/` 디렉토리에 대기 중이던 `Psy_assess_summary.md`를 정규화하여 `outputs/analyses/psy-assess-summary.md`로 편입하고, 관련 프로젝트(`projects/oka/`)와 개념 원자(`opq-framework`)를 연결함.
- 왜 중요한가: 분석된 파편적 데이터를 시스템의 '장기 기억'이자 '추론 근거'로 전환함으로써, HR 도메인 전문가의 지능을 에이전트 환경에 성공적으로 이식함.
- 영향 범위: `outputs/analyses/psy-assess-summary.md`, `projects/oka/README.md`, `KNOWLEDGE_PULSE.md`, `_ops/change-log.md`.

## 2026-07-09

### [REFLECT] 지능의 나침반과 오케스트레이션의 내재화

- 무엇이 바뀌었나: 2026 AI 도구 6대 택소노미(범용·리서치·개발·생산성·콘텐츠·자동화)를 확립하고, 슈퍼에이전트의 실질적 가치 측정을 위한 'Agentic ROI' 및 'Verification Gates' 개념을 정립함.
- 왜 중요한가: 기술 과잉 시대에 체계적인 분류를 통해 인지적 주권을 회복하고, 실행자가 아닌 시스템 지휘자로서의 HR 정체성을 공고히 함.
- 영향 범위: `outputs/daily-reflect/REFLECT_2026-07-09.md`, `_ops/change-log.md`.

## 2026-07-08

### [INGEST] AI 툴 업무별 정리 가이드 (2026 Ver.) 구축

- 무엇이 바뀌었나: 2026년 기준 핵심 AI 도구들을 6대 업무 도메인별로 분류한 `AI-TOOLBOX-2026.md`를 생성함.
- 왜 중요한가: 업무 워크플로우에 최적화된 도구 조합을 제시함으로써 조직의 AX(AI Transformation) 가이드라인을 확보함.
- 영향 범위: `AI-TOOLBOX-2026.md`, `outputs/daily-reflect/REFLECT_2026-07-08.md`.
