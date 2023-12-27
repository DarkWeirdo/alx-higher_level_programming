#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    key argument will be always a string
    value argument will be any type
    If a key exists in the dictionary, the value will be replaced
    If a key doesn’t exist in the dictionary, it will be created
    """
    a_dictionary[key] = value
    return a_dictionary
