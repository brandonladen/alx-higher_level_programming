#!/usr/bin/python3
"""Define `append_write` module"""


def append_write(filename="", text=""):
    """
        Args:
            filename is the name of the file to be read
            text is the text to be written in the file
        Returns:
            The number of characters written
    """
    with open(filename, mode="a", encoding="utf-8") as myFile:
        myFile.write(text)
    return len(text)
