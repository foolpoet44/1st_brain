# 스킬: Dream Cycle (주간 정리)

> 매주 금요일 실행하는 메모리 정리 루틴.  
> 뇌의 수면 중 기억 강화 과정에서 영감받은 패턴.

---

## 언제 쓰는가

- 매주 금요일
- 이번 주 대화/작업이 충분히 쌓였을 때
- inbox가 너무 많이 차있을 때 (임시 실행)

---

## 실행 단계

1. **inbox 정리**
   - `raw/inbox.md` 전체 읽기
   - 각 항목을 적절한 폴더로 이동
     - 프로젝트 관련 → 해당 `projects/` Timeline에 append
     - 인물 관련 → `people/` 파일 생성 또는 업데이트
     - 개념/이론 → `concepts/` 파일 생성
     - 결정 → `decisions/` 파일 생성
   - 처리 완료 항목 취소선 처리
   
2. **Compiled Truth 갱신**
   - 이번 주 변화가 있던 프로젝트 파악
   - 각 프로젝트 `README.md`의 Compiled Truth 업데이트
   - CLAUDE.md 프로젝트 상태 테이블 업데이트

3. **Weekly 파일 생성**
   - 파일명: `weekly/[YYYY-WNN].md`
   - 포함 내용: 핵심 활동, 주요 결정, 다음 주 액션

4. **inbox 초기화**
   - 처리 완료된 항목 제거
   - `마지막 Dream Cycle` 날짜 업데이트

---

## 주의사항

- Timeline에는 절대 손대지 않음 (append만 허용)
- Compiled Truth 갱신 시 이전 내용을 덮어씀 (의도적)
- 모든 inbox 항목을 처리하려 하지 말 것 — 분류 불명확하면 그냥 두기

---

## 관련 프롬프트

```
이번 주 Dream Cycle을 실행해줘.
오늘 날짜: [날짜]
이번 주 주요 대화 주제: [내용 요약]
```
