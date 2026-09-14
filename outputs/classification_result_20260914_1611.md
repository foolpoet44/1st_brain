# csp-brain Type 자동 분류 결과 보고서

**실행 일시**: 2026-09-14 16:11  
**Vault 경로**: `/Users/dkmac/csp-brain`  
**스크립트**: `scripts/auto-classify-types.sh`

---

## 📊 실행 결과

### 분류 수행 통계
| 항목 | 값 |
|------|-----|
| 배치 제한 | 50 개 문서 |
| 실제 처리 | 0 개 문서 |
| 미분류 문서 (시작) | 0 개 |
| 미분류 문서 (종료) | 0 개 |

### 현재 Vault 상태
| 항목 | 수량 | 비율 |
|------|------|------|
| 총 문서 수 | 2,456 개 | 100% |
| type 할당됨 | 2,456 개 | 100.0% |
| 미분류 | 0 개 | 0.0% |
| Type 문서 | 11 개 | 0.5% |

### EVAL SCORE
```
EVAL SCORE = (type 할당됨 / 총 문서) * 100
           = (2,456 / 2,456) * 100
           = 100.0 / 100 🎉
```

---

## 🎯 상태 분석

**완전 분류 달성 유지** - 모든 문서에 type 필드가 할당되어 있습니다.

- **자동화 시스템 상태**: 정상 가동 중 (67 번째 배치 실행)
- **모드**: 유지보수 모드 (신규 문서 발생 시 실시간 분류 대기)
- **증감**: 전일 대비 +9 개 문서 증가 (모두 기존 분류됨)

---

## 📋 분류 규칙 (참고)

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

## ✅ 다음 자동화 일정

- **Cronjob**: 매일 새벽 4 시 자동 실행 (Job ID: `ab1915821586`)
- **다음 실행**: 2026-09-15 04:00 예정
- **작업 내용**: 미분류 문서 스캔 → 자동 분류 → EVAL_STATUS.md 업데이트

---

*보고서 자동 생성 by csp-brain-type-auto-classifier*
