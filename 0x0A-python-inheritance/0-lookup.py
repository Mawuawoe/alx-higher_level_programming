#!/usr/bin/python3
""" This module return a list of attribute
and methods of an object
"""


def lookup(obj):
    """ A function that return a list of attribute
    and modules of an object
    
    Arg:
        obj - the object
    """
    return dir(obj)
