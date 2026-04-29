# 개념: CSP Brain 시스템

> 등록일: 2026-04-14  
> 관련 프로젝트: —  
> 출처: gbrain (Garry Tan)

---

## Compiled Truth

CSP Brain은 AI 에이전트와 인간이 함께 운영하는 **공유 메모리 시스템**이다.
Git 레포지토리를 기반으로 대화 간 컨텍스트를 유지하고, 지식을 축적하며, 의사결정을 추적한다.

---

## 정의

Git 레포지토리를 장기 메모리로 활용해, 모든 대화가 다음 대화를 더 똑똑하게 만드는 AI 에이전트 운영 체계.

---

## 핵심 구성 요소

1. **Compiled Truth**: 현재 상태의 가장 정확한 요약. 새 정보 오면 섹션째 덮어씀. 빠른 컨텍스트 복원용 TL;DR.
2. **Timeline**: append-only 증거 기록. 절대 수정/삭제 금지. 모든 변화의 증거가 남음.
3. **Dream Cycle**: 매주 금요일 실행하는 주간 정리 루틴. inbox 비우기 → 상태 갱신 → weekly 파일 생성.
4. **Inbox 우선 원칙**: 분류가 애매할 때 `raw/inbox.md`에 먼저 투입. 마찰 없이 기록하는 것이 목표.

---

## 왜 중요한가

- **CSP 맥락에서의 의미**: AI 에이전트와 대화할 때 매번 컨텍스트를 처음부터 설명하지 않아도 됨. Brain이 연속성을 보장.
- **실무 적용 포인트**: 모든 프로젝트·결정·인물 정보가 한 곳에 축적되어, 에이전트가 더 정확한 조언을 할 수 있게 됨.

---

## 관련 개념

| 개념 | 관계 |
|------|------|
| RAG (Retrieval-Augmented Generation) | Brain은 구조화된 수동 RAG에 가까움 |
| GTD (Getting Things Done) | inbox 우선 원칙의 철학적 유사성 |

---

## 관련 파일

- `CLAUDE.md` — Brain 진입점
- `raw/inbox.md` — 미분류 수신함
- `weekly/` — Dream Cycle 결과물

---

## Timeline (append-only — 절대 수정/삭제 금지)

<!-- 새 항목은 항상 맨 아래에 추가. 기존 항목 수정/삭제 금지. -->

### 2026-04-14
- 개념 등록
- csp-brain 초기화와 함께 공식 정의됨
- Compiled Truth / Timeline 이중 구조 적용 형식으로 재정비
