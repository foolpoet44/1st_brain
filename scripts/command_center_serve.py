#!/usr/bin/env python3
"""
커맨드센터 서버 — http://localhost:8090

왜 별도 서버인가
----------------
8080 은 기존 로컬 대시보드(_ops/web/server.py)가 이미 쓰고 있다. 뺏으면 그쪽이
조용히 죽고, 오늘 하루 종일 본 '조용히 죽은 자동화' 목록이 하나 더 늘어난다.
그래서 8090 을 쓴다.

신선도 보장
-----------
정적 HTML 만 서빙하면 사람은 어제 화면을 오늘로 착각한다. 그래서 요청이 올 때
데이터가 STALE_MIN 분보다 오래됐으면 먼저 다시 계산한다. 전체 스캔은 2,100 여
파일을 훑으므로 매 요청마다 하면 느리다 — 그 사이의 절충이다.

  GET /          최신이면 그대로, 오래됐으면 재계산 후 서빙
  GET /refresh   무조건 재계산 후 / 로 리다이렉트
  GET /knowledge 지식 인덱스 실시간 뷰 (270여 문서, 최신순)
  GET /health    무음 상태 확인용 (200/JSON)

지식 인덱스를 여기 붙인 이유
---------------------------
knowledge.html 은 Jekyll 템플릿이고 실제 데이터는 _data/knowledge.json 이다.
GitHub Pages(https://foolpoet44.github.io/1st_brain/knowledge/)는 main 에 push 된
뒤에야 갱신되므로, 지금 작업 중인 문서는 보이지 않는다. 커밋 전 상태를 보려면
로컬에서 생성기를 돌려야 한다. 그 한 단계를 사람이 매번 기억할 필요는 없다.
"""

import http.server
import json
import socketserver
import subprocess
import sys
import urllib.parse
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HTML = ROOT / "command-center.html"
GEN = ROOT / "scripts" / "command_center.py"
KGEN = ROOT / "_ops" / "scripts" / "gen_knowledge_index.py"
KJSON = ROOT / "_data" / "knowledge.json"
PAGES_URL = "https://foolpoet44.github.io/1st_brain/knowledge/"
PAGES_ROOT = "https://foolpoet44.github.io/1st_brain"

# Obsidian vault 이름 = vault 폴더의 basename. ~/Library/Application Support/obsidian/
# obsidian.json 에 등록된 이름과 일치해야 obsidian:// 스킴이 열린다.
VAULT = ROOT.name


def obsidian_url(rel_path):
    """vault 루트 기준 상대경로를 Obsidian 딥링크로.

    지식 인덱스에서 문서를 '읽는' 것과 '고치는' 것은 다른 행위다. 공개 페이지는
    읽기용이고, 실제로 무언가를 바꾸려면 편집기가 열려야 한다. 한 번의 클릭으로
    바로 그 문서 앞에 앉게 하는 것이 이 링크의 목적이다."""
    return (f"obsidian://open?vault={urllib.parse.quote(VAULT)}"
            f"&file={urllib.parse.quote(rel_path)}")
PORT = 8090
STALE_MIN = 10          # 이보다 오래된 데이터면 요청 시 자동 재계산


def regenerate():
    try:
        subprocess.run([sys.executable, str(GEN)], cwd=ROOT,
                       capture_output=True, timeout=180)
        return True
    except Exception:
        return False


def age_minutes():
    if not HTML.exists():
        return 1e9
    return (time.time() - HTML.stat().st_mtime) / 60


def knowledge_html():
    """지식 인덱스를 즉석 생성해 렌더한다.

    Jekyll 없이 보여주기 위해 _data/knowledge.json 을 직접 읽는다. 원격 Pages 와
    같은 데이터를 쓰되, 이쪽은 커밋 전 상태까지 반영한다는 점이 다르다."""
    try:
        subprocess.run([sys.executable, str(KGEN)], cwd=ROOT,
                       capture_output=True, timeout=120)
    except Exception:
        pass
    if not KJSON.exists():
        return "<h1>지식 인덱스 생성 실패</h1>"

    items = json.loads(KJSON.read_text(encoding="utf-8"))
    if isinstance(items, dict):
        items = items.get("items", [])

    dirs = {}
    for it in items:
        dirs.setdefault(it.get("dir", "기타"), []).append(it)

    chips = "".join(
        f'<button class="chip" data-dir="{d}">{d} <b>{len(v)}</b></button>'
        for d, v in sorted(dirs.items(), key=lambda x: -len(x[1]))
    )
    rows = "".join(
        f'<tr data-dir="{it.get("dir","")}" data-t="{(it.get("title","") + " " + it.get("path","")).lower()}">'
        f'<td class="dt">{it.get("date","")}</td>'
        f'<td><a href="{obsidian_url(it["path"])}" title="Obsidian 에서 열기">'
        f'{it.get("title") or it.get("path")}</a>'
        f'<a class="ext" href="{PAGES_ROOT}{it.get("url","")}" target="_blank"'
        f' title="공개 페이지에서 보기">↗</a></td>'
        f'<td class="dim">{it.get("dir","")}</td></tr>'
        for it in items
    )

    return f"""<!DOCTYPE html><html lang="ko"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>지식 인덱스 — CSP-Brain</title>
<style>
:root{{--bg:#0b0d10;--fg:#e6e9ef;--dim:#8b93a1;--line:#1e232b;--acc:#6aa8ff}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--fg);
font:14px/1.6 -apple-system,BlinkMacSystemFont,'Pretendard','Apple SD Gothic Neo',sans-serif}}
.wrap{{max-width:1100px;margin:0 auto;padding:26px 20px 60px}}
h1{{font-size:19px;margin:0 0 4px}}
.meta{{color:var(--dim);font-size:12px;margin-bottom:18px}}
.meta a{{color:var(--acc);text-decoration:none}}
input{{width:100%;background:#12151a;border:1px solid var(--line);border-radius:9px;
padding:10px 13px;color:var(--fg);font-size:14px;margin-bottom:12px}}
input:focus{{outline:none;border-color:var(--acc)}}
.chips{{margin-bottom:14px}}
.chip{{background:#1a1f27;border:1px solid transparent;border-radius:20px;padding:4px 12px;
margin:3px 5px 3px 0;font-size:12px;color:var(--dim);cursor:pointer;font-family:inherit}}
.chip b{{color:var(--fg)}} .chip.on{{border-color:var(--acc);color:var(--fg)}}
table{{width:100%;border-collapse:collapse;font-size:13px}}
td{{padding:6px 8px;border-bottom:1px solid var(--line);vertical-align:top}}
td a{{color:var(--fg);text-decoration:none}} td a:hover{{color:var(--acc)}}
.dt{{color:var(--dim);white-space:nowrap;font-size:12px;width:88px}}
.dim{{color:var(--dim);font-size:12px;white-space:nowrap}}
tr.hide{{display:none}}
a.ext{{color:var(--dim);font-size:11px;margin-left:8px;opacity:.45;text-decoration:none}}
a.ext:hover{{opacity:1;color:var(--acc)}}
</style></head><body><div class="wrap">
<h1>🧠 지식 인덱스</h1>
<div class="meta">{len(items)}개 문서 · 최신 수정순(git 커밋 기준) · 방금 생성 ·
<a href="/">← 커맨드센터</a> · <a href="{PAGES_URL}" target="_blank">공개 페이지 ↗</a><br>
제목을 클릭하면 <b>Obsidian</b>(vault: {VAULT})에서 열립니다 · ↗ 는 공개 페이지</div>
<input id="q" placeholder="제목·경로 검색…" autofocus>
<div class="chips"><button class="chip on" data-dir="">전체 <b>{len(items)}</b></button>{chips}</div>
<table>{rows}</table>
<script>
const q=document.getElementById('q'),rows=[...document.querySelectorAll('tr')];
let dir='';
function apply(){{const s=q.value.toLowerCase();rows.forEach(r=>{{
  const okD=!dir||r.dataset.dir===dir, okQ=!s||(r.dataset.t||'').includes(s);
  r.classList.toggle('hide',!(okD&&okQ));}});}}
q.addEventListener('input',apply);
document.querySelectorAll('.chip').forEach(c=>c.addEventListener('click',()=>{{
  document.querySelectorAll('.chip').forEach(x=>x.classList.remove('on'));
  c.classList.add('on');dir=c.dataset.dir;apply();}}));
</script>
</div></body></html>"""


class Handler(http.server.BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass  # 접속 로그로 디스크를 채우지 않는다

    def _send(self, code, body, ctype="text/html; charset=utf-8"):
        data = body.encode("utf-8") if isinstance(body, str) else body
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        path = self.path.split("?")[0]

        if path == "/health":
            self._send(200, json.dumps({
                "ok": True, "age_min": round(age_minutes(), 1),
                "html": HTML.exists(),
            }), "application/json")
            return

        if path == "/knowledge":
            self._send(200, knowledge_html())
            return

        if path == "/refresh":
            regenerate()
            self.send_response(302)
            self.send_header("Location", "/")
            self.end_headers()
            return

        if path in ("/", "/index.html", "/command-center.html"):
            if age_minutes() > STALE_MIN:
                regenerate()
            if not HTML.exists():
                self._send(503, "<h1>커맨드센터 생성 실패</h1>"
                                "<p>python3 scripts/command_center.py 를 직접 실행해 보세요.</p>")
                return
            html = HTML.read_text(encoding="utf-8")
            # 갱신 버튼을 주입한다 — 사람이 기다리지 않고 지금 상태를 볼 수 있어야 한다
            html = html.replace(
                "</div></body>",
                '<div style="margin-top:20px;font-size:12px">'
                '<a href="/refresh" style="color:#6aa8ff;text-decoration:none">지금 갱신 →</a>'
                '<span style="color:#8b93a1;margin:0 10px">·</span>'
                '<a href="/knowledge" style="color:#6aa8ff;text-decoration:none">지식 인덱스 →</a>'
                '</div></div></body>')
            self._send(200, html)
            return

        self._send(404, "<h1>404</h1>")


if __name__ == "__main__":
    if age_minutes() > STALE_MIN:
        regenerate()
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:
        print(f"커맨드센터: http://localhost:{PORT}")
        httpd.serve_forever()
