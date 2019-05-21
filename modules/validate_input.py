import tkinter
from tkinter import messagebox
import sys


def validate_length(key_dec):

    if len(key_dec.split('.')) != 32:
        messagebox.showinfo('Error', 'Length of key is wrong!')