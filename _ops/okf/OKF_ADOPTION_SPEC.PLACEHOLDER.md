---
type: Decision
title: OKF Adoption Spec — PLACEHOLDER (미수령)
description: 패키지 읽기 순서 1번인 정본 설계 문서. 이번 도입 작업 입력에 포함되지 않아 자리표시자로 둠.
timestamp: 2026-06-16T00:00:00Z
status: 🔴
---

# OKF_ADOPTION_SPEC.md — 미수령 (PLACEHOLDER)

> **이 파일은 자리표시자다.** OKF Adoption Package의 정본 설계 문서(`OKF_ADOPTION_SPEC.md`)는
> 이번 도입 작업의 입력에 **포함되지 않았다**. README에서 읽기 순서 1번으로 지정된 문서이며,
> 나머지 두 문서가 다음 섹션을 직접 참조한다:

PROTOCOL / BUILD_PLAN이 SPEC을 참조하는 지점:

- **§3 (번들 IN/OUT 경계)** — BUILD_PLAN 부록 A 디렉터리 결정표의 근거.
- **§5 (경로 → type 매핑)** — PROTOCOL §3.1 `derive_type`, `TYPE_MAP`의 정본.
- **§6.4 (relation 어휘 / typed-edge profile)** — BUILD_PLAN Phase 3.
- **§7 (wikilink → 링크 변환 규칙)** — PROTOCOL §3.4.
- **§8 (conformance 기준)** — PROTOCOL §4 LINT 검사 항목의 정본.
- **§10 (가정 목록)** — BUILD_PLAN Phase 0가 검증하는 대상.

## 조치

1. SPEC 원본을 확보해 이 파일을 대체한다(파일명 `OKF_ADOPTION_SPEC.md`로 교체).
2. **단, Phase 0 결과가 SPEC 가정과 크게 어긋났다**(아래 findings 참조).
   BUILD_PLAN 지침: "Phase 0 결과가 SPEC의 가정과 다르면, 코드 작성 전에 SPEC을 먼저 갱신하고
   사람 확인을 받는다." → SPEC 확보 후 `_ops/okf-phase0-findings.md`의 보정 항목을 SPEC에 반영한다.
3. Phase 1 코드 착수는 SPEC 확보 + Phase 0 결정 사람 확인 이후.
