---
type: Note
---

status: Active

# 🛰️ CSP-Brain 지능 리졸버 (Synaptic Resolver)

> "리졸버는 지식의 조직도입니다. 모든 것을 알 필요는 없습니다. 누구에게 물어봐야 할지 아는 것이 지능의 본질입니다."

## 1. 도메인별 라우팅 규칙 (Routing Rules)

| 도메인        | 핵심 키워드                   | 참조 경로 (Target Path)                         | 담당 스킬 ([[Understand-Anything/understand-anything-plugin/skills/understand-knowledge/SKILL.md | SKILL]])    |
| :------------ | :---------------------------- | :---------------------------------------------- | :----------------------------------------------------------------------------------------------- | ----------- |
| **HR 전략**   | 채용, 면접, 평가, 조직문화    | `wiki/concepts/hr-*`, `projects/oka/`           | `csp-brain`                                                                                      |
| **AI 공학**   | 에이전트, MCP, 토큰, 프롬프트 | `wiki/concepts/ai-*`, `_ops/scripts/`           | `hermes-agent`                                                                                   |
| **자기 개선** | 성찰, 대사, 진화, 맥박        | `outputs/daily-reflect/`, `[[KNOWLEDGE_PULSE.md | KNOWLEDGE_PULSE]].md`                                                                            | `navigator` |
| **투자/경제** | 분석, 레포트, 시장, 지표      | `outputs/analyses/INVESTMENT_*`                 | `investment-analyst`                                                                             |

## 2. 임계치 관리 (Token Escalation)

- **Warning**: Context > 30,000 tokens 시 리졸버 가동.
- **Action**: 가장 오래된 L4(산출물) 맥락부터 제거하고 L1([[SOUL.md|SOUL]])과 L3(타임라인)만 유지.

## 3. 파일링 컨벤션 (Filing as Logic)

- `_ops/`: 시스템 운영 및 리졸버 로직 (Internal Process)
- `wiki/`: 정제된 지식 원자 (Long-term Memory)
- `projects/`: 현재 실행 중인 맥락 (Working Memory)
- `outputs/`: 완료된 산출물 (Archived Wisdom)

---

_Last Updated: 2026-05-30 by Hermes Resolver_

## 4. Intelligent Effort Calibration (V4.8+)

- **Low Effort**: 단순 검색, 파일 존재 확인 (`ls`), 간단한 요약.
- **High Effort**: 코드 작성, 심리 지표 분석, 복잡한 리졸버 설계.
- **X-High Effort + Adaptive Thinking**: 신규 시스템 아키텍처 설계, 대규모 데이터 대사 작용 수행.
