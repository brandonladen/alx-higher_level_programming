#!/usr/bin/python3
"""
    Defines a function say_my_name(first_name, last_name="")
    that prints My name is <first name> <last name>.
"""

def say_my_name(first_name, last_name=""):
    """
    Args:
        first_name: A string representing the first name
        last_name: A string whose default value is an empty string
                    It represents the last name
        Prints a combination of <first name> and <last name>
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
