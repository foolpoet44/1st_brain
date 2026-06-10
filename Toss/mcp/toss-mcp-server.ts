import { TossConnector } from "../src/connectors/TossConnector.ts";
import { TossAssetAdapter } from "../src/adapters/TossAssetAdapter.ts";
import { InvestmentMandate } from "../src/types/toss.d.ts";

/**
 * Toss MCP Server Implementation
 * LLM 에이전트가 직접 호출할 수 있는 도구 규격 정의
 */

const defaultMandate: InvestmentMandate = {
  maxDailyTransactionAmount: 1000000,
  allowedSymbols: ["069500", "102110", "453810"], // KODEX 200, TIGER 200, KODEX 미국S&P500 등 배당/안전주 예시
  riskScoreLimit: 70,
  killSwitchActive: false,
};

const connector = new TossConnector(defaultMandate);
const adapter = new TossAssetAdapter(connector);

export const tossTools = {
  /**
   * 계좌 잔고 및 종목별 현재가 조회
   */
  get_balances: async (symbols: string[]) => {
    try {
      const prices = await adapter.getPrices(symbols);
      return {
        success: true,
        data: Object.fromEntries(prices),
        timestamp: new Date().toISOString(),
      };
    } catch (error: any) {
      return { success: false, error: error.message };
    }
  },

  /**
   * 특정 종목 주문 실행 (Mandate 가드레일 작동)
   */
  place_order: async (args: {
    symbol: string;
    side: "BUY" | "SELL";
    amount: number;
  }) => {
    try {
      const result = await connector.placeOrder(
        args.symbol,
        args.side,
        args.amount,
      );
      return {
        success: true,
        order_id: `toss-${Date.now()}`,
        ...result,
      };
    } catch (error: any) {
      return {
        success: false,
        error: error.message,
        reason: error.message.includes("MANDATE")
          ? "Security Violation"
          : "System Error",
      };
    }
  },

  /**
   * 킬 스위치 상태 확인 및 제어 (긴급 상황용)
   */
  check_safety: async () => {
    return {
      killSwitchActive: defaultMandate.killSwitchActive,
      dailyLimit: defaultMandate.maxDailyTransactionAmount,
      allowedUniverse: defaultMandate.allowedSymbols,
    };
  },
};
