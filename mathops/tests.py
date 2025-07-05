#from django.test import TestCase
import unittest
from .multiply import multiply

# Create your tests here.
class MultiplyTestCase(unittest.TestCase):
    def test_multiply_1x1(self):
        self.assertEqual(multiply(1, 1), 1)

    def test_multiply_2x2(self):
        self.assertEqual(multiply(2, 2), 4)

    def test_multiply_3x3(self):
        self.assertEqual(multiply(3, 3), 9)

    def test_multiply_4x4(self):
        self.assertEqual(multiply(4, 4), 16)

    def test_multiply_23x45(self):
        self.assertEqual(multiply(23, 45), 1035)

if __name__ == '__main__':
    unittest.main()        