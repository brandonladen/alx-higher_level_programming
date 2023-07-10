#!/usr/bin/python3
"""Deifines a lookup function"""

def lookup(obj):
    """
        A function that returns the list of available attributes
        and methods of an object
    """
    return dir(obj)
