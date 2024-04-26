#!/usr/bin/python3
import unittest

def sum(a, c):
    return a + c

class SumTest(unittest.TestCase):

    def setUp(self):
        print("SETUP CALLED")
        self.a = 10
        self.c = 20

    def tearDown(self):
        self.a = 0
        self.c = 0
        print("TEARDOWN CALLED")
    
    def test_sumfunc_1(self):
        print("TEST_1 CALLED")
        # Act
        result = sum(self.a, self.c)
        # Assert
        self.assertEqual(result, self.a + self.c)

    def test_sumfunc_2(self):
        print("TEST_2 CALLED")
        # Act
        result = sum(self.a, self.c)
        # Assert
        self.assertEqual(result, self.a + self.c)
        
    def test_func_2(self):
        pass

if __name__ == "__main__":
    unittest.main()