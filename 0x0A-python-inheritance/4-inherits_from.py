#!/usr/bin/python3
"""
This module has a function that returns True if the object
is an instance of a class that inherited (directly or indirectly)
the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """
    function that returns True if the object is an instance of
    a class that inherited (directly or indirectly)
    the specified class ; otherwise False.
    """
    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
