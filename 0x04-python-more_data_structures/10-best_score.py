#!/usr/bin/python3
def best_score(a_dictionary):
    """
    function that returns a key with the biggest integer value.
    You can assume that all values are only integers
    If no score found, return None
    You can assume all students have a different score
    """
    if not a_dictionary:
        return None

    return max(a_dictionary, key=a_dictionary.get)
