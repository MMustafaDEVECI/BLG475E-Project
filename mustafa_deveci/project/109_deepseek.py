def move_one_ball(arr):
    """
    We have an array 'arr' of N integers arr[1], arr[2], ..., arr[N].The
    numbers in the array will be randomly ordered. Your task is to determine if
    it is possible to get an array sorted in non-decreasing order by performing 
    the following operation on the given array:
        You are allowed to perform right shift operation any number of times.
    
    One right shift operation means shifting all elements of the array by one
    position in the right direction. The last element of the array will be moved to
    the starting position in the array i.e. 0th index. 

    If it is possible to obtain the sorted array by performing the above operation
    then return True else return False.
    If the given array is empty then return True.

    Note: The given list is guaranteed to have unique elements.

    For Example:
    
    move_one_ball([3, 4, 5, 1, 2])==>True
    Explanation: By performing 2 right shift operations, non-decreasing order can
                 be achieved for the given array.
    move_one_ball([3, 5, 4, 1, 2])==>False
    Explanation:It is not possible to get non-decreasing order for the given
                array by performing any number of right shift operations.
                
    """
    if not arr:
        return True
    
    n = len(arr)
    sorted_arr = sorted(arr)
    
    for k in range(n):
        # Perform k right shifts and check if the array is sorted
        shifted_arr = arr[-k:] + arr[:-k]
        if shifted_arr == sorted_arr:
            return True
    
    return False

def test_already_sorted():
    assert move_one_ball([1, 2, 3, 4, 5]) == True

def test_sortable_with_shifts():
    assert move_one_ball([3, 4, 5, 1, 2]) == True

def test_not_sortable():
    assert move_one_ball([3, 5, 4, 1, 2]) == False

def test_empty_array():
    assert move_one_ball([]) == True

def test_single_element():
    assert move_one_ball([5]) == True

if __name__ == '__main__':
    test_already_sorted()
    test_sortable_with_shifts()
    test_not_sortable()
    test_empty_array()
    test_single_element()
    print("All tests passed.")