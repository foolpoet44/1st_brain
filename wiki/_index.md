---
title: CSP Knowledge Bundle
type: bundle-index
bundle_version: "1.0"
owner: foolpoet44@gmail.com
created: 2026-06-29
updated: 2026-06-29
status: growing
tags: [bundle, wiki, okf, index]
---

# CSP Working Brain — Knowledge Bundle

Karpathy의 LLM Wiki 개념과 Google OKF(Open Knowledge Format)를 기반으로 구축된 CSP의 살아있는 지식 번들. 에이전트(Claude)가 유지보수하고, CSP가 소유한다.

> "Obsidian은 IDE, LLM은 프로그래머, 위키는 코드베이스" — Andrej Karpathy

## 번들 구조

| 폴더 | 역할 | 문서 수 |
|------|------|---------|
| [[concepts/_index\|concepts/]] | 핵심 개념 정의 (SDT, LMX, Vibe Coding 등) | ~45개 |
| [[frameworks/_index\|frameworks/]] | 이론·모델·방법론 | ~6개 |
| [[tools/_index\|tools/]] | 도구·플랫폼·기술 스택 | ~6개 |
| [[signals/_index\|signals/]] | 트렌드·약한 신호·관찰 | ~18개 |
| [[decisions/_index\|decisions/]] | 의사결정과 근거 | ~2개 |
| [[skills/_index\|skills/]] | 에이전트 스킬 패턴 | ~3개 |
| [[people/_index\|people/]] | 인물 프로필 | ~3개 |
| protocols/ | 검증·운영 프로토콜 | ~1개 |

## 에이전트 탐색 규칙

1. 질문을 받으면 이 파일을 먼저 읽어 관련 폴더를 특정한다
2. 해당 폴더의 `_index.md`를 읽어 관련 문서를 좁힌다
3. 필요한 파일만 열어 읽는다 — 나머지 폴더는 건너뛴다

## 변경 로그

→ `/_ops/change-log.md` 참조

## 관련 문서

- [[csp-brain-system|CSP Brain System]] — 이 번들의 설계 철학
- [[open-knowledge-format|Open Knowledge Format (OKF)]] — Google 공식 표준화 개념
