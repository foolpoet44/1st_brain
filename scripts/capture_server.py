import http.server
import json
import os
import subprocess
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
INBOX_DIR = BASE_DIR / "inbox" / "notes"
SHORT_MEMO_DIR = BASE_DIR / "inbox" / "short_memo"

class CaptureHandler(http.server.BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Origin, Accept')
        self.send_header('Access-Control-Max-Age', '86400')
        self.end_headers()

    def do_GET(self):
        """서버 상태 확인용 안내 페이지 및 CORS 체크"""
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        if self.path == '/health':
            self.wfile.write(json.dumps({"status": "online"}).encode('utf-8'))
            return

        html_content = """
        <html>
            <head>
                <title>CSP-Brain Capture Server</title>
                <style>
                    body { font-family: -apple-system, sans-serif; padding: 40px; background: #f7f3ec; color: #2f2a24; line-height: 1.6; }
                    .card { background: white; padding: 30px; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); max-width: 600px; margin: 0 auto; }
                    h2 { color: #9f3f22; margin-top: 0; }
                    code { background: #eee; padding: 2px 5px; border-radius: 4px; }
                    .status { display: inline-block; padding: 4px 12px; background: #48733f; color: white; border-radius: 999px; font-size: 14px; font-weight: bold; }
                </style>
            </head>
            <body>
                <div class="card">
                    <h2><span class="status">ONLINE</span> CSP-Brain Capture Server</h2>
                    <p>서버가 정상적으로 작동 중입니다.</p>
                    <p>이 서버는 대시보드 인터페이스의 <b>Quick Capture</b> 데이터를 <code>inbox/</code> 폴더에 저장하는 브릿지 역할을 수행합니다.</p>
                    <hr style="border: 0; border-top: 1px solid #eee; margin: 20px 0;">
                    <p><b>연결이 안 되나요?</b></p>
                    <ul style="font-size: 14px;">
                        <li>브라우저 주소창에 <code>http://localhost:8080/</code>를 직접 입력하여 이 페이지가 뜨는지 확인하세요.</li>
                        <li>브라우저 보안 설정에서 로컬 네트워크 접속이 차단되어 있을 수 있습니다.</li>
                    </ul>
                </div>
            </body>
        </html>
        """
        self.wfile.write(html_content.encode('utf-8'))

    def do_POST(self):
        if self.path == '/capture':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            data = json.loads(post_data)

            content = data.get('content', '')
            category = data.get('category', 'thought')
            is_short = data.get('is_short', False)

            if not content:
                self.send_error(400, "Content is required")
                return

            now = datetime.now()

            try:
                if is_short:
                    # Short Memo 처리 (주간 단위 파일 누적)
                    SHORT_MEMO_DIR.mkdir(parents=True, exist_ok=True)
                    year, week, _ = now.isocalendar()
                    filename = f"{year}-W{week:02d}-short_memo.md"
                    file_path = SHORT_MEMO_DIR / filename

                    if not file_path.exists():
                        header = f"# Short Memos - {year} Week {week:02d}\n\n"
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(header)

                    timestamp = now.strftime('%Y-%m-%d %H:%M:%S')
                    entry = f"### [{timestamp}]\n{content}\n\n---\n\n"
                    with open(file_path, 'a', encoding='utf-8') as f:
                        f.write(entry)
                    saved_path = file_path
                else:
                    # 일반 메모 처리 (개별 파일 생성)
                    title = data.get('title', f"Note-{now.strftime('%H%M%S')}")
                    INBOX_DIR.mkdir(parents=True, exist_ok=True)
                    filename = f"{now.strftime('%Y-%m-%d')}-{title.replace(' ', '-')}.md"
                    file_path = INBOX_DIR / filename
                    frontmatter = f"---\ntitle: {title}\ncreated: {now.strftime('%Y-%m-%d %H:%M:%S')}\ntype: {category}\nsource: dashboard-capture\nstatus: seed\n---\n\n"
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(frontmatter + content)
                    saved_path = file_path

                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                response = {"status": "success", "file": str(saved_path.relative_to(BASE_DIR))}
                self.wfile.write(json.dumps(response).encode('utf-8'))

                # 대시보드 자동 갱신 트리거
                try:
                    subprocess.run(["python3", "scripts/generate_change_dashboard.py"], cwd=BASE_DIR)
                except Exception as e:
                    print(f"[CAPTURE SERVER] Dashboard regen failed: {e}")
            except Exception as e:
                self.send_response(500)
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps({"status": "error", "message": str(e)}).encode('utf-8'))

def run_server(port=8080):
    server_address = ('0.0.0.0', port)
    httpd = http.server.HTTPServer(server_address, CaptureHandler)
    print(f"[CAPTURE SERVER] Started at http://0.0.0.0:{port}")
    print(f"[SAVE PATH] {INBOX_DIR}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[CAPTURE SERVER] Stopping...")
        httpd.server_close()

if __name__ == "__main__":
    run_server()
