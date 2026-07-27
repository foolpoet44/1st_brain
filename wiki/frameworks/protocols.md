---
title: CSP-Brain Protocols
created: 2026-04-29
updated: 2026-04-29
type: framework
status: growing
tags: [protocol, workflow, automation]
aliases: [프로토콜]
---

# CSP-Brain Protocols

## Compiled Truth

csp-brain 운영을 위한 6 가지 프로토콜 + 검증 체계.

| #   | Name     | Trigger    | What it does        |
| :-- | :------- | :--------- | :------------------ |
| 1   | INGEST   | `ingest`   | inbox/ → wiki/ 통합 |
| 2   | QUERY    | 질문       | 위키 기반 답변      |
| 3   | LINT     | `lint`     | 위키 자가 점검      |
| 4   | DIGEST   | `digest`   | 주간 다이제스트     |
| 5   | BRIDGE   | `sync`     | Notion 양방향 연동  |
| 6   | GENERATE | `generate` | 콘텐츠 자동 생성    |
| 7   | HARNESS  | `harness`  | Harness 구조 진단   |

### LINT 프로토콜 (검증 체크리스트)

| 항목                    | 기준                                  | 조치                       |
| :---------------------- | :------------------------------------ | :------------------------- |
| **백링크 0 개 문서**    | 고립 문서 감지                        | 관련 문서에 링크 추가 제안 |
| **frontmatter 누락**    | title, created, updated, type, status | 필수 필드 보강             |
| **Compiled Truth 갱신** | 6 주 이상 미갱신                      | 갱신 필요 플래그           |
| **스킬 동작 검증**      | [[Understand-Anything/understand-anything-plugin/skills/understand-knowledge/SKILL.md|SKILL]]s/ 문서가 실제 사용 가능한가?    | 동작 테스트                |

자세한 것은 [[[[CLAUDE.md|CLAUDE]].md]] 참조.

---

## Timeline

### 2026-04-29

- wiki 초기화와 함께 등록
- 각 프로토콜은 별도 문서로 확장 예정
