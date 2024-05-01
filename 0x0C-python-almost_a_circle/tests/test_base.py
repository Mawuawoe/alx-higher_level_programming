#!/usr/bin/python3
import unittest
import sys
from models.base import Base
# sys.path.append('..')


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


if __name__ == '__main__':
    unittest.main()
