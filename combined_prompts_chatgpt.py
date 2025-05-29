import unittest

class MathUtils:
    @staticmethod
    def triangle_area(a: float, h: float) -> float:
        """
        Given the length of a side (a) and height (h), return the area of a triangle.
        >>> MathUtils.triangle_area(5, 3)
        7.5
        """
        return 0.5 * a * h

    @staticmethod
    def fib(n: int) -> int:
        """
        Return the n-th Fibonacci number.
        >>> MathUtils.fib(10)
        55
        >>> MathUtils.fib(1)
        1
        >>> MathUtils.fib(8)
        21
        """
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

    @staticmethod
    def find_max_even_in_range(x: int, y: int) -> int:
        """
        Return the largest even integer within the inclusive range [x, y].
        If no even number exists in that range, return -1.
        >>> MathUtils.find_max_even_in_range(3, 9)
        8
        >>> MathUtils.find_max_even_in_range(7, 7)
        -1
        """
        for num in range(y, x - 1, -1):
            if num % 2 == 0:
                return num
        return -1


class TestMathUtilsIntegration(unittest.TestCase):

    def test_triangle_area_using_fib_and_even_range(self):
        base = MathUtils.find_max_even_in_range(4, 10)  # 10
        height = MathUtils.fib(5)  # 5
        area = MathUtils.triangle_area(base, height)
        self.assertEqual(area, 25.0)

    def test_triangle_area_with_no_even_in_range(self):
        base = MathUtils.find_max_even_in_range(7, 7)  # -1
        height = MathUtils.fib(4)  # 3
        area = MathUtils.triangle_area(base, height)
        self.assertEqual(area, -1.5)

    def test_fib_and_even_range_sequence(self):
        for i in range(1, 6):
            fib_value = MathUtils.fib(i)
            even_value = MathUtils.find_max_even_in_range(1, fib_value)
            if even_value != -1:
                self.assertEqual(even_value % 2, 0)
                self.assertLessEqual(even_value, fib_value)

    def test_large_integration_scenario(self):
        x, y = 13, 27
        base = MathUtils.find_max_even_in_range(x, y)  # 26
        height = MathUtils.fib(9)  # 34
        area = MathUtils.triangle_area(base, height)
        self.assertEqual(area, 442.0)

    def test_combined_failure_case(self):
        base = MathUtils.find_max_even_in_range(11, 11)  # -1
        height = MathUtils.fib(0)  # 0
        area = MathUtils.triangle_area(base, height)
        self.assertEqual(area, 0.0)


if __name__ == "__main__":
    unittest.main()
