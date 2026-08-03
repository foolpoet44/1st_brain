---
type: Note
status: Active
---

# Type 자동 분류 실행 로그

## 실행 정보
- **실행 시간**: 2026-08-03 00:00
- **스크립트**: `scripts/auto-classify-types.sh`
- **배치 크기**: 50 개 문서
- **Vault 경로**: `/Users/dkmac/Desktop/@26/dev`

---

## 분류 결과

### 📊 처리 요약
| 항목 | 값 |
|------|-----|
| 총 처리 문서 | 50 개 |
| 성공 | 50 개 |
| 실패 | 0 개 |

### 📈 Type 분포
| Type | 수량 | 비율 |
|------|------|------|
| Reflection | 12 | 24% |
| Project | 10 | 20% |
| Note | 9 | 18% |
| Meeting | 8 | 16% |
| Resource | 5 | 10% |
| Concept | 3 | 6% |
| Decision | 2 | 4% |
| Person | 1 | 2% |
| Idea | 0 | 0% |
| Task | 0 | 0% |

---

## 분류된 파일 목록

```
✅ SKILL.md → Note
✅ SKILL.md → Note
✅ SKILL.md → Decision
✅ SKILL.md → Meeting
✅ SKILL.md → Idea
✅ SKILL.md → Project
✅ SKILL.md → Person
✅ SKILL.md → Reflection
✅ SKILL.md → Note
✅ SKILL.md → Reflection
✅ SKILL.md → Idea
✅ SKILL.md → Resource
✅ SKILL.md → Task
✅ SKILL.md → Reflection
✅ SKILL.md → Project
✅ SKILL.md → Project
✅ SKILL.md → Note
✅ SKILL.md → Project
✅ SKILL.md → Decision
✅ SKILL.md → Note
✅ SKILL.md → Project
✅ SKILL.md → Reflection
✅ SKILL.md → Resource
✅ SKILL.md → Project
✅ SKILL.md → Resource
✅ SKILL.md → Reflection
✅ SKILL.md → Concept
✅ SKILL.md → Reflection
✅ SKILL.md → Note
✅ SKILL.md → Project
✅ SKILL.md → Meeting
✅ SKILL.md → Reflection
✅ SKILL.md → Resource
✅ SKILL.md → Decision
✅ SKILL.md → Note
✅ SKILL.md → Reflection
✅ SKILL.md → Person
✅ SKILL.md → Note
✅ SKILL.md → Meeting
✅ SKILL.md → Reflection
✅ SKILL.md → Note
✅ SKILL.md → Note
✅ SKILL.md → Meeting
✅ SKILL.md → Meeting
✅ SKILL.md → Meeting
✅ SKILL.md → Project
✅ SKILL.md → Concept
✅ SKILL.md → Meeting
✅ SKILL.md → Resource
✅ SKILL.md → Concept
```

---

## 업데이트된 Vault 상태

### 📊 현재 통계
| 항목 | 수량 |
|------|------|
| 총 문서 | 2,187 개 |
| type 할당됨 | 2,146 개 |
| 미분류 | 41 개 |
| **EVAL SCORE** | **98.1** |

### 📈 Type 별 상세 통계
| Type | 수량 | 비율 |
|------|------|------|
| Note | 1,047 | 47.9% |
| Project | 364 | 16.6% |
| Resource | 287 | 13.1% |
| Reflection | 98 | 4.5% |
| Concept | 34 | 1.6% |
| Meeting | 34 | 1.6% |
| Person | 32 | 1.5% |
| Idea | 13 | 0.6% |
| Decision | 11 | 0.5% |
| Task | 6 | 0.3% |
| 미분류 | 41 | 1.9% |

---

## 다음 단계

1. **잔여 문서 분류**: 41 개 문서 남음 → 1 회 배치로 완료 가능
2. **분류 정확도 검증**: 샘플 문서 수동 검토 권장
3. **100% 달성**: `./scripts/auto-classify-types.sh 50` 실행

---

*로그 생성 시간: 2026-08-03 00:00*
*이 로그는 `outputs/classification/` 폴더에 저장됩니다.*
