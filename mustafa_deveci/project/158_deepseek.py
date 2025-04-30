def find_max(words):
    """
    Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"
    """
    max_unique = -1
    result = None
    
    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_unique:
            max_unique = unique_chars
            result = word
        elif unique_chars == max_unique:
            if word < result:  # lexicographical order check
                result = word
    return result

def test_basic_case():
    assert find_max(["name", "of", "string"]) == "string"

def test_tiebreaker_case():
    assert find_max(["name", "enam", "game"]) == "enam"

def test_all_same_unique():
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

def test_empty():
    assert find_max([""]) == ""  # single empty string

if __name__ == "__main__":  
    test_basic_case()
    test_tiebreaker_case()
    test_all_same_unique()
    test_empty()
    print("All tests passed!")