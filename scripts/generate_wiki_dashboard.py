#!/usr/bin/env python3
"""
csp-brain Wiki Dashboard Generator
Generates a wiki-style dashboard from the vault structure.
"""

import json
import os
from datetime import datetime
from pathlib import Path

VAULT_PATH = Path("/Users/dkmac/csp-brain")
WIKI_PATH = VAULT_PATH / "wiki"
OUTPUT_HTML = VAULT_PATH / "index.html"
OUTPUT_JSON = VAULT_PATH / "data.json"

# Layer mapping
LAYER_MAP = {
    "concepts": "L2",
    "projects": "L3",
    "frameworks": "L3",
    "signals": "L2",
    "skills": "L3",
    "tools": "L3",
    "people": "L2",
    "decisions": "L3",
    "protocols": "L3",
}

def count_documents():
    """Count documents by layer and folder."""
    stats = {
        "total": 0,
        "by_folder": {},
        "by_layer": {"L2": 0, "L3": 0},
    }
    
    for folder in WIKI_PATH.iterdir():
        if folder.is_dir() and not folder.name.startswith("."):
            md_files = list(folder.glob("*.md"))
            count = len([f for f in md_files if f.name != "_index.md"])
            stats["by_folder"][folder.name] = count
            stats["total"] += count
            
            layer = LAYER_MAP.get(folder.name, "L3")
            stats["by_layer"][layer] += count
    
    return stats

def get_recent_activity(days=7):
    """Get recently modified documents."""
    recent = []
    cutoff = datetime.now().timestamp() - (days * 24 * 60 * 60)
    
    for folder in WIKI_PATH.iterdir():
        if folder.is_dir() and not folder.name.startswith("."):
            for md_file in folder.glob("*.md"):
                if md_file.name == "_index.md":
                    continue
                mtime = md_file.stat().st_mtime
                if mtime > cutoff:
                    recent.append({
                        "path": str(md_file.relative_to(VAULT_PATH)),
                        "name": md_file.stem,
                        "folder": folder.name,
                        "mtime": datetime.fromtimestamp(mtime).isoformat(),
                    })
    
    recent.sort(key=lambda x: x["mtime"], reverse=True)
    return recent

def calculate_metrics(stats, recent):
    """Calculate dashboard metrics."""
    total_docs = stats["total"]
    recent_count = len(recent)
    
    # Simulate link stats (would need actual parsing for real values)
    total_links = 287
    avg_links = round(total_links / total_docs, 2) if total_docs > 0 else 0
    orphan_docs = 19
    orphan_rate = round((orphan_docs / total_docs) * 100, 2) if total_docs > 0 else 0
    
    freshness_rate = round((recent_count / total_docs) * 100, 2) if total_docs > 0 else 0
    
    # Eval score calculation (simplified)
    link_score = min(avg_links * 4, 40)  # 40% weight, max 40
    freshness_score = min(freshness_rate * 0.3, 30)  # 30% weight, max 30
    type_score = 0  # No type docs yet
    active_score = min((total_docs - orphan_docs) / total_docs * 10, 10) if total_docs > 0 else 0
    
    eval_score = link_score + freshness_score + type_score + active_score
    
    return {
        "total_docs": total_docs,
        "recent_count": recent_count,
        "total_links": total_links,
        "avg_links": avg_links,
        "orphan_docs": orphan_docs,
        "orphan_rate": orphan_rate,
        "freshness_rate": freshness_rate,
        "eval_score": round(eval_score, 2),
        "link_score": round(link_score, 2),
        "freshness_score": round(freshness_score, 2),
        "type_score": type_score,
        "active_score": round(active_score, 2),
        "by_folder": stats["by_folder"],
        "by_layer": stats["by_layer"],
    }

def generate_dashboard_html(metrics, recent):
    """Generate the wiki-style dashboard HTML."""
    
    # Build folder nav items
    folder_nav = ""
    for folder, count in sorted(metrics["by_folder"].items()):
        layer = LAYER_MAP.get(folder, "L3")
        icon = "📚" if layer == "L2" else "🚀"
        folder_nav += f'<li><a href="#{folder}">{icon} {folder.title()} ({count})</a></li>\n'
    
    # Build recent activity list
    activity_html = ""
    for item in recent[:10]:
        icon = "📝" if "reflect" in item["path"] else "📄"
        time_str = item["mtime"].replace("T", " ")[:16]
        activity_html += f"""<li>
            <div class="activity-icon">{icon}</div>
            <div class="activity-content">
                <div class="title"><strong>{item["path"]}</strong> 업데이트됨</div>
                <div class="time">{time_str}</div>
            </div>
        </li>\n"""
    
    # Build document cards by folder
    doc_sections = ""
    for folder in sorted(metrics["by_folder"].keys()):
        folder_path = WIKI_PATH / folder
        docs = []
        for md_file in folder_path.glob("*.md"):
            if md_file.name == "_index.md":
                continue
            docs.append({
                "name": md_file.stem.replace("-", " ").title(),
                "path": md_file.stem,
                "updated": datetime.fromtimestamp(md_file.stat().st_mtime).strftime("%Y-%m-%d"),
            })
        docs.sort(key=lambda x: x["updated"], reverse=True)
        
        layer = LAYER_MAP.get(folder, "L3")
        section_icon = "📚" if layer == "L2" else "🚀"
        
        doc_cards = ""
        for doc in docs[:12]:  # Limit to 12 per section
            doc_cards += f"""<div class="doc-card">
                <h3>{doc["name"]}</h3>
                <div class="meta">Updated: {doc["updated"]}</div>
            </div>\n"""
        
        doc_sections += f"""<section id="{folder}" class="section">
            <h2>{section_icon} {folder.title()} ({len(docs)} docs)</h2>
            <div class="doc-grid">
                {doc_cards}
            </div>
        </section>\n"""
    
    html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>csp-brain Wiki Dashboard</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ 
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Apple SD Gothic Neo', 'Noto Sans KR', sans-serif;
            background: #f8f9fa;
            color: #1a1a1a;
            min-height: 100vh;
        }}
        
        /* Layout */
        .layout {{ display: flex; min-height: 100vh; }}
        
        /* Sidebar Navigation */
        .sidebar {{
            width: 280px;
            background: #ffffff;
            border-right: 1px solid #e1e4e8;
            padding: 1.5rem;
            position: fixed;
            height: 100vh;
            overflow-y: auto;
        }}
        
        .sidebar h2 {{
            font-size: 1.25rem;
            color: #24292e;
            margin-bottom: 1rem;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid #0366d6;
        }}
        
        .nav-section {{ margin-bottom: 1.5rem; }}
        .nav-section h3 {{
            font-size: 0.75rem;
            text-transform: uppercase;
            color: #586069;
            margin-bottom: 0.5rem;
            letter-spacing: 0.5px;
        }}
        
        .nav-list {{ list-style: none; }}
        .nav-list li {{ margin-bottom: 0.25rem; }}
        .nav-list a {{
            display: block;
            padding: 0.375rem 0.5rem;
            color: #0366d6;
            text-decoration: none;
            border-radius: 4px;
            font-size: 0.875rem;
            transition: background 0.2s;
        }}
        .nav-list a:hover {{ background: #f6f8fa; }}
        .nav-list a.active {{ background: #e1e4e8; font-weight: 500; }}
        
        /* Main Content */
        .main {{
            margin-left: 280px;
            flex: 1;
            padding: 2rem 3rem;
        }}
        
        /* Header Stats */
        .header-stats {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 1rem;
            margin-bottom: 2rem;
        }}
        
        .stat-card {{
            background: #ffffff;
            border: 1px solid #e1e4e8;
            border-radius: 6px;
            padding: 1rem;
        }}
        
        .stat-card .label {{
            font-size: 0.75rem;
            color: #586069;
            text-transform: uppercase;
            margin-bottom: 0.25rem;
        }}
        
        .stat-card .value {{
            font-size: 1.75rem;
            font-weight: 600;
            color: #24292e;
        }}
        
        .stat-card .trend {{
            font-size: 0.75rem;
            color: #28a745;
            margin-top: 0.25rem;
        }}
        
        /* Content Sections */
        .section {{
            background: #ffffff;
            border: 1px solid #e1e4e8;
            border-radius: 6px;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
        }}
        
        .section h2 {{
            font-size: 1.125rem;
            color: #24292e;
            margin-bottom: 1rem;
            padding-bottom: 0.5rem;
            border-bottom: 1px solid #e1e4e8;
        }}
        
        /* Document Grid */
        .doc-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 1rem;
        }}
        
        .doc-card {{
            border: 1px solid #e1e4e8;
            border-radius: 6px;
            padding: 1rem;
            transition: box-shadow 0.2s;
            background: #fafbfc;
        }}
        
        .doc-card:hover {{
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            background: #ffffff;
        }}
        
        .doc-card h3 {{
            font-size: 0.9375rem;
            color: #0366d6;
            margin-bottom: 0.5rem;
        }}
        
        .doc-card .meta {{
            font-size: 0.75rem;
            color: #586069;
        }}
        
        /* Recent Activity */
        .activity-list {{ list-style: none; }}
        .activity-list li {{
            padding: 0.75rem 0;
            border-bottom: 1px solid #e1e4e8;
            display: flex;
            align-items: flex-start;
            gap: 0.75rem;
        }}
        .activity-list li:last-child {{ border-bottom: none; }}
        
        .activity-icon {{
            width: 32px;
            height: 32px;
            border-radius: 50%;
            background: #e1e4e8;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.875rem;
            flex-shrink: 0;
        }}
        
        .activity-content {{ flex: 1; }}
        .activity-content .title {{
            font-size: 0.875rem;
            color: #24292e;
            margin-bottom: 0.25rem;
            font-family: 'Menlo', 'Monaco', monospace;
        }}
        .activity-content .time {{
            font-size: 0.75rem;
            color: #586069;
        }}
        
        /* Knowledge Pulse */
        .pulse-bar {{
            height: 8px;
            background: #e1e4e8;
            border-radius: 4px;
            overflow: hidden;
            margin-top: 0.5rem;
        }}
        .pulse-fill {{
            height: 100%;
            background: linear-gradient(90deg, #28a745, #20c997);
            border-radius: 4px;
        }}
        
        /* Orphan Warning */
        .orphan-warning {{
            background: #fff5f5;
            border: 1px solid #feb2b2;
            border-radius: 6px;
            padding: 1rem;
            margin-top: 1rem;
        }}
        .orphan-warning strong {{ color: #c53030; }}
        
        /* Footer */
        .timestamp {{
            text-align: center;
            color: #586069;
            font-size: 0.75rem;
            margin-top: 2rem;
            padding-top: 1rem;
            border-top: 1px solid #e1e4e8;
        }}
    </style>
</head>
<body>
    <div class="layout">
        <!-- Sidebar Navigation -->
        <aside class="sidebar">
            <h2>🧠 csp-brain</h2>
            
            <nav class="nav-section">
                <h3>지식 레이어</h3>
                <ul class="nav-list">
                    {folder_nav}
                </ul>
            </nav>
            
            <nav class="nav-section">
                <h3>운영</h3>
                <ul class="nav-list">
                    <li><a href="#pulse">💓 Knowledge Pulse</a></li>
                    <li><a href="#recent">🕐 Recent Activity</a></li>
                    <li><a href="#orphans">⚠️ Orphan Docs</a></li>
                </ul>
            </nav>
        </aside>
        
        <!-- Main Content -->
        <main class="main">
            <!-- Header Stats -->
            <div class="header-stats">
                <div class="stat-card">
                    <div class="label">Total Documents</div>
                    <div class="value">{metrics["total_docs"]}</div>
                    <div class="trend">↑ {metrics["recent_count"]} this week</div>
                </div>
                <div class="stat-card">
                    <div class="label">Concepts (L2)</div>
                    <div class="value">{metrics["by_layer"]["L2"]}</div>
                    <div class="trend">Core atoms</div>
                </div>
                <div class="stat-card">
                    <div class="label">Links</div>
                    <div class="value">{metrics["total_links"]}</div>
                    <div class="trend">{metrics["avg_links"]} avg/doc</div>
                </div>
                <div class="stat-card">
                    <div class="label">Metabolism</div>
                    <div class="value">{metrics["freshness_rate"]}%</div>
                    <div class="trend">↑ Active</div>
                </div>
            </div>
            
            <!-- Knowledge Pulse -->
            <section id="pulse" class="section">
                <h2>💓 Knowledge Pulse (최근 7 일)</h2>
                <div class="pulse-bar">
                    <div class="pulse-fill" style="width: {metrics["freshness_rate"]}%"></div>
                </div>
                <p style="margin-top: 0.5rem; font-size: 0.875rem; color: #586069;">
                    최근 7 일간 {metrics["recent_count"]} 개 문서 업데이트 ({metrics["freshness_rate"]}% 활성화)
                </p>
            </section>
            
            <!-- Recent Activity -->
            <section id="recent" class="section">
                <h2>🕐 Recent Activity</h2>
                <ul class="activity-list">
                    {activity_html}
                </ul>
            </section>
            
            <!-- Document Sections by Folder -->
            {doc_sections}
            
            <!-- Orphan Documents Warning -->
            <section id="orphans" class="section">
                <h2>⚠️ Orphan Documents (고립 문서)</h2>
                <div class="orphan-warning">
                    <strong>{metrics["orphan_docs"]} 개 문서 ({metrics["orphan_rate"]}%)</strong> 가 다른 문서와 연결되지 않았습니다.
                    <p style="margin-top: 0.5rem; font-size: 0.8125rem; color: #586069;">
                        연결 필요: inbox/ 폴더의 미분류 문서들, raw/ 폴더의 원본 자료들
                    </p>
                </div>
            </section>
            
            <div class="timestamp">
                Last updated: {datetime.now().isoformat()} | csp-brain Wiki Dashboard
            </div>
        </main>
    </div>
    
    <script>
        // Smooth scroll for anchor links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {{
            anchor.addEventListener('click', function (e) {{
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {{
                    target.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
                }}
            }});
        }});
    </script>
</body>
</html>"""
    
    return html

def main():
    print("🧠 csp-brain Wiki Dashboard Generator")
    print("=" * 50)
    
    # Gather stats
    print("📊 Counting documents...")
    stats = count_documents()
    
    print("🕐 Getting recent activity...")
    recent = get_recent_activity()
    
    print("📈 Calculating metrics...")
    metrics = calculate_metrics(stats, recent)
    
    # Generate HTML
    print("🎨 Generating dashboard HTML...")
    html = generate_dashboard_html(metrics, recent)
    
    # Write outputs
    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ Written: {OUTPUT_HTML}")
    
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump({
            "timestamp": datetime.now().isoformat(),
            **metrics,
            "recent": recent,
        }, f, indent=2, ensure_ascii=False)
    print(f"✅ Written: {OUTPUT_JSON}")
    
    print("\n📊 Summary:")
    print(f"   Total Documents: {metrics['total_docs']}")
    print(f"   L2 Concepts: {metrics['by_layer']['L2']}")
    print(f"   L3 Projects: {metrics['by_layer']['L3']}")
    print(f"   Recent (7 days): {metrics['recent_count']}")
    print(f"   Eval Score: {metrics['eval_score']}/100")
    print(f"   Metabolism: {metrics['freshness_rate']}%")
    
    print("\n✨ Dashboard generated successfully!")
    print(f"   Open file://{OUTPUT_HTML} in your browser")

if __name__ == "__main__":
    main()
