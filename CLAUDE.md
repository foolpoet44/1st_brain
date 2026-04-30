# CSP-Brain — Agent Operating Manual

> 이 문서는 Claude Code가 csp-brain Vault에서 작업할 때 따르는 운영 지침서입니다.
> 인간(CSP)은 이 파일을 직접 수정하지 않습니다. 에이전트가 유지보수합니다.

---

## 1. 나는 누구인가

CSP는 17년차 HR 전문가이자 Vibe Coder입니다.
SW 공학 백그라운드 없이, 심리학과 HR 경험을 코드로 변환하는 Creative Solution Provider.

### 핵심 관심 영역 (우선순위 순)
1. AX 내재화 — AI 활용도 제고, Vibe Coding 교육, 워크플로우 재설계
2. HR 자동화 & SaaS — EX Intelligence, ESCON, Pulse Check, LDS 360
3. 조직심리학 — SDT, LMX, POS, Ansoff Weak Signal Theory
4. Vibe Coding & AI Agent — Claude Code, Agent 아키텍처
5. 경제적 자유 — 한국 부동산, 채권/ETF, 한미 주식

### 커뮤니케이션 규칙
- 한국어로 응답
- 에세이형 설명 > 불렛 리스트
- 철학적/심리학적 유추 환영
- 코드 설명 시 "왜"를 반드시 포함
- 설명 없이 코드만 던지지 말 것

---

## 2. 아키텍처: 이중 뇌 모델

```
┌─────────────────────────────────────────────────────────┐
│                    CSP Knowledge System                  │
│                                                          │
│  ┌──────────────────┐         ┌──────────────────────┐  │
│  │  Working Brain    │ BRIDGE  │  Archive Brain        │  │
│  │  (Obsidian+Git)   │◄──────►│  (Notion)             │  │
│  │                   │         │                       │  │
│  │  • 작업 중 사고    │         │  • 완성된 산출물       │  │
│  │  • Claude 직접 R/W│         │  • 관계형 DB 필요한것  │  │
│  │  • 프로젝트 문맥   │         │  • Claude 대화 아카이브│  │
│  │  • 위키 지식 그래프 │         │  • Decision Log       │  │
│  │  • 주간 다이제스트  │         │  • 외부 공유 문서      │  │
│  └──────────────────┘         └──────────────────────┘  │
│           │                                              │
│           ▼                                              │
│  ┌──────────────────┐                                    │
│  │  GitHub (Private)  │                                   │
│  │  • 버전 히스토리    │                                   │
│  │  • 변경 추적       │                                   │
│  │  • 동기화 인프라    │                                   │
│  └──────────────────┘                                    │
└─────────────────────────────────────────────────────────┘
```

---

## 3. 폴더 구조와 규칙

```
csp-brain/                     ← Obsidian Vault Root = Git Repo Root
│
├── CLAUDE.md                  ← 이 파일. 에이전트 진입점.
├── README.md                  ← GitHub 레포 표지
├── .gitignore                 ← .obsidian/workspace* 등 제외
│
├── .obsidian/                 ← 옵시디언 설정 (Git 추적)
│   ├── app.json               ← 핵심 설정
│   ├── community-plugins.json ← 활성 플러그인 목록
│   └── snippets/              ← CSS 커스텀
│
├── .claude/                   ← Claude Code 규칙
│   └── rules/                 ← 원자적 규칙 파일들
│
├── inbox/                     ← 🔴 인간의 영역. 자료를 던지는 곳
│   ├── articles/              ← 웹 기사, 블로그, SNS
│   ├── papers/                ← 논문, 리서치 리포트
│   ├── notes/                 ← 회의 메모, 아이디어 스크래치
│   └── raw/                   ← 미분류
│
├── wiki/                      ← 🟢 AI의 영역. 정리된 지식
│   ├── concepts/              ← 개념 정의 (SDT, LMX, Vibe Coding 등)
│   ├── frameworks/            ← 이론·모델·방법론
│   ├── tools/                 ← 도구·플랫폼·기술 스택
│   ├── projects/              ← 프로젝트별 축적 지식
│   ├── decisions/             ← 의사결정과 근거
│   └── signals/               ← 트렌드·약한 신호·관찰
│
├── projects/                  ← 🔵 프로젝트별 Compiled Truth + Timeline
│   ├── ex-intelligence/
│   ├── pulse-check/
│   ├── escon/
│   ├── lds-360/
│   ├── llm-knowledge-base/
│   └── ax-internalization/
│
├── outputs/                   ← AI가 만든 산출물
│   ├── analyses/              ← 분석 리포트
│   ├── briefs/                ← 요약 브리프
│   ├── drafts/                ← 초안 (보고서, 에세이)
│   └── weekly/                ← 주간 다이제스트
│
├── _ops/                      ← 운영 메타데이터 (로그)
├── templates/                 ← 옵시디언/생성용 템플릿
└── scripts/                   ← 자동화 스크립트
```

### 읽기/쓰기 규칙

| 영역 | 인간(CSP) | AI(Claude) |
|:---|:---|:---|
| inbox/ | ✅ 자유롭게 던진다 | ✅ 읽기 + INGEST 처리 |
| wiki/ | ❌ 직접 수정 금지 | ✅ 생성·수정·병합 |
| projects/ | ✅ Timeline에 메모 추가 가능 | ✅ Compiled Truth 갱신 |
| outputs/ | ✅ 읽기 | ✅ 생성 |
| _ops/ | ❌ | ✅ 로그 기록 |
| CLAUDE.md | ❌ | ✅ 유지보수 |

---

## 4. 변경 가시성 원칙

CSP의 가장 큰 페인포인트는 "무엇이 어떻게 바뀌고 있는지 잘 모르겠다"는 점이다. 따라서 모든 운영은 지식 축적보다 **변경 해석 가능성**을 우선한다.

### Change Log 규칙

`_ops/change-log.md`는 사용자가 매일 확인하는 통합 변경 관제판이다. 기능별 로그는 세부 증거이고, change-log는 해석된 변화 요약이다.

다음 작업 후에는 반드시 `_ops/change-log.md`에 한 항목을 추가한다.

- `ingest`: 새 자료가 wiki/project에 편입된 경우
- `digest`: 주간 요약이 생성되거나 주요 변화가 확인된 경우
- `generate`: 외부 공유물, 보고서, 초안 등 산출물이 생성된 경우
- `wiki/`, `projects/`, `scripts/`, `CLAUDE.md`의 의미 있는 변경

각 항목은 반드시 네 질문에 답한다.

```markdown
### [변경 제목]
- 무엇이 바뀌었나:
- 왜 중요한가:
- 영향 범위:
- 다음 확인:
```

### 커밋 분리 규칙

Git은 백업 수단이 아니라 변화 이해 장치다. 의미가 다른 변경은 한 커밋에 섞지 않는다.

| 접두어 | 용도 |
|:---|:---|
| `knowledge:` | wiki/concepts/frameworks 등 지식 내용 변경 |
| `project:` | projects/의 상태, Timeline, Compiled Truth 변경 |
| `ops:` | scripts, templates, CLAUDE.md, _ops 등 운영 체계 변경 |
| `archive:` | raw, manifest, 변환 산출물 등 대량 원자료 변경 |
| `content:` | sharing, outputs/drafts, 외부 공유 초안 변경 |

대형 자동 산출물(`manifest.json`, 변환된 archive 등)은 지식 해석 변경과 같은 커밋에 섞지 않는다.

---

## 5. 문서 구조: Compiled Truth + Timeline

모든 프로젝트와 위키 문서는 이 이중 구조를 따릅니다.

```markdown
# [문서 제목]

## Compiled Truth
현재 알고 있는 최선의 요약. 새 정보가 오면 이 섹션만 덮어쓴다.

---

## Timeline
append-only 증거 기록. 절대 삭제/수정 금지.

### YYYY-MM-DD
- 오늘 배운 것, 결정한 것, 변화한 것
```

### Frontmatter 표준

```yaml
---
title: 문서 제목
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: concept | framework | tool | project | decision | signal
status: seed | growing | mature | archived
tags: [관련태그]
aliases: [대체명칭]
---
```

### 백링크 규칙
- 다른 wiki 문서 개념이 등장하면 반드시 `[[문서명]]`으로 링크
- 한 문서에서 최소 2개 이상의 백링크 (고립 방지)
- 백링크 0인 문서는 LINT에서 경고 대상

---

## 6. 프로토콜

### Protocol 1: INGEST — 자료 수집 처리

**트리거**: `ingest`, `수집`, `정리해줘`

```
1. inbox/ 전체 스캔
2. 각 파일 판별: 언어, 유형, 핵심 주제, 기존 wiki 관련성
3. 처리:
   a) 기존 wiki 관련 → 해당 문서에 병합
   b) 새로운 주제 → wiki/ 적절한 폴더에 새 문서 생성
   c) 여러 주제 → 분산 추가 + 교차 링크
4. 처리 완료된 inbox 파일에 frontmatter 추가: processed: true
5. _ops/ingest-log.md에 기록
6. 의미 있는 편입이면 _ops/change-log.md에 변경 요약 기록
```

### Protocol 2: QUERY — 지식 질문 응답

**트리거**: 질문 형태의 입력

```
1. wiki/ 전체를 참조하여 답변 구성
2. 답변에 사용한 wiki 문서를 [[링크]]로 명시
3. 답변 과정에서 발견한 빈틈이 있으면 보고
4. 답변 결과가 새로운 인사이트를 담고 있으면 wiki에 편입 제안
5. _ops/question-log.md에 질문-답변 기록
6. 관점이 바뀌는 답변이면 _ops/change-log.md에 변경 요약 기록
```

### Protocol 3: LINT — 자가 점검

**트리거**: `lint`, `점검`, `검증`

```
1. 백링크 0인 고립 문서 찾기
2. Compiled Truth가 6주 이상 갱신 안 된 문서 찾기
3. 모순되는 정보가 있는 문서 쌍 찾기
4. frontmatter 누락/불일치 찾기
5. 결과를 _ops/lint-log.md에 기록
6. 수정 제안을 CSP에게 보고
```

### Protocol 4: DIGEST — 주간 다이제스트

**트리거**: `digest`, `다이제스트`, 매주 금요일 Dream Cycle

```
1. 이번 주 변경된 wiki 문서 목록
2. 새로 생성된 문서와 핵심 내용
3. 가장 활발한 프로젝트
4. 발견된 교차 연결 (의외의 관계)
5. 다음 주 추천 탐구 주제
6. outputs/weekly/YYYY-WXX.md에 저장
7. _ops/change-log.md에 이번 주 핵심 변화 기록
```

### Protocol 5: BRIDGE — 노션 연동 (하이브리드)

**트리거**: `sync`, `노션 연동`, `bridge`

```
방향 1: Obsidian → Notion (내보내기)
  - outputs/의 완성된 산출물을 Notion 아카이브에 저장
  - 대상 DB: 💬 Claude 대화 아카이브 (d012343e-b2a2-461e-944b-6f166e91d8e9)
  - 메타데이터 자동 생성: 제목, 주제, 태그, 중요도, 상태

방향 2: Notion → Obsidian (가져오기)
  - Notion에서 관련 페이지 검색 → inbox/에 마크다운 저장
  - 이후 INGEST 프로토콜로 wiki에 통합

기록: _ops/bridge-log.md에 동기화 이력
```

### Protocol 6: GENERATE — 콘텐츠 자동 생성 ⭐ NEW

**트리거**: `generate`, `콘텐츠`, `초안 만들어줘`

AAA팀의 핵심 패턴을 CSP에 적용한 프로토콜.

```
1. projects/와 wiki/의 최근 변경사항을 스캔
2. 요청된 콘텐츠 유형에 따라 생성:
   a) weekly-report → 주간업무보고서 (weekly-report 스킬 사용)
   b) linkedin → 링크드인 포스트 초안
   c) essay → Working Backwards 에세이 초안
   d) slide → 경영진 보고 슬라이드 (mckinsey-slide-generator 스킬 사용)
   e) brief → 1페이지 요약 브리프
3. outputs/drafts/에 저장
4. _ops/change-log.md에 산출물 생성 이유와 영향 기록
5. CSP 검토 후 최종 확정
```

---

## 7. Dream Cycle (매주 금요일)

```
1. INGEST  — inbox/ 정리 → wiki/ 통합
2. LINT    — 위키 전체 점검
3. DIGEST  — 주간 다이제스트 생성
4. BRIDGE  — 주요 산출물 Notion 동기화
5. Git     — commit + push
```

---

## 8. 빠른 명령어

| 명령어 | 프로토콜 | 설명 |
|:---|:---|:---|
| `ingest` / `수집` | INGEST | inbox/ → wiki/ 통합 |
| `query` / 질문 형태 | QUERY | 위키 기반 질문 응답 |
| `lint` / `점검` | LINT | 위키 자가 점검 |
| `digest` / `다이제스트` | DIGEST | 주간 지식 변화 요약 |
| `sync` / `bridge` | BRIDGE | Notion 양방향 연동 |
| `generate [유형]` | GENERATE | 콘텐츠 자동 생성 |
| `status` | — | 최근 변화 브리핑 + 위키 현황 통계 |
| `dream` | Dream Cycle | 전체 주간 루틴 실행 |

---

## 9. 성장 단계

| 단계 | wiki 문서 수 | 가능해지는 것 |
|:---|:---|:---|
| 씨앗 | 5~15개 | 개별 개념 정리, 단순 검색 |
| 새싹 | 15~40개 | 개념 간 연결 발견, 비교 분석 |
| 성장 | 40~80개 | 교차 도메인 인사이트, 트렌드 추적 |
| 숲 | 80개+ | 자기 진화하는 지식 생태계 |

---

*v2.0 — 2026-04-29 옵시디언 + GitHub 하이브리드 전환*
*Based on: Karpathy LLM KB + gbrain Compiled Truth + SELFISH AAA Pipeline*
*Architecture: Working Brain (Obsidian) + Archive Brain (Notion)*
