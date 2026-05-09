# Extracted Knowledge from Conv: 97bfdbce-5415-4886-85ca-1bbd56de2f89

**Date**: 2026-01-30T00:44:08.940140Z

### Extracted Code (bash)

```bash
# Sonnet 3.5로 전환 (가장 안정적)
/model claude-3-5-sonnet-20241022

# 현재 모델 확인
/model

# API 상태 확인
claude code doctor
```

### Extracted Code (bash)

```bash
# Claude Code 설정 파일 확인
cat ~/.config/claude-code/config.json

# 또는 직접 설정
claude code config set defaultModel claude-3-5-sonnet-20241022
```

### Extracted Code (bash)

```bash
# Claude Code 재설정
claude code config reset

# API 키 다시 설정
claude code config set apiKey YOUR_API_KEY

# 모델 설정
/model claude-3-5-sonnet-20241022
```

### Extracted Code (text)

```text
claude-3-5-sonnet-20241022  ← 가장 추천 (성능/속도 균형)
claude-3-5-haiku-20241022   ← 빠르고 저렴
claude-3-opus-20240229      ← 가장 강력 (느리고 비쌈)
```

### Extracted Code (bash)

```bash
# macOS/Linux
code ~/.config/claude-code/config.json

# 또는 nano 에디터 사용
nano ~/.config/claude-code/config.json
```

### Extracted Code (bash)

```bash
# 일반적인 위치
~/.config/claude-code/config.json
~/.claude-code/config.json
~/Library/Application Support/claude-code/config.json  # macOS
```

### Extracted Code (bash)

```bash
# 설정 파일 내용 출력
cat ~/.config/claude-code/config.json

# 또는
find ~ -name "config.json" -path "*claude-code*" 2>/dev/null
```

### Extracted Code (bash)

```bash
# config 명령어로 직접 설정
claude code config set model claude-3-5-sonnet-20241022

# 또는
claude code config set defaultModel claude-3-5-sonnet-20241022

# 모든 설정 확인
claude code config list
```

### Extracted Code (bash)

```bash
# 1. 설정 파일 삭제
rm -rf ~/.config/claude-code
rm -rf ~/.claude-code

# 2. Claude Code 재설치 또는 재시작
claude code

# 3. API 키 재설정
claude code config set apiKey YOUR_API_KEY

# 4. 모델 설정
claude code config set defaultModel claude-3-5-sonnet-20241022
```

### Extracted Code (json)

```json
{
  "apiKey": "YOUR_API_KEY_HERE",
  "defaultModel": "claude-3-5-sonnet-20241022",
  "maxTokens": 4096,
  "temperature": 1.0
}
```

### Extracted Code (bash)

```bash
# 1. 현재 설정 확인
claude code config list

# 2. 설정 파일 위치 확인
which claude

# 3. 환경 변수 확인
env | grep CLAUDE

# 4. 버전 확인
claude code --version
```

### Extracted Code (bash)

```bash
# 한 번에 실행
cd ~
echo '{"defaultModel": "claude-3-5-sonnet-20241022"}' > .config/claude-code/config.json
claude code
```

### Extracted Code (powershell)

```powershell
# PowerShell에서 실행
notepad $env:APPDATA\claude-code\config.json

# 또는 직접 경로
notepad C:\Users\YOUR_USERNAME\AppData\Roaming\claude-code\config.json
```

### Extracted Code (powershell)

```powershell
# 설정 파일 내용 확인
Get-Content $env:APPDATA\claude-code\config.json

# 또는 CLI로 설정
claude code config set defaultModel claude-3-5-sonnet-20241022

# 모든 설정 확인
claude code config list
```

### Extracted Code (cmd)

```cmd
type %APPDATA%\claude-code\config.json

claude code config set defaultModel claude-3-5-sonnet-20241022
```

### Extracted Code (powershell)

```powershell
# 1. 설정 디렉토리 삭제
Remove-Item -Recurse -Force $env:APPDATA\claude-code

# 2. Claude Code 재시작
claude code

# 3. API 키 설정
claude code config set apiKey YOUR_API_KEY

# 4. 모델 설정
claude code config set defaultModel claude-3-5-sonnet-20241022
```

### Extracted Code (cmd)

```cmd
rmdir /s /q %APPDATA%\claude-code
claude code
claude code config set apiKey YOUR_API_KEY
claude code config set defaultModel claude-3-5-sonnet-20241022
```

### Extracted Code (json)

```json
{
  "apiKey": "sk-ant-api03-xxxxx",
  "defaultModel": "claude-3-5-sonnet-20241022",
  "maxTokens": 4096,
  "temperature": 1.0
}
```

### Extracted Code (powershell)

```powershell
# 한 번에 실행
$configPath = "$env:APPDATA\claude-code\config.json"
$config = @{
    defaultModel = "claude-3-5-sonnet-20241022"
} | ConvertTo-Json

$config | Out-File -FilePath $configPath -Encoding UTF8

# 확인
Get-Content $configPath
```

### Extracted Code (powershell)

```powershell
# PowerShell에서 실행

# 1. 설정 파일 존재 확인
Test-Path $env:APPDATA\claude-code\config.json

# 2. 설정 파일 내용 확인
Get-Content $env:APPDATA\claude-code\config.json

# 3. Claude Code 버전 확인
claude code --version

# 4. 현재 설정 확인
claude code config list
```

### Extracted Code (powershell)

```powershell
# Claude Code 설정 파일 찾기
Get-ChildItem -Path $env:USERPROFILE -Filter "config.json" -Recurse -ErrorAction SilentlyContinue | Where-Object { $_.FullName -like "*claude*" }

# 또는 직접 확인
dir C:\Users\$env:USERNAME\.claude-code\ -Recurse
dir C:\Users\$env:USERNAME\.config\claude-code\ -Recurse
```

### Extracted Code (text)

```text
C:\Users\[사용자명]\.claude-code\config.json
C:\Users\[사용자명]\.config\claude-code\config.json
C:\Users\[사용자명]\AppData\Local\claude-code\config.json
C:\Users\[사용자명]\AppData\Roaming\claude-code\config.json (←방금 확인한 곳)
```

### Extracted Code (powershell)

```powershell
# Claude Code CLI로 모델 설정
claude code config set model claude-3-5-sonnet-20241022

# 또는
claude code config set defaultModel claude-3-5-sonnet-20241022

# 설정 확인
claude code config list

# 또는
claude code config get model
```

### Extracted Code (powershell)

```powershell
# PowerShell에서 환경 변수 설정
$env:CLAUDE_MODEL = "claude-3-5-sonnet-20241022"

# 영구 설정 (시스템 재시작 후에도 유지)
[System.Environment]::SetEnvironmentVariable("CLAUDE_MODEL", "claude-3-5-sonnet-20241022", "User")
```

### Extracted Code (powershell)

```powershell
# Claude Code가 어디서 실행되는지 확인
where.exe claude

# Claude Code 실행 정보 확인
Get-Command claude | Select-Object Source

# 작업 디렉토리 찾기
cd ~
ls -la | Select-String claude
```

### Extracted Code (powershell)

```powershell
# 현재 프로젝트 디렉토리에 .clauderc 생성
@"
{
  "model": "claude-3-5-sonnet-20241022"
}
"@ | Out-File -FilePath .clauderc -Encoding UTF8

# 확인
Get-Content .clauderc
```

### Extracted Code (powershell)

```powershell
# 실행 시 모델 지정
claude code --model claude-3-5-sonnet-20241022

# 또는 alias 생성
Set-Alias cc 'claude code --model claude-3-5-sonnet-20241022'
```

### Extracted Code (powershell)

```powershell
# 1. Claude Code 버전
claude code --version

# 2. 현재 설정 확인
claude code config list

# 3. 도움말 확인
claude code --help

# 4. 설정 파일 위치 확인
claude code config path
```

### Extracted Code (powershell)

```powershell
# PowerShell에서 실행

# 1. 폴더 생성
New-Item -Path "$env:APPDATA\claude-code" -ItemType Directory -Force

# 2. 설정 파일 생성
@"
{
  "model": "claude-3-5-sonnet-20241022",
  "apiKey": "YOUR_API_KEY_HERE"
}
"@ | Out-File -FilePath "$env:APPDATA\claude-code\config.json" -Encoding UTF8

# 3. 확인
Get-Content "$env:APPDATA\claude-code\config.json"
```

### Extracted Code (powershell)

```powershell
# PowerShell에서 실행 - Claude 관련 모든 설정 파일 찾기
Get-ChildItem -Path C:\Users\$env:USERNAME -Filter "*claude*" -Recurse -Directory -ErrorAction SilentlyContinue | Select-Object FullName

# config.json 파일 찾기
Get-ChildItem -Path C:\Users\$env:USERNAME -Filter "config.json" -Recurse -ErrorAction SilentlyContinue | Where-Object { $_.DirectoryName -like "*claude*" } | Select-Object FullName
```

### Extracted Code (powershell)

```powershell
# 1. 현재 사용 중인 프로그램 확인
where.exe claude

# 2. 버전 확인
claude --version
claude code --version

# 3. 도움말 확인
claude --help
```

### Extracted Code (powershell)

```powershell
# 1. Claude 실행 파일 위치
where.exe claude

# 2. 버전 정보
claude --version

# 3. 현재 디렉토리 구조
Get-ChildItem $env:USERPROFILE\.* -Directory | Select-Object Name

# 4. AppData 내 Claude 관련 폴더
Get-ChildItem $env:APPDATA -Directory | Where-Object { $_.Name -like "*claude*" }

# 5. LocalAppData도 확인
Get-ChildItem $env:LOCALAPPDATA -Directory | Where-Object { $_.Name -like "*claude*" }
```

### Extracted Code (text)

```text
API Error: 404 {"type":"error","error":{"type":"not_found_error","message":"model 'claude-haiku-4-5-20251001' not found"}}
```

### Extracted Code (powershell)

```powershell
# 현재 프로젝트 폴더에 .clauderc 생성
@"
{
  "model": "claude-3-5-sonnet-20241022",
  "defaultModel": "claude-3-5-sonnet-20241022"
}
"@ | Out-File -FilePath .clauderc -Encoding UTF8

# 또는 .claude.json
@"
{
  "model": "claude-3-5-sonnet-20241022"
}
"@ | Out-File -FilePath .claude.json -Encoding UTF8
```

### Extracted Code (powershell)

```powershell
# 모든 정보 한 번에 수집
Write-Host "=== Claude 환경 진단 ===" -ForegroundColor Cyan

Write-Host "`n1. Claude 실행 파일 위치:" -ForegroundColor Yellow
where.exe claude

Write-Host "`n2. 버전 정보:" -ForegroundColor Yellow
try { claude --version } catch { "버전 확인 실패" }

Write-Host "`n3. AppData의 Claude 폴더들:" -ForegroundColor Yellow
Get-ChildItem $env:APPDATA | Where-Object { $_.Name -like "*claude*" } | Select-Object Name

Write-Host "`n4. LocalAppData의 Claude 폴더들:" -ForegroundColor Yellow
Get-ChildItem $env:LOCALAPPDATA | Where-Object { $_.Name -like "*claude*" } | Select-Object Name

Write-Host "`n5. 홈 디렉토리의 숨김 폴더들:" -ForegroundColor Yellow
Get-ChildItem $env:USERPROFILE\.* -Directory | Select-Object Name

Write-Host "`n6. 현재 디렉토리:" -ForegroundColor Yellow
Get-Location
```

### Extracted Code (powershell)

```powershell
# PowerShell에서 실행

# 1. .claude 폴더로 이동
cd C:\Users\Administrator\.claude

# 2. config.json 확인
Get-Content config.json

# 3. 메모장으로 열기
notepad config.json
```

### Extracted Code (powershell)

```powershell
# 모델 설정
claude config set model claude-3-5-sonnet-20241022

# 또는
claude config model claude-3-5-sonnet-20241022

# 설정 확인
claude config get model

# 또는 전체 설정 확인
claude config list
```

### Extracted Code (powershell)

```powershell
# .claude 폴더 내용 확인
Get-ChildItem C:\Users\Administrator\.claude -Recurse

# config.json 내용 확인
Get-Content C:\Users\Administrator\.claude\config.json
```

### Extracted Code (powershell)

```powershell
# 현재 프로젝트 폴더에 설정 생성
@"
{
  "model": "claude-3-5-sonnet-20241022"
}
"@ | Out-File -FilePath .claude-project.json -Encoding UTF8
```

### Extracted Code (powershell)

```powershell
# PowerShell에서 한 번에 실행

# 1. 현재 설정 백업
Copy-Item C:\Users\Administrator\.claude\config.json C:\Users\Administrator\.claude\config.json.backup

# 2. config.json 내용 확인
Write-Host "=== 현재 설정 ===" -ForegroundColor Cyan
Get-Content C:\Users\Administrator\.claude\config.json

# 3. 모델 설정 변경
claude config set model claude-3-5-sonnet-20241022

# 4. 변경 확인
Write-Host "`n=== 변경된 설정 ===" -ForegroundColor Green
claude config get model

# 5. 전체 설정 확인
Write-Host "`n=== 전체 설정 ===" -ForegroundColor Yellow
claude config list
```

### Extracted Code (powershell)

```powershell
# 문제 있는 플러그인 제거
claude plugin uninstall frontend-for-opus-4-5

# 또는 플러그인 캐시 정리
Remove-Item -Recurse -Force C:\Users\Administrator\.claude\plugins\cache\xavierchoi-skills-marketplace\frontend-for-opus-4-5
```

### Extracted Code (text)

```text
claude-3-5-sonnet-20241022  ← 추천 (안정적)
claude-3-5-haiku-20241022   ← 빠름
claude-3-opus-20240229      ← 강력
```

### Extracted Code (powershell)

```powershell
# 1. Claude 세션 종료 (현재 창에서)
# exit 입력 또는 Ctrl+C

# 2. PowerShell에서 설정 변경
claude config set model claude-3-5-sonnet-20241022

# 3. 설정 확인
claude config list

# 4. Claude 다시 시작
claude

# 5. 테스트
# > hello
```

### Extracted Code (powershell)

```powershell
# 모델을 직접 지정해서 시작
claude --model claude-3-5-sonnet-20241022

# 또는
claude -m claude-3-5-sonnet-20241022
```

### Extracted Code (powershell)

```powershell
# PowerShell에서 실행 (Claude 세션 밖에서)

# 1. 모든 Claude 프로세스 종료
Get-Process | Where-Object {$_.ProcessName -like "*claude*"} | Stop-Process -Force

# 2. 설정 변경
claude config set model claude-3-5-sonnet-20241022

# 3. 설정 파일 직접 확인
Get-Content C:\Users\Administrator\.claude\config.json | ConvertFrom-Json | Select-Object model

# 4. Claude 재시작
claude
```

### Extracted Code (text)

```text
❌ 잘못된 방법 (세션 내부):
> /model claude-3-5-sonnet-20241022
> config set model claude-3-5-sonnet-20241022

✅ 올바른 방법 (세션 외부):
C:\> claude config set model claude-3-5-sonnet-20241022
C:\> claude
```
