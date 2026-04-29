# Extracted Knowledge from Conv: 6f3fb9b3-80c9-4d03-a798-89ab5de3ce51

**Date**: 2026-03-13T00:53:37.976377Z

### Extracted Code (text)

```text
Task명: AX 교육 커리큘럼 초안 작성
프로젝트: AX 교육 (기존 프로젝트 매핑 또는 신규 생성)
마감일: 내일 (= 상대 날짜 → 절대 날짜 변환)
우선순위: 높음 (트리거 단어: "급하게")
컨텍스트: 팀장 보고용 (→ 산출물 유형 태깅)
상태: To Do (기본값)
```

### Extracted Code (text)

```text
Project (상위)
├── id, name, status, deadline, priority
│
Task (하위)
├── id, project_id (FK)
├── title
├── status: [todo / in_progress / blocked / done]
├── priority: [P1 / P2 / P3]
├── due_date
├── tags (보고용, 회의용, 검토필요 등)
└── created_at, updated_at
```

### Extracted Code (text)

```text
"AX 교육 커리큘럼 완료"         → status: done
"팀장 보고 내일로 미뤄짐"        → due_date: +1일
"ESCON 프로젝트 지금 막혀있어"   → status: blocked
"오늘 할 일 다 보여줘"           → 오늘의 대시보드 뷰 렌더링
```

### Extracted Code (text)

```text
System: 당신은 PM의 자연어 입력을 task 데이터로 변환합니다.
        기존 프로젝트 목록: {project_list}
        오늘 날짜: {today}
        
        반드시 JSON만 반환하세요:
        {task_name, project_id, due_date, priority, status, tags}

User: "AX 교육 커리큘럼 초안 내일까지 급하게"
```
