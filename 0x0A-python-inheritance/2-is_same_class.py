#!/usr/bin/python3
""" A module that checks if object is an instance of a class"""


def is_same_class(obj, a_class):
    """
    Return true if object is an instance of the
    class, otherwise return false
    """
    if type(obj) is a_class:
        return (True)
    else:
        return (False)
