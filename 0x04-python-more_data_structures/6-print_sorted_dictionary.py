#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """
    prints a dictionary by ordered keys.
    You can assume that all keys are strings
    Keys should be sorted by alphabetic order
    Only sort keys of the first level (don’t sort keys of a dictionary inside the main dictionary)
    Dictionary values can have any type
    You are not allowed to import any module
    """
    list_ord = list(a_dictionary.keys())
    # Extract dict keys into a list
    list_ord.sort()
    # Sort list by keys
    for i in list_ord:
        print("{}: {}".format(i, a_dictionary.get(i)))
        # Use sorted list to print dict values sorted by keys
