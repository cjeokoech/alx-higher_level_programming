#!/usr/bin/python3
def add_integer(a, b=98):
    """Add 2 integers

    Parameters:
    a: the first integer
    b(default 98): second integer

    Returns:
    int: sum of a and b

    Raises:
    TypeError: if a or b are not integers
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
