import os
from datetime import datetime

date_now = datetime.now()
user = "invisiblecat"
os.chdir(f"/home/{user}/.config/")
directorys = [
    "hypr",
    "alacritty",
    "swaylock",
    "wofi",
    "waybar",
    "light",
    "dunst"
]

files = {
    "README.md",
    os.path.basename(__file__),
    "install.sh"
}

os.system("git pull")

for file in files:
    os.system(f"git add {file}")

for dir in directorys:
    os.system(f"git add {dir}")

os.system(f"""git commit -m 'Update Dots - {date_now.strftime("%d/%m/%Y %H:%M:%S")}'""")
os.system(f"git push")
