#!/usr/bin/python3

"""my_int module
This module conatins the MyInt class used to demonstrate
object oriented programming and inheriatnce in python
"""


class MyInt(int):
    """MyInt class inherits from int class.
    It is used to demonstrate object oriented programming and inheritane
    in python
    """
    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
