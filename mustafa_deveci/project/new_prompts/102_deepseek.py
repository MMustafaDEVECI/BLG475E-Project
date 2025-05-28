def choose_num(x, y):
    if x > y:
        return -1
    largest_even = y if y % 2 == 0 else y - 1
    if largest_even >= x:
        return largest_even
    else:
        return -1

def test_choose_num_with_even_numbers():
    assert choose_num(12, 15) == 14

def test_choose_num_with_no_even_numbers():
    assert choose_num(13, 15) == 14
    
def test_choose_num_with_x_greater_than_y():
    assert choose_num(13, 12) == -1

def test_choose_num_with_all_odds():
    assert choose_num(11, 11) == -1

# Run the tests and print results
if __name__ == "__main__":  # pragma: no cover
    test_choose_num_with_even_numbers()
    test_choose_num_with_no_even_numbers()  # FIXED TEST
    test_choose_num_with_x_greater_than_y() 
    test_choose_num_with_all_odds()
    print("All tests passed!")