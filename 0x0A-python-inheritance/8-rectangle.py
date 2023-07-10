#!/usr/bin/python3
"""Defines ``Rectangle`` class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry




class Rectangle(BaseGeometry):
    """Class Rectangle"""

    def __init__(self, width, height):
        """Initializing a rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
