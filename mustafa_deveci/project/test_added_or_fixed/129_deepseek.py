def minPath(grid, k):
    """
    Given a grid with N rows and N columns (N >= 2) and a positive integer k, 
    each cell of the grid contains a value. Every integer in the range [1, N * N]
    inclusive appears exactly once on the cells of the grid.

    You have to find the minimum path of length k in the grid. You can start
    from any cell, and in each step you can move to any of the neighbor cells,
    in other words, you can go to cells which share an edge with you current
    cell.
    Please note that a path of length k means visiting exactly k cells (not
    necessarily distinct).
    You CANNOT go off the grid.
    A path A (of length k) is considered less than a path B (of length k) if
    after making the ordered lists of the values on the cells that A and B go
    through (let's call them lst_A and lst_B), lst_A is lexicographically less
    than lst_B, in other words, there exist an integer index i (1 <= i <= k)
    such that lst_A[i] < lst_B[i] and for any j (1 <= j < i) we have
    lst_A[j] = lst_B[j].
    It is guaranteed that the answer is unique.
    Return an ordered list of the values on the cells that the minimum path go through.

    Examples:

        Input: grid = [ [1,2,3], [4,5,6], [7,8,9]], k = 3
        Output: [1, 2, 1]

        Input: grid = [ [5,9,3], [4,1,6], [7,8,2]], k = 1
        Output: [1]
    """
    n = len(grid)
    min_path = None

    # Directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    from collections import deque

    # We'll perform BFS starting from each cell, keeping track of the path
    for i in range(n):
        for j in range(n):
            queue = deque()
            initial_path = [grid[i][j]]
            queue.append((i, j, initial_path))

            while queue:
                x, y, path = queue.popleft()

                if len(path) == k:
                    if min_path is None or path < min_path:
                        min_path = path.copy()
                    continue

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n:
                        new_path = path.copy()
                        new_path.append(grid[nx][ny])
                        queue.append((nx, ny, new_path))

    return min_path

def test_small_grid():
    grid = [[1,2,3], [4,5,6], [7,8,9]]
    assert minPath(grid, 3) == [1, 2, 1]

def test_single_cell_path():
    grid = [[5,9,3], [4,1,6], [7,8,2]]
    assert minPath(grid, 1) == [1]

def test_larger_grid():
    grid = [[10,15,20], [5,1,25], [30,35,40]]
    assert minPath(grid, 4) == [1, 5, 1, 5]

def test_edge_movement():
    grid = [[3,1,4], [2,5,8], [6,7,9]]
    assert minPath(grid, 3) == [1, 3, 1] 

def test_full_grid_traversal():
    grid = [[3,1], [4,2]]
    assert minPath(grid, 4) == [1, 2, 1, 2]

if __name__ == "__main__": # pragma: no cover
    test_small_grid()
    test_single_cell_path()
    test_larger_grid()
    test_edge_movement() # FIXED TEST
    test_full_grid_traversal()
    print("All tests passed!")