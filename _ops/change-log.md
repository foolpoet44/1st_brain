---
title: Change Log
created: 2026-04-30
updated: 2026-05-02
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

## 2026-05-02

### Intelligence Center 진화 및 Quick Capture 시스템 도입

- 무엇이 바뀌었나: 단순 대시보드를 통합 지식 관리 허브인 'Intelligence Center'로 격상하고, 브라우저에서 즉시 메모를 작성해 `inbox/`에 저장하는 Quick Capture(단상 및 주간 Short Memo) 시스템을 구축했다.
- 왜 중요한가: 지식의 입구(Capture)와 변화의 관찰(Dashboard)을 단일 인터페이스로 통합하여 지식 순환의 속도를 높였다. 특히 Short Memo를 통해 휘발되기 쉬운 작은 생각들을 주간 단위로 아카이빙할 수 있게 되었다.
- 영향 범위: `scripts/capture_server.py`, `scripts/generate_change_dashboard.py`, `outputs/briefs/change-dashboard.html`, `inbox/short_memo/`.
- 다음 확인: 서버의 안정적인 백그라운드 실행(PM2 등 도입 고려)과 모바일 기기에서의 접속 편의성을 점검한다.

### D3.js 기반 지식 그래프 및 Obsidian 다이렉트 링크 통합

- 무엇이 바뀌었나: `wiki/` 폴더 내의 지식 연결망을 시각화하는 D3.js Force-Directed Graph를 대시보드에 내장하고, 모든 파일 리스트와 그래프 노드에 Obsidian URI(`obsidian://open`) 연동 기능을 추가했다.
- 왜 중요한가: 텍스트로만 존재하던 지식의 연결 구조를 직관적으로 파악할 수 있으며, 대시보드에서 발견한 특정 지식으로 즉시 점프하여 편집할 수 있는 워크플로우를 완성했다.
- 영향 범위: `scripts/generate_change_dashboard.py`, `outputs/briefs/change-dashboard.html`.
- 다음 확인: 그래프 노드 필터링 기능(태그별, 상태별)과 대규모 노드 발생 시 성능 최적화를 고려한다.

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

### Dream Cycle 실행

- 무엇이 바뀌었나: 현재까지의 Dream Cycle을 실행해 inbox, lint, weekly digest, change dashboard, bridge 보류 상태를 점검하고 기록했다.
- 왜 중요한가: 변경 가시성 체계가 실제 운영 루틴으로 작동하는지 첫 통합 점검을 수행했다.
- 영향 범위: `_ops/ingest-log.md`, `_ops/lint-log.md`, `_ops/bridge-log.md`, `_ops/change-log.md`, `outputs/weekly/2026-W18.md`, `outputs/briefs/change-dashboard.html`, `outputs/briefs/2026-04-30-dream-cycle.md`.
- 다음 확인: `dev/` 미추적 폴더 처리 정책과 `wiki/frameworks/compiled-truth-timeline.md` 연결 보강 여부를 결정한다.
