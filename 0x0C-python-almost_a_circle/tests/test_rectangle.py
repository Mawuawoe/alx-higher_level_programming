#!/usr/bin/python3
import unittest
import sys
sys.path.append('..')
from models.base import Base
from models.rectangle import Rectangle


class Test_Rectanle(unittest.TestCase):
    """
    test if Rectanle is a subclass of Base
    """
    def test_rectangle_issubclass(self):
        self.assertTrue(issubclass(Rectangle, Base))

    """testing the id of rectangle """
    def test_rectangle_id(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(2, 10, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    """test for width"""
    def test_width(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)

    """width must be an integer"""
    def test_width_2(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle("10", 2)

    """width must be > 0"""
    def test_width_3(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(-10, 2)

    """test for height"""
    def test_height(self):
        r = Rectangle(10, 3, 0, 0, 12)
        self.assertEqual(r.height, 3)

    """width must be an integer"""
    def test_height_2(self):
        with self.assertRaises(TypeError):
            r = Rectangle(10, "2")

    """height must be > 0"""
    def test_height_3(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(10, -2)

    """test for x"""
    def test_x(self):
        r = Rectangle(10, 3, 1, 0, 12)
        self.assertEqual(r.x, 1)

    """x must be an integer"""
    def test_x_2(self):
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2, '1', 0, 11)

    """x must be >= 0"""
    def test_x_3(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(10, 2, -2, 0, 10)

    """test for x"""
    def test_y(self):
        r = Rectangle(10, 3, 1, 0, 12)
        self.assertEqual(r.y, 0)

    """y must be an integer"""
    def test_y_2(self):
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2, 1, '2', 11)

    """y must be >= 0"""
    def test_y_3(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(10, 2, 2, -1, 10)

    """Test for area"""
    def test_area(self):
        ra = Rectangle(2, 3, 0, 0, 5)
        self.assertEqual(ra.area(), 6)


if __name__ == '__main__':
    unittest.main()