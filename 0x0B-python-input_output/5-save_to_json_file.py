#!/usr/bin/python3
"""
This module write to file and return the
number of characters written
"""
import json


def save_to_json_file(my_obj, filename):
    """
    function to write to a file
    return:
        number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
