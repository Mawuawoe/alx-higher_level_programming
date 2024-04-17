#!/usr/bin/python3
"""
This module has 1 function that adds two integers together
"""
def add_integer(a, b=98):
    """
    Return the sum of two integers or float

    Args:
        a: first argument
        b: second argument

    Returns:
        sum of the two arguments

    Raises:
        TypeError: if either of the arguments are not integer or a float
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    result = int(a) + int(b)
    return result
