#!/usr/bin/python3
"""This module was created as part of the required files for
the almost a circle python project done during the alx
SE training course
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This is the Square class that inherits from the rectangle
    class. It creates an object of type Square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """This is the square initialiser/constructor that
        initialises the square object to be created

        Args:
            size (int): square's size in width and height
            x (int): x position
            y (int): y position
            id (int | None): square's id

        Return:
            None
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size attribute getter and setter. It gets the size attribute of
        the square
          class and also sets it to value specified
        """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self) -> str:
        return "[Square] ({}) {}/{} - {}".format(
            self.id,
            self.x,
            self.y,
            self.width,
        )

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute
        Args:
            args: argument to use to update all the attributes
            kwargs: same function as kwargs but keyworded instead of
                positional
        Return:
            None
        """
        if args:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                return
        elif kwargs:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """returns the dictionary representation of a Square
        Args:
            Empty (No args)
        Return:
            None
        """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y,
        }
