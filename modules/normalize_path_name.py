import os
from os import path


def normalize_path_name(*args):
    return path.abspath(path.join(os.sep, *args))


if __name__ == '__main__':
    pass
