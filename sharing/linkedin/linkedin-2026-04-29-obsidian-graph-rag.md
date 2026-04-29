## 당신의 Obsidian 이 Graph RAG 라고요? 맞습니다.

오늘 제 개인 지식 관리 시스템 (csp-brain) 을 분석하다가
놀라운 사실을 발견했습니다.

**"엔터프라이즈 Graph RAG 를 따로 구축할 필요가 없다"**는 것.

---

### 오늘의 작업에서 발견한 것

GitHub 에 커밋한 24 개의 wiki 문서를 분석했습니다.
백링크 (문서 간 연결) 기반의 지식 그래프 구조였죠.

**분석 결과:**
- 총 24 개 문서 중 **58% 가 서로 연결됨**
- **4 개의 지식 군집** 발견:
  1. HR/조직심리학 (SDT ←→ Vibe Coding)
  2. 데이터 감지 (Weak Signal → EX Intelligence)
  3. 시스템 도구 (Obsidian ←→ Notion)
  4. 프로토콜 (Dream Cycle → CSP-Brain)

**그리고 6 개의 고립 문서를 연결했습니다.**
상호 참조 링크를 추가하는 것만으로 지식 그래프가 더 촘촘해졌죠.

---

### Graph RAG 가 별건가요?

기업에서 Graph DB 도입하고, 엔티티 추출하고, 관계 정의하고...
그렇게 구축한다는 Graph RAG 가 **Obsidian 사용자의 일상**입니다.

- **노드** = 각 문서 (concepts/, tools/, skills/)
- **에지** = `[[백링크]]`
- **Multi-hop 추론** = 문서 간 연결을 따른 이동

**실제 추론 경로 예시:**

```
질문: "CSP 의 Vibe Coding 은 어떤 심리학 이론에 기반하는가?"

추론: Vibe Coding ←→ Self-Determination Theory
답변: 자율성 + 유능감 충족 (SDT)
```

---

### 제가 만든 것

오늘 이 인사이트를 바탕으로 2 가지를 만들었습니다:

1. **`generate-linkedin` 스킬**
   - wiki/projects/outputs 를 스캔하여 링크드인 포스트 자동 생성
   - Claude Code 가 학습한 지식으로 콘텐츠 마케팅

2. **Graph Backlink Analysis 리포트**
   - 고립 문서 탐지 및 연결 권고
   - 지식 그래프 건강도 진단

---

### 핵심 교훈

**"기술은 이미 당신 손안에 있습니다"**

- Obsidian 을 쓴다면 → Graph DB 가 있습니다
- 백링크를 추가한다면 → RAG 가 작동합니다
- Claude Code 를 쓴다면 → AI Agent 가 있습니다

별도의 Graph DB 를 도입하거나
복잡한 RAG 파이프라인을 구축할 필요가 없습니다.

**필요한 것:**
1. `[[백링크]]` 2 개 이상 규칙
2. 주간 정리 루틴 (Dream Cycle)
3. Claude Code 에게 "분석해줘" 라고 말하기

---

### 다음 실험

- Obsidian Graph View 로 지식 군집 시각화
- 고립 문서 자동 감지 스킬 추가
- 생성된 포스트 실제 링크드인에 게시 (A/B 테스트)

---

#Obsidian #GraphRAG #KnowledgeGraph #ClaudeCode #SecondBrain
#지식관리 #인공지능 #생산성 #VibeCoding

---

**질문:**
Obsidian 으로 지식 관리 중이신 분, Graph View 써보셨나요?
어떤 군집이 보이나요? 👇
