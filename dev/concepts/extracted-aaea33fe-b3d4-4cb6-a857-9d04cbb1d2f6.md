# Extracted Knowledge from Conv: aaea33fe-b3d4-4cb6-a857-9d04cbb1d2f6

**Date**: 2026-04-03T23:58:18.625725Z

### Extracted Code (bash)

```bash
find ~/Library/LaunchAgents -name "*openclaw*" -o -name "*moltbot*" -o -name "*gateway*" 2>/dev/null
find /Library/LaunchAgents -name "*openclaw*" -o -name "*moltbot*" -o -name "*gateway*" 2>/dev/null
find /Library/LaunchDaemons -name "*openclaw*" -o -name "*moltbot*" -o -name "*gateway*" 2>/dev/null
```

### Extracted Code (bash)

```bash
launchctl unload ~/Library/LaunchAgents/bot.molt.gateway.plist
launchctl unload ~/Library/LaunchAgents/ai.openclaw.gateway.plist
```

### Extracted Code (bash)

```bash
launchctl bootout gui/$(id -u) ~/Library/LaunchAgents/ai.openclaw.gateway.plist
launchctl bootout gui/$(id -u) ~/Library/LaunchAgents/bot.molt.gateway.plist
```

### Extracted Code (bash)

```bash
# 구버전 plist 비활성화 (삭제 대신 이름 변경으로 안전하게)
mv ~/Library/LaunchAgents/bot.molt.gateway.plist ~/Library/LaunchAgents/bot.molt.gateway.plist.bak
```
