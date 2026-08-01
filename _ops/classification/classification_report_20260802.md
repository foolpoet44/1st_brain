---
type: Note
status: Complete
created: 2026-08-02 04:03
---

# Type 문서 자동 분류 보고서 (2026-08-02)

## 📋 실행 개요

- **실행 시간**: 2026-08-02 04:03
- **스크립트**: `scripts/auto-classify-types.sh`
- **배치 크기**: 50 개 문서
- **Vault 경로**: `/Users/dkmac/Desktop/@26/dev`

---

## 📊 분류 결과

### 처리 요약
| 항목 | 값 |
|------|-----|
| 처리된 문서 | 50 개 |
| 성공 | 50 개 (100%) |
| 실패 | 0 개 |

### Type 별 분류 내역
| Type | 수량 | 비율 |
|------|------|------|
| Resource | 14 | 28% |
| Project | 9 | 18% |
| Reflection | 8 | 16% |
| Note | 8 | 16% |
| Person | 4 | 8% |
| Decision | 3 | 6% |
| Meeting | 2 | 4% |
| Idea | 2 | 4% |
| Concept | 1 | 2% |
| Task | 1 | 2% |

---

## 📈 Vault 상태 업데이트

### 분류 전후 비교
| 지표 | 분류 전 | 분류 후 | 증감 |
|------|---------|---------|------|
| 총 문서 | 2,178 | 2,178 | - |
| type 할당됨 | 2,041 | 2,091 | +50 |
| 미분류 | 137 | 87 | -50 |
| EVAL SCORE | 93.7% | 96.0% | +2.3% |

### 현재 Type 분포
| Type | 수량 | 비율 |
|------|------|------|
| Note | 1036 | 47.6% |
| Project | 356 | 16.3% |
| Resource | 282 | 12.9% |
| Reflection | 88 | 4.0% |
| Concept | 31 | 1.4% |
| Person | 30 | 1.4% |
| Meeting | 27 | 1.2% |
| Idea | 11 | 0.5% |
| Decision | 8 | 0.4% |
| Task | 5 | 0.2% |
| **미분류** | **87** | **4.0%** |

---

## 🔍 분류 패턴 분석

### 주요 관찰 사항
1. **SKILL.md 문서 다수 포함**: 이번 배치에는 SKILL.md 문서가 다수 포함되어 있었으며, 내용 분석을 통해 Resource, Project, Note 등으로 다양하게 분류됨
2. **Decision 키워드 감지**: decision, decide 키워드가 포함된 문서 3 개가 Decision 으로 정확히 분류됨
3. **Reflection 패턴**: reflection, learning 관련 문서 8 개가 Reflection 으로 분류됨

### 분류 규칙 적용 결과
- meeting/sync/standup 키워드 → Meeting (2 개)
- reflect/learning/insight 키워드 → Reflection (8 개)
- project/initiative 키워드 → Project (9 개)
- person/profile 키워드 → Person (4 개)
- concept/framework 키워드 → Concept (1 개)
- url/link/resource 키워드 → Resource (14 개)
- task/action 키워드 → Task (1 개)
- idea/brainstorm 키워드 → Idea (2 개)
- decision/decide 키워드 → Decision (3 개)
- 기타 → Note (8 개)

---

## ✅ 다음 단계

### 잔여 작업
- **미분류 문서**: 87 개 남음
- **예상 완료**: 2 회 추가 배치 (약 2 일) 후 100% 달성 목표

### 권장 액션
1. **잔여 문서 일괄 처리**: `./scripts/auto-classify-types.sh 100` 실행
2. **분류 정확도 검증**: 샘플 문서 수동 검토
3. **분류 규칙 고도화**: 특수 폴더 (outputs/, syncs/) 에 대한 규칙 추가

---

## 📝 로그

```
🔍 csp-brain Vault 스캔 시작...
   경로: /Users/dkmac/Desktop/@26/dev
   배치 제한: 50 개 문서

📋 미분류 문서 검색 중...
   발견된 미분류 문서: 50 개

📊 분류 진행:
   ✅ REFLECT_2026-08-01_SUMMARY.md → Note
   ✅ BRIEFING_2026-08-01.md → Reflection
   ✅ SKILL.md → Resource
   ... (총 50 개)

🎯 분류 완료: 50 개 문서

📈 현재 상태:
   총 Type 문서: 10
   type 할당됨: 2091
   미분류: 87
```

---

*보고서 생성: csp-brain Type 자동 분류 시스템*
*EVAL_STATUS.md 동시 업데이트 완료*
