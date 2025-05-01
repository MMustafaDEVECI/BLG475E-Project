def is_multiply_prime(a):
    """Returns True if the number a is the multiplication of exactly 3 prime numbers (not necessarily distinct), False otherwise."""
    def is_prime(n):
        if n < 2:
            return False
        for j in range(2, int(n**0.5) + 1):
            if n % j == 0:
                return False
        return True

    primes = [i for i in range(2, 100) if is_prime(i)]
    
    for i in primes:
        for j in primes:
            for k in primes:
                if i * j * k == a:
                    return True
    return False


# Unit tests
def test_is_multiply_prime():
    assert is_multiply_prime(5) == False  # Prime, but not product of 3 primes
    assert is_multiply_prime(30) == True  # 2 * 3 * 5
    assert is_multiply_prime(8) == True   # 2 * 2 * 2
    assert is_multiply_prime(10) == False # 2 * 5 (only two primes)
    assert is_multiply_prime(125) == True # 5 * 5 * 5
    assert is_multiply_prime(3 * 5 * 7) == True  # 105
    assert is_multiply_prime(3 * 6 * 7) == False # 6 is not prime
    assert is_multiply_prime(9 * 9 * 9) == False # 9 is not prime
    assert is_multiply_prime(11 * 9 * 9) == False # 9 not prime
    assert is_multiply_prime(11 * 13 * 7) == True # All primes

if __name__ == "__main__":
    test_is_multiply_prime()
    print("All tests passed.")
