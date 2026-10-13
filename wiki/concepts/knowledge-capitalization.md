---
title: Knowledge Capitalization (지식의 자산화)
created: 2026-04-14
updated: 2026-10-13
type: concept
status: growing
tags: [knowledge, asset, ax, capitalization]
aliases: [지식 자산화]
generated: {by: legacy-migration, at: 2026-04-29}
evidence: mixed
---

# Knowledge Capitalization (지식의 자산화)

## Compiled Truth

### 정의 [inferred]

기록된 데이터를 AI가 바로 처리할 수 있는 '원자 단위'로 나누어, 단순 백업이 아니라 추론의 재료로 만드는 과정이다. 이 문서의 핵심 비유인 **용해성(Solubility)**, 곧 지식이 얼마나 쉽게 녹아 다른 생각과 섞이는가도 같은 출처에서 왔다. 이 정의는 2026-04-29 이전 볼트(`D:\obsi\sync`)에서 옮겨 왔다. CSP가 직접 쓴 정의는 아니다(CSP 확인 2026-10-13). 그래서 AI가 정리했거나 외부 글을 요약한 것으로 보고 [inferred]로 둔다. 원 출처를 찾으면 그 출처 기준으로 다시 표시한다.

### 핵심 원칙 [inferred]

출처는 정의와 같다(CSP 작성 아님). 아래 세 원칙은 이후 이 저장소의 실제 운영(드라이브 수입 원장, Compiled Truth + Timeline)과 맞아떨어진다.

1. **Sharding**: 대용량 데이터를 시간 단위로 쪼개 에이전트의 기억 과부하를 막는다.
2. **Atomic Concepts**: 대화 속 핵심 개념을 개별 파일로 뽑아 검색 정확도를 높인다.
3. **Traceability**: 원본 기록과 추출된 개념 사이의 연결을 보존한다.

### AX 관점의 가치 [inferred]

전문가의 암묵지가 데이터로만 남으면 죽은 지식이다. '지능형 카드'로 바뀌면 신입 사원이나 AI 에이전트가 바로 꺼내 쓰는 **조직적 지능 자산**이 된다. 이는 해석이다. 조직에서 실제로 재사용된 사례로 확인된 것은 아직 없다.

### 외부 사례 [confirmed] / 해석 [inferred]

셀피쉬클럽 글(inbox/articles/셀피쉬클럽.md)은 Claude Code + Obsidian + GitHub 조합으로 팀의 지식 자산화와 자동 발행을 구현한 사례를 소개한다 [confirmed]. 이것이 csp-brain과 "같은 결론에 독립적으로 도달한 외부 검증"이라는 평가는 AI의 해석이다 [inferred].

### 확인되지 않은 주장 [unknown]

- Timeline 2026-04-14의 "114MB 대화 데이터 Sharding으로 실효성을 **증명**"이라는 표현은 자기 평가다. 무엇을 기준으로 증명했는지는 기록이 없다.
- 같은 날짜에 언급된 `scripts/brain_build.py`는 현재 저장소에 없다(2026-10-13 확인). 이력에서도 찾을 수 없다.

---

## Timeline

### 2026-04-29

- wiki 초기화와 함께 마이그레이션
- [[ax-internalization|AX Internalization]] 프로젝트의 핵심 원칙으로 설정됨

### 2026-04-14

- 114MB Conversations 데이터 Sharding 및 개념 추출을 통해 본 원칙의 실효성을 증명함
- `scripts/brain_build.py` 를 통해 지식의 무결성 관리 자동화 체계 수립

### 2026-07-02 — 셀피쉬클럽: 팀 단위 지식 자산화 사례 (INGEST, Issue #13)

- Claude Code + Obsidian + GitHub 조합으로 팀의 지식 자산화·문서 동기화·자동 발행을 구현한 커뮤니티 사례. 개인의 [[vibe-coding]] 흐름이 팀 협업으로 확장될 때 옵시디언(마크다운+Git)이 최적 기반이라는 논지 — csp-brain 아키텍처와 동일한 결론에 독립적으로 도달한 외부 검증 사례.

### 2026-10-13 — 인식 상태 표시 시범 적용

- Compiled Truth를 출처별로 나눴다. 내용은 삭제하지 않았다.
- 정의·원칙은 이전 볼트에서 이관됐으나 작성 주체가 남아 있지 않아 [unknown]으로 두었다(근거: `git log` 첫 커밋 "Migrate legacy knowledge from D:\obsi\sync").
- 셀피쉬클럽 사례 자체는 원문 확인 [confirmed], "독립적 외부 검증"이라는 평가는 [inferred].
- `scripts/brain_build.py` 가 현재 저장소와 git 이력 어디에도 없음을 확인하고 [unknown]으로 적었다. 04-14 Timeline 원문은 수정하지 않았다(append-only).
- **CSP 확인 필요**: 정의와 세 원칙을 CSP가 직접 쓴 것이라면 확인해 주면 [confirmed]로 승격한다.
- CSP 확인 2026-10-13: 정의와 세 원칙은 CSP가 직접 쓴 것이 아니다. → [unknown]에서 [inferred]로 변경. 승격 규칙이 실제로 쓰인 첫 사례이며, 방향은 '확정'이 아니라 '작성 주체 배제'였다.
