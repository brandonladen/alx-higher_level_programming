#!/usr/bin/python3
"""
    Defines a function print_square(size) that prints
    a square with the character #.
"""

def print_square(size):
    """
        Args:
            size: An integer that determines the size of the square
        Prints a square with the character #
    """

    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for x in range(1, size + 1):
        print("#" * size)
