import os, json, re, subprocess
from datetime import datetime, timedelta
from pathlib import Path
from urllib.parse import quote

# 스크립트 위치 기준 Vault 루트 (로컬 Mac과 GitHub Actions 체크아웃 경로 차이 흡수)
ROOT = Path(__file__).resolve().parents[2]
WEB_DIR = ROOT / "_ops/web"
WIKI = ROOT / "wiki"
REQUIRED_FM = ["title", "created", "updated", "type", "status"]
STALE_DAYS = 42
HISTORY_KEEP = 60
REPO_URL = "https://github.com/foolpoet44/1st_brain"


def issue_url(title, body):
    """GitHub Issue 프리필 링크 — 정적 Pages 에서 가능한 유일한 '쓰기'.
    대시보드 관측을 일감(이슈)으로 발행해 성장 루프(관측→행동→커밋→재관측)를 닫는다."""
    return (f"{REPO_URL}/issues/new?title={quote(title)}"
            f"&body={quote(body)}&labels={quote('knowledge-loop')}")

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


def knowledge_events(days=7, limit=40):
    """최근 N일의 문서 단위 이벤트(A/M/D/R)를 git 이력에서 도출 — append-only 이벤트 원장.
    상태 파일이 필요 없어(stateless) CI 재실행에도 항상 동일하게 재구성된다."""
    try:
        out = subprocess.run(
            ["git", "log", f"--since={days}.days", "--name-status",
             "--format=@%cI|%h|%s", "--", "wiki", "outputs", "projects"],
            cwd=ROOT, capture_output=True, text=True, timeout=60).stdout
    except Exception:
        return []
    events, cur = [], None
    for line in out.splitlines():
        if line.startswith("@"):
            iso, sha, subj = line[1:].split("|", 2)
            cur = {"date": iso[:10], "time": iso[11:16], "sha": sha, "subject": subj}
        elif line.strip() and cur:
            m = re.match(r"^([AMDR])\S*\t(.+)$", line)
            if not m:
                continue
            path = m.group(2).split("\t")[-1]  # R(rename)은 마지막 필드가 새 경로
            if path.endswith(".md") and not path.endswith("_index.md"):
                events.append({**cur, "action": m.group(1), "path": path,
                               "name": Path(path).stem})
        if len(events) >= limit:
            break
    return events


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
    activity_7d = 0
    dated = []
    for d in az.docs.values():
        iso = gitdates.get(d["path"], "")
        ds = days_since(iso)
        if ds is not None and ds <= 7:
            activity_7d += 1
        if iso:
            dated.append((iso, d["path"]))
    # recent_files: 2일 창에 의존하지 않고 '항상 최근 10개'를 git 커밋일 내림차순으로.
    # 조용한 날에도 패널이 비지 않도록(빈 화면=고장처럼 보이는 UX 문제 방지).
    dated.sort(reverse=True)
    recent_files = [{"name": Path(p).name, "time": iso[5:10], "path": p}
                    for iso, p in dated[:10]]

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

    # ── Action Queue (Layer 2: ACT) ─────────────────────────────────────
    # 관측(LINT)을 '다음 행동'으로 변환한다. 각 카드는 Issue 프리필 링크를 가져
    # 클릭 한 번으로 일감이 발행되고, 처리 커밋이 다시 대시보드에 반영된다.
    sr = az.serendipity()
    actions = []
    agent_footer = ("\n\n---\n> CSP-Brain 성장 루프가 발행한 작업입니다. "
                    "Claude Code 세션에서 이 이슈 번호를 지목해 처리하세요.")

    # 1) INGEST — inbox 적체 (대사의 입구가 막히면 루프 전체가 멈춘다)
    # processed: true 로 마킹된 파일은 이미 대사를 마친 것 — 카운트에서 제외해야
    # 처리 커밋 후 카드가 사라지며 루프가 실제로 닫힌다.
    inbox_files = [
        p for p in ((ROOT / "inbox").rglob("*.md") if (ROOT / "inbox").exists() else [])
        if "processed: true" not in p.read_text(encoding="utf-8", errors="ignore")[:500]
    ]
    if inbox_files:
        names = "\n".join(f"- `{p.relative_to(ROOT)}`" for p in inbox_files[:10])
        actions.append({
            "type": "INGEST", "title": f"inbox 대기 {len(inbox_files)}건 편입",
            "detail": "INGEST 프로토콜: 판별 → wiki 병합/생성 → processed 마킹",
            "links": [str(p.relative_to(ROOT)) for p in inbox_files[:3]],
            "issue": issue_url(f"[INGEST] inbox {len(inbox_files)}건 → wiki 편입",
                               f"## Action: INGEST\n대기 파일:\n{names}\n\n"
                               f"할 일: CLAUDE.md Protocol 1 수행 (판별→병합/생성→교차링크→로그){agent_footer}"),
        })

    # 2) CONNECT — 고립 문서 (그래프에서 끊긴 지식은 검색·연상의 사각지대)
    for o in orphans[:2]:
        stem = Path(o["path"]).stem
        actions.append({
            "type": "CONNECT", "title": f"{stem} 고립 해소",
            "detail": "백링크 0 — 인덱스 허브 연결 + 관련 문서 상호 링크",
            "links": [o["path"]],
            "issue": issue_url(f"[CONNECT] {stem} — 고립 문서 연결",
                               f"## Action: CONNECT\n- 대상: `{o['path']}`\n- 상태: inbound 백링크 0\n\n"
                               f"할 일: 해당 섹션 _index.md 에 stem 링크 추가, 주제가 겹치는 문서 2개 이상과 상호 [[링크]]{agent_footer}"),
        })

    # 3) STRUCTURE — 프론트매터 미비 (자동 유입 문서의 표준화)
    if fm_ok < wiki_total:
        actions.append({
            "type": "STRUCTURE", "title": f"프론트매터 미비 {wiki_total - fm_ok}건 정규화",
            "detail": "title/created/updated/type/status 보강 (날짜는 콘텐츠 원본 기준)",
            "links": [],
            "issue": issue_url(f"[STRUCTURE] 프론트매터 정규화 {wiki_total - fm_ok}건",
                               f"## Action: STRUCTURE\n- 현황: {fm_ok}/{wiki_total} 충족\n\n"
                               f"할 일: LINT 프로토콜로 누락 필드 식별 후 정규화 (updated 위조 금지 — 콘텐츠 날짜 사용){agent_footer}"),
        })

    # 4) BRIDGE — 세렌디피티 (가장 강한 미연결 고리를 연결 노트로)
    if sr:
        s1, s2 = (Path(l).stem for l in sr["links"])
        actions.append({
            "type": "BRIDGE", "title": f"{s1} ↔ {s2} 연결 노트",
            "detail": sr["reason"][:80] + "…",
            "links": sr["links"],
            "issue": issue_url(f"[BRIDGE] {s1} ↔ {s2} 연결 통찰 작성",
                               f"## Action: BRIDGE\n- {sr['reason']}\n- 파일: `{sr['links'][0]}`, `{sr['links'][1]}`\n\n"
                               f"할 일: 두 문서를 잇는 통찰을 각 문서 Timeline 에 추가하고 상호 [[링크]] 연결{agent_footer}"),
        })

    # 5) REVIEW — 복습 큐: 오래됐고(정체일수) 중요한(백링크수) 문서 우선.
    #    간격 반복(spaced repetition)의 지식 버전 — 정체는 부채가 아니라 복습 스케줄이다.
    scored = []
    for s, d in az.docs.items():
        ds = days_since(d["updated"])
        if ds is not None and ds >= STALE_DAYS:
            inb = len(az.inbound[s])
            scored.append((ds * (1 + inb), ds, inb, s, d["path"]))
    scored.sort(key=lambda x: (-x[0], x[3]))
    for _, ds, inb, s, p in scored[:4]:
        actions.append({
            "type": "REVIEW", "title": f"{s} 재소화",
            "detail": f"{ds}일 미갱신 · 백링크 {inb}개 — Compiled Truth 재방문",
            "links": [p],
            "issue": issue_url(f"[REVIEW] {s} — Compiled Truth 재방문 ({ds}일 경과)",
                               f"## Action: REVIEW (복습 큐)\n- 대상: `{p}`\n- 사유: {ds}일 미갱신, 백링크 {inb}개(중요도 높음)\n\n"
                               f"할 일: 최근 신호·개념과 대조해 Compiled Truth 갱신, Timeline 에 재방문 기록, updated 갱신{agent_footer}"),
        })

    # ── ARCHIVE 대기열 (Layer 3): mature 승격 문서 = Notion BRIDGE 후보 ──
    archive_queue = [
        {"name": s, "path": d["path"], "title": d["fm"].get("title", s)}
        for s, d in sorted(az.docs.items())
        if d["fm"].get("status", "").lower() == "mature"
    ]

    # ── 대사 지표 (Layer 3): 루프가 실제로 도는지 측정 ──
    # 문서 수가 아니라 '흐름'을 잰다: 입구 적체(inbox), 소화 속도(7d), 평균 신선도(중위 나이)
    inbox_dates = git_last_commit_dates("inbox")
    inbox_ages = [days_since(v) for v in inbox_dates.values() if days_since(v) is not None]
    ages = sorted(a for a in (days_since(d["updated"]) for d in az.docs.values()) if a is not None)
    metabolism = {
        "inbox_pending": len(inbox_files),
        "inbox_oldest_days": max(inbox_ages) if inbox_ages else 0,
        "median_age_days": ages[len(ages) // 2] if ages else 0,
        "updated_7d": activity_7d,
    }

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
        "serendipity": sr,
        "actions": actions,
        "events": knowledge_events(),
        "archive_queue": archive_queue,
        "metabolism": metabolism,
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
