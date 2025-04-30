def choose_num(x, y):
    """
    This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if x > y:
        return -1
    
    # Start from y and go down to x, return the first even number found
    for num in range(y, x - 1, -1):
        if num % 2 == 0:
            return num
    return -1

import unittest

class TestChooseNum(unittest.TestCase):

    def test_even_in_range(self):
        self.assertEqual(choose_num(12, 15), 14)  # Even number 14 is in the range

    def test_x_greater_than_y(self):
        self.assertEqual(choose_num(13, 12), -1)  # Invalid range, should return -1

    def test_no_even_in_range(self):
        self.assertEqual(choose_num(11, 13), 12)  # 12 is even, in range

if __name__ == '__main__':
    unittest.main()
