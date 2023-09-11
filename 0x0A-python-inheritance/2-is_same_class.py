#!/usr/bin/python3

"""Define a class-checking function."""


def is_same_class(obj, a_class):
    """Checks if object is exactly an instance of a given class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        True - if obj is exactly an instance of a_class.
        False - if its not.
    """
    if type(obj) == a_class:
        return True
    return False
