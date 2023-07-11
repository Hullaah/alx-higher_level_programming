#!/usr/bin/python3
"""to json string module
This module contains the to_json_string function used to convert
python objects to string
"""
import json


def to_json_string(my_obj):
    """returns JSON representation of an object.
    Args:
        my_obj: object to be converted to json string
    Return: string
    """
    return json.dumps(my_obj)
