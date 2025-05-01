import unittest

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

class TestFib(unittest.TestCase):
    def test_fib(self):
        self.assertEqual(fib(0), 0)  # Base case 1
        self.assertEqual(fib(1), 1)  # Base case 2
        self.assertEqual(fib(2), 1)  # Small non-base case
        self.assertEqual(fib(5), 5)  # Medium case
        self.assertEqual(fib(10), 55)  # From prompt example
        self.assertEqual(fib(8), 21)  # From prompt example
        self.assertEqual(fib(11), 89)  # Additional test case
        self.assertEqual(fib(12), 144)  # Additional test case
        self.assertEqual(fib(20), 6765)  # Larger test case

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            fib(-1)
        with self.assertRaises(ValueError):
            fib(-10)

if __name__ == '__main__':
    unittest.main()
