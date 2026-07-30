---
type: Meeting
---
# CSP-Brain 운영 규칙

## 커뮤니케이션

- 항상 한국어로 응답
- 에세이형 설명 우선 (불렛 리스트보다 연결된 문장)
- 코드 설명 시 "왜"를 반드시 포함
- 철학적/심리학적 유추를 환영

## 폴더 역할

- `inbox/` → 인간이 자료를 던지는 곳 (AI 는 읽기 + 정리는 가능)
- `wiki/` → AI 가 생성·수정·병합하는 지식 위키
- `projects/` → 프로젝트별 Compiled Truth + Timeline 관리
- `outputs/` → AI 가 생성한 산출물
- `_ops/` → 운영 로그 기록

## 문서 작성 규칙

1. 모든 wiki 문서는 frontmatter 포함 (title, created, updated, type, status, tags)
2. 백링크 2 개 이상 포함 (고립 방지)
3. Compiled Truth + Timeline 이중 구조 준수

## 프로토콜

- `ingest` → inbox/ 스캔 → wiki/ 통합
- `lint` → 위키 점검 (백링크, frontmatter, 갱신 주기)
- `digest` → 주간 다이제스트 생성
- `sync` → Notion 양방향 연동
- `generate` → 콘텐츠 자동 생성
