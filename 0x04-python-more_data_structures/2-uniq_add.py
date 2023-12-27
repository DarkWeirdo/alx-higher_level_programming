#!/usr/bin/python3
def uniq_add(my_list=[]):
    # adds all unique integers in a list (only once for each integer).
    uniq_list = set(my_list)
    # Turns a list into a set of unique values.
    num = 0

    for i in uniq_list:
        num += i
    # Adds all elements of the set.
    return num
