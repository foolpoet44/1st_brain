#!/usr/bin/env python3
"""
csp-brain Full Vault Eval Dashboard
Calculates health metrics for ALL documents in the vault (not just wiki/).
"""

import json
import os
import re
from datetime import datetime, timedelta
from pathlib import Path

VAULT_ROOT = Path("/Users/dkmac/csp-brain")
OUTPUT_JSON = VAULT_ROOT / "data.json"
OUTPUT_HTML = VAULT_ROOT / "index.html"

SKIP_DIRS = ['.git', '.obsidian', '.claude', '.agents', 'node_modules', '__pycache__', '.cursor', '.vscode']
VALID_TYPES = ['Note', 'Project', 'Person', 'Concept', 'Decision', 'Resource', 'Reflection', 'Task', 'Idea', 'Meeting', 'Type', 'Dashboard']

def scan_vault():
    docs = []
    now = datetime.now()
    seven_days_ago = now - timedelta(days=7)
    thirty_days_ago = now - timedelta(days=30)
    
    for md_file in VAULT_ROOT.rglob("*.md"):
        if any(skip in str(md_file) for skip in SKIP_DIRS):
            continue
        
        rel_path = str(md_file.relative_to(VAULT_ROOT))
        
        try:
            content = md_file.read_text(encoding='utf-8')
            mtime = datetime.fromtimestamp(md_file.stat().st_mtime)
            
            fm_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
            frontmatter = {}
            if fm_match:
                fm_text = fm_match.group(1)
                for line in fm_text.split('\n'):
                    if ':' in line:
                        key, value = line.split(':', 1)
                        frontmatter[key.strip()] = value.strip()
            
            body = content[fm_match.end():] if fm_match else content
            wikilinks = re.findall(r'\[\[([^\]]+)\]\]', body)
            
            doc = {
                'path': rel_path,
                'mtime': mtime,
                'type': frontmatter.get('type', ''),
                'status': frontmatter.get('status', ''),
                'links': len(wikilinks),
                'is_recent_7d': mtime > seven_days_ago,
                'is_recent_30d': mtime > thirty_days_ago,
                'is_active': frontmatter.get('status') == 'Active',
                'has_valid_type': frontmatter.get('type', '') in VALID_TYPES,
            }
            docs.append(doc)
            
        except Exception as e:
            print(f"  Error reading {rel_path}: {e}")
            continue
    
    return docs

def calculate_metrics(docs):
    now = datetime.now()
    total = len(docs)
    if total == 0:
        return None
    
    total_links = sum(d['links'] for d in docs)
    avg_links = total_links / total if total > 0 else 0
    
    orphan_docs = sum(1 for d in docs if d['links'] == 0)
    orphan_rate = (orphan_docs / total) * 100 if total > 0 else 0
    
    recent_7d = sum(1 for d in docs if d['is_recent_7d'])
    freshness_rate = (recent_7d / total) * 100 if total > 0 else 0
    
    type_docs = sum(1 for d in docs if d['has_valid_type'])
    type_rate = (type_docs / total) * 100 if total > 0 else 0
    
    active_docs = sum(1 for d in docs if d['is_active'])
    active_rate = (active_docs / total) * 100 if total > 0 else 0
    
    link_score = min(avg_links / 3.0, 1.0) * 40
    freshness_score = min(freshness_rate / 10.0, 1.0) * 20
    type_score = min(type_rate / 80.0, 1.0) * 25
    active_score = min(active_rate / 20.0, 1.0) * 15
    
    eval_score = link_score + freshness_score + type_score + active_score
    
    return {
        'timestamp': now.isoformat(),
        'total_docs': total,
        'total_links': total_links,
        'avg_links': round(avg_links, 2),
        'orphan_docs': orphan_docs,
        'orphan_rate': round(orphan_rate, 2),
        'recent_docs': recent_7d,
        'freshness_rate': round(freshness_rate, 2),
        'type_docs': type_docs,
        'type_rate': round(type_rate, 2),
        'active_docs': active_docs,
        'active_rate': round(active_rate, 2),
        'eval_score': round(eval_score, 2),
        'link_score': round(link_score, 2),
        'freshness_score': round(freshness_score, 2),
        'type_score': round(type_score, 2),
        'active_score': round(active_score, 2),
    }

def main():
    print("=" * 60)
    print("csp-brain Full Vault Eval Scan")
    print("=" * 60)
    print(f"Vault: {VAULT_ROOT}")
    print()
    
    print("Scanning vault...")
    docs = scan_vault()
    print(f"   Found {len(docs)} documents")
    print()
    
    print("Calculating metrics...")
    metrics = calculate_metrics(docs)
    
    if not metrics:
        print("No documents found!")
        return
    
    print()
    print("=" * 60)
    print("Eval Summary")
    print("=" * 60)
    print(f"Total Documents: {metrics['total_docs']:,}")
    print(f"Total Links: {metrics['total_links']:,}")
    print(f"Avg Links/Doc: {metrics['avg_links']}")
    print(f"Orphan Docs: {metrics['orphan_docs']:,} ({metrics['orphan_rate']}%)")
    print(f"Recent (7d): {metrics['recent_docs']} ({metrics['freshness_rate']}%)")
    print(f"Type Coverage: {metrics['type_docs']:,} ({metrics['type_rate']}%)")
    print(f"Active Docs: {metrics['active_docs']:,} ({metrics['active_rate']}%)")
    print()
    print("=" * 60)
    print("Eval Score")
    print("=" * 60)
    print(f"Link Score: {metrics['link_score']:.1f}/40")
    print(f"Freshness Score: {metrics['freshness_score']:.1f}/20")
    print(f"Type Score: {metrics['type_score']:.1f}/25")
    print(f"Active Score: {metrics['active_score']:.1f}/15")
    print(f"--------------------------------")
    print(f"TOTAL: {metrics['eval_score']:.1f}/100")
    print()
    
    with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
        json.dump(metrics, f, indent=2, ensure_ascii=False)
    print(f"Written: {OUTPUT_JSON}")

if __name__ == "__main__":
    main()
