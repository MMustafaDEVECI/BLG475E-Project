import unittest

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    def is_prime(k):
        if k < 2:
            return False
        for i in range(2, k - 1):
            if k % i == 0:
                return False
        return True
    largest = 1
    for j in range(2, n + 1):
        if n % j == 0 and is_prime(j):
            largest = max(largest, j)
    return largest

class TestLargestPrimeFactor(unittest.TestCase):
    def test_largest_prime_factor(self):
        self.assertEqual(largest_prime_factor(15), 5)
        self.assertEqual(largest_prime_factor(27), 3)
        self.assertEqual(largest_prime_factor(63), 7)
        self.assertEqual(largest_prime_factor(330), 11)
        self.assertEqual(largest_prime_factor(13195), 29)
        self.assertEqual(largest_prime_factor(2048), 2)
        self.assertEqual(largest_prime_factor(10), 5)
        self.assertEqual(largest_prime_factor(100), 5)
        self.assertEqual(largest_prime_factor(17*19), 19)
        self.assertEqual(largest_prime_factor(2*3*5*7*11), 11)

if __name__ == '__main__':
    unittest.main()
