#!/usr/bin/python3
# 1-square.py by Des
"""Defines a square"""
class Square:
    """Represents a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializing this square class
        Args: 
            size - represnets the size of the square defined
            position - 
     
        """
        self.size = size
        self.position = position
    @property
    def size(self):
        """Retrieves size of square"""
        return self.__size
    
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        return (self.__position)
    
    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        for i in value:
            if type(i) != int and i < 0:
                raise TypeError('position must be a tuple of 2 positive integers')
            self.__position = value

    def area(self):
        """Return the current square area"""
        return (self.__size ** 2)
    
    def pos_print(self):
        """returns the position in spaces"""
        pos = ""
        if self.size == 0:
            return "\n"
        for w in range(self.position[1]):
            pos += "\n"
        for w in range(self.size):
            for i in range(self.position[0]):
                pos += " "
            for j in range(self.size):
                pos += "#"
            pos += "\n"
        return pos    

    def my_print(self):
        """print the square in position"""
        print(self.pos_print(), end='')
