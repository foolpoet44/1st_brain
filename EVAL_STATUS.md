---
type: Note
status: Active
---

# [[EVAL_STATUS.md|EVAL_STATUS]]

*최종 업데이트: 2026-07-27 00:15*
*Vault 경로: `/Users/dkmac/Desktop/@26/dev`*

---

## 📊 주요 지표 분석

### 1️⃣ EVAL SCORE: 16.7 / 100 🟡
- **상태**: "분류 작업 진행 중"
- **해석**: 전체 2,120 개 문서 중 353 개 (16.7%) 가 type 필드 할당됨
- **개선 진행**: 2 배치 (50 개) 문서 자동 분류 완료
- **잔여 작업**: 1,767 개 문서 (83.3%)
- **목표**: 80 점 (1,696 개 문서 분류 필요)

### 2️⃣ TOTAL DOCUMENTS: 2,120 개
| 분류 | 수량 | 비율 | 증감 |
|------|------|------|------|
| **Type 문서** | 10 개 | 0.5% | - |
| **type 할당됨** | 353 개 | 16.7% | +51 ✅ |
| **미분류** | 1,767 개 | 83.3% | -51 |
| **Active (최근 7 일)** | 57 개 | 2.7% | - |

### 3️⃣ 현재 등록된 Type 문서 (10 종)
- ✅ Concept.md
- ✅ Decision.md
- ✅ Idea.md
- ✅ Meeting.md
- ✅ Note.md
- ✅ Person.md
- ✅ Project.md
- ✅ Reflection.md
- ✅ Resource.md
- ✅ Task.md

---

## 🎯 자동화 현황

### ✅ 완료된 작업
1. **Type 문서 10 종 생성** - 분류 체계의 기초 완성
2. **자동 분류 스크립트 개발** - `scripts/auto-classify-types.sh`
3. **스킬 박제** - `csp-brain-type-auto-classifier`
4. **Cronjob 설정** - 매일 새벽 4 시 자동 실행 (Job ID: `ab1915821586`)
5. **2 배치 분류 완료** - 50 개 문서 자동 할당 (누적 51 개)

### 📈 성장 링 (Growth Rings)
| 날짜 | Eval Score | Type 문서 | 분류됨 | 비고 |
|------|------------|-----------|--------|------|
| 2026-07-26 11:04 | 0.0 | 0 개 | 0 개 | 초기 상태 |
| 2026-07-26 21:05 | 13.1 | 6 개 | 277 개 | Type 문서 6 종 생성 |
| 2026-07-26 21:06 | 14.3 | 10 개 | 302 개 | +4 Type, +25 분류 |
| 2026-07-26 21:07 | 14.3 | 10 개 | 302 개 | 자동화 시스템 완성 |
| 2026-07-27 00:15 | 16.7 | 10 개 | 353 개 | +51 분류 (2 배치) |

---

## 🔄 자동화 워크플로우

```
매일 새벽 4 시 (cronjob ab1915821586)
    ↓
scripts/auto-classify-types.sh 실행 (50 개 배치)
    ↓
미분류 문서 스캔 → 내용 분석 → type 할당
    ↓
EVAL_STATUS.md 업데이트
    ↓
로컬 로그 저장 (~/.hermes/cron/output/)
```

---

## 📋 다음 실행 계획

### 즉시 실행 가능
- **3 배치 분류**: `./scripts/auto-classify-types.sh 100` 실행
- **inbox/papers/ 집중 분류**: 해당 폴더 300 개 문서 대상

### 자동화 예정
- **매일 4 시**: 50 개 문서 자동 분류 (Eval Score +2.4%/일 예상)
- **목표 달성일**: 약 27 일 후 (80 점 도달)

### 수동 개입 필요
- **분류 규칙 정교화**: 현재 키워드 기반 분류의 정확도 검증
- **특수 폴더 처리**: `outputs/`, `syncs/` 등 특수 폴더 분류 규칙
- **wikilink 복원**: 분류 후 `related_to` 자동 생성

---

## 🔍 분류 규칙 (현재)

| 키워드 | 할당 Type |
|--------|-----------|
| meeting, sync, standup, retro, agenda | Meeting |
| reflect, retro, learning, insight, lesson, grow | Reflection |
| project, initiative, roadmap, milestone, onboarding | Project |
| person, profile, 이정민, tony, lee | Person |
| concept, model, framework, theory, principle, pattern | Concept |
| url, link, resource, reference, article, doc | Resource |
| task, action, todo, checklist, assign | Task |
| idea, brainstorm, feature, opportunity, improve | Idea |
| decision, decide, choice, select | Decision |
| (기타) | Note |

---

## 📞 사용법

### 수동 실행
```bash
# 100 개 문서 분류
./scripts/auto-classify-types.sh 100

# 500 개 문서 분류 (대량 처리)
./scripts/auto-classify-types.sh 500
```

### 스킬 사용
```
[[Understand-Anything[[Understand-Anything/understand-anything-plugin/skills/understand/SKILL.md|SKILL]]-anything-plugin/skills/understand-knowledge/SKILL.md|SKILL]]: csp-brain-type-auto-classifier
- scripts/auto-classify-types.sh 포함
- 분류 규칙 및 Pitfalls 문서화됨
```

### Cronjob 관리
```bash
# 상태 확인
cronjob action='list'

# 즉시 실행 (테스트)
cronjob action='run' job_id='ab1915821586'

# 일시 정지
cronjob action='pause' job_id='ab1915821586'
```

---

## 📝 금일 분류 로그 (2026-07-27 00:15)

**배치 크기**: 50 개 문서  
**처리 결과**:

| Type | 수량 | 비율 |
|------|------|------|
| Project | 22 | 44% |
| Concept | 11 | 22% |
| Meeting | 7 | 14% |
| Reflection | 6 | 12% |
| Task | 1 | 2% |
| Resource | 1 | 2% |
| Person | 0 | 0% |
| Idea | 0 | 0% |
| Decision | 0 | 0% |
| Note | 2 | 4% |

**주요 분류 패턴**:
- 언어/기술 문서 (python.md, javascript.md 등) → Meeting/Project 위주 할당
- 구현 문서 (implementation.md) → Project 위주
- 스킬 문서 (SKILL.md) → Reflection/Project 혼합

---

*이 대시보드는 csp-brain 지식 생태계의 건강 상태를 실시간으로 진단합니다.*
*EVAL SCORE 는 지식의 구조화 수준을 나타내며, 80 점 이상을 '성숙'으로 간주합니다.*
