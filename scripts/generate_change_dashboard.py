"""
CSP-Brain 변화 대시보드 생성기.

왜 필요한가:
status.sh는 터미널 브리핑이고, change-log/weekly/briefing은 문서 기록이다.
이 스크립트는 세 흐름을 한 화면에 모아 "오늘 무엇을 봐야 하는가"를
브라우저에서 바로 확인할 수 있는 정적 HTML로 만든다.
"""
from __future__ import annotations

import html
import json
import re
import subprocess
from collections import Counter
from datetime import date
from pathlib import Path


BASE_DIR = Path(__file__).parent.parent
OUTPUT_PATH = BASE_DIR / "outputs" / "briefs" / "change-dashboard.html"


def run_git(args: list[str]) -> str:
    """Git 명령 결과를 가져온다. 실패하면 대시보드를 멈추지 않고 빈 값으로 둔다."""
    try:
        result = subprocess.run(
            ["git", "-c", "core.quotePath=false", *args],
            cwd=BASE_DIR,
            check=True,
            capture_output=True,
            text=True,
        )
        return result.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return ""


def md_files(directory: str) -> list[Path]:
    path = BASE_DIR / directory
    if not path.exists():
        return []
    return sorted(path.rglob("*.md"))


def latest_file(directory: str, pattern: str = "*.md") -> Path | None:
    path = BASE_DIR / directory
    if not path.exists():
        return None
    files = [item for item in path.rglob(pattern) if item.is_file()]
    if not files:
        return None
    return max(files, key=lambda item: item.stat().st_mtime)


def read_text(path: Path | None) -> str:
    if not path or not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="replace")


def strip_frontmatter(text: str) -> str:
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) == 3:
            return parts[2].strip()
    return text.strip()


def first_section_summary(markdown: str) -> str:
    """브리핑 문서에서 첫 설명 문단을 뽑는다."""
    body = strip_frontmatter(markdown)
    lines = []
    for line in body.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or stripped.startswith("-"):
            continue
        lines.append(stripped)
        if len(" ".join(lines)) > 140:
            break
    return " ".join(lines)[:260]


def change_log_entries(limit: int = 4) -> list[dict[str, str]]:
    text = read_text(BASE_DIR / "_ops" / "change-log.md")
    body = strip_frontmatter(text)
    entries = []
    current: dict[str, str] | None = None

    for line in body.splitlines():
        if line.startswith("### "):
            if current:
                entries.append(current)
            current = {"title": line.replace("### ", "", 1).strip(), "body": ""}
            continue
        if current and line.strip().startswith("- "):
            current["body"] += line.strip()[2:] + " "

    if current:
        entries.append(current)
    return entries[-limit:][::-1]


def operational_logs() -> list[dict[str, str]]:
    logs = [
        "_ops/change-log.md",
        "_ops/ingest-log.md",
        "_ops/lint-log.md",
        "_ops/question-log.md",
        "_ops/bridge-log.md",
    ]
    result = []
    for log in logs:
        path = BASE_DIR / log
        text = strip_frontmatter(read_text(path))
        meaningful_lines = [
            line for line in text.splitlines()
            if line.strip() and not line.startswith("#") and not line.startswith("---")
        ]
        status = "기록 있음" if len(meaningful_lines) > 2 else "비어 있음"
        if not path.exists():
            status = "없음"
        result.append({"path": log, "status": status})
    return result


def orphan_candidates(limit: int = 8) -> list[str]:
    candidates = []
    for path in md_files("wiki"):
        if path.name == "_index.md":
            continue
        text = read_text(path)
        if "[[" not in text:
            candidates.append(str(path.relative_to(BASE_DIR)))
        if len(candidates) >= limit:
            break
    return candidates


def weekly_area_counts() -> list[tuple[str, int]]:
    latest_weekly = latest_file("outputs/weekly")
    text = read_text(latest_weekly)
    counts = []
    for line in text.splitlines():
        match = re.match(r"^### (.+?) \((\d+)건\)", line.strip())
        if match:
            counts.append((match.group(1), int(match.group(2))))
    return counts[:8]


def latest_briefing() -> tuple[Path | None, str]:
    path = latest_file("outputs/briefs", "*change-briefing.md")
    return path, first_section_summary(read_text(path))


def status_summary() -> dict[str, object]:
    git_status = run_git(["status", "--short"]).splitlines()
    commits = run_git(["log", "--oneline", "-5"]).splitlines()
    changed = [line for line in git_status if not line.startswith("?? ")]
    untracked = [line for line in git_status if line.startswith("?? ")]

    latest_by_area = []
    for area in ["_ops", "wiki", "projects", "outputs", "weekly", "templates", "scripts"]:
        item = latest_file(area)
        if item:
            latest_by_area.append((area, str(item.relative_to(BASE_DIR))))

    return {
        "git_status": git_status,
        "changed": changed,
        "untracked": untracked,
        "commits": commits,
        "latest_by_area": latest_by_area,
        "wiki_count": len(md_files("wiki")),
        "inbox_count": len(md_files("inbox")),
        "project_count": len(md_files("projects")),
        "output_count": len(md_files("outputs")),
    }


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def obsidian_link(path: str) -> str:
    """Obsidian URI를 생성한다."""
    return f"obsidian://open?vault=@26&file={html.escape(path)}"


def bridge_summary() -> dict[str, str]:
    """_ops/bridge-log.md에서 최신 동기화 상태를 가져온다."""
    text = read_text(BASE_DIR / "_ops" / "bridge-log.md")
    body = strip_frontmatter(text)

    # 마지막 ## 섹션 찾기
    sections = re.split(r"##\s+", body)
    if len(sections) < 2:
        return {"date": "기록 없음", "status": "알 수 없음", "detail": "연동 기록이 없습니다."}

    last_section = sections[-1].strip()
    lines = last_section.splitlines()
    header = lines[0].strip()

    status = "알 수 없음"
    detail = ""
    for line in lines[1:]:
        if line.strip().startswith("- 상태:"):
            status = line.replace("- 상태:", "").strip()
        elif line.strip().startswith("- 이유:"):
            detail = line.replace("- 이유:", "").strip()

    return {"date": header, "status": status, "detail": detail[:100] + "..." if len(detail) > 100 else detail}


def external_signals() -> list[dict[str, str]]:
    """harness/ex_signals.json(있다면)에서 최신 신호를 가져온다."""
    # scripts/ex_signal.py에서 정의한 경로와 맞춘다 (harness/ex_signals.json 또는 scripts/../harness/ex_signals.json)
    path = BASE_DIR / "harness" / "ex_signals.json"
    if not path.exists():
        # 대체 경로 확인
        path = BASE_DIR / "scripts" / "harness" / "ex_signals.json"

    if not path.exists():
        return []

    try:
        import json
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            # 최신 5개만 반환
            return data[-5:][::-1]
    except Exception:
        return []


def recent_short_memos(limit: int = 5) -> list[str]:
    """최신 주간 short_memo 파일에서 마지막 항목들을 가져온다."""
    path = latest_file("inbox/short_memo", "*-short_memo.md")
    if not path:
        return []

    text = read_text(path)
    # ### [YYYY-MM-DD HH:MM:SS] 기준으로 분할
    entries = re.split(r"###\s+\[.*?\]", text)
    # 첫 번째는 헤더이므로 제외
    valid_entries = [e.strip() for e in entries[1:] if e.strip()]
    return [e.split("\n---")[0].strip() for e in valid_entries[-limit:][::-1]]


def render_list(items: list[str], empty: str = "없음", limit: int = 8) -> str:
    if not items:
        return f"<li class='muted'>{esc(empty)}</li>"

    rendered = []
    for item in items[:limit]:
        clean_item = item.strip()
        # 파일 경로인 경우 (M path, ?? path, 또는 그냥 path)
        path_match = re.search(r"(?:M |\?\? |^)([\w\-\./]+)", clean_item)
        if path_match:
            path = path_match.group(1).strip()
            # wiki 폴더 내 파일이나 명백한 md 파일인 경우 링크 추가
            if path.endswith(".md") or "wiki/" in path or "projects/" in path:
                link = obsidian_link(path)
                rendered.append(f"<li><code>{esc(clean_item)}</code> <a href='{link}' class='direct-link'>↗</a></li>")
            else:
                rendered.append(f"<li><code>{esc(clean_item)}</code></li>")
        else:
            rendered.append(f"<li><code>{esc(item)}</code></li>")

    return "\n".join(rendered)


def render_dashboard() -> str:
    data = status_summary()
    logs = operational_logs()
    areas = weekly_area_counts()
    changelog = change_log_entries()
    briefing_path, briefing_summary = latest_briefing()
    orphans = orphan_candidates()
    bridge = bridge_summary()
    signals = external_signals()
    short_memos = recent_short_memos()
    today = date.today().isoformat()

    area_total = sum(count for _, count in areas) or 1
    area_bars = "\n".join(
        f"""
        <div class="bar-row">
          <span>{esc(area)}</span>
          <div class="bar"><i style="width:{min(100, round(count / area_total * 100))}%"></i></div>
          <strong>{count}</strong>
        </div>
        """
        for area, count in areas
    ) or "<p class='muted'>주간 영역 데이터 없음</p>"

    log_cards = "\n".join(
        f"<div class='mini { 'ok' if item['status'] == '기록 있음' else 'warn' }'><span>{esc(item['path'])}</span><strong>{esc(item['status'])}</strong></div>"
        for item in logs
    )

    latest_cards = "\n".join(
        f"<li><span>{esc(area)}</span><code>{esc(path)}</code> <a href='{obsidian_link(path)}' class='direct-link'>↗</a></li>"
        for area, path in data["latest_by_area"]
    )

    # 지식 그래프 데이터 추출 (wiki/ 내 백링크 관계)
    nodes = []
    links = []
    wiki_files = md_files("wiki")
    file_to_id = {str(p.relative_to(BASE_DIR)): i for i, p in enumerate(wiki_files)}

    for i, path in enumerate(wiki_files):
        rel_path = str(path.relative_to(BASE_DIR))
        name = path.stem
        nodes.append({"id": i, "name": name, "path": rel_path})

        text = read_text(path)
        # [[문서명]] 패턴 찾기
        links_in_text = re.findall(r"\[\[(.*?)\]\]", text)
        for target_name in links_in_text:
            # 파일명으로 변환 시도
            target_stem = target_name.split("|")[0].split("#")[0].strip()
            # wiki 내에서 해당 stem을 가진 파일 찾기
            for tp in wiki_files:
                if tp.stem == target_stem:
                    target_rel = str(tp.relative_to(BASE_DIR))
                    if target_rel in file_to_id:
                        links.append({"source": i, "target": file_to_id[target_rel]})
                    break

    graph_data = json.dumps({"nodes": nodes, "links": links})

    changelog_cards = "\n".join(
        f"""
        <article class="timeline-item">
          <h3>{esc(entry['title'])}</h3>
          <p>{esc(entry['body'][:220])}</p>
        </article>
        """
        for entry in changelog
    ) or "<p class='muted'>change-log 기록 없음</p>"

    signal_cards = "\n".join(
        f"""
        <div class="mini {'warn' if float(s.get('score', 100)) < 60 else 'ok'}">
          <span>{esc(s.get('org_unit', 'Unknown'))} · {esc(s.get('issue', 'Signal'))}</span>
          <strong>{esc(s.get('score', '0'))}</strong>
        </div>
        """
        for s in signals
    ) or "<p class='muted'>수집된 외부 신호 없음</p>"

    short_memo_list = "\n".join(
        f"<div class='mini' style='display:block; font-size:13px; margin-bottom:6px;'>{esc(m[:120])}{'...' if len(m) > 120 else ''}</div>"
        for m in short_memos
    ) or "<p class='muted'>최근 단상 없음</p>"

    attention_count = len(data["changed"]) + len(data["untracked"])
    risk_label = "확인 필요" if attention_count else "안정"

    return f"""<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>CSP-Brain Change Dashboard</title>
  <style>
    :root {{
      --bg: #f7f3ec;
      --surface: #fffdf8;
      --surface-2: #efe7da;
      --border: rgba(54, 47, 39, 0.14);
      --text: #2f2a24;
      --text-dim: #71685c;
      --accent: #9f3f22;
      --accent-2: #587246;
      --accent-3: #1f5f6f;
      --warn: #b45309;
      --ok: #48733f;
      --shadow: 0 18px 50px rgba(66, 52, 34, 0.12);
    }}

    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: ui-sans-serif, "Apple SD Gothic Neo", "Malgun Gothic", system-ui, sans-serif;
      color: var(--text);
      background:
        linear-gradient(90deg, rgba(47, 42, 36, 0.035) 1px, transparent 1px),
        linear-gradient(rgba(47, 42, 36, 0.035) 1px, transparent 1px),
        radial-gradient(circle at 12% 8%, rgba(159, 63, 34, 0.12), transparent 30%),
        radial-gradient(circle at 82% 12%, rgba(88, 114, 70, 0.14), transparent 28%),
        var(--bg);
      background-size: 28px 28px, 28px 28px, auto, auto, auto;
    }}

    .shell {{
      width: min(1180px, calc(100vw - 40px));
      margin: 0 auto;
      padding: 34px 0 48px;
    }}

    header {{
      display: grid;
      grid-template-columns: 1.5fr 0.9fr;
      gap: 18px;
      align-items: stretch;
      margin-bottom: 18px;
    }}

    .hero, .card {{
      background: rgba(255, 253, 248, 0.88);
      border: 1px solid var(--border);
      box-shadow: var(--shadow);
      border-radius: 8px;
    }}

    .hero {{
      padding: 30px;
      min-height: 260px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}

    .eyebrow {{
      font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
      color: var(--accent);
      font-size: 12px;
      letter-spacing: 0;
      text-transform: uppercase;
    }}

    h1 {{
      margin: 12px 0;
      font-family: Georgia, "Times New Roman", serif;
      font-size: clamp(36px, 6vw, 68px);
      line-height: 0.95;
      letter-spacing: 0;
    }}

    h2 {{
      margin: 0 0 14px;
      font-size: 18px;
      letter-spacing: 0;
    }}

    h3 {{ margin: 0 0 8px; font-size: 15px; }}
    p {{ color: var(--text-dim); line-height: 1.62; }}
    code {{
      font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
      font-size: 12px;
      background: rgba(47, 42, 36, 0.06);
      padding: 2px 5px;
      border-radius: 4px;
      overflow-wrap: anywhere;
    }}

    .summary {{
      font-size: 17px;
      max-width: 740px;
    }}

    .scorecard {{
      padding: 22px;
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 12px;
    }}

    .metric {{
      padding: 15px;
      background: var(--surface-2);
      border: 1px solid var(--border);
      border-radius: 8px;
    }}

    .metric strong {{
      display: block;
      font-size: 28px;
      margin-top: 6px;
    }}

    .grid {{
      display: grid;
      grid-template-columns: repeat(12, 1fr);
      gap: 18px;
    }}

    .card {{
      padding: 22px;
    }}

    .span-4 {{ grid-column: span 4; }}
    .span-5 {{ grid-column: span 5; }}
    .span-7 {{ grid-column: span 7; }}
    .span-8 {{ grid-column: span 8; }}
    .span-12 {{ grid-column: span 12; }}

    ul {{ margin: 0; padding-left: 18px; }}
    li {{ margin: 8px 0; color: var(--text-dim); }}
    .latest li {{
      display: grid;
      grid-template-columns: 82px 1fr;
      gap: 10px;
      padding: 8px 0;
      border-bottom: 1px solid var(--border);
    }}
    .latest span {{
      color: var(--accent-3);
      font-weight: 700;
    }}

    .mini {{
      display: flex;
      justify-content: space-between;
      gap: 12px;
      align-items: center;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 10px 12px;
      margin-bottom: 8px;
      background: rgba(255, 255, 255, 0.35);
    }}
    .mini strong {{ color: var(--warn); }}
    .mini.ok strong {{ color: var(--ok); }}

    .bar-row {{
      display: grid;
      grid-template-columns: 110px 1fr 52px;
      gap: 10px;
      align-items: center;
      margin: 12px 0;
      color: var(--text-dim);
    }}
    .bar {{
      height: 11px;
      border-radius: 999px;
      background: rgba(47, 42, 36, 0.08);
      overflow: hidden;
    }}
    .bar i {{
      display: block;
      height: 100%;
      background: linear-gradient(90deg, var(--accent), var(--accent-2));
    }}

    .timeline {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 12px;
    }}
    .timeline-item {{
      border-left: 3px solid var(--accent);
      background: rgba(239, 231, 218, 0.55);
      border-radius: 6px;
      padding: 14px;
    }}
    .timeline-item p {{
      margin: 0;
      font-size: 13px;
    }}

    .badge {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 7px 10px;
      border-radius: 999px;
      background: rgba(159, 63, 34, 0.11);
      color: var(--accent);
      font-weight: 700;
    }}

    .direct-link {{
      text-decoration: none;
      font-size: 14px;
      margin-left: 4px;
      opacity: 0.5;
      transition: opacity 0.2s;
    }}
    .direct-link:hover {{ opacity: 1; color: var(--accent); }}

    .bridge-box {{
      background: rgba(47, 42, 36, 0.04);
      border-radius: 8px;
      padding: 12px;
      margin-top: 12px;
      font-size: 13px;
    }}
    .bridge-box strong {{ color: var(--accent-3); }}

    /* Graph Style */
    #knowledge-graph {{
      width: 100%;
      height: 300px;
      background: rgba(255, 255, 255, 0.4);
      border-radius: 12px;
      border: 1px solid var(--border);
      margin-bottom: 24px;
      cursor: grab;
    }}
    .node {{ fill: var(--accent); stroke: #fff; stroke-width: 1.5px; }}
    .link {{ stroke: var(--accent-2); stroke-opacity: 0.4; stroke-width: 1px; }}
    .node-label {{ font-size: 10px; fill: var(--text); pointer-events: none; }}

    /* Capture Interface Styles */
    .capture-panel {{
      margin-bottom: 24px;
      padding: 24px;
      background: rgba(159, 63, 34, 0.03);
      border: 1px dashed var(--accent);
      border-radius: 8px;
    }}
    .capture-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 16px;
    }}
    .capture-tabs {{
      display: flex;
      gap: 12px;
      margin-bottom: 16px;
    }}
    .capture-tab {{
      padding: 6px 16px;
      border-radius: 999px;
      border: 1px solid var(--border);
      background: var(--surface);
      cursor: pointer;
      font-size: 13px;
      transition: all 0.2s;
    }}
    .capture-tab.active {{
      background: var(--accent);
      color: white;
      border-color: var(--accent);
    }}
    .capture-input-group {{
      display: flex;
      flex-direction: column;
      gap: 12px;
    }}
    .capture-title {{
      width: 100%;
      padding: 10px;
      border: 1px solid var(--border);
      border-radius: 4px;
      background: var(--surface);
      font-family: inherit;
      font-size: 14px;
    }}
    .capture-content {{
      width: 100%;
      height: 100px;
      padding: 12px;
      border: 1px solid var(--border);
      border-radius: 4px;
      background: var(--surface);
      font-family: inherit;
      font-size: 14px;
      resize: vertical;
    }}
    .capture-footer {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-top: 12px;
    }}
    .capture-btn {{
      background: var(--accent);
      color: white;
      border: none;
      padding: 8px 24px;
      border-radius: 4px;
      cursor: pointer;
      font-weight: 600;
      transition: opacity 0.2s;
    }}
    .capture-btn:hover {{ opacity: 0.9; }}
    .capture-status {{ font-size: 13px; font-weight: 600; }}

    .muted {{ color: var(--text-dim); }}
    .foot {{
      margin-top: 18px;
      color: var(--text-dim);
      font-size: 13px;
    }}

    @media (max-width: 900px) {{
      header, .grid, .timeline {{
        grid-template-columns: 1fr;
      }}
      .span-4, .span-5, .span-7, .span-8, .span-12 {{
        grid-column: span 1;
      }}
      .scorecard {{
        grid-template-columns: 1fr;
      }}
      .shell {{
        width: min(100vw - 24px, 1180px);
        padding-top: 18px;
      }}
    }}
  </style>
</head>
<body>
  <main class="shell">
    <header>
      <section class="hero">
        <div>
          <div class="eyebrow">CSP-Brain Change Dashboard · {esc(today)}</div>
          <h1>오늘 무엇이 바뀌었나</h1>
          <p class="summary">{esc(briefing_summary or "오늘 브리핑 문서가 아직 없습니다. status와 change-log를 먼저 확인하세요.")}</p>
        </div>
        <div>
          <span class="badge">{esc(risk_label)} · 작업트리 항목 {attention_count}건</span>
        </div>
      </section>

      <aside class="scorecard card">
        <div class="metric"><span>Wiki</span><strong>{data["wiki_count"]}</strong></div>
        <div class="metric"><span>Projects</span><strong>{data["project_count"]}</strong></div>
        <div class="metric"><span>Outputs</span><strong>{data["output_count"]}</strong></div>
        <div class="metric"><span>Inbox</span><strong>{data["inbox_count"]}</strong></div>
      </aside>
    </header>

    <section class="card" style="padding: 20px; margin-bottom: 24px;">
      <h2 style="font-size: 16px; margin-bottom: 12px;">Knowledge Graph (Wiki Connectivity)</h2>
      <div id="knowledge-graph"></div>
    </section>

    <section class="capture-panel">
      <div class="capture-header">
        <h2 style="margin:0;">Quick Capture</h2>
        <span id="cap-location" class="muted" style="font-size:12px;">Saved to <code>inbox/notes/</code></span>
      </div>
      <div class="capture-tabs">
        <div id="tab-note" class="capture-tab active" onclick="setCaptureMode('note')">📝 Note</div>
        <div id="tab-short" class="capture-tab" onclick="setCaptureMode('short')">⚡ Short Memo</div>
      </div>
      <div class="capture-input-group">
        <input type="text" id="cap-title" class="capture-title" placeholder="메모 제목 (선택사항)">
        <textarea id="cap-content" class="capture-content" placeholder="무슨 생각을 하고 계신가요? 내용을 입력하세요."></textarea>
      </div>
      <div class="capture-footer">
        <select id="cap-category" style="padding:6px; border-radius:4px; border:1px solid var(--border); background:var(--surface);">
          <option value="thought">💭 생각</option>
          <option value="clip">📎 클리핑</option>
          <option value="note">📝 메모</option>
          <option value="idea">💡 아이디어</option>
        </select>
        <div>
          <span id="cap-status" class="capture-status"></span>
          <button onclick="captureNote()" class="capture-btn">저장하기</button>
        </div>
      </div>

      <div style="margin-top: 24px; border-top: 1px solid var(--border); padding-top: 20px;">
        <h3 style="margin-top:0; font-size:14px; color:var(--accent);">최근 단상 (Short Memos)</h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 12px; max-height: 400px; overflow-y: auto; padding-top: 10px;">
          {short_memo_list}
        </div>
      </div>
    </section>

    <section class="grid">
      <article class="card span-7">
        <h2>주의할 변화</h2>
        <h3>수정됨</h3>
        <ul>{render_list(data["changed"], "수정된 추적 파일 없음", 8)}</ul>
        <h3 style="margin-top:18px;">미추적</h3>
        <ul>{render_list(data["untracked"], "미추적 파일 없음", 8)}</ul>
      </article>

      <article class="card span-5">
        <h2>운영 로그 건강도</h2>
        {log_cards}

        <div class="bridge-box">
          <strong>Notion Bridge: {esc(bridge['date'])}</strong><br>
          상태: {esc(bridge['status'])}<br>
          <small>{esc(bridge['detail'])}</small>
        </div>
      </article>

      <article class="card span-12" style="background: rgba(31, 95, 111, 0.05);">
        <h2>External Signals & Pulse</h2>
        <div class="timeline" style="grid-template-columns: repeat(4, 1fr);">
          {signal_cards}
        </div>
      </article>

      <article class="card span-5">
        <h2>주간 변경 영역</h2>
        {area_bars}
      </article>

      <article class="card span-7">
        <h2>최근 수정된 핵심 문서</h2>
        <ul class="latest">{latest_cards}</ul>
      </article>

      <article class="card span-12">
        <h2>Change Log 최근 항목</h2>
        <div class="timeline">{changelog_cards}</div>
      </article>

      <article class="card span-4">
        <h2>최근 커밋</h2>
        <ul>{render_list(data["commits"], "커밋 기록 없음", 5)}</ul>
      </article>

      <article class="card span-4">
        <h2>고립 문서 후보</h2>
        <ul>{render_list(orphans, "고립 후보 없음", 8)}</ul>
      </article>

      <article class="card span-4">
        <h2>다음 확인</h2>
        <ul>
          <li><code>dev/</code> 미추적 폴더 정책 결정</li>
          <li>대량 archive 변경과 의미 변경 분리</li>
          <li>비어 있는 운영 로그가 실제 프로토콜 실행 때 채워지는지 확인</li>
        </ul>
      </article>
    </section>

    <p class="foot">
      Source: {esc(str((briefing_path or Path("outputs/briefs")).relative_to(BASE_DIR)) if briefing_path else "no briefing")}
      · Generated by <code>scripts/generate_change_dashboard.py</code>
    </p>
  </main>

  <script src="https://d3js.org/d3.v7.min.js"></script>
  <script>
    // Knowledge Graph Data
    const graphData = {graph_data};

    function initGraph() {{
      const width = document.getElementById('knowledge-graph').clientWidth;
      const height = 300;

      const svg = d3.select("#knowledge-graph")
        .append("svg")
        .attr("width", width)
        .attr("height", height)
        .call(d3.zoom().on("zoom", (event) => {{
          container.attr("transform", event.transform);
        }}));

      const container = svg.append("g");

      const simulation = d3.forceSimulation(graphData.nodes)
        .force("link", d3.forceLink(graphData.links).id(d => d.id).distance(50))
        .force("charge", d3.forceManyBody().strength(-100))
        .force("center", d3.forceCenter(width / 2, height / 2));

      const link = container.append("g")
        .attr("class", "links")
        .selectAll("line")
        .data(graphData.links)
        .enter().append("line")
        .attr("class", "link");

      const node = container.append("g")
        .attr("class", "nodes")
        .selectAll("circle")
        .data(graphData.nodes)
        .enter().append("circle")
        .attr("class", "node")
        .attr("r", 6)
        .on("click", (event, d) => {{
          window.location.href = `obsidian://open?vault=@26&file=${{encodeURIComponent(d.path)}}`;
        }})
        .call(d3.drag()
          .on("start", dragstarted)
          .on("drag", dragged)
          .on("end", dragended));

      node.append("title").text(d => d.name);

      const labels = container.append("g")
        .selectAll("text")
        .data(graphData.nodes)
        .enter().append("text")
        .attr("class", "node-label")
        .attr("dx", 8)
        .attr("dy", ".35em")
        .text(d => d.name);

      simulation.on("tick", () => {{
        link
          .attr("x1", d => d.source.x)
          .attr("y1", d => d.source.y)
          .attr("x2", d => d.target.x)
          .attr("y2", d => d.target.y);

        node
          .attr("cx", d => d.x)
          .attr("cy", d => d.y);

        labels
          .attr("x", d => d.x)
          .attr("y", d => d.y);
      }});

      function dragstarted(event, d) {{
        if (!event.active) simulation.alphaTarget(0.3).restart();
        d.fx = d.x;
        d.fy = d.y;
      }}

      function dragged(event, d) {{
        d.fx = event.x;
        d.fy = event.y;
      }}

      function dragended(event, d) {{
        if (!event.active) simulation.alphaTarget(0);
        d.fx = null;
        d.fy = null;
      }}
    }}

    window.addEventListener('load', initGraph);

    let captureMode = 'note';

    function setCaptureMode(mode) {{
      captureMode = mode;
      const tabNote = document.getElementById('tab-note');
      const tabShort = document.getElementById('tab-short');
      const titleInput = document.getElementById('cap-title');
      const locationLabel = document.getElementById('cap-location');
      const contentArea = document.getElementById('cap-content');

      if (mode === 'note') {{
        tabNote.classList.add('active');
        tabShort.classList.remove('active');
        titleInput.style.display = 'block';
        locationLabel.innerHTML = 'Saved to <code>inbox/notes/</code>';
        contentArea.placeholder = '무슨 생각을 하고 계신가요? 내용을 입력하세요.';
      }} else {{
        tabNote.classList.remove('active');
        tabShort.classList.add('active');
        titleInput.style.display = 'none';
        locationLabel.innerHTML = 'Appended to <code>inbox/short_memo/주간파일.md</code>';
        contentArea.placeholder = '지금 이 순간의 단상을 가볍게 기록하세요...';
      }}
    }}

    async function captureNote() {{
      const title = document.getElementById('cap-title').value;
      const content = document.getElementById('cap-content').value;
      const category = document.getElementById('cap-category').value;
      const statusEl = document.getElementById('cap-status');
      const isShort = (captureMode === 'short');

      if (!content) {{
        statusEl.style.color = 'var(--accent)';
        statusEl.innerText = '내용을 입력해주세요.';
        return;
      }}

      statusEl.style.color = 'var(--text)';
      statusEl.innerText = '저장 중...';

      try {{
        const response = await fetch('http://localhost:8080/capture', {{
          method: 'POST',
          headers: {{ 'Content-Type': 'application/json' }},
          body: JSON.stringify({{
            title,
            content,
            category,
            is_short: isShort
          }})
        }});

        if (response.ok) {{
          const result = await response.json();
          statusEl.style.color = 'var(--ok)';
          const obsLink = `obsidian://open?vault=@26&file=${{encodeURIComponent(result.file)}}`;
          statusEl.innerHTML = `저장 완료! <a href="${{obsLink}}" style="color:var(--accent-3); text-decoration:underline;">[Obsidian에서 열기]</a>`;
          document.getElementById('cap-title').value = '';
          document.getElementById('cap-content').value = '';
          // 5초 후에 상태 메시지 숨기기 (링크 클릭 시간을 고려해 조금 늘림)
          setTimeout(() => {{
            if (statusEl.innerHTML.includes('저장 완료')) statusEl.innerHTML = '';
          }}, 8000);
        }} else {{
          throw new Error('Server error');
        }}
      }} catch (err) {{
        statusEl.style.color = 'var(--accent)';
        statusEl.innerText = '서버 연결 실패 (capture_server.py 실행 확인)';
      }}
    }}
  </script>
</body>
</html>
"""


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(render_dashboard(), encoding="utf-8")
    print(f"[DASHBOARD] 생성 완료: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
