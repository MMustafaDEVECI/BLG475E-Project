def is_sorted(lst):
    '''
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers and only integers.

    Examples:
    is_sorted([5]) ➞ True
    is_sorted([1, 2, 3, 4, 5]) ➞ True
    is_sorted([1, 3, 2, 4, 5]) ➞ False
    is_sorted([1, 2, 3, 4, 5, 6]) ➞ True
    is_sorted([1, 2, 3, 4, 5, 6, 7]) ➞ True
    is_sorted([1, 3, 2, 4, 5, 6, 7]) ➞ False
    is_sorted([1, 2, 2, 3, 3, 4]) ➞ True
    is_sorted([1, 2, 2, 2, 3, 4]) ➞ False
    '''
    from collections import Counter

    count_digit = Counter(lst)

    # Check if any number appears more than twice
    if any(count > 2 for count in count_digit.values()):
        return False

    # Check if the list is sorted in ascending order
    return all(lst[i - 1] <= lst[i] for i in range(1, len(lst)))

import unittest

class TestIsSorted(unittest.TestCase):

    def test_sorted_with_no_duplicates(self):
        self.assertTrue(is_sorted([1, 2, 3, 4, 5]))

    def test_sorted_with_allowed_duplicates(self):
        self.assertTrue(is_sorted([1, 2, 2, 3, 3, 4]))

    def test_sorted_with_more_than_two_duplicates(self):
        self.assertFalse(is_sorted([1, 2, 2, 2, 3, 4]))

if __name__ == '__main__':
    unittest.main()