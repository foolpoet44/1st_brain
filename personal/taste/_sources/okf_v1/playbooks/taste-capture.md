---
type: Howto
title: Taste Capture & Validation
description: 30초 수집·주간 해석·결과 검증 루프
tags:
- taste
- archive
- workflow
status: draft
timestamp: '2026-10-13'
generated:
  by: ai-assisted-memory-synthesis
  at: '2026-10-13T09:13:00+09:00'
---

# Taste Capture & Validation

## 1단계: Capture — 즉시 30초

- 대상: 링크/파일/사진/음악 구간/농담/아이디어 등
- 상황: 언제, 어떤 맥락에서 만났는가?
- **내 첫 문장(본인 직접 작성):** 왜 마음이 움직였는가?
- 반응: 끌림/반감/양가감정

> AI는 '내 첫 문장'을 대신 쓰지 않는다.

## 2단계: Interpret — 주간 비교

서로 비슷한 사례 3~5개를 나란히 놓고 반복되는 요소, 차이, 반례를 기록한다. AI의 해석은 별도 섹션에 둔다.

## 3단계: Test — 실제 선택으로 검증

창작물·도구·메시지 가운데 무엇을 선택했고, 무엇을 포기했으며, 결과는 어땠는가? 예상과 달랐다면 수정한다.

## 캡처 템플릿

```yaml
observed_at: YYYY-MM-DD
item: '링크 또는 대상'
context: '상황'
my_first_reaction: '반드시 사용자가 직접 작성'
reaction: 'attracted | averse | mixed'
features: []
ai_interpretation: 'AI 가설, 확정 아님'
counterexample: ''
choice_and_outcome: ''
confidence: 'low | medium | high'
```

## 갱신 규칙

- 사용자의 직접 수정이 AI 해석보다 우선한다.
- 반복 사례가 생기면 기존 문서의 confirmed/inferred/unknown 구분을 업데이트한다.
- 단일 사례로 취향 전체를 일반화하지 않는다.
- 변경 사유는 [log.md](../log.md)에 남긴다.
