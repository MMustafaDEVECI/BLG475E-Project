class MathFunctions:
    @staticmethod
    def triangle_area(a, h):
        """Given length of a side and height, return the area of a triangle."""
        return (a * h) / 2

    @staticmethod
    def fib(n: int):
        """Return the n-th Fibonacci number."""
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

    @staticmethod
    def choose_num(x, y):
        """Return the biggest even integer in the range [x, y] inclusive."""
        if x > y:
            return -1
        largest_even = y if y % 2 == 0 else y - 1
        return largest_even if largest_even >= x else -1


# Enhanced Integration Tests
import unittest

class TestMathFunctionsIntegration(unittest.TestCase):
    def test_combined_operations(self):
        # Test case 1: Using Fibonacci result as triangle base
        fib_result = MathFunctions.fib(6)  # fib(6) = 8
        area = MathFunctions.triangle_area(fib_result, 4)  # area = (8*4)/2 = 16
        self.assertEqual(area, 16.0)
        
        # Find largest even number between fib result and 10
        even_num = MathFunctions.choose_num(fib_result, 10)  # 8-10 -> 10
        self.assertEqual(even_num, 10)

    def test_edge_case_combinations(self):
        # Test case 2: When Fibonacci returns 0
        fib_result = MathFunctions.fib(0)  # 0
        area = MathFunctions.triangle_area(fib_result, 5)  # 0
        self.assertEqual(area, 0.0)
        
        # Should return -1 since 0 is even but x=y=0
        even_num = MathFunctions.choose_num(fib_result, fib_result)  # 0-0 -> 0
        self.assertEqual(even_num, 0)

    def test_real_world_scenario(self):
        # Test case 3: Practical application scenario
        # Calculate area of triangle with sides based on fib sequence
        fib1 = MathFunctions.fib(5)  # 5
        fib2 = MathFunctions.fib(6)  # 8
        area = MathFunctions.triangle_area(fib1, fib2)  # (5*8)/2 = 20
        self.assertEqual(area, 20.0)
        
        # Find largest even in range between two fib numbers
        even_num = MathFunctions.choose_num(fib1, fib2)  # 5-8 -> 8
        self.assertEqual(even_num, 8)
        
        # Verify edge where no even exists
        even_num = MathFunctions.choose_num(fib1-1, fib1)  # 4-5 -> 4
        self.assertEqual(even_num, 4)

    def test_chain_operations(self):
        # Test case 4: Chaining multiple operations
        # Get fib number, use as base, find even in range with height
        fib_num = MathFunctions.fib(7)  # 13
        height = 6
        area = MathFunctions.triangle_area(fib_num, height)  # (13*6)/2 = 39
        self.assertEqual(area, 39.0)
        
        # Find largest even between height and area (6-39)
        even_num = MathFunctions.choose_num(height, area)  # 6-39 -> 38
        self.assertEqual(even_num, 38)
        
        # Verify with adjusted range
        even_num = MathFunctions.choose_num(height, fib_num)  # 6-13 -> 12
        self.assertEqual(even_num, 12)
        
    def test_choose_num_x_gt_y_with_fib1(self):
        """Test when x > y in choose_num combined with fib(1)"""
        fib_result = MathFunctions.fib(1)  # Should return 1
        self.assertEqual(fib_result, 1)
        
        # Use fib result as x, and a smaller number as y
        even_num = MathFunctions.choose_num(fib_result, fib_result - 1)  # 1 > 0
        self.assertEqual(even_num, -1)  # Because x > y
        
        # Also test with explicit x > y values
        even_num = MathFunctions.choose_num(5, 3)  # 5 > 3
        self.assertEqual(even_num, -1)
        
        # Test edge case where fib(1) is used as both x and y
        even_num = MathFunctions.choose_num(fib_result, fib_result)  # 1 == 1 (no even)
        self.assertEqual(even_num, -1)

if __name__ == '__main__':
    unittest.main()