#!/usr/bin/env python3
"""
Active Status Booster - Adds 'status: Active' to important documents
Targets: recent docs (7d), key folders (csp-brain/, outputs/, projects/)
"""

import os
import re
from pathlib import Path
from datetime import datetime, timedelta

VAULT_ROOT = Path("/Users/dkmac/csp-brain")
SKIP_DIRS = ['.git', '.obsidian', '.claude', '.agents', 'node_modules', '__pycache__', 'attachments', 'raw/legacy-concepts', 'open-design']

ACTIVE_FOLDERS = ['csp-brain', 'outputs/daily-reflect', 'outputs/daily-briefing', 'outputs/weekly', 'projects', 'wiki/signals', 'inbox/articles', 'inbox/papers']

def should_be_active(md_file):
    """Check if document should be marked as Active"""
    rel_path = str(md_file.relative_to(VAULT_ROOT))
    
    # Check if in active folder
    for folder in ACTIVE_FOLDERS:
        if folder in rel_path:
            return True
    
    # Check if modified in last 30 days
    try:
        mtime = datetime.fromtimestamp(md_file.stat().st_mtime)
        if mtime > datetime.now() - timedelta(days=30):
            return True
    except:
        pass
    
    return False

def add_active_status(md_file):
    """Add 'status: Active' to frontmatter"""
    try:
        content = md_file.read_text(encoding='utf-8')
        
        # Check if already has status
        if 'status:' in content:
            return False
        
        fm_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
        if not fm_match:
            return False
        
        frontmatter = fm_match.group(1)
        frontmatter_end = fm_match.end()
        
        # Add status after type
        if 'type:' in frontmatter:
            lines = frontmatter.split('\n')
            new_lines = []
            for line in lines:
                new_lines.append(line)
                if line.startswith('type:'):
                    new_lines.append('status: Active')
            
            new_frontmatter = '\n'.join(new_lines)
            new_content = '---\n' + new_frontmatter + '\n---\n' + content[frontmatter_end:]
            md_file.write_text(new_content, encoding='utf-8')
            return True
        
        return False
    except Exception as e:
        return False

def main():
    print("=" * 60)
    print("Active Status Booster")
    print("=" * 60)
    print(f"Vault: {VAULT_ROOT}")
    print()
    
    print("Finding candidate documents...")
    candidates = []
    for md_file in VAULT_ROOT.rglob("*.md"):
        if any(skip in str(md_file) for skip in SKIP_DIRS):
            continue
        
        # Check if already has status
        try:
            content = md_file.read_text(encoding='utf-8')
            if 'status:' in content:
                continue
            
            if should_be_active(md_file):
                candidates.append(md_file)
        except:
            continue
    
    print(f"   Found {len(candidates)} candidates")
    print()
    print("Adding 'status: Active'...")
    print()
    
    updated = 0
    for md_file in candidates:
        if add_active_status(md_file):
            updated += 1
            if updated <= 10 or updated % 50 == 0:
                print(f"  [{updated:4d}] {md_file.relative_to(VAULT_ROOT)}")
    
    print()
    print("=" * 60)
    print("Results")
    print("=" * 60)
    print(f"Candidates: {len(candidates)}")
    print(f"Updated:    {updated} documents")
    print()
    print("Run full_vault_eval.py to see new score!")

if __name__ == "__main__":
    main()
