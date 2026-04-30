---
title: Change Log
created: 2026-04-30
updated: 2026-04-30
type: ops-log
status: active
tags: [ops, change-log, visibility]
---

# Change Log

이 파일은 CSP-Brain의 통합 변경 관제판입니다.

기능별 로그는 `ingest-log.md`, `lint-log.md`, `question-log.md`, `bridge-log.md`에 남기되, 사용자가 매일 확인해야 하는 핵심 변화는 이곳에 요약합니다.

## 기록 원칙

각 변경은 아래 네 가지 질문에 답해야 합니다.

- 무엇이 바뀌었나
- 왜 중요한가
- 어디에 영향이 있나
- 다음에 무엇을 확인해야 하나

---

## 2026-04-30

### 변경 가시성 개선 체계 도입

- 무엇이 바뀌었나: 변경 해석을 위한 통합 로그, status 브리핑, weekly digest 생성 기준을 정비했다.
- 왜 중요한가: 기존 구조는 Git과 manifest에는 변화가 남았지만, 사용자가 바로 이해할 수 있는 변화 요약층이 약했다.
- 영향 범위: `CLAUDE.md`, `scripts/status.sh`, `scripts/generate_weekly.py`, `templates/daily-note.md`, `templates/weekly-digest.md`, `.obsidian/daily-notes.json`.
- 다음 확인: 앞으로 ingest, digest, generate, project/wiki 수정 후 이 파일에 핵심 변경을 남기는지 확인한다.

### 2026-W18 주간 변화 다이제스트 생성

- 무엇이 바뀌었나: `scripts/generate_weekly.py --date 2026-04-30` 기준으로 `outputs/weekly/2026-W18.md`를 생성하고 weekly index에 등록했다.
- 왜 중요한가: 사용자가 이번 주 변경 흐름을 파일 목록이 아니라 해석된 브리핑으로 확인할 수 있게 되었다.
- 영향 범위: `outputs/weekly/2026-W18.md`, `outputs/weekly/_index.md`.
- 다음 확인: W18 다이제스트의 대량 변경 항목 중 지식 승격이 필요한 것과 단순 archive 변경을 구분한다.

### 오늘의 변화 브리핑 작성

- 무엇이 바뀌었나: `outputs/briefs/2026-04-30-change-briefing.md`에 오늘의 변경 흐름과 주의 항목을 정리했다.
- 왜 중요한가: status 출력과 weekly digest를 사용자가 바로 읽을 수 있는 일일 해석 문서로 압축했다.
- 영향 범위: `outputs/briefs/2026-04-30-change-briefing.md`, `_ops/change-log.md`.
- 다음 확인: daily 브리핑을 매일 누적할지, weekly digest와 통합할지 운영 리듬을 정한다.

### Change Dashboard 생성기 추가

- 무엇이 바뀌었나: `scripts/generate_change_dashboard.py`를 추가해 change-log, status 정보, weekly digest, daily briefing을 `outputs/briefs/change-dashboard.html` 한 화면으로 모으게 했다.
- 왜 중요한가: 사용자가 여러 Markdown과 Git 출력을 오가지 않고 오늘 봐야 할 변화만 한눈에 확인할 수 있다.
- 영향 범위: `scripts/generate_change_dashboard.py`, `outputs/briefs/change-dashboard.html`.
- 다음 확인: 대시보드가 매일 브리핑 생성 후 자동 갱신되는 루틴이 필요한지 판단한다.
