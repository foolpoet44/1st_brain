## 2026-07-18

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
