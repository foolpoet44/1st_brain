#!/usr/bin/env python3
"""
csp-brain Vault Eval 진단 스크립트
지식 건강 지표를 측정하여 JSON 과 HTML 대시보드를 생성합니다.
"""

import os
import json
import re
from datetime import datetime, timedelta
from pathlib import Path

# csp-brain Vault 경로
VAULT_PATH = Path("/Users/dkmac/csp-brain")
OUTPUT_DIR = VAULT_PATH
DATA_JSON_PATH = OUTPUT_DIR / "data.json"
INDEX_HTML_PATH = OUTPUT_DIR / "index.html"

def parse_frontmatter(content):
    """Markdown 파일의 YAML frontmatter 를 파싱하여 딕셔너리로 반환"""
    fm_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not fm_match:
        return {}
    
    fm_text = fm_match.group(1)
    fm_dict = {}
    for line in fm_text.split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            fm_dict[key.strip()] = value.strip().strip('"\'')
    return fm_dict

def analyze_vault():
    """Vault 전체를 스캔하여 지식 건강 지표를 계산"""
    md_files = list(VAULT_PATH.rglob("*.md"))
    
    total_docs = len(md_files)
    total_links = 0
    orphan_docs = 0
    recent_docs = 0  # 최근 7 일 이내 수정
    type_docs = 0
    active_docs = 0
    
    all_wikilinks = set()  # 전체 wikilink 모음
    doc_links = {}  # 문서별 링크 수
    
    # 최근 7 일 기준
    week_ago = datetime.now() - timedelta(days=7)
    
    for md_file in md_files:
        # attachments 폴더는 제외
        if 'attachments' in md_file.parts:
            continue
            
        try:
            content = md_file.read_text(encoding='utf-8')
            fm = parse_frontmatter(content)
            
            # Wikilink 추출 ([[link]] 패턴)
            wikilinks = re.findall(r'\[\[([^\]]+)\]\]', content)
            link_count = len(wikilinks)
            total_links += link_count
            doc_links[md_file.name] = link_count
            all_wikilinks.update(wikilinks)
            
            # 고립된 문서 (링크가 0 개)
            if link_count == 0:
                orphan_docs += 1
            
            # 최근 수정 문서
            mtime = datetime.fromtimestamp(md_file.stat().st_mtime)
            if mtime > week_ago:
                recent_docs += 1
            
            # Type 문서
            if fm.get('type') == 'Type':
                type_docs += 1
            
            # Active 상태 문서
            if fm.get('status') == 'Active':
                active_docs += 1
                
        except Exception as e:
            print(f"Error reading {md_file}: {e}")
            continue
    
    # 지표 계산
    avg_links = total_links / total_docs if total_docs > 0 else 0
    orphan_rate = (orphan_docs / total_docs * 100) if total_docs > 0 else 0
    freshness_rate = (recent_docs / total_docs * 100) if total_docs > 0 else 0
    
    # Eval 점수 (가중치 부여)
    # link_density(40%) + freshness(30%) + type_structure(20%) + active_rate(10%)
    link_score = min(avg_links / 10, 1.0) * 40  # 10 개 이상이면 만점
    freshness_score = (freshness_rate / 100) * 30
    type_score = min(type_docs / 10, 1.0) * 20  # Type 이 10 개 이상이면 만점
    active_score = (active_docs / total_docs * 100) * 0.1 if total_docs > 0 else 0
    
    eval_score = link_score + freshness_score + type_score + active_score
    
    return {
        "timestamp": datetime.now().isoformat(),
        "total_docs": total_docs,
        "total_links": total_links,
        "avg_links": round(avg_links, 2),
        "orphan_docs": orphan_docs,
        "orphan_rate": round(orphan_rate, 2),
        "recent_docs": recent_docs,
        "freshness_rate": round(freshness_rate, 2),
        "type_docs": type_docs,
        "active_docs": active_docs,
        "eval_score": round(eval_score, 2),
        "link_score": round(link_score, 2),
        "freshness_score": round(freshness_score, 2),
        "type_score": round(type_score, 2),
        "active_score": round(active_score, 2),
    }

def generate_html_dashboard(data):
    """측정 결과를 HTML 대시보드로 생성"""
    
    # Eval 점수에 따른 색상과 메시지
    eval_score = data['eval_score']
    if eval_score >= 80:
        score_color = "#22c55e"  # green
        score_message = "우수함"
    elif eval_score >= 60:
        score_color = "#eab308"  # yellow
        score_message = "보통"
    else:
        score_color = "#ef4444"  # red
        score_message = "개선 필요"
    
    html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>csp-brain Eval Dashboard</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ 
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
            color: #f1f5f9;
            min-height: 100vh;
            padding: 2rem;
        }}
        .container {{ max-width: 1200px; margin: 0 auto; }}
        h1 {{ 
            font-size: 2.5rem; 
            margin-bottom: 0.5rem;
            background: linear-gradient(90deg, #60a5fa, #a78bfa);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        .subtitle {{ color: #94a3b8; margin-bottom: 2rem; }}
        .grid {{ 
            display: grid; 
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); 
            gap: 1.5rem;
            margin-bottom: 2rem;
        }}
        .card {{
            background: rgba(30, 41, 59, 0.7);
            border: 1px solid rgba(148, 163, 184, 0.1);
            border-radius: 1rem;
            padding: 1.5rem;
            backdrop-filter: blur(10px);
        }}
        .card h3 {{ color: #94a3b8; font-size: 0.875rem; margin-bottom: 0.5rem; }}
        .card .value {{ font-size: 2.5rem; font-weight: 700; }}
        .card .unit {{ font-size: 1rem; color: #64748b; }}
        .score-card {{ 
            border: 2px solid {score_color};
            background: rgba({int(score_color[1:3], 16)}, {int(score_color[3:5], 16)}, {int(score_color[5:7], 16)}, 0.1);
        }}
        .score-value {{ color: {score_color}; }}
        .progress-bar {{
            height: 8px;
            background: rgba(148, 163, 184, 0.2);
            border-radius: 4px;
            margin-top: 1rem;
            overflow: hidden;
        }}
        .progress-fill {{
            height: 100%;
            background: linear-gradient(90deg, #60a5fa, #a78bfa);
            border-radius: 4px;
            transition: width 0.5s ease;
        }}
        .metrics {{ display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; }}
        .metric {{ 
            background: rgba(15, 23, 42, 0.5);
            padding: 1rem;
            border-radius: 0.5rem;
        }}
        .metric label {{ color: #64748b; font-size: 0.75rem; }}
        .metric .val {{ font-size: 1.25rem; font-weight: 600; margin-top: 0.25rem; }}
        .timestamp {{ color: #475569; font-size: 0.875rem; text-align: center; margin-top: 2rem; }}
        .status-badge {{
            display: inline-block;
            padding: 0.25rem 0.75rem;
            border-radius: 9999px;
            font-size: 0.75rem;
            font-weight: 600;
            background: {score_color};
            color: #fff;
            margin-top: 0.5rem;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🧠 csp-brain Eval Dashboard</h1>
        <p class="subtitle">지식 건강 상태 실시간 진단</p>
        
        <div class="grid">
            <div class="card score-card">
                <h3>EVAL SCORE</h3>
                <div class="value score-value">{data['eval_score']}<span class="unit">/100</span></div>
                <span class="status-badge">{score_message}</span>
                <div class="progress-bar">
                    <div class="progress-fill" style="width: {data['eval_score']}%"></div>
                </div>
            </div>
            
            <div class="card">
                <h3>TOTAL DOCUMENTS</h3>
                <div class="value">{data['total_docs']}<span class="unit">개</span></div>
                <div class="metrics" style="margin-top: 1rem;">
                    <div class="metric">
                        <label>Type 문서</label>
                        <div class="val">{data['type_docs']}개</div>
                    </div>
                    <div class="metric">
                        <label>Active 문서</label>
                        <div class="val">{data['active_docs']}개</div>
                    </div>
                </div>
            </div>
            
            <div class="card">
                <h3>KNOWLEDGE DENSITY</h3>
                <div class="value">{data['avg_links']}<span class="unit">링크/문서</span></div>
                <div class="metrics" style="margin-top: 1rem;">
                    <div class="metric">
                        <label>총 연결</label>
                        <div class="val">{data['total_links']}개</div>
                    </div>
                    <div class="metric">
                        <label>고립 문서</label>
                        <div class="val">{data['orphan_docs']}개 ({data['orphan_rate']}%)</div>
                    </div>
                </div>
            </div>
            
            <div class="card">
                <h3>METABOLISM</h3>
                <div class="value">{data['freshness_rate']}<span class="unit">%</span></div>
                <div class="metric" style="margin-top: 1rem;">
                    <label>최근 7 일 수정 ({data['recent_docs']}개)</label>
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: {data['freshness_rate']}%"></div>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="card">
            <h3>SCORE BREAKDOWN</h3>
            <div class="metrics" style="margin-top: 1rem;">
                <div class="metric">
                    <label>Link Density (40%)</label>
                    <div class="val">{data['link_score']}점</div>
                </div>
                <div class="metric">
                    <label>Freshness (30%)</label>
                    <div class="val">{data['freshness_score']}점</div>
                </div>
                <div class="metric">
                    <label>Type Structure (20%)</label>
                    <div class="val">{data['type_score']}점</div>
                </div>
                <div class="metric">
                    <label>Active Rate (10%)</label>
                    <div class="val">{data['active_score']}점</div>
                </div>
            </div>
        </div>
        
        <p class="timestamp">Last updated: {data['timestamp']}</p>
    </div>
</body>
</html>
"""
    return html

if __name__ == "__main__":
    print("🔍 csp-brain Vault 분석 시작...")
    
    # 분석 실행
    data = analyze_vault()
    
    # JSON 저장 (GitHub Pages 데이터 소스)
    with open(DATA_JSON_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"✅ data.json 생성됨: {DATA_JSON_PATH}")
    
    # HTML 대시보드 생성
    html_content = generate_html_dashboard(data)
    with open(INDEX_HTML_PATH, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"✅ index.html 생성됨: {INDEX_HTML_PATH}")
    
    # 콘솔 출력 (크론잡 로그용)
    print("\n📊 EVAL 결과:")
    print(f"   총점: {data['eval_score']}/100")
    print(f"   문서: {data['total_docs']}개 (링크 {data['total_links']}개)")
    print(f"   고립: {data['orphan_docs']}개 ({data['orphan_rate']}%)")
    print(f"   신선도: {data['freshness_rate']}% ({data['recent_docs']}개/7 일)")
    print(f"   상태: {'우수함' if data['eval_score'] >= 80 else '보통' if data['eval_score'] >= 60 else '개선 필요'}")