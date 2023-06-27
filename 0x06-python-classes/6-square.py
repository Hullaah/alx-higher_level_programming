#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Square class module

This module is part of the project done during the alx SE course.
It contains a Square class object that stores a private size attribute.
Also, It posesses an area method that calculates the area of the square.

"""


class Square:
    """The Square class object.

        It is a class that stores a private size
        Attributes:
            __size (int): private size attribute
            __position (tuple): private position attribute. It is a tuple
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Args:
            size (int): The size of the square
            position (tuple): The position of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= to 0")
        self.__size = size
        self.__position = position

    def area(self) -> int:
        """
        Description: calculates the area of the square
        Args:
            Empty (No args)
        Return: area of square

        """

        return self.__size ** 2

    def my_print(self):
        """
        Description: prints the square
        Args:
            Empty (No args)
        Return: None

        """
        if self.__size == 0:
            print()
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for i in range(self.__position[0]):
                print(" ", end="")
            print(self.__size * "#")

    @property
    def size(self):
        """
        The size private attribute getter and setter gets and set the
        size attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= to 0")
        self.__size = value

    @property
    def position(self):
        """
        The position private attribute getter and setter gets and set the
        position attribute
        """
        return self.__position

    @position.getter
    def position(self, value):
        if len(self.__position) != 2 or type(self.__position[0]) is not int \
          or type(self.__position[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
