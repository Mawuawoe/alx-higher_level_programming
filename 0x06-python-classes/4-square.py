#!/usr/bin/python3
# 1-square.py by Des
"""Defines a square"""
class Square:
    """Represents a square"""

    def __init__(self, size=0):
        self.size = si
        """Initializing this square class
        Args: size - represnets the size of the square defined
        Raise:
        TypeError: if size is not interger
        ValueError: if size is less than 0
        """
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size


    
    @property
    def size(self):
        """Retrieves size of square"""
        return self.__size
    
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value = 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Return the current square area"""
        return (self.__size ** 2)
