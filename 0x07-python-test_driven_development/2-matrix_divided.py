#!/usr/bin/python3
"""Matrix_divided module

This module contains the matrix_divided function. It was created
during the alx SE sponsored programme. It was created to practice
and demonstrate testing with python doctest library
"""


def matrix_divided(matrix: list, div) -> list:
    """
    Description: divides all the element of a matrix by div
    Args:
        matrix: a two dimensional array of numbers
        div (number): divisor of matrix
    Return: new matrix divided by divisor
    Raises:
        TypeError: If matrix is not a list of list of numbers
        ZeroDivisionError: If div is zero

    """
    length = 0
    status = 0
    error = "matrix must be a matrix (list of lists) of integers/floats"
    if type(div) is not float and type(div) is not int:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list:
        raise TypeError()
    ans = []
    for elements in matrix:
        if type(elements) is not list:
            raise TypeError(error)
        if not status:
            length = len(elements)
            status = 1
        if length != len(elements):
            raise TypeError("Each row of the matrix must have the same size")
        for elem in elements:
            if type(elem) is not int and type(elem) is not float:
                raise TypeError(error)
        ans.append([round(x / div, 2) for x in elements])
    return ans
