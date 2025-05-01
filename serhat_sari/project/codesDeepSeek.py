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
    return len(set(string.lower()))

# HumanEval/22 - easy
def filter_integers(values: List[Any]) -> List[int]:
    return [x for x in values if type(x) == int]

# HumanEval/23 - easy
def strlen(string: str) -> int:
    return len(string)

# HumanEval/29 - easy
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]

# HumanEval/31 - easy
def is_prime(n: int) -> bool:
    """Return true if a given number is prime, and false otherwise."""
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