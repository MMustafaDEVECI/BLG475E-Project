import unittest
from codesGPT import *

class TestParseNestedParens(unittest.TestCase):
    def test_mixed(self):
        self.assertEqual(parse_nested_parens('(()()) ((())) () ((())()())'), [2, 3, 1, 3])
    def test_increasing(self):
        self.assertEqual(parse_nested_parens('() (()) ((())) (((())))'), [1, 2, 3, 4])
    def test_single_group(self):
        self.assertEqual(parse_nested_parens('(()(())((())))'), [4])
    def test_empty_string(self):
        self.assertEqual(parse_nested_parens(''), [])
    def test_irregular_spacing(self):
        self.assertEqual(parse_nested_parens(' ((()))   () '), [3, 1])

class TestCountDistinctCharacters(unittest.TestCase):
    def test_lower_and_upper(self):
        self.assertEqual(count_distinct_characters('AaBbCc'), 3)
    def test_all_same(self):
        self.assertEqual(count_distinct_characters('aaaa'), 1)
    def test_empty_string(self):
        self.assertEqual(count_distinct_characters(''), 0)
    def test_symbols_and_numbers(self):
        self.assertEqual(count_distinct_characters('abc123!'), 7)
    def test_mixed_case_and_symbols(self):
        self.assertEqual(count_distinct_characters('A!a!'), 2)

class TestFilterIntegers(unittest.TestCase):
    def test_mixed_types(self):
        self.assertEqual(filter_integers(['a', 1, 2.5, 3]), [1, 3])
    def test_all_integers(self):
        self.assertEqual(filter_integers([1, 2, 3]), [1, 2, 3])
    def test_no_integers(self):
        self.assertEqual(filter_integers(['1', 3.0, None]), [])
    def test_empty_list(self):
        self.assertEqual(filter_integers([]), [])
    def test_negative_and_zero(self):
        self.assertEqual(filter_integers([-1, 0, '0', 5]), [-1, 0, 5])

class TestStrlen(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(strlen(''), 0)
    def test_short_word(self):
        self.assertEqual(strlen('abc'), 3)
    def test_sentence(self):
        self.assertEqual(strlen('hello world'), 11)
    def test_unicode_chars(self):
        self.assertEqual(strlen('你好'), 2)
    def test_only_spaces(self):
        self.assertEqual(strlen('     '), 5)

class TestFilterByPrefix(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(filter_by_prefix([], 'a'), [])
    def test_some_matches(self):
        self.assertEqual(filter_by_prefix(['abc', 'bcd', 'array'], 'a'), ['abc', 'array'])
    def test_all_match(self):
        self.assertEqual(filter_by_prefix(['apple', 'apricot'], 'a'), ['apple', 'apricot'])
    def test_no_match(self):
        self.assertEqual(filter_by_prefix(['banana', 'grape'], 'z'), [])
    def test_empty_prefix(self):
        self.assertEqual(filter_by_prefix(['x', 'y'], ''), ['x', 'y'])

class TestIsPrime(unittest.TestCase):
    def test_small_non_prime(self):
        self.assertFalse(is_prime(1))  # edge case: less than 2

    def test_small_prime(self):
        self.assertTrue(is_prime(5))  # simple prime

    def test_composite_number(self):
        self.assertFalse(is_prime(85))  # 5 * 17

    def test_large_prime(self):
        self.assertTrue(is_prime(13441))  # known large prime

    def test_large_non_prime(self):
        self.assertFalse(is_prime(13441 * 19))  # large non-prime

class TestCarRaceCollision(unittest.TestCase):
    def test_two(self):
        self.assertEqual(car_race_collision(2), 4)
    def test_zero(self):
        self.assertEqual(car_race_collision(0), 0)
    def test_negative(self):
        self.assertEqual(car_race_collision(-3), 9)
    def test_large_number(self):
        self.assertEqual(car_race_collision(1000), 1000000)
    def test_one(self):
        self.assertEqual(car_race_collision(1), 1)

class TestPairsSumToZero(unittest.TestCase):
    def test_pair_exists(self):
        self.assertTrue(pairs_sum_to_zero([2, -2, 3]))
    def test_pair_not_exists(self):
        self.assertFalse(pairs_sum_to_zero([1, 2, 3]))
    def test_zero_pair(self):
        self.assertTrue(pairs_sum_to_zero([0, 0]))
    def test_large_list(self):
        self.assertTrue(pairs_sum_to_zero(list(range(1000)) + [-999]))
    def test_single_element(self):
        self.assertFalse(pairs_sum_to_zero([5]))

class TestTriangleArea(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(triangle_area(4, 5), 10.0)
    def test_zero_base(self):
        self.assertEqual(triangle_area(0, 5), 0.0)
    def test_zero_height(self):
        self.assertEqual(triangle_area(5, 0), 0.0)
    def test_negative_base(self):
        self.assertEqual(triangle_area(-3, 6), -9.0)
    def test_float_values(self):
        self.assertAlmostEqual(triangle_area(2.5, 4.2), 5.25)

class TestEncodeDecodeShift(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(decode_shift(encode_shift('hello')), 'hello')
    def test_wraparound(self):
        self.assertEqual(encode_shift('xyz'), 'cde')
    def test_empty_string(self):
        self.assertEqual(decode_shift(encode_shift('')), '')
    def test_single_letter(self):
        self.assertEqual(decode_shift(encode_shift('a')), 'a')
    def test_shift_consistency(self):
        original = 'shiftcipher'
        self.assertEqual(decode_shift(encode_shift(original)), original)

if __name__ == '__main__':
    unittest.main()