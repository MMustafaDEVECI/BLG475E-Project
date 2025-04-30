def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    start, end = min(a, b), max(a, b)
    return [i for i in range(start, end + 1) if i in range(0, 10) and i % 2 == 0]

import unittest

class TestGenerateIntegers(unittest.TestCase):

    def test_full_single_digit_range(self):
        self.assertEqual(generate_integers(0, 9), [0, 2, 4, 6, 8])

    def test_same_number_even(self):
        self.assertEqual(generate_integers(4, 4), [4])

    def test_same_number_odd(self):
        self.assertEqual(generate_integers(5, 5), [])

if __name__ == '__main__':
    unittest.main()
