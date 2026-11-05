---
title: ESCON
created: 2026-11-05
updated: 2026-11-05
type: project
status: growing
tags: [project, hr, saas, platform, skill-ontology, ax]
aliases: [ESCON 플랫폼, Digital Skill Ontology]
generated:
  by: ai-assisted-ingest
  at: 2026-11-05
evidence: mixed
---

# ESCON

## Compiled Truth

### 정의 [confirmed]

ESCON 은 ESCO(European Skills, Competences and Occupations) 표준을 토대로 삼은 HR 통합 플랫폼이며, 그 핵심 자산은 **Digital Skill Ontology** — 스킬과 스킬 사이의 관계를 기계가 읽을 수 있게 적어 둔 지도다. 1 차 구현은 **조직 → Enabler → Skill** 3 계층으로, "어떤 스킬이 존재하고 그것들이 어떻게 연결되는가"에 답한다. 즉 초기 ESCON 이 다루는 것은 *지식의 지도*이고, 사람의 이동 경로는 아직 그 안에 없다.

### College·Level 확장 (v1.0 설계) [confirmed]

설계 v1.0 은 기존 지도 위에 "누가·어떤 순서로·어떤 깊이까지 배우는가" — 곧 *사람의 여정* — 레이어를 얹어 **College → Level(Lv1~4) → Enabler → Skill** 5 계층으로 확장한다. College 는 네 갈래(physical-ai / **data-intelligence** / agentic-ai / digital-twin)이고 Level 은 AX Starter → Practitioner → Specialist → Expert 로 올라간다. data-intelligence 가 **HUB** 로 지정되어, Lv2 이상의 비(非)HUB 레벨은 data-intelligence 를 선수 과목으로 갖는다.

설계의 제 1 원칙은 **비파괴**다. 기존 Enabler·Skill 데이터는 건드리지 않고, 신규 테이블 3 개(colleges · levels · level_prerequisites)와 기존 `enablers` 의 nullable 컬럼 2 개(college_id · level_tier)만 더한다. 롤백 스크립트를 함께 둔다.

### 데이터 공백 진단 [confirmed]

기존 5 개 도메인은 대부분 physical-ai 칼리지에 몰려 있고 나머지 세 칼리지는 비어 있다. 따라서 확장은 스키마를 바꾸는 일이 아니라 **빈 칼리지를 점진적으로 채우는 일**이다.

### 왜 이 확장이 토대인가 [inferred]

이 5 계층이 서자 세 가지가 비로소 계산 가능해진다 — 학습경로의 선수 관계 검증, 인재 Pool 커버리지("Lv3 30 명 대비 충원율"), 그리고 경로 시각화. 세 기능이 공통으로 요구하는 것은 "스킬의 목록"이 아니라 "스킬 사이의 순서"이기 때문이다.

[[sf-domain-mapping]] 과의 관계도 같은 자리에서 설명된다. 직무역량평가 44 개 소분류를 4 대 도메인으로 번역한 좌표계가 *현재 위치*를, 프로젝트 스킬맵이 *도달 목표*를 가리키고, ESCON 의 College→Level 축이 그 둘 사이의 **거리를 단계로 환산**한다. [[fde-talent-model]] 의 양성 트랙은 이 환산 위에서만 "몇 단계 남았는가"를 말할 수 있다.

### 상태 [unknown]

2026-07-18 기록 기준 블로커는 Vercel 빌드 오류(Temporal Knowledge Graph 관련)이며, College·Level 확장은 데이터 레이어라 빌드와 무관하다고 적혀 있다. **이 블로커의 현재 해소 여부는 저장소에서 확인할 수 없다** — 2026-07-18 이후 프로젝트 문서의 상태 갱신이 없다.

---

## Timeline

### 2026-11-05

- **[위키 신설]** `projects/escon/README.md` 의 Compiled Truth 를 위키 노드로 승격했다. 이 문서를 세운 직접적 이유는 지식 자체보다 **도달**이다 — 위키 안에서 `[[escon]]` 이라는 이름을 부르는 링크가 **9 건**(`sf-domain-mapping` 2 · `fde-talent-model` 2 · `IO_PSYCHOLOGY_BRIEFING_2026-07-24` 3, 그리고 `leader-member-exchange` 의 표기 2) 있었으나, 그 이름을 가진 위키 문서는 없었다. 폴더 `projects/escon/` 은 있었고 문서는 없었다.
- 인식 상태 표시 적용: 정의·5 계층 설계·공백 진단 `[confirmed]`(2026-07-18 Drive 설계문서 v1.0 편입분) / 토대 해석 `[inferred]` / 블로커 현황 `[unknown]`.
- 유효 나가는 링크 2 건 — [[sf-domain-mapping]] · [[fde-talent-model]].
- 원천: `projects/escon/README.md`(created 2026-04-14, updated 2026-07-18). 원본은 수정하지 않았다.
