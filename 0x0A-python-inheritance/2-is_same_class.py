#!/usr/bin/python3
"""Defines module ``is_same_class``"""

def is_same_class(obj, a_class):
    """
    Args:
        obj: An object to check its instance
        a_class: An instance
    """
    if type(obj) == a_class:
        return True
    else:
        return False
