---
title: "OPQ32 (Occupational Personality Questionnaire) Framework"
created: 2026-04-29
updated: 2026-11-11
status: growing
type: concept
tags: [hr, psychology, assessment, opq32]
related_to: "[[oka-project]]"
generated:
  by: ai-assisted-ingest
  at: 2026-11-11
evidence: mixed
---

# OPQ32 (Occupational Personality Questionnaire) Framework

## Compiled Truth

> 2026-11-11 신설. 2026-07-18 설계 편입 이후 116일간 갱신되지 않았고 **결론을 적는 칸이 없었다.** 위키 안에서 4편이 이 문서를 인용한다. 아래가 현재까지의 최선의 요약이며, 아래 Timeline 은 손대지 않는 증거 원본이다.

### 한 문장 [inferred]

이 문서는 성격검사를 사람을 분류하는 도구에서 **검증받아야 할 가설을 생산하는 도구**로 바꾸는 설계다. 그래서 산출물의 문법이 "이 사람은 ~형이다"가 아니라 "~경향이 잠재되어 있고 관측이 ~만큼 지지한다"로 고정된다.

### 도구의 사실 [confirmed]

OPQ32 는 SHL 이 개발한 직업 성격 설문지이며, 임상 진단이 아니라 직무 적합성에 초점을 둔다. 성격을 세 영역(사람과의 관계·사고 스타일·느낌과 감정)으로 나눈다. 본 설계가 입력으로 쓰는 것은 강제선택 방식이 아니라 **규준 기반(OPQ32r/IRT) 점수 32개**이고, 이 전제가 깨지면 아래 산출 논리 전체가 성립하지 않는다.

### 산출 엔진의 설계 [confirmed]

두 개의 프로파일을 같은 변환 파이프라인으로 만든다. 하나는 직무 역량의 폭을 묻는 **UCF Great Eight** 여덟 역량(주도·지원·대인·분석·창의·조직·적응·성취), 다른 하나는 리더로서의 차별적 우위를 묻는 **Leader Edge** 다섯 축(전략·영향·추진·사람·회복)이다. 각 값은 관련 척도의 가중 선형합이고, 가중치 총합을 1.0 으로 고정해 산출값이 그대로 입력과 같은 밴드에 떨어진다. 역방향 문항은 뒤집어 계산한다. 가중치는 투명한 3단계(강·중·약)로 재구성했고, 그 이유는 설명 가능성이 코칭 신뢰의 전제이기 때문이다.

### 이 설계의 핵심 장치 [confirmed]

다섯 축은 각각 밝은 면과 그림자를 한 쌍으로 갖는다. **모든 강점은 압박 아래에서 자기 탈선 위험으로 뒤집힌다**는 전제다. 그림자에 불이 켜지는 조건은 하나뿐이다 — 어떤 축이 매우 높고 그것을 견제할 축이 매우 낮을 때. 영향력이 높고 사람이 낮으면 지배형, 추진이 높고 사람이 낮으면 소진형, 전략이 높고 조직화가 낮으면 공상형이다. 이 불빛은 판정이 아니라 **선험적 경보, 곧 이후의 행동 데이터가 검증할 가설**이다. 360 평가와 Pulse 결과가 그 가설을 등급으로 확인하면 관찰→경보→심각으로 수렴한다.

### 116일째 대기 중인 것 [unknown]

2026-07-18 Timeline 은 다음 갈래로 두 가지를 적어 두었다. 가중치를 담은 계산 엔진, 그리고 경보 단계 사이의 간극을 수치로 판정하는 논리다. **저장소에는 둘 다 없다.** 이 주제로 존재하는 파일은 이 문서와 수집함의 원본 설계서뿐이고, 가중치 표도 계산 코드도 어디에도 기록되어 있지 않다. 즉 지금 이 설계는 **재현할 수 없다.** 본문의 산식은 방법의 서술이고, 같은 사람의 점수를 넣어 같은 결과를 두 번 얻을 수 있는 상태가 아니다.

### HR 함의 [inferred]

이 설계가 옳게 잡은 것은 출력 문법이다. 성격검사가 조직에서 해를 끼치는 경로는 대개 측정 오차가 아니라 **가설이 판정으로 굳는 순간**이고, 이 문서는 그 지점을 문장 형식으로 막아 두었다. 반면 116일 동안 계산 엔진이 없다는 사실은 더 무거운 문제를 가리킨다. 재현할 수 없는 산식으로 사람에 관한 경보를 켜면, 그 경보는 반박할 수도 없다. 사람이 이의를 제기하려면 숫자가 어떻게 나왔는지 열어 볼 수 있어야 한다. **설명 가능성을 신뢰의 전제로 적어 둔 문서가, 정작 자기 가중치를 공개하지 않은 상태로 116일을 보냈다.**

### Vault 연계 [inferred]

이 레이어의 출력은 [[bp-signal-intelligence]] 신호 생성의 선행 소스로 들어가 개인 노드 속성을 채운다. 심리 프레임 매핑은 [[ex-insight-mining-pipeline]] 의 평정 격자와 같은 좌표계를 쓴다. 회복 축은 [[self-determination-theory]] 의 자율성·유능감 개념과 겹치는 영역이 있으나, 두 좌표계를 맞춰 본 기록은 없다.

---


## 1. 개요

OPQ32는 SHL에서 개발한 직업 성격 설문지로, 직장 내에서의 선호 행동과 잠재 역량을 측정하는 글로벌 표준 도구입니다. 임상적 진단이 아닌 '직무 적합성'에 초점을 맞춘 것이 특징입니다.

## 2. 3대 영역 (Three Domains)

성격을 크게 세 가지 심리적 영토로 구분합니다:

1. **사람들과의 관계 (Relationships with People)**: 영향력, 사교성, 공감 및 지원.
2. **사고 스타일 (Thinking Style)**: 분석적 사고, 창의성, 계획 및 구조화.
3. **느낌 및 감정 (Feelings and Emotions)**: 정서적 안정성, 동기 부여, 역동성.

## 3. 핵심 지표 (Conceptual Atoms)

- **정서적 회복탄력성 (Resilience)**: 스트레스 상황에서의 회복 속도와 평정심 유지.
- **직무 몰입 (Engagement)**: 과업에 대한 열정과 에너지 수준.
- **스트레스 내성 (Tolerance)**: 압박감 속에서의 결정력과 성과 지속성.

## 4. HR Tech적 가치

- **Vibe Check의 데이터화**: 추상적인 인상을 객관적인 스텐(Sten) 점수로 치환하여 'Vibe Coding'의 근거를 제공합니다.
- **역량 매핑**: 특정 직무 요구사항과 개인의 성격 프로파일을 매칭하여 'Do it once, automate it forever'의 채용/배치 자동화를 가능케 합니다.

## 5. UCF × Leader Edge 산출 엔진 (Disposition 레이어)

OPQ32 sten(1–10) 32개를 입력으로, 두 개의 성격이 다른 프로파일을 같은 변환 파이프라인으로 산출합니다. 각 역량/엣지는 관련 스케일의 가중 선형합이며 **가중치 총합을 1.0으로 고정**해 산출값이 그대로 1–10 밴드에 떨어집니다(역채점 `s* = 11 − s`). ipsative(강제선택)가 아닌 **normative(OPQ32r/IRT) 입력**이 전제입니다.

- **UCF Great Eight (평면)**: "이 사람이 직무 역량을 발휘할 잠재력의 폭"을 묻습니다. SHL의 OPQ–UCF 연결을 따르되 가중치를 투명한 3-tier(강 .25–.30 / 중 .15–.20 / 약 .10)로 재구성 — 설명가능성이 코칭 신뢰의 전제이므로 규칙기반. 8개 역량: Leading&Deciding, Supporting&Cooperating, Interacting&Presenting, Analysing&Interpreting, Creating&Conceptualising, Organising&Executing, Adapting&Coping, Enterprising&Performing.
- **Leader Edge (벡터·양날)**: "리더로서의 차별적 우위 — 그리고 그 우위가 칼날처럼 뒤집히는 지점"을 묻습니다. 5개 엣지(Strategic / Influence / Drive / People / Resilience) 각각이 밝은 면과 *그림자(dark-side)*를 한 쌍으로 갖습니다. 모든 강점은 압박 하에서 자기 탈선 위험으로 뒤집힙니다.

**그림자 점등 규칙 (두 층을 잇는 다리)**: `IF Edge_score ≥ 8 AND Counterbalancer ≤ 3 → Dark-risk 플래그`. 예: Influence↑ + People↓ → 지배형, Drive↑ + People↓ → 소진형, Strategic↑ + UCF#6(Organising)↓ → 공상형. 이 플래그가 **선험적 경보 — EX 신호가 검증할 가설**입니다. OPQ가 사전확률(예: "변화 압력 하 지배형 탈선 가능성")을 던지고, 이후 360·Pulse·BP Report가 행동 데이터로 A–D 등급 확인하면 Watch→Alert→Critical로 수렴합니다. 출력 문법은 판결이 아니라 가설 — "~형이다"가 아니라 "~경향이 ~만큼 잠재되어 있고 관측이 ~만큼 지지한다".

이 Disposition 레이어의 출력이 [[bp-signal-intelligence]] Signal Generation의 _선행_ 소스로 들어가 People Context Graph 개인 노드 속성을 채웁니다. 심리 프레임 매핑(Direction&Meaning·LMX·JD-R·SDT·POS)은 [[ex-insight-mining-pipeline]]의 연역 평정 격자와 동일 좌표계입니다. 리더 선발 역량은 projects/physical-ai-talent 면접 키트와 교차 검증됩니다.

---

## Timeline

### 2026-07-18

- Drive 설계문서에서 편입: **OPQ → UCF / Leader Edge 산출 로직** (Opq-ucf-le).
- 공통 산출 엔진: OPQ32 sten → 가중 선형합(Σw=1.0, 역채점 s\*=11−s), normative 입력 전제.
- UCF Great Eight(잠재력 평면) + Leader Edge 5종(우위이자 칼날, 그림자 모델링).
- 그림자 점등 규칙(Edge≥8 & 균형추≤3)이 EX 신호가 검증할 선험적 가설 → [[bp-signal-intelligence]] Disposition 선행 소스.
- 다음 갈래(대기): (1) 가중치 JSON/파이썬 계산 엔진, (2) Watch/Alert/Critical 간극 정량화 판정 로직.
