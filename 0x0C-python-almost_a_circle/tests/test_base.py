#!/usr/bin/python3
"""
Test for Base
"""


import unittest
import sys
sys.path.append('..')
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


'''
    Creating test cases for the base module
'''


class test_base(unittest.TestCase):
    '''
        Testing base
    '''
    def test_id_none(self):
        '''
            when you pass in no id
        '''
        b = Base()
        self.assertEqual(1, b.id)

    def test_id(self):
        '''
            when you pass in a valid id
        '''
        b = Base(50)
        self.assertEqual(50, b.id)

    def test_id_zero(self):
        '''
            for an id = 0
        '''
        b = Base(0)
        self.assertEqual(0, b.id)

    def test_id_negative(self):
        '''
            for a negative id
        '''
        b = Base(-20)
        self.assertEqual(-20, b.id)

    def test_id_string(self):
        '''
            for an id that is not an int
        '''
        b = Base("Betty")
        self.assertEqual("Betty", b.id)

    def test_id_list(self):
        '''
            for an id that is not an int
        '''
        b = Base([1, 2, 3])
        self.assertEqual([1, 2, 3], b.id)

    def test_id_dict(self):
        '''
            Sending an id that is not an int
        '''
        b = Base({"id": 109})
        self.assertEqual({"id": 109}, b.id)

    def test_id_tuple(self):
        '''
            Sending an id that is not an int
        '''
        b = Base((8,))
        self.assertEqual((8,), b.id)

    def test_to_json_string(self):
        s1 = Rectangle(10, 10, 2, 3, 89)
        s1_dict = s1.to_dictionary()
        s1_json_string = Base.to_json_string([s1_dict])
        self.assertEqual(type(s1_json_string), str)
        self.assertEqual(s1_json_string, '[{"x": 2, "y": 3, "id": 89, "width": 10, "height": 10}]')

    def test_to_json_None(self):
        '''
            Testing the json string
        '''
        sq = Square(1, 0, 0, 609)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_to_json_Empty(self):
        '''
            Testing the json string
        '''
        sq = Square(1, 0, 0, 609)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")


if __name__ == '__main__':
    unittest.main()
