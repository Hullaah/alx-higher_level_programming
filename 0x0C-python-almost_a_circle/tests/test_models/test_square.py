import unittest
import sys
import io
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_initialise_all(self):
        sqr = Square(9, 78, 90, 1009)
        self.assertEqual(sqr.size, 9)
        self.assertEqual(sqr.height, 9)
        self.assertEqual(sqr.width, 9)
        self.assertEqual(sqr.x, 78)
        self.assertEqual(sqr.y, 90)
        self.assertEqual(sqr.id, 1009)

    def test_initialise_necessary(self):
        sqr = Square(2)
        self.assertEqual(sqr.size, 2)
        self.assertEqual(sqr.height, 2)
        self.assertEqual(sqr.width, 2)
        self.assertEqual(sqr.x, 0)
        self.assertEqual(sqr.y, 0)
        self.assertEqual(sqr.id, sqr._Base__nb_objects)

    def test_set_all(self):
        sqr = Square(9, 78, 90, 1987)
        sqr.size = 908
        self.assertEqual(sqr.size, 908)
        self.assertEqual(sqr.height, 908)
        self.assertEqual(sqr.width, 908)
        sqr.x = 10
        self.assertEqual(sqr.x, 10)
        sqr.y = 89
        self.assertEqual(sqr.y, 89)
        sqr.id = 80
        self.assertEqual(sqr.id, 80)

    def test_invalid_args(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sqr = Square("Hello", 1, 2, 3)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            sqr = Square(1, (1, 3, 4), 3, 4)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            sqr = Square(87, 1, {"name": 87}, 4)

    def test_invalid_args_value(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sqr = Square(0, 1, 2, 3)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sqr = Square(-7, 2, 2, 3)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            sqr = Square(900, -90, 3, 4)
        sqr = Square(1, 0, 3, 4)
        self.assertEqual(sqr.x, 0)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            sqr = Square(90, 0, -90, 4)
        sqr = Square(1, 2)
        self.assertEqual(sqr.y, 0)

    def test_setter(self):
        sqr = Square(909, 1, 2, 3)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sqr.size = 0
        sqr = Square(98, 2, 2, 3)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sqr.size = -7
        sqr = Square(900, 1, 987, 3)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            sqr.x = -65
        sqr = Square(1, 2, 90, 3)
        sqr.x = 0
        self.assertEqual(sqr.x, 0)
        sqr = Square(90, 1, 0, 90)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            sqr.y = -32
        sqr = Square(1, 2, 5, 89)
        sqr.y = 0
        self.assertEqual(sqr.y, 0)

    def test_area(self):
        sqr = Square(45, 67, 90, 876)
        self.assertEqual(sqr.area(), 45 ** 2)

    def test_stringify(self):
        sqr = Square(4, 6, 2, 1)
        string = "[Square] (1) 6/2 - 4"
        self.assertEqual(str(sqr), string)
        sqr = Square(5, 5, 1)
        string = "[Square] (" + str(sqr.id) + ") 5/1 - 5"
        self.assertEqual(str(sqr), string)

    def test_update1(self):
        sqr = Square(10, 10, 10, 10)
        self.assertEqual(str(sqr), "[Square] (" + str(sqr.id) + ") 10/10 - 10")
        sqr.update(89)
        self.assertEqual(str(sqr), "[Square] (89) 10/10 - 10")
        sqr.update(89, 2)
        self.assertEqual(str(sqr), "[Square] (89) 10/10 - 2")
        sqr.update(89, 2, 3)
        self.assertEqual(str(sqr), "[Square] (89) 3/10 - 2")
        sqr.update(89, 2, 3, 4)
        self.assertEqual(str(sqr), "[Square] (89) 3/4 - 2")
        sqr.update(89, 2, 3, 4)
        self.assertEqual(str(sqr), "[Square] (89) 3/4 - 2")

    def test_update2(self):
        sqr = Square(10, 10, 10, 10)
        self.assertEqual(str(sqr), "[Square] (" + str(sqr.id) + ") 10/10 - 10")
        sqr.update(size=1)
        self.assertEqual(str(sqr), "[Square] (" + str(sqr.id) + ") 10/10 - 1")
        sqr.update(size=1, x=2)
        self.assertEqual(str(sqr), "[Square] (" + str(sqr.id) + ") 2/10 - 1")
        sqr.update(y=1, size=2, x=3, id=89)
        self.assertEqual(str(sqr), "[Square] (" + str(sqr.id) + ") 3/1 - 2")
        sqr.update(x=1, size=2, y=3)
        self.assertEqual(str(sqr), "[Square] (" + str(sqr.id) + ") 1/3 - 2")

    def test_update1and2(self):
        sqr = Square(1, 2, 3, 4)
        sqr.update(98, width=90, size=789, id=90)
        self.assertEqual(str(sqr), "[Square] (98) 2/3 - 1")

    def test_display1(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        sqr = Square(4)
        sqr.display()
        string = captured_output.getvalue().strip()
        self.assertEqual(string, ((("#" * 4) + "\n") * 4)[:-1])
        sys.stdout = sys.__stdout__
        captured_output.close()
        captured_output = io.StringIO()
        sys.stdout = captured_output
        sqr = Square(2)
        sqr.display()
        string = captured_output.getvalue().strip()
        self.assertEqual(string, ((("#" * 2) + "\n") * 2)[:-1])
        sys.stdout = sys.__stdout__

    def test_display2(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        sqr = Square(8, 3, 4, 2)
        sqr.display()
        string = captured_output.getvalue().rstrip(" ")
        self.assertEqual(string, "\n\n\n\n" + (("   " + ("#" * 8) + "\n") * 8))
        sys.stdout = sys.__stdout__

    def test_to_dictionary(self):
        rect = Square(10, 2, 1, 9)
        sqr_dict = rect.to_dictionary()
        self.assertEqual(sqr_dict, {"id": 9, "size": 10, "x": 2, "y": 1})

if __name__ == "__main__":
    unittest.main()
