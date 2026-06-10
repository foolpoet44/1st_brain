import {
  TossTokenResponse,
  TossPriceResponse,
  TossCandleResponse,
  InvestmentMandate,
} from "../types/toss.d.ts";

/**
 * TossConnector: 토스증권 Open API와의 저수준 통신 및 가드레일 관리
 * "자극과 반응 사이의 공간을 코드로 지배한다."
 */
export class TossConnector {
  private tokenCache: { token: string | null; expiresAt: number } = {
    token: null,
    expiresAt: 0,
  };
  private mandate: InvestmentMandate;
  private dailyVolume: number = 0; // 오늘 누적 거래량 (단순화된 예시)

  constructor(mandate?: InvestmentMandate) {
    this.mandate = mandate || {
      maxDailyTransactionAmount: 1000000,
      allowedSymbols: [], // Empty means all allowed for simplicity in mock, but should be restrictive
      riskScoreLimit: 70,
      killSwitchActive: false,
    };
  }

  private get baseUrl(): string {
    return process.env.TOSS_BASE_URL || "https://openapi.tossinvest.com";
  }

  private get clientId(): string | undefined {
    return process.env.TOSS_CLIENT_ID;
  }

  private get clientSecret(): string | undefined {
    return process.env.TOSS_CLIENT_SECRET;
  }

  public isMock(): boolean {
    return !this.clientId || !this.clientSecret;
  }

  /**
   * 가드레일 체크: 킬 스위치 및 거래 한도 확인
   */
  private checkGuardrails(amount: number = 0): void {
    if (this.mandate.killSwitchActive) {
      throw new Error(
        "FAIL-CLOSED: Kill switch is active. All transactions frozen.",
      );
    }

    if (this.dailyVolume + amount > this.mandate.maxDailyTransactionAmount) {
      throw new Error(
        `MANDATE VIOLATION: Exceeds daily transaction limit of ${this.mandate.maxDailyTransactionAmount}`,
      );
    }
  }

  private async getAccessToken(): Promise<string> {
    const now = Date.now();
    if (this.tokenCache.token && now < this.tokenCache.expiresAt - 30000) {
      return this.tokenCache.token;
    }

    if (this.isMock()) return "mock-token";

    const body = new URLSearchParams({
      grant_type: "client_credentials",
      client_id: this.clientId!,
      client_secret: this.clientSecret!,
    });

    const res = await fetch(`${this.baseUrl}/oauth2/token`, {
      method: "POST",
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
      body,
    });

    if (!res.ok) throw new Error(`Toss OAuth 실패: ${res.status}`);

    const json = (await res.json()) as TossTokenResponse;
    const ttl = (json.expires_in || 3600) * 1000;
    this.tokenCache = { token: json.access_token, expiresAt: now + ttl };
    return json.access_token;
  }

  public async authedGet<T>(
    path: string,
    params: Record<string, string | number> = {},
  ): Promise<T> {
    this.checkGuardrails(); // 읽기 작업에서도 킬 스위치 체크

    const token = await this.getAccessToken();
    const url = new URL(`${this.baseUrl}${path}`);
    Object.entries(params).forEach(([k, v]) =>
      url.searchParams.set(k, String(v)),
    );

    const res = await fetch(url, {
      headers: { Authorization: `Bearer ${token}` },
    });

    if (!res.ok) throw new Error(`Toss API ${path} 실패: ${res.status}`);
    return res.json() as Promise<T>;
  }

  /**
   * 주문 실행 (가드레일 검증 포함)
   */
  public async placeOrder(
    symbol: string,
    side: "BUY" | "SELL",
    amount: number,
  ): Promise<any> {
    this.checkGuardrails(amount);

    if (
      this.mandate.allowedSymbols.length > 0 &&
      !this.mandate.allowedSymbols.includes(symbol)
    ) {
      throw new Error(
        `MANDATE VIOLATION: Symbol ${symbol} is not in the allowed universe.`,
      );
    }

    console.log(
      `[ORDER] Executing ${side} for ${symbol} with amount ${amount}`,
    );

    // 실제 주문 로직은 Mock 생략 또는 API 연동
    this.dailyVolume += amount;
    return {
      success: true,
      symbol,
      side,
      amount,
      timestamp: new Date().toISOString(),
    };
  }
}
