# Extracted Knowledge from Conv: 7bcde490-1862-4bff-b2d4-5775e9acedf6

**Date**: 2026-01-29T01:00:42.399984Z

### Extracted Code (text)

```text
추적 대상:
├─ 미국 국채 수익률 곡선 (실시간)
│  ├─ 2년물 vs 10년물 스프레드 (경기 전환점 예측)
│  ├─ 10년물 실질금리 (자금의 기회비용)
│  └─ TIP(물가연동채) vs 명목채 스프레드 (인플레이션 기대)
│
├─ 회사채 스프레드
│  ├─ 하이일드 스프레드 확대 → 위험자산 이탈 신호
│  └─ IG-하이일드 스프레드 → 신용 경색 조짐
│
└─ 국가별 국채 금리차
   ├─ 한미 금리차 (원화 압력)
   ├─ 독미 금리차 (유로 압력)
   └─ 일미 금리차 (엔화 압력)
```

### Extracted Code (python)

```python
# 실시간 모니터링 지표
currency_flow_indicators = {
    # 직접 지표
    "DXY": "달러 인덱스 (전체 자금 방향)",
    "USDKRW": "원달러 환율 (한국 유출입)",
    "USDJPY": "달러엔 (캐리트레이드 상태)",
    
    # 간접 지표
    "VIX": "변동성 지수 (공포도)",
    "MOVE": "채권 변동성 (채권시장 스트레스)",
    
    # 크로스 레이트
    "EURUSD": "유럽→미국 자금 흐름",
    "AUDUSD": "위험선호도 (호주달러=원자재 통화)",
}
```

### Extracted Code (text)

```text
일일 모니터링 대상:

【미국 주식】
├─ SPY (S&P 500) - 기관 선호
├─ QQQ (나스닥) - 성장주 선호도
└─ IWM (러셀2000) - 중소형주 = 위험선호도

【채권】
├─ TLT (장기 국채) - 안전자산 수요
├─ SHY (단기 국채) - 현금 대체
└─ HYG (하이일드) - 신용 위험 선호도

【섹터별】
├─ XLF (금융) - 경기 민감
├─ XLE (에너지) - 인플레이션 헤지
├─ XLV (헬스케어) - 방어적 포지션
└─ XLK (기술) - 성장 기대

【국가별】
├─ EWY (한국) - 한국 유출입 직접 관측
├─ EWJ (일본)
└─ EEM (이머징 전체)
```

### Extracted Code (text)

```text
옵션 시장 체크:
├─ Put/Call Ratio (공포/탐욕 비율)
├─ Skew Index (꼬리 위험 프리미엄)
├─ Open Interest 변화 (대형 포지션 구축)
└─ 옵션 만기일 (감마 스퀴즈 가능성)

선물 시장:
├─ COT Report (상품선물거래위원회 보고서)
│  └─ 상업적 헤저 vs 투기꾼 포지션
├─ Basis (현물-선물 차이)
└─ Contango/Backwardation (시장 구조)
```

### Extracted Code (python)

```python
# 무료 + 유료 조합 전략
data_sources = {
    "실시간 (무료)": {
        "Yahoo Finance API": "주식, ETF, 환율",
        "FRED API": "경제지표, 국채금리",
        "Investing.com": "글로벌 지수, 원자재",
        "TradingView": "기술적 지표, 차트",
    },
    
    "기관급 데이터 (유료이지만 필수)": {
        "Bloomberg Terminal": "전방위 데이터 + 뉴스",
        "Refinitiv Eikon": "자금흐름 분석 특화",
        "FactSet": "ETF flow 데이터 최강",
    },
    
    "대안 데이터 (엣지 확보)": {
        "Unusual Whales": "옵션 플로우",
        "Quiver Quantitative": "의회 거래, 내부자 거래",
        "Whale Wisdom": "13F 헤지펀드 포지션",
    }
}
```

### Extracted Code (text)

```text
대시보드 구조:

[LEVEL 1: 거시 환경]
├─ 금리 환경 (Fed Funds Rate, 국채 곡선)
├─ 달러 강도 (DXY)
└─ 글로벌 유동성 (Fed+ECB+BOJ 밸런스시트)

[LEVEL 2: 자금 흐름 방향]
├─ 채권 ETF 플로우 (TLT, HYG, LQD)
├─ 주식 ETF 플로우 (SPY, QQQ, IWM)
├─ 섹터 로테이션 (상대 강도)
└─ 국가별 플로우 (EWY, EWJ, EEM)

[LEVEL 3: 센티먼트]
├─ VIX (공포 지수)
├─ Put/Call Ratio
├─ 하이일드 스프레드
└─ 신용 스프레드

[LEVEL 4: 실시간 트리거]
├─ 비정상 거래량 알림
├─ 급격한 환율 변동
├─ 옵션 대량 거래
└─ 뉴스 이벤트 (Fed, 지정학적 리스크)
```

### Extracted Code (python)

```python
# 개념적 구조 (실제 구현은 복잡함)

class MoneyFlowScanner:
    """
    매 시간마다 자금 흐름 이상 징후 탐지
    """
    
    def scan_anomalies(self):
        signals = []
        
        # 1. 채권 시장 신호
        if self.treasury_yield_spike() > 2_std_deviation:
            signals.append("국채 급등락 - 유동성 경색 가능")
        
        # 2. ETF 플로우 이상
        if self.etf_outflow(['SPY', 'QQQ']) > threshold:
            signals.append("주식형 ETF 대규모 유출")
        
        # 3. 통화 압력
        if self.usdkrw_acceleration() > critical_level:
            signals.append("원화 약세 가속 - 외국인 이탈")
        
        # 4. 크로스 체크
        if self.vix_spike() and self.hyg_spread_widening():
            signals.append("⚠️ 리스크오프 전환 신호")
        
        return self.prioritize_signals(signals)
    
    def predict_next_move(self):
        """
        과거 패턴 매칭 + 머신러닝 조합
        """
        current_state = self.get_market_state()
        historical_matches = self.find_similar_episodes()
        
        # 과거 유사 상황에서 24-48시간 후 어떻게 됐나?
        return self.forecast_probability_distribution()
```

### Extracted Code (text)

```text
트리거 체인:
1. 한미 금리차 역전 (-0.5%p 이상)
   ↓
2. USDKRW 급등 (1일 +1% 이상)
   ↓
3. EWY(한국 ETF) 3일 연속 순유출
   ↓
4. KOSPI 외국인 순매도 가속
   ↓
[결론] 외국인 자금 이탈 본격화
→ 포지션 축소 또는 헤지 검토
```

### Extracted Code (text)

```text
신호 조합:
1. VIX 20 → 30 급등
2. TLT(장기채 ETF) 대량 유입
3. HYG(하이일드) 스프레드 확대
4. 금 가격 상승 + 달러 강세 동시 발생

[해석] 
"퀄리티로의 도피" (Flight to Quality)
→ 주식 비중 축소
→ 현금/단기채 확보
→ 변동성 낮아질 때까지 대기
```

### Extracted Code (text)

```text
위험 신호:
1. LIBOR-OIS 스프레드 급등
2. 레포 금리 스파이크
3. MOVE 지수 (채권 변동성) 급등
4. 회사채 발행 급감

[해석]
은행 간 신뢰 무너짐 → 2008년 재현?
→ 극도로 보수적 포지션
→ 현금 확보 최우선
```

### Extracted Code (text)

```text
📊 자금흐름 추적 시스템
├─ 📈 일일 대시보드
│  ├─ 오늘의 주요 지표 스냅샷
│  ├─ 이상 신호 감지 로그
│  └─ AI 해석 (Claude/GPT 요약)
│
├─ 📚 플레이북 라이브러리
│  ├─ 시나리오별 대응 매뉴얼
│  ├─ 과거 유사 사례 (2008, 2020 등)
│  └─ 실패 사례 분석
│
├─ 🔔 실시간 알림 규칙
│  ├─ 임계값 설정 (VIX>30, USDKRW>1400 등)
│  ├─ 알림 채널 (Slack, Email, SMS)
│  └─ 액션 체크리스트
│
└─ 📊 백테스팅 결과
   ├─ 신호 정확도 추적
   ├─ 오경보 분석
   └─ 지속적 개선 로그
```
