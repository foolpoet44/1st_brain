import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path
import json
from datetime import datetime, timedelta
import sys
import os
import time

# 현재 디렉토리를 경로에 추가하여 모듈 임포트 가능하게 함
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from search import HybridSearch
from ex_signal import EXIntelligenceDB, SignalDetector, ActionTrigger, Signal
from report_gen import create_report_generator

# --- 설정 및 경로 ---
BASE_DIR = Path(__file__).parent.parent
MANIFEST_PATH = BASE_DIR / "manifest.json"
INDEX_DIR = BASE_DIR / "harness" / "embeddings"
DB_PATH = BASE_DIR / "harness" / "ex_signals.json"
OUTPUT_DIR = BASE_DIR / "harness" / "output"

# 페이지 설정
st.set_page_config(
    page_title="Zavis_Brain Intelligence Dashboard",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 프리미엄 디자인 시스템 (Glassmorphism & Neon) ---
def apply_premium_style():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Pretendard+Variable:wght@100..900&display=swap');
        
        * {
            font-family: 'Pretendard Variable', -apple-system, BlinkMacSystemFont, inherit;
        }
        
        .stApp {
            background: radial-gradient(circle at top right, #1a1c24, #0f1117);
            color: #e0e0e0;
        }
        
        /* Glassmorphism Sidebar */
        [data-testid="stSidebar"] {
            background-color: rgba(30, 34, 45, 0.7);
            backdrop-filter: blur(10px);
            border-right: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        /* Custom Cards */
        .premium-card {
            background: rgba(30, 34, 45, 0.6);
            padding: 24px;
            border-radius: 16px;
            border: 1px solid rgba(255, 255, 255, 0.08);
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
            margin-bottom: 20px;
        }
        
        .neon-text {
            color: #00f2fe;
            text-shadow: 0 0 10px rgba(0, 242, 254, 0.5);
            font-weight: 700;
        }
        
        .warning-text {
            color: #ff4b2b;
            text-shadow: 0 0 10px rgba(255, 75, 43, 0.5);
        }
        
        /* Tab Styling */
        .stTabs [data-baseweb="tab-list"] {
            gap: 16px;
            background-color: transparent;
        }
        
        .stTabs [data-baseweb="tab"] {
            background-color: rgba(255, 255, 255, 0.05);
            border-radius: 12px 12px 0 0;
            padding: 12px 24px;
            color: #888;
            transition: all 0.3s ease;
        }
        
        .stTabs [data-baseweb="tab"]:hover {
            background-color: rgba(255, 255, 255, 0.1);
            color: #fff;
        }
        
        .stTabs [aria-selected="true"] {
            background-color: rgba(0, 242, 254, 0.1) !important;
            color: #00f2fe !important;
            border-bottom: 2px solid #00f2fe !important;
        }
        
        /* Metric Styling */
        div[data-testid="stMetricValue"] {
            font-size: 2.2rem;
            font-weight: 800;
            background: linear-gradient(45deg, #00f2fe, #4facfe);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        </style>
    """, unsafe_allow_html=True)

# --- 리소스 캐싱 ---
@st.cache_resource
def load_search_engine():
    searcher = HybridSearch(INDEX_DIR)
    if MANIFEST_PATH.exists():
        searcher.index_from_manifest(MANIFEST_PATH, BASE_DIR)
    return searcher

@st.cache_resource
def load_signal_db():
    return EXIntelligenceDB(DB_PATH)

@st.cache_resource
def load_report_tools():
    try:
        return create_report_generator(BASE_DIR)
    except Exception as e:
        st.error(f"보고서 도구 로드 실패: {e}")
        return None

# --- 메인 대시보드 인터페이스 ---
def main():
    apply_premium_style()
    
    # 사이드바
    with st.sidebar:
        st.markdown("<h1 style='text-align: center; color: white;'>🧠 Zavis_Brain</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #888;'>Local Intelligence Harness</p>", unsafe_allow_html=True)
        st.markdown("---")
        
        menu = st.radio(
            "Intelligence Engine",
            ["📊 EX Monitoring", "🔍 Knowledge Search", "📝 Smart Reporter"],
            index=0
        )
        
        st.markdown("---")
        st.info(f"**Vitals**\n- Core: Local SLM\n- Index: Active\n- Privacy: Maximum")
        
        with st.expander("⚙️ System Config"):
            st.checkbox("Auto-Refresh Index", value=True)
            st.slider("Anomaly Threshold", 1.0, 3.0, 2.0)

    # 1. EX Monitoring Tab
    if menu == "📊 EX Monitoring":
        st.markdown("<h1 class='neon-text'>📊 EX 인텔리전스 모니터링</h1>", unsafe_allow_html=True)
        
        db = load_signal_db()
        detector = SignalDetector()
        trigger = ActionTrigger()
        
        latest_signals = db.get_latest_signals(limit=100)
        
        if not latest_signals:
            st.warning("분석할 신호 데이터가 없습니다. `harness/indexer.py`를 실행해 주세요.")
            return

        df = pd.DataFrame([vars(s) for s in latest_signals])
        df['detected_at'] = pd.to_datetime(df['detected_at'])
        
        # 상단 핵심 메트릭
        m1, m2, m3, m4 = st.columns(4)
        with m1:
            st.metric("Total Signals", len(df))
        with m2:
            avg_score = df['score'].mean()
            st.metric("Avg EX Score", f"{avg_score:.1f}", delta=f"{avg_score-70:.1f}")
        with m3:
            anomalies = sum(1 for s in latest_signals if detector.detect_anomaly(db.get_history(s.org_unit, s.issue))['is_anomaly'])
            st.metric("Critical Alerts", anomalies, delta_color="inverse", delta=f"+{anomalies if anomalies > 0 else 0}")
        with m4:
            active_orgs = df['org_unit'].nunique()
            st.metric("Monitored Orgs", active_orgs)

        col_left, col_right = st.columns([3, 2])
        
        with col_left:
            st.markdown("### 📈 Time-Series Insight")
            selected_org = st.selectbox("조직 상세 분석", df['org_unit'].unique())
            org_df = df[df['org_unit'] == selected_org].sort_values('detected_at')
            
            fig = px.area(org_df, x='detected_at', y='score', color='issue',
                          title=f"[{selected_org}] EX Health Trend",
                          template="plotly_dark",
                          color_discrete_sequence=px.colors.qualitative.Pastel)
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color="#888")
            )
            st.plotly_chart(fig, use_container_width=True)

        with col_right:
            st.markdown("### 🕸️ Org Comparison")
            # 이슈별 평균 점수 Radar 차트 준비
            avg_by_issue = df.groupby('issue')['score'].mean().reset_index()
            fig_radar = px.line_polar(avg_by_issue, r='score', theta='issue', line_close=True,
                                     title="이슈별 건강도 프로파일", template="plotly_dark")
            fig_radar.update_traces(fill='toself', line_color='#00f2fe')
            st.plotly_chart(fig_radar, use_container_width=True)

        # 🚨 상세 경보 리스트
        st.markdown("### 🚨 REAL-TIME SIGNALS")
        for _, row in df.head(10).iterrows():
            with st.container():
                st.markdown(f"""
                    <div class="premium-card">
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <div>
                                <span style="font-weight: 800; font-size: 1.2rem;">{row['org_unit']}</span>
                                <span style="color: #888; margin-left:10px;">| {row['issue']}</span>
                            </div>
                            <div style="font-size: 1.5rem; font-weight: 800; color: {'#ff4b2b' if row['score'] < 50 else '#00f2fe'};">
                                {row['score']}
                            </div>
                        </div>
                        <div style="margin-top: 10px; font-size: 0.9rem; color: #aaa;">
                            감지시간: {row['detected_at'].strftime('%Y-%m-%d %H:%M')}
                        </div>
                    </div>
                """, unsafe_allow_html=True)

    # 2. Knowledge Search Tab
    elif menu == "🔍 Knowledge Search":
        st.markdown("<h1 class='neon-text'>🔍 시맨틱 지식 검색</h1>", unsafe_allow_html=True)
        st.markdown("로컬 임베딩 모델을 통해 문서의 의미적 맥락을 탐색합니다. (No Cloud Calls)")
        
        searcher = load_search_engine()
        
        col1, col2 = st.columns([5, 1])
        with col1:
            query = st.text_input("질문이나 키워드를 입력하세요", placeholder="CX팀의 HR 트렌드 분석 보고서 찾아줘...", key="search_query")
        with col2:
            st.write("") # Padding
            search_btn = st.button("Search 🚀", use_container_width=True)

        if query or search_btn:
            with st.spinner("지식 공간을 투영하는 중..."):
                results = searcher.search(query, top_k=10)
            
            if results:
                st.success(f"'{query}'에 대해 관련된 문서 {len(results)}건을 발견했습니다.")
                
                for i, res in enumerate(results):
                    # 카테고리별 컬러 매핑
                    cat_color = {
                        "업무보고": "#4facfe",
                        "인원현황": "#00f2fe",
                        "AI_DX": "#a18cd1",
                        "기타": "#888"
                    }.get(res.get('category', '기타'), "#888")
                    
                    with st.container():
                        st.markdown(f"""
                            <div class="premium-card">
                                <div style="display: flex; gap: 10px; align-items: center;">
                                    <span style="background: {cat_color}; color: black; padding: 2px 8px; border-radius: 4px; font-size: 0.7rem; font-weight: 800;">
                                        {res.get('category', 'UNCATEGORIZED')}
                                    </span>
                                    <span style="font-weight: 700;">{Path(res['path']).name}</span>
                                    <span style="color: #555; font-size: 0.8rem;">Score: {res['score']:.3f}</span>
                                </div>
                                <div style="margin-top: 10px; color: #ccc; font-size: 0.9rem; line-height: 1.6;">
                                    {res['snippet']}...
                                </div>
                                <div style="margin-top: 10px;">
                                    {" ".join([f'<span style="color: #666; font-size: 0.8rem;">#{tag}</span>' for tag in res.get('tags', [])])}
                                </div>
                            </div>
                        """, unsafe_allow_html=True)
            else:
                st.info("검색 결과가 없습니다. 다른 검색어를 시도해 보세요.")

    # 3. Smart Reporter Tab
    elif menu == "📝 Smart Reporter":
        st.markdown("<h1 class='neon-text'>📝 지능형 보고서 생성기</h1>", unsafe_allow_html=True)
        
        report_tools = load_report_tools()
        if not report_tools:
            st.error("보고서 생성 모듈을 초기화할 수 없습니다.")
            return

        with st.container():
            st.markdown('<div class="premium-card">', unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            with col1:
                week_val = st.text_input("보고 주차", value=datetime.now().strftime("%W주차 (%m월 %d일)"))
            with col2:
                team_val = st.text_input("대상 조직", value="생산기술 HR 실")
            
            items_text = st.text_area("주요 업무 실적 (리스트 형식)", height=150, 
                                     placeholder="- 스마트 팩토리 인재 육성 전략 수립: 초안 완료\n- HR 데이터 클렌징: 80% 진행")
            
            gen_btn = st.button("보고서 초안 생성 및 PPTX 변환 🚀", use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        if gen_btn:
            # 파싱 로직
            items = []
            for line in items_text.split('\n'):
                if line.strip().startswith('-'):
                    line = line[1:].strip()
                    if ':' in line:
                        task, result = line.split(':', 1)
                        items.append({"task": task.strip(), "result": result.strip(), "status": "진행완료"})
                    else:
                        items.append({"task": line, "result": "기록됨", "status": "진행중"})

            if not items:
                st.warning("입력된 항목이 없습니다. 기본 예시로 생성합니다.")
                items = [{"task": "업무 자동화 시스템 구축", "result": "완료", "status": "완료"}]

            with st.spinner("AI가 보고 맥락을 분석하고 슬라이드를 구성합니다..."):
                time.sleep(1) # 시뮬레이션
                report_content = report_tools["generator"].generate_weekly_report(
                    week=week_val,
                    team=team_val,
                    items=items
                )
                
                # 결과 표시
                st.markdown("### 📄 Draft Preview")
                st.markdown(f'<div class="premium-card" style="background: rgba(255,255,255,0.03); white-space: pre-wrap;">{report_content}</div>', unsafe_allow_html=True)
                
                # PPTX 생성 및 다운로드
                out_file = f"Zavis_Weekly_{datetime.now().strftime('%m%d_%H%M')}.pptx"
                out_path = OUTPUT_DIR / out_file
                OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
                
                report_tools["exporter"].export(report_content, out_path)
                
                if out_path.exists():
                    with open(out_path, "rb") as f:
                        st.download_button(
                            label="📥 PowerPoint(.pptx) 다운로드",
                            data=f,
                            file_name=out_file,
                            mime="application/vnd.openxmlformats-officedocument.presentationml.presentation",
                            use_container_width=True
                        )

    # Footer
    st.markdown("---")
    st.markdown(f"""
        <div style="text-align: center; color: #555; font-size: 0.8rem;">
            Zavis_Brain Harness Engine | Build: 2026.04.14 | Mode: 100% Local Intelligence<br>
            Powered by Python, Streamlit & Sentence-Transformers
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
