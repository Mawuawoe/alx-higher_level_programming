#!/usr/bin/python3
"""
unittesting example
"""
import unittest
import sys
sys.path.append('..')
from models.base import Base


class Base_Test(unittest.TestCase):

    def test_baseconstruct(self):
        b1 = Base(12)
        id_no = b1.id
        self.assertEqual(id_no, 12)


if __name__ == '__main__':
    unittest.main()
