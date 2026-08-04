#!/usr/bin/env python3
"""
CSP-Brain 커맨드센터 — 위키 진화 관제탑

왜 8 번째 대시보드를 만들지 않는가
----------------------------------
2026-08-04 조사 결과, 이 Vault 에는 대시보드 생성 스크립트 7 개와 산출물 6 개가
난립하고 있었다. 파일 수정 시각만 보면 절반이 죽은 것처럼 보였다.

그런데 참조를 세어보니 셋은 살아 있었다. manifest.json 은 Understand-Anything 이
54 곳에서 쓰고, knowledge.html 은 GitHub Actions 가 매일 만들며, _ops/web/index.html 은
localhost:8080 서버가 지금도 서빙 중이다. **수정 시각으로 생사를 판단하면 살아 있는
것을 죽인다.** 실제로 멈춘 것은 둘뿐이었다(METABOLISM_SNAPSHOT.html, index_wiki.html).

그래서 이 스크립트는 새 대시보드가 아니라 **통합 대시보드이자 지도**다. 지표를 한곳에
모으고, 어느 화면이 무엇이며 누가 만드는지를 DASHBOARD_MAP 으로 함께 띄운다.
난립의 진짜 비용은 개수가 아니라 '무엇이 무엇인지 모르는 것'이기 때문이다.

무엇을 보여주는가
-----------------
CLAUDE.md 는 "지능은 저장의 양이 아니라 연결의 밀도와 변화의 속도로 증명된다"고 말한다.
따라서 문서 수를 세는 것은 관제가 아니다. 이 대시보드는 여섯 개의 생체 신호를 본다.

  성장   — 문서 수와 성장 단계 (씨앗/새싹/성장/숲)
  대사   — 최근 7 일 위키가 실제로 얼마나 변했는가
  소화   — 들어온 것 대비 편입된 것의 비율 (적체 감지)  ★ 가장 중요
  밀도   — 백링크 총량과 고립 문서
  신선도 — 6 주 이상 갱신되지 않은 문서의 비율
  대사관 — 자동화 파이프라인 9 개의 건강

소화율이 가장 중요한 이유: 2026-07-23 ~ 08-03 사이 브리핑 11 건이 inbox 에 쌓이는 동안
위키는 거의 변하지 않았다. 생산은 자동인데 소화는 수동이었기 때문이다. 문서 수만 보는
대시보드는 이 정체를 영영 보여주지 못한다.

사용
----
  python3 scripts/command_center.py            # JSON + HTML 갱신
  python3 scripts/command_center.py --json     # 지표만 stdout 으로
  python3 scripts/command_center.py --check    # 경보만 출력 (정상이면 무음)
"""

import json
import os
import re
import subprocess
import sys
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
INBOX = ROOT / "inbox"
BRIEFINGS = ROOT / "outputs" / "briefings"
OUT_JSON = ROOT / "_ops" / "command-center.json"
OUT_HTML = ROOT / "command-center.html"
HISTORY = ROOT / "_ops" / "command-center-history.jsonl"
JOBS_JSON = Path.home() / ".hermes/cron/jobs.json"

# 대시보드 지도 — 이 Vault 의 화면이 무엇이고 누가 만드는지.
#
# 2026-08-04 조사에서 "죽은 대시보드 5개"로 보였던 것 중 셋은 살아 있었다.
#   manifest.json      — Understand-Anything 플러그인이 54 곳에서 참조
#   knowledge.html     — gen_knowledge_index.py 가 만들고 GitHub Actions 가 발행
#   _ops/web/index.html — localhost:8080 서버가 실제로 서빙 중
# 파일 수정 시각만 보고 죽었다고 판단하면 살아 있는 것을 죽인다. 참조를 세어야 한다.
#
# 이 지도를 화면에 띄우는 이유: 난립의 진짜 비용은 개수가 아니라 '무엇이 무엇인지
# 모르는 것'이다. 어느 화면이 현재를 보여주는지 알면 멈춘 화면을 현재로 착각하지 않는다.
DASHBOARD_MAP = [
    ("command-center.html", "이 화면 — 위키 진화 관제", "csp-command-center (09:45/23:45)", "live"),
    ("index.html", "GitHub Pages 공개 대시보드", "eval_dashboard.py + Actions", "live"),
    ("knowledge.html", "지식 인덱스", "gen_knowledge_index.py + Actions", "live"),
    ("_ops/web/index.html", "로컬 대시보드 :8080", "update_dashboard.py + server.py", "live"),
    ("METABOLISM_SNAPSHOT.html", "대사 스냅샷 (1.3MB)", "생성 주체 없음 · 06-10 멈춤", "dead"),
    ("index_wiki.html", "위키 인덱스", "생성 주체 없음 · 07-26 멈춤", "dead"),
]
RETIRED_DASHBOARDS = [(n, s) for n, _, s, st in DASHBOARD_MAP if st == "dead"]

# Obsidian vault 이름 = vault 폴더 basename. obsidian:// 딥링크로 문서를 바로 연다.
# 관제 화면에서 문제를 발견했을 때, 그 문서까지 가는 데 클릭이 여러 번 필요하면
# 사람은 '나중에'로 미룬다. 한 번에 편집기 앞에 앉게 하는 것이 목적이다.
VAULT = ROOT.name


def obsidian(rel_path):
    from urllib.parse import quote
    return f"obsidian://open?vault={quote(VAULT)}&file={quote(rel_path)}"


STALE_WEEKS = 6          # CLAUDE.md LINT 규칙: 6 주 이상 미갱신은 점검 대상
MIN_BACKLINKS = 2        # CLAUDE.md: 한 문서에 최소 2 개 백링크
WIKILINK = re.compile(r"\[\[([^\]|#]+)")


def sh(*args, cwd=ROOT):
    """git 호출용. 실패해도 죽지 않고 빈 문자열을 준다 — 관제탑이 관제 대상 때문에
    멈추면 안 된다."""
    try:
        r = subprocess.run(args, cwd=cwd, capture_output=True, text=True, timeout=30)
        return r.stdout.strip() if r.returncode == 0 else ""
    except Exception:
        return ""


# ---------------------------------------------------------------- 성장 / 밀도

def scan_wiki():
    docs, links, missing_fm = {}, Counter(), []
    for p in WIKI.rglob("*.md"):
        if p.name.startswith("_"):        # _index.md 는 허브라 문서 통계에서 제외
            continue
        text = p.read_text(encoding="utf-8", errors="ignore")
        stem = p.stem
        docs[stem] = {
            "path": str(p.relative_to(ROOT)),
            "folder": p.parent.name,
            "mtime": p.stat().st_mtime,
            "outlinks": set(),
        }
        if not text.startswith("---"):
            missing_fm.append(str(p.relative_to(ROOT)))
        for m in WIKILINK.finditer(text):
            target = m.group(1).strip().split("/")[-1].replace(".md", "")
            docs[stem]["outlinks"].add(target)

    # 인바운드 링크 집계 — 고립 판정은 '들어오는 링크'가 아니라 문서가 가진 링크 수로 한다.
    # CLAUDE.md 는 "한 문서에서 최소 2 개 이상의 백링크"를 요구하므로 outlink 기준이 맞다.
    for stem, d in docs.items():
        for t in d["outlinks"]:
            links[t] += 1

    return docs, links, missing_fm


def growth_stage(n):
    if n >= 80:  return "숲", "자기 진화하는 지식 생태계"
    if n >= 40:  return "성장", "교차 도메인 인사이트, 트렌드 추적"
    if n >= 15:  return "새싹", "개념 간 연결 발견, 비교 분석"
    return "씨앗", "개별 개념 정리, 단순 검색"


# ---------------------------------------------------------------- 대사 / 소화

def metabolism():
    """최근 7 일 위키가 실제로 변한 양. 커밋 기준이라 '만들어졌지만 커밋 안 된 것'은
    잡히지 않는다 — 그것이 오히려 정확하다. 커밋되지 않은 지식은 아직 자산이 아니다."""
    changed = sh("git", "log", "--since=7 days ago", "--name-only",
                 "--pretty=format:", "--", "wiki/")
    files = {l for l in changed.splitlines() if l.strip()}
    added = sh("git", "log", "--since=7 days ago", "--diff-filter=A", "--name-only",
               "--pretty=format:", "--", "wiki/")
    new = {l for l in added.splitlines() if l.strip()}
    return {"changed_7d": len(files), "new_7d": len(new),
            "daily_avg": round(len(files) / 7, 1)}


def digestion():
    """소화율 — 들어온 자료 중 위키로 편입된 비율.

    이 지표가 이 대시보드의 심장이다. 브리핑은 매일 3 건씩 자동 생성되지만,
    편입은 최근까지 사람이 수동으로 해야 했다. 그 간극이 11 건 적체로 나타났다."""
    pending, total = [], 0
    for folder in (INBOX, BRIEFINGS):
        if not folder.exists():
            continue
        for p in folder.rglob("*.md"):
            total += 1
            head = p.read_text(encoding="utf-8", errors="ignore")[:600]
            if "processed: true" not in head:
                pending.append({
                    "path": str(p.relative_to(ROOT)),
                    "age_days": round((datetime.now().timestamp() - p.stat().st_mtime) / 86400),
                })
    pending.sort(key=lambda x: -x["age_days"])
    rate = round((total - len(pending)) / total * 100, 1) if total else 100.0
    return {"total": total, "pending": len(pending), "rate": rate,
            "oldest_days": pending[0]["age_days"] if pending else 0,
            "items": pending[:10]}


# ---------------------------------------------------------------- 전체 규모

def vault_scale():
    """Vault 전체 규모와 type 분류율.

    기존 EVAL_STATUS.md 가 담당하던 지표를 흡수했다. wiki 만 보면 이 Vault 의
    5% 만 보는 셈이다 — 전체 2,200 여 문서 중 위키는 100 개 남짓이다.
    나머지는 원자료·산출물·프로젝트 문서이며, 그것들의 type 분류율이
    '검색 가능한 상태인가'를 말해준다."""
    total = typed = 0
    for p in ROOT.rglob("*.md"):
        s = str(p)
        if "/.git/" in s or "/node_modules/" in s or "/Understand-Anything/" in s:
            continue
        total += 1
        head = p.read_text(encoding="utf-8", errors="ignore")[:400]
        if re.search(r"^type:\s*\S", head, re.M):
            typed += 1
    return {"total_md": total, "typed": typed,
            "typed_ratio": round(typed / total * 100, 1) if total else 0}


def recent_changes(n=8):
    """최근 변경된 위키 문서 — KNOWLEDGE_PULSE.md 의 '최근의 지능적 도약'을 흡수."""
    out = sh("git", "log", "-40", "--pretty=format:%ad|%h|%s", "--date=format:%m-%d %H:%M",
             "--name-only", "--", "wiki/")
    items, cur = [], None
    for line in out.splitlines():
        if "|" in line and line.count("|") >= 2:
            cur = line.split("|")
        elif line.strip() and cur:
            items.append({"date": cur[0], "file": line.strip().replace("wiki/", "")})
            if len(items) >= n:
                break
    return items


def trend(today):
    """전일 대비 추이. 절대값보다 방향이 중요하다 — 늘고 있는가 줄고 있는가."""
    prev = None
    if HISTORY.exists():
        for line in HISTORY.read_text(encoding="utf-8").splitlines():
            try:
                r = json.loads(line)
                if r.get("date") != today["date"]:
                    prev = r
            except Exception:
                pass
    if not prev:
        return {}
    d = {}
    for k in ("docs", "digestion_rate", "links", "isolated", "pending"):
        if k in prev and k in today:
            d[k] = round(today[k] - prev[k], 1)
    return d


def save_history(row):
    HISTORY.parent.mkdir(parents=True, exist_ok=True)
    lines = []
    if HISTORY.exists():
        lines = [l for l in HISTORY.read_text(encoding="utf-8").splitlines()
                 if l.strip() and json.loads(l).get("date") != row["date"]]
    lines.append(json.dumps(row, ensure_ascii=False))
    HISTORY.write_text("\n".join(lines[-120:]) + "\n", encoding="utf-8")


# ---------------------------------------------------------------- 파이프라인

def pipeline():
    """자동화 9 개의 건강. 산출물이 나오는 한 죽은 job 은 보이지 않으므로,
    대시보드가 직접 캐물어야 한다."""
    if not JOBS_JSON.exists():
        return {"jobs": [], "error": "jobs.json 없음"}
    try:
        data = json.loads(JOBS_JSON.read_text(encoding="utf-8"))
    except Exception as e:
        return {"jobs": [], "error": f"파싱 실패: {e}"}

    jobs = data if isinstance(data, list) else data.get("jobs", data)
    if isinstance(jobs, dict):
        jobs = list(jobs.values())

    now, out = datetime.now(timezone.utc), []
    for j in jobs:
        if not isinstance(j, dict):
            continue
        last, age_h = j.get("last_run_at"), None
        if last:
            try:
                ts = datetime.fromisoformat(last.replace("Z", "+00:00"))
                if ts.tzinfo is None:
                    ts = ts.replace(tzinfo=timezone.utc)
                age_h = round((now - ts).total_seconds() / 3600, 1)
            except Exception:
                pass
        enabled = bool(j.get("enabled"))
        status = j.get("last_status") or "-"
        state = "ok"
        if not enabled:
            state = "paused"
        elif status not in ("ok", "-"):
            state = "fail"
        elif age_h is not None and age_h > 26:
            state = "stale"
        out.append({
            "name": j.get("name") or j.get("id", "?"),
            "schedule": (j.get("schedule") or {}).get("expr", "?"),
            "enabled": enabled, "status": status,
            "age_h": age_h, "state": state,
        })
    out.sort(key=lambda x: x["schedule"])
    return {"jobs": out}


# ---------------------------------------------------------------- 조립

def collect():
    docs, links, missing_fm = scan_wiki()
    n = len(docs)
    stage, stage_desc = growth_stage(n)

    isolated = [s for s, d in docs.items() if len(d["outlinks"]) < MIN_BACKLINKS]
    total_links = sum(len(d["outlinks"]) for d in docs.values())
    # 링크 대상이 실제 문서로 해결되는지 — 깨진 링크는 연결이 아니라 착각이다
    known = set(docs) | {p.stem for p in WIKI.rglob("_index.md")}
    broken = sorted({t for d in docs.values() for t in d["outlinks"] if t not in known})

    cutoff = datetime.now().timestamp() - STALE_WEEKS * 7 * 86400
    stale = sorted(
        ({"name": s, "path": d["path"],
          "weeks": round((datetime.now().timestamp() - d["mtime"]) / 604800)}
         for s, d in docs.items() if d["mtime"] < cutoff),
        key=lambda x: -x["weeks"])

    dig, met, pipe = digestion(), metabolism(), pipeline()

    alerts = []
    if dig["pending"] > 0:
        alerts.append({
            "level": "warn" if dig["pending"] < 5 else "crit",
            "msg": f"미편입 자료 {dig['pending']}건 (최고 {dig['oldest_days']}일 경과) — "
                   f"소화율 {dig['rate']}%",
        })
    if met["changed_7d"] == 0:
        alerts.append({"level": "crit", "msg": "최근 7일 위키 변경 0건 — 대사 정지"})
    if isolated:
        alerts.append({"level": "warn",
                       "msg": f"고립 문서 {len(isolated)}건 (백링크 {MIN_BACKLINKS}개 미만)"})
    if broken:
        alerts.append({"level": "warn", "msg": f"해결되지 않는 링크 {len(broken)}종"})
    if missing_fm:
        alerts.append({"level": "warn", "msg": f"frontmatter 누락 {len(missing_fm)}건"})
    for j in pipe.get("jobs", []):
        if j["state"] == "fail":
            alerts.append({"level": "crit", "msg": f"job 실패: {j['name']} ({j['status']})"})
        elif j["state"] == "stale":
            alerts.append({"level": "crit",
                           "msg": f"job 정체: {j['name']} — {j['age_h']:.0f}시간째 무소식"})
    if len(stale) > n * 0.5:
        alerts.append({"level": "warn",
                       "msg": f"{STALE_WEEKS}주 이상 미갱신 {len(stale)}건 (전체의 "
                              f"{round(len(stale)/n*100)}%)"})

    scale = vault_scale()
    today_row = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "docs": n, "digestion_rate": dig["rate"], "links": total_links,
        "isolated": len(isolated), "pending": dig["pending"],
        "broken": len(broken), "typed_ratio": scale["typed_ratio"],
    }
    delta = trend(today_row)
    save_history(today_row)

    return {
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "scale": scale,
        "recent": recent_changes(),
        "delta": delta,
        "retired": RETIRED_DASHBOARDS,
        "dashboard_map": DASHBOARD_MAP,
        "growth": {
            "docs": n, "stage": stage, "stage_desc": stage_desc,
            "by_folder": dict(Counter(d["folder"] for d in docs.values()).most_common()),
        },
        "metabolism": met,
        "digestion": dig,
        "density": {
            "total_links": total_links,
            "avg_per_doc": round(total_links / n, 1) if n else 0,
            "isolated": len(isolated),
            "isolated_items": [{"name": s, "path": docs[s]["path"]}
                               for s in sorted(isolated)[:10]],
            "broken": len(broken), "broken_items": broken[:10],
            "missing_frontmatter": len(missing_fm),
        },
        "freshness": {
            "stale": len(stale),
            "ratio": round(len(stale) / n * 100, 1) if n else 0,
            "items": stale[:10],
        },
        "pipeline": pipe,
        "alerts": alerts,
        "git": {
            "head": sh("git", "log", "-1", "--pretty=format:%h %s")[:90],
            "uncommitted": len([l for l in sh("git", "status", "--porcelain").splitlines() if l]),
        },
    }


# ---------------------------------------------------------------- 렌더

def render_html(d):
    dl = d.get("delta", {})

    def arrow(key, invert=False):
        """전일 대비 화살표. invert=True 면 감소가 좋은 지표(미편입, 고립 등)."""
        v = dl.get(key)
        if v is None or v == 0:
            return ""
        good = (v < 0) if invert else (v > 0)
        cls = "up" if good else "down"
        sign = "+" if v > 0 else ""
        return f'<span class="delta {cls}">{sign}{v}</span>'

    def card(label, value, sub="", tone="ok", dkey=None, invert=False):
        a = arrow(dkey, invert) if dkey else ""
        return (f'<div class="card {tone}"><div class="lbl">{label}</div>'
                f'<div class="val">{value}{a}</div><div class="sub">{sub}</div></div>')

    dig, met, den, fre = d["digestion"], d["metabolism"], d["density"], d["freshness"]
    dig_tone = "ok" if dig["pending"] == 0 else ("warn" if dig["pending"] < 5 else "crit")
    met_tone = "ok" if met["changed_7d"] > 0 else "crit"

    alerts = "".join(
        f'<li class="{a["level"]}">{a["msg"]}</li>' for a in d["alerts"]
    ) or '<li class="ok">이상 없음 — 모든 지표 정상</li>'

    rows = "".join(
        f'<tr class="{j["state"]}"><td>{j["schedule"]}</td><td>{j["name"]}</td>'
        f'<td>{"●" if j["enabled"] else "○"}</td>'
        f'<td>{("%.0fh" % j["age_h"]) if j["age_h"] is not None else "-"}</td>'
        f'<td>{j["state"]}</td></tr>'
        for j in d["pipeline"].get("jobs", [])
    )

    folders = "".join(
        f'<span class="chip">{k} <b>{v}</b></span>'
        for k, v in d["growth"]["by_folder"].items()
    )

    pending = "".join(
        f'<li><a href="{obsidian(i["path"])}"><code>{i["path"]}</code></a> '
        f'<em>{i["age_days"]}일</em></li>'
        for i in dig["items"]
    ) or "<li>없음</li>"

    isolated_list = "".join(
        f'<li><a href="{obsidian(i["path"])}"><code>{i["name"]}</code></a></li>'
        for i in d["density"]["isolated_items"]
    ) or "<li>없음</li>"

    return f"""<!DOCTYPE html>
<html lang="ko"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta http-equiv="refresh" content="300">
<title>CSP-Brain 커맨드센터</title>
<style>
:root{{--bg:#0b0d10;--fg:#e6e9ef;--dim:#8b93a1;--line:#1e232b;
--ok:#3ddc97;--warn:#ffb454;--crit:#ff5c7a;--acc:#6aa8ff}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--fg);
font:14px/1.6 -apple-system,BlinkMacSystemFont,'Pretendard','Apple SD Gothic Neo',sans-serif}}
.wrap{{max-width:1180px;margin:0 auto;padding:28px 20px 60px}}
h1{{font-size:20px;margin:0 0 4px;letter-spacing:-.3px}}
.meta{{color:var(--dim);font-size:12px;margin-bottom:24px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(168px,1fr));gap:12px;margin-bottom:26px}}
.card{{background:#12151a;border:1px solid var(--line);border-radius:12px;padding:14px 16px}}
.card.warn{{border-color:#4a3a1e}} .card.crit{{border-color:#4a1e2a}}
.lbl{{color:var(--dim);font-size:11px;letter-spacing:.4px;text-transform:uppercase}}
.val{{font-size:26px;font-weight:600;margin:6px 0 2px;letter-spacing:-.5px}}
.card.warn .val{{color:var(--warn)}} .card.crit .val{{color:var(--crit)}}
.card.ok .val{{color:var(--ok)}}
.sub{{color:var(--dim);font-size:11px}}
h2{{font-size:13px;color:var(--dim);text-transform:uppercase;letter-spacing:.6px;
margin:28px 0 10px;font-weight:600}}
.panel{{background:#12151a;border:1px solid var(--line);border-radius:12px;padding:16px 18px}}
ul{{margin:0;padding-left:18px}} li{{margin:3px 0}}
li.ok{{color:var(--ok)}} li.warn{{color:var(--warn)}} li.crit{{color:var(--crit)}}
table{{width:100%;border-collapse:collapse;font-size:13px}}
th,td{{text-align:left;padding:7px 8px;border-bottom:1px solid var(--line)}}
th{{color:var(--dim);font-size:11px;text-transform:uppercase;letter-spacing:.4px}}
tr.fail td,tr.stale td{{color:var(--crit)}} tr.paused td{{color:var(--dim)}}
code{{background:#1a1f27;padding:1px 6px;border-radius:5px;font-size:12px}}
li a{{text-decoration:none}} li a:hover code{{color:var(--acc);background:#1e2530}}
em{{color:var(--warn);font-style:normal;font-size:12px}}
.chip{{display:inline-block;background:#1a1f27;border-radius:20px;padding:3px 11px;
margin:3px 4px 3px 0;font-size:12px;color:var(--dim)}}
.chip b{{color:var(--fg)}}
.quote{{color:var(--dim);font-size:12px;font-style:italic;margin-top:32px;
padding-top:16px;border-top:1px solid var(--line)}}
.delta{{font-size:12px;margin-left:7px;font-weight:500;vertical-align:middle}}
.delta.up{{color:var(--ok)}} .delta.down{{color:var(--crit)}}
.dim{{color:var(--dim)}}
p.dim{{font-size:12px;line-height:1.5}}
</style></head><body><div class="wrap">

<h1>🧠 CSP-Brain 커맨드센터</h1>
<div class="meta">{d['generated_at']} 갱신 · 5분마다 자동 새로고침 ·
HEAD <code>{d['git']['head']}</code> · 미커밋 {d['git']['uncommitted']}건</div>

<div class="grid">
{card("위키 문서", d['growth']['docs'], f"{d['growth']['stage']} 단계 — {d['growth']['stage_desc']}", dkey="docs")}
{card("소화율", f"{dig['rate']}%", f"미편입 {dig['pending']}건 · 최고 {dig['oldest_days']}일", dig_tone, "digestion_rate")}
{card("7일 대사", met['changed_7d'], f"신규 {met['new_7d']} · 일평균 {met['daily_avg']}", met_tone)}
{card("연결 밀도", den['avg_per_doc'], f"총 {den['total_links']}개 링크", "ok", "links")}
{card("고립 문서", den['isolated'], f"백링크 {MIN_BACKLINKS}개 미만",
      "ok" if den['isolated']==0 else "warn", "isolated", invert=True)}
{card("노후 문서", f"{fre['ratio']}%", f"{STALE_WEEKS}주 이상 미갱신 {fre['stale']}건",
      "ok" if fre['ratio']<50 else "warn")}
{card("Vault 전체", f"{d['scale']['total_md']:,}", f"type 분류 {d['scale']['typed_ratio']}%",
      "ok" if d['scale']['typed_ratio']>95 else "warn")}
{card("깨진 링크", den['broken'], "해결되지 않는 링크 종수",
      "ok" if den['broken']==0 else "warn")}
</div>

<h2>경보</h2>
<div class="panel"><ul>{alerts}</ul></div>

<h2>파이프라인</h2>
<div class="panel"><table>
<tr><th>스케줄</th><th>Job</th><th>활성</th><th>최근</th><th>상태</th></tr>
{rows}
</table></div>

<h2>고립 문서 <span class="dim" style="font-weight:400;text-transform:none">— 백링크 2개 미만</span></h2>
<div class="panel"><ul>{isolated_list}</ul></div>

<h2>미편입 대기열</h2>
<div class="panel"><ul>{pending}</ul></div>

<h2>최근 지식 변동</h2>
<div class="panel"><ul>{"".join(f'<li><span class="dim">{r["date"]}</span> <a href="{obsidian("wiki/" + r["file"])}"><code>{r["file"]}</code></a></li>' for r in d.get("recent", [])) or "<li>최근 7일 위키 변경 없음</li>"}</ul></div>

<h2>폴더 분포</h2>
<div class="panel">{folders}</div>

<h2>대시보드 지도</h2>
<div class="panel"><p class="dim" style="margin:0 0 10px">
난립의 진짜 비용은 개수가 아니라 <b>무엇이 무엇인지 모르는 것</b>이다.
어느 화면이 현재를 보여주는지 알면 멈춘 화면을 현재로 착각하지 않는다.</p>
<table>
<tr><th>화면</th><th>역할</th><th>생성 주체</th><th></th></tr>
{"".join(f'<tr class="{"" if st=="live" else "paused"}"><td><code>{n}</code></td>'
         f'<td>{r}</td><td class="dim">{s}</td>'
         f'<td>{"●" if st=="live" else "은퇴"}</td></tr>'
         for n, r, s, st in d.get("dashboard_map", []))}
</table></div>

<div class="quote">
"지능은 저장의 양이 아니라, 연결의 밀도와 변화의 속도로 증명됩니다."<br>
이 대시보드가 멈추면 그것도 신호다 — 갱신 시각이 오늘이 아니면 파이프라인을 의심하라.
</div>
</div></body></html>"""


def main():
    args = sys.argv[1:]
    data = collect()

    if "--json" in args:
        print(json.dumps(data, ensure_ascii=False, indent=2))
        return 0

    if "--check" in args:
        # 워치독과 같은 무음 원칙 — 이상이 있을 때만 말한다
        crit = [a for a in data["alerts"] if a["level"] == "crit"]
        if crit:
            print("🚨 위키 진화 경보")
            for a in crit:
                print(f"  • {a['msg']}")
        return 0

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    OUT_HTML.write_text(render_html(data), encoding="utf-8")

    g, dg = data["growth"], data["digestion"]
    print(f"커맨드센터 갱신: 문서 {g['docs']}개({g['stage']}) · "
          f"소화율 {dg['rate']}% · 경보 {len(data['alerts'])}건")
    print(f"  → {OUT_HTML.relative_to(ROOT)}")
    for a in data["alerts"]:
        print(f"  [{a['level']}] {a['msg']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
