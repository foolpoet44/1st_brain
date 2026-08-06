# csp-brain Type 자동 분류 결과 보고서

**실행 일시**: 2026-08-06 13:02  
**스크립트**: `scripts/auto-classify-types.sh 50`  
**Vault 경로**: `/Users/dkmac/csp-brain`

---

## 📊 분류 결과 요약

| 항목 | 값 |
|------|-----|
| 배치 제한 | 50 개 |
| 실제 분류 | 3 개 |
| 미분류 잔여 | 0 개 |
| EVAL SCORE | 100.0 / 100 |

---

## ✅ 분류된 문서 목록

| 문서명 | 할당 Type | 비고 |
|--------|-----------|------|
| TELEGRAM_SUMMARY_2026-08-05.md | Note | 일일 요약 문서 |
| METABOLISM_REPORT_2026-08-05.md | Reflection | 학습/성찰 보고서 |
| classification_result_20260805_1302.md | Meeting | 분류 결과 로그 |

---

## 📈 Type 별 분포

| Type | 수량 | 비율 |
|------|------|------|
| Note | 1 | 33.3% |
| Reflection | 1 | 33.3% |
| Meeting | 1 | 33.3% |

---

## 🎯 현재 Vault 상태

| 지표 | 수치 |
|------|------|
| 총 문서 수 | 2,246 개 |
| type 할당됨 | 2,246 개 (100.0%) |
| 미분류 | 0 개 (0.0%) |
| Type 문서 종 | 11 종 |

---

## 📋 Type 별 상세 통계

| Type | 수량 | 비율 |
|------|------|------|
| Note | 1055 | 46.9% |
| Project | 367 | 16.4% |
| Resource | 301 | 13.4% |
| Reflection | 104 | 4.6% |
| Person | 44 | 2.0% |
| Concept | 42 | 1.9% |
| Meeting | 40 | 1.8% |
| Idea | 14 | 0.6% |
| Decision | 11 | 0.5% |
| Task | 7 | 0.3% |
| Signal | 3 | 0.1% |

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

## ✅ 다음 단계

1. **유지보수 모드 지속**: 신규 문서 생성 시 자동 분류 cronjob 이 실시간 처리
2. **분류 정확도 검증**: 키워드 기반 분류의 정확도 지속 모니터링
3. **EVAL SCORE 100 점 유지**: 완전 분류 상태 유지

---

*보고서 생성: csp-brain Type 자동 분류 시스템*
