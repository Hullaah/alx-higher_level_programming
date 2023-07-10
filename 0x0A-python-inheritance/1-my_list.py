#!/usr/bin/python3
"""
This is the module for 1-my_list.py done during the alx SE course
"""


class MyList(list):
    """
    MyList inherits from the python built-in list
    """
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
