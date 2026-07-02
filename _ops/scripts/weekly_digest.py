"""주간 DIGEST 자동 생성 — Dream Cycle 의 클라우드 자율신경계 버전.

매주 금요일 cron(weekly-digest.yml)이 실행한다. CLAUDE.md Protocol 4(DIGEST)의
뼈대를 사람 손 없이 돌린다: 이번 주 이벤트 → 신규/변경 문서 → health 추세 →
다음 주 추천(Action Queue 상위). 산출물은 outputs/weekly/YYYY-WXX.md 로 커밋되어
그 자체가 다시 SENSE 대상이 된다(루프의 ④ARCHIVE 단계).
"""
import json
from datetime import datetime
from pathlib import Path

# update_dashboard 의 분석기를 재사용 (같은 수치 = 같은 진실)
from update_dashboard import (ROOT, WEB_DIR, WikiAnalyzer, knowledge_events,
                              load_history, days_since, STALE_DAYS)


def build_digest():
    now = datetime.now()
    week_id = now.strftime("%Y-W%W")
    today = now.strftime("%Y-%m-%d")

    az = WikiAnalyzer()
    az.scan()
    events = knowledge_events(days=7, limit=200)
    hist = load_history()

    created = sorted({e["name"] for e in events if e["action"] == "A" and e["path"].startswith("wiki/")})
    updated = sorted({e["name"] for e in events if e["action"] == "M" and e["path"].startswith("wiki/")})
    # 가장 활발한 영역: 이벤트 경로의 2단계 폴더 빈도
    folders = {}
    for e in events:
        parts = e["path"].split("/")
        key = "/".join(parts[:2]) if len(parts) > 1 else parts[0]
        folders[key] = folders.get(key, 0) + 1
    hot = sorted(folders.items(), key=lambda x: -x[1])[:3]

    # health 추세 (이번 주 history)
    week_hist = hist[-7:]
    trend = ""
    if len(week_hist) >= 2:
        dh = week_hist[-1]["health"] - week_hist[0]["health"]
        arrow = "▲" if dh > 0 else ("▼" if dh < 0 else "→")
        trend = (f"health {week_hist[0]['health']} {arrow} {week_hist[-1]['health']}"
                 f" (위키 {week_hist[0]['wiki_total']}→{week_hist[-1]['wiki_total']},"
                 f" 정체 {week_hist[0]['stale']}→{week_hist[-1]['stale']})")
    else:
        cur = week_hist[-1] if week_hist else {}
        trend = f"health {cur.get('health','-')} (추세는 다음 주부터)"

    # 다음 주 추천: 복습 큐 상위 3 (오래됨×중요도)
    scored = []
    for s, d in az.docs.items():
        ds = days_since(d["updated"])
        if ds is not None and ds >= STALE_DAYS:
            scored.append((ds * (1 + len(az.inbound[s])), ds, s))
    scored.sort(key=lambda x: (-x[0], x[2]))
    recs = [f"- [[{s}]] — {ds}일 미갱신, 재소화 우선순위 {i+1}"
            for i, (_, ds, s) in enumerate(scored[:3])]

    lines = [
        "---",
        f"title: 주간 다이제스트 {week_id}",
        f"created: {today}",
        f"updated: {today}",
        "type: project",
        "status: mature",
        "tags: [weekly, digest, auto-generated]",
        "---",
        "",
        f"# 주간 다이제스트 — {week_id}",
        "",
        "> weekly-digest.yml cron 이 자동 생성한 DIGEST 입니다 (Dream Cycle Layer 3).",
        "",
        "## 이번 주 흐름",
        f"- {trend}",
        f"- 이벤트 {len(events)}건 · 신규 위키 {len(created)}건 · 갱신 {len(updated)}건",
        f"- 가장 활발한 영역: " + (", ".join(f"`{k}`({v})" for k, v in hot) if hot else "없음"),
        "",
        "## 새로 태어난 문서",
        *([f"- [[{n}]]" for n in created[:10]] or ["- 없음"]),
        "",
        "## 갱신된 문서",
        *([f"- [[{n}]]" for n in updated[:10]] or ["- 없음"]),
        "",
        "## 다음 주 추천 재소화 (복습 큐)",
        *(recs or ["- 없음 — 모든 문서가 신선합니다"]),
        "",
    ]
    return week_id, "\n".join(lines)


def main():
    week_id, content = build_digest()
    out = ROOT / "outputs/weekly" / f"{week_id}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(content, encoding="utf-8")
    print(f"✅ digest: {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
