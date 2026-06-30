import os, json, re, subprocess
from datetime import datetime, timedelta
from pathlib import Path

# 스크립트 위치 기준 Vault 루트 (로컬 Mac과 GitHub Actions 체크아웃 경로 차이 흡수)
ROOT = Path(__file__).resolve().parents[2]
WEB_DIR = ROOT / "_ops/web"
WIKI = ROOT / "wiki"
REQUIRED_FM = ["title", "created", "updated", "type", "status"]
STALE_DAYS = 42
HISTORY_KEEP = 60

# ──────────────────────────────────────────────────────────────────────────
# 날짜원(源) 분리 — 이 대시보드의 신뢰성 핵심:
#   • stale(콘텐츠 신선도)  = 프론트매터 `updated`  (정규화·번역 등 비-내용 변경에 오염되지 않음)
#   • recent(저장소 활동)   = git 마지막 커밋 시각  (GitHub Actions 체크아웃은 mtime을 '지금'으로
#                              리셋하므로 os.path.getmtime 은 CI 에서 거짓 → git 시각만 신뢰)
# ──────────────────────────────────────────────────────────────────────────

def git_last_commit_dates(rel_dir="wiki"):
    """wiki/ 파일별 마지막 커밋 ISO 날짜를 git log 한 번으로 수집."""
    try:
        out = subprocess.run(
            ["git", "log", "--name-only", "--format=@%cI", "--", rel_dir],
            cwd=ROOT, capture_output=True, text=True, timeout=60
        ).stdout
    except Exception:
        return {}
    dates, cur = {}, None
    for line in out.splitlines():
        if line.startswith("@"):
            cur = line[1:]
        elif line.strip() and cur:
            if line not in dates:  # git log 최신순 → 첫 등장이 마지막 커밋
                dates[line] = cur
    return dates


def parse_frontmatter(text):
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    fm = {}
    for ln in text[3:end].splitlines():
        m = re.match(r"^([A-Za-z_][\w-]*):(.*)$", ln)
        if m:
            fm[m.group(1).strip()] = m.group(2).strip().strip('"')
    return fm


def days_since(iso):
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})", iso or "")
    if not m:
        return None
    d = datetime(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    return (datetime.now() - d).days


# ── 위키 스코프 LINT 분석 (대시보드와 LINT 프로토콜이 같은 수치를 내도록) ──
class WikiAnalyzer:
    def __init__(self):
        self.docs = {}       # stem -> {path, fm, tags, links, updated}
        self.inbound = {}    # stem -> set(stem)

    def scan(self):
        files = [p for p in WIKI.rglob("*.md")]
        # 1단계: 문서 등록
        for p in files:
            if p.name == "_index.md":
                continue
            text = p.read_text(encoding="utf-8", errors="ignore")
            fm = parse_frontmatter(text)
            tags = re.findall(r"[\[\s\"']([a-zA-Z][\w-]+)", fm.get("tags", ""))
            links = set(l.split("|")[0].split("#")[0].strip()
                        for l in re.findall(r"\[\[([^\]]+)\]\]", text))
            self.docs[p.stem] = {
                "path": str(p.relative_to(ROOT)),
                "fm": fm, "tags": set(tags), "links": links,
                "updated": fm.get("updated", ""),
            }
            self.inbound[p.stem] = set()
        # 2단계: 백링크(인덱스 포함, stem 기준) — 인덱스 허브 링크도 인바운드로 인정
        all_index_text = ""
        for idx in WIKI.rglob("_index.md"):
            all_index_text += idx.read_text(encoding="utf-8", errors="ignore")
        index_links = set(l.split("|")[0].split("#")[0].strip()
                          for l in re.findall(r"\[\[([^\]]+)\]\]", all_index_text))
        for stem, d in self.docs.items():
            for link in d["links"]:
                t = Path(link).stem
                if t in self.inbound and t != stem:
                    self.inbound[t].add(stem)
        for link in index_links:
            t = Path(link).stem
            if t in self.inbound:
                self.inbound[t].add("_index")

    def orphans(self):
        return sorted(
            ({"name": Path(d["path"]).name, "path": d["path"]}
             for s, d in self.docs.items() if not self.inbound[s]),
            key=lambda x: x["path"])

    def stale(self):
        out = []
        for s, d in self.docs.items():
            ds = days_since(d["updated"])
            if ds is not None and ds >= STALE_DAYS:
                out.append({"name": Path(d["path"]).name, "path": d["path"], "days": ds})
        return sorted(out, key=lambda x: -x["days"])

    def frontmatter_ok(self):
        return sum(1 for d in self.docs.values()
                   if all(k in d["fm"] for k in REQUIRED_FM))

    def serendipity(self):
        """결정론적: 태그 공유가 '가장 강한'(공유 태그 수 최다) 미연결·이종폴더 쌍 선택.
        첫 매칭이 아니라 잠재 연결이 가장 강한 쌍을 고르므로 추천 가치가 높다.
        동점은 (stem1, stem2) 사전순으로 안정 정렬 → 매 실행 동일 결과."""
        items = sorted(self.docs.items())
        best = None  # (shared_count, s1, s2, shared_tags, path1, path2)
        for i, (s1, d1) in enumerate(items):
            if not d1["tags"]:
                continue
            links1 = {Path(l).stem for l in d1["links"]}
            for s2, d2 in items[i + 1:]:
                shared = d1["tags"] & d2["tags"]
                if not shared:
                    continue
                if Path(d1["path"]).parent == Path(d2["path"]).parent:
                    continue
                if s2 in links1 or s1 in {Path(l).stem for l in d2["links"]}:
                    continue
                cand = (len(shared), s1, s2, shared, d1["path"], d2["path"])
                # 더 많은 공유 태그 우선; 동점이면 사전순 앞쪽 우선(음수 비교 불가하므로 별도 처리)
                if best is None or cand[0] > best[0]:
                    best = cand
        if not best:
            return None
        _, s1, s2, shared, p1, p2 = best
        tags = ", ".join("#" + t for t in sorted(shared))
        return {
            "title": "Serendipity: 가장 강한 미연결 고리",
            "reason": f"[[{s1}]] 와 [[{s2}]] 는 {tags} 를 공유(공유 태그 {len(shared)}개)하지만 아직 직접 연결되지 않았습니다. 둘을 잇는 통찰이 가장 큰 시너지를 낼 지점입니다.",
            "links": [p1, p2],
        }


def count_md(path):
    try:
        return len([f for f in os.listdir(path) if f.endswith(".md") and f != "_index.md"])
    except Exception:
        return 0


def count_md_recursive(path):
    return sum(1 for p in Path(path).rglob("*.md") if p.name != "_index.md") if Path(path).exists() else 0


def get_latest_changes():
    p = ROOT / "_ops/change-log.md"
    if not p.exists():
        return []
    content = p.read_text(encoding="utf-8").strip()
    if content.startswith("## "):
        content = "|||" + content[3:]
    sections = content.replace("\n## ", "|||").split("|||")
    changes = []
    for sec in sections[1:3]:
        lines = sec.strip().split("\n")
        if not lines:
            continue
        date = lines[0].strip()
        for entry in ("\n".join(lines[1:])).split("### ")[1:]:
            el = entry.strip().split("\n")
            title = el[0].strip()
            what = why = ""
            for ln in el[1:]:
                s = ln.strip()
                if s.startswith("- 무엇이 바뀌었나:"):
                    what = s.split(":", 1)[1].strip()
                elif s.startswith("- 왜 중요한가:"):
                    why = s.split(":", 1)[1].strip()
            changes.append({"date": date, "title": title, "what_changed": what, "why_important": why})
    return changes


def load_history():
    p = WEB_DIR / "history.jsonl"
    if not p.exists():
        return []
    rows = []
    for ln in p.read_text(encoding="utf-8").splitlines():
        ln = ln.strip()
        if ln:
            try:
                rows.append(json.loads(ln))
            except Exception:
                pass
    return rows


def save_history(rows):
    (WEB_DIR / "history.jsonl").write_text(
        "\n".join(json.dumps(r, ensure_ascii=False) for r in rows) + "\n",
        encoding="utf-8")


def build():
    today = datetime.now().strftime("%Y-%m-%d")
    az = WikiAnalyzer()
    az.scan()

    wiki_total = len(az.docs)
    orphans = az.orphans()
    stale = az.stale()
    fm_ok = az.frontmatter_ok()

    # 폴더별 정직한 집계
    by_folder = {}
    for d in az.docs.values():
        folder = Path(d["path"]).parent.name
        by_folder[folder] = by_folder.get(folder, 0) + 1

    # 저장소 활동(git 커밋일) — CI 에서 신뢰 가능
    gitdates = git_last_commit_dates("wiki")
    recent_files = []
    activity_7d = 0
    for d in az.docs.values():
        iso = gitdates.get(d["path"], "")
        ds = days_since(iso)
        if ds is not None and ds <= 7:
            activity_7d += 1
        if ds is not None and ds <= 2:
            recent_files.append({
                "name": Path(d["path"]).name,
                "time": iso[5:10] if iso else "",
                "path": d["path"],
            })
    recent_files = sorted(recent_files, key=lambda x: x["time"], reverse=True)[:10]

    # 분포(C/P/O) — 정직한 카운트
    l2 = count_md_recursive(WIKI / "concepts") + count_md_recursive(WIKI / "frameworks") + count_md_recursive(WIKI / "tools")
    l3 = count_md_recursive(ROOT / "projects")
    l4 = count_md_recursive(ROOT / "outputs")

    # 건강 점수(0~100): 연결성 40% + 신선도 30% + 구조 30%
    connectivity = 1 - (len(orphans) / wiki_total) if wiki_total else 0
    freshness = 1 - (len(stale) / wiki_total) if wiki_total else 0
    structure = (fm_ok / wiki_total) if wiki_total else 0
    health = round(100 * (0.4 * connectivity + 0.3 * freshness + 0.3 * structure))

    # 델타(어제/직전 스냅샷 대비)
    hist = load_history()
    prev = next((r for r in reversed(hist) if r.get("date") != today), None)
    def delta(key, cur):
        return (cur - prev[key]) if prev and key in prev else 0
    deltas = {
        "wiki_total": delta("wiki_total", wiki_total),
        "orphans": delta("orphans", len(orphans)),
        "stale": delta("stale", len(stale)),
        "health": delta("health", health),
    }

    # 오늘 스냅샷을 history 에 1일 1엔트리로 upsert
    snap = {"date": today, "wiki_total": wiki_total, "orphans": len(orphans),
            "stale": len(stale), "frontmatter_ok": fm_ok, "health": health}
    hist = [r for r in hist if r.get("date") != today] + [snap]
    hist = hist[-HISTORY_KEEP:]
    save_history(hist)

    # 그래프(위키 한정)
    stems = list(az.docs.keys())
    def grp(path):
        return "L2" if "/concepts/" in path or "/frameworks/" in path or "/tools/" in path else \
               ("L3" if "projects" in path else "L4")
    nodes = [{"id": d["path"], "label": s, "group": grp(d["path"])}
             for s, d in az.docs.items()]
    pathset = {d["path"] for d in az.docs.values()}
    stem2path = {s: d["path"] for s, d in az.docs.items()}
    edges = []
    for s, d in az.docs.items():
        for link in d["links"]:
            t = Path(link).stem
            if t in stem2path and stem2path[t] != d["path"]:
                edges.append({"from": d["path"], "to": stem2path[t]})

    return {
        # 헤드라인(정직화)
        "total_atoms": wiki_total,
        "recent_activity": activity_7d,
        "last_update": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "l2": l2, "l3": l3, "l4": l4,
        "inbox": count_md_recursive(ROOT / "inbox"),
        "by_folder": by_folder,
        # 변화 가시성(Phase B)
        "health": health,
        "deltas": deltas,
        "history": hist[-14:],
        "lint": {
            "orphans": len(orphans),
            "stale": len(stale),
            "frontmatter_ok": fm_ok,
            "frontmatter_total": wiki_total,
        },
        # 패널 데이터
        "recent_files": recent_files,
        "latest_changes": get_latest_changes(),
        "orphans": orphans,
        "stale_count": len(stale),
        "serendipity": az.serendipity(),
        "graph": {"nodes": nodes, "edges": edges},
    }


if __name__ == "__main__":
    data = build()
    WEB_DIR.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(data, ensure_ascii=False)
    # data.json 을 두 곳에 쓴다:
    #   • 루트 data.json  → GitHub Pages 발행본(루트 index.html 이 fetch). _ops/ 는 Jekyll exclude 이므로 발행은 루트에서.
    #   • _ops/web/data.json → 로컬 server.py 개발용. (history 는 data.json 안에 embed 되므로 브라우저는 data.json 만 필요)
    (WEB_DIR / "data.json").write_text(payload, encoding="utf-8")
    (ROOT / "data.json").write_text(payload, encoding="utf-8")
    print(f"✅ dashboard: wiki={data['total_atoms']} orphans={data['lint']['orphans']} "
          f"stale={data['lint']['stale']} fm_ok={data['lint']['frontmatter_ok']}/{data['lint']['frontmatter_total']} "
          f"health={data['health']} deltas={data['deltas']}")
