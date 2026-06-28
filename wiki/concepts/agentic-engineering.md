---
type: Concept
related_to: "[[vibe-coding]]", "[[execution-surface]]"
status: Active
tags: [agent, engineering, karpathy, hr-analogy]
---

# Agentic Engineering (에이전틱 엔지니어링)

> "소프트웨어의 설치는 이제 명령줄(`.sh`)이 아니라, 의미(`.md`)의 전수로 이행됩니다." — Andrej Karpathy

## 1. 개념의 본질: '지시'에서 '교육'으로

전통적인 소프트웨어 공학이 컴퓨터에게 '어떻게(How)' 행동할지 일련의 스텝을 주입하는 **'훈련(Training)'**의 영역이었다면, 에이전틱 엔지니어링은 AI에게 '무엇을(What)' 그리고 '왜(Why)' 해야 하는지를 가르치는 **'교육(Education)'**의 영역입니다.

HR 관점에서 이는 **'직무 기술서(JD)'**의 진화와 같습니다.

- **Legacy (.sh)**: "오전 9시에 A 버튼을 누르고, 결과값을 B 시트에 복사하라" (단순 오퍼레이터)
- **Agentic (.md)**: "우리 팀의 생산성 데이터를 수집하여, 인간이 판단하기 쉬운 대시보드로 요약하라" (전략적 파트너)

## 2. Karpathy의 5대 통찰과 시스템적 연결

1. **Markdown as Skill**: `.md` 파일은 단순한 문서가 아니라, 에이전트의 '장기(Organ)'가 됩니다. `csp-brain`의 `SKILL.md`가 바로 이 철학의 실현체입니다.
2. **Unstructured Workspace**: PDF와 메모는 읽기 전용 데이터가 아니라, 에이전트가 사고하고 판단하는 **'작업대(Workbench)'**입니다.
3. **Model as App**: UI나 백엔드 로직이 모델 내부로 흡수됩니다. '앱'을 깔 필요 없이 '능력'을 호출합니다.
4. **Jaggedness (들쭉날쭉한 능력)**: AI의 지능은 선형적이지 않습니다. 따라서 에이전틱 엔지니어링은 '안정적 검증(Verifiability)' 환경을 만드는 것이 핵심입니다.
5. **Logic / Actuator / Sensor**: 에이전트를 설계할 때 이 세 요소를 분리하여 설계해야 합니다.
6. **Self-Optimization (SkillOpt)**: 기술 문서는 고정된 것이 아니라, 실행 결과를 바탕으로 스스로 진화해야 합니다. ([[skillopt]])
7. **Relational Pathfinding**: 지식은 고립된 섬이 아니라 연결된 길이어야 하며, 에이전트는 결론에 도달한 '경로'를 증명해야 합니다. ([[knowledge-graph-as-map]])
8. **Knowledge Exactness**: 지식의 사슬은 앞뒤 맥락이 완벽하게 들어맞는 '최대 정합 구조'를 지향해야 합니다. ([[maximal-knowledge-exactness]])

## 3. Vibe Coder의 대응 전략

- **Text-Centricity**: 모든 자동화 로직을 인간이 읽기 쉬운 자연어로 먼저 기술합니다.
- **Metabolism Integration**: 새로운 지식이 들어오면 이를 단순히 저장하는 것이 아니라, `SKILL.md`라는 실행 가능한 형태로 '환원'시킵니다.
