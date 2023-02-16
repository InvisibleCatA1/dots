# My dots

.config files for my system. 

Install:

```
1. Download the install.sh script
2. Run: chmod +x install.sh
3. Run: ./install.sh
```

This will install these dots on your system, and update them when you restart your computer if using hyprland. If you want to use this feture go into ``~/.config/dot_update.py`` and change ``user = "invisiblecat"`` to your username. If you dont want this remove the ``exec-once = python3 ~/.config/dot_update.py`` line in ``~/.config/hypr/hyprland.conf`` 
