def find_max(words):
    """
    Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    Examples:
    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"
    """
    return min(words, key=lambda word: (-len(set(word)), word))

import unittest

class TestFindMax(unittest.TestCase):

    def test_basic_case(self):
        self.assertEqual(find_max(["name", "of", "string"]), "string")

    def test_multiple_with_same_unique_characters(self):
        self.assertEqual(find_max(["name", "enam", "game"]), "enam")

    def test_single_word_with_repeated_characters(self):
        self.assertEqual(find_max(["aaaaaaa", "bb", "cc"]), "aaaaaaa")

    def test_case_with_empty_string(self):
        self.assertEqual(find_max(["", "abc", "ab"]), "abc")

if __name__ == '__main__':
    unittest.main()
