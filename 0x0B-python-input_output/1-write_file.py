#!/usr/bin/python3
"""Define `write_file` module"""


def write_file(filename="", text=""):
    """
        Args:
            filename is the name of the file to be read
            text is the text to be written in the file
        Returns:
            The number of characters written
    """
    with open(filename, mode="w", encoding="utf-8") as myFile:
        myFile.write(text)
    return len(text)
