import unittest
from codesGPT import *

class TestParseNestedParens(unittest.TestCase):
    def test_mixed_depths(self):
        # Multiple groups with varying levels of nesting
        self.assertEqual(parse_nested_parens('(()()) ((())) () ((())()())'), [2, 3, 1, 3])

    def test_deep_nesting(self):
        # Single group with deep nesting
        self.assertEqual(parse_nested_parens('(((((())))))'), [6])

    def test_empty_string(self):
        # Edge case: no input
        self.assertEqual(parse_nested_parens(''), [])

    def test_unbalanced_assumed_balanced(self):
        # Boundary assumption: input always balanced, but we test partial string
        self.assertEqual(parse_nested_parens('(()'), [2])

    def test_single_group_no_nesting(self):
        # Minimal valid nesting
        self.assertEqual(parse_nested_parens('()'), [1])

class TestCountDistinctCharacters(unittest.TestCase):
    def test_empty(self):
        # Edge case: empty string
        self.assertEqual(count_distinct_characters(''), 0)

    def test_case_insensitivity(self):
        # Upper and lower case treated the same
        self.assertEqual(count_distinct_characters('AaBb'), 2)

    def test_all_same(self):
        # All characters are the same
        self.assertEqual(count_distinct_characters('aaaaAAA'), 1)

    def test_unique_characters(self):
        # Each character is unique
        self.assertEqual(count_distinct_characters('abcde'), 5)

    def test_spaces_and_letters(self):
        # Include whitespace in test
        self.assertEqual(count_distinct_characters('A A A'), 2)  # 'a' and ' ' (space)


class TestFilterIntegers(unittest.TestCase):
    def test_empty_list(self):
        # Edge case: empty input
        self.assertEqual(filter_integers([]), [])

    def test_no_integers(self):
        # List has no integers
        self.assertEqual(filter_integers(['x', {}, 3.14]), [])

    def test_only_integers(self):
        # All valid integers
        self.assertEqual(filter_integers([1, 2, 3]), [1, 2, 3])

    def test_mixed_types(self):
        # Mix of types
        self.assertEqual(filter_integers(['a', 1, 2.0, 3]), [1, 3])

    def test_nested_structure(self):
        # Integers inside containers should not be matched
        self.assertEqual(filter_integers([[], [1], {1: 2}, 7]), [7])

class TestStrlen(unittest.TestCase):
    def test_empty_string(self):
        # Edge case: empty string
        self.assertEqual(strlen(''), 0)

    def test_single_char(self):
        # Smallest non-empty input
        self.assertEqual(strlen('x'), 1)

    def test_spaces(self):
        # Spaces count as characters
        self.assertEqual(strlen('   '), 3)

    def test_unicode_chars(self):
        # Unicode emoji counts as one char
        self.assertEqual(strlen('😀😃😄'), 3)

    def test_long_string(self):
        # Long input string
        self.assertEqual(strlen('a' * 1000), 1000)


class TestFilterByPrefix(unittest.TestCase):
    def test_empty_list(self):
        # Edge case: no input strings
        self.assertEqual(filter_by_prefix([], 'a'), [])

    def test_no_matches(self):
        # None of the strings match prefix
        self.assertEqual(filter_by_prefix(['bob', 'car', 'delta'], 'x'), [])

    def test_some_matches(self):
        # Mixed results
        self.assertEqual(filter_by_prefix(['apple', 'banana', 'apricot'], 'ap'), ['apple', 'apricot'])

    def test_case_sensitive(self):
        # Prefix is case-sensitive
        self.assertEqual(filter_by_prefix(['Apple', 'apple'], 'Ap'), ['Apple'])

    def test_empty_prefix(self):
        # Every string matches an empty prefix
        self.assertEqual(filter_by_prefix(['a', 'b', 'c'], ''), ['a', 'b', 'c'])


class TestIsPrime(unittest.TestCase):
    def test_less_than_two(self):
        # Edge cases: 0 and 1 are not prime
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))

    def test_two(self):
        # Smallest and only even prime
        self.assertTrue(is_prime(2))

    def test_small_composite(self):
        # Composite with small factor
        self.assertFalse(is_prime(9))  # 3*3

    def test_large_prime(self):
        # A known large prime
        self.assertTrue(is_prime(7919))

    def test_large_composite(self):
        # A large non-prime
        self.assertFalse(is_prime(7920))

class TestCarRaceCollision(unittest.TestCase):
    def test_zero_cars(self):
        # Edge case: no cars
        self.assertEqual(car_race_collision(0), 0)

    def test_single_car(self):
        # Smallest case of one car each direction
        self.assertEqual(car_race_collision(1), 1)

    def test_typical_case(self):
        # Normal test
        self.assertEqual(car_race_collision(4), 16)

    def test_larger_case(self):
        # Larger input to verify square calculation
        self.assertEqual(car_race_collision(100), 10000)

    def test_negative_input(self):
        # Boundary case: negative input should ideally be 0 (if allowed)
        self.assertEqual(car_race_collision(-5), 25)  # If not clamped, (-5)^2 = 25


class TestPairsSumToZero(unittest.TestCase):
    def test_empty_list(self):
        # Edge case: nothing to pair
        self.assertFalse(pairs_sum_to_zero([]))

    def test_single_zero(self):
        # A single zero can't pair with itself
        self.assertFalse(pairs_sum_to_zero([0]))

    def test_positive_negative_pair(self):
        # Basic positive and negative pair
        self.assertTrue(pairs_sum_to_zero([2, -2]))

    def test_all_positives(self):
        # No negatives to cancel out
        self.assertFalse(pairs_sum_to_zero([1, 2, 3]))

    def test_zero_pair(self):
        # Two zeros make a valid pair summing to zero
        self.assertTrue(pairs_sum_to_zero([0, 0]))


class TestTriangleArea(unittest.TestCase):
    def test_typical_case(self):
        # Standard triangle
        self.assertEqual(triangle_area(5, 3), 7.5)

    def test_zero_height(self):
        # Edge: zero height results in zero area
        self.assertEqual(triangle_area(10, 0), 0.0)

    def test_zero_base(self):
        # Edge: zero base results in zero area
        self.assertEqual(triangle_area(0, 10), 0.0)

    def test_float_input(self):
        # Valid floats
        self.assertAlmostEqual(triangle_area(4.5, 2), 4.5)

    def test_large_input(self):
        # Large base/height
        self.assertEqual(triangle_area(10000, 5000), 25000000.0)


class TestDecodeShift(unittest.TestCase):
    def test_identity(self):
        # Encode then decode yields original
        self.assertEqual(decode_shift(encode_shift('hello')), 'hello')

    def test_empty_string(self):
        # Edge: no characters
        self.assertEqual(decode_shift(''), '')

    def test_wraparound(self):
        # 'z' shifted by 5 wraps to 'e'
        self.assertEqual(decode_shift('e'), 'z')

    def test_all_letters(self):
        # Full alphabet test
        import string
        original = string.ascii_lowercase
        encoded = encode_shift(original)
        decoded = decode_shift(encoded)
        self.assertEqual(decoded, original)

    def test_repeated_characters(self):
        # Same character repeated
        self.assertEqual(decode_shift(encode_shift('aaaaa')), 'aaaaa')

if __name__ == '__main__':
    unittest.main()