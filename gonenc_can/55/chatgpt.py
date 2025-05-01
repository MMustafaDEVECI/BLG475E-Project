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


# Unit tests
import unittest

class TestFib(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(fib(10), 55)
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(8), 21)

    def test_additional(self):
        self.assertEqual(fib(11), 89)
        self.assertEqual(fib(12), 144)

    def test_edge_cases(self):
        self.assertEqual(fib(0), 0)
        self.assertEqual(fib(2), 1)
        self.assertEqual(fib(3), 2)

if __name__ == "__main__":
    unittest.main()
