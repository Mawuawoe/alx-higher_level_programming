#!/usr/bin/python3
"""
This module contain a class that inherite from list
"""


class MyList(list):
    """
     a class MyList that inherits from list
    """
    def print_sorted(self):
        """
        Public instance method that prints the list,
        but sorted (ascending sort)
        """
        print(sorted(self))
