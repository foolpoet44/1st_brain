# Extracted Knowledge from Conv: c09e9d99-e95a-4f67-8899-bcbaef5c7fe9

**Date**: 2026-03-11T23:34:45.938393Z

### Extracted Code (jsx)

```jsx
import { useState, useEffect } from "react";

const STOCKS = [
  { rank: 1, name: "삼성전자", code: "005930", sector: "반도체" },
  { rank: 2, name: "SK하이닉스", code: "000660", sector: "반도체" },
  { rank: 3, name: "현대차", code: "005380", sector: "자동차" },
  { rank: 4, name: "삼성전자우", code: "005935", sector: "반도체" },
  { rank: 5, name: "LG에너지솔루션", code: "373220", sector: "배터리" },
  { rank: 6, name: "삼성바이오로직스", code: "207940", sector: "바이오" },
  { rank: 7, name: "SK스퀘어", code: "402340", sector: "지주" },
  { rank: 8, name: "한화에어로스페이스", code: "012450", sector: "방산" },
  { rank: 9, name: "두산에너빌리티", code: "034020", sector: "발전/원자력" },
  { rank: 10, name: "기아", code: "000270", sector: "자동차" },
  { rank: 11, name: "HD현대중공업", code: "329180", sector: "조선" },
  { rank: 12, name: "KB금융", code: "105560", sector: "금융" },
  { rank: 13, name: "삼성물산", code: "028260", sector: "지주/건설" },
  { rank: 14, name: "신한지주", code: "055550", sector: "금융" },
  { rank: 15, name: "HD한국조선해양", code: "009540", sector: "조선" },
  { rank: 16, name: "삼성SDI", code: "006400", sector: "배터리" },
  { rank: 17, name: "포스코홀딩스", code: "005490", sector: "철강" },
  { rank: 18, name: "SK텔레콤", code: "017670", sector: "통신" },
  { rank: 19, name: "한화시스템", code: "272210", sector: "방산" },
  { rank: 20, name: "하나금융지주", code: "086790", sector: "금융" },
  { rank: 21, name: "현대모비스", code: "012330", sector: "자동차부품" },
  { rank: 22, name: "한국항공우주", code: "047810", sector: "방산" },
  { rank: 23, name: "LG전자", code: "066570", sector: "전자" },
  { rank: 24, name: "삼성전기", code: "009150", sector: "전자부품" },
  { rank: 25, name: "SK이노베이션", code: "096770", sector: "에너지/배터리" },
  { rank: 26, name: "미래에셋증권", code: "006800", sector: "증권" },
  { rank: 27, name: "우리금융지주", code: "316140", sector: "금융" },
  { rank: 28, name: "한국전력", code: "015760", sector: "전력" },
  { rank: 29, name: "SK㈜", code: "034730", sector: "지주" },
  { rank: 30, name: "LG화학", code: "051910", sector: "화학/배터리" },
  { rank: 31, name: "현대글로비스", code: "086280", sector: "물류" },
  { rank: 32, name: "HD현대", code: "267250", sector: "지주/조선" },
  { rank: 33, name: "롯데지주", code: "004990", sector: "지주" },
  { rank: 34, name: "S-Oil", code: "010950", sector: "정유" },
  { rank: 35, name: "삼성중공업", code: "010140", sector: "조선" },
  { rank: 36, name: "LS", code: "006260", sector: "전선/에너지" },
  { rank: 37, name: "두산", code: "000150", sector: "지주" },
  { rank: 38, name: "KT", code: "030200", sector: "통신" },
  { rank: 39, name: "LG", code: "003550", sector: "지주" },
  { rank: 40, name: "네이버", code: "035420", sector: "플랫폼" },
  { rank: 41, name: "SK스퀘어", code: "402340", sector: "지주" },
  { rank: 42, name: "현대건설", code: "000720", sector: "건설" },
  { rank: 43, name: "한국조선해양", code: "009540", sector: "조선" },
  { rank: 44, name: "포스코퓨처엠", code: "003670", sector: "2차전지소재" },
  { rank: 45, name: "카카오", code: "035720", sector: "플랫폼" },
  { rank: 46, name: "LG이노텍", code: "011070", sector: "전자부품" },
  { rank: 47, name: "한미반도체", code: "042700", sector: "반도체장비" },
  { rank: 48, name: "삼성생명", code: "032830", sector: "보험" },
  { rank: 49, name: "기업은행", code: "024110", sector: "금융" },
  { rank: 50, name: "셀트리온", code: "068270", sector: "바이오" },
];
```

### Extracted Code (jsx)

```jsx
export default function KospiPBRScanner() {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(false);
  const [filter, setFilter] = useState(0.7);
  const [sortBy, setSortBy] = useState("pbr");
  const [analysisResult, setAnalysisResult] = useState("");
  const [analyzing, setAnalyzing] = useState(false);
  const [activeTab, setActiveTab] = useState("scanner");

  // Mock data based on known estimates for March 11, 2026
  const mockData = [
    { rank: 1, name: "삼성전자", sector: "반도체", pbr: 2.1, per: 18.2, marketCap: "980조", treasuryRatio: "8.2%", dividendYield: "1.2%", soakPlan: "15.6조 소각 계획" },
    // ... more
  ];
  // ...
}
```

### Extracted Code (jsx)

```jsx
export default function App() {
  const [pbrThreshold, setPbrThreshold] = useState(0.7);
  const [sortKey, setSortKey] = useState("pbr");
  const [selectedSector, setSelectedSector] = useState("전체");
  const [aiAnalysis, setAiAnalysis] = useState("");
  const [analyzing, setAnalyzing] = useState(false);
  const [selectedStock, setSelectedStock] = useState(null);
  // ...
}
```

### Extracted Code (jsx)

```jsx
import { useState, useMemo } from "react";

const STOCKS_DATA = [
  { rank: 1, name: "삼성전자", sector: "반도체", pbr: 2.1, per: 18.2, mcap: 980, treasury: 8.2, div: 1.2 },
  { rank: 2, name: "SK하이닉스", sector: "반도체", pbr: 3.8, per: 8.1, mcap: 720, treasury: 2.1, div: 0.5 },
  { rank: 3, name: "현대차", sector: "자동차", pbr: 0.72, per: 6.2, mcap: 108, treasury: 3.5, div: 3.8 },
  // ...
];
```

### Extracted Code (jsx)

```jsx
import { useState, useMemo } from "react";

// KOSPI Top 50 stocks with estimated PBR data (3/11/2026 closing price basis)
const ALL_STOCKS = [
  { rank:1, name:"삼성전자", sector:"반도체", pbr:2.10, per:18.2, mcap:980, treasury:8.2, div:1.2, soakPlan:true },
  { rank:2, name:"SK하이닉스", sector:"반도체", pbr:3.82, per:8.1, mcap:720, treasury:2.1, div:0.5, soakPlan:false },
  // ...50 stocks total
];
```

### Extracted Code (jsx)

```jsx
import { useState, useMemo, useEffect } from "react";

const STOCKS = [
  { rank: 1, name: "삼성전자", sector: "반도체", pbr: 2.10, per: 18.2, mcap: 980, treasury: 8.2, div: 1.2, soakPlan: "15.6조 소각" },
  { rank: 2, name: "SK하이닉스", sector: "반도체", pbr: 3.82, per: 8.1, mcap: 720, treasury: 2.1, div: 0.5, soakPlan: "" },
  { rank: 3, name: "현대차", sector: "자동차", pbr: 0.72, per: 6.2, mcap: 108, treasury: 3.5, div: 3.8, soakPlan: "3년 4조 소각" },
  { rank: 4, name: "LG에너지솔루션", sector: "배터리", pbr: 2.95, per: null, mcap: 94, treasury: 0.0, div: 0.0, soakPlan: "" },
  { rank: 5, name: "삼성바이오로직스", sector: "바이오", pbr: 5.20, per: 48.1, mcap: 85, treasury: 0.5, div: 0.0, soakPlan: "" },
  { rank: 6, name: "SK스퀘어", sector: "지주", pbr: 0.55, per: 9.8, mcap: 78, treasury: 4.2, div: 0.8, soakPlan: "" },
  { rank: 7, name: "한화에어로스페이스", sector: "방산", pbr: 4.10, per: 28.5, mcap: 72, treasury: 1.2, div: 0.3, soakPlan: "" },
  { rank: 8, name: "두산에너빌리티", sector: "발전/원전", pbr: 0.68, per: 22.1, mcap: 65, treasury: 1.8, div: 0.5, soakPlan: "" },
  { rank: 9, name: "기아", sector: "자동차", pbr: 0.62, per: 5.8, mcap: 62, treasury: 4.1, div: 4.5, soakPlan: "자사주 소각 추진" },
  { rank: 10, name: "HD현대중공업", sector: "조선", pbr: 1.82, per: 18.9, mcap: 61, treasury: 0.8, div: 0.6, soakPlan: "" },
  { rank: 11, name: "KB금융", sector: "금융", pbr: 1.02, per: 7.8, mcap: 56, treasury: 2.5, div: 4.2, soakPlan: "자사주 소각 실시" },
  { rank: 12, name: "삼성물산", sector: "지주/건설", pbr: 0.65, per: 12.1, mcap: 55, treasury: 12.0, div: 1.8, soakPlan: "자사주 전량 소각" },
  { rank: 13, name: "신한지주", sector: "금융", pbr: 0.88, per: 7.2, mcap: 52, treasury: 3.1, div: 4.8, soakPlan: "자사주 소각 실시" },
  { rank: 14, name: "HD한국조선해양", sector: "조선", pbr: 1.65, per: 16.2, mcap: 50, treasury: 1.0, div: 0.8, soakPlan: "" },
  { rank: 15, name: "삼성SDI", sector: "배터리", pbr: 0.58, per: null, mcap: 47, treasury: 0.9, div: 1.1, soakPlan: "" },
  { rank: 16, name: "포스코홀딩스", sector: "철강", pbr: 0.42, per: 18.5, mcap: 44, treasury: 5.2, div: 3.5, soakPlan: "자사주 소각 계획" },
  { rank: 17, name: "SK텔레콤", sector: "통신", pbr: 1.12, per: 12.8, mcap: 43, treasury: 6.8, div: 5.5, soakPlan: "자사주 소각 추진" },
  { rank: 18, name: "하나금융지주", sector: "금융", pbr: 0.72, per: 6.9, mcap: 42, treasury: 2.8, div: 5.2, soakPlan: "자사주 소각 실시" },
  { rank: 19, name: "한화시스템", sector: "방산", pbr: 3.85, per: 42.1, mcap: 41, treasury: 0.5, div: 0.2, soakPlan: "" },
  { rank: 20, name: "현대모비스", sector: "자동차부품", pbr: 0.58, per: 7.5, mcap: 40, treasury: 2.2, div: 3.2, soakPlan: "" },
  { rank: 21, name: "한국항공우주", sector: "방산", pbr: 5.20, per: 35.8, mcap: 38, treasury: 0.3, div: 0.4, soakPlan: "" },
  { rank: 22, name: "LG전자", sector: "전자", pbr: 0.82, per: 14.2, mcap: 37, treasury: 1.5, div: 2.1, soakPlan: "" },
  { rank: 23, name: "삼성전기", sector: "전자부품", pbr: 1.25, per: 16.8, mcap: 36, treasury: 0.8, div: 1.5, soakPlan: "" },
  { rank: 24, name: "미래에셋증권", sector: "증권", pbr: 0.68, per: 9.2, mcap: 35, treasury: 8.5, div: 3.8, soakPlan: "" },
  { rank: 25, name: "우리금융지주", sector: "금융", pbr: 0.60, per: 6.5, mcap: 34, treasury: 4.2, div: 6.1, soakPlan: "자사주 소각 실시" },
  { rank: 26, name: "한국전력", sector: "전력", pbr: 0.35, per: null, mcap: 42, treasury: 0.0, div: 0.0, soakPlan: "" },
  { rank: 27, name: "SK㈜", sector: "지주", pbr: 0.52, per: 8.8, mcap: 41, treasury: 18.5, div: 2.5, soakPlan: "5.1조 소각" },
  { rank: 28, name: "LG화학", sector: "화학/배터리", pbr: 0.55, per: null, mcap: 38, treasury: 1.2, div: 2.2, soakPlan: "" },
  { rank: 29, name: "현대글로비스", sector: "물류", pbr: 0.62, per: 8.8, mcap: 36, treasury: 0.5, div: 4.1, soakPlan: "" },
  { rank: 30, name: "HD현대", sector: "지주/조선", pbr: 0.65, per: 7.2, mcap: 35, treasury: 2.8, div: 3.8, soakPlan: "자사주 소각 계획" },
  { rank: 31, name: "롯데지주", sector: "지주", pbr: 0.45, per: null, mcap: 34, treasury: 8.2, div: 1.5, soakPlan: "자사주 소각 발표" },
  { rank: 32, name: "S-Oil", sector: "정유", pbr: 0.52, per: 12.5, mcap: 32, treasury: 0.2, div: 4.2, soakPlan: "" },
  { rank: 33, name: "삼성중공업", sector: "조선", pbr: 0.98, per: 18.5, mcap: 31, treasury: 0.5, div: 0.0, soakPlan: "" },
  { rank: 34, name: "LS", sector: "전선/에너지", pbr: 0.55, per: 8.2, mcap: 30, treasury: 3.5, div: 2.8, soakPlan: "" },
  { rank: 35, name: "두산", sector: "지주", pbr: 0.48, per: 6.5, mcap: 29, treasury: 5.8, div: 1.2, soakPlan: "자사주 소각 발표" },
  { rank: 36, name: "KT", sector: "통신", pbr: 0.75, per: 10.5, mcap: 28, treasury: 0.8, div: 4.5, soakPlan: "" },
  { rank: 37, name: "LG㈜", sector: "지주", pbr: 0.58, per: 9.2, mcap: 27, treasury: 6.5, div: 2.5, soakPlan: "2500억 소각" },
  { rank: 38, name: "네이버", sector: "플랫폼", pbr: 1.42, per: 22.8, mcap: 26, treasury: 3.2, div: 0.5, soakPlan: "" },
  { rank: 39, name: "현대건설", sector: "건설", pbr: 0.45, per: 8.2, mcap: 25, treasury: 1.5, div: 2.8, soakPlan: "" },
  { rank: 40, name: "포스코퓨처엠", sector: "2차전지소재", pbr: 1.85, per: null, mcap: 24, treasury: 0.2, div: 0.8, soakPlan: "" },
  { rank: 41, name: "카카오", sector: "플랫폼", pbr: 0.87, per: null, mcap: 23, treasury: 1.8, div: 0.3, soakPlan: "" },
  { rank: 42, name: "LG이노텍", sector: "전자부품", pbr: 0.72, per: 12.5, mcap: 22, treasury: 0.5, div: 1.5, soakPlan: "" },
  { rank: 43, name: "한미반도체", sector: "반도체장비", pbr: 8.50, per: 38.2, mcap: 22, treasury: 1.2, div: 0.5, soakPlan: "" },
  { rank: 44, name: "삼성생명", sector: "보험", pbr: 0.52, per: 8.5, mcap: 21, treasury: 2.1, div: 4.2, soakPlan: "" },
  { rank: 45, name: "기업은행", sector: "금융", pbr: 0.45, per: 5.8, mcap: 20, treasury: 1.5, div: 6.5, soakPlan: "" },
  { rank: 46, name: "셀트리온", sector: "바이오", pbr: 3.20, per: 28.5, mcap: 20, treasury: 0.8, div: 0.2, soakPlan: "" },
  { rank: 47, name: "SK이노베이션", sector: "에너지/배터리", pbr: 0.62, per: null, mcap: 19, treasury: 1.2, div: 1.8, soakPlan: "" },
  { rank: 48, name: "아모레퍼시픽홀딩스", sector: "지주/화장품", pbr: 0.55, per: 22.1, mcap: 18, treasury: 4.8, div: 1.5, soakPlan: "자사주 소각 발표" },
  { rank: 49, name: "대우건설", sector: "건설", pbr: 0.48, per: 7.2, mcap: 17, treasury: 2.8, div: 3.5, soakPlan: "자사주 소각 발표" },
  { rank: 50, name: "DB하이텍", sector: "반도체", pbr: 1.25, per: 14.8, mcap: 17, treasury: 0.8, div: 1.2, soakPlan: "" },
];

const SECTOR_COLORS = {
  "반도체": "#3B82F6", "자동차": "#10B981", "배터리": "#8B5CF6",
  "바이오": "#EC4899", "지주": "#F59E0B", "방산": "#EF4444",
  "금융": "#06B6D4", "조선": "#84CC16", "철강": "#6B7280",
  "통신": "#F97316", "전자": "#14B8A6", "에너지/배터리": "#A78BFA",
  "화학/배터리": "#FB7185", "정유": "#FBBF24", "플랫폼": "#34D399",
  "전력": "#FCD34D", "물류": "#93C5FD", "건설": "#C084FC",
  "보험": "#67E8F9", "증권": "#86EFAC", "2차전지소재": "#FCA5A5",
  "전자부품": "#A5F3FC", "전선/에너지": "#BBF7D0", "반도체장비": "#FDE68A",
  "지주/건설": "#DDD6FE", "발전/원전": "#FDBA74", "자동차부품": "#6EE7B7",
  "지주/조선": "#94A3B8",
};

export default function KospiPBRScanner() {
  const [threshold, setThreshold] = useState(0.7);
  const [sortKey, setSortKey] = useState("pbr");
  const [sectorFilter, setSectorFilter] = useState("전체");
  const [soakOnly, setSoakOnly] = useState(false);
  const [hovered, setHovered] = useState(null);
  const [aiText, setAiText] = useState("");
  const [aiLoading, setAiLoading] = useState(false);
  const [activeView, setActiveView] = useState("list");

  const sectors = ["전체", ...Array.from(new Set(ALL_STOCKS.map(s => s.sector)))];

  const filtered = useMemo(() => {
    return ALL_STOCKS
      .filter(s => s.pbr <= threshold)
      .filter(s => sectorFilter === "전체" || s.sector === sectorFilter)
      .filter(s => !soakOnly || s.soakPlan)
      .sort((a, b) => {
        if (sortKey === "pbr") return a.pbr - b.pbr;
        if (sortKey === "rank") return a.rank - b.rank;
        if (sortKey === "mcap") return b.mcap - a.mcap;
        if (sortKey === "treasury") return b.treasury - a.treasury;
        return 0;
      });
  }, [threshold, sectorFilter, soakOnly, sortKey]);

  async function runAIAnalysis() {
    setAiLoading(true);
    setAiText("");
    const stockList = filtered.map(s =>
      `${s.name}(PBR ${s.pbr}, 자사주 ${s.treasury}%, ${s.soakPlan || "소각계획없음"})`
    ).join(", ");

    const prompt = `자사주 소각 의무화 법안(3차 상법 개정, 2026년 3월 시행) 맥락에서, 코스피 시총 50위 중 PBR ${threshold}배 이하 종목 ${filtered.length}개를 분석해줘.

종목 리스트: ${stockList}

다음을 포함해서 간결하게 분석해줘:
1. 핵심 수혜 종목 TOP 3 (자사주 소각 의무화 + 저PBR 복합 효과)
2. 업종별 패턴 해석
3. 투자 시 주의해야 할 리스크 요인

한국어로, 에세이 스타일로 300자 내외로 작성.`;

    try {
      const res = await fetch("https://api.anthropic.com/v1/messages", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          model: "claude-sonnet-4-20250514",
          max_tokens: 1000,
          messages: [{ role: "user", content: prompt }],
        }),
      });
      const data = await res.json();
      setAiText(data.content?.[0]?.text || "분석 실패");
    } catch (e) {
      setAiText("분석 중 오류가 발생했습니다.");
    }
    setAiLoading(false);
  }

  const pbrColor = (v) => {
    if (v <= 0.4) return "#EF4444";
    if (v <= 0.5) return "#F97316";
    if (v <= 0.6) return "#EAB308";
    if (v <= 0.7) return "#22C55E";
    return "#94A3B8";
  };

  return (
    <div style={{ minHeight: "100vh", background: "#0A0E1A", color: "#E2E8F0", fontFamily: "'IBM Plex Mono', 'Courier New', monospace" }}>
      {/* Header */}
      <div style={{ borderBottom: "1px solid #1E2A3A", padding: "24px 32px", display: "flex", alignItems: "center", justifyContent: "space-between", background: "rgba(15,23,42,0.8)", backdropFilter: "blur(12px)", position: "sticky", top: 0, zIndex: 100 }}>
        <div>
          <div style={{ fontSize: "11px", letterSpacing: "3px", color: "#475569", marginBottom: "4px" }}>KOSPI TOP 50 · 자사주 소각 의무화 수혜 스캐너</div>
          <div style={{ fontSize: "22px", fontWeight: "700", color: "#F1F5F9", letterSpacing: "-0.5px" }}>
            PBR<span style={{ color: "#22D3EE" }}>_</span>SCANNER
            <span style={{ fontSize: "12px", color: "#475569", marginLeft: "12px" }}>3/11 종가 추정 기준</span>
          </div>
        </div>
        <div style={{ display: "flex", gap: "8px" }}>
          {["list", "chart"].map(v => (
            <button key={v} onClick={() => setActiveView(v)} style={{ padding: "8px 16px", borderRadius: "6px", border: "1px solid", borderColor: activeView === v ? "#22D3EE" : "#1E2A3A", background: activeView === v ? "rgba(34,211,238,0.1)" : "transparent", color: activeView === v ? "#22D3EE" : "#475569", cursor: "pointer", fontSize: "11px", letterSpacing: "2px", textTransform: "uppercase" }}>
              {v === "list" ? "LIST" : "CHART"}
            </button>
          ))}
        </div>
      </div>

      <div style={{ padding: "24px 32px" }}>
        {/* Controls */}
        <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(200px, 1fr))", gap: "16px", marginBottom: "24px" }}>
          {/* PBR Threshold */}
          <div style={{ background: "#0F172A", border: "1px solid #1E2A3A", borderRadius: "12px", padding: "16px" }}>
            <div style={{ fontSize: "10px", letterSpacing: "2px", color: "#475569", marginBottom: "8px" }}>PBR THRESHOLD</div>
            <div style={{ display: "flex", alignItems: "center", gap: "12px" }}>
              <input type="range" min="0.3" max="1.0" step="0.05" value={threshold}
                onChange={e => setThreshold(parseFloat(e.target.value))}
                style={{ flex: 1, accentColor: "#22D3EE" }} />
              <div style={{ fontSize: "20px", fontWeight: "700", color: "#22D3EE", minWidth: "40px" }}>{threshold.toFixed(2)}</div>
            </div>
            <div style={{ fontSize: "11px", color: "#475569", marginTop: "4px" }}>{filtered.length}개 종목 해당</div>
          </div>

          {/* Sort */}
          <div style={{ background: "#0F172A", border: "1px solid #1E2A3A", borderRadius: "12px", padding: "16px" }}>
            <div style={{ fontSize: "10px", letterSpacing: "2px", color: "#475569", marginBottom: "8px" }}>SORT BY</div>
            <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "6px" }}>
              {[["pbr","PBR↑"],["rank","시총순"],["mcap","시총↓"],["treasury","자사주↓"]].map(([k,l]) => (
                <button key={k} onClick={() => setSortKey(k)} style={{ padding: "6px", borderRadius: "6px", border: "1px solid", borderColor: sortKey === k ? "#22D3EE" : "#1E2A3A", background: sortKey === k ? "rgba(34,211,238,0.1)" : "transparent", color: sortKey === k ? "#22D3EE" : "#64748B", cursor: "pointer", fontSize: "10px", letterSpacing: "1px" }}>
                  {l}
                </button>
              ))}
            </div>
          </div>

          {/* Sector */}
          <div style={{ background: "#0F172A", border: "1px solid #1E2A3A", borderRadius: "12px", padding: "16px" }}>
            <div style={{ fontSize: "10px", letterSpacing: "2px", color: "#475569", marginBottom: "8px" }}>SECTOR</div>
            <select value={sectorFilter} onChange={e => setSectorFilter(e.target.value)}
              style={{ width: "100%", background: "#0A0E1A", border: "1px solid #1E2A3A", borderRadius: "6px", padding: "8px", color: "#E2E8F0", fontSize: "12px" }}>
              {sectors.map(s => <option key={s} value={s}>{s}</option>)}
            </select>
          </div>

          {/* Soak Filter */}
          <div style={{ background: "#0F172A", border: "1px solid #1E2A3A", borderRadius: "12px", padding: "16px" }}>
            <div style={{ fontSize: "10px", letterSpacing: "2px", color: "#475569", marginBottom: "8px" }}>소각 계획 필터</div>
            <label style={{ display: "flex", alignItems: "center", gap: "10px", cursor: "pointer" }}>
              <div onClick={() => setSoakOnly(!soakOnly)} style={{ width: "40px", height: "22px", borderRadius: "11px", background: soakOnly ? "#22D3EE" : "#1E2A3A", position: "relative", transition: "background 0.2s", cursor: "pointer" }}>
                <div style={{ position: "absolute", top: "3px", left: soakOnly ? "21px" : "3px", width: "16px", height: "16px", borderRadius: "50%", background: soakOnly ? "#0A0E1A" : "#475569", transition: "left 0.2s" }} />
              </div>
              <span style={{ fontSize: "12px", color: soakOnly ? "#22D3EE" : "#475569" }}>자사주 소각 계획 있는 종목만</span>
            </label>
          </div>
        </div>

        {/* Stats Row */}
        <div style={{ display: "grid", gridTemplateColumns: "repeat(4, 1fr)", gap: "12px", marginBottom: "24px" }}>
          {[
            { label: "필터된 종목", value: `${filtered.length}개`, color: "#22D3EE" },
            { label: "평균 PBR", value: filtered.length ? (filtered.reduce((a,b)=>a+b.pbr,0)/filtered.length).toFixed(2) : "-", color: "#F59E0B" },
            { label: "소각 계획 보유", value: `${filtered.filter(s=>s.soakPlan).length}개`, color: "#22C55E" },
            { label: "평균 자사주 비율", value: filtered.length ? `${(filtered.reduce((a,b)=>a+b.treasury,0)/filtered.length).toFixed(1)}%` : "-", color: "#A78BFA" },
          ].map(item => (
            <div key={item.label} style={{ background: "#0F172A", border: "1px solid #1E2A3A", borderRadius: "10px", padding: "14px 16px" }}>
              <div style={{ fontSize: "10px", letterSpacing: "2px", color: "#475569" }}>{item.label}</div>
              <div style={{ fontSize: "24px", fontWeight: "700", color: item.color, marginTop: "4px" }}>{item.value}</div>
            </div>
          ))}
        </div>

        {activeView === "list" ? (
          /* Stock List */
          <div style={{ background: "#0F172A", border: "1px solid #1E2A3A", borderRadius: "12px", overflow: "hidden" }}>
            {/* Table Header */}
            <div style={{ display: "grid", gridTemplateColumns: "40px 1fr 80px 80px 80px 80px 80px 1fr", gap: "0", padding: "12px 16px", borderBottom: "1px solid #1E2A3A", fontSize: "10px", letterSpacing: "2px", color: "#475569" }}>
              <div>#</div><div>종목</div><div>PBR</div><div>PER</div><div>시총(조)</div><div>자사주%</div><div>배당%</div><div>소각 계획</div>
            </div>
            {filtered.length === 0 ? (
              <div style={{ padding: "40px", textAlign: "center", color: "#475569" }}>해당 조건의 종목이 없습니다</div>
            ) : (
              filtered.map((s, i) => (
                <div key={s.rank} onMouseEnter={() => setHovered(s.rank)} onMouseLeave={() => setHovered(null)}
                  style={{ display: "grid", gridTemplateColumns: "40px 1fr 80px 80px 80px 80px 80px 1fr", gap: "0", padding: "14px 16px", borderBottom: "1px solid #0A0E1A", background: hovered === s.rank ? "rgba(34,211,238,0.03)" : "transparent", transition: "background 0.15s", cursor: "pointer" }}>
                  <div style={{ color: "#475569", fontSize: "12px" }}>{s.rank}</div>
                  <div>
                    <span style={{ color: "#F1F5F9", fontWeight: "600", fontSize: "13px" }}>{s.name}</span>
                    <span style={{ marginLeft: "8px", fontSize: "10px", padding: "2px 6px", borderRadius: "4px", background: `${SECTOR_COLORS[s.sector] || "#475569"}22`, color: SECTOR_COLORS[s.sector] || "#94A3B8" }}>{s.sector}</span>
                  </div>
                  <div style={{ color: pbrColor(s.pbr), fontWeight: "700", fontSize: "14px" }}>{s.pbr.toFixed(2)}</div>
                  <div style={{ color: "#94A3B8", fontSize: "13px" }}>{s.per ? s.per.toFixed(1) : "N/A"}</div>
                  <div style={{ color: "#94A3B8", fontSize: "13px" }}>{s.mcap}조</div>
                  <div style={{ color: s.treasury > 5 ? "#A78BFA" : "#64748B", fontSize: "13px" }}>{s.treasury.toFixed(1)}%</div>
                  <div style={{ color: s.div > 4 ? "#22C55E" : "#64748B", fontSize: "13px" }}>{s.div.toFixed(1)}%</div>
                  <div style={{ fontSize: "11px", color: s.soakPlan ? "#22C55E" : "#374151" }}>
                    {s.soakPlan || "—"}
                  </div>
                </div>
              ))
            )}
          </div>
        ) : (
          /* Chart View */
          <div style={{ background: "#0F172A", border: "1px solid #1E2A3A", borderRadius: "12px", padding: "24px" }}>
            <div style={{ fontSize: "11px", letterSpacing: "2px", color: "#475569", marginBottom: "20px" }}>PBR vs 자사주 비율 (버블 크기 = 시가총액)</div>
            <div style={{ position: "relative", height: "380px", border: "1px solid #1E2A3A", borderRadius: "8px", overflow: "hidden", background: "#0A0E1A" }}>
              {/* Grid lines */}
              {[0, 0.25, 0.5, 0.75, 1].map(v => (
                <div key={v} style={{ position: "absolute", left: `${v*100}%`, top: 0, bottom: 0, borderLeft: "1px solid #1E2A3A", opacity: 0.5 }} />
              ))}
              {/* PBR threshold line */}
              <div style={{ position: "absolute", left: 0, right: 0, top: `${(1 - threshold)*100}%`, borderTop: "1px dashed #22D3EE", opacity: 0.5 }} />

              {ALL_STOCKS.map(s => {
                const x = Math.min(s.treasury / 20, 1) * 90 + 5;
                const y = Math.max(0, Math.min(1 - s.pbr / 2, 0.95)) * 90 + 5;
                const size = Math.sqrt(s.mcap / 980) * 32 + 4;
                const isFiltered = s.pbr <= threshold;
                return (
                  <div key={s.rank} title={`${s.name} | PBR: ${s.pbr} | 자사주: ${s.treasury}%`}
                    style={{
                      position: "absolute",
                      left: `${x}%`, top: `${y}%`,
                      width: `${size}px`, height: `${size}px`,
                      borderRadius: "50%",
                      background: isFiltered ? (SECTOR_COLORS[s.sector] || "#22D3EE") : "#1E2A3A",
                      opacity: isFiltered ? 0.85 : 0.3,
                      transform: "translate(-50%, -50%)",
                      transition: "all 0.2s",
                      cursor: "pointer",
                      border: s.soakPlan && isFiltered ? "2px solid #22D3EE" : "none",
                      boxShadow: isFiltered ? `0 0 8px ${SECTOR_COLORS[s.sector] || "#22D3EE"}44` : "none",
                    }}
                    onMouseEnter={() => setHovered(s.rank)}
                    onMouseLeave={() => setHovered(null)}
                  />
                );
              })}

              {/* Axis Labels */}
              <div style={{ position: "absolute", bottom: "4px", left: "50%", transform: "translateX(-50%)", fontSize: "10px", color: "#475569" }}>← 자사주 비율 낮음 / 높음 →</div>
              <div style={{ position: "absolute", left: "4px", top: "50%", transform: "translateY(-50%) rotate(-90deg)", fontSize: "10px", color: "#475569" }}>← PBR 높음 / 낮음 →</div>
            </div>
            <div style={{ marginTop: "12px", display: "flex", gap: "16px", flexWrap: "wrap" }}>
              {Object.entries(SECTOR_COLORS).slice(0, 8).map(([sector, color]) => (
                <div key={sector} style={{ display: "flex", alignItems: "center", gap: "4px" }}>
                  <div style={{ width: "8px", height: "8px", borderRadius: "50%", background: color }} />
                  <span style={{ fontSize: "10px", color: "#64748B" }}>{sector}</span>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* AI Analysis */}
        <div style={{ marginTop: "24px", background: "#0F172A", border: "1px solid #1E2A3A", borderRadius: "12px", overflow: "hidden" }}>
          <div style={{ padding: "16px 20px", borderBottom: "1px solid #1E2A3A", display: "flex", alignItems: "center", justifyContent: "space-between" }}>
            <div>
              <div style={{ fontSize: "10px", letterSpacing: "2px", color: "#475569" }}>AI ANALYSIS</div>
              <div style={{ fontSize: "13px", color: "#94A3B8", marginTop: "2px" }}>자사주 소각 의무화 수혜 분석 · {filtered.length}개 종목 기준</div>
            </div>
            <button onClick={runAIAnalysis} disabled={aiLoading}
              style={{ padding: "10px 20px", borderRadius: "8px", border: "1px solid #22D3EE", background: aiLoading ? "rgba(34,211,238,0.05)" : "rgba(34,211,238,0.1)", color: "#22D3EE", cursor: aiLoading ? "not-allowed" : "pointer", fontSize: "11px", letterSpacing: "2px", display: "flex", alignItems: "center", gap: "8px" }}>
              {aiLoading ? (
                <>
                  <div style={{ width: "12px", height: "12px", borderRadius: "50%", border: "2px solid #22D3EE", borderTopColor: "transparent", animation: "spin 0.8s linear infinite" }} />
                  ANALYZING...
                </>
              ) : "▶ ANALYZE"}
            </button>
          </div>
          <div style={{ padding: "20px", minHeight: "80px" }}>
            {aiText ? (
              <div style={{ fontSize: "14px", lineHeight: "1.8", color: "#CBD5E1", whiteSpace: "pre-wrap" }}>{aiText}</div>
            ) : (
              <div style={{ color: "#334155", fontSize: "13px", textAlign: "center", paddingTop: "20px" }}>
                ▶ ANALYZE 버튼을 클릭하면 현재 필터 조건의 종목을 AI가 분석합니다
              </div>
            )}
          </div>
        </div>

        {/* Disclaimer */}
        <div style={{ marginTop: "16px", padding: "12px 16px", background: "#0F172A", borderRadius: "8px", border: "1px solid #1E2A3A" }}>
          <div style={{ fontSize: "10px", color: "#374151", lineHeight: "1.6" }}>
            ⚠ 본 데이터는 공개된 리포트 및 추정치 기반이며 3/11 종가 기준 정확한 PBR은 KRX 데이터 시스템 또는 FnGuide에서 확인하세요. 투자 참고용이며 투자 권유가 아닙니다.
          </div>
        </div>
      </div>

      <style>{`@keyframes spin { to { transform: rotate(360deg); } }`}</style>
    </div>
  );
}
```

### Extracted Code (jsx)

```jsx
import { useState, useMemo } from "react";

const SECTOR_COLORS = {
  "반도체": "#3B82F6", "자동차": "#10B981", "배터리": "#8B5CF6",
  "바이오": "#EC4899", "지주": "#F59E0B", "방산": "#EF4444",
  "금융": "#06B6D4", "조선": "#84CC16", "철강": "#6B7280",
  "통신": "#F97316", "전자": "#14B8A6", "에너지/배터리": "#A78BFA",
  "화학/배터리": "#FB7185", "정유": "#FBBF24", "플랫폼": "#34D399",
  "전력": "#FCD34D", "물류": "#93C5FD", "건설": "#C084FC",
  "보험": "#67E8F9", "증권": "#86EFAC", "2차전지소재": "#FCA5A5",
  "전자부품": "#A5F3FC", "전선/에너지": "#BBF7D0", "반도체장비": "#FDE68A",
  "지주/건설": "#DDD6FE", "발전/원전": "#FDBA74", "자동차부품": "#6EE7B7",
  "지주/조선": "#94A3B8", "지주/화장품": "#F9A8D4",
};

const ALL_STOCKS = [
  { rank:1, name:"삼성전자", sector:"반도체", pbr:2.10, per:18.2, mcap:980, treasury:8.2, div:1.2, soakPlan:"15.6조 소각" },
  { rank:2, name:"SK하이닉스", sector:"반도체", pbr:3.82, per:8.1, mcap:720, treasury:2.1, div:0.5, soakPlan:"" },
  { rank:3, name:"현대차", sector:"자동차", pbr:0.72, per:6.2, mcap:108, treasury:3.5, div:3.8, soakPlan:"3년 4조 소각" },
  { rank:4, name:"LG에너지솔루션", sector:"배터리", pbr:2.95, per:null, mcap:94, treasury:0.0, div:0.0, soakPlan:"" },
  { rank:5, name:"삼성바이오로직스", sector:"바이오", pbr:5.20, per:48.1, mcap:85, treasury:0.5, div:0.0, soakPlan:"" },
  { rank:6, name:"SK스퀘어", sector:"지주", pbr:0.55, per:9.8, mcap:78, treasury:4.2, div:0.8, soakPlan:"" },
  { rank:7, name:"한화에어로스페이스", sector:"방산", pbr:4.10, per:28.5, mcap:72, treasury:1.2, div:0.3, soakPlan:"" },
  { rank:8, name:"두산에너빌리티", sector:"발전/원전", pbr:0.68, per:22.1, mcap:65, treasury:1.8, div:0.5, soakPlan:"" },
  { rank:9, name:"기아", sector:"자동차", pbr:0.62, per:5.8, mcap:62, treasury:4.1, div:4.5, soakPlan:"자사주 소각 추진" },
  { rank:10, name:"HD현대중공업", sector:"조선", pbr:1.82, per:18.9, mcap:61, treasury:0.8, div:0.6, soakPlan:"" },
  { rank:11, name:"KB금융", sector:"금융", pbr:1.02, per:7.8, mcap:56, treasury:2.5, div:4.2, soakPlan:"자사주 소각 실시" },
  { rank:12, name:"삼성물산", sector:"지주/건설", pbr:0.65, per:12.1, mcap:55, treasury:12.0, div:1.8, soakPlan:"자사주 전량 소각" },
  { rank:13, name:"신한지주", sector:"금융", pbr:0.88, per:7.2, mcap:52, treasury:3.1, div:4.8, soakPlan:"자사주 소각 실시" },
  { rank:14, name:"HD한국조선해양", sector:"조선", pbr:1.65, per:16.2, mcap:50, treasury:1.0, div:0.8, soakPlan:"" },
  { rank:15, name:"삼성SDI", sector:"배터리", pbr:0.58, per:null, mcap:47, treasury:0.9, div:1.1, soakPlan:"" },
  { rank:16, name:"포스코홀딩스", sector:"철강", pbr:0.42, per:18.5, mcap:44, treasury:5.2, div:3.5, soakPlan:"자사주 소각 계획" },
  { rank:17, name:"SK텔레콤", sector:"통신", pbr:1.12, per:12.8, mcap:43, treasury:6.8, div:5.5, soakPlan:"자사주 소각 추진" },
  { rank:18, name:"하나금융지주", sector:"금융", pbr:0.72, per:6.9, mcap:42, treasury:2.8, div:5.2, soakPlan:"자사주 소각 실시" },
  { rank:19, name:"한화시스템", sector:"방산", pbr:3.85, per:42.1, mcap:41, treasury:0.5, div:0.2, soakPlan:"" },
  { rank:20, name:"현대모비스", sector:"자동차부품", pbr:0.58, per:7.5, mcap:40, treasury:2.2, div:3.2, soakPlan:"" },
  { rank:21, name:"한국항공우주", sector:"방산", pbr:5.20, per:35.8, mcap:38, treasury:0.3, div:0.4, soakPlan:"" },
  { rank:22, name:"LG전자", sector:"전자", pbr:0.82, per:14.2, mcap:37, treasury:1.5, div:2.1, soakPlan:"" },
  { rank:23, name:"삼성전기", sector:"전자부품", pbr:1.25, per:16.8, mcap:36, treasury:0.8, div:1.5, soakPlan:"" },
  { rank:24, name:"미래에셋증권", sector:"증권", pbr:0.68, per:9.2, mcap:35, treasury:8.5, div:3.8, soakPlan:"" },
  { rank:25, name:"우리금융지주", sector:"금융", pbr:0.60, per:6.5, mcap:34, treasury:4.2, div:6.1, soakPlan:"자사주 소각 실시" },
  { rank:26, name:"한국전력", sector:"전력", pbr:0.35, per:null, mcap:42, treasury:0.0, div:0.0, soakPlan:"" },
  { rank:27, name:"SK㈜", sector:"지주", pbr:0.52, per:8.8, mcap:41, treasury:18.5, div:2.5, soakPlan:"5.1조 소각" },
  { rank:28, name:"LG화학", sector:"화학/배터리", pbr:0.55, per:null, mcap:38, treasury:1.2, div:2.2, soakPlan:"" },
  { rank:29, name:"현대글로비스", sector:"물류", pbr:0.62, per:8.8, mcap:36, treasury:0.5, div:4.1, soakPlan:"" },
  { rank:30, name:"HD현대", sector:"지주/조선", pbr:0.65, per:7.2, mcap:35, treasury:2.8, div:3.8, soakPlan:"자사주 소각 계획" },
  { rank:31, name:"롯데지주", sector:"지주", pbr:0.45, per:null, mcap:34, treasury:8.2, div:1.5, soakPlan:"자사주 소각 발표" },
  { rank:32, name:"S-Oil", sector:"정유", pbr:0.52, per:12.5, mcap:32, treasury:0.2, div:4.2, soakPlan:"" },
  { rank:33, name:"삼성중공업", sector:"조선", pbr:0.98, per:18.5, mcap:31, treasury:0.5, div:0.0, soakPlan:"" },
  { rank:34, name:"LS", sector:"전선/에너지", pbr:0.55, per:8.2, mcap:30, treasury:3.5, div:2.8, soakPlan:"" },
  { rank:35, name:"두산", sector:"지주", pbr:0.48, per:6.5, mcap:29, treasury:5.8, div:1.2, soakPlan:"자사주 소각 발표" },
  { rank:36, name:"KT", sector:"통신", pbr:0.75, per:10.5, mcap:28, treasury:0.8, div:4.5, soakPlan:"" },
  { rank:37, name:"LG㈜", sector:"지주", pbr:0.58, per:9.2, mcap:27, treasury:6.5, div:2.5, soakPlan:"2500억 소각" },
  { rank:38, name:"네이버", sector:"플랫폼", pbr:1.42, per:22.8, mcap:26, treasury:3.2, div:0.5, soakPlan:"" },
  { rank:39, name:"현대건설", sector:"건설", pbr:0.45, per:8.2, mcap:25, treasury:1.5, div:2.8, soakPlan:"" },
  { rank:40, name:"포스코퓨처엠", sector:"2차전지소재", pbr:1.85, per:null, mcap:24, treasury:0.2, div:0.8, soakPlan:"" },
  { rank:41, name:"카카오", sector:"플랫폼", pbr:0.87, per:null, mcap:23, treasury:1.8, div:0.3, soakPlan:"" },
  { rank:42, name:"LG이노텍", sector:"전자부품", pbr:0.72, per:12.5, mcap:22, treasury:0.5, div:1.5, soakPlan:"" },
  { rank:43, name:"한미반도체", sector:"반도체장비", pbr:8.50, per:38.2, mcap:22, treasury:1.2, div:0.5, soakPlan:"" },
  { rank:44, name:"삼성생명", sector:"보험", pbr:0.52, per:8.5, mcap:21, treasury:2.1, div:4.2, soakPlan:"" },
  { rank:45, name:"기업은행", sector:"금융", pbr:0.45, per:5.8, mcap:20, treasury:1.5, div:6.5, soakPlan:"" },
  { rank:46, name:"셀트리온", sector:"바이오", pbr:3.20, per:28.5, mcap:20, treasury:0.8, div:0.2, soakPlan:"" },
  { rank:47, name:"SK이노베이션", sector:"에너지/배터리", pbr:0.62, per:null, mcap:19, treasury:1.2, div:1.8, soakPlan:"" },
  { rank:48, name:"아모레퍼시픽", sector:"지주/화장품", pbr:0.55, per:22.1, mcap:18, treasury:4.8, div:1.5, soakPlan:"자사주 소각 발표" },
  { rank:49, name:"현대건설기계", sector:"건설", pbr:0.48, per:7.2, mcap:17, treasury:2.8, div:3.5, soakPlan:"" },
  { rank:50, name:"DB하이텍", sector:"반도체", pbr:1.25, per:14.8, mcap:17, treasury:0.8, div:1.2, soakPlan:"" },
];

function PBRBar({ value, max = 1.0 }) {
  const pct = Math.min(value / max, 1) * 100;
  const color = value <= 0.4 ? "#EF4444" : value <= 0.5 ? "#F97316" : value <= 0.6 ? "#EAB308" : "#22C55E";
  return (
    <div style={{ display:"flex", alignItems:"center", gap:8 }}>
      <div style={{ flex:1, height:4, background:"#1E2A3A", borderRadius:2, overflow:"hidden" }}>
        <div style={{ width:`${pct}%`, height:"100%", background:color, borderRadius:2, transition:"width 0.3s" }} />
      </div>
      <span style={{ fontSize:13, fontWeight:700, color, minWidth:32, textAlign:"right" }}>{value.toFixed(2)}</span>
    </div>
  );
}

export default function App() {
  const [threshold, setThreshold] = useState(0.7);
  const [sortKey, setSortKey] = useState("pbr");
  const [sectorFilter, setSectorFilter] = useState("전체");
  const [soakOnly, setSoakOnly] = useState(false);
  const [view, setView] = useState("list");
  const [aiText, setAiText] = useState("");
  const [aiLoading, setAiLoading] = useState(false);
  const [hovered, setHovered] = useState(null);

  const sectors = useMemo(() => ["전체", ...Array.from(new Set(ALL_STOCKS.map(s => s.sector))).sort()], []);

  const filtered = useMemo(() =>
    ALL_STOCKS
      .filter(s => s.pbr <= threshold)
      .filter(s => sectorFilter === "전체" || s.sector === sectorFilter)
      .filter(s => !soakOnly || !!s.soakPlan)
      .sort((a,b) => {
        if (sortKey === "pbr") return a.pbr - b.pbr;
        if (sortKey === "rank") return a.rank - b.rank;
        if (sortKey === "mcap") return b.mcap - a.mcap;
        if (sortKey === "treasury") return b.treasury - a.treasury;
        if (sortKey === "div") return b.div - a.div;
        return 0;
      }), [threshold, sectorFilter, soakOnly, sortKey]);

  const avgPBR = filtered.length ? (filtered.reduce((a,b)=>a+b.pbr,0)/filtered.length).toFixed(2) : "-";
  const soakCount = filtered.filter(s=>s.soakPlan).length;
  const avgTreasury = filtered.length ? (filtered.reduce((a,b)=>a+b.treasury,0)/filtered.length).toFixed(1) : "-";
  const avgDiv = filtered.length ? (filtered.reduce((a,b)=>a+b.div,0)/filtered.length).toFixed(1) : "-";

  async function runAI() {
    if (aiLoading) return;
    setAiLoading(true);
    setAiText("");
    const list = filtered.map(s=>`${s.name}(PBR ${s.pbr}, 자사주 ${s.treasury}%, ${s.soakPlan||"소각계획없음"})`).join(", ");
    const prompt = `자사주 소각 의무화 법안(3차 상법 개정, 2026년 3월 시행) 맥락에서 코스피 시총 50위 중 PBR ${threshold}배 이하 ${filtered.length}개 종목을 분석해줘.\n\n종목: ${list}\n\n핵심수혜 TOP3, 업종별 패턴, 리스크 요인을 에세이 스타일로 한국어 400자 내외로 써줘.`;
    try {
      const res = await fetch("https://api.anthropic.com/v1/messages", {
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify({ model:"claude-sonnet-4-20250514", max_tokens:1000, messages:[{role:"user",content:prompt}] })
      });
      const data = await res.json();
      setAiText(data.content?.[0]?.text || "분석 실패");
    } catch { setAiText("오류 발생"); }
    setAiLoading(false);
  }

  const pbrColor = v => v<=0.4?"#EF4444":v<=0.5?"#F97316":v<=0.6?"#EAB308":"#22C55E";

  return (
    <div style={{minHeight:"100vh",background:"#050A14",color:"#CBD5E1",fontFamily:"'IBM Plex Mono','Courier New',monospace",fontSize:13}}>
      {/* ── HEADER ── */}
      <div style={{borderBottom:"1px solid #0F1F30",padding:"20px 28px",background:"rgba(5,10,20,0.9)",backdropFilter:"blur(16px)",position:"sticky",top:0,zIndex:100,display:"flex",alignItems:"center",justifyContent:"space-between"}}>
        <div>
          <div style={{fontSize:10,letterSpacing:"3px",color:"#334155",marginBottom:3}}>KOSPI TOP 50 · 자사주소각 의무화 수혜 스캐너 · 2026.03.11 종가 추정</div>
          <div style={{fontSize:20,fontWeight:700,color:"#F8FAFC",letterSpacing:"-0.5px"}}>
            PBR<span style={{color:"#22D3EE"}}>_</span>SCAN
            <span style={{fontSize:11,color:"#1E3A5F",marginLeft:10,fontWeight:400}}>v1.0</span>
          </div>
        </div>
        <div style={{display:"flex",gap:6}}>
          {[["list","≡ LIST"],["chart","◉ MAP"]].map(([v,l])=>(
            <button key={v} onClick={()=>setView(v)} style={{padding:"7px 14px",borderRadius:6,border:"1px solid",borderColor:view===v?"#22D3EE":"#0F1F30",background:view===v?"rgba(34,211,238,0.08)":"transparent",color:view===v?"#22D3EE":"#334155",cursor:"pointer",fontSize:10,letterSpacing:"2px"}}>
              {l}
            </button>
          ))}
        </div>
      </div>

      <div style={{padding:"20px 28px"}}>
        {/* ── CONTROLS ── */}
        <div style={{display:"grid",gridTemplateColumns:"1fr 1fr 1fr 1fr",gap:12,marginBottom:20}}>
          {/* Threshold */}
          <div style={{background:"#0A1628",border:"1px solid #0F1F30",borderRadius:10,padding:"14px 16px"}}>
            <div style={{fontSize:9,letterSpacing:"3px",color:"#334155",marginBottom:8}}>PBR 임계값</div>
            <input type="range" min="0.3" max="1.0" step="0.05" value={threshold} onChange={e=>setThreshold(parseFloat(e.target.value))}
              style={{width:"100%",accentColor:"#22D3EE",marginBottom:4}} />
            <div style={{display:"flex",justifyContent:"space-between",alignItems:"center"}}>
              <span style={{fontSize:9,color:"#1E3A5F"}}>0.30</span>
              <span style={{fontSize:22,fontWeight:700,color:"#22D3EE"}}>{threshold.toFixed(2)}</span>
              <span style={{fontSize:9,color:"#1E3A5F"}}>1.00</span>
            </div>
          </div>

          {/* Sort */}
          <div style={{background:"#0A1628",border:"1px solid #0F1F30",borderRadius:10,padding:"14px 16px"}}>
            <div style={{fontSize:9,letterSpacing:"3px",color:"#334155",marginBottom:8}}>정렬 기준</div>
            <div style={{display:"grid",gridTemplateColumns:"1fr 1fr",gap:4}}>
              {[["pbr","PBR↑"],["rank","시총순위"],["treasury","자사주%"],["div","배당%"]].map(([k,l])=>(
                <button key={k} onClick={()=>setSortKey(k)} style={{padding:"5px 0",borderRadius:5,border:"1px solid",borderColor:sortKey===k?"#22D3EE":"#0F1F30",background:sortKey===k?"rgba(34,211,238,0.1)":"transparent",color:sortKey===k?"#22D3EE":"#334155",cursor:"pointer",fontSize:9,letterSpacing:"1px"}}>
                  {l}
                </button>
              ))}
            </div>
          </div>

          {/* Sector */}
          <div style={{background:"#0A1628",border:"1px solid #0F1F30",borderRadius:10,padding:"14px 16px"}}>
            <div style={{fontSize:9,letterSpacing:"3px",color:"#334155",marginBottom:8}}>업종 필터</div>
            <select value={sectorFilter} onChange={e=>setSectorFilter(e.target.value)}
              style={{width:"100%",background:"#050A14",border:"1px solid #0F1F30",borderRadius:5,padding:"7px 8px",color:"#CBD5E1",fontSize:11,outline:"none"}}>
              {sectors.map(s=><option key={s} value={s}>{s}</option>)}
            </select>
          </div>

          {/* Soak Toggle */}
          <div style={{background:"#0A1628",border:"1px solid #0F1F30",borderRadius:10,padding:"14px 16px"}}>
            <div style={{fontSize:9,letterSpacing:"3px",color:"#334155",marginBottom:10}}>소각 계획 보유 종목</div>
            <div style={{display:"flex",alignItems:"center",gap:10,cursor:"pointer"}} onClick={()=>setSoakOnly(!soakOnly)}>
              <div style={{width:42,height:24,borderRadius:12,background:soakOnly?"#22D3EE":"#0F1F30",position:"relative",transition:"background 0.2s",flexShrink:0}}>
                <div style={{position:"absolute",top:3,left:soakOnly?21:3,width:18,height:18,borderRadius:"50%",background:soakOnly?"#050A14":"#334155",transition:"left 0.2s"}} />
              </div>
              <span style={{fontSize:11,color:soakOnly?"#22D3EE":"#334155"}}>{soakOnly?"소각 계획 있음만":"전체 표시"}</span>
            </div>
          </div>
        </div>

        {/* ── STATS ── */}
        <div style={{display:"grid",gridTemplateColumns:"repeat(5,1fr)",gap:10,marginBottom:20}}>
          {[
            {label:"필터 종목 수",value:`${filtered.length}개`,color:"#22D3EE"},
            {label:"평균 PBR",value:avgPBR,color:"#F59E0B"},
            {label:"소각계획 보유",value:`${soakCount}개`,color:"#22C55E"},
            {label:"평균 자사주%",value:`${avgTreasury}%`,color:"#A78BFA"},
            {label:"평균 배당수익률",value:`${avgDiv}%`,color:"#FB7185"},
          ].map(item=>(
            <div key={item.label} style={{background:"#0A1628",border:"1px solid #0F1F30",borderRadius:10,padding:"12px 14px"}}>
              <div style={{fontSize:9,letterSpacing:"2px",color:"#334155",marginBottom:4}}>{item.label}</div>
              <div style={{fontSize:20,fontWeight:700,color:item.color}}>{item.value}</div>
            </div>
          ))}
        </div>

        {/* ── CONTENT ── */}
        {view==="list" ? (
          <div style={{background:"#0A1628",border:"1px solid #0F1F30",borderRadius:12,overflow:"hidden",marginBottom:20}}>
            {/* Header Row */}
            <div style={{display:"grid",gridTemplateColumns:"36px 160px 1fr 64px 64px 70px 64px 1fr",gap:0,padding:"10px 16px",borderBottom:"1px solid #0F1F30",fontSize:9,letterSpacing:"2px",color:"#1E3A5F"}}>
              <div>#</div><div>종목명</div><div style={{paddingLeft:8}}>PBR</div><div>PER</div><div>시총</div><div>자사주%</div><div>배당%</div><div>소각 계획</div>
            </div>
            {filtered.length===0 ? (
              <div style={{padding:40,textAlign:"center",color:"#1E3A5F"}}>조건에 맞는 종목이 없습니다</div>
            ) : filtered.map(s=>(
              <div key={s.rank} onMouseEnter={()=>setHovered(s.rank)} onMouseLeave={()=>setHovered(null)}
                style={{display:"grid",gridTemplateColumns:"36px 160px 1fr 64px 64px 70px 64px 1fr",gap:0,padding:"12px 16px",borderBottom:"1px solid #050A14",background:hovered===s.rank?"rgba(34,211,238,0.03)":"transparent",transition:"background 0.15s",alignItems:"center"}}>
                <div style={{color:"#1E3A5F",fontSize:11}}>{s.rank}</div>
                <div>
                  <div style={{color:"#F1F5F9",fontWeight:600,fontSize:13}}>{s.name}</div>
                  <div style={{marginTop:2}}>
                    <span style={{fontSize:9,padding:"2px 5px",borderRadius:3,background:`${SECTOR_COLORS[s.sector]||"#475569"}18`,color:SECTOR_COLORS[s.sector]||"#94A3B8",letterSpacing:"1px"}}>{s.sector}</span>
                  </div>
                </div>
                <div style={{paddingLeft:8}}>
                  <PBRBar value={s.pbr} max={Math.max(threshold,0.7)} />
                </div>
                <div style={{color:"#64748B",fontSize:12}}>{s.per?s.per.toFixed(1):"N/A"}</div>
                <div style={{color:"#64748B",fontSize:12}}>{s.mcap}조</div>
                <div style={{color:s.treasury>8?"#A78BFA":s.treasury>5?"#7C3AED":"#64748B",fontSize:12,fontWeight:s.treasury>5?700:400}}>{s.treasury.toFixed(1)}%</div>
                <div style={{color:s.div>5?"#22C55E":s.div>3?"#86EFAC":"#64748B",fontSize:12}}>{s.div.toFixed(1)}%</div>
                <div style={{fontSize:10,color:s.soakPlan?"#22C55E":"#1E3A5F",letterSpacing:"0.5px"}}>{s.soakPlan||"—"}</div>
              </div>
            ))}
          </div>
        ) : (
          /* BUBBLE CHART */
          <div style={{background:"#0A1628",border:"1px solid #0F1F30",borderRadius:12,padding:20,marginBottom:20}}>
            <div style={{fontSize:9,letterSpacing:"3px",color:"#334155",marginBottom:12}}>PBR × 자사주 비율 버블맵 (버블 크기 = 시가총액 / 테두리 = 소각계획 보유)</div>
            <div style={{position:"relative",height:340,background:"#050A14",borderRadius:8,overflow:"hidden",border:"1px solid #0F1F30"}}>
              {[0,25,50,75,100].map(p=>(
                <React.Fragment key={p}>
                  <div style={{position:"absolute",left:`${p}%`,top:0,bottom:0,borderLeft:"1px solid #0F1F30",opacity:0.5}} />
                  <div style={{position:"absolute",top:`${p}%`,left:0,right:0,borderTop:"1px solid #0F1F30",opacity:0.5}} />
                </React.Fragment>
              ))}
              <div style={{position:"absolute",top:0,bottom:0,left:`${Math.min(threshold/20*100,99)}%`,borderLeft:"1px dashed #22D3EE",opacity:0.6,zIndex:2}} />
              <div style={{position:"absolute",top:`${Math.max(0,(1-threshold/2)*100)}%`,left:0,right:0,borderTop:"2px dashed #22D3EE",opacity:0.6,zIndex:2}} />
              <div style={{position:"absolute",top:`${Math.max(0,(1-threshold/2)*100)-3}%`,right:8,fontSize:9,color:"#22D3EE",letterSpacing:"1px"}}>PBR {threshold}</div>

              {ALL_STOCKS.map(s=>{
                const x = Math.min(s.treasury/25,1)*85+7;
                const y = (1-Math.min(s.pbr/2,1))*84+4;
                const r = Math.max(6, Math.sqrt(s.mcap/980)*36);
                const isIn = s.pbr<=threshold;
                const col = SECTOR_COLORS[s.sector]||"#22D3EE";
                return (
                  <div key={s.rank} title={`${s.name} | PBR:${s.pbr} | 자사주:${s.treasury}% | 시총:${s.mcap}조`}
                    style={{position:"absolute",left:`${x}%`,top:`${y}%`,width:r,height:r,borderRadius:"50%",
                      background:isIn?`${col}CC`:"#0F1F30",
                      border:s.soakPlan&&isIn?`2px solid ${col}`:"1px solid #0F1F30",
                      transform:"translate(-50%,-50%)",
                      boxShadow:isIn?`0 0 ${r/2}px ${col}44`:"none",
                      transition:"all 0.2s",cursor:"pointer",zIndex:isIn?2:1,
                      opacity:isIn?1:0.3}}>
                  </div>
                );
              })}
              <div style={{position:"absolute",bottom:6,left:"50%",transform:"translateX(-50%)",fontSize:9,color:"#1E3A5F",letterSpacing:"2px"}}>← 자사주 비율 →</div>
              <div style={{position:"absolute",left:4,top:"50%",transform:"translateY(-50%) rotate(-90deg)",fontSize:9,color:"#1E3A5F",letterSpacing:"2px",whiteSpace:"nowrap"}}>← PBR 높음 / 낮음 →</div>
            </div>
            <div style={{marginTop:10,display:"flex",gap:10,flexWrap:"wrap"}}>
              {Object.entries(SECTOR_COLORS).map(([s,c])=>(
                <div key={s} style={{display:"flex",alignItems:"center",gap:4}}>
                  <div style={{width:6,height:6,borderRadius:"50%",background:c}} />
                  <span style={{fontSize:9,color:"#334155"}}>{s}</span>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* ── AI ANALYSIS ── */}
        <div style={{background:"#0A1628",border:"1px solid #0F1F30",borderRadius:12,overflow:"hidden"}}>
          <div style={{padding:"14px 20px",borderBottom:"1px solid #0F1F30",display:"flex",alignItems:"center",justifyContent:"space-between"}}>
            <div>
              <div style={{fontSize:9,letterSpacing:"3px",color:"#334155"}}>AI ANALYSIS · Claude Sonnet</div>
              <div style={{fontSize:12,color:"#475569",marginTop:2}}>현재 필터 조건({filtered.length}개 종목) 기준 자사주 소각 의무화 수혜 분석</div>
            </div>
            <button onClick={runAI} disabled={aiLoading}
              style={{padding:"9px 18px",borderRadius:7,border:"1px solid",borderColor:aiLoading?"#0F1F30":"#22D3EE",
                background:aiLoading?"transparent":"rgba(34,211,238,0.08)",
                color:aiLoading?"#1E3A5F":"#22D3EE",cursor:aiLoading?"not-allowed":"pointer",
                fontSize:10,letterSpacing:"2px",display:"flex",alignItems:"center",gap:8}}>
              {aiLoading?<>
                <div style={{width:10,height:10,borderRadius:"50%",border:"2px solid #22D3EE",borderTopColor:"transparent",animation:"spin 0.7s linear infinite"}} />
                분석중...
              </>:"▶ AI 분석 실행"}
            </button>
          </div>
          <div style={{padding:20,minHeight:80}}>
            {aiText ? (
              <div style={{fontSize:13,lineHeight:1.9,color:"#94A3B8",whiteSpace:"pre-wrap"}}>{aiText}</div>
            ) : (
              <div style={{color:"#1E3A5F",textAlign:"center",paddingTop:16,fontSize:12,letterSpacing:"1px"}}>
                ▶ AI 분석 실행 버튼을 누르면 현재 필터 조건의 종목을 Claude가 분석합니다
              </div>
            )}
          </div>
        </div>

        <div style={{marginTop:14,padding:"10px 14px",background:"#0A1628",borderRadius:8,border:"1px solid #0F1F30"}}>
          <div style={{fontSize:9,color:"#1E3A5F",lineHeight:1.7,letterSpacing:"0.5px"}}>
            ⚠ 본 PBR 수치는 공개 리포트 및 추정치 기반입니다. 정확한 수치는 KRX 데이터시스템(data.krx.co.kr) 또는 FnGuide에서 직접 확인하세요. 투자 참고용이며 투자 권유가 아닙니다.
          </div>
        </div>
      </div>
      <style>{`@keyframes spin{to{transform:rotate(360deg)}}`}</style>
    </div>
  );
}
```
