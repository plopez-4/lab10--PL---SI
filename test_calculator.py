import unittest
from calculator import *
# git link-https://github.com/plopez-4/lab10--PL---SI.git
# Partner 1: Pierce Lopez
# Partner 2: Solomiia Ivanovska

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):  # 3 assertions
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, -1), -2)
        self.assertEqual(add(-2, 5), 3)

    def test_subtract(self):  # 3 assertions
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(-1, -1), 0)
        self.assertEqual(subtract(3, 5), -2)

  ## PARTNER 1 
    def test_multiply(self):
            self.assertEqual(multiply(4, 5), 20)  # Standard case
            self.assertEqual(multiply(-3, 7), -21)  # Handling negatives
            self.assertEqual(multiply(0, 10), 0)  # Zero multiplication

    def test_divide(self):
            self.assertEqual(div(10, 2), 5)  # Basic division
            self.assertEqual(div(-20, 5), -4)  # Negative number division
            self.assertRaises(ZeroDivisionError, div, 8, 0)  # Division by zero




    ######## Partner 2
    def test_divide_by_zero(self):  # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)

    def test_logarithm(self):  # 3 assertions
        self.assertAlmostEqual(logarithm(100, 10), 2)
        self.assertAlmostEqual(logarithm(8, 2), 3)
        self.assertAlmostEqual(logarithm(1, 10), 0)

    def test_log_invalid_base(self):  # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(10, 1)
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self):
        # Logarithm function should raise an error for non-positive values
        with self.assertRaises(ValueError):
            math.log(0, 5)  # Logarithm of zero is invalid

    def test_hypotenuse(self):
        # Testing the hypotenuse function
        self.assertAlmostEqual(math.hypot(3, 4), 5)  # Basic Pythagorean triple
        self.assertAlmostEqual(math.hypot(6, 8), 10)  # Another Pythagorean case
        self.assertAlmostEqual(math.hypot(0, 5), 5)  # Edge case with zero

    def test_sqrt(self):
        # Square root function should raise an error for negative values
        with self.assertRaises(ValueError):
            math.sqrt(-1)  # Square root of negative number is invalid

        # Basic function tests
        self.assertEqual(math.sqrt(4), 2)  # Perfect square
        self.assertAlmostEqual(math.sqrt(2), 1.41421356237, places=10)  # Approximate value for √2

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()