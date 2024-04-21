#!/usr/bin/python3
"""
This module read a file and print to stdout
"""


def read_file(filename=""):
    """
    function to read a file and print to stdout
    """
    with open(filename, 'r', encoding="utf-8") as f:
        f_content = f.read()
        print(f_content, end='')
    print()
