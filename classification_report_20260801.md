# csp-brain Type 자동 분류 결과 보고서

## 실행 정보
- **실행 일시**: 2026-08-01 04:03
- **스크립트**: scripts/auto-classify-types.sh
- **배치 크기**: 50 개 문서
- **Vault 경로**: /Users/dkmac/Desktop/@26/dev

## 분류 결과 요약

### 전체 통계
| 항목 | 수량 |
|------|------|
| 총 문서 수 | 2,167 개 |
| type 할당됨 | 2,004 개 (92.5%) |
| 미분류 | 163 개 (7.5%) |
| **EVAL SCORE** | **92.5 / 100** 🟢 |

### 금일 분류 내역 (50 개)
| Type | 수량 | 비율 |
|------|------|------|
| Project | 14 | 28% |
| Meeting | 10 | 20% |
| Reflection | 8 | 16% |
| Resource | 6 | 12% |
| Note | 5 | 10% |
| Concept | 4 | 8% |
| Idea | 4 | 8% |
| Person | 2 | 4% |
| Decision | 2 | 4% |
| Task | 1 | 2% |
| **합계** | **50** | **100%** |

### Type 별 누적 통계
| Type | 수량 | 비율 |
|------|------|------|
| Note | 995 | 49.6% |
| Project | 349 | 17.4% |
| Resource | 270 | 13.5% |
| Reflection | 64 | 3.2% |
| Concept | 30 | 1.5% |
| Person | 26 | 1.3% |
| Meeting | 24 | 1.2% |
| Idea | 9 | 0.4% |
| Decision | 5 | 0.2% |
| Task | 4 | 0.2% |
| 미분류 | 163 | 7.5% |
| **총계** | **2,167** | **100%** |

## 성장 링 (Growth Rings)
| 날짜 | Eval Score | 분류됨 | 증감 | 비고 |
|------|------------|--------|------|------|
| 2026-07-26 11:04 | 0.0 | 0 개 | - | 초기 상태 |
| 2026-07-26 21:05 | 13.1 | 277 개 | +277 | Type 문서 6 종 생성 |
| 2026-07-26 21:06 | 14.3 | 302 개 | +25 | +4 Type 문서 |
| 2026-07-27 00:15 | 16.7 | 353 개 | +51 | 2 배치 완료 |
| 2026-07-30 13:04 | 88.3 | 1,904 개 | +1,551 | 31 배치 완료 🎉 |
| 2026-07-31 01:15 | 90.5 | 1,954 개 | +50 | 32 배치 완료 |
| 2026-08-01 04:03 | 92.5 | 2,004 개 | +50 | 33 배치 완료 |

## 분류 규칙
| 키워드 패턴 | 할당 Type |
|------------|-----------|
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

## 다음 단계
1. **잔여 문서 분류**: 163 개 문서 남음 (약 3-4 회 배치 필요)
2. **목표**: EVAL SCORE 100 점 달성
3. **자동화**: cronjob(ab1915821586) 이 매일 새벽 4 시 자동 실행

## 제외 폴더
- node_modules/*
- .git/*

---
*보고서 생성: 2026-08-01 04:03*
*csp-brain Vault 자동 분류 시스템*
