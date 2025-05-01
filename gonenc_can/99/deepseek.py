import unittest
from math import floor, ceil

def closest_integer(value):
    '''
    Create a function that takes a value (string) representing a number
    and returns the closest integer to it. If the number is equidistant
    from two integers, round it away from zero.

    Examples
    >>> closest_integer("10")
    10
    >>> closest_integer("15.3")
    15

    Note:
    Rounding away from zero means that if the given number is equidistant
    from two integers, the one you should return is the one that is the
    farthest from zero. For example closest_integer("14.5") should
    return 15 and closest_integer("-14.5") should return -15.
    '''
    if value.count('.') == 1:
        # remove trailing zeros
        while (value[-1] == '0'):
            value = value[:-1]

    num = float(value)
    if value[-2:] == '.5':
        if num > 0:
            res = ceil(num)
        else:
            res = floor(num)
    elif len(value) > 0:
        res = int(round(num))
    else:
        res = 0

    return res

class TestClosestInteger(unittest.TestCase):
    def test_integer(self):
        self.assertEqual(closest_integer("10"), 10)
    
    def test_round_up_positive(self):
        self.assertEqual(closest_integer("14.5"), 15)
    
    def test_round_down_negative(self):
        self.assertEqual(closest_integer("-15.5"), -16)
    
    def test_round_down_positive(self):
        self.assertEqual(closest_integer("15.3"), 15)
    
    def test_zero(self):
        self.assertEqual(closest_integer("0"), 0)
    
    def test_round_up_negative(self):
        self.assertEqual(closest_integer("-14.5"), -15)
    
    def test_trailing_zeros(self):
        self.assertEqual(closest_integer("14.500"), 15)
    
    def test_small_positive(self):
        self.assertEqual(closest_integer("0.1"), 0)
    
    def test_small_negative(self):
        self.assertEqual(closest_integer("-0.1"), 0)
    
    def test_large_positive(self):
        self.assertEqual(closest_integer("123456789.999"), 123456790)
    
    def test_large_negative(self):
        self.assertEqual(closest_integer("-123456789.999"), -123456790)

if __name__ == '__main__':
    unittest.main()
