#!/usr/bin/python3
import unittest
import sys
# sys.path.append('..')
from models.base import Base
from models.rectangle import Rectangle



class test_rectangle(unittest.TestCase):
    '''
        Testing rectangle
    '''

    def setUp(self):
        '''
            Initializing instance with width and height
            parameters
        '''
        self.r = Rectangle(5, 10)

    def tearDown(self):
        '''
            Deleting created instance
        '''
        del self.r

    def test_width(self):
        '''
            Testing the Rectangle width getter
        '''
        self.assertEqual(5, self.r.width)

    def test_height(self):
        '''
            Testing the Rectangle height getter
        '''
        self.assertEqual(10, self.r.height)

    def test_x(self):
        '''
            Testing Rectangle x getter and setter
        '''

        self.r.x = 54
        self.assertEqual(54, self.r.x)
        self.assertEqual(0, self.r.y)

    def test_y(self):
        '''
            Testing Rectangle y getter and setter
        '''

        self.r.y = 45
        self.assertEqual(45, self.r.y)
        self.assertEqual(0, self.r.x)

    def test_arectangle_id(self):
        '''
            Test the id for Rectangle
        '''
        rect = Rectangle(1, 3, 0, 0, 199)
        self.assertEqual(199, rect.id)

    def test_width_string(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            rect = Rectangle("1", 5)

    def test_width_list(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            rect = Rectangle([10, 6], 5)

    def test_height_string(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            rect = Rectangle(1, "5")

    def test_height_list(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            rect = Rectangle(5, [10, 6])

    def test_x_string(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 5, "46")

    def test_x_list(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 5, [10, 6])

    def test_y_string(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 5, 7, "46")

    def test_x_list(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 5, 7, [10, 6])

    def test_width_negative(self):
        '''
            Testing with negative int
        '''
        with self.assertRaises(ValueError):
            rect = Rectangle(-4, 5)

    def test_height_negative(self):
        '''
            Testing with negative int
        '''
        with self.assertRaises(ValueError):
            rect = Rectangle(4, -5)

    def test_x_negative(self):
        '''
            Testing with negative int
        '''
        with self.assertRaises(ValueError):
            rect = Rectangle(4, 5, -3)

    def test_y_negative(self):
        '''
            Testing with negative int
        '''
        with self.assertRaises(ValueError):
            rect = Rectangle(4, 5, 2, -3)

    def test_width_zero(self):
        '''
            Testing with negative int
        '''
        with self.assertRaises(ValueError):
            rect = Rectangle(0, 5)

    def test_height_zero(self):
        '''
            Testing with negative int
        '''
        with self.assertRaises(ValueError):
            rect = Rectangle(8, 0)

    def test_width_float(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            rect = Rectangle(1.07, 5)

    def test_height_float(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            rect = Rectangle(5, 1.07)

    def test_x_float(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            rect = Rectangle(5, 8, 1.07)

    def test_y_float(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            rect = Rectangle(5, 5, 8, 1.07)
    
    def test_area(self):
        rect = Rectangle(2, 3, 0, 0, 92)
        self.assertEqual(rect.area(), 6)

    def test_print(self):
        r = Rectangle(5, 10, 8, 7, 88)
        self.assertEqual(r.__str__(), "[Rectangle] (88) 8/7 - 5/10")

    def test_update_id(self):
        self.r.update(10)
        self.assertEqual(self.r.id, 10)

    def test_update_width(self):
        self.r.update(10, 10)
        self.assertEqual(self.r.width, 10)

    def test_update_height(self):
        self.r.update(10, 10, 10)
        self.assertEqual(self.r.height, 10)

    def test_update_x(self):
        self.r.update(10, 10, 10, 10)
        self.assertEqual(self.r.x, 10)

    def test_update_y(self):
        self.r.update(10, 10, 10, 10, 10)
        self.assertEqual(self.r.y, 10)

    def test_update_kwarg(self):
        self.r.update(id = 20, width = 20, height = 20, x = 20, y = 20)
        self.assertEqual(self.r.id, 20)
        self.assertEqual(self.r.width, 20)
        self.assertEqual(self.r.height, 20)
        self.assertEqual(self.r.x, 20)
        self.assertEqual(self.r.y, 20)

    def test_update_dict_list(self):
        '''
            Testing the update method with **kwargs and *args
        '''
        self.r.update(1000, y=1, width=2, x=3, id=89)
        self.assertEqual(1000, self.r.id)

    def test_to_dictionary(self):
        rect_2 = Rectangle(10,10,0,0,89)
        rect_2_dict = rect_2.to_dictionary()
        self.assertEqual(type(rect_2_dict), dict)

    def test_dict(self):
        rect_2 = Rectangle(10,10,0,0,89)
        rect_2_dict = rect_2.to_dictionary()
        self.assertEqual(rect_2_dict, {'x': 0, 'y': 0,
                    'id': 89, 'width': 10,
                    'height': 10})        

    def test_missing_width(self):
        '''
            Expecting an error because width is missing
        '''
        with self.assertRaises(TypeError):
            Rectangle(1)


if __name__ == '__main__':
    unittest.main()
