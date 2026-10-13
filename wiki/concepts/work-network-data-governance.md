---
title: Work Network 데이터 정비 원칙 (원문·추출·확정 분리)
created: 2026-10-12
updated: 2026-10-13
type: concept
status: seed
tags: [work-network, workflow, data-governance, provenance, ai-inference, hr-data]
aliases: [Work Network 데이터 정비, 원문-추출-확정 분리, Activity 원장]
generated: {by: ai-assisted-ingest, at: 2026-10-12}
evidence: mixed
---

# Work Network 데이터 정비 원칙 (원문·추출·확정 분리)

## Compiled Truth

### 정비 원칙 [confirmed]

(원문: `Work_Network_데이터정비_ACT0019_20261012_추론보충.xlsx` 의 `00_관리원칙` 시트)

- **요약 원칙**: 원본 보존 · 업무 정의 · 관계 정의 · 실행 증거를 분리하고, 원문/추출/확정 및 제출/정의/관계/실행/품질 상태를 구분한다.
- **네 구획**: 원본 보존(원본 시트는 변경하지 않고 뒤에 둔다, 이미 유실된 보정 전 값은 "복원불가"로 명시), 업무 정의(기존 Activity_Code 보존 + 관리용 Activity_Object_ID 별도 부여), 관계 정의(모든 연결은 유형·조건·근거·확인 상태를 가진 Relation_ID), 실행 증거(정의상 출력과 실제 Run에서 확인된 증거를 분리, 미확보는 미확인 유지).
- **두 분리**: 값의 분리(원문값·추출값·확정값을 별도 열로, AI 추론명과 확인완료명을 섞지 않음), 상태의 분리(제출·정의·관계·실행·품질검증 상태를 각각의 열로).
- **추론 보충 규칙**: 추론 보충값은 별도 시트에서 신뢰성(높음/중간/낮음)과 함께 관리하고, 사람이 확인자·확인일을 남기기 전에는 확정값으로 승격하지 않는다.

### 현황 수치 [confirmed]

원본 레코드 779건 → Activity 객체 740개. 기존 코드 734, 중복 코드 그룹 33(동일명 27, 코드 충돌 6). 보정명 105건 중 AI 추론명 80, 코드 매핑명 25이며 105건 모두 미확인. ACT-0019(교육 결과보고 계열) 원본 2행, 실행 Run 1건 — "PLC LV1 2차 결과보고: 결재·첨부는 확인, 입력 원천·LMS 반영·HRD-NET 환급은 미확인".

### 해석과 연결 [inferred]

- Work Network는 구성원이 제출한 업무 활동 기록을 업무 정의·관계·실행 증거로 엮어, 조직이 실제로 일하는 방식을 지도로 만드는 데이터로 보인다.
- 이 정비본의 첫 원칙은 데이터를 고치는 것보다 **무엇이 원래 값이고 무엇이 손댄 값인지를 끝까지 구분하는 것**이다. 이는 [[ex-insight-mining-pipeline]]과 ex-analyzer의 Human Gate("이상치를 AI가 자동 제거하지 않는다")와 같은 계보의 규칙이다.
- [[knowledge-capitalization]]에 출처(provenance)라는 조건을 붙인 사례로 읽힌다. 자산은 쌓인 양이 아니라 믿을 수 있는 정도로 가치가 매겨진다.
- AF 오퍼레이션 메타모델(10-08 v0.3, 관찰 중)의 "상태는 사건에서 파생되고, 틀린 기록은 정정 사건으로 쌓는다"와 같은 사고방식을 데이터 정비 현장에서 실천한 것이며, [[autonomous-factory]]가 공정에 요구하는 "검증 가능한 행동"을 HR 업무 데이터에 요구한 셈이다. 이 저장소의 인식 상태 규칙(confirmed/inferred/unknown)과도 구조가 같다.

### 아직 모르는 것 [unknown]

- ACT-0019의 승인 필수 기준, LMS·환급 승인 필요 여부와 선후관계 (원문이 "미확인"으로 명시).
- 정비본의 관리원칙을 사람이 설계했는지, AI가 초안을 만들고 사람이 채택했는지.

---

## Timeline

### 2026-10-12

- Drive `Work_Network_데이터정비_ACT0019_20261012_추론보충.xlsx`(10-12 생성)의 `00_관리원칙` 시트에서 신규 편입. 핵심 지표(원본 779 · 객체 740 · 중복 코드 그룹 33 · 코드 충돌 6 · 보정명 105 중 AI 추론 80/코드 매핑 25, 전부 미확인), 관리 구획 8종, 6단계 검토 순서.
- **Human Gate**: 01~08 시트는 작성자 실명·사내 이메일·팀명을 포함하므로 Vault로 옮기지 않았다. 원본은 Drive에만 있다.
- 연결: [[knowledge-capitalization]] · [[ex-insight-mining-pipeline]] · [[autonomous-factory]].

### 2026-10-13 — 인식 상태 표시 적용

- 원문 시트에 적힌 원칙·수치는 [confirmed], Work Network의 정의·계보·연결 해석은 [inferred], 원문이 미확인으로 둔 항목과 설계 주체는 [unknown]으로 나눴다. 내용은 삭제하지 않았다.
