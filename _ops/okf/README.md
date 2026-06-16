# OKF Adoption Package — csp-brain

csp-brain(`foolpoet44/1st_brain`)에 Open Knowledge Format v0.1을 적용하기 위한 **Claude Code 빌드용 문서 묶음**.

## 읽는 순서

1. **OKF_ADOPTION_SPEC.md** — 무엇을·왜 (정본 설계: 번들 경계, 이중 방언, type 매핑, relations profile, conformance).
2. **OKF_PUBLISH_PROTOCOL.md** — 어떻게 돌리나 (PUBLISH 패스 변환 규칙, LINT=conformance, Python 참조 스켈레톤).
3. **OKF_BUILD_PLAN.md** — 어떤 순서로 (Phase 0 인벤토리 → Phase 1~4, 수용 기준·위험).

## 핵심 원칙 (모든 문서 공통)

- 갈아엎지 않는다. csp-brain은 이미 ~90% OKF. **번들 경계 + 발행 프로토콜 하나** 추가.
- 옵시디언 작성본은 **비파괴 보존**. OKF는 `dist/okf/`로 나가는 발행 산출물.
- Claude Code는 코드 전에 **Phase 0로 실제 리포를 검사해 가정을 검증**한다.

## 핸드오프

리포 루트에 이 묶음을 두고(예: `_ops/okf/`), BUILD_PLAN 부록 C의 부트스트랩 프롬프트로 첫 세션을 시작한다.

## 현재 상태 (2026-06-16)

- ✅ 패키지 문서 보존: `_ops/okf/` (이 디렉터리).
- ⚠️ **`OKF_ADOPTION_SPEC.md` 미수령** — 정본 설계 문서가 아직 이 리포에 없다. PROTOCOL/BUILD_PLAN이 SPEC §3/§5/§6/§7/§8을 참조하므로 Phase 1 코드 착수 전 반드시 확보해야 한다. 자리표시자: `OKF_ADOPTION_SPEC.PLACEHOLDER.md`.
- ✅ **Phase 0 완료**: `_ops/okf-phase0-findings.md` — 실제 리포 인벤토리로 SPEC 가정 검증. AC0 충족.
- ⏸️ Phase 1~4: 코드 미착수 (SPEC 확보 + Phase 0 결정 사람 확인 대기).
