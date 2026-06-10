/**
 * Toss Securities Open API Types
 */

export interface TossTokenResponse {
  access_token: string;
  token_type: string;
  expires_in: number;
  scope?: string;
}

export interface TossPriceRow {
  symbol?: string;
  code?: string;
  price?: number | string;
  close?: number | string;
  last?: number | string;
  change?: number | string;
  changeRate?: number | string;
  rate?: number | string;
}

export interface TossPriceResponse {
  prices?: TossPriceRow[];
  data?: TossPriceRow[];
}

export interface TossCandleRow {
  time?: string | number;
  timestamp?: string | number;
  date?: string | number;
  close?: number | string;
  c?: number | string;
}

export interface TossCandleResponse {
  candles?: TossCandleRow[];
  data?: TossCandleRow[];
}

export interface AssetPrice {
  price: number | null;
  change: number | null;
  changeRate: number | null;
}

export interface Candle {
  time: string | number;
  close: number | null;
}

/**
 * Investment Mandate - 에이전트 가드레일 규격
 */
export interface InvestmentMandate {
  maxDailyTransactionAmount: number; // 하루 최대 누적 거래 대금 (KRW)
  allowedSymbols: string[]; // 매수 가능 종목 유니버스
  riskScoreLimit: number; // 허용 리스크 점수
  killSwitchActive: boolean; // 소프트웨어적 킬 스위치
}
