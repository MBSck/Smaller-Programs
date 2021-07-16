import time
import os, sys, random
import ctypes

# sys.stderr.write("Hello")

wallpaper_folder = "C:\\Users\Marten\Desktop\Wallpapers"


def get_desktop_background():
    file = random.choice(os.listdir(wallpaper_folder))
    return os.path.join(wallpaper_folder, file)


def automatic_loop():
    while True:
        time.sleep(1800)
        ctypes.windll.user32.SystemParametersInfoW(20, 0, get_desktop_background(), 0)


if __name__ == "__main__":
    automatic_loop()