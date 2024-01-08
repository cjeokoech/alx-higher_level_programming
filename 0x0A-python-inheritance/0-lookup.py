#!/usr/bin/python3
"""Return list of available attributes"""


def lookup(obj):
    """Return list

    Args:
    obj: object containing attributes

    Returns:
    list: of attributes
    """
    return dir(obj)
