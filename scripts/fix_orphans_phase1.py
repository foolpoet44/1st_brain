#!/usr/bin/env python3
"""
Eval Health Recovery Script - Phase 1
Add Type frontmatter to orphaned documents based on directory structure.

Target: 7,442 orphan docs → Add Type to 3,000+ docs
"""

import os
import re
from pathlib import Path
from datetime import datetime

# Vault configuration
VAULT_ROOT = Path("/Users/dkmac/csp-brain")
DRY_RUN = False  # Set True to test without writing

# Directory to Type mapping
DIR_TYPE_MAP = {
    'inbox/': ('Note', 'status: Inbox'),
    'syncs/': ('Note', 'status: Synced'),
    'projects/': ('Project', 'status: Active'),
    'people/': ('Person', ''),
    'decisions/': ('Decision', ''),
    'atoms/': ('Concept', ''),
    'thinklog/': ('Reflection', ''),
    'wiki/': ('Concept', ''),
    'outputs/daily-reflect/': ('Reflection', ''),
    'outputs/analyses/': ('Note', ''),
    'outputs/briefs/': ('Note', ''),
    'analysis/': ('Note', ''),
    'references/': ('Resource', ''),
    'templates/': ('Resource', ''),
    'raw/': ('Resource', ''),
}

# Skip patterns
SKIP_DIRS = ['.git', '.obsidian', '.claude', '.agents', 'node_modules', '__pycache__']

def get_type_for_path(rel_path: str) -> tuple[str, str]:
    """Determine Type and additional frontmatter based on directory path."""
    for dir_prefix, (doc_type, extra_fm) in DIR_TYPE_MAP.items():
        if rel_path.startswith(dir_prefix):
            return doc_type, extra_fm
    return ('Note', '')  # Default fallback

def add_frontmatter(md_file: Path) -> bool:
    """Add Type frontmatter to a markdown file if missing."""
    try:
        content = md_file.read_text(encoding='utf-8')
        
        # Check if already has type
        if re.search(r'^type:\s*\w+', content, re.MULTILINE):
            return False  # Already has type
        
        # Parse existing frontmatter
        fm_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
        
        if fm_match:
            # Has frontmatter, add type
            existing_fm = fm_match.group(1)
            if 'type:' not in existing_fm:
                rel_path = str(md_file.relative_to(VAULT_ROOT))
                doc_type, extra_fm = get_type_for_path(rel_path)
                
                new_fm = f"type: {doc_type}\n{existing_fm}"
                if extra_fm:
                    new_fm = f"{extra_fm}\n{new_fm}"
                
                new_content = content.replace(fm_match.group(0), f"---\n{new_fm}\n---\n")
                
                if not DRY_RUN:
                    md_file.write_text(new_content, encoding='utf-8')
                return True
        else:
            # No frontmatter, add new
            rel_path = str(md_file.relative_to(VAULT_ROOT))
            doc_type, extra_fm = get_type_for_path(rel_path)
            
            new_fm = f"---\ntype: {doc_type}\n"
            if extra_fm:
                new_fm = f"---\n{extra_fm}\ntype: {doc_type}\n"
            else:
                new_fm = f"---\ntype: {doc_type}\n"
            new_fm += "---\n\n"
            
            new_content = new_fm + content
            
            if not DRY_RUN:
                md_file.write_text(new_content, encoding='utf-8')
            return True
            
    except Exception as e:
        print(f"  ⚠️  Error processing {md_file}: {e}")
        return False

def main():
    print("=" * 60)
    print("Eval Health Recovery - Phase 1: Type Assignment")
    print("=" * 60)
    print(f"Vault: {VAULT_ROOT}")
    print(f"Dry Run: {DRY_RUN}")
    print()
    
    processed = 0
    updated = 0
    skipped = 0
    
    # Find all markdown files
    for md_file in VAULT_ROOT.rglob("*.md"):
        # Skip special directories
        if any(skip in str(md_file) for skip in SKIP_DIRS):
            skipped += 1
            continue
        
        # Skip Type files themselves
        if 'Type/' in str(md_file):
            continue
        
        rel_path = str(md_file.relative_to(VAULT_ROOT))
        processed += 1
        
        if add_frontmatter(md_file):
            updated += 1
            if updated <= 20:  # Show first 20
                print(f"  ✅ {rel_path}")
    
    print()
    print("=" * 60)
    print("Summary")
    print("=" * 60)
    print(f"Processed: {processed}")
    print(f"Updated:   {updated}")
    print(f"Skipped:   {skipped}")
    print()
    
    if DRY_RUN:
        print("⚠️  DRY RUN MODE - No files were modified")
        print("   Set DRY_RUN = False to apply changes")
    else:
        print("✅ Changes applied! Run know_grow_monitor.py to verify")

if __name__ == "__main__":
    main()
