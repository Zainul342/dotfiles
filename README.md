# Zain-Zen Dotfiles

A premium, aesthetic, and highly optimized Linux configuration setup featuring **Catppuccin Mocha** colors, custom keyboard workflows, and lightweight tools. 

Designed for **EndeavourOS** running **bspwm** and configured for maximum developer productivity.

---

## 🎨 Setup Details
* **OS**: EndeavourOS
* **WM**: bspwm
* **Theme**: Catppuccin Mocha (Zain-Zen Variant)
* **Shell**: zsh (customized with starship and fzf-tab)
* **Terminal**: Ghostty
* **Editor**: Neovim (Kickstart base configuration)
* **File Manager**: Yazi
* **App Launcher**: Rofi

---

## 🚀 Key Workflows Included
- **Global Translation Shortcut (`super + t`)**: Opens a Rofi prompt, lets you type in Indonesian, translates to English using a direct API query (~170ms), and:
  - **`Enter`**: Auto-pastes it directly into your active window/terminal (saves tokens for LLM chat agents).
  - **`Shift + Enter`**: Copies it to your clipboard only.

---

## 📦 What's Managed
This repository contains configuration directories for:
- `.config/bspwm` (Window manager settings + `sxhkd` keybindings)
- `.config/ghostty` (Terminal emulator settings)
- `.config/nvim` (Neovim editor configurations)
- `.zshrc` (Shell integrations and aliases)

---

## 🛠️ Installation

> [!WARNING]
> Running the installer will automatically backup any existing configuration files at `~/.config/...` to `~/.config/...bak` to ensure you do not lose your original settings.

Clone the repository and run the self-contained installation script:

```bash
git clone https://github.com/Zainul342/dotfiles.git ~/dotfiles
cd ~/dotfiles
chmod +x install.sh
./install.sh
```

---

## ⚖️ License
Licensed under the [MIT License](LICENSE).
