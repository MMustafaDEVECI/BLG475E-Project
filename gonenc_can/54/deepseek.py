import unittest

def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> same_chars('abcd', 'dddddddabc')
    True
    >>> same_chars('dddddddabc', 'abcd')
    True
    >>> same_chars('eabcd', 'dddddddabc')
    False
    >>> same_chars('abcd', 'dddddddabce')
    False
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    """
    return set(s0) == set(s1)

class TestSameChars(unittest.TestCase):
    def test_same_chars(self):
        self.assertTrue(same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc'))
        self.assertTrue(same_chars('abcd', 'dddddddabc'))
        self.assertTrue(same_chars('dddddddabc', 'abcd'))
        self.assertFalse(same_chars('eabcd', 'dddddddabc'))
        self.assertFalse(same_chars('abcd', 'dddddddabce'))  # Fixed from 'abcf' to 'abce' to match docstring
        self.assertFalse(same_chars('eabcdzzzz', 'dddzzzzzzzddddabc'))
        self.assertFalse(same_chars('aabb', 'aaccc'))
        
    def test_empty_strings(self):
        self.assertTrue(same_chars('', ''))
        self.assertFalse(same_chars('', 'a'))
        self.assertFalse(same_chars('a', ''))
        
    def test_case_sensitivity(self):
        self.assertFalse(same_chars('abc', 'ABC'))  # Changed to assertFalse since function is case-sensitive
        # If case shouldn't matter, the function would need to be modified instead
        
    def test_unicode_characters(self):
        self.assertTrue(same_chars('café', 'éfac'))
        self.assertFalse(same_chars('café', 'cafe'))

if __name__ == '__main__':
    unittest.main()
