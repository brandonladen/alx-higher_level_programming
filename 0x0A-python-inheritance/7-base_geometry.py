#!/usr/bin/python3
"""Defines ```BaseGeometry``` class"""


class BaseGeometry:
    """
        A class with one function
    """
    def area(self):
        """
            Public instance  that raises an exception
        """
        raise Exception("area() is not implemented")
        
    def integer_validator(self, name, value):
        """
            Public instance that  validates value
            Args:
                name: Is always a string
                value: To be validated
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
