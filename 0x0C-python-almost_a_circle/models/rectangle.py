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
        self.width = width
        self.height = height
        self.x = x
        self.y = y
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
        if value <= 0:
            raise ValueError('width must be > 0')
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
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """get x"""
        return self.__x

    @x.setter
    def x(self, value):
        """set x"""
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """get y"""
        return self.__y

    @y.setter
    def y(self, value):
        """set y"""
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """Area of a rectantangle"""
        return (self.__width * self.__height)

    def display(self):
        """print the shape of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            print("")
        rectangle = ""
        for y in range(self.__y):
            print("")
        for i in range(self.__height):
            for x in range(self.__x):
                rectangle += " "
            for j in range(self.__width):
                rectangle += '#'
            if i < self.__height - 1:
                rectangle += '\n'
        print(rectangle)

    def __str__(self):
        """what you will get if you print(obj/r1)"""
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """passing variable position arg"""
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.__width = arg
                elif a == 2:
                    self.__height = arg
                elif a == 3:
                    self.__x = arg
                elif a == 4:
                    self.__y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == 'id':
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == 'width':
                    self.__width = v
                elif k == 'height':
                    self.__height = v
                elif k == 'x':
                    self.__x = v
                elif k == 'y':
                    self.__y = v

    def to_dictionary(self):
        """dict"""
        return self.__dict__
