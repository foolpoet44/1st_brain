import os, json, re
from datetime import datetime, timedelta
from pathlib import Path

# 스크립트 자신의 위치를 기준으로 Vault 루트를 계산합니다.
# 이렇게 해야 로컬 Mac과 GitHub Actions의 체크아웃 경로가 달라도 같은 코드가 동작합니다.
root = str(Path(__file__).resolve().parents[2])
web_dir = os.path.join(root, "_ops/web")

def count_files(path):
    try: return len([f for f in os.listdir(path) if f.endswith('.md')])
    except: return 0

class BacklinkAnalyzer:
    def __init__(self, root_dir):
        self.root_dir = root_dir
        self.file_map = {} # filename -> rel_path
        self.title_map = {} # title -> rel_path
        self.backlinks = {} # rel_path -> [incoming_rel_paths]
        self.outlinks = {} # rel_path -> [outgoing_rel_paths]

    def scan(self):
        # 1. Build file & title map
        # 분석 대상 폴더를 핵심 지식 영역으로 제한하여 노이즈를 제거합니다.
        TARGET_DIRS = ["wiki", "projects", "outputs", "concepts", "decisions", "signals", "inbox"]

        for r, d, f in os.walk(self.root_dir):
            # 시스템 폴더 및 외부 라이브러리 제외
            if any(x in r for x in ["_ops", ".git", "web", ".obsidian", "node_modules", "harness", "Understand-Anything"]): continue

            # TARGET_DIRS에 포함되거나 루트 레벨에 있는 경우만 스캔
            rel_r = os.path.relpath(r, self.root_dir)
            top_dir = rel_r.split(os.sep)[0] if rel_r != "." else "."

            if top_dir not in TARGET_DIRS and top_dir != ".": continue

            for file in f:
                if file.endswith('.md'):
                    rel_path = os.path.relpath(os.path.join(r, file), self.root_dir)
                    name_no_ext = file[:-3]
                    # _index.md는 제목에서 제외
                    if name_no_ext == "_index": continue

                    if name_no_ext.lower() not in self.file_map: self.file_map[name_no_ext.lower()] = rel_path
                    self.outlinks[rel_path] = []
                    self.backlinks[rel_path] = []

        # 2. Extract links
        link_pattern = re.compile(r"\[\[(.*?)\]\]")
        for rel_path in self.outlinks.keys():
            full_path = os.path.join(self.root_dir, rel_path)
            try:
                with open(full_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    links = link_pattern.findall(content)
                    for link in links:
                        # Handle aliases [[Link|Alias]]
                        target = link.split('|')[0].strip().lower()
                        if target in self.file_map:
                            target_path = self.file_map[target]
                            if target_path != rel_path:
                                self.outlinks[rel_path].append(target_path)
                                if rel_path not in self.backlinks[target_path]:
                                    self.backlinks[target_path].append(rel_path)
            except: continue

    def get_orphans(self):
        orphans = []
        for path, incoming in self.backlinks.items():
            if not incoming:
                # Filter out indexes or very new files if needed
                if not path.endswith('_index.md'):
                    orphans.append({"name": os.path.basename(path), "path": path})
        return orphans

    def get_stale_files(self, days=42):
        stale = []
        cutoff = datetime.now() - timedelta(days=days)
        for path in self.outlinks.keys():
            mtime = datetime.fromtimestamp(os.path.getmtime(os.path.join(self.root_dir, path)))
            if mtime < cutoff:
                stale.append({"name": os.path.basename(path), "path": path, "days": (datetime.now() - mtime).days})
        return stale

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

    analyzer = BacklinkAnalyzer(root)
    analyzer.scan()

    # 분석 및 표시 대상 폴더 제한
    TARGET_DIRS = ["wiki", "projects", "outputs", "inbox"]

    for r, d, f in os.walk(root):
        # 시스템 폴더 및 외부 라이브러리 제외
        if any(x in r for x in ["_ops", ".git", "web", ".obsidian", "node_modules", "harness", "Understand-Anything"]): continue

        rel_r = os.path.relpath(r, root)
        top_dir = rel_r.split(os.sep)[0] if rel_r != "." else "."
        if top_dir not in TARGET_DIRS and top_dir != ".": continue

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

    orphans = analyzer.get_orphans()
    stale = analyzer.get_stale_files()

    # Improved Serendipity Logic: Pick from core knowledge zones
    import random
    core_paths = [p for p in analyzer.outlinks.keys() if any(x in p for x in ["wiki/", "projects/"])]
    wiki_paths = [p for p in core_paths if "wiki/" in p]
    project_paths = [p for p in core_paths if "projects/" in p]

    serendipity = None
    if wiki_paths and project_paths:
        f1 = random.choice(wiki_paths)
        f2 = random.choice(project_paths)
        serendipity = {
            "title": "Soul Bridge: Theory meets Practice",
            "reason": f"이론([[{(os.path.basename(f1)[:-3])}]])과 실전([[{(os.path.basename(f2)[:-3])}]])의 교차점에서 새로운 HR 에이전트 전략을 구상해보세요.",
            "links": [f1, f2]
        }
    elif len(core_paths) > 2:
        # Fallback to random core paths
        f1 = random.choice(core_paths)
        f2 = random.choice(core_paths)
        if os.path.dirname(f1) != os.path.dirname(f2):
            serendipity = {
                "title": "Cross-Domain Synapse",
                "reason": f"[[{os.path.basename(f1)[:-3]}]] 와 [[{os.path.basename(f2)[:-3]}]] 사이의 연결고리를 HR 관점에서 탐구해보세요.",
                "links": [f1, f2]
            }

    return {
        "total_atoms": l2 + l3 + l4,
        "recent_activity": len(recent_files),
        "last_update": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "l2": l2, "l3": l3, "l4": l4, "inbox": inbox,
        "recent_files": sorted(recent_files, key=lambda x: x['time'], reverse=True)[:10],
        "latest_changes": get_latest_changes(),
        "orphans": [o for o in orphans if not any(x in o['path'] for x in ["node_modules", "Understand-Anything"])][:5],
        "stale_count": len([s for s in stale if not any(x in s['path'] for x in ["node_modules", "Understand-Anything"])]),
        "serendipity": serendipity,
        "graph": {
            "nodes": [{"id": p, "label": os.path.basename(p)[:-3], "group": "L2" if "wiki" in p else ("L3" if "projects" in p else "L4")} for p in core_paths[:100]], # Increase limit for core paths
            "edges": [{"from": s, "to": t} for s, targets in analyzer.outlinks.items() for t in targets if s in core_paths[:100] and t in core_paths[:100]]
        }
    }

data = get_recent_data()
os.makedirs(web_dir, exist_ok=True)
with open(os.path.join(web_dir, "data.json"), 'w') as f:
    with open(os.path.join(root, "data.json"), 'w') as fr:
        json.dump(data, fr)
    json.dump(data, f)
