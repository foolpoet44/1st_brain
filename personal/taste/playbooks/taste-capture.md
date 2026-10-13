---
title: Taste Capture & Validation
created: 2026-10-13
updated: 2026-10-13
type: playbook
status: growing
tags: [taste, personal, archive, workflow]
aliases: []
generated: {by: ai-assisted-synthesis, at: 2026-10-13}
evidence: mixed
visibility: private
---

# Taste Capture & Validation

## Compiled Truth

### 원칙 [confirmed]

**취향은 목록보다 판단 규칙이다.** 수집 단계에서는 콘텐츠·반응·이유를 기록하고, 반복해서 확인된 선택 기준만 Taste Rule로 승격한다. 직접 진술은 중요한 근거지만, 실제 사례로 그 취향이 적용되는 범위를 검증한다. (Taste Profile v1.2 Archiving principle)

### 1단계: Capture — 즉시 30초

- 대상: 링크·파일·사진·음악 구간·농담·아이디어
- 상황: 언제, 어떤 맥락에서 만났는가?
- **내 첫 문장(CSP가 직접 쓴다):** 왜 마음이 움직였는가?
- 반응: 끌림 / 반감 / 양가감정

> AI는 '내 첫 문장'을 대신 쓰지 않는다. 드라이브 수집 중 취향 신호를 발견하면 카드를 만들되 이 칸은 비워 두고 CSP에게 묻는다.

### 2단계: Interpret — 주간 비교

비슷한 사례 3~5개를 나란히 놓고 반복 요소, 차이, 반례를 적는다. AI의 해석은 별도 섹션에 둔다. 금요일 Dream Cycle에서 한다.

### 3단계: Test — 실제 선택으로 검증

창작물·도구·메시지 가운데 무엇을 고르고 무엇을 포기했으며, 결과는 어땠는가? 예상과 다르면 고친다.

### 캡처 카드 (inbox/taste/YYYY-MM-DD_<대상>.md)

```yaml
observed_at: YYYY-MM-DD
item: '링크 또는 대상'
context: '상황'
my_first_reaction: ''   # 반드시 CSP가 직접 작성
reaction: 'attracted | averse | mixed'
features: []
ai_interpretation: ''   # AI 가설, 확정 아님
counterexample: ''
choice_and_outcome: ''
confidence: 'low | medium | high'
```

### 승격 규칙 [confirmed]

- 승격은 저장소 공통 규칙(`.claude/rules/epistemic-status.md`)을 따른다. [inferred] → [confirmed]는 Timeline의 `CSP 확인 YYYY-MM-DD` 한 줄로만 한다.
- 시청 기록 같은 공동 사용 가능 데이터에서 나온 해석은 [inferred] 이상으로 시작하지 않는다.
- 단일 사례로 취향 전체를 일반화하지 않는다. 변경 사유는 [[log]]에 남긴다.

---

## Timeline

### 2026-10-13

- OKF v1.0 운영법과 Taste Profile v1.2 아카이빙 원칙 병합. 캡처 카드 위치를 `inbox/taste/` 로 정함(inbox는 Pages 발행 제외).
- 연결: [[decision-heuristics]] · [[sources]].
