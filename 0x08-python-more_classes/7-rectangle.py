#!/usr/bin/python3
"""rectangle 1 module

This module contains the text_indentation function. It was created
during the alx SE sponsored programme. It was created to practice
and demonstrate Object orinted programming in python
"""


class Rectangle:
    """
    This is an rectangle class created during the Alx software
    engineering course used to demonstrate object oriented
    programming in python.
    Attributes:
        number_of_instances (int): count of the number of instaces
        instantiated from the class
        print_symbol (Any): symbol to be used for string representation of
        class
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width: int = 0, height: int = 0):
        """initialises the class instances with the given arguments
        Args:
            width: rectangle width
            height: rectangle height
        Return: None
        Raises:
            TypeError: if width or height is not an integer
            ValueError: if width or height is < 0
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height
        self.number_of_instances += 1

    @property
    def width(self):
        """
            The width settter and getter sets and gets the width private
            instance attribute
        """
        return self.__width

    @width.setter
    def width(self, value: int):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
            The height settter and getter sets and gets the height private
            instance attribute
        """
        return self.__height

    @height.setter
    def height(self, value: int):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculates the area of a rectangle class
        Args:
            empty (no args)
        Return: calculation of rectangle area
        """
        return self.__height * self.__width

    def perimeter(self):
        """calculates the perimeter of a rectangle class
        Args:
            empty (no args)
        Return: calculation of rectangle perimeter
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self) -> str:
        ret = ""
        printed = str(self.print_symbol)
        if self.__width == 0 or self.__height == 0:
            return ret
        for _ in range(self.__height):
            ret += self.__width * printed + "\n"
        ret = ret[:-1]
        return ret

    def __repr__(self) -> str:
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self) -> None:
        self.number_of_instances -= 1
        print("Bye rectangle...")
