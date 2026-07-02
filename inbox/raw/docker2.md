---
type: daily
processed: true
processed_date: 2026-07-02
processed_note: "hermes-agent 도커 재시작 메모 — 운영 스크랩(보류)"
---

# docker_260502

(base) dkmac@MacBook-Air-5 dev % cd /Users/dkmac/.hermes/hermes-agent

(base) dkmac@MacBook-Air-5 hermes-agent % docker compose up -d  

## 5. 유지보수 및 문제 해결

### 5.1 시스템 재시작

설정을 변경했거나 에이전트가 응답하지 않을 때는 도커 컴포즈를 통해 재시작할 수 있습니다.

- **명령어**: `docker compose restart` (해당 디렉토리 내에서)4

*
