def is_sorted(lst):
    '''
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers and only integers.

    Examples
    is_sorted([5]) → True
    is_sorted([1, 2, 3, 4, 5]) → True
    is_sorted([1, 3, 2, 4, 5]) → False
    is_sorted([1, 2, 3, 4, 5, 6]) → True
    is_sorted([1, 2, 3, 4, 5, 6, 7]) → True
    is_sorted([1, 3, 2, 4, 5, 6, 7]) → False
    is_sorted([1, 2, 2, 3, 3, 4]) → True
    is_sorted([1, 2, 2, 2, 3, 4]) → False
    '''
    # Check for duplicates appearing more than twice
    count_digit = {}
    for num in lst:
        count_digit[num] = count_digit.get(num, 0) + 1
        if count_digit[num] > 2:
            return False
    
    # Check if the list is sorted in ascending order
    for i in range(1, len(lst)):
        if lst[i-1] > lst[i]:
            return False
    
    return True

def test_sorted_no_duplicates():
    assert is_sorted([1, 2, 3, 4, 5]) == True

def test_sorted_with_valid_duplicates():
    assert is_sorted([1, 2, 2, 3, 3, 4]) == True

def test_unsorted_with_invalid_duplicates():
    assert is_sorted([1, 2, 2, 2, 3, 4]) == False

def test_not_sorted_example():
    assert is_sorted([1, 3, 2, 4, 5]) == False

if __name__ == '__main__':
    test_sorted_no_duplicates()
    test_sorted_with_valid_duplicates()
    test_unsorted_with_invalid_duplicates()
    test_not_sorted_example() # NEW TEST
    print("All tests passed.")