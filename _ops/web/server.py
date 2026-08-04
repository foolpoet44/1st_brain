
import http.server
import socketserver
import json
import os
import subprocess
import re
from urllib.parse import urlparse, parse_qs

PORT = 8080
ROOT_DIR = "/Users/dkmac/csp-brain"
WEB_DIR = "/Users/dkmac/csp-brain/_ops/web"

class DashboardHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        url_path = urlparse(self.path)
        if url_path.path == '/api/open':
            query = parse_qs(url_path.query)
            file_name = query.get('file', [None])[0]
            if file_name:
                found_path = None
                for r, d, f in os.walk(ROOT_DIR):
                    if file_name in f:
                        found_path = os.path.join(r, file_name)
                        break
                
                if found_path:
                    subprocess.run(["open", found_path])
                    self.send_response(200)
                    self.end_headers()
                    self.wfile.write(b"OK")
                else:
                    self.send_response(404)
                    self.end_headers()
                    self.wfile.write(b"File Not Found")
            return
        
        elif url_path.path == '/api/toggle_checklist':
            query = parse_qs(url_path.query)
            file_name = query.get('file', ['meta-harnessing-review.md'])[0]
            target_idx = int(query.get('index', [-1])[0])
            checked = query.get('checked', ['false'])[0].lower() == 'true'
            
            if file_name and target_idx >= 0:
                checklist_path = os.path.join(ROOT_DIR, "_ops/checklists", file_name)
                if os.path.exists(checklist_path):
                    with open(checklist_path, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                    
                    match_idx = 0
                    modified = False
                    for i, line in enumerate(lines):
                        match = re.match(r'^(\s*-\s*\[)([ xX])(\]\s*.*)', line)
                        if match:
                            if match_idx == target_idx:
                                new_char = 'x' if checked else ' '
                                lines[i] = f"{match.group(1)}{new_char}{match.group(3)}\n"
                                modified = True
                                break
                            match_idx += 1
                    
                    if modified:
                        with open(checklist_path, 'w', encoding='utf-8') as f:
                            f.writelines(lines)
                        
                        # Trigger update
                        subprocess.Popen(["python3", os.path.join(ROOT_DIR, "_ops/scripts/update_dashboard.py")])
                        
                        self.send_response(200)
                        self.end_headers()
                        self.wfile.write(b"OK")
                        return
            
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Invalid Parameters")
            return

        elif url_path.path == '/api/connect':
            query = parse_qs(url_path.query)
            file1 = query.get('file1', [None])[0]
            file2 = query.get('file2', [None])[0]
            
            if file1 and file2:
                path1 = os.path.join(ROOT_DIR, file1)
                path2 = os.path.join(ROOT_DIR, file2)
                
                if os.path.exists(path1) and os.path.exists(path2):
                    title1 = os.path.basename(path1)[:-3]
                    title2 = os.path.basename(path2)[:-3]
                    
                    # add link to path1
                    with open(path1, 'r', encoding='utf-8') as f:
                        content1 = f.read()
                    if f"[[{title2}]]" not in content1:
                        # Append before metadata or at the end
                        with open(path1, 'a', encoding='utf-8') as f:
                            f.write(f"\n\n## Related (Soul Bridge)\n- [[{title2}]]\n")
                            
                    # add link to path2
                    with open(path2, 'r', encoding='utf-8') as f:
                        content2 = f.read()
                    if f"[[{title1}]]" not in content2:
                        with open(path2, 'a', encoding='utf-8') as f:
                            f.write(f"\n\n## Related (Soul Bridge)\n- [[{title1}]]\n")
                            
                    # Trigger update
                    subprocess.Popen(["python3", os.path.join(ROOT_DIR, "_ops/scripts/update_dashboard.py")])
                    
                    self.send_response(200)
                    self.end_headers()
                    self.wfile.write(b"OK")
                    return
            
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Missing files or path mismatch")
            return
        
        # Default behavior: serve static files from WEB_DIR
        os.chdir(WEB_DIR)
        return super().do_GET()

os.chdir(WEB_DIR)
socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("", PORT), DashboardHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
