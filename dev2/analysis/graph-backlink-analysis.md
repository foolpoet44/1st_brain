---
title: Graph Backlink Analysis Report
created: 2026-04-29
type: analysis
tags: [graph, backlink, analysis, knowledge-graph]
---

# Graph Backlink Analysis Report

## 📊 지식 그래프 현황

### 전체 통계

| 지표                   | 값          |
| :--------------------- | :---------- |
| **총 문서 수**         | 24 개       |
| **백링크 사용 문서**   | 14 개 (58%) |
| **백링크 0 개 (고립)** | 10 개 (42%) |
| **총 백링크 연결**     | 19 개       |

---

## 🔍 문서별 백링크 분석

### 백링크가 있는 문서 (연결됨 ✅)

| 문서                                    | 백링크 대상                                                    | 연결 수 |
| :-------------------------------------- | :------------------------------------------------------------- | :------ |
| `concepts/vibe-coding.md`               | Self-Determination Theory, AX Internalization                  | 2       |
| `concepts/weak-signal-theory.md`        | EX Intelligence, Pulse Check                                   | 2       |
| `concepts/self-determination-theory.md` | Vibe Coding                                                    | 1       |
| `concepts/leader-member-exchange.md`    | ESCON, LDS 360                                                 | 1       |
| `concepts/knowledge-capitalization.md`  | AX Internalization                                             | 1       |
| `concepts/data-sensing.md`              | EX Intelligence                                                | 1       |
| `concepts/csp-brain-system.md`          | Obsidian, Git                                                  | 2       |
| `tools/claude-code.md`                  | Vibe Coding                                                    | 1       |
| `tools/notion.md`                       | Obsidian, BRIDGE                                               | 2       |
| `tools/obsidian.md`                     | Notion                                                         | 1       |
| `skills/dream-cycle.md`                 | CSP-Brain Protocols                                            | 1       |
| `skills/_index.md`                      | Dream Cycle, Context Restore, Memory Save, CSP-Brain Protocols | 4       |
| `people/_index.md`                      | CSP                                                            | 1       |
| `frameworks/protocols.md`               | CLAUDE.md                                                      | 1       |

### 고립 문서 (백링크 0 개 ⚠️)

| 문서                                    | 유형      | 상태   | 조치 권고                                       |
| :-------------------------------------- | :-------- | :----- | :---------------------------------------------- |
| `concepts/ax-internalization.md`        | concept   | seed   | AX Internalization 를 참조하는 문서에 링크 추가 |
| `concepts/_index.md`                    | index     | mature | 개념 문서들에서 역참조 추가                     |
| `people/csp.md`                         | people    | seed   | 프로젝트 문서에서 CSP 언급 시 링크              |
| `projects/_index.md`                    | index     | seed   | -                                               |
| `decisions/_index.md`                   | index     | seed   | -                                               |
| `signals/_index.md`                     | index     | seed   | -                                               |
| `frameworks/compiled-truth-timeline.md` | framework | seed   | protocols.md 와 연결                            |
| `frameworks/_index.md`                  | index     | seed   | -                                               |
| `tools/_index.md`                       | index     | seed   | -                                               |
| `skills/context-restore.md`             | skills    | seed   | dream-cycle.md 와 상호 연결                     |
| `skills/memory-save.md`                 | skills    | seed   | dream-cycle.md 와 상호 연결                     |

---

## 🕸️ 지식 그래프 구조

### 핵심 허브 문서 (연결 3 개 이상)

```
skills/_index.md (4 개의 연결)
  ├── Dream Cycle
  ├── Context Restore
  ├── Memory Save
  └── CSP-Brain Protocols
```

### 연결 군집 (Clusters)

#### Cluster 1: HR/조직심리학

```
Self-Determination Theory ←→ Vibe Coding
                                    ↑
                              Claude Code (도구)
```

#### Cluster 2: 데이터/감지

```
Weak Signal Theory → EX Intelligence
                     Pulse Check
Data Sensing ─────→ EX Intelligence
```

#### Cluster 3: 시스템/도구

```
Obsidian ←→ Notion (BRIDGE 프로토콜)
   ↑
Git ─┘
```

#### Cluster 4: 프로토콜

```
CSP-Brain Protocols ← skills/_index.md
                           ↑
                    Dream Cycle
```

---

## 🎯 Graph RAG 아키텍처 매핑

### 엔티티 (노드)

| 엔티티 유형   | 문서 폴더     | 예시                          |
| :------------ | :------------ | :---------------------------- |
| **Concept**   | `concepts/`   | SDT, LMX, Vibe Coding         |
| **Framework** | `frameworks/` | Protocols, Compiled Truth     |
| **Tool**      | `tools/`      | Obsidian, Notion, Claude Code |
| **Skill**     | `skills/`     | Dream Cycle, Context Restore  |
| **People**    | `people/`     | CSP                           |
| **Project**   | `projects/`   | EX Intelligence, Pulse Check  |

### 관계 (에지)

| 관계 유형      | 백링크 패턴      | 의미           |
| :------------- | :--------------- | :------------- |
| **is-a**       | `[[개념명]]`     | 하위/상위 개념 |
| **uses**       | `[[도구명]]`     | 도구 활용      |
| **implements** | `[[프로토콜명]]` | 프로토콜 구현  |
| **related-to** | `[[프로젝트명]]` | 프로젝트 연관  |
| **defined-by** | `[[이론명]]`     | 이론적 근거    |

---

## 📈 Graph RAG 추론 경로 예시

### Multi-hop Query 예시

**질문**: "CSP 의 Vibe Coding 방식은 어떤 심리학 이론에 기반하는가?"

**추론 경로**:

```
Vibe Coding
  ←→ Self-Determination Theory (자율성, 유능감)

답변: 자기결정이론 (SDT) — 자율성과 유능감 충족
```

**질문**: "조직의 약한 신호를 포착하는 시스템은 무엇인가?"

**추론 경로**:

```
Weak Signal Theory
  → EX Intelligence (필터링 알고리즘)
  → Pulse Check (감지 도구)

답변: EX Intelligence 와 Pulse Check 가 L1/L2/L3 아키텍처로 감지
```

---

## ⚠️ 개선 권고사항

### 1. 고립 문서 해소 (우선순위: 상)

다음 문서들에 백링크 2 개 이상 추가 필요:

```markdown
# concepts/ax-internalization.md 에 추가할 내용

관련 문서:

- [[Knowledge Capitalization]] — 하위 원칙
- [[Vibe Coding]] — AX 의 실천 방식
```

### 2. Index 문서 활성화 (우선순위: 중)

`_index.md` 파일들이 단순 목록을 넘어 그래프 허브 역할 하도록 개선:

```markdown
# concepts/\_index.md 개선안

## 개념 지도

### 심리학 이론

- [[Self-Determination Theory]] → [[Vibe Coding]] 과 연결
- [[Leader-Member Exchange]] → [[ESCON]], [[LDS 360]] 기반

### AI/코딩

- [[Vibe Coding]] ← [[Claude Code]] 도구 활용
```

### 3. 역참조 자동 생성 (우선순위: 중)

Obsidian 의 "Backlinks" 패널 활용 또는 수동으로:

```markdown
## 이 문서를 참조하는 문서들

- [[Vibe Coding]] 에서 SDT 를 언급
- [[Data Sensing]] 에서 EX Intelligence 언급
```

### 4. Graph View 시각화 (우선순위: 하)

Obsidian Graph View 에서:

- **노드 크기**: 백링크 수에 비례
- **색상**: 폴더별 (concepts=파랑, tools=초록, skills=주황)
- **고립 노드**: 빨간색 강조

---

## 🚀 다음 액션

1. **고립 문서 연결** — ax-internalization.md, people/csp.md 에 백링크 추가
2. **Index 문서 개선** — \_index.md 파일들에 개념 지도 추가
3. **주간 점검 루틴** — LINT 프로토콜에 "백링크 0 개 문서" 체크 추가
4. **Graph View 공유** — 지식 그래프 시각화 이미지 생성 (링크드인 공유용)

---

_분석 생성일: 2026-04-29 | 총 24 개 문서 분석_
