#!/usr/bin/python3
import unittest
import cal

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(cal.add(10, 5), 15)
        self.assertEqual(cal.add(-1, 1), 0)
        self.assertEqual(cal.add(-1, -1), -2)

    def test_sub(self):
        self.assertEqual(cal.sub(10, 5), 5)
        self.assertEqual(cal.sub(-1, 1), -2)
        self.assertEqual(cal.sub(-1, -1), 0)

    def test_mul(self):
        self.assertEqual(cal.mul(10, 5), 50)
        self.assertEqual(cal.mul(-1, 1), -1)
        self.assertEqual(cal.mul(-1, -1), 1)
    
    def test_div(self):
        self.assertEqual(cal.div(10, 5), 2)
        self.assertEqual(cal.div(-1, 1), -1)
        self.assertEqual(cal.div(-1, -1), 1)

        with self.assertRaises(ValueError):
            cal.div(10, 0)

if __name__ == '__main__':
    unittest.main()