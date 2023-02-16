import random
import time
import os

time.sleep(2)

dir = "/home/invisiblecat/.config/hypr/wallpapers/"
max = 0
for path in os.listdir(dir):
    if os.path.isfile(os.path.join(dir, path)):
        max += 1

number = random.randint(1, max)

print(number)
os.system(f"hyprctl hyprpaper wallpaper eDP-1,/home/invisiblecat/.config/hypr/wallpapers/{number}.jpg")