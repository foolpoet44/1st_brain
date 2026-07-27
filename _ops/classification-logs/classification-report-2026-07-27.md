---
type: Note
status: Active
---

# 📊 Type 문서 자동 분류 보고서

**실행 일시**: 2026-07-27 00:15  
**실행 스크립트**: `scripts/auto-classify-types.sh 50`  
**Vault 경로**: `/Users/dkmac/Desktop/@26/dev`

---

## 📈 실행 요약

| 항목 | 값 |
|------|-----|
| 배치 제한 | 50 개 |
| 실제 분류 | 50 개 |
| 성공률 | 100% |

---

## 📊 분류 결과 상세

### Type 별 분포
| Type | 수량 | 비율 |
|------|------|------|
| Project | 22 | 44% |
| Concept | 11 | 22% |
| Meeting | 7 | 14% |
| Reflection | 6 | 12% |
| Task | 1 | 2% |
| Resource | 1 | 2% |
| Note | 2 | 4% |

### 분류된 문서 목록
1. ko.md → Concept
2. swift.md → Meeting
3. markdown.md → Project
4. kotlin.md → Meeting
5. dockerfile.md → Project
6. go.md → Meeting
7. python.md → Meeting
8. yaml.md → Concept
9. css.md → Concept
10. csharp.md → Meeting
11. json.md → Project
12. rust.md → Meeting
13. php.md → Reflection
14. sql.md → Concept
15. javascript.md → Meeting
16. protobuf.md → Concept
17. terraform.md → Concept
18. java.md → Project
19. graphql.md → Concept
20. ruby.md → Concept
21. cpp.md → Project
22. typescript.md → Project
23. shell.md → Project
24. html.md → Concept
25. [[Understand-Anything[[Understand-Anything/understand-anything-plugin/skills/understand/SKILL.md|SKILL]]-anything-plugin/skills/understand-knowledge/SKILL.md|SKILL]].md → Reflection
26. spring.md → Project
27. rails.md → Project
28. vue.md → Project
29. nextjs.md → Project
30. express.md → Project
31. gin.md → Project
32. django.md → Meeting
33. react.md → Reflection
34. fastapi.md → Project
35. flask.md → Reflection
36. SKILL.md → Project
37. SKILL.md → Project
38. [[README.md|README]].md → Project
39. 2026-03-14-phase2-implementation.md → Project
40. 2026-03-18-multi-platform-simple-implementation.md → Project
41. 2026-03-21-language-agnostic-plan.md → Concept
42. 2026-03-14-phase3-implementation.md → Reflection
43. 2026-04-09-understand-knowledge.md → Project
44. 2026-04-10-understandignore-impl.md → Project
45. 2026-03-29-homepage-update-impl.md → Reflection
46. 2026-03-14-phase4-implementation.md → Project
47. 2026-03-25-dashboard-robustness-impl.md → Task
48. 2026-03-14-phase1-implementation.md → Project
49. 2026-05-03-graph-layout-scaling.md → Resource
50. 2026-03-15-homepage-implementation.md → Project

---

## 📊 Vault 전체 현황 (분류 후)

| 지표 | 값 |
|------|-----|
| 총 문서 수 | 2,120 개 |
| type 할당됨 | 353 개 (16.7%) |
| 미분류 | 1,767 개 (83.3%) |
| EVAL SCORE | 16.7 / 100 |

---

## 🔍 관찰 사항

### 분류 패턴 분석
1. **기술 언어 문서**: python.md, javascript.md 등이 Meeting 으로 분류됨
   - 이는 키워드 매칭의 한계로, 실제 내용은 언어 레퍼런스일 가능성
   - 분류 규칙 정교화 필요

2. **구현 문서**: implementation.md 파일들이 Project 로 잘 분류됨

3. **SKILL.md 파일**: 맥락에 따라 Reflection 또는 Project 로 분류

### 개선 제안
1. 언어 이름 키워드는 Concept 또는 Resource 로 재매핑 고려
2. 파일 경로 기반 분류 규칙 추가 (예: `skills/**` → Concept)
3. frontmatter 에 `tags:` 필드도 함께 분석하는 규칙 추가

---

## ✅ 다음 액션

1. **분류 규칙 검토**: 언어 이름 키워드 재평가
2. **3 배치 실행**: 추가 100 개 문서 분류 고려
3. **정확도 검증**: 무작위 샘플링으로 분류 정확도 확인

---

*보고서 생성: csp-brain Type 자동 분류 시스템*
