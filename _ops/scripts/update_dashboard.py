
import os, json
from datetime import datetime, timedelta

root = "/Users/dkmac/Desktop/@26/dev"
web_dir = os.path.join(root, "_ops/web")

def count_files(path):
    try: return len([f for f in os.listdir(path) if f.endswith('.md')])
    except: return 0

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
                    recent_files.append({"name": file, "time": mtime.strftime("%H:%M")})
    
    l2 = count_files(os.path.join(root, "wiki/concepts"))
    l3 = count_files(os.path.join(root, "projects"))
    l4 = count_files(os.path.join(root, "outputs/analyses"))
    inbox = count_files(os.path.join(root, "inbox"))
    
    return {
        "total_atoms": l2 + l3 + l4,
        "recent_activity": len(recent_files),
        "last_update": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "l2": l2, "l3": l3, "l4": l4, "inbox": inbox,
        "recent_files": sorted(recent_files, key=lambda x: x['time'], reverse=True)[:10]
    }

data = get_recent_data()
with open(os.path.join(web_dir, "data.json"), 'w') as f:
    json.dump(data, f)
