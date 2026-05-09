---
title: Claude code plugin 기능 및 사용법
date: 2025-12-01
time: 00:24
uuid: 7abbe0c9-cb87-4ad9-b89c-e4f92abf90be
type: conversation
tags: [archive, conversation]
---

# Claude code plugin 기능 및 사용법

**날짜**: 2025-12-01 00:24

---

## Human (Message 1)

claude code plugin의 기능과 사용방법

## Claude (Message 2)

사용자가 Claude Code 플러그인의 기능과 사용방법에 대해 물어보고 있습니다. 제 지식 기준일은 2025년 1월 말이고, Claude Code는 명령줄 도구(command line tool)로서 개발자들이 터미널에서 직접 Claude에게 코딩 작업을 위임할 수 있게 해주는 도구입니다.

하지만 제품 정보가 변경되었을 수 있으므로, 최신 정보를 확인하기 위해 Anthropic의 공식 문서를 검색해야 합니다. 특히 사용방법이나 구체적인 기능에 대해서는 웹 검색을 통해 최신 정보를 제공하는 것이 좋겠습니다.Claude Code에 대한 최신 정보를 찾아보겠습니다.

```
This block is not supported on your current device yet.
```

좋습니다. Claude Code 플러그인에 대한 충분한 정보를 얻었습니다. 이제 사용자에게 명확하고 체계적으로 설명할 수 있습니다. 주요 내용은:

1. Claude Code 플러그인이란?
2. 주요 기능
3. 설치 및 사용 방법
4. 플러그인 마켓플레이스
5. 플러그인의 구성 요소

사용자가 한국어로 질문했으므로 한국어로 답변하겠습니다.# Claude Code 플러그인 소개

Claude Code 플러그인은 슬래시 커맨드, 에이전트, MCP 서버, 훅을 하나의 명령어로 설치할 수 있는 커스텀 컬렉션입니다. 2025년 10월에 공개 베타로 출시되었습니다.

## 주요 기능

플러그인은 다음 4가지 요소를 포함할 수 있습니다:

1. **슬래시 커맨드(Slash Commands)**: 자주 사용하는 작업을 위한 커스텀 단축키
2. **서브에이전트(Subagents)**: 특정 개발 작업을 위한 전문 에이전트
3. **MCP 서버**: Model Context Protocol을 통해 도구 및 데이터 소스에 연결
4. **훅(Hooks)**: Claude Code의 워크플로우 주요 지점에서 동작을 커스터마이징

## 설치 및 사용 방법

### 기본 설치

```bash
# 플러그인 마켓플레이스 추가
/plugin marketplace add user-or-org/repo-name

# 플러그인 설치
/plugin install plugin-name@marketplace-name
```

### 공식 마켓플레이스 사용 예시

```bash
# Anthropic 공식 마켓플레이스 추가
/plugin marketplace add anthropics/claude-code

# 특정 플러그인 설치
/plugin install frontend-design@claude-code
```

### 플러그인 관리

- `/plugin` - 플러그인 메뉴 열기
- 플러그인 브라우징, 설치, 관리 가능
- 설치 후 Claude Code 재시작 필요

## 주요 활용 사례

플러그인의 일반적인 용도는 다음과 같습니다: 엔지니어링 리더가 코드 리뷰나 테스팅 워크플로우를 위한 특정 훅을 실행하도록 하여 팀 전체의 일관성을 유지하고, 오픈소스 메인테이너가 개발자들이 패키지를 올바르게 사용할 수 있도록 돕는 슬래시 커맨드를 제공하며, 개발자들이 디버깅 설정, 배포 파이프라인, 테스팅 하네스와 같은 생산성 향상 워크플로우를 쉽게 공유할 수 있습니다.

## 인기 플러그인 예시

1. **DevOps 자동화** - 배포 및 인프라 관리
2. **문서 생성** - 자동 문서화 도구
3. **코드 리뷰** - PR 리뷰 자동화
4. **프론트엔드 개발** - UI/UX 개선 도구
5. **테스팅** - 자동화된 테스트 생성

## 팀 전체 설정

프로젝트의 `.claude/settings.json`에 플러그인 설정을 추가하면 팀원들이 자동으로 동일한 플러그인을 사용할 수 있습니다.

더 자세한 정보는 [Claude Code 공식 문서](https://code.claude.com/docs/en/plugins)에서 확인하실 수 있습니다.

---

_Archived from: `7abbe0c9-cb87-4ad9-b89c-e4f92abf90be.json`_
