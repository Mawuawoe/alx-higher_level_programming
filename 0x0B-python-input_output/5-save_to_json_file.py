#!/usr/bin/python3
"""
This module has a function to write to a file
it take any python obj via json 
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Arg:
        my_obj: it a python object and not a string.
        so to write it to a .txt file we need to convert to
        a string.
        the json.dumps(my_obj) does this

        filename: is the .txt file to write to 
    """
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
