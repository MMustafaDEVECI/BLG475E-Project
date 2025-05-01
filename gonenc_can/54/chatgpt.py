import unittest

def same_chars(s0: str, s1: str) -> bool:
    return set(s0) == set(s1)

class TestSameChars(unittest.TestCase):
    
    def test_true_cases(self):
        self.assertTrue(same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc'))
        self.assertTrue(same_chars('abcd', 'dddddddabc'))
        self.assertTrue(same_chars('dddddddabc', 'abcd'))

    def test_false_cases(self):
        self.assertFalse(same_chars('eabcd', 'dddddddabc'))
        self.assertFalse(same_chars('abcd', 'dddddddabcf'))
        self.assertFalse(same_chars('eabcdzzzz', 'dddzzzzzzzddddabc'))
        self.assertFalse(same_chars('aabb', 'aaccc'))
        self.assertFalse(same_chars('', 'a'))
        self.assertFalse(same_chars('a', ''))
    
    def test_empty_strings(self):
        self.assertTrue(same_chars('', ''))
    
    def test_identical_strings(self):
        self.assertTrue(same_chars('abc', 'abc'))
        self.assertTrue(same_chars('aaaa', 'a'))

if __name__ == '__main__':
    unittest.main()
