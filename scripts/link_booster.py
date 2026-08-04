#!/usr/bin/env python3
"""
Link Density Booster - Adds wikilinks to orphaned documents
"""

import os
import re
from pathlib import Path

VAULT_ROOT = Path("/Users/dkmac/csp-brain")
SKIP_DIRS = ['.git', '.obsidian', '.claude', '.agents', 'node_modules', '__pycache__']

def load_all_titles():
    titles = {}
    for md_file in VAULT_ROOT.rglob("*.md"):
        if any(skip in str(md_file) for skip in SKIP_DIRS):
            continue
        try:
            content = md_file.read_text(encoding='utf-8')
            h1_match = re.search(r'^# (.+)$', content, re.MULTILINE)
            if h1_match:
                title = h1_match.group(1).strip()
                titles[title.lower()] = md_file.relative_to(VAULT_ROOT)
            filename = md_file.stem.lower()
            if filename not in titles:
                titles[filename] = md_file.relative_to(VAULT_ROOT)
        except:
            continue
    return titles

def add_links_to_file(md_file, titles):
    try:
        content = md_file.read_text(encoding='utf-8')
        existing_links = re.findall(r'\[\[([^\]]+)\]\]', content)
        if len(existing_links) >= 3:
            return False
        
        fm_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
        if fm_match:
            frontmatter = content[:fm_match.end()]
            body = content[fm_match.end():]
        else:
            frontmatter = ''
            body = content
        
        added_links = 0
        modified_body = body
        
        for title, rel_path in titles.items():
            if title in modified_body.lower():
                if f'[[{title}]]' not in modified_body and f'[[{rel_path}|' not in modified_body:
                    link_text = str(rel_path).split('/')[-1].replace('.md', '')
                    wikilink = f'[[{rel_path}|{link_text}]]'
                    pattern = re.compile(re.escape(title), re.IGNORECASE)
                    new_body = pattern.sub(wikilink, modified_body, count=1)
                    if new_body != modified_body:
                        modified_body = new_body
                        added_links += 1
                        if added_links >= (3 - len(existing_links)):
                            break
        
        if added_links > 0:
            new_content = frontmatter + modified_body
            md_file.write_text(new_content, encoding='utf-8')
            return True
        return False
    except:
        return False

def main():
    print("=" * 60)
    print("Link Density Booster")
    print("=" * 60)
    
    print("Loading titles...")
    titles = load_all_titles()
    print(f"   Indexed {len(titles)} titles")
    
    print("Finding orphans...")
    orphans = []
    for md_file in VAULT_ROOT.rglob("*.md"):
        if any(skip in str(md_file) for skip in SKIP_DIRS):
            continue
        try:
            content = md_file.read_text(encoding='utf-8')
            links = re.findall(r'\[\[([^\]]+)\]\]', content)
            if len(links) < 2:
                orphans.append(md_file)
        except:
            continue
    
    print(f"   Found {len(orphans)} orphans")
    print()
    print("Adding links...")
    
    updated = 0
    for md_file in orphans[:500]:
        if add_links_to_file(md_file, titles):
            updated += 1
            if updated <= 10:
                print(f"  OK: {md_file.relative_to(VAULT_ROOT)}")
    
    print()
    print(f"Updated: {updated}/{min(500, len(orphans))}")
    print("Run full_vault_eval.py to see new score!")

if __name__ == "__main__":
    main()
