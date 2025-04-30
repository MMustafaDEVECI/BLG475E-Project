def sort_array(arr):
    """
    Sort an array of integers based on:
    1. Number of 1s in the binary representation (ascending)
    2. For same number of 1s, sort by decimal value (ascending)
    
    Negative numbers are sorted by decimal value alone, as their binary
    representations in Python are not straightforwardly comparable.

    Examples:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) == [0, 1, 2, 3, 4]
    """
    return sorted(arr, key=lambda x: (bin(x).count('1') if x >= 0 else float('inf'), x))

import unittest

class TestSortArray(unittest.TestCase):

    def test_basic_case(self): #assertion error
        self.assertEqual(sort_array([1, 5, 2, 3, 4]), [1, 2, 3, 4, 5])

    def test_negative_numbers(self): 
        self.assertEqual(sort_array([-2, -3, -4, -5, -6]), [-6, -5, -4, -3, -2])

    def test_mixed_positive_and_negative(self): # assertion error
        self.assertEqual(sort_array([1, 0, 2, 3, 4, -1, -2]), [0, 1, 2, 3, 4, -2, -1])

    def test_edge_case_with_zero(self): # assertetion error
        self.assertEqual(sort_array([0, 0, 1, 1, 2, 3, 4]), [0, 0, 1, 1, 2, 3, 4])

if __name__ == '__main__':
    unittest.main()
