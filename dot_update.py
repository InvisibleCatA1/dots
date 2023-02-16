import os


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

os.system(f"git commit -m 'Update Dots'")
os.system(f"git push")
    