#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Replaces all occurrences of an element by another in a new list.
    new_list = list(map(lambda x: replace if x == search else x, my_list))
    """
    List comprehension:
    function where input x is scanned
    if x == search, x = replace
    else x stays x
    function input mapped to my_list
    output is list()-ed
    """
    return new_list
