#!/usr/bin/python3
"""
This module append to file and return the
number of characters written
"""


def append_write(filename="", text=""):
    '''Appends a string to the end of a UTF8 text file
    '''
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
