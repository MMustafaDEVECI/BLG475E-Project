from math import floor, ceil

def closest_integer(value):
    '''
    Create a function that takes a value (string) representing a number
    and returns the closest integer to it. If the number is equidistant
    from two integers, round it away from zero.

    Examples
    >>> closest_integer("10")
    10
    >>> closest_integer("15.3")
    15

    Note:
    Rounding away from zero means that if the given number is equidistant
    from two integers, the one you should return is the one that is the
    farthest from zero. For example closest_integer("14.5") should
    return 15 and closest_integer("-14.5") should return -15.
    '''
    
    if value.count('.') == 1:
        # remove trailing zeros
        while (value[-1] == '0'):
            value = value[:-1]

    num = float(value)
    
    if value[-2:] == '.5':
        if num > 0:
            res = ceil(num)
        else:
            res = floor(num)
    elif len(value) > 0:
        res = int(round(num))
    else:
        res = 0

    return res

def check(candidate):
    # Check some simple cases
    assert candidate("10") == 10, "Test 1"
    assert candidate("14.5") == 15, "Test 2"
    assert candidate("-15.5") == -16, "Test 3"
    assert candidate("15.3") == 15, "Test 4"

    # Check some edge cases that are easy to work out by hand.
    assert candidate("0") == 0, "Test 0"
    assert candidate("100.5") == 101, "Test 5"
    assert candidate("-100.5") == -101, "Test 6"
    assert candidate("2.5") == 3, "Test 7"
    assert candidate("-2.5") == -3, "Test 8"
    assert candidate("3.99") == 4, "Test 9"
    assert candidate("-3.99") == -4, "Test 10"

if __name__ == '__main__':
    check(closest_integer)
