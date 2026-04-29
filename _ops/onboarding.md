---
title: CSP Brain Onboarding
created: 2026-04-29
type: guide
tags: [onboarding, guide, getting-started]
---

# CSP Brain Onboarding

> 새로운 멤버 (인간 또는 AI) 가 csp-brain 에서 작업을 시작하기 위한 가이드

---

## 5 분 컷 이해

### 1 분: CLAUDE.md 읽기

[`CLAUDE.md`](../CLAUDE.md) 는 csp-brain 의 진입점입니다.

- **누구인가**: CSP 는 17 년차 HR 전문가, Vibe Coder
- **아키텍처**: Working Brain (Obsidian) + Archive Brain (Notion)
- **폴더 구조**: inbox/, wiki/, projects/, outputs/
- **핵심 규칙**: Compiled Truth + Timeline 이중 구조

### 2 분: wiki/concepts/_index.md 스캔

[`wiki/concepts/_index.md`](../wiki/concepts/_index.md) 에서 핵심 개념을 파악합니다:

- [[Self-Determination Theory (자기결정이론)]] — 자율성, 유능감, 관계성
- [[Leader-Member Exchange (LMX)]] — 리더 - 구성원 관계
- [[Vibe Coding]] — AI 와 함께하는 흐름 코딩
- [[AX Internalization]] — AI 내재화 3 단계
- [[Knowledge Capitalization]] — 지식의 원자화

### 2 분: projects/ README.md 확인

각 프로젝트의 `Compiled Truth` 를 읽어 현재 상태를 파악합니다:

```
projects/
├── ax-internalization/README.md
├── escon/README.md
├── ex-intelligence/README.md
├── lds-360/README.md
├── llm-knowledge-base/README.md
└── pulse-check/README.md
```

---

## 첫 작업 시작하기

### 기본 명령어

| 명령어 | 설명 | 예시 |
|:---|:---|:---|
| `ingest` | inbox/ 정리 → wiki/ 통합 | `ingest 해줘` |
| `query` | 위키 기반 질문 응답 | `LMX 이론이 뭐야?` |
| `lint` | 위키 자가 점검 | `lint 해줘` |
| `digest` | 주간 다이제스트 생성 | `이번 주 digest` |
| `generate` | 콘텐츠 자동 생성 | `generate linkedin` |
| `harness` | Harness 구조 진단 | `harness-audit 해줘` |

### 작업 흐름 예시

#### 1. 자료 수집 후 정리

```
사용자: "inbox 에 새 자료 추가했어"
→ AI: ingest 프로토콜 실행
→ 결과: wiki/ 에 통합, inbox/ 초기화
```

#### 2. 질문 기반 학습

```
사용자: "Vibe Coding 이 심리학적으로 어떤 근거가 있어?"
→ AI: query 프로토콜 실행
→ 결과: [[Self-Determination Theory]] 연결, 답변 생성
```

#### 3. 주간 정리

```
사용자: "이번 주 정리해줘" (매주 금요일)
→ AI: Dream Cycle 실행
→ 결과: weekly/ 생성, projects/ 갱신, inbox/ 정리
```

---

## 폴더별读写 규칙

| 폴더 | 인간 (CSP) | AI (Claude) | 설명 |
|:---|:---:|:---:|:---|
| `inbox/` | ✅ 던지기 | ✅ 읽기 + 정리 | 미가공 자료 |
| `wiki/` | ❌ | ✅ 생성/수정 | 정리된 지식 |
| `projects/` | ✅ Timeline | ✅ Compiled Truth | 프로젝트 기록 |
| `outputs/` | ✅ 읽기 | ✅ 생성 | 산출물 |
| `skills/` | ✅ 요청 | ✅ 생성 | 작업 패턴 |
| `analysis/` | ✅ 읽기 | ✅ 생성 | 분석 리포트 |
| `sharing/` | ✅ 검토 | ✅ 생성 | 공개용 콘텐츠 |

---

## Git 워크플로우

### 커밋 규칙

```bash
# 작업 후 항상 커밋
git add -A
git commit -m "무엇을 + 왜"
git push
```

### 커밋 메시지 예시

```
✅ 좋은 예:
"Add backlink connections to reduce isolated documents
- concepts/ax-internalization: link to Knowledge Capitalization, Vibe Coding
- people/csp: link to SDT, LMX, EX Intelligence"

❌ 나쁜 예:
"수정사항 커밋"
"update"
```

---

## 문제 해결

### "어디서부터 시작할지 모르겠어요"

1. `ingest` 실행 — inbox/ 부터 정리
2. `lint` 실행 — 현재 위키 상태 진단
3. `query "지금 뭐부터 해야 해?"` — AI 에게 물어보기

### "문서가 너무 많아요"

1. `wiki/concepts/_index.md` — 개념 지도
2. `wiki/skills/_index.md` — 스킬 목록
3. `analysis/` — 분석 리포트 (요약본)

### "백링크가 뭐예요?"

`[[문서명]]` 형식의 링크입니다. Obsidian 에서 자동으로 그래프를 생성합니다.

예시:
```markdown
[[Self-Determination Theory]] — 이 개념을 참조
[[Vibe Coding]] — 이 실천 방식과 연결
```

---

## 다음 단계

### Level 1: 기본 사용자 (1 주)
- [ ] ingest 실행
- [ ] query 로 질문하기
- [ ] git push 까지 완료

### Level 2: 숙련 사용자 (1 개월)
- [ ] digest 주간 실행
- [ ] generate 로 콘텐츠 생성
- [ ] wiki/ 문서 추가

### Level 3: 기여자 (3 개월)
- [ ] 스킬 추가
- [ ] 프로젝트 README 갱신
- [ ] harness-audit 월간 실행

---

## 질문 템플릿

```
query [질문]

관련 문서: [알고 있는 문서명]
목적: [무엇을 하려는가]
```

예시:
```
query LMX 이론이 ESCON 프로젝트에 어떻게 적용되나요?

관련 문서: [[Leader-Member Exchange]], [[ESCON]]
목적: 리더십 개발 모듈 설계
```

---

*최종 수정: 2026-04-29 | 버전: 1.0*
