# Zain-Zen Dotfiles

My personal config files for EndeavourOS + bspwm, themed around Catppuccin Mocha.

## Details
- **WM**: bspwm
- **Terminal**: Ghostty
- **Shell**: zsh (with starship & fzf-tab)
- **Editor**: Neovim (Kickstart base config)
- **App Launcher**: Rofi

## Key Features
- **Translator Popup (`super + t`)**: A custom script (`rofi-translate`) that opens a Rofi box, takes Indonesian input, translates it to English via curl in ~150ms, and pastes it into your focused terminal. Great for prompting AI tools in English without wasting tokens on bilingual context.

## Installation
The repository includes a simple linking script that backups your existing configurations to `*.bak` and creates symbolic links to this directory:

```bash
git clone https://github.com/Zainul342/dotfiles.git ~/dotfiles
cd ~/dotfiles
./install.sh
```
