#!/usr/bin/python3
"""
Test for Square
"""
import unittest
import sys
# sys.path.append('..')
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class test_square(unittest.TestCase):

    def setUp(self):
        self.s = Square(5)

    def tearDown(self):
        del self.s
    
    def test_size(self):
        self.assertEqual(self.s.size, 5)
    
    def test_width(self):
        self.assertEqual(self.s.width, 5)
    
    def test_height(self):
        self.assertEqual(self.s.height, 5)
    
    def test_x(self):
        self.s.x = 54
        self.assertEqual(self.s.x, 54)
        self.assertEqual(self.s.y, 0)
    
    def test_y(self):
        self.s.y = 50
        self.assertEqual(self.s.y, 50)
        self.assertEqual(self.s.x, 0)
    
    def test_id(self):
        s1 = Square(10,0,0,89)
        self.assertEqual(s1.id, 89)

    def test_width_string(self):
        with self.assertRaises(TypeError):
            s2 = Square('2')

    def test_width_list(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            sq = Square([10, 6])

    def test_x_string(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            sq = Square(1, "46")

    def test_x_list(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            sq = Square(1, [10, 6])

    def test_y_string(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            sq = Square(1, 7, "46")

    def test_y_list(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            sq = Square(1, 7, [10, 6])

    def test_width_negative(self):
        '''
            Testing with negative int
        '''
        with self.assertRaises(ValueError):
            sq = Square(-4)

    def test_x_negative(self):
        '''
            Testing with negative int
        '''
        with self.assertRaises(ValueError):
            sq = Square(4, -3)

    def test_y_negative(self):
        '''
            Testing with negative int
        '''
        with self.assertRaises(ValueError):
            sq = Square(4, 2, -3)

    def test_width_zero(self):
        '''
            Testing with negative int
        '''
        with self.assertRaises(ValueError):
            sq = Square(0, 5)

    def test_width_float(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            sq = Square(1.07, 5)

    def test_x_float(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            sq = Square(5, 1.07)

    def test_y_float(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            sq = Square(5, 8, 1.07)

    def test_area(self):
        self.assertEqual(self.s.area(), 25)

    def test_str_overload(self):
        s = Square(5, 8, 7, 88)
        self.assertEqual(s.__str__(), "[Square] (88) 8/7 - 5")

    def test_update_id(self):
        '''
            Testing the update method
        '''
        self.s.update(54)
        self.assertEqual(54, self.s.id)

    def test_update_width(self):
        '''
            Testing the update method
        '''
        self.s.update(54, 30)
        self.assertEqual(30, self.s.size)

    def test_update_x(self):
        '''
            Testing the update method
        '''
        self.s.update(54, 30, 10)
        self.assertEqual(10, self.s.x)

    def test_update_y(self):
        '''
            Testing the update method
        '''
        self.s.update(54, 30, 6, 2)
        self.assertEqual(2, self.s.y)

    def test_update_dict(self):
        '''
            Testing the update method with **kwargs
        '''
        self.s.update(y=1, size=2, x=3, id=89)
        self.assertEqual(1, self.s.y)
        self.assertEqual(2, self.s.size)
        self.assertEqual(3, self.s.x)
        self.assertEqual(89, self.s.id)

    def test_to_dict(self):
        '''
            Testing the type that is returned from the to_dictionary method
        '''
        r1 = Square(5)
        self.assertEqual(type(r1.to_dictionary()), dict)

    def test_to_dict_print(self):
        '''
            Testing the dict that will be printed
        '''
        r1 = Square(5, 0, 0, 410)
        r1_dict = r1.to_dictionary()
        self.assertEqual(r1_dict,
                         {'size': 5, 'id': 410, 'x': 0, 'y': 0})


if __name__ == '__main__':
    unittest.main()
