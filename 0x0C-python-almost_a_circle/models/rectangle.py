#!/usr/bin/python3
"""This module was created as part of the required files for
the almost a circle python project done during the alx
SE training course
"""
from models.base import Base


class Rectangle(Base):
    """This is the rectangle class that inherits from the base
    class. It creates an object of type Rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """This is the Rectangle initialiser/constructor that
        initialises the Rectangle object to be created

        Args:
            width (int): rectangle's width
            height (int): rectangle's height
            x (int): x position
            y (int): y position
            id (int | None): rectangle's id

        Return:
            None
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """width attribute getter and setter. It gets the width attribute of
        the rectangle class and also sets it to value specified
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height attribute getter and setter. It gets the height attribute of
        the rectangle class and also sets it to value specified
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x attribute getter and setter. It gets the x attribute of the
        rectangle class and also sets it to value specefied
        """
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """y attribute getter and setter. It gets the y attribute of the
        rectangle class and also sets it to value specefied
        """
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """calculates the area of the rectangle
        Args:
            Empty (No args)
        Return:
            area of rectangle
        """
        return self.__height * self.__width

    def display(self):
        """prints in stdout the Rectangle instance with the character #
        Args:
            Empty (No args)
        Return:
            None
        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            for _ in range(self.__x):
                print(" ", end="")
            print(self.__width * "#")

    def __str__(self) -> str:
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height
        )

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute
        Args:
            args: argument to use to update all the attributes
            kwargs: same function as kwargs but keyworded instead of
                positional
        Return:
            None
        """
        if args:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                return
        elif kwargs:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle
        Args:
            Empty (No args)
        Return:
            None
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,
        }
