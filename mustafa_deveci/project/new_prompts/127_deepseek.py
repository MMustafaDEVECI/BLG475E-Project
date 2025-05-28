def intersection(interval1, interval2):
    """
    Determines if the length of intersection between two closed intervals is a prime number.
    
    Args:
        interval1 (tuple): First interval (start, end)
        interval2 (tuple): Second interval (start, end)
        
    Returns:
        str: "YES" if intersection length is prime, "NO" otherwise
    """
    # Find the intersection interval
    start = max(interval1[0], interval2[0])
    end = min(interval1[1], interval2[1])
    
    # Check if intervals intersect
    if start > end:
        return "NO"
    
    # Calculate intersection length
    length = end - start + 1
    
    # Handle special cases for prime check
    if length < 2:
        return "NO"
    
    # Check if length is prime
    for i in range(2, int(length**0.5) + 1):
        if length % i == 0:
            return "NO"
    
    return "YES"

def test_no_intersection():
    assert intersection((1, 2), (3, 4)) == "NO"

def test_prime_intersection():
    assert intersection((-3, -1), (-5, 5)) == "YES"

def test_single_point_intersection():
    assert intersection((1, 2), (2, 3)) == "NO"

def test_negative_intersection():
    assert intersection((-5, 0), (-2, 2)) == "YES"

def test_no_prime_intersection(): # Newly added test
    assert intersection((1, 10), (2, 12)) == "NO"

if __name__ == "__main__": #pragma: no cover
    test_no_intersection()
    test_prime_intersection()
    test_single_point_intersection()
    test_negative_intersection()
    test_no_prime_intersection()
    print("All tests passed!")