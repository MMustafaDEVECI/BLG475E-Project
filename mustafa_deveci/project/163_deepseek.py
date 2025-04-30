def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    start = min(a, b)
    end = max(a, b)
    result = []
    for num in range(start, end + 1):
        if num % 2 == 0:
            result.append(num)
    return result

def test_single_even_number():
    assert generate_integers(4, 4) == [4]

def test_single_odd_number():
    assert generate_integers(3, 3) == []

def test_large_range():
    assert generate_integers(10, 20) == [10, 12, 14, 16, 18, 20]

if __name__ == "__main__":
    test_single_even_number()
    test_single_odd_number()
    test_large_range()
    print("All tests passed!")