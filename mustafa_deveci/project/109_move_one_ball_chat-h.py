def move_one_ball(arr):
    """
    Determines if the given array can be sorted into non-decreasing order
    by performing any number of right shift operations.

    A right shift means the last element becomes the first, and all others
    move one step to the right.

    Returns True if possible, False otherwise.
    """
    if not arr:
        return True

    n = len(arr)
    count = 0

    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            count += 1
            pivot = i

    if count == 0:
        return True  # already sorted
    if count > 1:
        return False  # more than one drop — can't be fixed with a rotation

    # check if rotated array from pivot is sorted
    rotated = arr[pivot:] + arr[:pivot]
    return rotated == sorted(arr)

import unittest

class TestMoveOneBall(unittest.TestCase):

    def test_already_sorted(self):
        self.assertTrue(move_one_ball([1, 2, 3, 4, 5]))

    def test_single_rotation_needed(self):
        self.assertTrue(move_one_ball([4, 5, 1, 2, 3]))

    def test_unsortable_by_rotation(self):
        self.assertFalse(move_one_ball([3, 1, 4, 2, 5]))

    def test_empty_list(self):
        self.assertTrue(move_one_ball([]))

    def test_single_element(self):
        self.assertTrue(move_one_ball([7]))

if __name__ == '__main__':
    unittest.main()
