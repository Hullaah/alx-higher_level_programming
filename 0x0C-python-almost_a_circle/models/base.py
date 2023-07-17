#!/usr/bin/python3
"""This module was created as part of the required files for
the almost a circle python project done during the alx
SE training course
"""
import json


class Base:
    """This class will be the “base” of all other classes in this project.
    The goal of it is to manage id attribute in all your future classes and
    to avoid duplicating the same code (by extension, same bugs)

    Attributes:
        __nb_objects (int):
    """

    __nb_objects = 0

    def __init__(self, id=None) -> None:
        """The initialiser/constructor for the Base class

        Args:
            id: object id

        Return:
            None
        """
        if id is None:
            self.__class__.__nb_objects += 1
            id = self.__class__.__nb_objects
        self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """converts a list to a json string format

        Args:
            list_dictionaries: list to be converted

        Return:
            converted string
        """
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """saves the json representation of a list to a file

        Args:
            list_objects: a list of objects

        Return:
            None
        """
        if not list_objs:
            list_objs = []
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as json_file:
            arr = [x.to_dictionary() for x in list_objs]
            json_file.write(cls.to_json_string(arr))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string

        Args:
            json_string: json string representation

        Return:
            list of json string representation of json_string
        """
        if json_string:
            return json.loads(json_string)
        return []

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set

        Args:
            dictionary: dictionary to be used to instantiate object

        Return:
            an instance wih all attribute set
        """
        if cls.__name__ == "Square":
            ret = cls(1, 1, 0, 0)
            ret.update(**dictionary)
            return ret
        ret = cls(1, 1, 0, 0, 0)
        ret.update(**dictionary)
        return ret

    @classmethod
    def load_from_file(cls):
        ret = []
        try:
            with open(cls.__name__ + ".json", encoding="utf-8") as json_file:
                obj_arr = cls.from_json_string(json_file.read())
                for obj in obj_arr:
                    ret.append(cls.create(**obj))
        except IOError:
            pass
        return ret
