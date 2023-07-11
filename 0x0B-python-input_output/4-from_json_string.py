#!/usr/bin/python3
"""from json string module
This module contains the from_json_string function used to convert
json to python object
"""
import json


def from_json_string(my_obj):
    """returns an object (Python data structure) represented by a JSON string.
    Args:
        my_obj: object to be converted to json string
    Return: object
    """
    return json.loads(my_obj)
