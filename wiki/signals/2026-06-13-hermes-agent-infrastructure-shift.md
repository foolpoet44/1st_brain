---
title: "[Weak Signal] AI Agent as an Operating Layer"
created: 2026-06-13
updated: 2026-06-13
type: signal
status: Active
date: 2026-06-13
source: "Goobong Jeong (LinkedIn)"
importance: High
tags:
  - agent-infrastructure
  - hermes-agent
  - industry-trend
---

# [Weak Signal] AI Agent as an Operating Layer

정구봉(GB Jeong)님이 링크드인을 통해 공유한 Hermes Agent에 대한 고찰은 AI 에이전트의 패러다임이 '개별 작업(IC)'에서 '운영 인프라(Infrastructure)'로 이동하고 있음을 시사합니다.

## 핵심 신호 (Signals)
1. **Curator의 중요성**: 지식의 양보다 '정제(Curation)'가 에이전트 품질의 핵심 지표가 됨.
2. **Procedural Memory**: 단순 기억이 아닌 '일하는 방식([[Understand-Anything/understand-anything-plugin/skills/understand-knowledge/SKILL.md|SKILL]]s)'의 자동 저장 및 재사용.
3. **Runtime Identity**: 프로필별로 완전히 분리된 [[SOUL.md|SOUL]]과 Runtime 환경 구축.
4. **GEPA (Evaluation Gate)**: 에이전트의 자기 객관화 부족을 해결하기 위한 외부 평가 루프.

## csp-brain에의 함의
- 우리의 `skill_manage` 도구가 단순한 자동화 스크립트 관리를 넘어, 시스템의 **절차적 기억(Procedural Memory)**으로 기능해야 함.
- 주기적인 `Curator` 활동(Stale 스킬 정리)을 스케줄링(Cron)하여 시스템 부하 및 컨텍스트 오염을 방지할 필요가 있음.

---
**관련 Atom**: [[hermes-agent-as-ai-os]]
