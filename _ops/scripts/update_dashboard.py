import os, json
from datetime import datetime, timedelta

root = "/Users/dkmac/Desktop/@26/dev"
web_dir = os.path.join(root, "_ops/web")

def count_files(path):
    try: return len([f for f in os.listdir(path) if f.endswith('.md')])
    except: return 0

def get_latest_changes():
    """
    최상위 change-log.md 마크다운 파일에서 가장 최근 2개 날짜의 이력 항목들을
    구조화된 딕셔너리 리스트로 발라내는 마크다운 파서 함수입니다.
    """
    change_log_path = os.path.join(root, "_ops/change-log.md")
    if not os.path.exists(change_log_path):
        return []
    try:
        with open(change_log_path, 'r', encoding='utf-8') as f:
            content = f.read()
        normalized = content.strip()
        if normalized.startswith("## "):
            normalized = "|||" + normalized[3:]
        normalized = normalized.replace("\n## ", "|||")
        sections = normalized.split("|||")
        
        valid_changes = []
        
        # 최근 2개의 날짜 섹션 분석
        for sec in sections[1:3]:
            lines = sec.strip().split('\n')
            if not lines: continue
            
            date = lines[0].strip()
            sec_content = '\n'.join(lines[1:])
            entries = sec_content.split('### ')
            
            for entry in entries[1:]:
                entry_lines = entry.strip().split('\n')
                if not entry_lines: continue
                
                title = entry_lines[0].strip()
                what_changed = ""
                why_important = ""
                
                for line in entry_lines[1:]:
                    line_str = line.strip()
                    if line_str.startswith('- 무엇이 바뀌었나:'):
                        what_changed = line_str.replace('- 무엇이 바뀌었나:', '').strip()
                    elif line_str.startswith('- 왜 중요한가:'):
                        why_important = line_str.replace('- 왜 중요한가:', '').strip()
                
                valid_changes.append({
                    "date": date,
                    "title": title,
                    "what_changed": what_changed,
                    "why_important": why_important
                })
        return valid_changes
    except Exception as e:
        print(f"Change log parsing error: {e}")
        return []

def get_recent_data():
    cutoff = datetime.now() - timedelta(days=1)
    recent_files = []
    for r, d, f in os.walk(root):
        if "_ops" in r or ".git" in r or "web" in r: continue
        for file in f:
            if file.endswith('.md'):
                path = os.path.join(r, file)
                mtime = datetime.fromtimestamp(os.path.getmtime(path))
                if mtime > cutoff:
                    rel_path = os.path.relpath(path, root)
                    recent_files.append({"name": file, "time": mtime.strftime("%H:%M"), "path": rel_path})
    
    l2 = count_files(os.path.join(root, "wiki/concepts"))
    l3 = count_files(os.path.join(root, "projects"))
    l4 = count_files(os.path.join(root, "outputs/analyses"))
    inbox = count_files(os.path.join(root, "inbox"))
    
    return {
        "total_atoms": l2 + l3 + l4,
        "recent_activity": len(recent_files),
        "last_update": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "l2": l2, "l3": l3, "l4": l4, "inbox": inbox,
        "recent_files": sorted(recent_files, key=lambda x: x['time'], reverse=True)[:10],
        "latest_changes": get_latest_changes()
    }

data = get_recent_data()
with open(os.path.join(web_dir, "data.json"), 'w') as f:
    json.dump(data, f)

