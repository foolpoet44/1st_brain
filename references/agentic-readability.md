---
type: Note
status: Active
tags: [protocol, documentation, agent-friendly]
---

# Ag[[Understand-Anything/understand-anything-plugin/skills/understand/locales/en.md|en]]tic Readability Guidelines (에이전틱 가독성 가이드라인)

에이전트가 문서를 읽고 즉시 '수행 가능한 스킬'로 전환할 수 있도록 돕는 작성 원칙입니다.

## 1. 명시적 가이드 (Explicit Guardrails)

- "함부로 삭제하지 말 것" 대신 "변수 X는 레거시 시스템 호환성을 위해 유지해야 함"과 같이 **'이유'**를 명시하세요.
- 에이전트는 맥락이 부족할 때 환각(Hallucination)을 일으킵니다.

## 2. 구조적 앵커 (St[[Understand-Anything/understand-anything-plugin/skills/understand/locales/ru.md|ru]]ctural Anchors)

- H1(Title), H2(Section), [[Understand-Anything/understand-anything-plugin/skills/understand/languages/yaml.md|yaml]] Frontmatter를 통해 위계를 명확히 하세요.
- 에이전트는 문서의 '형태'를 보고 중요도를 판단합니다.

## 3. 실행 가능한 지식 (Actionable Knowledge)

- "최선을 다해보고 공유하세요" 대신 "작업 완료 후 `_ops/change-log.md`에 변경 사항을 기록하세요"와 같이 **'도구(Tool)'**나 **'경로(Path)'**를 구체화하세요.
