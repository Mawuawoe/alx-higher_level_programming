#!/usr/bin/python3
"""
This is a baseGeometry class
"""


class BaseGeometry:
    """
    area method  that raises an Exception
    with the message area() is not implemented
    """
    def area(self):
        raise Exception("area() is not implemented")
