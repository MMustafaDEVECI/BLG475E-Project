def sort_array(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) == [0, 1, 2, 3, 4]
    """
    def count_ones(x):
        if x < 0:
            x = -x
        return bin(x).count('1')
    
    return sorted(arr, key=lambda x: (count_ones(x), x))

def test_basic_sorting():
    assert sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]

def test_negative_numbers():
    assert sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]

def test_with_zero_and_duplicates():
    assert sort_array([1, 0, 2, 3, 4, 4]) == [0, 1, 2, 4, 4, 3]

def test_same_ones_count():
    assert sort_array([7, 14, 28, 56]) == [7, 14, 28, 56]

if __name__ == '__main__':
    test_basic_sorting() #assertion error
    test_negative_numbers() #assertion error
    test_with_zero_and_duplicates()
    test_same_ones_count()
    print("All tests passed.")