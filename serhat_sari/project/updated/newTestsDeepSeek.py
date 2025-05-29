import unittest
from codesDeepSeek import *

class TestParseNestedParens(unittest.TestCase):
    def test_mixed_nesting(self):
        # Test with maximum depth at different positions
        self.assertEqual(parse_nested_parens('((())) () (()())'), [3, 1, 2])
    def test_single_parentheses(self):
        # Test with single parenthesis
        self.assertEqual(parse_nested_parens('( )'), [1, 0])
    def test_empty_groups(self):
        # Test with empty groups
        self.assertEqual(parse_nested_parens('() () ()'), [1, 1, 1])
    def test_unbalanced_input(self):
        # Test with unbalanced parentheses (should still work)
        self.assertEqual(parse_nested_parens('(()()'), [2])

class TestCountDistinctCharacters(unittest.TestCase):
    def test_mixed_case_unicode(self):
        # Test with mixed case unicode characters
        self.assertEqual(count_distinct_characters('äÄ'), 1)
    def test_non_alphabetic(self):
        # Test with only non-alphabetic characters
        self.assertEqual(count_distinct_characters('123!@#'), 0)
        # Test with whitespace characters
    def test_whitespace_characters(self):
        self.assertEqual(count_distinct_characters('a b c'), 3)
        # Test with maximum ASCII characters
    def test_max_ascii(self):
        self.assertEqual(count_distinct_characters('\x00\x7F'), 2)

class TestFilterIntegers(unittest.TestCase):
    def test_large_integers(self):
        # Test with large integers
        self.assertEqual(filter_integers([2**64, 'x']), [18446744073709551616])
        # Test with boolean values (should be filtered out)
    def test_booleans_filtered(self):
        self.assertEqual(filter_integers([True, False]), [])
        # Test with mixed numeric types
    def test_mixed_numeric_types(self):
        self.assertEqual(filter_integers([1, 1.0, '1']), [1])
    def test_large_list(self):
        # Test with very large list
        self.assertEqual(len(filter_integers([i if i%2 else str(i) for i in range(1000)])), 500)

class TestStrlen(unittest.TestCase):
    def test_unicode_char(self):
        # Test with unicode characters
        self.assertEqual(strlen('ñ'), 1)
    def test_very_long_string(self):
        # Test with very long string
        self.assertEqual(strlen('a'*1000000), 1000000)
    def test_special_characters(self):
        # Test with special characters
        self.assertEqual(strlen('\n\t\r'), 3)
    def test_zero_width_characters(self):
        # Test with zero-width characters
        self.assertEqual(strlen('a\u200bb'), 2)

class TestFilterByPrefix(unittest.TestCase):
    def test_empty_prefix(self):
        # Test with empty prefix
        self.assertEqual(filter_by_prefix(['a', 'b', 'c'], ''), ['a', 'b', 'c'])
    def test_whitespace_prefix(self):
        # Test with whitespace prefix
        self.assertEqual(filter_by_prefix([' a', 'a'], ' '), [' a'])
    def test_unicode_prefix(self):
        # Test with unicode prefix
        self.assertEqual(filter_by_prefix(['ñame', 'name'], 'ñ'), ['ñame'])
    def test_very_long_prefix(self):
        # Test with very long prefix
        self.assertEqual(filter_by_prefix(['a'*1000, 'b'*1000], 'a'*999), ['a'*1000])

class TestCarRaceCollision(unittest.TestCase):
    def test_large_numbers(self):
        # Test with very large n
        self.assertEqual(car_race_collision(10**6), 10**12)
    def test_negative_element(self):
        # Test with negative n (should raise error)
        with self.assertRaises(ValueError):
            car_race_collision(-1)
    def test_all_zeros(self):
        # Test with zero cars
        self.assertEqual(car_race_collision(0), 0)
    def test_max_min_int(self):
        # Test with maximum integer value
        self.assertEqual(car_race_collision(2**31-1), (2**31-1)**2)

class TestPairsSumToZero(unittest.TestCase):
    def test_large_numbers(self):
        # Test with large numbers
        self.assertTrue(pairs_sum_to_zero([10**6, -10**6, 1]))
    def test_single_element(self):
        # Test with single element
        self.assertFalse(pairs_sum_to_zero([0]))
    def test_all_zeros(self):
        # Test with all zeros
        self.assertTrue(pairs_sum_to_zero([0, 0, 0]))
    def test_max_min_int(self):
        # Test with maximum integer values
        self.assertTrue(pairs_sum_to_zero([2**31-1, -(2**31-1)]))

class TestTriangleArea(unittest.TestCase):
    def test_very_large_dimensions(self):
        # Test with very large dimensions
        self.assertEqual(triangle_area(1e300, 1e300), 5e599)
    def test_negative_value(self):
        # Test with negative values (should raise error)
        with self.assertRaises(ValueError):
            triangle_area(-1, 5)
    def test_zero_height(self):
        # Test with zero height
        self.assertEqual(triangle_area(10, 0), 0.0)
    def test_floating_precision(self):
        # Test with floating point precision
        self.assertAlmostEqual(triangle_area(0.1, 0.1), 0.005)

class TestEncodeDecodeShift(unittest.TestCase):
    def test_non_alpha_characters(self):
        # Test with non-alphabetic characters
        self.assertEqual(encode_shift('123!@#'), '123!@#')
    def test_empty_string(self):
        # Test with empty string
        self.assertEqual(encode_shift(''), '')
    def test_full_alphabet_roundtrip(self):
        # Test with all letters
        self.assertEqual(decode_shift(encode_shift('abcdefghijklmnopqrstuvwxyz')), 
                         'abcdefghijklmnopqrstuvwxyz')
    def test_very_long_string_roundtrip(self):
        # Test with very long string
        long_str = 'a'*10000
        self.assertEqual(decode_shift(encode_shift(long_str)), long_str)

class TestIsPrime(unittest.TestCase):
    def test_even_prime(self):
        # Test with even prime
        self.assertTrue(is_prime(2))
    def test_negative_number(self):
        # Test with negative numbers
        self.assertFalse(is_prime(-5))
    def test_float_input(self):
        # Test with floating point numbers (should raise error)
        with self.assertRaises(TypeError):
            is_prime(5.5)
    def test_carmichael_number(self):
        # Test with Carmichael numbers (tough cases)
        self.assertFalse(is_prime(561))  # 561 is a Carmichael number

if __name__ == '__main__':
    unittest.main()