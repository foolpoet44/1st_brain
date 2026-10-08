---
title: 사고 기록 — Hermes 동기화가 remote 없는 사본 저장소에 커밋한 기간 (2026-09-20 ~ 09-24)
created: 2026-10-08
updated: 2026-10-08
type: decision
status: archived
tags: [incident, hermes, sync, 계측]
---

# Hermes 사본 저장소 사고 (2026-09-20 ~ 09-24)

## Compiled Truth

이 폴더는 **증거 보관소**이지 살아 있는 산출물이 아니다. 여기 있는 파일은 `~/.hermes/csp-brain` 이라는, GitHub remote 가 없는 별도 git 저장소에서 가져왔다. 그 저장소는 09-20 에 생겼고 09-23 ~ 09-24 사이 커밋 5 개를 받았다.

무슨 일이 있었나. `daily-knowledge-sync` 크론 작업의 지시문은 `/Users/dkmac/csp-brain/scripts/sync_brain.sh` 를 실행하라고 했지만, Hermes 의 터미널 도구가 하드코딩된 작업 폴더 때문에 세 번 연속 실패했고, 에이전트는 `execute_code + subprocess` 로 우회했다(이 폴더의 `REFLECT_2026-09-23.md` Atom 2 가 그 기록이다). 우회한 셸의 현재 폴더가 `~/.hermes` 쪽이었기 때문에 커밋은 본 볼트가 아니라 `~/.hermes/csp-brain` 에 쌓였다. 실행 리포트는 매번 「✅ 완료 · 원격 저장소 미설정」이라고 적었다 — 완료는 사실이었고, 그 완료가 어디에도 연결되지 않았다는 것도 사실이었다.

그래서 이 폴더의 계측값을 본 볼트의 값으로 읽으면 안 된다. 여기 리포트들이 말하는 「Total Docs 7 · Links 14 · Orphan 57.1% · Health 36.9」는 **문서 7 편짜리 사본 저장소**를 잰 숫자다. 본 볼트(`wiki/` 127 편)와는 아무 관계가 없다.

왜 `outputs/` 가 아니라 여기에 두었나. 같은 이름의 파일 대부분(`REFLECT_2026-09-20/21/23`, `TELEGRAM_SUMMARY_2026-09-20/21/23`, `CONSOLIDATION_REPORT_2026-09-23`, `KNOWLEDGE_PULSE.md`, `data.json`)이 본 볼트에 이미 있고, 사본 쪽은 틀린 저장소를 잰 재작성본이다. 본 볼트 파일을 덮어쓰면 정본이 오염되고, `outputs/` 에 접미사로 나란히 두면 계기판과 INGEST 가 이것을 살아 있는 산출물로 센다. `_ops/` 는 Jekyll 발행에서 제외되는 영역이므로 증거를 보관하되 계측에는 들어가지 않는다.

들여오지 않은 것. `raw/sessions/` 의 Hermes 세션 기록 996 편(86MB)은 개인 대화 원문이라 GitHub 에 올리지 않았다. 원본은 `~/.hermes/csp-brain/raw/` 에 그대로 있다.

## 파일 목록

| 파일 | 본 볼트와의 관계 |
| :--- | :--- |
| `outputs/daily-reflect/CONSOLIDATION_REPORT_2026-09-20.md` | 사본에만 존재 |
| `outputs/daily-reflect/CONSOLIDATION_REPORT_2026-09-24.md` | 사본에만 존재 |
| `outputs/daily-reflect/TELEGRAM_SUMMARY_2026-09-24.md` | 사본에만 존재 |
| `outputs/daily-reflect/REFLECT_2026-09-23.md` | 본 볼트의 동명 파일(Claude 성찰)과 다른 Hermes 성찰 — 원인 기록(Atom 2) 포함 |
| `outputs/daily-reflect/CONSOLIDATION_REPORT_2026-09-23.md`, `TELEGRAM_SUMMARY_2026-09-23.md` | 본 볼트에 09-23 08:00 판이 있고, 이것은 같은 날 23:00 사본 판 |
| `outputs/daily-reflect/REFLECT_2026-09-20.md`, `REFLECT_2026-09-21.md`, `TELEGRAM_SUMMARY_2026-09-20.md`, `TELEGRAM_SUMMARY_2026-09-21.md` | 09-23 14:03 사본에 다시 쓰인 판 |
| `KNOWLEDGE_PULSE.md`, `data.json` | 사본 저장소를 잰 계측값 |
| `_ops/change-log.md` | 사본 저장소의 변경 기록(129 줄) |
| `scripts/archive_raw_sessions.py` | `csp-brain-raw-archiver` 작업이 쓰는 스크립트 사본 — 검토 전이라 `scripts/` 에 두지 않음 |

---

## Timeline

### 2026-10-08

- 본 볼트 분기 복구 중 발견. 사본 저장소의 비-raw 파일 14 편을 이 폴더로 옮겼다(본 볼트 파일은 하나도 덮어쓰지 않음).
- 남은 조치: `daily-knowledge-sync` 지시문에 볼트 경로와 push 확인을 고정할 것. 관련 기록은 [[change-log]] 의 2026-10-08 항목.
