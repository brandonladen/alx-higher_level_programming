#!/usr/bin/python3
"""Defines Rectangle module"""
from models.base import Base


class Rectangle(Base):
    """
        A representation of a rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
            Init function
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
            width getter
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
            width setter
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):
        """
            height getter
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
            height setter
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @property
    def x(self):
        """
            x getter
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
            x setter
        """
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        """
            y getter
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
            y setter
        """
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def area(self):
        """
            Calculates the earea of a rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
            Prints in stdout the Rectangle instance with the character #
        """
        space = " "
        for space_y in range(self.__y):
            print()
        
        for height in range(self.__height):
            print(space * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """
            String information of the rectangle
        """
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
            A public method that assigns an argument to each attribute
        """
        i = 0
        if args:
            for arg in args:
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.width = arg
                if i == 2:
                    self.height = arg
                if i == 3:
                    self.x = arg
                if i == 4:
                    self.y = arg
                i += 1
        else:
            for arg in kwargs:
                setattr(self, arg, kwargs.get(arg))

    def to_dictionary(self):
        return {'id': self.id, 'height': self.height, 'width': self.width, 'x': self.x, 'y': self.y}
