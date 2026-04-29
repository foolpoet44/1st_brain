# Extracted Knowledge from Conv: 5af22ccf-f9b9-470e-a6da-da58ca67fd14

**Date**: 2026-01-26T04:12:51.037340Z

### Extracted Code (text)

```text
✨ 전체 672개 문제 통합 완료!

📋 포함 시트:
  • 통합_문제은행_마스터 (전체 문제)
  • 대영역별_통계 (집계 데이터)

📈 통계:
  • 데이터 분석: 380문제 (56.5%)
  • DX 기초: 162문제 (24.1%)
  • 과제 실행: 117문제 (17.4%)
  • 신규추가: 13문제 (1.9%)

📊 난이도 분포:
  • 중: 309문제 (46.0%)
  • 하: 217문제 (32.3%)
  • 상: 146문제 (21.7%)

🎯 출제 현황:
  • 출제: 375문제 (55.8%)
  • 미출제: 297문제 (44.2%)
```

### Extracted Code (text)

```text
✅ 단일 마스터 시트 (32개 표준 컬럼)
✅ 메타데이터 명시화 (대영역, 중영역, 모듈코드)
✅ 전체 검색 가능
✅ 실시간 통계 집계
✅ 문제ID 기반 중복 방지
✅ 무한 확장 가능
✅ DB 전환 준비 완료
```

### Extracted Code (text)

```text
A. 식별자 (2개)
   - 문제ID, 순번

B. 분류/메타데이터 (6개)
   - 대영역, 중영역, 소영역, 모듈코드, 출처, 키워드

C. 문제 핵심 (6개)
   - 문제유형, 문제, 정답, 해설, 난이도, 학습목표

D. 출제 관리 (7개)
   - 출제여부, 출제연도, 출제월, 출제회차, 출제빈도, 최종출제일, Pick여부

E. 품질 관리 (4개)
   - 검토상태, 최종의견, 정답률, 변별도

F. 이력 관리 (7개)
   - 작성일, 작성자, 최종수정일, 최종수정자, 수정이력, 버전, 활성화여부
```

### Extracted Code (text)

```text
Excel:  138 KB  ← 기준선
JSON:   420-514 KB  (3-4배 증가)

이유:
• Excel: 이진 압축 + 중복 제거
• JSON: 평문 텍스트 + 키 반복
```

### Extracted Code (text)

```text
✅ Excel 유지
   → 피벗 테이블, 필터 활용
   → 실무자 직접 관리 가능
   → 조건부 서식, 검증 규칙

❌ JSON 전환 불필요
   → 파일만 커짐 (3배)
   → 추가 개발 필요
   → 유지보수 복잡
```

### Extracted Code (text)

```text
✅ Excel + JSON 하이브리드
   Excel (Master) → JSON 자동 변환 → 웹앱 배포
   
   빌드 파이프라인:
   1. Excel 읽기
   2. JSON 변환 (계층적 구조)
   3. 웹앱에 embed
   4. 캐싱 (성능)
```

### Extracted Code (text)

```text
✅ PostgreSQL + Redis + JSON
   
   DB (Master) → Redis (캐시) → JSON (API export)
   
   장점:
   • 대규모 트래픽 대응
   • 복잡한 쿼리 지원
   • 실시간 업데이트
   • API 표준화
```

### Extracted Code (text)

```text
1. Storage (저장): Excel / DB
   → 압축, 효율, 백업

2. Processing (처리): Python / SQL
   → 변환, 분석, 검증

3. Presentation (표현): JSON / HTML
   → 전송, 렌더링, 상호작용
```

### Extracted Code (text)

```text
[Master Data]
Excel (문제은행_통합_최종결과_v2.xlsx)
  • 실무자가 직접 관리
  • 피벗 테이블, 필터 활용
  • 조건부 서식
  ↓
[Production Database]  
SQLite (question_bank.db)
  • 시험지 자동 생성 엔진
  • 출제 이력 자동 관리
  • Python 완벽 연동
  ↓
[Output]
HTML/PDF 시험지
  • 문제지 + 정답지
  • A형, B형, C형 자동 생성
  • 5분 만에 완성
```

### Extracted Code (bash)

```bash
python generate_exam_complete.py \
  --name "2025년 1차 인증제 시험" \
  --date "2025-03-15" \
  --template 기본시험
```

### Extracted Code (bash)

```bash
python generate_exam_complete.py \
  --name "2025년 1차 인증제 시험" \
  --date "2025-03-15" \
  --template 기본시험 \
  --count 3
```

### Extracted Code (python)

```python
# 1. 템플릿 한 번만 정의
EXAM_TEMPLATES = {
    "기본시험": [...],
    "심화시험": [...],
    "입문시험": [...]
}

# 2. 이후 무한 반복 사용
for exam_type in ['기본', '심화', '입문']:
    for version in ['A', 'B', 'C']:
        generate_exam(template=exam_type, version=version)
        # → 9개 시험지가 5분 만에 생성!
```

### Extracted Code (sql)

```sql
-- 향후 추가 가능: 스킬-문제 매핑
CREATE TABLE skill_mappings (
    문제ID TEXT,
    스킬ID TEXT,
    중요도 INTEGER
);

-- 학습경로 기반 시험 생성
SELECT q.* FROM questions q
JOIN skill_mappings sm ON q.문제ID = sm.문제ID
WHERE sm.스킬ID IN ('Python', '데이터분석', '통계')
ORDER BY sm.중요도 DESC, RANDOM();
```

### Extracted Code (text)

```text
Year 1 (현재): SQLite + Python → 시험지 자동 생성 ✅
Year 2: PostgreSQL + FastAPI → 웹 기반 시험 시스템
Year 3: AI 기반 적응형 시험 → 개인 맞춤 난이도
Year 4: 멀티테넌시 SaaS → 다기업 서비스
```

### Extracted Code (bash)

```bash
# 1. 샘플 HTML 파일 열어보기
# sample_question_paper.html을 브라우저로 열기

# 2. 실제 시험지 생성해보기
python generate_exam_complete.py \
  --name "테스트 시험" \
  --date "2025-02-01" \
  --template 입문시험
```

### Extracted Code (text)

```text
1. Executive Summary ────────── 핵심 요약
2. Vision & Philosophy ──────── CSP님의 철학 반영
3. Problem Statement ────────── 해결할 문제
4. Goals & Success Metrics ──── 목표와 측정 지표
5. User Personas ────────────── 사용자 페르소나
6. User Stories & Use Cases ─── 사용자 스토리
7. Functional Requirements ──── 기능 요구사항
8. Non-Functional Requirements  성능/보안 요구사항
9. Technical Architecture ───── 기술 아키텍처
10. Data Model & Schema ──────── 데이터 모델
11. System Components ────────── 시스템 컴포넌트
12. UI/UX ───────────────────── 사용자 인터페이스
13. Security & Compliance ────── 보안과 규정 준수
14. Testing Strategy ─────────── 테스트 전략
15. Deployment & Operations ──── 배포와 운영
16. Roadmap & Milestones ──────── 로드맵 (3단계)
17. Risks & Mitigation ────────── 리스크 관리
18. Appendix ─────────────────── 부록
```

### Extracted Code (text)

```text
Phase 1: MVP (2개월)
  └─ CLI 도구 + SQLite
  └─ 로컬 실행
  └─ 5분/시험

Phase 2: 웹 UI (3개월)
  └─ Streamlit 대시보드
  └─ PostgreSQL
  └─ 10명 동시 사용

Phase 3: SaaS (6개월)
  └─ 클라우드 배포
  └─ 멀티테넌시
  └─ 100+ 사용자
```

### Extracted Code (sql)

```sql
-- 4개 테이블 ERD
questions ──1:N── exam_questions ──N:1── exam_papers
                        │
                       1:N
                        │
                  exam_history
```

### Extracted Code (markdown)

```markdown
# Sprint 1 (Week 1-2): 데이터 모델

## Goals
- SQLite 스키마 생성
- Excel → SQLite 동기화

## Tasks (from PRD Section 10)
- [ ] questions 테이블 생성
- [ ] exam_papers 테이블 생성
- [ ] exam_questions 테이블 생성
- [ ] exam_history 테이블 생성
- [ ] 인덱스 생성
- [ ] 동기화 스크립트

## Acceptance Criteria (from PRD Section 4)
- ✅ 672개 문제 마이그레이션
- ✅ 데이터 검증 통과
- ✅ 쿼리 성능 < 1초
```

### Extracted Code (markdown)

```markdown
# Technical Review Meeting

## Agenda (based on PRD)

1. Architecture Review (Section 9)
   - 현재 구조 vs PRD 설계
   - 변경 사항 논의

2. Performance (Section 8)
   - 응답 시간 측정
   - 목표: 5초 이내
   - 현재: 3초 ✅

3. Risks (Section 17)
   - R1 데이터 품질: 해결 ✅
   - R2 성능: 모니터링 중
   - R4 사용자 채택: 교육 진행 중
```
