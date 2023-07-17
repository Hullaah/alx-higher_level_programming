import unittest
import json
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    def test_with_args(self):
        base = Base(17)
        self.assertEqual(base.id, 17)
        self.assertEqual(base._Base__nb_objects, 4)
        base = Base(90)
        self.assertEqual(base.id, 90)
        self.assertEqual(base._Base__nb_objects, 4)

    def test_no_args(self):
        base = Base()
        self.assertEqual(base.id, 1)
        self.assertEqual(base._Base__nb_objects, 1)
        base = Base()
        self.assertEqual(base.id, 2)
        self.assertEqual(base._Base__nb_objects, 2)

    def test_with_and_without_args(self):
        base = Base()
        self.assertEqual(base.id, 3)
        self.assertEqual(base._Base__nb_objects, 3)
        base = Base(134)
        self.assertEqual(base.id, 134)
        self.assertEqual(base._Base__nb_objects, 3)
        base = Base(345)
        self.assertEqual(base.id, 345)
        self.assertEqual(base._Base__nb_objects, 3)
        base = Base()
        self.assertEqual(base.id, 4)
        self.assertEqual(base._Base__nb_objects, 4)

    def test_to_json_string(self):
        rect = Rectangle(10, 7, 2, 8, 1)
        dictionary = rect.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        json_dictionary = json.loads(json_dictionary)
        self.assertEqual([dictionary], json_dictionary)
        sqr = Square(10, 7, 2, 8)
        dictionary = sqr.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        json_dictionary = json.loads(json_dictionary)
        self.assertEqual([dictionary], json_dictionary)
        json_dictionary = Base.to_json_string([])
        self.assertEqual("[]", json_dictionary)
        json_dictionary = Base.to_json_string(None)
        self.assertEqual("[]", json_dictionary)

    def test_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        self.assertTrue(os.path.exists("Rectangle.json"))
        with open("Rectangle.json") as json_file:
            loaded_dict = json.load(json_file)
            self.assertEqual(loaded_dict, [r1.to_dictionary(), r2.to_dictionary()])
        Rectangle.save_to_file(None)
        with open("Rectangle.json") as json_file:
            self.assertEqual(json_file.read(), "[]")
        Rectangle.save_to_file([])
        with open("Rectangle.json") as json_file:
            self.assertEqual(json_file.read(), "[]")
        s1 = Square(10, 7, 2, 8)
        s2 = Square(2, 4)
        Square.save_to_file([s1, s2])
        self.assertTrue(os.path.exists("Square.json"))
        with open("Square.json") as json_file:
            loaded_dict = json.load(json_file)
            self.assertEqual(loaded_dict, [s1.to_dictionary(), s2.to_dictionary()])
        Square.save_to_file(None)
        with open("Square.json") as json_file:
            self.assertEqual(json_file.read(), "[]")
        Square.save_to_file([])
        with open("Square.json") as json_file:
            self.assertEqual(json_file.read(), "[]")
        os.remove("Rectangle.json")
        os.remove("Square.json")

    def test_from_json_string(self):
        list_input = [
            {'id': 89, 'width': 10, 'height': 4}, 
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, list_input)
        list_input = None
        list_output = Rectangle.from_json_string(list_input)
        self.assertEqual(list_output, [])
        list_input = [
            {'id': 89, 'size': 10}, 
            {'id': 7, 'size': 1}
        ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_output, list_input)
        list_input = None
        list_output = Square.from_json_string(list_input)
        self.assertEqual(list_output, [])

    def test_create(self):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 3/5")
        s1 = Square(1, 2, 3, 4)
        s1_dictionary = s1.to_dictionary()
        s2 = s1.create(**s1_dictionary)
        self.assertEqual(str(s2), "[Square] (4) 2/3 - 1")

    def test_load_from_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        test1 = [str(x) for x in list_rectangles_input]
        test2 = [str(x) for x in list_rectangles_output]
        self.assertEqual(test1, test2)
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        test1 = [str(x) for x in list_squares_input]
        test2 = [str(x) for x in list_squares_output]
        self.assertEqual(test1, test2)


if __name__ == "__main__":
    unittest.main()
