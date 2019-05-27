import platform
import os
import subprocess
import sys

from modules.normalize_path_name import normalize_path_name


def recognize_platform():
    os_platform =  platform.system()

    if os_platform == 'Darwin':
        return 'osx'
    elif os_platform == 'Windows':
        return 'windows'
    elif os_platform == 'Linux':
        return 'linux'
    else:
        return 'unknown', os_platform


def change_wallpaper():
    system = recognize_platform()
    path_to_img = normalize_path_name(sys._MEIPASS, 'frog.jpg')

    if system == 'windows':
        # Test windows background change
        import ctypes

        SPI_SETDESKWALLPAPER = 20
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path_to_img, 0)

    elif system == 'osx':
        # Test osx background change

        script = """

        on run(x)
            tell application "Finder" to set desktop picture to POSIX file x   
        end run

        """

        args = [path_to_img]
        p = subprocess.Popen(['osascript', '-'] + args, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        p.communicate(script)

    elif system == 'linux':
        # Test linux background change
        pass


if __name__ == '__main__':
    change_wallpaper()