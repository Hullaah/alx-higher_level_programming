#!/usr/bin/python3
"""rectangle 0 module

This module contains the text_indentation function. It was created
during the alx SE sponsored programme. It was created to practice
and demonstrate Object orinted programming in python
"""


class BaseGeometry:
    """
    This is BaseGeometry class created during the Alx software
    engineering course used to demonstrate object oriented programming and
    inheritance in python.
    """

    def area(self):
        """ raises an exception that area is not defined
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name: str, value: int):
        """validates the value parameter
        Args:
            name: name of the value to be validated
            value: integer to be validated
        Return: None
        Raises:
            TypeError: if value is not an integer
            Valueerror: if value is <= 0
        """
        if type(value) is not int:
            raise TypeError(str(name) + " must be an integer")
        if value <= 0:
            raise ValueError(str(name) + " must be greater than 0")


class Rectangle(BaseGeometry):
    """
    This is Rectangle class created during the Alx software
    engineering course used to demonstrate object oriented programming and
    inheritance in python.
    """
    def __init__(self, width: int, height: int) -> None:
        """
        Args:
            width: rectangle width
            height: rectangle height
        Raises:
            TypeError: if height or width is not an integer
            Valueerror: if height or width is <= 0
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ calculates the area of the rectangle
        Return: area of the ractangle
        """
        return self.__height * self.__width

    def __str__(self) -> str:
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    def __init__(self, size: int) -> None:
        """
        Args:
            size: size of square
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is <= 0
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ calculates the area of the rectangle
        Return: area of the square
        """
        return self.__size ** 2
