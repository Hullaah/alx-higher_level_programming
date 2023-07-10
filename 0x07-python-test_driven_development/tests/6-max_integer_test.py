import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_normal(self):
        result = max_integer([1, 2, 3, 4 , 5])
        self.assertEqual(result, 5)
    def test_max_negative(self):
        result = max_integer([-1, -2, -3, -4, -5, -6])
        self.assertEqual(result, -1)
    def test_empty(self):
        result = max_integer([])
        self.assertEqual(result, None)
    def test_one_element(self):
        result = max_integer([1])
        self.assertEqual(result, 1)
    def test_middle_element(self):
        result = max_integer([1, 2, 5, 3, 4])
        self.assertEqual(result, 5)


if __name__ == "__main__":
    unittest.main()
