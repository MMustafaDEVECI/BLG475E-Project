def histogram(test):
    """
    Given a string of space-separated lowercase letters, returns a dictionary containing
    the letter(s) that appear most frequently along with their counts.
    
    Args:
        test (str): Input string of space-separated lowercase letters
        
    Returns:
        dict: Dictionary with most frequent letters as keys and their counts as values
              Returns empty dict if input is empty or only whitespace
    """
    # Remove all whitespace and check if string is empty
    letters = test.replace(" ", "")
    if not letters:
        return {}
    
    # Count frequency of each letter
    freq = {}
    for char in letters:
        freq[char] = freq.get(char, 0) + 1
    
    # Find maximum frequency
    max_freq = max(freq.values()) if freq else 0
    
    # Get all letters with max frequency
    result = {k: v for k, v in freq.items() if v == max_freq}
    
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