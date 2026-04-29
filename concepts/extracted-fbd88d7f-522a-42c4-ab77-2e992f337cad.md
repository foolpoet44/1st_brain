# Extracted Knowledge from Conv: fbd88d7f-522a-42c4-ab77-2e992f337cad

**Date**: 2025-12-20T21:47:29.180662Z

### Extracted Code (bash)

```bash
# BMAD Method 설치
npx bmad-method@alpha install  # v6 알파 버전 (권장)
# 또는
npx bmad-method install  # 안정 버전
```

### Extracted Code (text)

```text
1. Analyst 에이전트 (*analyst 명령)
   → 프로젝트 브리프 생성 (10-15페이지)
   → 시장 분석, 사용자 페르소나, 경쟁사 분석 포함

2. PM 에이전트 (*pm 명령)
   → 브리프를 상세한 PRD로 변환
   → 기능 요구사항, 비기능 요구사항, Epic, Story 정의

3. Architect 에이전트
   → 시스템 아키텍처 설계
   → 기술 스택, 데이터베이스 스키마, API 명세

4. Scrum Master 에이전트
   → Epic을 상세한 개발 스토리로 분할

5. Developer 에이전트
   → 한 번에 하나의 스토리 구현
   → 전체 컨텍스트와 명확한 수락 기준 보유

6. QA 에이전트
   → 코드 리뷰, 품질 리팩토링, 테스트 통과 확인
```

### Extracted Code (text)

```text
50페이지 PRD 대신:
├─ Epic 1 스토리들
├─ Epic 2 스토리들
└─ Epic 3 스토리들

각 샤드 = 집중된 컨텍스트
→ AI 환각 방지
→ 프로젝트 전반 일관성 유지
```

### Extracted Code (text)

```text
월요일: "할 일 관리 앱 만들어줘" 🚀
화요일: "음... 인증 방식 바꿔줘" 🤔
수요일: "DB 구조 다시 설계해줘" 😰
목요일: "프론트엔드가 백엔드랑 안 맞는데?" 😵
금요일: "처음부터 다시..." 💀
```

### Extracted Code (bash)

```bash
# 프로젝트 폴더 생성
mkdir my-saas-idea
cd my-saas-idea

# BMAD Method 설치
npx bmad-method@alpha install

# 또는 Claude Code 전용 버전
git clone https://github.com/24601/BMAD-AT-CLAUDE
npm run install:bmad
```

### Extracted Code (text)

```text
*analyst

나는 1인 개발자로 SaaS 사업을 시작하려고 합니다.
관심 분야:
- AI 활용 자동화 도구
- 중소기업/프리랜서 타겟
- 월 구독 모델 ($29-99)
- 3개월 내 MVP 출시

시장 조사와 아이템 추천을 해주세요.
```

### Extracted Code (text)

```text
*pm

Project Brief를 기반으로 PRD를 작성해주세요.

핵심 기능:
1. 블로그 글 분석 (SEO 점수, 가독성)
2. AI 개선 제안 (제목, 메타 설명, 키워드)
3. 경쟁사 키워드 분석
4. 월 50개 글 분석 ($29/월)

기술 스택 선호:
- Next.js (프론트엔드)
- Supabase (백엔드/DB/인증)
- Claude API (AI 분석)
- Vercel (배포)
```

### Extracted Code (text)

```text
docs/planning/
├── prd.md (Product Requirements Document)
│   ├── Executive Summary
│   ├── User Stories
│   ├── Functional Requirements (FR-001 ~ FR-020)
│   ├── Non-Functional Requirements
│   ├── Success Metrics (MRR, User Acquisition)
│   └── Go-to-Market Strategy
└── epics/
    ├── epic-1-user-auth.md
    ├── epic-2-content-analysis.md
    ├── epic-3-ai-suggestions.md
    └── epic-4-payment-billing.md
```

### Extracted Code (text)

```text
*architect

PRD를 기반으로 시스템 아키텍처를 설계해주세요.

제약사항:
- 1인 개발자 운영 가능한 구조
- 월 운영비 $50 이하
- Auto-scaling 가능
- 보안 우선 (API 키 관리, 사용자 데이터)
```

### Extracted Code (text)

```text
docs/planning/architecture.md
├── System Overview (다이어그램)
├── Technology Stack
│   ├── Frontend: Next.js 14 (App Router)
│   ├── Backend: Next.js API Routes
│   ├── Database: Supabase PostgreSQL
│   ├── Auth: Supabase Auth
│   ├── AI: Anthropic Claude API
│   ├── Payment: Stripe
│   └── Hosting: Vercel
├── Database Schema
│   ├── users
│   ├── subscriptions
│   ├── content_analyses
│   └── api_usage_logs
├── API Design
│   ├── POST /api/analyze
│   ├── GET /api/history
│   └── POST /api/subscribe
├── Security Considerations
└── Scalability Plan
```

### Extracted Code (bash)

```bash
# Scrum Master가 Epic을 스토리로 분할
*sm shard-epic epic-1-user-auth.md

생성된 스토리:
docs/stories/
├── story-1.1-setup-supabase.md
├── story-1.2-signup-flow.md
├── story-1.3-login-flow.md
└── story-1.4-protected-routes.md
```

### Extracted Code (bash)

```bash
# Claude Code에서
*dev implement story-1.1-setup-supabase.md

# 생성되는 것:
1. Supabase 프로젝트 셋업 가이드
2. 환경 변수 설정 (.env.example)
3. 데이터베이스 마이그레이션 파일
4. 인증 헬퍼 함수
5. 테스트 코드
```

### Extracted Code (text)

```text
Day 1-2:   Analyst - 3개 아이템 도출
Day 3-4:   간단한 랜딩 페이지로 시장 반응 테스트
Day 5-7:   최종 아이템 선정, PM으로 PRD 작성
Day 8-10:  Architect로 기술 스택 확정
```

### Extracted Code (text)

```text
Week 3:  Epic 1 (인증) + Epic 2 (핵심 기능 1개)
Week 4:  Epic 3 (결제) + 배포
Week 5:  베타 테스터 모집 및 피드백
Week 6:  개선 및 정식 런칭
```

### Extracted Code (text)

```text
1. Architect가 이미 DB 스키마 정의 완료
2. Story 파일에 모든 컨텍스트 포함:
   - 기능 설명
   - 관련 아키텍처 섹션
   - API 명세
   - 수락 기준
   - 테스트 시나리오
3. Dev 에이전트가 Story 열면 → 즉시 이해하고 구현
```

### Extracted Code (bash)

```bash
# 1. 설치 (5분)
mkdir my-saas
cd my-saas
npx bmad-method@alpha install

# 2. Web UI에서 기획 (2-3시간)
# claude.ai에 team-fullstack.txt 업로드
*analyst
"1인 개발자가 3개월 내 런칭 가능한 
 AI 기반 SaaS 아이템 3개 추천해주세요.
 
 제약사항:
 - 초기 개발비 $0
 - 월 운영비 $50 이하  
 - 타겟: 중소기업/프리랜서
 - 가격대: $29-99/월"

# 3. PRD 작성 (2-3시간)
*pm
# Analyst 브리프 기반으로 PRD 생성

# 4. 아키텍처 (1-2시간)
*architect
# 1인 운영 가능한 스택 설계

# 5. Claude Code로 개발 (2-3주)
*sm shard-epic epic-1
*dev implement story-1.1
*qa review story-1.1
```

### Extracted Code (text)

```text
*analyst

저는 10년 경력의 HR 전문가입니다. 1인 개발자로 HR Tech SaaS를 만들려고 합니다.

== 배경 ==
현재 대부분의 기업들은:
- 역량 평가를 엑셀이나 레거시 HCM 시스템으로 관리
- 고성과자 육성이 감에 의존 (데이터 기반 아님)
- 개인별 성장 경로가 불명확
- 이직률 예측 실패로 인재 손실

== 제품 아이디어 ==
"TalentPredict" - AI 기반 개인별 역량 프로파일 & 고성과자 성장 예측 플랫폼

핵심 기능:
1. 개인별 역량 프로파일 자동 구축
   - 다면평가, 성과데이터, 역량평가 통합
   - AI 분석으로 강점/약점 시각화
   
2. 고성과자 성장 확률 분석
   - 기존 고성과자 데이터 패턴 학습
   - 개인별 고성과자 도달 확률 예측
   - 성장 저해 요인 식별

3. 맞춤형 육성 계획 자동 생성
   - AI 기반 교육/경험 추천
   - 경력 경로 시뮬레이션

== 타겟 고객 ==
- 1차: 중견기업 (100-500명) HR 팀
- 2차: 스타트업 People Team
- 3차: HR 컨설턴트

== 제약사항 ==
- 1인 개발/운영 가능해야 함
- 3개월 내 MVP 출시
- 초기 개발비 최소화
- 데이터 보안/프라이버시 필수
- 월 운영비 $100 이하

== 비즈니스 모델 ==
- B2B SaaS 구독
- 예상 가격: $199-499/월 (기업당)
- 또는 사용자당 $29/월

다음을 분석해주세요:
1. 시장 규모 및 성장성 (HR Tech, People Analytics)
2. 경쟁사 분석 (Culture Amp, Lattice, 15Five, Eightfold AI)
3. 차별화 포인트
4. Go-to-Market 전략
5. 3개월 MVP 범위 추천
6. 리스크 및 대응 방안
7. 수익화 시나리오 (낙관/보통/비관)
```

### Extracted Code (text)

```text
docs/planning/project-brief.md
├── Executive Summary
├── Market Analysis
│   ├── TAM: $8.8B (HR Tech Market 2025)
│   ├── SAM: $1.2B (People Analytics)
│   └── SOM: $2M (First Year Target)
├── Competitive Landscape
│   ├── Culture Amp ($500-2000/월) - 종합 플랫폼, 복잡함
│   ├── Lattice ($11/user/월) - 성과관리 중심
│   ├── 15Five ($4-16/user/월) - 1on1 & OKR
│   └── Eightfold AI (Enterprise) - AI 채용, 비쌈
├── Differentiation Strategy
│   ✅ HR 전문가가 만든 실전 중심 UX
│   ✅ 중견기업 특화 (대기업 도구는 과함, 소기업용은 부족함)
│   ✅ AI 예측에 설명 가능성 강조 (HR팀이 신뢰할 수 있게)
│   ✅ 합리적 가격 ($199/월 vs $2000/월)
└── Recommended MVP Scope
    ✅ 역량 프로파일 생성 (수동 입력)
    ✅ 기본 시각화 대시보드
    ✅ 간단한 성장 확률 점수 (룰 기반)
    ✅ 5개 기업 파일럿 목표
    ❌ 고급 AI 예측 (Phase 2)
    ❌ HCM 시스템 연동 (Phase 2)
```

### Extracted Code (text)

```text
*pm

Project Brief를 기반으로 상세 PRD를 작성해주세요.

== MVP 기능 우선순위 ==

P0 (필수 - 3개월 내):
1. 관리자 대시보드
   - 팀원 목록 및 기본 정보
   - 역량 프로파일 등록 UI

2. 역량 프로파일 시스템
   - 역량 항목 템플릿 (리더십, 전문성, 협업 등)
   - 5점 척도 평가 입력
   - 레이더 차트 시각화
   - PDF 리포트 생성

3. 성장 확률 분석 (v1 - 룰 기반)
   - 역량 점수 기반 간단한 알고리즘
   - 고성과자 기준선 설정
   - 개인별 성장 확률 점수 (0-100%)
   - 개선 영역 자동 추천

4. 팀 분석 대시보드
   - 팀 평균 역량 프로파일
   - 성장 확률 분포
   - 육성 우선순위 리스트

P1 (Phase 2 - 6개월):
- AI 기반 예측 모델 (고성과자 데이터 학습)
- 개인별 육성 계획 자동 생성
- 경력 경로 시뮬레이션

P2 (Phase 3 - 12개월):
- HCM 시스템 연동 (SAP, Workday)
- 조직 네트워크 분석
- 이직 위험 예측

== 비기능 요구사항 ==
- 보안: 개인정보 암호화, GDPR 준수
- 성능: 100명 데이터 3초 내 로딩
- 확장성: 500명까지 지원
- 사용성: HR 담당자 5분 내 온보딩

== 성공 지표 ==
- 3개월: 5개 파일럿 고객
- 6개월: 20개 유료 고객
- 12개월: MRR $5,000 ($250/고객 x 20개)
```

### Extracted Code (text)

```text
docs/planning/
├── prd.md (50-70페이지)
│   ├── User Personas
│   │   ├── Primary: HR Manager (Julie, 35세)
│   │   ├── Secondary: People & Culture Lead
│   │   └── End User: 팀원 (셀프서비스)
│   ├── User Stories
│   │   ├── US-001: 관리자가 팀원 프로파일을 등록한다
│   │   ├── US-002: 관리자가 역량을 평가한다
│   │   ├── US-003: 시스템이 성장 확률을 계산한다
│   │   └── ...
│   ├── Functional Requirements
│   │   ├── FR-001: 역량 항목 템플릿 관리
│   │   ├── FR-002: 다면평가 입력 인터페이스
│   │   ├── FR-003: 레이더 차트 생성
│   │   └── ...
│   └── Go-to-Market Strategy
│       ├── 파일럿 고객 모집 (HR 커뮤니티)
│       ├── 무료 평가 리포트 제공 (리드 생성)
│       └── HR 컨퍼런스 부스
└── epics/
    ├── epic-1-auth-tenant.md (멀티테넌트 인증)
    ├── epic-2-profile-system.md (역량 프로파일)
    ├── epic-3-scoring-algorithm.md (점수 알고리즘)
    ├── epic-4-dashboard.md (대시보드)
    └── epic-5-reporting.md (리포트)
```

### Extracted Code (text)

```text
*architect

PRD를 기반으로 시스템 아키텍처를 설계해주세요.

== 기술 스택 선호 ==
- 프론트엔드: Next.js 14 (TypeScript)
- 백엔드: Next.js API Routes
- 데이터베이스: PostgreSQL (Supabase 또는 Neon)
- 인증: Supabase Auth (멀티테넌트)
- AI/ML: Claude API (초기), Python/FastAPI (향후)
- 차트: Recharts 또는 Chart.js
- PDF: jsPDF 또는 Puppeteer
- 배포: Vercel
- 결제: Stripe

== 데이터 모델 중요 고려사항 ==
1. 멀티테넌트 (회사별 데이터 격리)
2. 역량 프레임워크 유연성 (회사마다 다름)
3. 평가 이력 추적 (시계열 분석용)
4. GDPR 대응 (데이터 삭제 요청)

== 보안 요구사항 ==
- 역할 기반 접근 제어 (RBAC)
- 개인정보 암호화
- 감사 로그
- API Rate Limiting
```

### Extracted Code (text)

```text
docs/planning/architecture.md
├── System Architecture
│   ├── Multi-Tenant SaaS Pattern
│   ├── API Gateway Structure
│   └── Database Isolation Strategy
├── Database Schema
│   ├── tenants (회사)
│   ├── users (사용자)
│   ├── employees (직원 프로파일)
│   ├── competency_frameworks (역량 프레임워크)
│   ├── competency_items (역량 항목)
│   ├── assessments (평가)
│   ├── assessment_scores (평가 점수)
│   ├── growth_predictions (성장 예측)
│   └── audit_logs (감사 로그)
├── API Design
│   ├── POST /api/v1/employees
│   ├── POST /api/v1/assessments
│   ├── GET /api/v1/analytics/growth-probability
│   ├── GET /api/v1/reports/profile/:employeeId
│   └── ...
├── Security Architecture
│   ├── Row-Level Security (RLS) - Supabase
│   ├── JWT Token Management
│   ├── Data Encryption at Rest
│   └── GDPR Compliance Checklist
└── Scalability Plan
    ├── Database Indexing Strategy
    ├── Caching Layer (Redis - Phase 2)
    └── CDN for Reports
```

### Extracted Code (bash)

```bash
*sm shard-epic epic-2-profile-system.md

# 생성되는 스토리들:
docs/stories/
├── story-2.1-competency-framework-crud.md
├── story-2.2-employee-profile-page.md
├── story-2.3-assessment-input-form.md
├── story-2.4-radar-chart-visualization.md
└── story-2.5-profile-pdf-export.md
```

### Extracted Code (markdown)

```markdown
# Story 2.4: 역량 프로파일 레이더 차트 시각화

## Context
사용자는 직원의 역량을 한눈에 파악하기 위해 레이더 차트가 필요합니다.
다면평가 결과를 5-8개 역량 축으로 시각화합니다.

## Architecture Reference
- Component: ProfileVisualization
- Database: assessments, assessment_scores
- API: GET /api/v1/employees/:id/competency-profile

## Acceptance Criteria
✅ 5-8개 역량 축을 레이더 차트로 표시
✅ 평균 대비 개인 점수 오버레이
✅ 호버 시 상세 점수 툴팁
✅ 반응형 디자인 (모바일 대응)
✅ 차트 이미지 다운로드 기능

## Technical Details
- Library: Recharts (radarChart)
- Data format: { subject: string, A: number, fullMark: number }[]
- Colors: 개인(#3b82f6), 평균(#94a3b8)

## Test Scenarios
1. 역량 5개 데이터로 차트 렌더링
2. 데이터 없을 때 placeholder
3. 모바일 화면 (375px) 레이아웃 테스트
```

### Extracted Code (text)

```text
*qa review story-2.4

체크리스트:
✅ TypeScript 타입 안전성
✅ 접근성 (ARIA labels)
✅ 에러 처리 (API 실패 시)
✅ 로딩 상태 표시
✅ 성능 (100개 데이터 포인트 테스트)
✅ 브라우저 호환성
```

### Extracted Code (text)

```text
✅ Day 1-2:   Analyst - 시장 분석, 경쟁사 리서치
✅ Day 3-5:   PM - PRD 작성 (50페이지)
✅ Day 6-7:   Architect - 시스템 설계
✅ Day 8-10:  파일럿 고객 3-5개 확보 (사전 인터뷰)
✅ Day 11-14: 와이어프레임, DB 스키마 확정
```

### Extracted Code (text)

```text
Sprint 1:
├── Story 1.1: Next.js 프로젝트 셋업
├── Story 1.2: Supabase 연동 (DB + Auth)
├── Story 1.3: 멀티테넌트 구조
├── Story 1.4: 회원가입/로그인
└── Story 1.5: 기본 대시보드 레이아웃

배포: Vercel (Staging)
```

### Extracted Code (text)

```text
Sprint 2:
├── Story 2.1: 역량 프레임워크 CRUD
├── Story 2.2: 직원 프로파일 등록
├── Story 2.3: 평가 입력 폼
├── Story 2.4: 레이더 차트 시각화
└── Story 2.5: PDF 리포트 생성

파일럿 고객 1차 데모
```

### Extracted Code (text)

```text
Sprint 3:
├── Story 3.1: 점수 계산 알고리즘
├── Story 3.2: 성장 확률 스코어링
├── Story 3.3: 개선 영역 추천 로직
├── Story 3.4: 팀 분석 대시보드
└── Story 3.5: 육성 우선순위 리스트

파일럿 고객 피드백 수집
```

### Extracted Code (text)

```text
Sprint 4:
├── Story 4.1: Stripe 연동
├── Story 4.2: 구독 플랜 페이지
├── Story 4.3: UI/UX 개선 (피드백 반영)
├── Story 4.4: 온보딩 튜토리얼
└── Story 4.5: 이메일 알림

베타 테스트 시작
```

### Extracted Code (text)

```text
Sprint 5:
├── Story 5.1: 보안 감사
├── Story 5.2: 성능 최적화
├── Story 5.3: SEO & 랜딩 페이지
├── Story 5.4: 헬프 센터/문서
└── Story 5.5: 런칭 이벤트

✨ 정식 런칭!
```

### Extracted Code (text)

```text
일반 개발자가 만든 제품:
- "역량 평가" 기능
- 복잡한 설정
- HR 용어 오류

당신이 만든 제품:
- "리더십 역량 다면평가 (360도)"
- HR 담당자가 3분 내 이해
- 실무에 바로 쓸 수 있는 템플릿
```

### Extracted Code (text)

```text
예시:
- "고성과자 정의"가 회사마다 다름
  → 커스터마이징 가능한 기준선

- 평가 시즌에 엑셀 지옥
  → 벌크 업로드, 자동 계산

- 임원 보고용 차트 만들기 힘듦
  → 원클릭 PPT 템플릿
```

### Extracted Code (text)

```text
당신의 네트워크:
- 기존 고객사 HR 팀
- HR 커뮤니티 (SHRM, 한국HRD협회)
- LinkedIn HR 그룹

첫 3개월 전략:
- 5개 파일럿 고객 (무료/할인)
- 주간 피드백 세션
- 추천 인센티브 (1개월 무료)
```

### Extracted Code (text)

```text
도메인: $12/년
Vercel Pro: $20/월 x 3 = $60
Supabase Pro: $25/월 x 3 = $75
Claude API: ~$50 (개발용)
Stripe: $0 (거래 시작 전)
-----------------------
총: ~$200
```

### Extracted Code (text)

```text
Vercel Pro: $20
Supabase Pro: $25 (500명까지)
Claude API: $50 (20개 고객 기준)
기타 (이메일 등): $10
-----------------------
총: ~$105/월
```

### Extracted Code (text)

```text
보수적 (6개월):
- 10개 기업 x $199/월 = $1,990/월
- MRR: $1,990
- 순이익: $1,885/월
- Break-even: 1개월 차

낙관적 (12개월):
- 30개 기업 x $299/월 = $8,970/월
- MRR: $8,970
- 순이익: $8,865/월
- 연 매출: ~$107K
```

### Extracted Code (bash)

```bash
1. BMAD 설치 (10분)
mkdir talentpredict
cd talentpredict
npx bmad-method@alpha install

2. Claude.ai에서 Analyst 실행 (2시간)
# 위의 프롬프트 사용

3. HR 커뮤니티에 아이디어 검증 (1시간)
LinkedIn 게시글:
"HR 동료분들께 질문드립니다. 
AI 기반 역량 프로파일 & 성장 예측 도구가 있다면 
월 얼마 정도가 적정할까요?"
```
