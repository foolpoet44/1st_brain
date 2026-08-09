#!/usr/bin/env python3
"""INGEST 프로토콜 1 단계 — 미처리 파일 수집"""
import os
import json
import re
from datetime import datetime

# Vault 경로 발견 (하드코딩 금지)
vault_path = None
for base in ["/Users/dkmac", "/opt", "/output", "/home", "/root", "/data"]:
    if os.path.exists(base):
        for root, dirs, files in os.walk(base):
            if "_ops" in dirs or "change-log.md" in files or "KNOWLEDGE_PULSE.md" in files:
                vault_path = root
                break
        if vault_path:
            break

if not vault_path:
    print("ERROR: csp-brain vault 를 찾을 수 없습니다.")
    exit(1)

print(f"=== Vault 발견: {vault_path} ===\n")

# 디렉토리 구조 확인
inbox_path = os.path.join(vault_path, "inbox")
briefings_path = os.path.join(vault_path, "outputs", "briefings")
signals_path = os.path.join(vault_path, "wiki", "signals")
concepts_path = os.path.join(vault_path, "wiki", "concepts")
ops_path = os.path.join(vault_path, "_ops")

# 필수 디렉토리 생성
for d in [inbox_path, briefings_path, signals_path, concepts_path, ops_path]:
    os.makedirs(d, exist_ok=True)

def is_processed(filepath):
    """frontmatter 에 processed: true 가 있는지 확인"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read(2000)
        if content.startswith('---'):
            end = content.find('---', 3)
            if end > 0:
                frontmatter = content[4:end]
                if 'processed: true' in frontmatter or 'processed:true' in frontmatter:
                    return True
        return False
    except Exception as e:
        print(f"  [WARN] {filepath} 읽기 오류: {e}")
        return False

def extract_metadata(filepath):
    """파일에서 메타데이터 추출"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read(5000)
        
        metadata = {
            'path': filepath,
            'filename': os.path.basename(filepath),
            'title': None,
            'date': None,
            'source': None,
            'tags': [],
            'stats': []
        }
        
        if content.startswith('---'):
            end = content.find('---', 3)
            if end > 0:
                frontmatter = content[4:end]
                for line in frontmatter.split('\n'):
                    if ':' in line:
                        key, val = line.split(':', 1)
                        key = key.strip()
                        val = val.strip().strip('"\'')
                        if key == 'title':
                            metadata['title'] = val
                        elif key == 'date':
                            metadata['date'] = val
                        elif key == 'source':
                            metadata['source'] = val
                        elif key == 'tags' and val.startswith('['):
                            metadata['tags'] = val.strip('[]').split(',')
        
        stat_pattern = r'\d+(?:\.\d+)?(?:%| Billion| Trillion| 배| 명| 점)'
        metadata['stats'] = re.findall(stat_pattern, content[:3000])
        
        h_pattern = r'#+\s+(.+)'
        h_matches = re.findall(h_pattern, content[1000:3000])
        if h_matches:
            metadata['headline'] = h_matches[0].strip()
        
        return metadata
    except Exception as e:
        print(f"  [WARN] {filepath} 메타데이터 추출 오류: {e}")
        return None

# inbox/ 스캔
inbox_files = []
if os.path.exists(inbox_path):
    for f in os.listdir(inbox_path):
        if f.endswith('.md'):
            filepath = os.path.join(inbox_path, f)
            if not is_processed(filepath):
                inbox_files.append(filepath)

# outputs/briefings/ 스캔
briefing_files = []
if os.path.exists(briefings_path):
    for f in os.listdir(briefings_path):
        if f.endswith('.md'):
            filepath = os.path.join(briefings_path, f)
            if not is_processed(filepath):
                briefing_files.append(filepath)

print(f"=== 미처리 파일 수집 완료 ===")
print(f"  inbox/: {len(inbox_files)}개")
for f in inbox_files:
    print(f"    - {os.path.basename(f)}")

print(f"  outputs/briefings/: {len(briefing_files)}개")
for f in briefing_files:
    print(f"    - {os.path.basename(f)}")

total_files = len(inbox_files) + len(briefing_files)
if total_files == 0:
    print("\n=== 편입 대상 없음 ===")
    print("모든 파일이 이미 처리되었거나, 새 브리핑이 없습니다.")
else:
    print(f"\n=== 총 {total_files}개 파일 편입 대기 ===")

print("\n=== 파일 메타데이터 ===")
all_files = []
for filepath in inbox_files + briefing_files:
    meta = extract_metadata(filepath)
    if meta:
        all_files.append(meta)
        print(f"\n  [{os.path.basename(meta['path'])}]")
        print(f"    제목: {meta['title']}")
        print(f"    날짜: {meta['date']}")
        print(f"    통계: {meta['stats'][:5]}")
        if 'headline' in meta:
            print(f"    헤드라인: {meta['headline']}")

result_file = os.path.join(ops_path, "ingest_stage1.json")
with open(result_file, 'w', encoding='utf-8') as f:
    json.dump({
        'vault_path': vault_path,
        'inbox_files': inbox_files,
        'briefing_files': briefing_files,
        'metadata': all_files,
        'timestamp': datetime.now().isoformat()
    }, f, ensure_ascii=False, indent=2)

print(f"\n=== 1 단계 완료: {result_file} ===")
