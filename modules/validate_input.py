import tkinter
from tkinter import messagebox
import sys
import re


def validate_length(key_dec):

    if len(key_dec.split('.')) != 32:
        messagebox.showinfo('Error', 'Length of key is wrong!')


def validate_email(email):
    validate = re.search('.+@gmail.com', email)

    try:
        validate.group(0)
        return True

    except AttributeError:
        return False
