#!/usr/bin/python3
def number_keys(a_dictionary):
    # returns the number of keys in a dictionary.
    num = 0
    list_keys = list(a_dictionary.keys())
    # Extracts keys from the input dictionary and lists them in list_keys
    for i in list_keys:
        num += 1
        # scans the list and counts the number of key in the list.
    return num
