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
    "light"
]

os.system("git pull")

os.system(f"git add README.md {os.path.basename(__file__)}")

for dir in directorys:
    os.system(f"git add {dir}")

os.system(f"""git commit -m 'Update Dot - {date_now.strftime("%d/%m/%Y %H:%M:%S")}'""")
os.system(f"git push")
    