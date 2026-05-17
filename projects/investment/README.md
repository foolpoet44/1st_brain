---
type: Project
status: Active
tags: [investment, finance, automation, portfolio]
related_to: "[[weak-signal-ansoff]]", "[[daishin-report-search]]"
---

# Global Investment Strategy 2026

## 1. Investment Thesis: "The Taco Rebound"

2026년 1월 대신증권 리포트 분석 결과, 글로벌 증시는 '방향'이 아닌 '속도'의 조정을 겪는 중입니다. 미-EU 간의 갈등은 극한 대립보다는 협상(TACO)으로 흘러갈 가능성이 높으며, 이는 증시의 지속적인 동력이 될 것입니다.

## 2. Weak Signal Dashboard

- **시그널 1 (L4 IMPACT)**: 비농업 부문 고용 추세 감소 (-2.2만 명). → **해석**: 연준의 비둘기파적 전환(Pivot) 시그널.
- **시그널 2 (L2 SOURCE)**: 트럼프 2기 자국 우선주의 강화. → **해석**: 반도체/에너지 공급망의 물리적 재편 가속화.
- **시그널 3 (L3 ISSUE)**: 그린란드 영토 분쟁. → **해석**: 지정학적 변동성은 단기 노이즈, 실질적 무력 충돌 가능성은 희박.

## 3. Target Portfolio Weights (Proposed)

- **Core (Growth)**: QQQ (미국 기술주) - 40% (AI 인프라 선점)
- **Strategic (Value)**: EWY (한국 국국) - 20% (상법 개정/배당 세제 기대)
- **Theme (Future)**: BOTZ (로봇), URA (원전) - 20%
- **Defensive (Hedge)**: GLD (금), Cash - 20%

## 4. Automation Logic: "Do it once, automate it forever"

- [ ] **Data Crawler**: `daishin-report-search` 스킬을 활용해 매주 월요일 '고용' 및 '금리' 키워드 리포트 자동 파싱.
- [ ] **Signal Scorer**: 파싱된 데이터에서 수치 변화 감지 시 텔레그램으로 `[Weak Signal ALERT]` 전송.
- [ ] **Insight Linker**: 애널리스트(예: 문남중)의 의견을 `wiki/people/`에 자동 이력 관리.
