#!/usr/bin/python3
import unittest
from employee_class import Employee

class Test_Employee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("run once at the very beginning")
    
    @classmethod
    def tearDownClass(cls):
        print("run once after everything")

    def setUp(self):
        self.emp_1 = Employee('Des', 'Dzakago', 8000)
        self.emp_2 = Employee('Sav', 'Klutse', 6000)
    

    def tearDown(self):
        pass

    def test_email(self):


        self.assertEqual(self.emp_1.email, 'Des.Dzakago@email.com')
        self.assertEqual(self.emp_2.email, "Sav.Klutse@email.com")

        self.emp_1.first = "John"
        self.emp_2.first = "Jane"

        self.assertEqual(self.emp_1.email, 'John.Dzakago@email.com')
        self.assertEqual(self.emp_2.email, "Jane.Klutse@email.com")

    def test_fullname(self):

        self.assertEqual(self.emp_1.fullname, 'Des Dzakago')
        self.assertEqual(self.emp_2.fullname, "Sav Klutse")

        self.emp_1.first = "John"
        self.emp_2.first = "Jane"

        self.assertEqual(self.emp_1.fullname, 'John Dzakago')
        self.assertEqual(self.emp_2.fullname, "Jane Klutse")

    def test_apply_raise(self):

        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, (8000 * 1.05))
        self.assertEqual(self.emp_2.pay, (6000 * 1.05))


if __name__ == "__main__":
    unittest.main()