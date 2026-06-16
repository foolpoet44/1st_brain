---
type: Decision
title: OKF Build Plan — csp-brain (Claude Code 실행 계획)
description: Claude Code가 OKF 적용을 단계적으로 빌드하기 위한 작업 분해·수용기준·위험 목록.
tags: [okf, build-plan, claude-code, implementation]
timestamp: 2026-06-16T00:00:00Z
status: 🔄
---

# OKF Build Plan — csp-brain

> 설계: `OKF_ADOPTION_SPEC.md` · 실행 사양: `OKF_PUBLISH_PROTOCOL.md` · **이 문서: 빌드 순서.**
> Claude Code는 이 계획을 위에서 아래로 수행한다. 각 Phase는 **수용 기준(AC)**을 통과해야 다음으로 넘어간다.
> 모든 파괴적 변경 전 사람 확인. 작성본 비파괴, 출력은 `dist/okf/`.

## Phase 0 — 인벤토리 & 가정 검증 (코드 없음, 먼저 수행)

SPEC §10의 가정을 실제 리포로 검증한다. 결과를 `_ops/okf-phase0-findings.md`에 기록.

작업:
- [ ] 번들 IN 각 디렉터리의 .md 개수 + 프론트매터 보유율 측정.
- [ ] 기존 프론트매터 키 분포 수집(충돌 키 식별).
- [ ] `concepts/` vs `wiki/concepts/`, `decisions/` vs `wiki/decisions/` 중복·드리프트 진단 → **정본 디렉터리 결정**.
- [ ] 위키링크 표본 100개: 경로형/이름형/별칭형/임베드 비율 + 이름 충돌 후보.
- [ ] `_index` 파일 위치·확장자 분포.
- [ ] `moc/` 콘텐츠 성격 판정(색인 vs 독립 개념).
- [ ] `weekly/`·`projects/*/Timeline` 실제 포맷 → log.md 매핑 규칙 초안.
- [ ] `dist/okf/` 격리 방식 결정: `.gitignore` vs `okf-dist` 발행 브랜치.

수용 기준(AC0):
- `_ops/okf-phase0-findings.md`에 위 8개 항목 결론과 SPEC §3/§5/§7 수정 필요분이 적혀 있다.
- 정본 디렉터리(중복 해소 방향)가 1개로 결정되어 있다.

> ⚠ Phase 0 결과가 SPEC의 가정과 다르면, **코드 작성 전에 SPEC을 먼저 갱신**하고 사람 확인을 받는다.

## Phase 1 — type 부여 + LINT 게이트 (방안 2+1, 최소 비용 즉효)

목표: 발행 없이도 "conformance 측정"이 가능해지고 루트 정크가 격리된다.

작업:
- [ ] `scripts/okf/` 스캐폴드 + 단위 테스트 하네스(`harness/` 활용).
- [ ] `discover` + `derive_type` + `check_conformance` 구현(PROTOCOL [0][1][7]).
- [ ] `--only conformance --dry-run`으로 현재 상태 LINT 리포트 1회 생성 → 베이스라인 기록.
- [ ] 루트 정크(`무제.md`, `이름 없는 보드.md`, `untitled-daily-*`, 비정형 날짜) 격리 규칙 적용 → `inbox/` 이동 또는 삭제 큐(사람 확인).
- [ ] LINT을 기존 `LINT` 프로토콜 정의에 연결(트리거 `lint` → conformance checker).

수용 기준(AC1):
- `dist/okf/lint-report.md`가 생성되고 ERROR 건수 베이스라인이 보인다.
- 정크 파일이 번들 IN에서 사라진다(격리 완료).
- 단위 테스트: `derive_type` 전체 prefix 케이스 통과.

## Phase 2 — PUBLISH 패스 + 링크 변환 (설계결정② + 방안 3)

목표: 첫 OKF-conformant 발행본(`dist/okf/`)이 손에 들어온다.

작업:
- [ ] `ensure_frontmatter`(비파괴 병합, git timestamp) 구현(PROTOCOL [2]).
- [ ] `rename_index`(`_index`→`index.md`) + 루트 `index.md`에 `okf_version` 구현(PROTOCOL [3]).
- [ ] 전역 파일명 인덱스 + `convert_wikilinks` 구현(PROTOCOL [4], 충돌/미해석 LINT 처리).
- [ ] `generate_log`(weekly/Timeline → log.md) 구현(PROTOCOL [5]).
- [ ] `--dry-run` diff 검토 → 사람 확인 → `--write` 실행.
- [ ] 발행본을 OKF 그래프 뷰어(또는 OKF repo의 visualize)로 1회 렌더해 그래프 연결성 육안 확인.

수용 기준(AC2):
- `dist/okf/`가 SPEC §8 conformance PASS(ERROR 0).
- 발행본에 `_index`·`[[ ]]`·비정형 날짜 잔존 0(`legacy-dialect` WARN 0).
- 작성본 diff = 0(비파괴 검증).
- 멱등성: 연속 2회 `--write` 결과 동일.

## Phase 3 — Typed-Edge Profile (방안 4)

목표: 평면 그래프 → 진짜 온톨로지. people/·decisions/·skills/ 우선.

작업:
- [ ] SPEC §6.4 relation 어휘를 프론트매터 `relations`로 도입(우선 `people/`, `decisions/`).
- [ ] `relations` ↔ 본문 링크 동기화 검사 구현(PROTOCOL [6], 자동 분류 금지).
- [ ] 시드 데이터: People Context Graph 핵심 노드 + Decision supersede 체인 수기 입력.
- [ ] 뷰어에서 타입별 엣지 색상 구분 확인.

수용 기준(AC3):
- `people/`·`decisions/` 노드의 relations가 타입과 함께 직렬화된다.
- `relation-target-missing`는 INFO로만 남고 빌드를 막지 않는다.

## Phase 4 — 소비/교환 레이어 (방안 5+6)

목표: 발행본을 실제로 굴린다.

작업:
- [ ] GENERATE에 `viz.html`(Cytoscape) 산출 추가. 기존 `index.html`/`knowledge.html`과 역할 분담 문서화.
- [ ] `_config.yml`(Jekyll) 발행과 OKF 번들 공존 확인(충돌 없이 같은 소스).
- [ ] BRIDGE를 OKF 교환 포맷 위에 재정의: Obsidian(producer) → OKF → Notion(consumer). `status`/`importance` 매핑 검증.
- [ ] `ragapp/`가 `dist/okf/`를 소비하도록 인덱싱 경로 연결(이 스펙 범위 밖, 후속 과제로 티켓화).

수용 기준(AC4):
- `viz.html`이 발행본에서 1파일로 생성·열람된다.
- Notion 왕복(round-trip) 1건에서 메타데이터 손실 없음.

## 부록 A — 디렉터리 IN/OUT 결정표

| 디렉터리 | 판정 | 근거 |
| --- | --- | --- |
| wiki, concepts, decisions, people, references, permanent, projects, research, analysis, moc | **IN** | 지식 개념 |
| inbox, raw, Clippings, Toss, Atoms | OUT(피드스톡) | 미정제 원료 |
| _ops, scripts, ragapp, harness, dev, dev2, sync, sy, syncs | OUT(코드/운영) | 비지식 |
| .claude, .agents, .github, .obsidian*, .understand-anything | OUT(설정) | 도구 설정 |
| open-design@, Understand-Anything@, temp_skill@ | OUT(서브모듈) | 외부 코드 |
| outputs, sharing, weekly, thinklog | OUT(산출/로그) | weekly는 log.md 입력으로만 |
| 루트 정크(무제/이름없는보드/untitled-daily/비정형날짜) | OUT→격리 | Phase 1 |

> 이 표는 SPEC §3 기반 초안. **Phase 0 결과로 확정**한다.
> ⚠ Phase 0 검증 결과 이 표는 보정이 필요하다. `_ops/okf-phase0-findings.md` §3 참조
> (요약: 루트 `concepts/`는 추출 덤프 → OUT, 루트 `people/`는 슬라이드 이미지 오염 → 필터 필요,
> 정본 IN 번들은 사실상 `wiki/` + `projects/`).

## 부록 B — 실행 안전 체크리스트 (매 Phase 공통)

- [ ] 작업 전 깨끗한 git 상태(커밋/스태시).
- [ ] 파괴적 변경(파일 이동/삭제) 전 사람 확인.
- [ ] 발행은 `dist/okf/`로만. 작성본 수정 금지.
- [ ] `--dry-run` 검토 후에만 `--write`.
- [ ] 각 Phase 종료 시 LINT 리포트 갱신·커밋.

## 부록 C — 첫 세션 부트스트랩 프롬프트 (Claude Code)

```
이 디렉터리의 OKF_ADOPTION_SPEC.md, OKF_PUBLISH_PROTOCOL.md, OKF_BUILD_PLAN.md를
모두 읽어라. 그런 다음 BUILD_PLAN Phase 0만 수행하라:
번들 IN/OUT을 실제 리포로 검증하고, 가정과 어긋나는 부분을 _ops/okf-phase0-findings.md에
정리하라. 코드는 아직 작성하지 말고, Phase 0 수용 기준(AC0)을 만족하면 멈추고 보고하라.
```
