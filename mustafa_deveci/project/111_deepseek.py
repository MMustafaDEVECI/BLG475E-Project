def histogram(test):
    """
    Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    
    Example:
    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    histogram('a b b a') == {'a': 2, 'b': 2}
    histogram('a b c a b') == {'a': 2, 'b': 2}
    histogram('b b b b a') == {'b': 4}
    histogram('') == {}
    """
    if not test:
        return {}
    
    letters = test.split()
    count_dict = {}
    
    for letter in letters:
        if letter in count_dict:
            count_dict[letter] += 1
        else:
            count_dict[letter] = 1
    
    if not count_dict:
        return {}
    
    max_count = max(count_dict.values())
    result = {k: v for k, v in count_dict.items() if v == max_count}
    
    return result

def test_all_unique_letters():
    assert histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}

def test_tied_most_frequent():
    assert histogram('a b b a c') == {'a': 2, 'b': 2}

def test_single_dominant_letter():
    assert histogram('b b b a c c') == {'b': 3}

def test_empty_input():
    assert histogram('') == {}

if __name__ == "__main__":
    test_all_unique_letters()
    test_tied_most_frequent()
    test_single_dominant_letter()
    test_empty_input()
    print("All tests passed!")