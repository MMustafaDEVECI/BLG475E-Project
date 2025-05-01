import unittest
from codesDeepSeek import *

class TestParseNestedParens(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(parse_nested_parens('(()()) ((())) () ((())()())'), [2, 3, 1, 3])
        self.assertEqual(parse_nested_parens('() (()) ((())) (((())))'), [1, 2, 3, 4])
    
    def test_edge_cases(self):
        self.assertEqual(parse_nested_parens('(()(())((())))'), [4])
        self.assertEqual(parse_nested_parens('()'), [1])
        self.assertEqual(parse_nested_parens(''), [])

class TestCountDistinctCharacters(unittest.TestCase):
    def test_case_insensitive(self):
        self.assertEqual(count_distinct_characters('xyzXYZ'), 3)
        self.assertEqual(count_distinct_characters('Jerry'), 4)
    
    def test_special_cases(self):
        self.assertEqual(count_distinct_characters('aAaaAa'), 1)
        self.assertEqual(count_distinct_characters(''), 0)
        self.assertEqual(count_distinct_characters('abc123ABC'), 6)

class TestFilterIntegers(unittest.TestCase):
    def test_mixed_types(self):
        self.assertEqual(filter_integers(['a', 3.14, 5]), [5])
        self.assertEqual(filter_integers([1, 2, 3, 'abc', {}, []]), [1, 2, 3])
    
    def test_edge_cases(self):
        self.assertEqual(filter_integers([]), [])
        self.assertEqual(filter_integers([10, '20', 30.5]), [10])

class TestStrlen(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(strlen(''), 0)
        self.assertEqual(strlen('abc'), 3)
        self.assertEqual(strlen('hello world'), 11)
    
    def test_special_cases(self):
        self.assertEqual(strlen('12345'), 5)
        self.assertEqual(strlen(' '), 1)

class TestFilterByPrefix(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(filter_by_prefix([], 'a'), [])
        self.assertEqual(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'), ['abc', 'array'])
    
    def test_various_prefixes(self):
        self.assertEqual(filter_by_prefix(['apple', 'banana', 'avocado'], 'a'), ['apple', 'avocado'])
        self.assertEqual(filter_by_prefix(['test', 'testing', 'tested'], 'test'), ['test', 'testing', 'tested'])


class TestIsPrime(unittest.TestCase):
    def test_prime_numbers(self):
        self.assertTrue(is_prime(13441))
        self.assertTrue(is_prime(61))
    
    def test_non_prime_numbers(self):
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(15))
    
    def test_edge_cases(self):
        self.assertFalse(is_prime(-10))

class TestCarRaceCollision(unittest.TestCase):
    def test_collisions(self):
        self.assertEqual(car_race_collision(2), 4)
        self.assertEqual(car_race_collision(3), 9)
        self.assertEqual(car_race_collision(10), 100)
    
    def test_edge_cases(self):
        self.assertEqual(car_race_collision(1), 1)
        self.assertEqual(car_race_collision(0), 0)

class TestPairsSumToZero(unittest.TestCase):
    def test_basic(self):
        self.assertFalse(pairs_sum_to_zero([1, 3, 5, 0]))
        self.assertTrue(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))
    
    def test_edge_cases(self):
        self.assertFalse(pairs_sum_to_zero([1]))
        self.assertTrue(pairs_sum_to_zero([-1, 1]))
        self.assertFalse(pairs_sum_to_zero([-1, -2, -3]))

class TestTriangleArea(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(triangle_area(5, 3), 7.5)
        self.assertEqual(triangle_area(2, 2), 2.0)
    
    def test_edge_cases(self):
        self.assertEqual(triangle_area(0, 5), 0.0)
        self.assertEqual(triangle_area(10, 0), 0.0)

class TestEncodeDecodeShift(unittest.TestCase):
    def test_encode(self):
        self.assertEqual(encode_shift('hello'), 'mjqqt')
        self.assertEqual(encode_shift('XYZ'), 'CDE')
        self.assertEqual(encode_shift('123'), '123')
    
    def test_decode(self):
        self.assertEqual(decode_shift('mjqqt'), 'hello')
        self.assertEqual(decode_shift('CDE'), 'XYZ')
        self.assertEqual(decode_shift('123'), '123')
    
    def test_round_trip(self):
        self.assertEqual(decode_shift(encode_shift('Test123')), 'Test123')
        self.assertEqual(decode_shift(encode_shift('aBc!@#')), 'aBc!@#')

if __name__ == '__main__':
    unittest.main()