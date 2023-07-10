#!/usr/bin/python3
"""Defines ``is_kind_of_class`` method"""


def is_kind_of_class(obj, a_class):
    """
    Args:
        obj: The object to check
        a_class: The class for object to compare
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
