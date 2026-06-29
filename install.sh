#!/usr/bin/env bash

# Setup script to link dotfiles to system config locations

DOTFILES_DIR="$HOME/dotfiles"

link_file() {
  local src="$1"
  local dest="$2"
  
  # Ensure destination parent directory exists
  mkdir -p "$(dirname "$dest")"
  
  # If destination already exists
  if [ -e "$dest" ] || [ -L "$dest" ]; then
    # Check if it already points to the correct place
    if [ "$(readlink -f "$dest")" = "$(readlink -f "$src")" ]; then
      echo "✓ Already linked: $dest"
      return
    fi
    # Backup existing
    echo "⚠️ Backup existing config: $dest -> ${dest}.bak"
    mv "$dest" "${dest}.bak"
  fi
  
  echo "🔗 Linking: $src -> $dest"
  ln -s "$src" "$dest"
}

# Create links
link_file "$DOTFILES_DIR/zsh/.zshrc" "$HOME/.zshrc"
link_file "$DOTFILES_DIR/ghostty/.config/ghostty" "$HOME/.config/ghostty"
link_file "$DOTFILES_DIR/nvim/.config/nvim" "$HOME/.config/nvim"
link_file "$DOTFILES_DIR/bspwm/.config/bspwm" "$HOME/.config/bspwm"
link_file "$DOTFILES_DIR/copyq/.config/copyq/copyq.conf" "$HOME/.config/copyq/copyq.conf"
link_file "$DOTFILES_DIR/copyq/.config/copyq/copyq-commands.ini" "$HOME/.config/copyq/copyq-commands.ini"

echo "✨ Dotfiles setup completed successfully!"
