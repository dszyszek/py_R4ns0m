## py_R4ns0m
Implementation of ransomware in python 3

## Technologies

- Python 3.7
- tkinter

## Features
The main goal of py_R4ns0m ransomware is to encrypt data of someones computer.<br>
All the data will be encrypted with 256-bit AES CBC, so after encryption, the only reasonable way to get the data back is to contact with you. <br>
There are several features, to make program better:
- Program will test if key you input (after encryption) is valid (to avoid situation where data is decrypted with wrong key -> this would screw up all the data)
- Report with key, hashing etc. will be sent to your email address
- If there are problems with internet connection, program will wait and try every 10 seconds to send email with report (to prevent key loss)
- After encryption, there will be GUI message prompted to victim
- Closing the GUI prompt is disabled (because this window is the only wawy to decrypt data, so it'll be better to not close this)
- Wallpaper of victims computer will be changed to frog.jpg file
- Length of key the victim input is validated

## Usage

Ok, so after you set the program up with (in main dir): <br>
```$ python3 setup.py``` <br>
ransomware is ready to go.<br>
If you want program to behave like trojan, you can pack everything up with pyinstaller. Type: <br>
```pyinstaller ./ransom.py --add-data "<path to fake file (pdf, jpg)>;." --add-data "./img/frog.jpg;." --onefile --noconsole --icon "<path to icon of fake file>"``` <br>
in main dir. After that you'll have standalone ransomware, ready to launch.

## Info
Program created for educational purposes only! Encrypting someones hard drive without the permission is illegal, so I'm not taking the responsibility for possible losses.

## Author

[dszyszek](https://github.com/dszyszek)