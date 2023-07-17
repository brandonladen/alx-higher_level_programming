#!/usr/bin/python3
"""Defines class Square that inherits from Rectangle mmodel"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
        A representation of a square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
            class Square constructor
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
            Size Getter
        """
        return self.width

    @size.setter
    def size(self, value):
        """
            Size Setter
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
            String representation
        """
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """
            updates class square
        """
        i = 0
        if args:
            for arg in args:
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.size = arg
                if i == 2:
                    self.x = arg
                if i == 3:
                    self.y = arg
                i += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """the dictionary representation"""
        return {"id": self.id, "x": self.x, "size": self.size, "y": self.y}
