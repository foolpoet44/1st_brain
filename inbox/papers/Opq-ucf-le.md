---
status: Inbox
type: Note
source: gdrive
original_title: "Opq-ucf-le"
drive_id: 15KCJvf_oagg2VAblY-GgZ7xpanrC5WXSDLSUbULwOEQ
pulled: 2026-07-18
processed: true
---

좋습니다. 캐러밴이 어디로 가는지 아는 사람과 설계하는 건 즐거운 일입니다. 군더더기 빼고 로직으로 바로 들어가죠.

먼저 두 프로파일의 성격을 분명히 구분하고 시작하는 게 중요합니다. **UCF는 "이 사람이 직무 역량을 발휘할 잠재력의 폭"을 묻고, Leader Edge는 "리더로서의 차별적 우위 — 그리고 그 우위가 칼날처럼 뒤집히는 지점"을 묻습니다.** UCF가 평면이라면 Leader Edge는 벡터이자 양날입니다. 같은 OPQ 스케일이 두 프로파일에 모두 들어가지만, 가중치도 다르고 무엇보다 Leader Edge는 _그림자(dark-side)_ 를 명시적으로 모델링한다는 점에서 결이 다릅니다. 이 비대칭이 나중에 Intellig[[Understand-Anything/understand-anything-plugin/skills/understand/locales/en.md|en]]ce 레이어로 가는 다리가 됩니다.

## 공통 산출 엔진

두 프로파일 모두 동일한 변환 파이프라인을 탑니다.

입력은 OPQ32 sten(1–10) 32개. 역채점 스케일은 `s* = 11 − s`로 변환합니다(아래 표에서 _R_ 표기). 각 역량/엣지는 관련 스케일의 가중 선형합이며, **가중치 총합을 1.0으로 고정**했기 때문에 산출값이 그대로 1–10 스케일 위에 떨어집니다.

```
Score(C) = Σ wᵢ · sᵢ*      (단, Σwᵢ = 1.0, 역채점은 sᵢ* = 11 − sᵢ)
밴드:  1–3 낮음 / 4–5 중하 / 6–7 중상 / 8–10 높음
```

ipsative(강제선택) 데이터면 이 선형합 자체가 통계적으로 오염된다는 점은 이미 짚었으니 반복하지 않겠습니다. normative(OPQ32r/IRT) 입력이라는 전제만 확인하고 진행합니다.

## ① OPQ32 → UCF Great Eight

SHL의 OPQ–UCF 연결 논리를 따르되, 가중치는 투명한 3-tier(강 0.25–0.30 / 중 0.15–0.20 / 약 0.10)로 재구성했습니다. 설명가능성이 코칭 신뢰의 전제이므로 1차는 의도적으로 규칙기반입니다.

| Great Eight                       | 앵커(강)                                                                                              | 지지(중)                                  | 변조(약)                                                                          |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------- | --------------------------------------------------------------------------------- | ------------------------- |
| **1. Leading & Deciding**         | Controlling .30, Decisive .25                                                                         | Persuasive .15                            | Independent Minded .10, Outspoken .10, Socially Confident .10                     |
| **2. Supporting & Cooperating**   | Caring .30, Democratic .25                                                                            | Affiliative .20                           | T[[Understand-Anything/understand-anything-plugin/skills/understand/locales/ru.md | ru]]sting .15, Modest .10 |
| **3. Interacting & Presenting**   | Persuasive .25, Out[[Understand-Anything/understand-anything-plugin/skills/understand/languages/go.md | go]]ing .25, Socially Confident .25       | Affiliative .15                                                                   | Outspoken .10             |
| **4. Analysing & Interpreting**   | Data Rational .30, Evaluative .30                                                                     | Behavioural .20                           | Conceptual .10, Detail Conscious .10                                              |
| **5. Creating & Conceptualising** | Innovative .30, Conceptual .25                                                                        | Variety Seeking .15, Forward Thinking .15 | Adaptable .15                                                                     |
| **6. Organising & Executing**     | Conscientious .30, Detail Conscious .25                                                               | Forward Thinking .20                      | Rule Following .15, Achieving .10                                                 |
| **7. Adapting & Coping**          | Adaptable .25, Relaxed .25                                                                            | Tough Minded .20                          | Optimistic .15, Worrying _R_ .15                                                  |
| **8. Enterprising & Performing**  | Achieving .30                                                                                         | Competitive .20, Vigorous .20             | Decisive .15, Forward Thinking .15                                                |

여기까지가 "직무 역량 잠재력 지도"입니다. 8개 막대가 그 사람의 일하는 방식의 윤곽을 그려주죠. 하지만 리더십은 8개 역량의 평균이 아닙니다. 그래서 두 번째 층이 필요합니다.

## ② OPQ32 → Leader Edge

리더십 공간을 다섯 개의 *엣지*로 압축합니다. 각 엣지는 OPQ 합성치(밝은 면)와, 그 합성치가 균형추를 잃었을 때 드러나는 *그림자*를 한 쌍으로 갖습니다. 'Edge'를 우위(advantage)이자 칼날(blade)로 동시에 읽는 게 이 설계의 핵심입니다 — 모든 리더십 강점은 압박 하에서 자기 자신의 탈선 위험으로 뒤집히니까요.

| Leader Edge                    | OPQ 합성                                                                                    | 밝은 면 (Bright)                  | 그림자 (Dark)                     | 심리 프레임                    |
| ------------------------------ | ------------------------------------------------------------------------------------------- | --------------------------------- | --------------------------------- | ------------------------------ |
| **Strategic Edge** 전략적 통찰 | Forward Thinking .30, Conceptual .30, Innovative .25, Variety Seeking .15                   | 미래 프레이밍·패턴 인식·방향 제시 | 현실 이탈, 실행 경시, 공상        | Direction & Meaning            |
| **Influence Edge** 영향력      | Persuasive .30, Controlling .25, Socially Confident .25, Outspoken .20                      | 설득·동원·존재감                  | 지배·의사결정 독점·마이크로매니징 | LMX                            |
| **Drive Edge** 추진력          | Achieving .30, Decisive .25, Competitive .25, Vigorous .20                                  | 결과 창출·속도·집요함             | 단기주의, 팀 소진, 관계 희생      | JD-R(요구)                     |
| **People Edge** 사람 중심      | Caring .30, Democratic .25, Affiliative .25, Trusting .20                                   | 심리적 안전·육성·신뢰             | 갈등 회피·결정 지연·과합의        | SDT 관계성 / POS               |
| **Resilience Edge** 회복탄력   | Relaxed .25, Tough Minded .25, Optimistic .20, Emotionally Controlled .15, Worrying _R_ .15 | 압박 하 안정·평정                 | 정서 둔감·공감 차단·무사안일      | JD-R(자원) / Energy & Survival |

## 그림자가 켜지는 규칙 — 두 층을 잇는 다리

Leader Edge가 단순한 강점 막대가 아니라 *인텔리전스의 씨앗*이 되는 건 바로 이 균형추 로직 때문입니다. 어떤 엣지가 높다는 사실만으로는 위험이 아닙니다. **높은 엣지가 자신의 천연 균형추를 잃었을 때** 비로소 그림자가 켜집니다.

```
IF  Edge_score ≥ 8  AND  Counterbalancer ≤ 3  →  Dark-risk 플래그 점등
```

- Influence Edge↑ + People Edge↓ → **지배형** (정서 차단·독점 의사결정)
- Drive Edge↑ + People Edge↓ → **소진형** (성과를 위한 사람 갈아넣기)
- Strategic Edge↑ + UCF#6(Organising&Executing)↓ → **공상형** (비전은 화려하나 착지 못 함)
- People Edge↑ + Drive Edge↓ → **무결정형** (따뜻하지만 끌고 가지 못함)
- Resilience Edge↑ + People Edge↓ → **냉담형** (자기는 흔들림 없으나 타인 신호에 둔감)

이 플래그가 바로 지난번에 합의한 구조의 **선험적 경보 — 즉 EX 신호가 검증할 *가설***입니다. OPQ만으로 "이 리더는 변화 압력 하에서 지배형 탈선 가능성"이라는 사전확률을 던지고, 이후 360·Pulse·BP Report가 그 가설을 행동 데이터로 확인(A–D 등급)하면 Watch가 Alert로, Alert가 Critical로 수렴합니다. UCF×Leader Edge의 교차가 Disposition 레이어를 완성하고, 그 출력이 Signal Generation의 _선행_ 소스로 들어가는 거죠. People Context Graph의 개인 노드 속성이 여기서 채워집니다.

마지막으로 출력 문법 한 줄만. 모든 산출은 "이 리더는 ~형이다"가 아니라 "~경향이 ~만큼 잠재되어 있고, 관측이 그것을 ~만큼 지지한다"로 적힙니다. 판결이 아니라 가설 — 그 문법이 시스템의 품격을 정합니다.

---

다음 두 갈래 중 어디로 갈까요. (1) 이 산출 로직을 실제 **계산 엔진(파이썬 모듈 또는 가중치 JSON 스키마)**으로 떨어뜨리거나, (2) Disposition 레이어 → Watch/Alert/Critical로 가는 **간극 정량화·판정 로직**(지난번 2번)으로 넘어가는 것. 코드나 파일 생성은 방향 확정하고 확인받은 뒤 진행하겠습니다.
