import unittest
from src.utils import add, subtract, multiply, divide, reverse_string, is_palindrome

class TestUtils(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        with self.assertRaises(ValueError):
            divide(1, 0)

    def test_reverse_string(self):
        self.assertEqual(reverse_string('abc'), 'cba')

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome('racecar'))
        self.assertFalse(is_palindrome('python'))

if __name__ == '__main__':
    unittest.main()