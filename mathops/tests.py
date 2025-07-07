#from django.test import TestCase
import unittest
from .multiply import multiply


class MultiplyTestCase(unittest.TestCase):
    def test_multiply_1x1(self):
        result = multiply(1, 1)
        print(f"Multiplying 1 by 1 → should return 1 → Got: {result}")
        self.assertEqual(result, 1)

    def test_multiply_2x2(self):
        result = multiply(2, 2)
        print(f"Multiplying 2 by 2 → should return 4 → Got: {result}")
        self.assertEqual(result, 4)

    def test_multiply_3x3(self):
        result = multiply(3, 3)
        print(f"Multiplying 3 by 3 → should return 9 → Got: {result}")
        self.assertEqual(result, 9)

    def test_multiply_4x4(self):
        result = multiply(4, 4)
        print(f"Multiplying 4 by 4 → should return 16 → Got: {result}")
        self.assertEqual(result, 16)

    def test_multiply_23x45(self):
        result = multiply(23, 45)
        print(f"Multiplying 23 by 45 → should return 1035 → Got: {result}")
        self.assertEqual(result, 1035)

if __name__ == '__main__':
    unittest.main()        