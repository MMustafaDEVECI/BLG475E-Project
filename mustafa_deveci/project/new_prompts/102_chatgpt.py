def choose_num(x, y):
    """
    This function takes two positive numbers x and y and returns the
    biggest even integer that is in the range [x, y] inclusive.
    If there's no such number or x > y, then the function returns -1.
    """
    if x > y:
        return -1

    # Start from y and go down until we find an even number
    if y % 2 == 0:
        return y
    elif y - 1 >= x:
        return y - 1
    else:
        return -1

import unittest

class TestChooseNum(unittest.TestCase):

    def test_even_in_range(self):
        self.assertEqual(choose_num(12, 15), 14)  # Even number 14 is in the range

    def test_x_greater_than_y(self):
        self.assertEqual(choose_num(13, 12), -1)  # Invalid range, should return -1

    def test_no_even_in_range(self):
        self.assertEqual(choose_num(11, 13), 12)  # 12 is even, in range
        
    def test_no_even_number(self):
        self.assertEqual(choose_num(11, 11), -1) # NEW TEST

    def test_even_at_y(self):
        self.assertEqual(choose_num(10, 20), 20) # NEW TEST

if __name__ == '__main__':
    unittest.main()