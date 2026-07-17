---
title: "OPQ32 (Occupational Personality Questionnaire) Framework"
created: 2026-04-29
updated: 2026-07-18
status: growing
type: concept
tags: [hr, psychology, assessment, opq32]
related_to: "[[oka-project]]"
---

# OPQ32 (Occupational Personality Questionnaire) Framework

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

이 Disposition 레이어의 출력이 [[bp-signal-intelligence]] Signal Generation의 *선행* 소스로 들어가 People Context Graph 개인 노드 속성을 채웁니다. 심리 프레임 매핑(Direction&Meaning·LMX·JD-R·SDT·POS)은 [[ex-insight-mining-pipeline]]의 연역 평정 격자와 동일 좌표계입니다. 리더 선발 역량은 projects/physical-ai-talent 면접 키트와 교차 검증됩니다.

---

## Timeline

### 2026-07-18

- Drive 설계문서에서 편입: **OPQ → UCF / Leader Edge 산출 로직** (Opq-ucf-le).
- 공통 산출 엔진: OPQ32 sten → 가중 선형합(Σw=1.0, 역채점 s*=11−s), normative 입력 전제.
- UCF Great Eight(잠재력 평면) + Leader Edge 5종(우위이자 칼날, 그림자 모델링).
- 그림자 점등 규칙(Edge≥8 & 균형추≤3)이 EX 신호가 검증할 선험적 가설 → [[bp-signal-intelligence]] Disposition 선행 소스.
- 다음 갈래(대기): (1) 가중치 JSON/파이썬 계산 엔진, (2) Watch/Alert/Critical 간극 정량화 판정 로직.
