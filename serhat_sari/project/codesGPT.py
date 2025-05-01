from typing import List, Any
import unittest

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
    return [x for x in values if isinstance(x, int)]

# HumanEval/23 - easy
def strlen(string: str) -> int:
    return len(string)

# HumanEval/29 - easy
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]

# HumanEval/31 - easy
def is_prime(n):
    """Return True if a given number is prime, and False otherwise."""
    if n < 2:
        return False
    for k in range(2, int(n ** 0.5) + 1):
        if n % k == 0:
            return False
    return True

# HumanEval/41 - easy?
def car_race_collision(n: int):
    return n ** 2

# HumanEval/43 - medium
def pairs_sum_to_zero(l):
    for i, l1 in enumerate(l):
        for j in range(i + 1, len(l)):
            if l1 + l[j] == 0:
                return True
    return False

# HumanEval/45 - easy
def triangle_area(a, h):
    return a * h / 2.0

# HumanEval/50 - medium
def encode_shift(s: str):
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])