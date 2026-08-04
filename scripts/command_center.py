#!/usr/bin/env python3
"""
CSP-Brain 커맨드센터 — 위키 진화 관제탑

왜 8 번째 대시보드를 만들지 않는가
----------------------------------
2026-08-04 조사 결과, 이 Vault 에는 대시보드 생성 스크립트 7 개와 산출물 6 개가
난립하고 절반이 죽어 있었다. knowledge.html 은 6/13, METABOLISM_SNAPSHOT.html(1.3MB)은
6/10, manifest.json 은 5/02 에 멈췄다. 그런데 아무도 몰랐다. 오늘 launchd job 이
142 회 실패한 것을 아무도 모른 것과 같은 구조다.

그래서 이 스크립트는 **새 대시보드가 아니라 통합 대시보드**다. 기존 산출물을 대체하고,
나머지는 은퇴시킨다. 하나만 살아 있으면 그것이 멈췄을 때 바로 보인다.

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
JOBS_JSON = Path.home() / ".hermes/cron/jobs.json"

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

    return {
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "growth": {
            "docs": n, "stage": stage, "stage_desc": stage_desc,
            "by_folder": dict(Counter(d["folder"] for d in docs.values()).most_common()),
        },
        "metabolism": met,
        "digestion": dig,
        "density": {
            "total_links": total_links,
            "avg_per_doc": round(total_links / n, 1) if n else 0,
            "isolated": len(isolated), "isolated_items": sorted(isolated)[:10],
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
    def card(label, value, sub="", tone="ok"):
        return (f'<div class="card {tone}"><div class="lbl">{label}</div>'
                f'<div class="val">{value}</div><div class="sub">{sub}</div></div>')

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
        f'<li><code>{i["path"]}</code> <em>{i["age_days"]}일</em></li>'
        for i in dig["items"]
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
em{{color:var(--warn);font-style:normal;font-size:12px}}
.chip{{display:inline-block;background:#1a1f27;border-radius:20px;padding:3px 11px;
margin:3px 4px 3px 0;font-size:12px;color:var(--dim)}}
.chip b{{color:var(--fg)}}
.quote{{color:var(--dim);font-size:12px;font-style:italic;margin-top:32px;
padding-top:16px;border-top:1px solid var(--line)}}
</style></head><body><div class="wrap">

<h1>🧠 CSP-Brain 커맨드센터</h1>
<div class="meta">{d['generated_at']} 갱신 · 5분마다 자동 새로고침 ·
HEAD <code>{d['git']['head']}</code> · 미커밋 {d['git']['uncommitted']}건</div>

<div class="grid">
{card("위키 문서", d['growth']['docs'], f"{d['growth']['stage']} 단계 — {d['growth']['stage_desc']}")}
{card("소화율", f"{dig['rate']}%", f"미편입 {dig['pending']}건 · 최고 {dig['oldest_days']}일", dig_tone)}
{card("7일 대사", met['changed_7d'], f"신규 {met['new_7d']} · 일평균 {met['daily_avg']}", met_tone)}
{card("연결 밀도", den['avg_per_doc'], f"총 {den['total_links']}개 링크")}
{card("고립 문서", den['isolated'], f"백링크 {MIN_BACKLINKS}개 미만",
      "ok" if den['isolated']==0 else "warn")}
{card("노후 문서", f"{fre['ratio']}%", f"{STALE_WEEKS}주 이상 미갱신 {fre['stale']}건",
      "ok" if fre['ratio']<50 else "warn")}
</div>

<h2>경보</h2>
<div class="panel"><ul>{alerts}</ul></div>

<h2>파이프라인</h2>
<div class="panel"><table>
<tr><th>스케줄</th><th>Job</th><th>활성</th><th>최근</th><th>상태</th></tr>
{rows}
</table></div>

<h2>미편입 대기열</h2>
<div class="panel"><ul>{pending}</ul></div>

<h2>폴더 분포</h2>
<div class="panel">{folders}</div>

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
