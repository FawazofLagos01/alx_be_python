import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition_positive(self):
        """Test the addition method."""
        result = self.calc.add(2, 3)
        self.assertEqual(result, 5)

    def test_add_negative(self):
        """Test the addition method"""
        self.assertEqual(self.calc.add(-1, 1), 0)
    
    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(4, 3), 1)
        self.assertEqual(self.calc.subtract(5, 10), -5)
        self.assertEqual(self.calc.subtract(0, 2), -2)
    
    def test_multiplication(self):
        """Test the Multiplication method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(100, 0), 0)
        self.assertEqual(self.calc.multiply(250, -4), -1000)
        self.assertEqual(self.calc.multiply(-10, -4), 40)
        self.assertEqual(self.calc.multiply(30, 1), 30)

    def test_division_by_normal_operation(self):
        """Test the division method by normal numbers."""
        self.assertEqual(self.calc.divide(4, 2), 2)
        self.assertEqual(self.calc.divide(-10, 5), -2)
        self.assertEqual(self.calc.divide(20, 8), 2.50)

    def test_division_by_zero(self):
        """Test division by zero returns None."""
        self.assertIsNone(self.calc.divide(10,0))
        self.assertIsNone(self.calc.divide(0, 0))

if __name__ == "__main__":
    unittest.main()