---
type: Atom
status: Active
source: "Goobong Jeong (LinkedIn)"
url: https://www.linkedin.com/posts/gb-jeong_hermes-agent%EB%8A%94-ai%EB%A5%BC-%EC%9E%98-%EC%93%B0%EA%B8%B0-%EC%9C%84%ED%95%9C-%EC%9A%B4%EC%98%81%EC%B2%B4%EC%A0%9C%EC%97%90-%EA%B0%80%EA%B9%9D%EC%8A%B5%EB%8B%88%EB%8B%A4-%ED%9D%A5%EB%AF%B8%EB%A1%9C%EC%9A%B4-share-7465443762241097728-m5Pk/
tags:
  - hermes-agent
  - ai-os
  - infrastructure
  - learning-loop
  - gepa
date: 2026-06-13
---

# Hermes Agent: AI를 위한 운영체제 (Operating System for AI)

정구봉(Goobong Jeong)님은 Hermes Agent를 단순한 챗봇이 아닌, **"AI를 잘 쓰기 위한 운영체제(Operating Layer)"**로 정의합니다. 이는 세션이 종료되면 초기화되는 기존 에이전트의 한계를 극복하고, 지식이 축적되고 스스로 진화하는 인프라스트럭처로서의 에이전트 철학을 담고 있습니다.

## 1. 핵심 메커니즘: 지능의 축적과 관리

- **계층형 메모리 (Layered Memory)**: 모든 정보를 컨텍스트에 쏟아붓는 대신, `MEMORY.md`와 `USER.md`와 같은 핵심 압축 데이터, SQLite 기반의 세션 검색, 그리고 외부 Provider를 유기적으로 결합하여 사용합니다. "핵심은 모든 걸 넣는 게 아니라, 중요한 것만 작게 압축하는 것"입니다.
- **절차적 기억으로서의 스킬 (Skills as Procedural Memory)**: 스킬은 단순한 프롬프트 모음이 아닙니다. 문제 해결 과정에서의 시행착오와 성공 방정식을 '플레이북' 형태로 저장하여, 다음번에는 동일한 문제를 처음부터 다시 풀지 않도록 합니다. 에이전트가 자동으로 "일하는 방법"을 저장하는 셈입니다.
- **자동 큐레이터 (Curator)**: 에이전트가 생성한 방대한 스킬 중 불필요하거나 오래된 것(Stale)을 자동으로 식별하고 아카이브(Archive)하여 컨텍스트의 오염을 방지합니다. 제품의 품질은 '무엇을 기억하느냐'보다 '무엇을 큐레이션하느냐'에서 결정됩니다.

## 2. 진화하는 정체성: Profiles & GEPA

- **프로필 기반 격리 (Profiles)**: 단순한 역할(Role) 변경을 넘어, 설정/메모리/스킬/세션/[[SOUL.md]]이 완전히 분리된 독립적인 작업 환경을 제공합니다. 이는 서로 다른 작업 환경을 가진 여러 에이전트를 운영하는 체계입니다.
- **GEPA (Goal-driven Evaluation and Planning Agent)**: 스스로를 잘했다고 평가하는 AI의 약점을 보완하기 위해, 실행 트레이스를 읽고 실패 지점을 찾아 개선안(PR)을 만드는 별도의 평가 체계를 제안합니다. 이는 런타임 외부에서 동작하는 '감시와 개선의 루프'입니다.

## 3. 지휘자의 통찰 (Orchestrator's Note)

Hermes는 UI가 아닌 **Runtime**이며, 프롬프트가 아닌 **축적되는 Workflow**입니다. AI 에이전트의 진정한 경쟁력은 내 일을 구조화하고 다시 실행하는 능력에 있습니다. 이는 `csp-brain`이 추구하는 "Do it once, automate it forever" 원칙이 시스템 레벨에서 구현된 형태라 할 수 있습니다.

---
**관련 문서**:
- [[hermes-pi-philosophy]]
- [[context-linker]]
- [[harness-protocol]]
