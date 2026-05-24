# csp-brain 🧠

> Working Brain — CSP의 옵시디언 기반 지식 운영 시스템

## Architecture

**이중 뇌 모델**: 작업뇌(Obsidian + Git) ↔ 아카이브뇌(Notion)

- **Working Brain**: 이 레포. Claude Code가 직접 읽고 쓰는 지식 베이스
- **Archive Brain**: Notion 세컨브레인. 완성된 산출물과 관계형 데이터 저장소

## Structure

```
inbox/      → 인간이 자료를 던지는 곳
wiki/       → AI가 정리한 지식 위키 (6 categories)
projects/   → 프로젝트별 Compiled Truth + Timeline
outputs/    → 분석·콘텐츠·다이제스트 산출물
```

## Protocols

| #   | Name     | Trigger    | What it does        |
| :-- | :------- | :--------- | :------------------ |
| 1   | INGEST   | `ingest`   | inbox/ → wiki/ 통합 |
| 2   | QUERY    | 질문       | 위키 기반 답변      |
| 3   | LINT     | `lint`     | 위키 자가 점검      |
| 4   | DIGEST   | `digest`   | 주간 다이제스트     |
| 5   | BRIDGE   | `sync`     | Notion 양방향 연동  |
| 6   | GENERATE | `generate` | 콘텐츠 자동 생성    |

## Library (Knowledge Index)

- [[wiki/concepts/_index|개념 (Concepts)]] — HR, AI, 조직심리학 핵심 개념
- [[wiki/tools/_index|도구 (Tools)]] — 기술 스택 및 플랫폼
- [[wiki/frameworks/_index|프레임워크 (Frameworks)]] — 운영 이론 및 모델
- [[wiki/skills/_index|에이전트 기술 (Skills)]] — 시스템 운영 자동화 스킬
- [[wiki/decisions/_index|의사결정 (Decisions)]] — 시스템 아키텍처 및 정책 변경 이력

- [[Concepts|_index (개념 사전)]] — HR, AI, 조직심리학 핵심 개념
- [[Tools|_index (도구 상자)]] — 활용 중인 기술 스택 및 플랫폼

## Quick Start

```bash
# Claude Code에서
cd ~/csp-brain
claude

# 첫 세션
> CLAUDE.md를 읽고, 현재 wiki/ 상태를 파악한 뒤 status를 보고해줘
```

---

_v2.0 — Obsidian + GitHub Hybrid | Notion Archive_
