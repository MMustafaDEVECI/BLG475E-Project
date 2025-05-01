def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    def is_prime(n):
        if n < 2:
            return False
        for j in range(2, n):
            if n % j == 0:
                return False
        return True

    for i in range(2, 101):
        if not is_prime(i):
            continue
        for j in range(2, 101):
            if not is_prime(j):
                continue
            for k in range(2, 101):
                if not is_prime(k):
                    continue
                if i * j * k == a:
                    return True
    return False


# Unit tests
def test_is_multiply_prime():
    assert is_multiply_prime(5) == False
    assert is_multiply_prime(30) == True
    assert is_multiply_prime(8) == True  # 2 * 2 * 2
    assert is_multiply_prime(10) == False
    assert is_multiply_prime(125) == True  # 5 * 5 * 5
    assert is_multiply_prime(3 * 5 * 7) == True  # 105
    assert is_multiply_prime(3 * 6 * 7) == False  # 6 is not prime
    assert is_multiply_prime(9 * 9 * 9) == False  # 9 is not prime
    assert is_multiply_prime(11 * 9 * 9) == False  # 9 is not prime
    assert is_multiply_prime(11 * 13 * 7) == True  # 1001 (but note a < 100 in prompt)
    assert is_multiply_prime(1) == False
    assert is_multiply_prime(2) == False
    assert is_multiply_prime(27) == True  # 3 * 3 * 3
    assert is_multiply_prime(0) == False

if __name__ == "__main__":
    test_is_multiply_prime()
    print("All tests passed")
