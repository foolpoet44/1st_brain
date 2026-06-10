import { TossConnector } from "./connectors/TossConnector.ts";
import { TossAssetAdapter } from "./adapters/TossAssetAdapter.ts";

async function runTest() {
  console.log("--- Toss Core Smoke Test (Mock Mode) ---");

  const mandate = {
    maxDailyTransactionAmount: 500000,
    allowedSymbols: ["005930", "000660"], // 삼성전자, SK하이닉스
    riskScoreLimit: 80,
    killSwitchActive: false,
  };

  const connector = new TossConnector(mandate);
  const adapter = new TossAssetAdapter(connector);

  console.log("1. Testing Connector Mock Mode...");
  console.log(`Is Mock? ${connector.isMock()}`);

  try {
    console.log("2. Testing Asset Adapter - getPrices...");
    const prices = await adapter.getPrices(["005930", "000660"]);
    console.log("Prices retrieved:", Object.fromEntries(prices));

    console.log("3. Testing Mandate Guardrails - Order within limit...");
    const order1 = await connector.placeOrder("005930", "BUY", 100000);
    console.log("Order 1 success:", order1.success);

    console.log("4. Testing Mandate Guardrails - Symbol restriction...");
    try {
      await connector.placeOrder("035420", "BUY", 10000); // NAVER (not in allowedSymbols)
    } catch (e: any) {
      console.log("Caught expected restriction:", e.message);
    }

    console.log("5. Testing Mandate Guardrails - Daily limit...");
    try {
      await connector.placeOrder("005930", "BUY", 1000000); // Exceeds 500k
    } catch (e: any) {
      console.log("Caught expected limit violation:", e.message);
    }

    console.log("6. Testing Kill Switch...");
    const emergencyConnector = new TossConnector({
      ...mandate,
      killSwitchActive: true,
    });
    try {
      await emergencyConnector.authedGet("/api/v1/prices");
    } catch (e: any) {
      console.log("Caught expected kill switch activation:", e.message);
    }

    console.log("\n--- Smoke Test Completed Successfully ---");
  } catch (error) {
    console.error("Test failed:", error);
    process.exit(1);
  }
}

runTest();
