import os

os.system("git pull")
directorys = [
    "hypr",
    "alacritty",
    "swaylock",
    "wofi",
    "waybar",
    "light"
]

os.system(f"git add README.md {os.path.basename(__file__)}")
files = 0
for dir in directorys:
    os.system(f"git add {dir}")
    files += 1

os.system(f"git commit -m 'Update Dots - {files} file(s) updated'")
os.system(f"git push")
    