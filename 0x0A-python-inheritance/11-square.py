#!/usr/bin/python3
"""Defines class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class that inherits from class Rectangle"""
    def __init__(self, size):
        """initializer taking size parameter"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Area of a square"""
        return self.__size ** 2

    def __str__(self):
        """Human readable output"""
        return "[Square] {}/{}".format(self.__size, self.__size)
