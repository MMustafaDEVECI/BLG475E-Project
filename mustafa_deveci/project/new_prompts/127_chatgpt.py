def is_prime(n):
    """Check if a number is a prime number."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def intersection(interval1, interval2):
    """
    Given two closed intervals (start, end), determine if the length of their
    intersection is a prime number.
    Return "YES" if it is, otherwise return "NO".
    """
    start1, end1 = interval1
    start2, end2 = interval2

    # Calculate intersection
    inter_start = max(start1, start2)
    inter_end = min(end1, end2)

    if inter_start > inter_end:
        return "NO"  # No intersection

    intersection_length = inter_end - inter_start + 1
    return "YES" if is_prime(intersection_length) else "NO"

import unittest

class TestIntersection(unittest.TestCase):

    def test_intersection_with_prime_length(self): 
        self.assertEqual(intersection([1, 5], [4, 8]), "YES")  

    def test_intersection_with_non_prime_length(self): 
        self.assertEqual(intersection([1, 5], [2, 7]), "NO")  

    def test_no_intersection(self):
        self.assertEqual(intersection([1, 3], [4, 6]), "NO")  # No intersection

    def test_intersection_with_prime_length_at_edge(self): 
        self.assertEqual(intersection([1, 5], [5, 8]), "NO")  

    def test_identical_intervals(self):
        self.assertEqual(intersection([2, 6], [2, 6]), "YES")  
    
    def test_non_divisible_by_2_non_prime_length(self):
        self.assertEqual(intersection([1, 15], [7, 16]), "NO")

if __name__ == '__main__':
    unittest.main()