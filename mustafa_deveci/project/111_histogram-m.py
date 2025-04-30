from collections import Counter

def histogram(test):
    """
    Given a space-separated string of lowercase letters,
    return a dictionary of the letter(s) with the highest count.
    """
    if not test.strip():
        return {}

    counts = Counter(test.split())
    max_count = max(counts.values())
    return {char: cnt for char, cnt in counts.items() if cnt == max_count}

import unittest

class TestHistogram(unittest.TestCase):

    def test_single_most_frequent(self):
        self.assertEqual(histogram("a b a c a b"), {"a": 3})

    def test_multiple_most_frequent(self):
        self.assertEqual(histogram("a b c a b c"), {"a": 2, "b": 2, "c": 2})

    def test_empty_input(self):
        self.assertEqual(histogram("   "), {})

    def test_single_word(self):
        self.assertEqual(histogram("x"), {"x": 1})

if __name__ == '__main__':
    unittest.main()

