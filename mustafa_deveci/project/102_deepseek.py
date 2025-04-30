def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    start = min(x, y)
    end = max(x, y)
    
    # Iterate from the end to start to find the biggest even number
    for num in range(end, start - 1, -1):
        if num % 2 == 0:
            return num
    return -1

def test_choose_num_with_even_numbers():
    assert choose_num(12, 15) == 14

def test_choose_num_with_no_even_numbers():
    assert choose_num(13, 15) == -1
    
def test_choose_num_with_x_greater_than_y():
    assert choose_num(13, 12) == -1

# Run the tests and print results
if __name__ == "__main__":
    test_choose_num_with_even_numbers()
    test_choose_num_with_no_even_numbers() #assertion error
    test_choose_num_with_x_greater_than_y()
    print("All tests passed!")