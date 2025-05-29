from typing import List, Any

# HumanEval/6 - medium
def parse_nested_parens(paren_string: str) -> List[int]:
    def parse_paren_group(s):
        depth = 0
        max_depth = 0
        for c in s:
            if c == '(':
                depth += 1
                max_depth = max(depth, max_depth)
            else:
                depth -= 1
        return max_depth
    return [parse_paren_group(x) for x in paren_string.split(' ') if x]

# HumanEval/16 - easy
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) it contains.
    The count should be case-insensitive and include all characters (letters, numbers, 
    symbols, whitespace, etc.) after converting to lowercase.
    
    Args:
        string: Input string to analyze (may be empty)
        
    Returns:
        Number of distinct case-insensitive characters
        
    Examples:
        >>> count_distinct_characters('xyzXYZ')
        3
        >>> count_distinct_characters('Jerry123!')
        7  # J,e,r,y,1,2,3,!
        >>> count_distinct_characters(' ')
        1
    """
    return len(set(string.lower()))

# HumanEval/22 - easy
def filter_integers(values: List[Any]) -> List[int]:
    return [x for x in values if type(x) == int]

# HumanEval/23 - easy
def strlen(string: str) -> int:
    """
    Return the length of a given string in characters.
    Counts all Unicode characters including whitespace and special characters.
    
    Args:
        string: Input string (may be empty)
        
    Returns:
        Number of characters in the string
        
    Examples:
        >>> strlen('hello')
        5
        >>> strlen('ñ')
        1
        >>> strlen('')
        0
    """
    return len(string)

# HumanEval/29 - easy
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]

# HumanEval/31 - easy
def is_prime(n: int) -> bool:
    """
    Check if a given number is prime (has exactly two distinct positive divisors).
    
    Args:
        n: Integer to check (must be >= 0)
        
    Returns:
        True if n is prime, False otherwise
        Note: Returns False for numbers < 2
        
    Raises:
        TypeError: If input is not an integer
        
    Examples:
        >>> is_prime(5)
        True
        >>> is_prime(4)
        False
        >>> is_prime(1)
        False
    """
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2  # Only even prime is 2
    # Check odd divisors up to sqrt(n)
    max_divisor = int(n**0.5) + 1
    for k in range(3, max_divisor, 2):
        if n % k == 0:
            return False
    return True

# HumanEval/41 - easy?
def car_race_collision(n: int) -> int:
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars are driving left to right; simultaneously, a different set of n cars
    are driving right to left. The two sets of cars start out being very far from
    each other. All cars move at the same speed. Two cars are said to collide
    when a car moving left-to-right hits a car moving right-to-left.
    
    This function outputs the number of such collisions.
    
    Args:
        n: Number of cars in each direction (must be non-negative integer)
    
    Returns:
        Number of collisions (n squared)
    
    Raises:
        ValueError: If n is negative
        
    Examples:
        >>> car_race_collision(2)
        4
        >>> car_race_collision(0)
        0
    """
    return n ** 2

# HumanEval/43 - medium
def pairs_sum_to_zero(l: List[int]) -> bool:
    for i, l1 in enumerate(l):
        for j in range(i + 1, len(l)):
            if l1 + l[j] == 0:
                return True
    return False

# HumanEval/45 - easy
def triangle_area(a: float, h: float) -> float:
    """
    Calculate the area of a triangle given base length and height.
    
    Args:
        a: Length of the base (must be non-negative)
        h: Height of triangle (must be non-negative)
        
    Returns:
        Area of the triangle (a * h / 2)
        
    Raises:
        ValueError: If either input is negative
        
    Examples:
        >>> triangle_area(5, 3)
        7.5
        >>> triangle_area(2.5, 4.0)
        5.0
    """

    return a * h / 2.0

# HumanEval/50 - medium
def encode_shift(s: str) -> str:
    encoded = []
    for ch in s:
        if 'a' <= ch <= 'z':
            encoded_ch = chr(((ord(ch) - ord('a') + 5) % 26 + ord('a')))
        elif 'A' <= ch <= 'Z':
            encoded_ch = chr(((ord(ch) - ord('A') + 5) % 26 + ord('A')))
        else:
            encoded_ch = ch
        encoded.append(encoded_ch)
    return ''.join(encoded)

def decode_shift(s: str) -> str:
    decoded = []
    for ch in s:
        if 'a' <= ch <= 'z':
            decoded_ch = chr(((ord(ch) - ord('a') - 5) % 26 + ord('a')))
        elif 'A' <= ch <= 'Z':
            decoded_ch = chr(((ord(ch) - ord('A') - 5) % 26 + ord('A')))
        else:
            decoded_ch = ch
        decoded.append(decoded_ch)
    return ''.join(decoded)