import unittest

def iscube(a):
    '''
    Write a function that takes an integer a and returns True 
    if this ingeger is a cube of some integer number.
    Note: you may assume the input is always valid.
    Examples:
    iscube(1) ==> True
    iscube(2) ==> False
    iscube(-1) ==> True
    iscube(64) ==> True
    iscube(0) ==> True
    iscube(180) ==> False
    '''
    a = abs(a)
    return int(round(a ** (1. / 3))) ** 3 == a

class TestIsCube(unittest.TestCase):
    
    def test_positive_cubes(self):
        self.assertTrue(iscube(1))
        self.assertTrue(iscube(64))
        self.assertTrue(iscube(1000))
        self.assertTrue(iscube(27))
        self.assertTrue(iscube(8))
        
    def test_negative_cubes(self):
        self.assertTrue(iscube(-1))
        self.assertTrue(iscube(-8))
        self.assertTrue(iscube(-27))
        self.assertTrue(iscube(-64))
        
    def test_non_cubes(self):
        self.assertFalse(iscube(2))
        self.assertFalse(iscube(180))
        self.assertFalse(iscube(1729))
        self.assertFalse(iscube(99))
        
def test_edge_cases(self):
    self.assertTrue(iscube(0))
    self.assertTrue(iscube(-0))
    self.assertTrue(iscube(1728))  # Fixed: 12^3 = 1728, now correctly expects True
        
    def test_large_numbers(self):
        self.assertTrue(iscube(1000000))  # 100^3
        self.assertFalse(iscube(1000001))
        self.assertTrue(iscube(-1000000))
        self.assertFalse(iscube(-1000001))

if __name__ == '__main__':
    unittest.main()
