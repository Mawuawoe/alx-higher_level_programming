#!/usr/bin/python3
"""
This module contain a class Rectangle
that inherite from base
"""
from models.base import Base


class Rectangle(Base):
    """
    Class rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialises obj attributes"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """get heigth"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    @property
    def x(self):
        """get x"""
        return self.__x

    @x.setter
    def height(self, value):
        """set x"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__x = value

    @property
    def y(self):
        """get y"""
        return self.__y

    @y.setter
    def height(self, value):
        """set y"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__y = value
