# csp-brain Type 문서 자동 분류 결과 보고서

## 실행 정보
- **실행 일시**: 2026-07-30 13:04
- **Vault 경로**: /Users/dkmac/Desktop/@26/dev
- **스크립트**: scripts/auto-classify-types.sh
- **배치 크기**: 50 개 문서

---

## 📊 실행 결과 요약

### 분류 통계
| 항목 | 값 |
|------|-----|
| **처리된 문서 수** | 50 개 |
| **총 문서 수** | 2,157 개 |
| **type 할당됨** | 1,904 개 (88.3%) |
| **미분류** | 253 개 (11.7%) |
| **EVAL SCORE** | 88.3 / 100 🟢 |

### 금일 분류 내역 (50 개)
| Type | 수량 | 비율 |
|------|------|------|
| Note | 10 | 20% |
| Project | 10 | 20% |
| Resource | 9 | 18% |
| Concept | 6 | 12% |
| Reflection | 5 | 10% |
| Person | 4 | 8% |
| Meeting | 3 | 6% |
| Idea | 1 | 2% |
| Task | 1 | 2% |
| Decision | 0 | 0% |

---

## 📈 Type 별 누적 통계

| Type | 수량 | 비율 |
|------|------|------|
| Note | 975 | 51.2% |
| Project | 331 | 17.4% |
| Resource | 253 | 13.3% |
| Reflection | 49 | 2.6% |
| Concept | 24 | 1.3% |
| Person | 20 | 1.1% |
| Meeting | 11 | 0.6% |
| Task | 1 | 0.1% |
| Idea | 1 | 0.1% |
| Decision | 0 | 0.0% |

---

## ✅ 달성 목표

- [x] **EVAL SCORE 80 점 이상** → 88.3 점 달성
- [x] **type 할당 1,900 개 이상** → 1,904 개 달성
- [x] **미분류 300 개 이하** → 253 개 달성

---

## 🎯 다음 단계

1. **잔여 문서 분류**: 253 개 문서 추가 분류 시 100% 달성 가능
2. **분류 정확도 검증**: 샘플 문서 수동 검토 권장
3. **자동화 유지**: cronjob 을 통한 지속적 관리

---

## 📝 실행 로그

```
🔍 csp-brain Vault 스캔 시작...
   경로: /Users/dkmac/Desktop/@26/dev
   배치 제한: 50 개 문서

📋 미분류 문서 검색 중...
   발견된 미분류 문서: 50 개

📊 분류 진행:
   ✅ BRIEFING_2026-07-30_IO_PSYCHOLOGY.md → Concept
   ✅ HR_TECH_BRIEFING_2026-07-29.md → Concept
   ✅ pull_request_template.md → Reflection
   ✅ SKILL.md → Resource
   ... (50 개 문서 처리)

🎯 분류 완료: 50 개 문서

📈 현재 상태:
   총 Type 문서: 10
   type 할당됨: 1904
   미분류: 253
```

---

*보고서 생성일: 2026-07-30 13:04*
*csp-brain Type 문서 자동 분류 시스템*
