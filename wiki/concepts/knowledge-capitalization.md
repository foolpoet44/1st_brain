---
title: Knowledge Capitalization (지식의 자산화)
created: 2026-04-14
updated: 2026-07-02
type: concept
status: growing
tags: [knowledge, asset, ax, capitalization]
aliases: [지식 자산화]
---

# Knowledge Capitalization (지식의 자산화)

## Compiled Truth

기록된 데이터를 AI 가 즉각적으로 처리 가능한 '원자 단위'로 분해하고 지각화하는 과정입니다. 단순 백업과 달리, 지식의 **용해성 (Solubility)**을 높여 추론의 재료로 만드는 것을 의미합니다.

**핵심 원칙**

1. **Sharding**: 대용량 데이터를 시계열로 쪼개어 에이전트의 메모리 과부하를 방지
2. **Atomic Concepts**: 대화 속 핵심 개념을 추출하여 개별 파일로 관리함으로써 검색 정확도 향상
3. **Traceability**: 원본 로그와 추출된 개념 간의 연결 고리 보존

**AX 관점의 가치**

조직 내 전문가의 암묵지가 '데이터'로만 남으면 죽은 지식이 되지만, '지능형 카드'로 변환되면 신입 사원이나 AI 에이전트가 즉시 복제하여 사용할 수 있는 **조직적 지능 자산**이 됩니다.

---

## Timeline

### 2026-04-29

- wiki 초기화와 함께 마이그레이션
- [[AX Internalization]] 프로젝트의 핵심 원칙으로 설정됨

### 2026-04-14

- 114MB Conversations 데이터 Sharding 및 개념 추출을 통해 본 원칙의 실효성을 증명함
- `scripts/brain_build.py` 를 통해 지식의 무결성 관리 자동화 체계 수립

### 2026-07-02 — 셀피쉬클럽: 팀 단위 지식 자산화 사례 (INGEST, Issue #13)

- Claude Code + Obsidian + GitHub 조합으로 팀의 지식 자산화·문서 동기화·자동 발행을 구현한 커뮤니티 사례. 개인의 [[vibe-coding]] 흐름이 팀 협업으로 확장될 때 옵시디언(마크다운+Git)이 최적 기반이라는 논지 — csp-brain 아키텍처와 동일한 결론에 독립적으로 도달한 외부 검증 사례.
