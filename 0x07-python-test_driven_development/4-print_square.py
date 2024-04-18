#!/usr/bin/python3
"""
this module has 1 function that print a square
"""


def print_square(size):
    """
    this function prints a sqaure using #

    Arg:
        size: the size of the square

    the size must be an integer else a TypeError is raised
    size must be >= 0 else a ValueError is raised
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print("#" * size)
