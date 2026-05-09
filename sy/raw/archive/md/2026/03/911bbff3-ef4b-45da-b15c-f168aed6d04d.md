---
title: Claude.md 설정 방법
date: 2026-03-18
time: 05:20
uuid: 911bbff3-ef4b-45da-b15c-f168aed6d04d
type: conversation
tags: [archive, conversation]
---

# Claude.md 설정 방법

**날짜**: 2026-03-18 05:20

---

## Human (Message 1)

claude.ai에서 claude.md를 설정한다는 건 어떤 의미이며, 어떤 방법으로 진행할 수 있나?

## Claude (Message 2)

Claude.ai에서 CLAUDE.md를 설정한다는 것의 의미와 방법에 대해 이야기해볼게요.

## 먼저, 맥락을 구분해야 합니다

"CLAUDE.md"는 원래 **Claude Code(CLI 환경)**의 개념입니다. CSP가 hr-workspace에서 구축한 4-layer 폴더 구조의 핵심 파일 — 바로 그것이죠. 하지만 claude.ai 웹 인터페이스에서 "CLAUDE.md를 설정한다"는 표현은 약간 다른 의미로 쓰입니다.

---

## claude.ai에서의 "CLAUDE.md적 역할"

claude.ai에는 공식적으로 CLAUDE.md 파일을 업로드하는 기능이 있는 건 아닙니다. 대신 동일한 철학을 구현하는 세 가지 경로가 있습니다.

**① User Preferences (지금 CSP가 사용하는 방식)**
Settings > Profile에서 설정하는 텍스트가 사실상 claude.ai의 CLAUDE.md입니다. 매 대화에 자동으로 주입되는 영구적 컨텍스트 — CSP의 self-definition, 업무 맥락, 저장 트리거 규칙이 모두 여기에 있죠. 지금 이 대화에서도 작동하고 있는 것이 바로 그것입니다.

**② Project Instructions (Project 기능)**
claude.ai의 Projects를 생성하면 각 프로젝트에 **system prompt 수준의 지침**을 설정할 수 있습니다. Claude Code의 CLAUDE.md가 프로젝트별로 다른 규칙을 가질 수 있듯이, 여기서는 "EX Intelligence 프로젝트용 Claude"와 "ESCON 프로젝트용 Claude"를 분리해서 운영할 수 있습니다.

**③ 대화 시작 시 파일 첨부**
실제 CLAUDE.md 파일을 매 대화 시작 시 첨부하는 방식입니다. 가장 원시적이지만, Claude Code 환경과 claude.ai 환경 간의 컨텍스트를 동기화하고 싶을 때 유효합니다.

---

## CSP에게 가장 유용한 설정 방법

지금 CSP의 User Preferences가 이미 상당히 정교하게 구성되어 있기 때문에, 추가로 할 수 있는 것은 **Projects 활용**입니다.

예를 들어, "EX Intelligence" 프로젝트를 만들고 그 안의 Instructions에 다음을 넣으면:

```
이 프로젝트는 LG PRI EX Intelligence 시스템 개발 전용입니다.
- 기술 스택: Supabase, PostgreSQL, LG EP SSO
- 현재 단계: April 킥오프 승인을 위한 자료 준비
- 보고서 언어: LG PRI 임원 커뮤니케이션 스타일 준수
- 과장된 표현 금지, 컴팩트한 보고서체 유지
```

이렇게 하면 해당 프로젝트 내 모든 대화가 그 맥락 위에서 시작됩니다.

---

## Claude Code의 CLAUDE.md와의 근본적 차이

|           | Claude Code CLAUDE.md        | claude.ai Projects/Preferences |
| --------- | ---------------------------- | ------------------------------ |
| 형태      | 파일 시스템의 실제 파일      | UI 설정값                      |
| 적용 범위 | 해당 디렉토리 내 세션        | 해당 프로젝트 내 대화          |
| 버전 관리 | Git으로 추적 가능            | 불가                           |
| 동적 수정 | Claude Code가 직접 수정 가능 | 수동 수정만                    |
| 계층 구조 | 루트/서브 디렉토리 계층      | 단일 레이어                    |

CSP의 Ouroboros 아키텍처처럼 Claude가 스스로 CLAUDE.md를 진화시키는 자기참조 루프는 claude.ai에서는 구현되지 않습니다. 그것이 Claude Code 환경의 결정적 강점이죠.

---

결국 claude.ai에서 "CLAUDE.md를 설정한다"는 것은, **Claude Code의 파일 기반 컨텍스트 주입을 UI 기반으로 근사하는 행위**입니다. 완전한 등가물은 아니지만, User Preferences + Projects의 조합으로 꽤 강력한 맞춤화가 가능합니다. CSP는 이미 그 절반 이상을 구현하고 있는 셈입니다.

---

_Archived from: `911bbff3-ef4b-45da-b15c-f168aed6d04d.json`_
