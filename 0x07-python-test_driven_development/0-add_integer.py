#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two numbers after casting them to integers.

    :param a: The first number, must be an integer or float.
    :param b: The second number, defaults to 98 if not provided.
    :return: The addition of a and b casted to integers.
    :raises TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)) or a is None or isinstance(a, bool):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)) or b is None or isinstance(b, bool):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
