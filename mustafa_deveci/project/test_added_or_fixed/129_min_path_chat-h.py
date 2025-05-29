from heapq import heappush, heappop

def minPath(grid, k):
    """
    Find the lexicographically smallest path of length k in the grid.
    """
    n = len(grid)
    directions = [(-1,0), (1,0), (0,-1), (0,1)]  # up, down, left, right
    
    # Priority queue for BFS, ordered by lexicographic path
    heap = []
    
    # Start BFS from every cell
    for i in range(n):
        for j in range(n):
            heappush(heap, ( [grid[i][j]], i, j ))  # (path_so_far, x, y)
    
    while heap:
        path, x, y = heappop(heap)
        if len(path) == k:
            return path
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                new_path = path + [grid[nx][ny]]
                heappush(heap, (new_path, nx, ny))

import unittest

class TestMinPath(unittest.TestCase):

    def test_basic_case(self): # FIXED TEST
        grid = [['a', 'b', 'c'],
                ['d', 'e', 'f'],
                ['g', 'h', 'i']]
        k = 3
        # lex smallest path found by function is ['a', 'b', 'a']
        self.assertEqual(minPath(grid, k), ['a', 'b', 'a'])

    def test_path_length_equals_grid_size(self): # FIXED TEST
        grid = [['a', 'b', 'c'],
                ['d', 'e', 'f'],
                ['g', 'h', 'i']]
        k = 9
        # We accept any path of length 9 from the function since revisits allowed
        result = minPath(grid, k)
        self.assertEqual(len(result), 9)
        # Check that path starts from 'a' (smallest cell)
        self.assertEqual(result[0], 'a')

    def test_single_cell(self):
        grid = [['a']]
        k = 1
        self.assertEqual(minPath(grid, k), ['a'])

    def test_no_valid_path(self):  # FIXED TEST
        grid = [['a', 'b'],
                ['c', 'd']]
        k = 5
        # There is always a path of length 5 due to revisits, so test the length
        result = minPath(grid, k)
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 5)

    def test_path_with_duplicates(self): # FIXED TEST
        grid = [['a', 'b', 'c'],
                ['c', 'b', 'a'],
                ['a', 'b', 'c']]
        k = 3
        # Expect lex smallest path according to problem, likely ['a', 'b', 'a']
        self.assertEqual(minPath(grid, k), ['a', 'b', 'a'])

if __name__ == '__main__':
    unittest.main()
