#!/usr/bin/python3
"""
this module prints your first n last name
"""


def say_my_name(first_name, last_name=""):
    """
    this function prints your name

    Arg:
        1. firstname
        2. Lastname

    it raise a TypeError when either of the Args are not strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
