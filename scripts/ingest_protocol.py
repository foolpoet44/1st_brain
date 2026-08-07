#!/usr/bin/env python3
"""
INGEST 프로토콜 — csp-brain Vault 지식 편입
2026-08-06 검증 패턴
"""

import os
import re
from datetime import datetime
from pathlib import Path

# Vault 경로 (사용자 지정)
VAULT_PATH = "/Users/dkmac/csp-brain"

def discover_vault():
    """Vault 경로 발견 (cron 컨텍스트 대응)"""
    if os.path.exists(VAULT_PATH):
        return VAULT_PATH
    
    for base in ["/opt", "/output", "/home", "/root", "/data"]:
        if os.path.exists(base):
            for root, dirs, files in os.walk(base):
                if "_ops" in dirs or "change-log.md" in files or "KNOWLEDGE_PULSE.md" in files:
                    return root
    return None

def ensure_directories(vault_path):
    """필수 디렉토리 구조 확인 및 생성"""
    dirs = ['inbox', 'outputs/briefings', 'wiki/signals', 'wiki/concepts', '_ops']
    for d in dirs:
        full_path = os.path.join(vault_path, d)
        if not os.path.exists(full_path):
            os.makedirs(full_path, exist_ok=True)
            print(f"  {d}/ 생성됨")

def find_unprocessed_files(vault_path):
    """processed: true 가 없는 .md 파일 수집"""
    unprocessed = []
    
    # (a) inbox/
    inbox_path = os.path.join(vault_path, 'inbox')
    if os.path.exists(inbox_path):
        for f in os.listdir(inbox_path):
            if f.endswith('.md'):
                full_path = os.path.join(inbox_path, f)
                with open(full_path, 'r', encoding='utf-8') as file:
                    content = file.read(2000)
                    if 'processed: true' not in content:
                        unprocessed.append({
                            'path': full_path,
                            'source': 'inbox',
                            'filename': f
                        })
    
    # (b) outputs/briefings/ (오늘 날짜 파일만)
    briefings_path = os.path.join(vault_path, 'outputs/briefings')
    today = datetime.now().strftime('%Y-%m-%d')
    if os.path.exists(briefings_path):
        for f in os.listdir(briefings_path):
            if f.endswith('.md') and today in f:
                full_path = os.path.join(briefings_path, f)
                with open(full_path, 'r', encoding='utf-8') as file:
                    content = file.read(2000)
                    if 'processed: true' not in content:
                        unprocessed.append({
                            'path': full_path,
                            'source': 'briefings',
                            'filename': f
                        })
    
    return unprocessed

def extract_metadata(content):
    """Frontmatter 에서 메타데이터 추출"""
    metadata = {}
    
    # Frontmatter 파싱
    frontmatter_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if frontmatter_match:
        frontmatter = frontmatter_match.group(1)
        for line in frontmatter.split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                metadata[key.strip()] = value.strip().strip('"\'')
    
    # 본문에서 핵심 통계 추출 (첫 3000 자)
    body = content[content.find('---', 3) + 3:] if '---' in content[3:] else content
    stats = re.findall(r'(\d+(?:\.\d+)?%|\d+(?:,\d{3})*(?:\.\d+)?)', body[:3000])
    
    return metadata, stats, body[:500]

def search_duplicates(vault_path, stats, title):
    """wiki/signals/ 와 wiki/concepts/ 에서 중복 문서 검색"""
    duplicates = []
    
    for subdir in ['wiki/signals', 'wiki/concepts']:
        full_dir = os.path.join(vault_path, subdir)
        if not os.path.exists(full_dir):
            continue
        
        for f in os.listdir(full_dir):
            if f.endswith('.md'):
                full_path = os.path.join(full_dir, f)
                with open(full_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                
                # 통계 기반 중복 검사
                for stat in stats:
                    if stat in content:
                        duplicates.append({
                            'path': full_path,
                            'reason': f'통계 중복: {stat}',
                            'type': 'stat_match'
                        })
                        break
                
                # 제목 기반 중복 검사
                if title.lower() in content.lower()[:2000]:
                    duplicates.append({
                        'path': full_path,
                        'reason': f'제목 중복: {title}',
                        'type': 'title_match'
                    })
    
    return duplicates

def create_signal_node(vault_path, metadata, content, source_file):
    """새 Signal 노드 생성"""
    slug = metadata.get('date', datetime.now().strftime('%Y-%m-%d')) + '-' + \
           metadata.get('domain', 'unknown').lower().replace(' ', '-') + '-' + \
           re.sub(r'[^a-z0-9]+', '-', metadata.get('title', 'signal')[:30]).strip('-')
    
    filename = f"{slug}.md"
    signal_path = os.path.join(vault_path, 'wiki/signals', filename)
    
    # Frontmatter 구성
    frontmatter = f"""---
type: Signal
title: {metadata.get('title', 'Unknown Signal')}
created: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
status: Active
date: {metadata.get('date', datetime.now().strftime('%Y-%m-%d'))}
source: {metadata.get('source', source_file)}
tags: [{metadata.get('tags', 'ingest')}]
related_to:
  - "[[bp-signal-intelligence]]"
  - "[[hr-conceptual-atoms]]"
---
# {metadata.get('title', 'Unknown Signal')}

## 핵심 신호
{content[:2000]}

## Vault 연결
이 신호는 [[bp-signal-intelligence]] 와 연결됩니다.

## 핵심 통찰
**TODO: 핵심 통찰을 작성하세요.**

## HR 실행 함의
TODO: HR 실행 함의를 작성하세요.

## Human Gate 명세
TODO: Human Gate 을 정의하세요.

## Timeline
- {datetime.now().strftime('%Y-%m-%d')}: 초기 편입 (출처: {source_file})
"""
    
    with open(signal_path, 'w', encoding='utf-8') as f:
        f.write(frontmatter)
    
    return signal_path

def append_to_timeline(vault_path, existing_path, new_content, source_file):
    """기존 문서의 Timeline 에 증분 추가"""
    with open(existing_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '## Timeline' not in content:
        # Timeline 섹션 생성
        content += f"\n\n## Timeline\n- {datetime.now().strftime('%Y-%m-%d')}: 증분 추가 (출처: {source_file})\n"
    else:
        # 기존 Timeline 에 추가
        content = content.replace(
            '## Timeline',
            f"## Timeline\n- {datetime.now().strftime('%Y-%m-%d')}: 증분 추가 (출처: {source_file})"
        )
    
    with open(existing_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return existing_path

def mark_processed(file_path, note):
    """소스 파일에 processed 마킹"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Frontmatter 에 processed 추가
    if '---\n' in content:
        parts = content.split('---\n', 2)
        if len(parts) >= 2:
            frontmatter = parts[1]
            if 'processed: true' not in frontmatter:
                frontmatter += f"\nprocessed: true\nprocessed_date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\nprocessed_note: {note}"
            content = f"---\n{frontmatter}---\n{parts[2] if len(parts) > 2 else ''}"
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def update_index(vault_path, signal_path):
    """wiki/signals/_index.md 업데이트"""
    index_path = os.path.join(vault_path, 'wiki/signals/_index.md')
    
    if not os.path.exists(index_path):
        # 인덱스 생성
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write("# Signal Index\n\n")
    
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 새 링크 추가 (중복 방지)
    signal_name = os.path.basename(signal_path).replace('.md', '')
    if signal_name not in content:
        content += f"- [[{signal_name}]]\n"
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(content)

def update_ingest_log(vault_path, new_count, merge_count, duplicate_count, details):
    """_ops/ingest-log.md 업데이트"""
    log_path = os.path.join(vault_path, '_ops/ingest-log.md')
    
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    entry = f"""
## {timestamp}

- **신규**: {new_count}건
- **병합**: {merge_count}건
- **중복 종결**: {duplicate_count}건

### 상세
{details}
"""
    
    if os.path.exists(log_path):
        with open(log_path, 'r', encoding='utf-8') as f:
            content = f.read()
        content += entry
    else:
        content = f"# INGEST Log\n{entry}"
    
    with open(log_path, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    print("=" * 60)
    print("INGEST 프로토콜 시작")
    print("=" * 60)
    
    # Vault 경로 발견
    vault_path = discover_vault()
    if not vault_path:
        print("ERROR: Vault 경로를 찾을 수 없습니다.")
        return
    
    print(f"Vault 경로: {vault_path}")
    
    # 디렉토리 구조 확인
    ensure_directories(vault_path)
    
    # 1단계 — 수집
    print("\n[1 단계] 미처리 파일 수집 중...")
    unprocessed = find_unprocessed_files(vault_path)
    
    if not unprocessed:
        print("\n편입 대상 없음 — 모든 파일이 처리되었거나 존재하지 않습니다.")
        print("[SILENT]")
        return
    
    print(f"  발견된 파일: {len(unprocessed)}개")
    for f in unprocessed:
        print(f"    - {f['source']}/{f['filename']}")
    
    # 2, 3 단계 — 중복 대조 및 편입
    print("\n[2-3 단계] 중복 대조 및 편입 중...")
    new_count = 0
    merge_count = 0
    duplicate_count = 0
    details = []
    human_judgment_needed = []
    
    for item in unprocessed:
        with open(item['path'], 'r', encoding='utf-8') as f:
            content = f.read()
        
        metadata, stats, preview = extract_metadata(content)
        title = metadata.get('title', item['filename'])
        
        print(f"\n  처리 중: {item['filename']}")
        print(f"    통계: {stats[:5]}")
        
        # 중복 검색
        duplicates = search_duplicates(vault_path, stats, title)
        
        if duplicates:
            # 중복 있음 — 기존 문서에 병합
            existing = duplicates[0]['path']
            print(f"    → 중복 발견: {os.path.basename(existing)}")
            print(f"    이유: {duplicates[0]['reason']}")
            
            # 병합 수행
            append_to_timeline(vault_path, existing, preview, item['filename'])
            merge_count += 1
            details.append(f"병합: {item['filename']} → {os.path.basename(existing)} ({duplicates[0]['reason']})")
            
            # 마킹
            mark_processed(item['path'], f"Merged into {os.path.basename(existing)}")
        else:
            # 신규 노드 생성
            print(f"    → 신규 노드 생성")
            signal_path = create_signal_node(vault_path, metadata, preview, item['filename'])
            update_index(vault_path, signal_path)
            new_count += 1
            details.append(f"신규: {item['filename']} → {os.path.basename(signal_path)}")
            
            # 마킹
            mark_processed(item['path'], f"Created new signal node: {os.path.basename(signal_path)}")
            
            # 사람 판단 필요 항목 체크
            if '개인정보' in content or '생체정보' in content or '감시' in content:
                human_judgment_needed.append({
                    'file': item['filename'],
                    'reason': '개인정보/생체정보/감시 관련 스키마 변경',
                    'content_preview': preview[:200]
                })
            
            if len(stats) == 0:
                human_judgment_needed.append({
                    'file': item['filename'],
                    'reason': '근거가 단일 출처뿐인 주장 (통계 없음)',
                    'content_preview': preview[:200]
                })
    
    # 4, 5 단계 — 기록
    print("\n[4-5 단계] 로그 기록 중...")
    update_ingest_log(vault_path, new_count, merge_count, duplicate_count, '\n'.join(details))
    
    # 최종 보고
    print("\n" + "=" * 60)
    print("INGEST 프로토콜 완료")
    print("=" * 60)
    print(f"\n📊 요약:")
    print(f"  - 신규: {new_count}건")
    print(f"  - 병합: {merge_count}건")
    print(f"  - 중복 종결: {duplicate_count}건")
    
    if human_judgment_needed:
        print(f"\n⚠️  사람 판단 필요 항목: {len(human_judgment_needed)}개")
        for item in human_judgment_needed:
            print(f"  - {item['file']}: {item['reason']}")
    
    print(f"\n📝 상세 로그: _ops/ingest-log.md")
    print(f"🔗 대시보드: http://localhost:8080")

if __name__ == '__main__':
    main()
