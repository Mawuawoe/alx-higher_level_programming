#!/usr/bin/python3
"""
this module return a dictionary that holds
the attribute(variable) and their corresponding
values of an object
"""


def class_to_json(obj):
    """
    the function
    """
    return obj.__dict__
