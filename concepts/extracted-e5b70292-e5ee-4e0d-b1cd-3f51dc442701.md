# Extracted Knowledge from Conv: e5b70292-e5ee-4e0d-b1cd-3f51dc442701

**Date**: 2025-09-11T01:24:33.109593Z

### Extracted Code (bash)

```bash
# Ubuntu/Debian
sudo apt install ibus-hangul
sudo apt install fcitx5-hangul

# CentOS/RHEL/Fedora
sudo yum install ibus-hangul
sudo dnf install fcitx5-hangul
```

### Extracted Code (bash)

```bash
# GUI에서 설정
gnome-control-center region

# 또는 명령어로
gsettings set org.gnome.desktop.input-sources sources "[('xkb', 'us'), ('ibus', 'hangul')]"
```

### Extracted Code (bash)

```bash
export GTK_IM_MODULE=ibus
export QT_IM_MODULE=ibus
export XMODIFIERS=@im=ibus
export QT4_IM_MODULE=ibus
```

### Extracted Code (bash)

```bash
# 이미 설치된 ibus-hangul 확인
rpm -qa | grep ibus-hangul
dnf list installed | grep ibus

# 사용자 설정으로 활성화
ibus-setup
```

### Extracted Code (bash)

```bash
# 환경변수를 사용자 프로필에만 추가
echo 'export GTK_IM_MODULE=ibus' >> ~/.bashrc
echo 'export QT_IM_MODULE=ibus' >> ~/.bashrc  
echo 'export XMODIFIERS=@im=ibus' >> ~/.bashrc

# 현재 세션에 적용
source ~/.bashrc
```

### Extracted Code (bash)

```bash
# GUI 없이 gsettings로 설정
gsettings set org.gnome.desktop.input-sources sources "[('xkb', 'us'), ('ibus', 'hangul')]"
gsettings set org.gnome.desktop.wm.keybindings switch-input-source "['<Super>space']"
```

### Extracted Code (bash)

```bash
# 현재 활성화된 입력 소스 확인
gsettings get org.gnome.desktop.input-sources current
gsettings get org.gnome.desktop.input-sources sources

# 한글 입력 소스로 강제 전환
gsettings set org.gnome.desktop.input-sources current 1
```
