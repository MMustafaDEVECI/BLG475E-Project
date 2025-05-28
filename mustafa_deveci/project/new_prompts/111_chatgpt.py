from collections import Counter

def histogram(test):
    """
    Given a string of space-separated lowercase letters, return a dictionary 
    containing the letter(s) that appear most frequently along with their counts.
    If multiple letters have the same highest frequency, include all of them.
    Return an empty dictionary if the input is empty or only whitespace.
    """
    if not test.strip():
        return {}

    # Split into letters and count occurrences
    letters = test.split()
    freq = Counter(letters)

    # Find the maximum frequency
    max_freq = max(freq.values())

    # Return only the letters with the highest frequency
    return {letter: count for letter, count in freq.items() if count == max_freq}

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

