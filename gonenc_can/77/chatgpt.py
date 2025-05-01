import math
import unittest

def iscube(a):
    '''
    Write a function that takes an integer a and returns True 
    if this integer is a cube of some integer number.
    Note: you may assume the input is always valid.
    Examples:
    iscube(1) ==> True
    iscube(2) ==> False
    iscube(-1) ==> True
    iscube(64) ==> True
    iscube(0) ==> True
    iscube(180) ==> False
    '''
    a_abs = abs(a)
    return int(round(a_abs ** (1. / 3))) ** 3 == a_abs

class TestIsCube(unittest.TestCase):
    def test_simple_cases(self):
        self.assertTrue(iscube(1), "First test error")
        self.assertFalse(iscube(2), "Second test error")
        self.assertTrue(iscube(-1), "Third test error")
        self.assertTrue(iscube(64), "Fourth test error")
        self.assertFalse(iscube(180), "Fifth test error")
        self.assertTrue(iscube(1000), "Sixth test error")

    def test_edge_cases(self):
        self.assertTrue(iscube(0), "1st edge test error")
        self.assertFalse(iscube(1729), "2nd edge test error")

if __name__ == "__main__":
    unittest.main()
