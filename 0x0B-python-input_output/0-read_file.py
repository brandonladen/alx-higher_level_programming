#!/usr/bin/python3
"""Define `read_file` module"""


def read_file(filename=""):
    """
        Args:
            filename is the name of the file to be read
        Returns:
            Prints the text to the standard output
    """
    with open(filename, "r", encoding="utf-8") as f:
            print(f.read(), end="")
