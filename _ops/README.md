---
title: 운영 내비게이션 — 현황은 어디서 보는가 (SSOT)
created: 2026-06-27
updated: 2026-06-27
type: ops
status: mature
tags: [ops, ssot, dashboard, navigation]
---

# _ops — 운영 메타데이터 & 현황 단일 진실 공급원(SSOT)

> CSP의 핵심 페인포인트는 "무엇이 어떻게 바뀌는지 모르겠다"이다. 그 원인의 절반은
> **현황을 보여주는 화면이 5개로 난립**해, 어디를 봐야 할지 정해져 있지 않았다는 점이다.
> 이 문서는 그 혼란을 끝낸다. **현황을 알고 싶으면 아래 두 곳만 본다.**

## ✅ 정본 (Canonical) — 이 둘만 신뢰한다

| 용도 | 위치 | 갱신 주체 |
| :--- | :--- | :--- |
| **사람이 읽는 변화 해석판** | [`_ops/change-log.md`](change-log.md) | 에이전트가 의미 있는 변경마다 4-질문 형식으로 기록 |
| **자동 통계 대시보드 (라이브)** | GitHub Pages = `_ops/web/` (`index.html`+`data.[[Understand-Anything/understand-anything-plugin/skills/understand/languages/json.md|json]]`) | `deploy-visual.yml`이 매일 `update_dashboard.py`로 갱신 후 Pages 발행 |

- "이번 주 무엇이, 왜 바뀌었나?" → **change-log.md** 를 본다.
- "지금 위키 규모·고립·신선도 통계는?" → **Pages 대시보드** 를 본다.

## ⚠️ 레거시 / 로컬 전용 — 참고만, 정본 아님

아래 표면들은 과거에 만들어졌고 일부는 로컬 자동화가 아직 재생성하지만, **신뢰의 기준으로 삼지 않는다.** 정본과 불일치할 수 있다.

| 표면 | 상태 | 비고 |
| :--- | :--- | :--- |
| `[[KNOWLEDGE_PULSE.md|KNOWLEDGE_PULSE]].md` (루트) | 로컬 자동생성 | `scripts/know_grow_monitor.py`가 매 싱크 재생성. 단발 스냅샷. |
| `scripts/dashboard.py` | 로컬 전용(Streamlit) | Pages(정적)에선 동작 불가. Zavis_Brain 시절 잔재. |
| `outputs/briefs/change-dashboard.html` | 독립 HTML | `g[[Understand-Anything/understand-anything-plugin/skills/understand/locales/en.md|en]]erate_change_dashboard.py` 산출. Pages 파이프라인과 무관. |

> 이 레거시 표면들을 물리적으로 제거하려면 이를 재생성하는 로컬 스크립트
> (`know_grow_monitor.py`, `publish_dashboard.sh`, `sync_brain_auto.sh`)를 함께
> 수정해야 하므로, 라이브 동기화를 깨지 않기 위해 별도 작업으로 분리한다.

## 로그 파일 안내

| 파일 | 역할 |
| :--- | :--- |
| `change-log.md` | **정본** — 해석된 변화 요약 (매일 확인) |
| `lint-log.md` | LINT 자가 점검 이력 |
| `ingest-log.md` | inbox → wiki 편입 이력 |
| `question-log.md` | QUERY 질문-답변 이력 |
| `bridge-log.md` | Notion 동기화 이력 |
