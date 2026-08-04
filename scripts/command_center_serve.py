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
  GET /health    무음 상태 확인용 (200/JSON)
"""

import http.server
import json
import socketserver
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HTML = ROOT / "command-center.html"
GEN = ROOT / "scripts" / "command_center.py"
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
                '<div style="margin-top:20px"><a href="/refresh" '
                'style="color:#6aa8ff;font-size:12px;text-decoration:none">지금 갱신 →</a>'
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
