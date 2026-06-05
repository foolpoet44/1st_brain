---
title: OpenClaw gateway port conflict resolution
date: 2026-04-03
time: 23:58
uuid: aaea33fe-b3d4-4cb6-a857-9d04cbb1d2f6
type: conversation
tags: [archive, conversation]
---

# OpenClaw gateway port conflict resolution

**날짜**: 2026-04-03 23:58

---

## Human (Message 1)

(base) dkmac@MacBook-Air-3 openclaw % ollama launch openclaw                                                       

Launching OpenClaw with deepseek-v3.1:671b-cloud...
│
◇  Doctor warnings ───────────────────────────────────────╮
│                                                         │
│  - State dir migration skipped: target already exists   │
│    (/Users/dkmac/.openclaw). Remove or merge manually.  │
│                                                         │
├─────────────────────────────────────────────────────────╯
2026-04-03T23:55:57.228Z [canvas] host mounted at http://127.0.0.1:18789/__openclaw__/canvas/ (root /Users/dkmac/.openclaw/canvas)
2026-04-03T23:55:57.230Z Gateway failed to start: another gateway instance is already listening on ws://127.0.0.1:18789
If the gateway is supervised, stop it with: openclaw gateway stop
2026-04-03T23:55:57.255Z Port 18789 is already in use.
2026-04-03T23:55:57.255Z - pid 20372 dkmac: moltbot-gateway (127.0.0.1:18789)
2026-04-03T23:55:57.256Z - Another process is listening on this port.
Error: exit status 1

## Claude (Message 2)

이 에러를 분석해보면, 핵심 문제는 하나입니다. **포트 18789가 이미 사용 중**이에요.

에러 메시지를 보면 `pid 20372` 프로세스(`moltbot-gateway`)가 이미 해당 포트를 점유하고 있고, OpenClaw가 두 번째 gateway 인스턴스를 띄우려다 충돌한 거죠.

---

**해결 순서는 이렇습니다.**

먼저 기존 gateway를 정상 종료해 보세요.

```bash
openclaw gateway stop
```

그래도 안 된다면, 직접 프로세스를 죽이는 방법으로 갑니다.

```bash
# pid 확인 (20372로 나왔지만 재확인)
lsof -i :18789

# 해당 pid 종료
kill -9 20372
```

그 다음 state dir 경고도 처리해야 해요. 에러에 나온 것처럼 `/Users/dkmac/.openclaw`가 이미 존재해서 migration이 스킵됐거든요. 이건 두 가지 선택지가 있어요.

```bash
# 옵션 1: 기존 디렉토리 백업 후 제거
mv ~/.openclaw ~/.openclaw_backup
```

```bash
# 옵션 2: 그냥 두고 재실행 (migration 경고는 무시해도 되는 경우가 많음)
```

마지막으로 다시 실행하면 됩니다.

```bash
ollama launch openclaw
```

---

**근본 원인을 추측하자면**, 이전 세션에서 OpenClaw가 정상 종료되지 않고 gateway 프로세스가 백그라운드에 살아남은 것 같아요. Mac 재부팅 없이 계속 작업하셨다면 흔히 발생하는 패턴입니다.

`openclaw gateway stop` 먼저 시도해보시고 결과 알려주시면 추가로 도와드릴게요.

## Human (Message 3)

(base) dkmac@MacBook-Air-3 openclaw % openclaw gateway stop

🦞 OpenClaw 2026.2.1 (ed4529e) — It's not "failing," it's "discovering new ways to configure the same thing wrong."

│
◇  Doctor warnings ──────────────────────────────────────────────────────────────────────────╮
│                                                                                            │
│  - State dir migration skipped: target already exists (/Users/dkmac/.openclaw). Remove or  │
│    merge manually.                                                                         │
│                                                                                            │
├────────────────────────────────────────────────────────────────────────────────────────────╯
Gateway service not loaded.

## Claude (Message 4)

`Gateway service not loaded` — 즉 supervisor가 관리하는 서비스로 등록된 게 아니라, 그냥 고아 프로세스(orphan process)로 떠 있는 거예요.

직접 pid를 잡아서 죽여야 합니다.

```bash
# 포트 점유 프로세스 확인
lsof -i :18789
```

결과에서 PID 컬럼 값을 확인 후:

```bash
kill -9 20372
```

그 다음 바로 재실행:

```bash
ollama launch openclaw
```

---

State dir 경고는 일단 무시하셔도 됩니다. migration 실패지 기능 오류는 아니에요. 포트 충돌만 해결하면 뜰 거예요.

## Human (Message 5)

(base) dkmac@MacBook-Air-3 openclaw % lsof -i :18789
COMMAND     PID  USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
Google     1589 dkmac   39u  IPv4 0xda3f4df7b0b63cd9      0t0  TCP localhost:51840->localhost:18789 (ESTABLISHED)
node      20372 dkmac   15u  IPv4 0x223b1ce329b86921      0t0  TCP localhost:18789 (LISTEN)
node      20372 dkmac   16u  IPv6 0x92992a2b0b3355ee      0t0  TCP localhost:18789 (LISTEN)
node      20372 dkmac   24u  IPv4 0xe8fc6268b93624cb      0t0  TCP localhost:18789->localhost:51840 (ESTABLISHED)
(base) dkmac@MacBook-Air-3 openclaw %

## Claude (Message 6)

흥미로운 상황이네요. `node 20372`가 포트를 점유하고 있는데, **Google 프로세스(pid 1589)가 그 포트에 연결되어 있어요.** Claude in Chrome 같은 브라우저 확장이 이 gateway에 붙어 있는 것 같습니다.

일단 node 프로세스를 종료하세요:

```bash
kill -9 20372
```

그 다음 바로 재실행:

```bash
ollama launch openclaw
```

---

참고로 Google 프로세스(1589)는 건드리지 않아도 됩니다. node가 죽으면 연결이 끊어지면서 자연스럽게 정리돼요. openclaw가 다시 뜨면 Chrome extension도 재연결될 거예요.

## Human (Message 7)

(base) dkmac@MacBook-Air-3 openclaw % ollama launch openclaw

Launching OpenClaw with deepseek-v3.1:671b-cloud...
│
◇  Doctor warnings ───────────────────────────────────────╮
│                                                         │
│  - State dir migration skipped: target already exists   │
│    (/Users/dkmac/.openclaw). Remove or merge manually.  │
│                                                         │
├─────────────────────────────────────────────────────────╯
2026-04-04T00:05:07.619Z [canvas] host mounted at http://127.0.0.1:18789/__openclaw__/canvas/ (root /Users/dkmac/.openclaw/canvas)
2026-04-04T00:05:07.623Z Gateway failed to start: another gateway instance is already listening on ws://127.0.0.1:18789
If the gateway is supervised, stop it with: openclaw gateway stop
2026-04-04T00:05:07.649Z Port 18789 is already in use.
2026-04-04T00:05:07.649Z - pid 20372 dkmac: moltbot-gateway (127.0.0.1:18789)
2026-04-04T00:05:07.650Z - Another process is listening on this port.
Error: exit status 1

## Claude (Message 8)

흥미롭네요. `kill -9 20372`를 했는데 아직도 pid 20372가 살아있다고 나오는 거예요. 좀비 프로세스이거나 새로운 프로세스가 같은 pid를 재사용했을 가능성이 있어요.

실제 상태를 다시 확인해봅시다:

```bash
lsof -i :18789
```

결과 보여주시면 pid가 바뀌었는지 확인할 수 있어요. 만약 여전히 뭔가 붙어있다면:

```bash
# 포트 점유 프로세스 전체 강제 종료
sudo lsof -ti :18789 | xargs kill -9
```

그 다음 포트가 실제로 비었는지 확인:

```bash
lsof -i :18789
# 아무것도 안 나오면 성공
```

그리고 재실행하면 됩니다.

## Human (Message 9)

(base) dkmac@MacBook-Air-3 openclaw % lsof -i :18789
COMMAND   PID  USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
node    20372 dkmac   15u  IPv4 0x223b1ce329b86921      0t0  TCP localhost:18789 (LISTEN)
node    20372 dkmac   16u  IPv6 0x92992a2b0b3355ee      0t0  TCP localhost:18789 (LISTEN)

## Claude (Message 10)

`kill -9`가 먹히지 않았네요. 같은 pid가 그대로예요. 이건 정말 드문 케이스인데, 두 가지 가능성이 있어요 — 프로세스가 kernel level에서 보호되고 있거나, sudo 권한이 필요한 상황입니다.

```bash
sudo kill -9 20372
```

그래도 안 되면:

```bash
sudo lsof -ti :18789 | xargs sudo kill -9
```

확인:

```bash
lsof -i :18789
```

아무것도 안 나오면 바로 재실행하시면 됩니다.

## Human (Message 11)

(base) dkmac@MacBook-Air-3 openclaw % lsof -i :18789    
COMMAND   PID  USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
node    21189 dkmac   15u  IPv4 0x83995965cab0f0e5      0t0  TCP localhost:18789 (LISTEN)
node    21189 dkmac   16u  IPv6 0x2faa6b29401b3318      0t0  TCP localhost:18789 (LISTEN)

## Claude (Message 12)

pid가 20372 → 21189로 바뀌었어요. 즉 **프로세스가 죽으면 자동으로 재시작되는 구조**입니다. 어딘가에 supervisor나 launchd가 이 프로세스를 감시하고 있는 거예요.

Mac launchd에 등록된 서비스인지 확인해봅시다:

```bash
launchctl list | grep -i openclaw
launchctl list | grep -i moltbot
launchctl list | grep -i node
```

결과 보여주시면 정확히 어떤 서비스가 이걸 살려두는지 찾을 수 있어요. 그걸 unload해야 근본적으로 해결됩니다.

## Human (Message 13)

(base) dkmac@MacBook-Air-3 openclaw % launchctl list | grep -i openclaw
(base) dkmac@MacBook-Air-3 openclaw % launchctl list | grep -i moltbot
(base) dkmac@MacBook-Air-3 openclaw % launchctl list | grep -i node
(base) dkmac@MacBook-Air-3 openclaw %

## Claude (Message 14)

launchd에는 없네요. 그러면 다른 방향으로 — 누가 이 프로세스를 살려두는지 부모 프로세스를 추적해봅시다:

```bash
ps aux | grep 21189
```

그리고 부모 pid(PPID) 확인:

```bash
ps -o pid,ppid,command -p 21189
```

부모가 누구인지 보면 자동 재시작의 주체를 찾을 수 있어요.

## Human (Message 15)

(base) dkmac@MacBook-Air-3 openclaw % ps aux | grep 21189
dkmac            21189   0.3  2.4 444901200 400384   ??  S     9:06오전   0:03.27 moltbot-gateway    
dkmac            21232   0.0  0.0 435302224   1376 s000  S+    9:07오전   0:00.00 grep 21189

## Claude (Message 16)

`??` 가 터미널 세션과 무관하게 떠 있다는 뜻이에요. PPID를 확인해봅시다:

```bash
ps -o pid,ppid,command -p 21189
```

## Human (Message 17)

(base) dkmac@MacBook-Air-3 openclaw % ps -o pid,ppid,command -p 21189
  PID  PPID COMMAND
21189     1 moltbot-gateway

## Claude (Message 18)

PPID가 `1` — 즉 **init(launchd) 자식 프로세스**예요. launchd가 직접 관리하는데 `launchctl list`에는 안 잡혔다는 게 이상하네요.

숨겨진 plist 파일을 직접 찾아봅시다:

```bash
find ~/Library/LaunchAgents -name "*openclaw*" -o -name "*moltbot*" -o -name "*gateway*" 2>/dev/null
find /Library/LaunchAgents -name "*openclaw*" -o -name "*moltbot*" -o -name "*gateway*" 2>/dev/null
find /Library/LaunchDaemons -name "*openclaw*" -o -name "*moltbot*" -o -name "*gateway*" 2>/dev/null
```

## Human (Message 19)

(base) dkmac@MacBook-Air-3 openclaw % find ~/Library/LaunchAgents -name "_openclaw_" -o -name "_moltbot_" -o -name "_gateway_" 2>/dev/null
find /Library/LaunchAgents -name "_openclaw_" -o -name "_moltbot_" -o -name "_gateway_" 2>/dev/null
find /Library/LaunchDaemons -name "_openclaw_" -o -name "_moltbot_" -o -name "_gateway_" 2>/dev/null
/Users/dkmac/Library/LaunchAgents/ai.openclaw.gateway.plist
/Users/dkmac/Library/LaunchAgents/bot.molt.gateway.plist

## Claude (Message 20)

찾았어요. 두 개의 plist가 등록되어 있네요. `bot.molt.gateway.plist`가 범인입니다. 이걸 unload해야 해요:

```bash
launchctl unload ~/Library/LaunchAgents/bot.molt.gateway.plist
launchctl unload ~/Library/LaunchAgents/ai.openclaw.gateway.plist
```

확인:

```bash
lsof -i :18789
```

아무것도 안 나오면 성공. 그 다음 재실행:

```bash
ollama launch openclaw
```

## Human (Message 21)

(base) dkmac@MacBook-Air-3 openclaw % launchctl unload ~/Library/LaunchAgents/ai.openclaw.gateway.plist
Unload failed: 5: Input/output error
Try running `launchctl bootout` as root for richer errors.
(base) dkmac@MacBook-Air-3 openclaw % lsof -i :18789

## Claude (Message 22)

`unload`가 실패했네요. `bootout`으로 시도해봅시다:

```bash
launchctl bootout gui/$(id -u) ~/Library/LaunchAgents/ai.openclaw.gateway.plist
launchctl bootout gui/$(id -u) ~/Library/LaunchAgents/bot.molt.gateway.plist
```

확인:

```bash
lsof -i :18789
```

## Human (Message 23)

Last login: Sat Apr  4 09:06:10 on ttys001
(base) dkmac@MacBook-Air-3 openclaw % ollama launch openclaw

Launching OpenClaw with deepseek-v3.1:671b-cloud...
│
◇  Doctor warnings ───────────────────────────────────────╮
│                                                         │
│  - State dir migration skipped: target already exists   │
│    (/Users/dkmac/.openclaw). Remove or merge manually.  │
│                                                         │
├─────────────────────────────────────────────────────────╯
2026-04-04T00:10:00.494Z [canvas] host mounted at http://127.0.0.1:18789/__openclaw__/canvas/ (root /Users/dkmac/.openclaw/canvas)
2026-04-04T00:10:00.526Z [heartbeat] started
2026-04-04T00:10:00.527Z [gateway] agent model: ollama/deepseek-v3.1:671b-cloud
2026-04-04T00:10:00.528Z [gateway] listening on ws://127.0.0.1:18789 (PID 21452)
2026-04-04T00:10:00.528Z [gateway] listening on ws://[::1]:18789
2026-04-04T00:10:00.528Z [gateway] log file: /tmp/openclaw/openclaw-2026-04-04.log
2026-04-04T00:10:00.536Z [browser/service] Browser control service ready (profiles=2)
2026-04-04T00:10:00.546Z Registered hook: boot-md -> gateway:startup
2026-04-04T00:10:00.547Z Registered hook: command-logger -> command
2026-04-04T00:10:00.548Z Registered hook: session-memory -> command:new
2026-04-04T00:10:00.549Z [hooks] loaded 3 internal hook handlers
2026-04-04T00:10:02.783Z [telegram] [default] starting provider (@molt49_bot)
2026-04-04T00:10:02.788Z [telegram] autoSelectFamily=false (default-node22)

## Claude (Message 24)

🎉 성공입니다!

모든 서비스가 정상 기동됐어요:

- gateway listening on ws://127.0.0.1:18789 ✅
- browser control service ready ✅
- telegram bot 연결 ✅
- hooks 3개 로드 ✅

---

결국 원인은 **두 개의 plist가 충돌**하고 있었던 거예요. `bot.molt.gateway.plist`(구버전)와 `ai.openclaw.gateway.plist`(신버전)가 동시에 같은 포트를 두고 경쟁하는 구조였고, `bootout`으로 둘 다 정리하고 나서야 깨끗하게 뜬 것입니다.

재발 방지를 원하시면 두 plist 파일 중 하나를 제거해두는 게 좋아요:

```bash
# 구버전 plist 비활성화 (삭제 대신 이름 변경으로 안전하게)
mv ~/Library/LaunchAgents/bot.molt.gateway.plist ~/Library/LaunchAgents/bot.molt.gateway.plist.bak
```

이제 OpenClaw 잘 쓰세요, CSP!

## Human (Message 25)

```
http://127.0.0.1:18789/__openclaw__/canvas/%20(root%20/Users/dkmac/.openclaw/canvas)
not found
```

이거 맞음?

## Claude (Message 26)

아니요, 그 URL은 잘못된 거예요. 로그에서 복사할 때 뒷부분 `(root /Users/dkmac/.openclaw/canvas)`까지 같이 딸려온 거예요.

올바른 URL은:

```
http://127.0.0.1:18789/__openclaw__/canvas/
```

이걸 브라우저에 직접 입력해보세요.

## Human (Message 27)

_(내용 없음)_

## Claude (Message 28)

Canvas 페이지는 뜨고 있어요. 그런데 **Bridge: missing** 이게 문제예요.

Canvas는 브라우저와 gateway 사이의 WebSocket bridge가 연결되어야 작동하는데, 지금 그 연결이 없는 상태입니다. iOS=no, Android=no도 같은 맥락이고요.

이건 **일반 브라우저로 직접 접근하면 안 되는 페이지**예요. OpenClaw가 제어하는 브라우저(내장 브라우저 또는 확장이 설치된 Chrome) 안에서 열려야 bridge가 연결됩니다.

확인해보세요:

```bash
# OpenClaw가 어떤 방식으로 UI를 여는지 확인
openclaw --help
# 또는
openclaw open
openclaw ui
```

원래 OpenClaw를 어떤 용도로 쓰시려던 건가요? Telegram bot으로 명령을 보내는 방식인지, 아니면 별도 UI가 있는 건지 — 목적을 알면 올바른 접근 방법을 찾을 수 있어요.

---

_Archived from: `aaea33fe-b3d4-4cb6-a857-9d04cbb1d2f6.json`_
