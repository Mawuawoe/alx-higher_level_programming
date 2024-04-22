#!/usr/bin/python3
"""
This module write to file and return the
number of characters written
"""


def write_file(filename="", text=""):
    """
    function to write to a file
    return:
        number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
