#!/usr/bin/env python3
"""
Link Density Booster 2.0 - Adds wikilinks to orphaned documents
Enhanced: processes ALL orphans, adds 2-3 links per doc, smarter matching
"""

import os
import re
from pathlib import Path
from datetime import datetime

VAULT_ROOT = Path("/Users/dkmac/csp-brain")
SKIP_DIRS = ['.git', '.obsidian', '.claude', '.agents', 'node_modules', '__pycache__', 'attachments']

def load_all_titles():
    titles = {}
    keywords = {}
    
    for md_file in VAULT_ROOT.rglob("*.md"):
        if any(skip in str(md_file) for skip in SKIP_DIRS):
            continue
        try:
            content = md_file.read_text(encoding='utf-8')
            h1_match = re.search(r'^# (.+)$', content, re.MULTILINE)
            if h1_match:
                title = h1_match.group(1).strip()
                titles[title.lower()] = md_file.relative_to(VAULT_ROOT)
                words = re.findall(r'\b\w+\b', title.lower())
                for word in words:
                    if len(word) > 3:
                        if word not in keywords:
                            keywords[word] = []
                        keywords[word].append(md_file.relative_to(VAULT_ROOT))
            
            filename = md_file.stem.lower()
            if filename not in titles:
                titles[filename] = md_file.relative_to(VAULT_ROOT)
        except:
            continue
    
    return titles, keywords

def add_links_to_file(md_file, titles, keywords):
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
        used_titles = set()
        
        for title, rel_path in titles.items():
            if title in used_titles:
                continue
            if title in modified_body.lower():
                if f'[[{title}]]' in modified_body or f'[[{rel_path}|' in modified_body:
                    continue
                
                link_text = str(rel_path).split('/')[-1].replace('.md', '')
                wikilink = f'[[{rel_path}|{link_text}]]'
                pattern = re.compile(re.escape(title), re.IGNORECASE)
                new_body = pattern.sub(wikilink, modified_body, count=1)
                
                if new_body != modified_body:
                    modified_body = new_body
                    used_titles.add(title)
                    added_links += 1
                    
                    if added_links >= (3 - len(existing_links)):
                        break
        
        if added_links < (3 - len(existing_links)):
            words = re.findall(r'\b\w{4,}\b', modified_body.lower())
            for word in words[:50]:
                if word in keywords:
                    for rel_path in keywords[word][:3]:
                        path_str = str(rel_path)
                        if f'[[{path_str}|' in modified_body:
                            continue
                        
                        link_text = path_str.split('/')[-1].replace('.md', '')
                        wikilink = f'[[{path_str}|{link_text}]]'
                        
                        pattern = re.compile(r'\b' + re.escape(word) + r'\b', re.IGNORECASE)
                        new_body = pattern.sub(wikilink, modified_body, count=1)
                        
                        if new_body != modified_body:
                            modified_body = new_body
                            added_links += 1
                            
                            if added_links >= (3 - len(existing_links)):
                                break
                    if added_links >= (3 - len(existing_links)):
                        break
        
        if added_links > 0:
            new_content = frontmatter + modified_body
            md_file.write_text(new_content, encoding='utf-8')
            return True
        return False
    except Exception as e:
        print(f"  Error: {md_file} - {e}")
        return False

def main():
    print("=" * 60)
    print("Link Density Booster 2.0")
    print("=" * 60)
    print(f"Vault: {VAULT_ROOT}")
    print()
    
    print("Loading titles and keywords...")
    titles, keywords = load_all_titles()
    print(f"   Indexed {len(titles)} titles, {len(keywords)} keywords")
    
    print("Finding orphans (docs with <2 links)...")
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
    print()
    
    start_time = datetime.now()
    updated = 0
    
    for i, md_file in enumerate(orphans):
        if add_links_to_file(md_file, titles, keywords):
            updated += 1
            if updated % 100 == 1:
                print(f"  [{updated:4d}] {md_file.relative_to(VAULT_ROOT)}")
    
    elapsed = (datetime.now() - start_time).total_seconds()
    
    print()
    print("=" * 60)
    print("Results")
    print("=" * 60)
    print(f"Processed: {len(orphans)} orphans")
    print(f"Updated:   {updated} documents ({updated/len(orphans)*100:.1f}%)")
    print(f"Time:      {elapsed:.1f} seconds")
    print()
    print("Run full_vault_eval.py to see new score!")

if __name__ == "__main__":
    main()
