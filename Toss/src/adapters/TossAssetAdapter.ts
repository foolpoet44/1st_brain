import { TossConnector } from "../connectors/TossConnector.ts";
import {
  TossPriceResponse,
  TossCandleResponse,
  AssetPrice,
  Candle,
} from "../types/toss.d.ts";

/**
 * TossAssetAdapter: 토스 고유 규격을 서비스 표준 인터페이스로 변환
 * "시장의 노이즈를 걸러내고 에이전트가 이해할 수 있는 정제된 데이터로 변환한다."
 */
export class TossAssetAdapter {
  private connector: TossConnector;

  constructor(connector: TossConnector) {
    this.connector = connector;
  }

  /**
   * 여러 종목의 현재가를 조회하여 정제된 맵으로 반환
   */
  public async getPrices(symbols: string[]): Promise<Map<string, AssetPrice>> {
    const out = new Map<string, AssetPrice>();

    // 200개씩 청크 분할 처리 (API 제한 대응)
    for (let i = 0; i < symbols.length; i += 200) {
      const chunk = symbols.slice(i, i + 200);
      const json = await this.connector.authedGet<TossPriceResponse>(
        "/api/v1/prices",
        {
          symbols: chunk.join(","),
        },
      );

      const rows = json.prices || json.data || [];
      for (const row of rows) {
        const code = row.symbol || row.code;
        if (!code) continue;

        out.set(code, {
          price: this.parseNum(row.price ?? row.close ?? row.last),
          change: this.parseNum(row.change),
          changeRate: this.parseNum(row.changeRate ?? row.rate),
        });
      }
    }
    return out;
  }

  /**
   * 일봉 데이터를 조회하여 정제된 리스트로 반환 (과거 -> 현재 정렬)
   */
  public async getCandles(
    symbol: string,
    days: number = 260,
  ): Promise<Candle[]> {
    const collected: Candle[] = [];
    let before: string | number | undefined = undefined;

    while (collected.length < days) {
      const params: Record<string, string | number> = {
        symbol,
        interval: "1d",
        count: 200,
      };
      if (before) params.before = before;

      const json = await this.connector.authedGet<TossCandleResponse>(
        "/api/v1/candles",
        params,
      );
      const rows = json.candles || json.data || [];
      if (!rows.length) break;

      for (const r of rows) {
        collected.push({
          time: r.time ?? r.timestamp ?? r.date ?? "",
          close: this.parseNum(r.close ?? r.c),
        });
      }

      const lastRow = rows[rows.length - 1];
      before = lastRow.time ?? lastRow.timestamp;
      if (rows.length < 200) break;
    }

    // 중복 제거 및 시간순 정렬
    return this.dedupeAndSort(collected).slice(-days);
  }

  private parseNum(v: any): number | null {
    if (v === undefined || v === null) return null;
    const n = typeof v === "string" ? parseFloat(v.replace(/,/g, "")) : v;
    return Number.isFinite(n) ? n : null;
  }

  private dedupeAndSort(rows: Candle[]): Candle[] {
    const seen = new Set();
    return rows
      .filter((r) => {
        const k = String(r.time);
        if (seen.has(k)) return false;
        seen.add(k);
        return true;
      })
      .sort((a, b) => String(a.time).localeCompare(String(b.time)));
  }
}
