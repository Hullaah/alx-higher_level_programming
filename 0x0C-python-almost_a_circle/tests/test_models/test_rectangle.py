import unittest
import sys
import io
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_initialise_all(self):
        rect = Rectangle(9, 5, 78, 90, 1009)
        self.assertEqual(rect.height, 5)
        self.assertEqual(rect.width, 9)
        self.assertEqual(rect.x, 78)
        self.assertEqual(rect.y, 90)
        self.assertEqual(rect.id, 1009)

    def test_initialise_necessary(self):
        rect = Rectangle(2, 4)
        self.assertEqual(rect.height, 4)
        self.assertEqual(rect.width, 2)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)
        self.assertEqual(rect.id, rect._Base__nb_objects)

    def test_set_all(self):
        rect = Rectangle(9, 5, 78, 90, 1987)
        self.assertEqual(rect.height, 5)
        rect.height = 10
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.width, 9)
        rect.width = 76
        self.assertEqual(rect.width, 76)
        self.assertEqual(rect.x, 78)
        rect.x = 10
        self.assertEqual(rect.x, 10)
        self.assertEqual(rect.y, 90)
        rect.y = 89
        self.assertEqual(rect.y, 89)
        self.assertEqual(rect.id, 1987)
        rect.id = 80
        self.assertEqual(rect.id, 80)

    def test_invalid_args(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rect = Rectangle("Hello", 1, 2, 3, 4)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rect = Rectangle(1, [23, 45, 67], 2, 3, 4)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rect = Rectangle(90, 1, (1, 3, 4), 3, 4)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rect = Rectangle(87, 1, 2, {"name": 87}, 4)

    def test_invalid_args_value(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rect = Rectangle(0, 1, 2, 3, 4)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rect = Rectangle(-7, 2, 2, 3, 4)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rect = Rectangle(89, 0, 8, 3, 4)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rect = Rectangle(87, -908, 2, 89, 4)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            rect = Rectangle(900, 1, -90, 3, 4)
        rect = Rectangle(1, 2, 0, 3, 4)
        self.assertEqual(rect.x, 0)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            rect = Rectangle(90, 1, 0, -90, 4)
        rect = Rectangle(1, 2)
        self.assertEqual(rect.y, 0)

    def test_setter(self):
        rect = Rectangle(909, 1, 2, 3, 4)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rect.width = 0
        rect = Rectangle(98, 2, 2, 3, 4)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rect.width = -7
        rect = Rectangle(89, 78, 8, 3, 4)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rect.height = 0
        rect = Rectangle(87, 908, 2, 89, 4)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rect.height = -987
        rect = Rectangle(900, 1, 987, 3, 4)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            rect.x = -65
        rect = Rectangle(1, 2, 90, 3, 4)
        rect.x = 0
        self.assertEqual(rect.x, 0)
        rect = Rectangle(90, 1, 0, 90, 4)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            rect.y = -32
        rect = Rectangle(1, 2, 5, 89)
        rect.y = 0
        self.assertEqual(rect.y, 0)

    def test_area(self):
        rect = Rectangle(45, 67, 90, 876)
        self.assertEqual(rect.area(), 45 * 67)

    def test_stringify(self):
        rect = Rectangle(4, 6, 2, 1, 12)
        string = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(str(rect), string)
        rect = Rectangle(5, 5, 1)
        string = "[Rectangle] (" + str(rect.id) + ") 1/0 - 5/5"
        self.assertEqual(str(rect), string)

    def test_update1(self):
        rect = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(rect), "[Rectangle] (" + str(rect.id) + ") 10/10 - 10/10")
        rect.update(89)
        self.assertEqual(str(rect), "[Rectangle] (89) 10/10 - 10/10")
        rect.update(89, 2)
        self.assertEqual(str(rect), "[Rectangle] (89) 10/10 - 2/10")
        rect.update(89, 2, 3)
        self.assertEqual(str(rect), "[Rectangle] (89) 10/10 - 2/3")
        rect.update(89, 2, 3, 4)
        self.assertEqual(str(rect), "[Rectangle] (89) 4/10 - 2/3")
        rect.update(89, 2, 3, 4, 5)
        self.assertEqual(str(rect), "[Rectangle] (89) 4/5 - 2/3")

    def test_update2(self):
        rect = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(rect), "[Rectangle] (" + str(rect.id) + ") 10/10 - 10/10")
        rect.update(height=1)
        self.assertEqual(str(rect), "[Rectangle] (" + str(rect.id) + ") 10/10 - 10/1")
        rect.update(width=1, x=2)
        self.assertEqual(str(rect), "[Rectangle] (" + str(rect.id) + ") 2/10 - 1/1")
        rect.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(rect), "[Rectangle] (" + str(rect.id) + ") 3/1 - 2/1")
        rect.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(rect), "[Rectangle] (" + str(rect.id) + ") 1/3 - 4/2")

    def test_update1and2(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(98, width=90, height=789, id=90)
        self.assertEqual(str(rect), "[Rectangle] (98) 3/4 - 1/2")

    def test_display1(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        rect = Rectangle(4, 6)
        rect.display()
        string = captured_output.getvalue().strip()
        self.assertEqual(string, ((("#" * 4) + "\n") * 6)[:-1])
        sys.stdout = sys.__stdout__
        captured_output.close()
        captured_output = io.StringIO()
        sys.stdout = captured_output
        rect = Rectangle(2, 2)
        rect.display()
        string = captured_output.getvalue().strip()
        self.assertEqual(string, ((("#" * 2) + "\n") * 2)[:-1])
        sys.stdout = sys.__stdout__

    def test_display2(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        rect = Rectangle(2, 3, 2, 2)
        rect.display()
        string = captured_output.getvalue().rstrip(" ")
        self.assertEqual(string, "\n\n" + (("  ##" + "\n") * 3))
        sys.stdout = sys.__stdout__

    def test_to_dictionary(self):
        rect = Rectangle(10, 2, 1, 9, 1000)
        rect_dict = rect.to_dictionary()
        self.assertEqual(rect_dict, {"id": 1000, "width": 10, "height": 2, "x": 1, "y": 9, "id": 1000})


if __name__ == "__main__":
    unittest.main()
