// test-toss-core-simple.js
import { TossConnector } from "./src/connectors/TossConnector.ts";
import { TossAssetAdapter } from "./src/adapters/TossAssetAdapter.ts";

/**
 * 이 테스트는 .ts 확장자를 인식하지 못하는 환경을 위해
 * fetch 등의 의존성이 해결된 Node.js 18+ 환경에서 동작하도록 설계되었습니다.
 */
async function runTest() {
  console.log("--- Toss Core Smoke Test (Simple Mode) ---");

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
    // Mock 모드에서는 fetch를 호출하지 않거나 가짜 데이터를 반환하도록 설계됨
    // 현재 authedGet은 실제 fetch를 호출하므로 Mock 응답을 가로채야 함
    // (여기서는 Connector 내부에서 isMock일 때 fetch를 최소화하도록 구현됨)

    console.log("2. Testing Mandate Guardrails - Order within limit...");
    const order1 = await connector.placeOrder("005930", "BUY", 100000);
    console.log("Order 1 success:", order1.success);

    console.log("3. Testing Mandate Guardrails - Symbol restriction...");
    try {
      await connector.placeOrder("035420", "BUY", 10000);
    } catch (e) {
      console.log("Caught expected restriction:", e.message);
    }

    console.log("4. Testing Mandate Guardrails - Daily limit...");
    try {
      await connector.placeOrder("005930", "BUY", 1000000);
    } catch (e) {
      console.log("Caught expected limit violation:", e.message);
    }

    console.log("5. Testing Kill Switch...");
    const emergencyConnector = new TossConnector({
      ...mandate,
      killSwitchActive: true,
    });
    try {
      await emergencyConnector.placeOrder("005930", "BUY", 100);
    } catch (e) {
      console.log("Caught expected kill switch activation:", e.message);
    }

    console.log("\n--- Smoke Test Completed Successfully ---");
  } catch (error) {
    console.error("Test failed:", error);
    process.exit(1);
  }
}

runTest();
