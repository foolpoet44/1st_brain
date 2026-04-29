# Extracted Knowledge from Conv: 0cffa37a-5ef5-4905-a98a-6cdbf60ab471

**Date**: 2026-02-08T02:55:57.951282Z

### Extracted Code (text)

```text
기존: "Vibe Coding 교육 4과정 개발"
→ 개선: "시민 개발자 육성 프로그램 - 6개월 내 30명의 실전 배출"

실행 방법:
- 1단계(Q1): Cursor, Replit 등 검증된 플랫폼 선정
- 2단계(Q2): 부서별 "1인 1 AI Tool" 개발 챌린지
- 3단계(Q3-Q4): 우수 사례 코드 라이브러리화 및 재사용
```

### Extracted Code (text)

```text
기존: "LV3 이상 Physical AI Leader Pool 30명 확보"
→ 강화: "Smart Factory Transformation Champion 30명 육성"

육성 로드맵:
Phase 1: Digital Twin 설계 능력
- Nvidia Omniverse 또는 Siemens 플랫폼 활용
- 현재 공장 라인의 3D 시뮬레이션 구축

Phase 2: Physical AI 기술 스택 습득
- IoT 센서 데이터 수집/분석
- AI 기반 예측 유지보수
- 로봇 좌표 자동 조정 알고리즘

Phase 3: ROI 증명 프로젝트
- 1개 라인에서 "10% 생산성 향상" 시범 사례 창출
- 이를 전사 확산의 레퍼런스로 활용
```

### Extracted Code (text)

```text
Tier 1 (Input Metrics):
- AX 성숙도 Survey 점수
- 교육 이수율
- Tool 활용률

Tier 2 (Output Metrics):
- 업무 자동화율 (현재 10% 목표)
- 의사결정 속도 (예: 보고서 작성 시간 30% 단축)
- 직원 업무 만족도

Tier 3 (Outcome Metrics) ⭐
- 매출 기여도 (예: 신제품 출시 사이클 단축)
- 비용 절감액 (연간 ₩XX억)
- 고객 만족도 개선
```

### Extracted Code (text)

```text
위험: 45%의 AI 생성 코드에 보안 취약점 존재
해결책:
- "공통 AX Tool" 승인 프로세스 확립
- 보안 체크리스트 의무화
- 주간 "AI Code Review" 세션 운영
```

### Extracted Code (text)

```text
목표: "상시학습 체계 구축"
실행:
- Slack/Teams에 "#ai-wins" 채널 개설
- 매주 "5분 AI Tip" 영상 제작/공유
- 월간 "AI Town Hall" 운영 (성공/실패 사례 공유)
```

### Extracted Code (text)

```text
원칙: "작게 시작, 빠르게 증명, 점진적 확장"

Q1-Q2: Quick Wins 확보
- 공통업무 중 가장 쉽고 임팩트 큰 것 3개 선정
- 각각 파일럿 후 ROI 측정
- 성공 사례로 내부 모멘텀 구축

Q3-Q4: 스케일업
- 검증된 접근법만 전사 확산
- 실패한 것은 과감히 중단 (Fail Fast)
```

### Extracted Code (text)

```text
┌─────────────────────────────────────────────────────┐
│   LAYER 3: Intelligence Layer (AI Orchestration)    │
│   - AX Copilot (개인화된 AI 어시스턴트)              │
│   - Auto-Learning Engine (패턴 학습 & 추천)         │
│   - Impact Analytics (실시간 ROI 측정)              │
└─────────────────────────────────────────────────────┘
                         ↕️
┌─────────────────────────────────────────────────────┐
│   LAYER 2: Workflow Layer (Process Automation)      │
│   - Smart Workflow Designer (노코드 프로세스 빌더)   │
│   - Task Orchestrator (업무 자동 라우팅)            │
│   - Knowledge Graph (조직 지식 연결망)              │
└─────────────────────────────────────────────────────┘
                         ↕️
┌─────────────────────────────────────────────────────┐
│   LAYER 1: Foundation Layer (Data & People)         │
│   - Unified Data Lake (모든 데이터의 단일 소스)     │
│   - Skill Ontology Engine (역량 매핑 시스템)        │
│   - Engagement Tracker (참여도 실시간 측정)         │
└─────────────────────────────────────────────────────┘
```

### Extracted Code (python)

```python
# 개념적 구조
class PersonalAXCopilot:
    def __init__(self, user_profile):
        self.skill_level = user_profile.ax_maturity_level
        self.work_context = user_profile.department_workflows
        self.learning_style = user_profile.preferences
    
    def recommend_next_action(self):
        """
        - 현재 업무 패턴 분석
        - 자동화 가능 작업 식별
        - 맞춤형 학습 콘텐츠 추천
        - 동료 성공 사례 연결
        """
        if self.skill_level == "Beginner":
            return self.suggest_quick_wins()
        elif self.skill_level == "Intermediate":
            return self.suggest_workflow_redesign()
        else:
            return self.suggest_innovation_projects()
    
    def track_impact(self):
        """실시간으로 AI 도구 사용 효과 측정"""
        return {
            'time_saved': self.calculate_time_savings(),
            'quality_improvement': self.measure_output_quality(),
            'learning_velocity': self.track_skill_growth()
        }
```

### Extracted Code (text)

```text
┌─────────────────────────────────────────────┐
│  📊 AX 성숙도 히트맵 (부서별/레벨별)         │
│  ┌──────┬──────┬──────┬──────┐             │
│  │ 영업 │ 생산 │ 연구 │ 지원 │             │
│  │ 🟢🟢 │ 🟡🟡 │ 🔴🔴 │ 🟢🟢 │             │
│  └──────┴──────┴──────┴──────┘             │
│                                             │
│  🎯 실시간 임팩트 메트릭                    │
│  • 총 절감 시간: 2,340시간/월               │
│  • 자동화율: 23% → 목표 10% 초과달성        │
│  • MVP 완성: 3/5건                          │
│                                             │
│  ⚠️ Action Required                         │
│  • 연구팀 AX 성숙도 낮음 → 타겟 인터벤션   │
│  • Physical AI 파일럿 진행률 60%            │
└─────────────────────────────────────────────┘
```

### Extracted Code (javascript)

```javascript
// 학습 여정 자동 생성 알고리즘
const generateLearningPath = (user) => {
  const assessment = assessCurrentLevel(user);
  const goalAlignment = alignWithBusinessGoals(user.department);
  
  return {
    week1_2: "Foundation - AI 기초 & 프롬프트 엔지니어링",
    week3_4: "Tools Mastery - Cursor/Replit 실습",
    week5_6: "First MVP - 본인 업무 자동화 도구 개발",
    week7_8: "Collaboration - 팀 프로젝트 참여",
    week9_10: "Production - 실제 배포 & 운영",
    week11_12: "Teaching - 후배 멘토링"
  }
}
```

### Extracted Code (text)

```text
Notion (학습 허브)
  ↓
├─ 📚 Course Library (동영상, 문서, 코드 템플릿)
├─ 🎯 Weekly Challenges (실전 과제)
├─ 👥 Peer Review System (동료 피드백)
├─ 🏆 Achievement Tracker (gamification)
└─ 💬 AI Tutor (24/7 질문 응답)
```

### Extracted Code (text)

```text
┌─────────────────────────────────────────┐
│   🎯 AX 프로젝트 대시보드 (Single Page)  │
│   - 주간 체크인                          │
│   - 진행 상황 시각화                     │
│   - 다음 액션 자동 생성                  │
└─────────────────────────────────────────┘
            ↓ ↓ ↓
┌──────────┐  ┌──────────┐  ┌──────────┐
│ 📊 OKR   │  │ 📝 Tasks │  │ 💡 Wins  │
│ Tracker  │  │ Pipeline │  │ Journal  │
└──────────┘  └──────────┘  └──────────┘
```

### Extracted Code (text)

```text
┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐
│   Q1    │  │   Q2    │  │   Q3    │  │   Q4    │
├─────────┤  ├─────────┤  ├─────────┤  ├─────────┤
│ Vibe    │  │ Physical│  │ AX 역량 │  │ 성과    │
│ Coding  │  │ AI 육성 │  │ 고도화  │  │ 측정    │
│ 🟢 60%  │  │ 🟡 30%  │  │ ⚪ 0%   │  │ ⚪ 0%   │
└─────────┘  └─────────┘  └─────────┘  └─────────┘
```

### Extracted Code (markdown)

```markdown
## 이번 주 (2026.02.10 - 02.14)

### P0 - 반드시 완료 (3개 이하로 제한)
- [ ] Vibe Coding 플랫폼 선정 최종 확정
- [ ] Physical AI 파일럿 라인 섭외 미팅

### P1 - 가능하면 완료
- [ ] Skill Ontology 1차 구조 스케치
- [ ] 공통업무 자동화 후보 3건 리스트업

### P2 - 시간 남으면
- [ ] 벤치마킹 자료 읽기
```

### Extracted Code (markdown)

```markdown
# 2026년 6주차 회고 (2/10-2/14)

## 🎉 이번 주 Wins (자동 로드)
1. Cursor 도입 결정 - 팀 미팅에서 만장일치
2. 첫 Vibe Coding MVP: 휴가 신청 자동화 봇 완성
3. Physical AI 컨퍼런스 참석 - 3개 인사이트 획득

## 📊 숫자로 보는 한 주
- 완료한 작업: 7개
- OKR 진척: +5%
- 학습 시간: 3.5시간

## 🤔 What Went Well
- Vibe Coding이 생각보다 쉬웠음
- 동료들 반응이 긍정적

## 😅 What Could Be Better
- Physical AI 파일럿 진행 늦어짐
- 주말에 번아웃 느낌

## 🎯 다음 주 Focus (자동 로드)
- P0 작업 3개
```

### Extracted Code (markdown)

```markdown
# 🚀 26년 AX 프로젝트 대시보드

---

## ⚡ Quick Check (매일 아침 5분)

### 오늘 해야 할 일 (P0만 자동 표시)
@database(Tasks, filter: 담당주차=이번주 AND 우선순위=P0)

### 위험 신호 🚨
@database(OKR Tracker, filter: 진척률 < 30% AND 분기 = Current)

---

## 📈 진행 상황 (주간 업데이트)

### OKR 달성도
@database(OKR Tracker, view: Progress Chart)

| 목표 | 목표치 | 현재 | 진척률 | 상태 |
|------|--------|------|--------|------|
| Vibe Coding MVP | 5건 | 2건 | 40% | 🟡 |
| Physical AI Pool | 30명 | 8명 | 27% | 🔴 |
| 생산성 개선 | 10% | 3% | 30% | 🔴 |

**인사이트:**
- Physical AI 육성이 병목 → Q2에 집중 투입 필요
- Vibe Coding은 순조로움

---

## 🎯 이번 주 Sprint (자동 갱신)
@database(Tasks, view: Weekly Sprint)

---

## 💡 최근 Wins (동기부여)
@database(Wins Journal, limit: 5, sort: 날짜 desc)

---

## 📚 학습 대기열
- [ ] Cursor 고급 기능 튜토리얼 (30분)
- [ ] Physical AI 백서 읽기 (1시간)
- [ ] Skill Ontology 설계 사례 연구

---

## 🔄 주간 루틴 체크리스트

### 월요일 아침
- [ ] 지난주 회고 작성
- [ ] 이번주 P0 작업 3개 선정
- [ ] OKR 진척률 업데이트

### 수요일 점심
- [ ] Mid-week check: P0 진행 상황
- [ ] 필요시 우선순위 재조정

### 금요일 오후
- [ ] 완료한 작업 → Wins Journal 기록
- [ ] 다음주 Backlog 정리

---

## 📞 Quick Links
- [전사 AX 성숙도 Survey 폼]()
- [Vibe Coding 플랫폼 비교표]()
- [Physical AI 벤치마킹 자료]()
- [월간 리포트 템플릿]()
```

### Extracted Code (text)

```text
트리거: 매주 월요일 오전 9시
↓
Notion API: OKR Tracker 조회
↓
조건 분기:
  IF 진척률 < 50% THEN
    → Slack DM 발송: "⚠️ [목표명] 진행 느림 - 체크 필요"
  ELSE
    → 계속 진행
```

### Extracted Code (text)

```text
트리거: Notion Tasks DB의 상태가 "Done"으로 변경
↓
Notion API: 
  1. 관련 OKR의 "현재값" +1
  2. Wins Journal에 새 항목 생성
↓
Claude API 호출:
  "이 작업을 한 줄로 축하해줘"
↓
Slack: 축하 메시지 + 🎉
```

### Extracted Code (text)

```text
트리거: 매주 금요일 오후 4시
↓
Notion API: 
  - 이번 주 완료한 Tasks 조회
  - Wins Journal 항목 조회
  - OKR 진척률 계산
↓
Claude API:
  "이 데이터로 회고 초안 작성해줘"
↓
Notion: 새 회고 페이지 생성 (템플릿 적용)
↓
Apple Notes: 같은 내용 백업
```

### Extracted Code (text)

```text
/template → Database → Full page
   
   1️⃣ AX OKR Tracker
   2️⃣ AX Tasks Pipeline  
   3️⃣ AX Wins Journal
```

### Extracted Code (text)

```text
목표 1: Vibe Coding MVP 5건 개발
   - 핵심지표: 5
   - 분기: Q1-Q2
   
   목표 2: Physical AI Leader Pool 30명
   - 핵심지표: 30
   - 분기: Q2-Q3
   
   목표 3: 생산성 10% 개선
   - 핵심지표: 10
   - 분기: Q1-Q4
```

### Extracted Code (text)

```text
You: "이번 주 계획 리뷰해줘"

[Notion 대시보드 스크린샷 첨부]

Claude: 
- P0 작업이 3개인데 실현 가능해 보입니다
- Physical AI 관련 작업이 없네요 - 의도적인가요?
- 추천: Vibe Coding 플랫폼 선정 전에 벤치마킹 1개 추가
```

### Extracted Code (text)

```text
You: "이번 주 회고 데이터야. 인사이트 뽑아줘"

[Wins Journal 데이터 복사]

Claude:
- 패턴: Vibe Coding 관련 승리가 많음 → 강점 활용 중
- 갭: Physical AI는 한 건도 없음 → 다음 주 집중 필요
- 추천: 성공 모멘텀 유지 위해 작은 Physical AI Win 하나 만들기
```

### Extracted Code (text)

```text
┌─────────────────────────────────────────────────────────────┐
│  Feb  │  Mar  │  Apr  │  May  │  Jun  │  Jul  │  Aug  │  Sep  │  Oct  │  Nov  │  Dec  │
├───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤
│  🔧 Foundation Phase   │  🚀 Acceleration    │  📈 Scale & Optimize │  ✅ Harvest  │
│                        │                     │                      │              │
│ [OKR 1] Vibe Coding MVP 5건                                                        │
│ ●─────●─────●─────●─────●─────────────────────────────────────────●              │
│ Setup  Pilot  MVP1  MVP2  MVP3              MVP4                  MVP5            │
│                                                                                    │
│ [OKR 2] Physical AI Leader Pool 30명                                              │
│ ●─────●─────●─────────●─────────●───────────●───────────●─────────●              │
│ Plan  Recruit Onboard-10  Train-20    Certify  Deploy    Mentor   Complete       │
│                                                                                    │
│ [OKR 3] AX 성숙도 15% 향상 & 생산성 10% 개선                                       │
│ ●─────────●─────────●─────────●─────────●─────────●─────────●─────●              │
│ Survey1  Env1   Workflow1  Tool   Env2   Workflow2  Survey2  Final Measure       │
└─────────────────────────────────────────────────────────────────────────────────┘
```

### Extracted Code (markdown)

```markdown
## 2월: 인프라 구축 (Week 1-4)
- [ ] Vibe Coding 플랫폼 선정 (Cursor vs Replit vs Bolt)
- [ ] 학습 커리큘럼 설계 (6주 과정)
- [ ] 파일럿 그룹 10명 모집 (각 부서 2명씩)
- [ ] Notion Academy 페이지 구축
- [ ] Quick Win 후보 업무 10개 리스트업

## 3월: 1차 교육 & 첫 MVP (Week 5-8)
- [ ] Week 1-2: 기초 교육 (프롬프트 엔지니어링)
- [ ] Week 3-4: 실습 (간단한 도구 만들기)
- [ ] 🎯 **MVP 1: 휴가 신청 자동화 봇** (3월 말 완료)

## 4월: 2차 MVP 개발 (Week 9-13)
- [ ] 파일럿 그룹 피드백 수렴
- [ ] 2기 모집 (20명 추가)
- [ ] 🎯 **MVP 2: 주간 보고서 자동 생성기** (4월 말 완료)

## 5월: 3차 MVP & 확산 (Week 14-17)
- [ ] 성공 사례 전사 공유 (Town Hall)
- [ ] 🎯 **MVP 3: 회의록 요약 AI** (5월 말 완료)
- [ ] Code Library 구축 시작

## 6-8월: 심화 & 안정화
- [ ] 기존 MVP 운영 최적화
- [ ] 사용률 모니터링 & 개선

## 9월: 4차 MVP (Week 30-34)
- [ ] 🎯 **MVP 4: 데이터 분석 대시보드 생성기**
- [ ] 3기 모집 (심화 과정)

## 10-11월: 최종 MVP (Week 35-43)
- [ ] 🎯 **MVP 5: 고객 문의 응답 템플릿 AI**
- [ ] 전체 시민개발자 네트워크 구축

## 12월: 성과 측정 (Week 44-48)
- [ ] 5개 MVP 사용 통계 집계
- [ ] ROI 보고서 작성
- [ ] 27년 로드맵 수립
```

### Extracted Code (markdown)

```markdown
## 2월: 후보군 발굴 & 체계 설계 (Week 1-4)
- [ ] Physical AI Skill Ontology 정의
  - Technical: IoT, Digital Twin, 로봇 제어
  - Domain: 공정 지식, 품질 관리
  - Soft: 문제해결, 협업
- [ ] 부서별 후보 추천 요청 (관리자 미팅)
- [ ] 벤치마킹: Siemens, BMW 사례 연구
- [ ] 파일럿 라인 선정 (자동화 효과 큰 곳)

## 3월: 1차 그룹 온보딩 (10명) (Week 5-8)
- [ ] 선발 기준 확정 (현장 경험 + 학습 의지)
- [ ] Onboarding Session (Physical AI 개요)
- [ ] 🎯 **첫 10명 Pool 구축 완료**
- [ ] Digital Twin 기초 교육 (Omniverse 소개)

## 4월: 실습 프로젝트 시작 (Week 9-13)
- [ ] 파일럿 라인 현황 분석 (병목 지점 식별)
- [ ] IoT 센서 데이터 수집 시작
- [ ] Digital Twin 1차 모델링

## 5월: 2차 그룹 확대 (20명 누적) (Week 14-17)
- [ ] 2차 모집 (10명 추가)
- [ ] 🎯 **누적 20명 Pool 확보**
- [ ] 1차 그룹 멘토-멘티 매칭

## 6월: 심화 교육 (Week 18-22)
- [ ] AI 기반 예측 유지보수 교육
- [ ] 로봇 자동화 워크샵
- [ ] Digital Twin 고급 과정

## 7월: 파일럿 프로젝트 가동 (Week 23-26)
- [ ] Smart Factory 파일럿 정식 가동
- [ ] 실시간 모니터링 체계 구축
- [ ] 🎯 **25명 Pool (5명 추가 모집)**

## 8월: 중간 평가 & 조정 (Week 27-30)
- [ ] Skill Assessment (LV 측정)
- [ ] 부족 영역 보충 교육
- [ ] 성과 사례 문서화

## 9월: 최종 확대 (Week 31-35)
- [ ] 3차 모집 (5명 추가)
- [ ] 🎯 **목표 30명 달성**
- [ ] 전문가 인증 체계 확립

## 10월: 실전 배치 (Week 36-39)
- [ ] 각 전문가를 실제 프로젝트에 배치
- [ ] 멘토링 체계 가동

## 11월: 지속가능성 확보 (Week 40-43)
- [ ] 내부 교육 과정 정식화
- [ ] Knowledge Base 구축

## 12월: 성과 측정 (Week 44-48)
- [ ] 30명 최종 스킬 검증
- [ ] Smart Factory 파일럿 성과 측정
- [ ] 27년 확대 계획 수립
```

### Extracted Code (markdown)

```markdown
## 2월: Baseline 측정 (Week 1-4)
- [ ] AX 성숙도 Survey 1차 실시 (전체 구성원)
- [ ] 현재 생산성 Baseline 측정
  - 공통업무 소요 시간 추적 (보고서, 회의록, 데이터 입력)
- [ ] 환경 인식도 조사 (5대 불편 요소 도출)
- [ ] 🎯 **기준선 확정: 성숙도 X점, 생산성 Y시간**

## 3월: Quick Win & 개선과제 착수 (Week 5-8)
- [ ] 5대 환경 개선과제 확정
  1. AI Tool 접근성
  2. 학습 콘텐츠 부족
  3. 성과 인정 체계
  4. 협업 플랫폼
  5. 기술 지원
- [ ] 개선 1: AI Tool 카탈로그 & 신청 프로세스 구축
- [ ] 공통업무 워크플로우 분석 착수

## 4월: 워크플로우 재설계 1차 (Week 9-13)
- [ ] 보고서 작성 프로세스 재설계
  - AS-IS: 수작업 취합 → 검토 → 작성
  - TO-BE: AI 자동 취합 → 초안 생성 → 인간 검토
- [ ] 🎯 **개선 2: 학습 플랫폼 오픈** (Notion Academy)
- [ ] 파일럿 부서 적용 (영업팀)

## 5월: 효과 측정 1차 (Week 14-17)
- [ ] 파일럿 부서 생산성 측정
- [ ] 개선 3: 성과 인정 체계 도입 (AX Champion 제도)
- [ ] 워크플로우 재설계 2차 착수 (회의 프로세스)

## 6월: 중간 Survey (Week 18-22)
- [ ] AX 성숙도 Survey 2차 (중간 점검)
- [ ] 🎯 **목표 중간 점검: +5% 달성 확인**
- [ ] 개선 4: 협업 플랫폼 통합 (Slack + Notion)

## 7월: 전사 확산 시작 (Week 23-26)
- [ ] 재설계된 워크플로우 전사 확대
- [ ] AI Agent 개발 착수 (반복 업무 자동화)
- [ ] 개선 5: 기술 지원 데스크 운영

## 8월: AI Agent 적용 (Week 27-30)
- [ ] AI Agent 1호: 데이터 입력 자동화
- [ ] AI Agent 2호: 일정 관리 어시스턴트
- [ ] 사용자 피드백 수집

## 9월: 최적화 (Week 31-35)
- [ ] AI Agent 고도화
- [ ] 워크플로우 미세 조정
- [ ] 🎯 **생산성 +7% 확인**

## 10월: 공통 AX Tool 확정 (Week 36-39)
- [ ] 검증된 Tool만 선별 (5-7개)
- [ ] 전사 표준 Tool로 확정
- [ ] 교육 자료 정비

## 11월: 최종 Survey 준비 (Week 40-43)
- [ ] 개별 인터뷰 (정성적 피드백)
- [ ] 사례 수집 (Before/After)
- [ ] AX 성숙도 Survey 3차 (최종)

## 12월: 성과 측정 & 보고 (Week 44-48)
- [ ] 🎯 **최종 측정: 성숙도 +15%, 생산성 +10%**
- [ ] 경영진 보고서 작성
- [ ] 성공 요인 / 실패 요인 분석
- [ ] 2027년 전략 수립
```

### Extracted Code (markdown)

```markdown
### P0 - 이번 주 반드시 (Week 2 기준)

| 작업 | OKR | 카테고리 | 예상시간 | 상태 |
|------|-----|----------|----------|------|
| Cursor vs Replit 데모 테스트 | OKR1 | Vibe Coding | 3h | In Progress |
| Physical AI 후보 10명 리스트 확정 | OKR2 | Physical AI | 2h | Todo |
| AX 성숙도 Survey 문항 검토 | OKR3 | 환경개선 | 1h | Done ✅ |

### P1 - 가능하면

| 작업 | OKR | 카테고리 | 예상시간 | 상태 |
|------|-----|----------|----------|------|
| Notion Academy 페이지 구조 설계 | OKR1 | Vibe Coding | 2h | Todo |
| Skill Ontology 1차 드래프트 | OKR2 | Physical AI | 4h | Todo |
| 공통업무 시간 측정 도구 선정 | OKR3 | 환경개선 | 1h | Todo |

### P2 - 시간 나면

| 작업 | OKR | 카테고리 | 예상시간 | 상태 |
|------|-----|----------|----------|------|
| AI 뉴스레터 구독 (Physical AI) | OKR2 | 학습 | 0.5h | Todo |
| 벤치마킹 자료 읽기 | All | 학습 | 1h | Todo |
```

### Extracted Code (text)

```text
트리거: 매주 금요일 오후 5시
↓
Notion API 호출:
  - OKR 1 진척률 조회
  - OKR 2 진척률 조회  
  - OKR 3 진척률 조회
  - 이번 주 완료 Tasks 수
  - 이번 주 Wins 수
↓
Claude API:
  """
  이 데이터로 주간 리포트 생성:
  - 이번 주 하이라이트
  - 3대 OKR 진행 상황
  - 다음 주 Focus
  - 리스크 알림
  """
↓
Apple Notes 자동 저장
Slack DM 발송
```

### Extracted Code (text)

```text
트리거: 매주 수요일 정오
↓
조건 체크:
  IF OKR 진척률 < (목표 / 남은 주수) THEN
    → ⚠️ 리스크 알림
↓
Notion: 
  - OKR 카드에 🚨 이모지 추가
  - Status를 "위험"으로 변경
↓
Slack DM:
  "[OKR 2] Physical AI Pool 육성이 예상보다 느립니다.
  현재: 5명 / 목표: 10명 (2월말)
  Action: 추가 모집 또는 기준 조정 필요"
```

### Extracted Code (text)

```text
트리거: Wins Journal에 "🔥대박" 임팩트 항목 추가
↓
Notion API:
  - 해당 Win이 어느 OKR에 기여했는지 확인
  - OKR 진척률 업데이트
↓
Claude API:
  "이 성공을 한 줄로 축하해주고, 
  다음 마일스톤까지 무엇이 필요한지 제안해줘"
↓
Slack: 축하 메시지 + 다음 액션 제안
```

### Extracted Code (text)

```text
Notion 앱 열기
↓
1. 대시보드 Quick Check
   → 오늘 할 P0 3개 확인
   → 🚨 위험 신호 있는지 체크
   
2. 멘탈 체크
   → "오늘은 어느 OKR에 집중할까?"
   → Vibe Coding 날 / Physical AI 날 / 환경개선 날
```

### Extracted Code (markdown)

```markdown
# 🚀 2026 AX 프로젝트 통합 대시보드

## ⚡ Today's Focus (매일 아침 자동 갱신)
**오늘은 [Vibe Coding / Physical AI / 환경개선] 날**

### 오늘 할 일 (P0만)
- [ ] [자동 로드]
- [ ] [자동 로드]  
- [ ] [자동 로드]

---

## 📊 3-OKR 스코어보드 (실시간)

| OKR | 목표 | 현재 | 진척 | 예상 | 상태 |
|-----|------|------|------|------|------|
| 1. Vibe Coding MVP | 5 | 2 | 40% | 45% | 🟢 |
| 2. Physical AI Pool | 30 | 8 | 27% | 30% | 🟡 |
| 3. AX 성숙도/생산성 | 15%/10% | 3%/2% | 20% | 25% | 🔴 |

**종합 건강도: 🟡 주의 필요**
- ✅ OKR 1 순조로움
- ⚠️ OKR 2 약간 느림
- 🚨 OKR 3 집중 필요

---

## 🎯 이번 주 Sprint (Week 6: 2/10-2/14)

### OKR 1 관련
@database(Tasks, filter: OKR=1 AND 주차=이번주)

### OKR 2 관련  
@database(Tasks, filter: OKR=2 AND 주차=이번주)

### OKR 3 관련
@database(Tasks, filter: OKR=3 AND 주차=이번주)

---

## 💡 이번 주 Wins (동기부여)
@database(Wins Journal, limit: 5, sort: 날짜 desc)

---

## 📅 다가오는 마일스톤

| 날짜 | OKR | 마일스톤 |
|------|-----|----------|
| 2/28 | OKR 1 | 플랫폼 선정 완료 |
| 2/28 | OKR 2 | 1차 10명 Pool 확보 |
| 2/28 | OKR 3 | Baseline 측정 완료 |
| 3/31 | OKR 1 | 첫 MVP 완성 |
| 6/30 | ALL | 중간 점검 (50% 달성) |
| 12/31 | ALL | 최종 목표 달성 |

---

## 🔧 Quick Actions

- [새 Task 추가]()
- [Win 기록하기]()
- [주간 회고 쓰기]()
- [Claude에게 물어보기]()

---

## 📈 Progress Chart
@gallery(OKR Tracker, view: Progress Bar)
```

### Extracted Code (text)

```text
아침 시나리오:
1. 앱 실행 → 대시보드 확인 (30초)
2. 오늘 할 P0 작업 3개 확인 (1분)
3. 리스크 알림 확인 (30초)

저녁 시나리오:
1. 완료한 작업 체크 (1분)
2. 간단한 메모/Win 기록 (2분)
3. 내일 준비 (1분)

주말 시나리오:
1. 주간 회고 자동 생성 확인 (3분)
2. 다음 주 계획 검토 (5분)
3. AI 인사이트 읽기 (2분)
```

### Extracted Code (text)

```text
┌─────────────────────────────────────────────────────┐
│                  Streamlit Web UI                   │
│  (대시보드, OKR 관리, Task 관리, 회고, 차트)         │
└─────────────────────────────────────────────────────┘
                         ↕️
┌─────────────────────────────────────────────────────┐
│              Business Logic Layer                   │
│  - OKR Calculator                                   │
│  - Task Prioritizer                                 │
│  - AI Insight Generator (Claude API)                │
│  - Progress Analyzer                                │
└─────────────────────────────────────────────────────┘
                         ↕️
┌─────────────────────────────────────────────────────┐
│               Data Access Layer                     │
│  - OKR Repository                                   │
│  - Task Repository                                  │
│  - Wins Repository                                  │
│  - Analytics Repository                             │
└─────────────────────────────────────────────────────┘
                         ↕️
┌─────────────────────────────────────────────────────┐
│                SQLite Database                      │
│  okrs | tasks | wins | weekly_reviews | settings   │
└─────────────────────────────────────────────────────┘
```

### Extracted Code (text)

```text
사용자 입력 → Streamlit UI → Validation → Business Logic
                                              ↓
                                         DB 저장
                                              ↓
                                      자동 계산 트리거
                                              ↓
                             (필요시) Claude API 호출 → 인사이트 생성
                                              ↓
                                         결과 표시
```

### Extracted Code (txt)

```txt
streamlit>=1.31.0
anthropic>=0.18.0
pandas>=2.1.0
plotly>=5.18.0
python-dotenv>=1.0.0
pydantic>=2.5.0
sqlalchemy>=2.0.0
pytest>=7.4.0
black>=23.12.0
```

### Extracted Code (text)

```text
┌─────────────┐         ┌─────────────┐         ┌─────────────┐
│    OKRs     │1      *│    Tasks    │1      *│    Wins     │
├─────────────┤◄────────├─────────────┤◄────────├─────────────┤
│ id (PK)     │         │ id (PK)     │         │ id (PK)     │
│ title       │         │ title       │         │ title       │
│ quarter     │         │ okr_id (FK) │         │ task_id(FK) │
│ target      │         │ category    │         │ date        │
│ current     │         │ priority    │         │ impact      │
│ unit        │         │ status      │         │ content     │
│ created_at  │         │ due_date    │         │ learning    │
│ updated_at  │         │ est_hours   │         │ created_at  │
└─────────────┘         │ actual_hours│         └─────────────┘
                        │ created_at  │
                        └─────────────┘

┌──────────────────┐
│ Weekly_Reviews   │
├──────────────────┤
│ id (PK)          │
│ week_number      │
│ year             │
│ highlights       │
│ metrics          │
│ went_well        │
│ to_improve       │
│ next_focus       │
│ ai_insights      │
│ created_at       │
└──────────────────┘
```

### Extracted Code (sql)

```sql
CREATE TABLE okrs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    quarter TEXT CHECK(quarter IN ('Q1', 'Q2', 'Q3', 'Q4', 'ALL')),
    category TEXT CHECK(category IN ('vibe_coding', 'physical_ai', 'ax_maturity')),
    target_value REAL NOT NULL,
    current_value REAL DEFAULT 0,
    unit TEXT,  -- '건', '명', '%' 등
    milestone_dates TEXT,  -- JSON 형식으로 저장
    status TEXT CHECK(status IN ('on_track', 'at_risk', 'off_track')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Extracted Code (sql)

```sql
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    okr_id INTEGER,
    title TEXT NOT NULL,
    description TEXT,
    category TEXT CHECK(category IN ('vibe_coding', 'physical_ai', 'ax_maturity')),
    priority TEXT CHECK(priority IN ('P0', 'P1', 'P2')),
    status TEXT CHECK(status IN ('backlog', 'in_progress', 'done', 'blocked')),
    difficulty TEXT CHECK(difficulty IN ('easy', 'medium', 'hard')),
    due_date DATE,
    assigned_week TEXT,  -- 'Week 6', 'Week 7' 등
    estimated_hours REAL,
    actual_hours REAL,
    blocker_reason TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMP,
    FOREIGN KEY (okr_id) REFERENCES okrs(id)
);
```

### Extracted Code (sql)

```sql
CREATE TABLE wins (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_id INTEGER,
    title TEXT NOT NULL,
    date DATE DEFAULT CURRENT_DATE,
    category TEXT CHECK(category IN ('learning', 'execution', 'impact', 'insight')),
    impact TEXT CHECK(impact IN ('great', 'good', 'okay')),
    content TEXT,
    learning TEXT,
    okr_category TEXT,  -- 어느 OKR에 기여했는지
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (task_id) REFERENCES tasks(id)
);
```

### Extracted Code (sql)

```sql
CREATE TABLE weekly_reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    week_number INTEGER NOT NULL,
    year INTEGER NOT NULL,
    week_start_date DATE,
    week_end_date DATE,
    
    -- 정량 데이터
    tasks_completed INTEGER,
    okr1_progress REAL,
    okr2_progress REAL,
    okr3_progress REAL,
    total_hours REAL,
    
    -- 정성 데이터
    highlights TEXT,  -- JSON 배열
    went_well TEXT,
    could_be_better TEXT,
    next_week_focus TEXT,
    
    -- AI 생성 인사이트
    ai_insights TEXT,
    ai_recommendations TEXT,
    
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(week_number, year)
);
```

### Extracted Code (sql)

```sql
CREATE TABLE settings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    key TEXT UNIQUE NOT NULL,
    value TEXT,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 기본 설정값
INSERT INTO settings (key, value) VALUES
    ('project_start_date', '2026-02-03'),
    ('project_end_date', '2026-12-31'),
    ('work_hours_per_week', '40'),
    ('claude_api_key', ''),
    ('enable_notifications', 'true');
```

### Extracted Code (text)

```text
Core Features (MVP - Week 1-2)
├─ 대시보드 (Dashboard)
├─ OKR 관리 (OKR Management)
├─ Task 관리 (Task Management)
└─ 기본 통계 (Basic Analytics)

Enhanced Features (Week 3-4)
├─ Wins 기록 (Wins Journal)
├─ 주간 회고 (Weekly Review)
├─ AI 인사이트 (AI Insights)
└─ 고급 차트 (Advanced Charts)

Advanced Features (Week 5-6)
├─ 자동화 (Automation)
├─ 데이터 Export/Import
├─ 모바일 최적화
└─ 알림 시스템
```

### Extracted Code (text)

```text
┌────────────────────────────────────────────────┐
│  🚀 AX 프로젝트 대시보드                       │
├────────────────────────────────────────────────┤
│                                                │
│  ⚡ Today's Focus                              │
│  오늘은 [Vibe Coding] 날                       │
│  □ Task 1 (P0)                                 │
│  □ Task 2 (P0)                                 │
│  □ Task 3 (P0)                                 │
│                                                │
├────────────────────────────────────────────────┤
│                                                │
│  📊 3-OKR 스코어보드                           │
│  ┌──────────┬───────┬───────┬───────┬──────┐  │
│  │ OKR      │ 목표  │ 현재  │ 진척  │ 상태 │  │
│  ├──────────┼───────┼───────┼───────┼──────┤  │
│  │ Vibe     │ 5     │ 2     │ 40%   │ 🟢   │  │
│  │ Phys AI  │ 30    │ 8     │ 27%   │ 🟡   │  │
│  │ AX Mat.  │ 15%   │ 3%    │ 20%   │ 🔴   │  │
│  └──────────┴───────┴───────┴───────┴──────┘  │
│                                                │
│  [Progress Chart - 시간대별 진척도]            │
│                                                │
├────────────────────────────────────────────────┤
│                                                │
│  💡 최근 Wins (3개)                            │
│  ⭐ [2/10] Cursor 도입 결정 완료               │
│  ⭐ [2/9] 첫 MVP 아이디어 확정                 │
│  ⭐ [2/8] Physical AI 파일럿 라인 섭외         │
│                                                │
├────────────────────────────────────────────────┤
│                                                │
│  🎯 다가오는 마일스톤                          │
│  - 2/28: 플랫폼 선정 완료                      │
│  - 2/28: 10명 Pool 확보                        │
│                                                │
│  [🤖 AI 인사이트 보기]                         │
│                                                │
└────────────────────────────────────────────────┘
```

### Extracted Code (python)

```python
def render_dashboard():
    # 1. 오늘 P0 작업 로드
    today_tasks = get_today_p0_tasks()
    
    # 2. OKR 현황 로드
    okr_status = calculate_okr_status()
    
    # 3. 최근 Wins 로드
    recent_wins = get_recent_wins(limit=5)
    
    # 4. 다음 마일스톤 계산
    upcoming = get_upcoming_milestones()
    
    # 5. AI 인사이트 (캐시 활용)
    insights = get_cached_insights()
    
    # 6. 렌더링
    st.metric("종합 진척률", f"{okr_status['overall']}%")
    # ...
```

### Extracted Code (python)

```python
def create_okr():
    with st.form("new_okr"):
        title = st.text_input("목표명")
        category = st.selectbox("카테고리", 
            ["Vibe Coding", "Physical AI", "AX Maturity"])
        target = st.number_input("목표값", min_value=0)
        unit = st.text_input("단위", value="건")
        quarter = st.multiselect("분기", ["Q1", "Q2", "Q3", "Q4"])
        
        if st.form_submit_button("등록"):
            save_okr(title, category, target, unit, quarter)
            st.success("OKR이 등록되었습니다!")
```

### Extracted Code (python)

```python
def update_okr_progress(okr_id):
    current = st.number_input("현재값", min_value=0)
    
    # 자동 계산
    progress = (current / target) * 100
    status = get_status_by_progress(progress, weeks_left)
    
    update_okr(okr_id, current, status)
```

### Extracted Code (text)

```text
┌────────────────────────────────────────────┐
│  📝 Task Pipeline                          │
├────────────────────────────────────────────┤
│                                            │
│  [+ New Task]  [Filter ▼]  [Sort ▼]       │
│                                            │
│  ┌─ Backlog (5) ────────────────────────┐ │
│  │ □ Task A (P1) - Vibe Coding          │ │
│  │ □ Task B (P2) - Physical AI          │ │
│  └──────────────────────────────────────┘ │
│                                            │
│  ┌─ In Progress (3) ────────────────────┐ │
│  │ □ Task C (P0) - 진행률 60%           │ │
│  │ □ Task D (P0) - 진행률 30%           │ │
│  └──────────────────────────────────────┘ │
│                                            │
│  ┌─ Done This Week (7) ─────────────────┐ │
│  │ ✅ Task E - 2시간 소요               │ │
│  │ ✅ Task F - 3시간 소요               │ │
│  └──────────────────────────────────────┘ │
│                                            │
└────────────────────────────────────────────┘
```

### Extracted Code (python)

```python
def create_task_with_ai():
    user_input = st.text_area("무엇을 해야 하나요?")
    
    if st.button("AI 추천 받기"):
        # Claude API 호출
        suggestion = claude_suggest_task_details(user_input)
        
        # 자동 채우기
        st.selectbox("우선순위", value=suggestion['priority'])
        st.number_input("예상 시간", value=suggestion['hours'])
        st.selectbox("난이도", value=suggestion['difficulty'])
```

### Extracted Code (python)

```python
def update_task_status():
    task_id = st.selectbox("Task", get_all_tasks())
    new_status = st.radio("상태", ["Backlog", "In Progress", "Done"])
    
    if st.button("업데이트"):
        update_status(task_id, new_status)
        
        # Done으로 변경 시 자동 처리
        if new_status == "Done":
            auto_create_win(task_id)
            update_related_okr(task_id)
```

### Extracted Code (python)

```python
def show_weekly_sprint():
    current_week = get_current_week_number()
    
    st.header(f"Week {current_week} Sprint")
    
    # P0 작업 (3개 제한)
    p0_tasks = get_tasks_by_priority("P0", current_week)
    if len(p0_tasks) > 3:
        st.warning("⚠️ P0 작업이 3개를 초과했습니다!")
    
    # P1, P2 작업
    # ...
```

### Extracted Code (python)

```python
def quick_win_entry():
    with st.form("quick_win"):
        col1, col2 = st.columns([3, 1])
        
        with col1:
            title = st.text_input("한 줄 요약")
        with col2:
            impact = st.select_slider("임팩트", 
                ["👍괜찮", "✨좋음", "🔥대박"])
        
        content = st.text_area("무슨 일이 있었나요?")
        learning = st.text_area("배운 점")
        
        if st.form_submit_button("기록"):
            save_win(title, impact, content, learning)
```

### Extracted Code (python)

```python
def show_wins_timeline():
    wins = get_all_wins_by_date()
    
    for date, wins_on_date in wins.groupby('date'):
        st.markdown(f"### {date}")
        for win in wins_on_date:
            with st.expander(f"{win.impact} {win.title}"):
                st.write(win.content)
                st.caption(f"학습: {win.learning}")
```

### Extracted Code (python)

```python
INSIGHT_PROMPT = """
당신은 프로젝트 관리 전문가입니다. 다음 데이터를 분석하여 인사이트를 제공하세요.

# 현재 상황
- Week: {week_number}
- 전체 진척률: {overall_progress}%

# OKR 현황
{okr_data}

# 이번 주 활동
- 완료한 작업: {completed_tasks}개
- 총 소요 시간: {total_hours}시간
- 기록한 Wins: {wins_count}개

# 요청사항
1. 가장 잘하고 있는 점 1가지
2. 가장 주의가 필요한 점 1가지
3. 다음 주 집중해야 할 구체적 액션 1가지

각 항목을 한 문장으로 간결하게 작성하세요.
"""

def generate_ai_insights(week_data):
    response = anthropic_client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=500,
        messages=[{
            "role": "user",
            "content": INSIGHT_PROMPT.format(**week_data)
        }]
    )
    
    return parse_insights(response.content)
```

### Extracted Code (python)

```python
def generate_weekly_review():
    week_data = {
        'completed_tasks': get_completed_tasks_count(),
        'wins': get_wins_this_week(),
        'okr_progress': get_okr_delta(),
        'blockers': get_blocked_tasks(),
    }
    
    # AI가 회고 초안 작성
    draft = claude_generate_review(week_data)
    
    # 사용자가 편집 가능
    with st.form("weekly_review"):
        highlights = st.text_area("하이라이트", value=draft['highlights'])
        went_well = st.text_area("잘한 점", value=draft['went_well'])
        to_improve = st.text_area("개선할 점", value=draft['to_improve'])
        next_focus = st.text_area("다음 주 Focus", value=draft['next_focus'])
        
        if st.form_submit_button("저장"):
            save_review(highlights, went_well, to_improve, next_focus)
```

### Extracted Code (text)

```text
ax-project-manager/
│
├── .env                        # 환경 변수 (API 키 등)
├── .gitignore
├── README.md
├── requirements.txt
│
├── main.py                     # Streamlit 앱 진입점
│
├── config/
│   ├── __init__.py
│   ├── settings.py             # 전역 설정
│   └── database.py             # DB 연결 설정
│
├── database/
│   ├── __init__.py
│   ├── init_db.sql             # 초기 스키마
│   ├── seed_data.sql           # 샘플 데이터
│   └── ax_project.db           # SQLite 파일 (gitignore)
│
├── models/
│   ├── __init__.py
│   ├── okr.py                  # OKR 모델
│   ├── task.py                 # Task 모델
│   ├── win.py                  # Win 모델
│   └── review.py               # Review 모델
│
├── repositories/
│   ├── __init__.py
│   ├── okr_repository.py
│   ├── task_repository.py
│   ├── win_repository.py
│   └── review_repository.py
│
├── services/
│   ├── __init__.py
│   ├── okr_service.py          # OKR 비즈니스 로직
│   ├── task_service.py         # Task 비즈니스 로직
│   ├── analytics_service.py    # 통계/분석
│   └── ai_service.py           # Claude API 통합
│
├── pages/
│   ├── 1_📊_Dashboard.py
│   ├── 2_🎯_OKR_Management.py
│   ├── 3_📝_Tasks.py
│   ├── 4_💡_Wins.py
│   ├── 5_📅_Weekly_Review.py
│   └── 6_⚙️_Settings.py
│
├── components/
│   ├── __init__.py
│   ├── charts.py               # 재사용 차트 컴포넌트
│   ├── forms.py                # 재사용 폼 컴포넌트
│   └── widgets.py              # 커스텀 위젯
│
├── utils/
│   ├── __init__.py
│   ├── date_utils.py           # 날짜 계산 유틸
│   ├── validators.py           # 입력 검증
│   └── formatters.py           # 데이터 포맷팅
│
└── tests/
    ├── __init__.py
    ├── test_okr_service.py
    ├── test_task_service.py
    └── test_ai_service.py
```

### Extracted Code (markdown)

```markdown
## Week 1: 기반 구축
- [ ] Day 1-2: 프로젝트 셋업
  - 디렉토리 구조 생성
  - requirements.txt 작성
  - DB 스키마 설계 및 생성
  
- [ ] Day 3-4: 데이터 레이어
  - SQLite 연결 설정
  - OKR, Task 모델 정의
  - Repository 패턴 구현
  
- [ ] Day 5: 기본 UI
  - Streamlit 기본 레이아웃
  - 네비게이션 구조

## Week 2: 핵심 기능
- [ ] Day 1-2: OKR 관리
  - OKR CRUD 구현
  - 진척률 계산 로직
  
- [ ] Day 3-4: Task 관리
  - Task CRUD 구현
  - Status 변경 기능
  
- [ ] Day 5: 대시보드 v1
  - 오늘 할 일 표시
  - OKR 현황 표시
  - 기본 차트
```

### Extracted Code (markdown)

```markdown
## Week 3: AI 통합
- [ ] Day 1-2: Claude API 연결
  - AI Service 클래스 구현
  - 인사이트 생성 로직
  
- [ ] Day 3-4: Wins Journal
  - Wins CRUD
  - Timeline 뷰
  
- [ ] Day 5: 테스트 & 리팩토링

## Week 4: 회고 & 고급 기능
- [ ] Day 1-2: 주간 회고
  - 자동 데이터 집계
  - AI 회고 생성
  
- [ ] Day 3-4: 고급 차트
  - Progress Timeline
  - Category 분석
  - Burndown 차트
  
- [ ] Day 5: UX 개선
```

### Extracted Code (markdown)

```markdown
## Week 5: 자동화
- [ ] 알림 시스템 (선택)
- [ ] 데이터 Export (JSON/CSV)
- [ ] 백업 기능

## Week 6: 배포 & 문서화
- [ ] 배포 스크립트
- [ ] 사용자 가이드
- [ ] 비디오 튜토리얼 (선택)
```

### Extracted Code (python)

```python
def generate_insight(
    week_number: int,
    okr_data: dict,
    task_data: dict,
    wins_data: dict
) -> dict:
    """
    주간 데이터를 분석하여 AI 인사이트 생성
    
    Args:
        week_number: 주차 번호
        okr_data: OKR 진척 데이터
        task_data: Task 완료 데이터
        wins_data: Wins 데이터
    
    Returns:
        {
            'strength': '가장 잘하고 있는 점',
            'concern': '주의가 필요한 점',
            'action': '다음 주 액션'
        }
    """
```

### Extracted Code (python)

```python
def suggest_task_breakdown(task_description: str) -> list:
    """
    큰 작업을 작은 서브태스크로 분해 제안
    
    Args:
        task_description: 작업 설명
    
    Returns:
        [
            {'title': 'Subtask 1', 'hours': 2},
            {'title': 'Subtask 2', 'hours': 3}
        ]
    """
```

### Extracted Code (python)

```python
def calculate_status(
    okr_id: int, 
    current_week: int
) -> str:
    """
    OKR 상태 자동 계산
    
    Logic:
    - 진척률이 예상보다 10% 이상 높음 → 'on_track' 🟢
    - 진척률이 예상 ±10% 범위 → 'at_risk' 🟡
    - 진척률이 예상보다 10% 이상 낮음 → 'off_track' 🔴
    
    Returns:
        'on_track' | 'at_risk' | 'off_track'
    """
    target = get_okr_target(okr_id)
    current = get_okr_current(okr_id)
    
    # 프로젝트 시작일부터 현재까지 경과 비율
    elapsed_ratio = (current_week - 1) / 48  # 1년 = 48주
    expected_progress = target * elapsed_ratio
    actual_progress = current
    
    delta = (actual_progress - expected_progress) / target
    
    if delta >= 0.1:
        return 'on_track'
    elif delta >= -0.1:
        return 'at_risk'
    else:
        return 'off_track'
```

### Extracted Code (bash)

```bash
# 1. 레포지토리 클론
git clone https://github.com/yourusername/ax-project-manager.git
cd ax-project-manager

# 2. 가상환경 생성
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. 의존성 설치
pip install -r requirements.txt

# 4. 환경 변수 설정
cp .env.example .env
# .env 파일에 ANTHROPIC_API_KEY 입력

# 5. DB 초기화
python -m database.init_db

# 6. 앱 실행
streamlit run main.py
```

### Extracted Code (markdown)

```markdown
1. GitHub에 코드 푸시
2. https://share.streamlit.io 접속
3. "New app" 클릭
4. Repository 선택
5. Branch: main
6. Main file path: main.py
7. Secrets 설정:
```

### Extracted Code (dockerfile)

```dockerfile
# Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### Extracted Code (markdown)

```markdown
Claude Code에서:

1. 프로젝트 생성
"AX 프로젝트 관리 시스템을 만들고 싶어. 
위 개발 문서의 Phase 1: MVP부터 시작하자.
먼저 프로젝트 구조를 만들어줘."

2. 단계별 개발
"database/init_db.sql 파일을 작성해줘. 
OKRs, Tasks, Wins 테이블이 필요해."

3. 테스트
"main.py에 간단한 대시보드 화면을 만들어줘.
OKR 3개가 표시되고 진척률이 보이면 돼."

4. 디버깅
"OKR 진척률 계산이 안 되는데, 
calculate_status 함수를 확인해줘."
```

### Extracted Code (markdown)

```markdown
## 파일 생성 패턴
"models/okr.py 파일을 만들어줘.
Pydantic 모델로 OKR 클래스를 정의하고,
id, title, target, current, status 필드가 필요해."

## 기능 구현 패턴
"services/okr_service.py에 
create_okr 함수를 추가해줘.
입력 검증과 DB 저장을 포함해서."

## 디버깅 패턴
"이 에러를 봐줘: [에러 메시지]
okr_repository.py의 get_all 함수에서 발생했어."

## 리팩토링 패턴
"task_service.py가 너무 길어졌어.
공통 로직을 utils로 분리할 수 있을까?"
```

### Extracted Code (markdown)

```markdown
## 아침 (30분)
1. 오늘 개발할 기능 선정
2. Claude Code에 "오늘은 [기능]을 만들 거야. 어떻게 시작하면 좋을까?" 물어보기
3. 파일 구조 먼저 생성

## 점심 (1시간)
4. 핵심 로직 구현
5. 간단한 테스트 작성

## 저녁 (30분)
6. UI 연결
7. 실제 데이터로 테스트
8. Git commit

## 주말 회고
9. 이번 주 완성한 기능 정리
10. 다음 주 계획 수립
```

### Extracted Code (python)

```python
import streamlit as st
from config.database import init_database
from services.okr_service import get_all_okrs
from services.task_service import get_today_p0_tasks
from components.charts import render_okr_progress_chart

# 페이지 설정
st.set_page_config(
    page_title="AX 프로젝트 관리",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# DB 초기화 (최초 실행 시)
init_database()

# 사이드바
with st.sidebar:
    st.title("🚀 AX Project")
    st.divider()
    
    # 현재 주차 표시
    current_week = get_current_week()
    st.metric("현재", f"Week {current_week}")
    
    # 빠른 액션
    st.subheader("Quick Actions")
    if st.button("✅ Win 기록"):
        st.switch_page("pages/4_💡_Wins.py")
    if st.button("📝 Task 추가"):
        st.switch_page("pages/3_📝_Tasks.py")

# 메인 대시보드
st.title("🚀 AX 프로젝트 대시보드")

# Today's Focus
st.header("⚡ Today's Focus")
today_tasks = get_today_p0_tasks()

if today_tasks:
    for task in today_tasks:
        col1, col2 = st.columns([0.1, 0.9])
        with col1:
            done = st.checkbox("", key=f"task_{task.id}")
            if done:
                complete_task(task.id)
                st.rerun()
        with col2:
            st.markdown(f"**{task.title}** ({task.category})")
else:
    st.info("오늘 할 P0 작업이 없습니다!")

# OKR 스코어보드
st.header("📊 3-OKR 스코어보드")

okrs = get_all_okrs()
okr_data = []

for okr in okrs:
    progress = (okr.current_value / okr.target_value) * 100
    status = get_status_emoji(okr.status)
    
    okr_data.append({
        "OKR": okr.title[:20],
        "목표": okr.target_value,
        "현재": okr.current_value,
        "진척": f"{progress:.0f}%",
        "상태": status
    })

st.dataframe(
    okr_data,
    use_container_width=True,
    hide_index=True
)

# Progress Chart
st.plotly_chart(
    render_okr_progress_chart(okrs),
    use_container_width=True
)

# 최근 Wins
st.header("💡 최근 Wins")
recent_wins = get_recent_wins(limit=3)

for win in recent_wins:
    with st.expander(f"{win.impact} {win.title}"):
        st.caption(win.date.strftime("%Y-%m-%d"))
        st.write(win.content)
```

### Extracted Code (python)

```python
import anthropic
import os
from typing import Dict

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def generate_weekly_insights(week_data: Dict) -> Dict:
    """주간 데이터로 AI 인사이트 생성"""
    
    prompt = f"""
당신은 프로젝트 관리 전문가입니다.

# 이번 주 데이터 (Week {week_data['week_number']})
- 완료한 작업: {week_data['completed_tasks']}개
- OKR 1 진척: {week_data['okr1_progress']}%
- OKR 2 진척: {week_data['okr2_progress']}%
- OKR 3 진척: {week_data['okr3_progress']}%
- 총 작업 시간: {week_data['total_hours']}시간
- 기록한 Wins: {week_data['wins_count']}개

다음 3가지를 각각 한 문장으로 작성하세요:
1. 가장 잘하고 있는 점
2. 주의가 필요한 점
3. 다음 주 구체적 액션

JSON 형식으로 응답하세요:
{{"strength": "...", "concern": "...", "action": "..."}}
"""
    
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=300,
        messages=[{"role": "user", "content": prompt}]
    )
    
    # JSON 파싱
    import json
    insight = json.loads(response.content[0].text)
    
    return insight
```

### Extracted Code (python)

```python
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def render_okr_progress_chart(okrs):
    """OKR 진척률 차트"""
    
    fig = go.Figure()
    
    categories = []
    current_values = []
    target_values = []
    
    for okr in okrs:
        categories.append(okr.title[:15])
        current_values.append(okr.current_value)
        target_values.append(okr.target_value)
    
    # 현재값
    fig.add_trace(go.Bar(
        name='현재',
        x=categories,
        y=current_values,
        marker_color='lightblue'
    ))
    
    # 목표값
    fig.add_trace(go.Bar(
        name='목표',
        x=categories,
        y=target_values,
        marker_color='lightgray',
        opacity=0.5
    ))
    
    fig.update_layout(
        title="OKR 진척 현황",
        barmode='overlay',
        height=400
    )
    
    return fig
```

### Extracted Code (bash)

```bash
# 1. 이 문서를 Claude Code에 공유
"이 개발 문서를 기반으로 프로젝트를 시작하고 싶어.
먼저 파일 구조부터 만들어줄래?"

# 2. Phase 1 시작
"Phase 1의 Week 1, Day 1-2 작업을 시작하자.
프로젝트 셋업을 도와줘."

# 3. 첫 화면 보기
"대시보드 기본 레이아웃을 만들어줘.
일단 더미 데이터로 화면만 나오게 해줘."
```

### Extracted Code (bash)

```bash
# Claude API
ANTHROPIC_API_KEY=your-api-key-here

# Database
DATABASE_PATH=database/ax_project.db

# Project Settings
PROJECT_START_DATE=2026-02-03
PROJECT_END_DATE=2026-12-31
WORK_HOURS_PER_WEEK=40

# Features
ENABLE_AI_INSIGHTS=true
ENABLE_NOTIFICATIONS=false
```

### Extracted Code (text)

```text
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/

# Database
*.db
*.sqlite

# Secrets
.env
.env.local

# IDE
.vscode/
.idea/
*.swp

# OS
.DS_Store
Thumbs.db
```

### Extracted Code (sql)

```sql
-- OKR 샘플
INSERT INTO okrs (title, category, target_value, unit, quarter, status) VALUES
('Vibe Coding MVP 5건 개발', 'vibe_coding', 5, '건', 'Q1,Q2', 'on_track'),
('Physical AI Leader Pool 30명', 'physical_ai', 30, '명', 'Q2,Q3', 'at_risk'),
('AX 성숙도 15% 향상', 'ax_maturity', 15, '%', 'ALL', 'off_track');

-- Task 샘플
INSERT INTO tasks (okr_id, title, category, priority, status, due_date) VALUES
(1, 'Cursor 플랫폼 테스트', 'vibe_coding', 'P0', 'in_progress', '2026-02-14'),
(2, 'Physical AI 후보 10명 선발', 'physical_ai', 'P0', 'backlog', '2026-02-28'),
(3, 'AX 성숙도 Survey 실시', 'ax_maturity', 'P1', 'done', '2026-02-07');
```

### Extracted Code (python)

```python
# 이게 전부다
okr_data = get_all_okrs()
st.dataframe(okr_data)
st.plotly_chart(render_progress_chart(okr_data))
```
