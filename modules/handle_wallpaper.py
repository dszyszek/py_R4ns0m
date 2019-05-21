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