#!/usr/bin/python3
"""
This is a baseGeometry class
"""


class BaseGeometry:
    """
    method:
        area method  that raises an Exception
        with the message area() is not implemented

        nteger_validator(self, name, value):
        validattes value as an integer which is greater than 0
    """
    def area(self):
        """
        area method
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates a value as a greater than 0 integer
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
