---
title: "Claude Code 워크플로우 (Explore-Plan-Code-Commit)"
created: 2026-04-29
updated: 2026-04-29
type: concept
status: Active
related_to: "[[vibe-coding]]", "[[ax-internalization]]"
---

# Claude Code 워크플로우 (Explore-Plan-Code-Commit)

## 개념 재정의

워크플로우는 단순한 단축키의 조합이 아니라, AI에게 **"어떻게 일할지"**를 가르치는 합의된 매뉴얼이자 협업 방식의 디자인입니다.

## 4단계 표준 골격

1. **Explore (탐색)**: 코드베이스를 분석하고 맥락을 파악.
2. **Plan (설계)**: 작업 합의서(Plan)를 작성. (건축의 평면도 단계)
3. **Code (구현)**: 실제 로직을 수정 및 생성.
4. **Commit (확정)**: 작업 결과를 검증하고 기록.

## 핵심 도구 및 패턴

- **Plan Mode (Shift+Tab)**: 코드를 건드리기 전 계획서를 먼저 제시하는 모드. '인테리어 공사 전 도면 합의'와 같으며, 예기치 못한 사고를 방지하는 안전장치.
- **TDD (Test-Driven Development)**: Anthropic이 권장하는 가장 강력한 패턴. '실패하는 테스트'라는 명확한 검증 신호를 먼저 만든 뒤 구현에 착수.

## Vibe Coding 적용 유추

"그냥 망치 들고 벽 두드리지 마라."
Vibe Coder에게 워크플로우란 '직관'을 '신뢰할 수 있는 계획'으로 변환하는 브릿지입니다. 특히 3개 이상의 파일이 변경되는 복잡한 작업일수록 이 4단계 골격을 따르는 것이 지능의 휘발을 막는 핵심입니다.

---

_Source: 정상록(SangRok Jung) LinkedIn_
_Last Updated: {now}_
