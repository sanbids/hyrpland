<div align="center">
<img alt="Profiles Pictures" src="https://raw.githubusercontent.com/sanbids/hyrpland/main/screenshot/face.jpg" width="200" height="200" style="border-radius: 15px;"/>
</div>

<div align="center">
  <h1>Sanbids Dotfiles 📁</h1>
      <img src="https://readme-typing-svg.demolab.com?font=Iosevka+Nerd+Font&weight=900&pause=1000&color=6791C9&background=0C0E0F00&center=true&vCenter=true&width=435&lines=Love+Yourself"
</div>

![](https://img.shields.io/github/last-commit/sanbids/hyprland?&style=for-the-badge&color=8D748C&logoColor=D9E0EE&labelColor=252733)
![](https://img.shields.io/github/stars/sanbids/hyprland?style=for-the-badge&logo=starship&color=AB6C6A&logoColor=D9E0EE&labelColor=252733)
[![](https://img.shields.io/github/repo-size/sanbids/hyprland?color=%23DDB&label=SIZE&logo=codesandbox&style=for-the-badge&logoColor=D9E0EE&labelColor=252733)](https://github.com/1amSimp1e/dots)
<a href="https://github.com/sanbids/hyprland/blob/main/LICENSE">
<img alt="License" src="https://img.shields.io/github/license/sanbids/hyprland?style=for-the-badge&logo=starship&color=A1C999&logoColor=D9E0EE&labelColor=252733" />
</a>
<a href="https://github.com/sanbids/hyprland/issues">
<img alt="Issues" src="https://img.shields.io/github/issues/sanbids/hyprland?style=for-the-badge&logo=bilibili&color=5E81AC&logoColor=D9E0EE&labelColor=252733" />
</a>


<br>
<br>
<div align="center" >
  
|Distro|[Arch](https://archlinux.org/)|
|:----:|:----:|
| WM|[HyprLand](https://github.com/hyprwm/Hyprland)|
|Bar|[Waybar](https://github.com/Alexays/Waybar)|
|Menu|[Rofi](https://github.com/davatorium/rofi)|
|Compositor|[Wayland](https://wayland.freedesktop.org/)|
|Terminal|[kitty](https://github.com/kovidgoyal/kitty)|
|Wallpaper Changer|[Swaybg](https://github.com/swaywm/swaybg)|
|Music/Player|[mpd](https://archlinux.org/packages/extra/x86_64/mpd/)-[ncmpcpp](https://archlinux.org/packages/community/x86_64/ncmpcpp/)|
|File Manager|[Thunar](https://archlinux.org/packages/extra/x86_64/thunar/)|
|Shell|[Zsh](https://archlinux.org/packages/extra/x86_64/zsh/)|
|Aur Helper|[yay](https://github.com/Jguer/yay)|
|IDE |[nvim](https://github.com/neovim/neovim)|


</div>

<div>

  <img src="" alt="wallpaper">

</div>
<br>
  
<div align="center">
    <h1>Installations 💫</h1>
</div>

<div>
  <h3 align="left">Auto-Script 󰑷 </h3>
</div>

<div align="left">

- First of all, Update your system

```bash
sudo pacman -Syu

```
  
- Install stow and git

  ```zsh
   sudo pacman -S git stow
  ```
  
- Install waybar, Rofi, Dunst, kitty terminal, swaybg, swaylock-fancy, swayidle, pamixer, light, Brillo etc..

```zsh
yay -S --noconfirm --needed base-devel rustup pacman-contrib kitty\
  alacritty brightnessctl dunst rofi lsd \
  jq polkit-gnome git playerctl mpd \
  ncmpcpp geany ranger mpc \
  feh pamixer libwebp \
  swaylock papirus-icon-theme \
  waybar-hyprland \
  swaybg swaylock-effects wofi wlogout mako thunar \
  noto-fonts-emoji \
  python-requests starship \
  swappy grim slurp gvfs gvfs-afc gvfs-mtp gvfs-nfs \
  bluez bluez-utils lxappearance xfce4-settings gtk3 qt5ct \ 
 hyprland bspwm 
  
```

  - Clone this repo and stow it
  
  ```zsh
  git clone https://github.com/sanbids/hyrpland && cd hyprland && stow .
  ```
  
</div>


  ---------------------


  
<div>
  <h3 align="left">Manually 💻</h3>
</div>

<div align="left">

- First of all, Update your system

```bash
sudo pacman -Syu

```
  
  - Then Install the newest [Hyprland](https://hyprland.org/) using this [guide](https://wiki.hyprland.org/Getting-Started/Installation/) depend on your Distro:

  ```zsh
  yay -S hyprland-git
  ```
  
  
- Install waybar, Rofi, Dunst, kitty terminal, swaybg, swaylock-fancy, swayidle, pamixer, light, Brillo etc..

```zsh
yay -S --noconfirm --needed base-devel rustup pacman-contrib kitty\
  alacritty brightnessctl dunst rofi lsd \
  jq polkit-gnome git playerctl mpd \
  ncmpcpp geany ranger mpc \
  feh pamixer libwebp \
  swaylock papirus-icon-theme \
  waybar-hyprland \
  swaybg swaylock-effects wofi wlogout mako thunar \
  noto-fonts-emoji  \
  python-requests starship \
  swappy grim slurp gvfs gvfs-afc gvfs-mtp gvfs-nfs \
  bluez bluez-utils lxappearance xfce4-settings gtk3 qt5ct bspwm \
   hyprland 
```
</div>

<br>
<div align="left">
  
### Necessary Font 🔑:

- [JetBrains Mono Nerd Font](https://github.com/ryanoasis/nerd-fonts/releases/download/v2.2.2/JetBrainsMono.zip)

- [Iosevka Nerd Font](https://github.com/ryanoasis/nerd-fonts/releases/download/v2.3.3/Iosevka.zip)

- [Font Awesome](https://archlinux.org/packages/community/any/ttf-font-awesome/)
  ```zsh
  yay -S ttf-font-awesome ttf-jetbrains-mono ttf-jetbrains-mono-nerd ttf-terminus-nerd ttf-inconsolata ttf-joypixels --noconfirm --needed
  ```
  </div>


<br>
<div align="left">
  
### Copy Files 💾

  - copy files in your $HOME/.config/ Before that backup your previous config files
```bash
git clone https://github.com/sanbids/hyprland
cd hyprland
cp -r ./.configs/* ~/.config/
```

</div>


> Finally, now you can login with Hyprland Rice

Congratulations, at this point you successfully have installed hyprland config and just rebooot your system
