#!/usr/bin/python3
"""
This module has a class that inherite from
Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    square class
    method:
        arae(self): to cal the area
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
