#!/usr/bin/python3
"""student module
This module defines a student class which is used
to demonstrate file I/O in python
"""


class Student:
    """The student class
    This is the student class that is
    used to demonstrate file I/O in python
    """
    def __init__(self, first_name, last_name, age):
        """this is the student constructor
        Args:
            first_name: student's first name
            last_name: student's last name
            age: student's age
        Return:
            None
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance
        Args:
            Empty (No args)
        Return:
            dictionary representation of string
        """
        if attrs is None or any([type(i) is not str for i in attrs]):
            return ({
                "first_name": self.first_name,
                "age": self.age,
                "last_name": self.last_name
                })
        else:
            ans = {}
            for i in range(len(attrs)):
                temp = getattr(self, attrs[i], None)
                if temp:
                    ans[attrs[i]] = temp
            return ans
