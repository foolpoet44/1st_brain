---
title: ESCON
created: 2026-04-14
updated: 2026-07-18
type: project
status: blocked
tags: [project, hr, saas, platform]
---

# ESCON

## Compiled Truth

HR 통합 플랫폼 — ESCO 표준 기반 Digital Skill Ontology. 현재 **조직 → Enabler → Skill** 3계층으로 "어떤 스킬이 있고 어떻게 연결되는가"(지식의 지도)를 다룬다.

**칼리지·레벨 확장 (v1.0 설계)**: 그 위에 "누가·어떤 순서로·어떤 깊이까지 배우는가"(사람의 여정) 레이어를 **비파괴적으로** 얹는다 → 5계층 `College → Level(Lv1~4) → Enabler → Skill`. 4개 칼리지(physical-ai / **data-intelligence=HUB** / agentic-ai / digital-twin) × Lv1~4(AX Starter→Practitioner→Specialist→Expert). 원칙: 기존 Enabler-Skill 데이터 변경 금지 — 신규 테이블 3개(colleges·levels·level_prerequisites) + 기존 `enablers`에 nullable 컬럼 2개(college_id·level_tier)만 추가. 진단: ESCON은 기존 5도메인이 대부분 Physical AI 칼리지에 편중, 나머지 3칼리지는 데이터 공백(점진 채움 대상). Lv2+ 비HUB 레벨은 data-intelligence를 선수로 갖는 설계 규칙(HUB 게이트). 이 확장이 학습경로 DRC 검증·인재 Pool 커버리지("Lv3 30명 대비 충원율")·경로 시각화의 공통 토대다.

**현재 블로커**: Vercel 빌드 오류 (Temporal Knowledge Graph 관련) — 단, 칼리지·레벨 확장은 데이터 레이어라 빌드 무관.

**연결**: [[sf-domain-mapping]](직무역량 좌표계) · projects/physical-ai-talent(Lv3 30명 Pool) · [[fde-talent-model]](FDE 양성 트랙).

---

## Timeline

### 2026-07-18

- **[INGEST]** Drive 설계문서 편입: **ESCON College & Level Extension Design v1.0**.
- 5계층 확장 설계: College(4) → Level(Lv1~4) → Enabler(기존) → Skill(기존). data-intelligence가 HUB.
- 비파괴 원칙: 신규 테이블 3개 + 기존 enablers nullable 컬럼 2개(college_id·level_tier)만 수정. 롤백 스크립트 동반.
- Claude Code 작업 체크리스트(Task 1~6): college-types.ts / college-mapping.json / 00X_college_level.sql / college-resolver.ts / migrate-college.js / 무결성 검증(선수 실재·HUB 게이트 규칙).
- 도메인→칼리지 매핑: 기존 5도메인 대부분 physical-ai 편중, 3칼리지 신규 확장 필요(ESCO 재임포트 별도 Phase).
- 후속 예고: 커버리지 API / 학습경로 DRC / 페르소나 경로 그래프 / FDE 5단계 양성 트랙.

### 2026-04-29

- wiki 초기화와 함께 마이그레이션
- 상태: blocked (Vercel 빌드 오류)

### 2026-04-14

- Vercel 빌드 오류로 인한 지연
- Temporal Knowledge Graph 구현 중
