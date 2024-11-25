import unittest
from lab3_1 import get_numbers_in_between

class TestGetNumbersInBetween(unittest.TestCase):
    def test_example_1(self):
        a = [2, 4]
        b = [32, 16, 96]
        expected = [4, 8, 16]
        self.assertEqual(get_numbers_in_between(a, b), expected)

    def test_example_2(self):
        a = [6, 2]
        b = [24, 36]
        expected = [6, 12]
        self.assertEqual(get_numbers_in_between(a, b), expected)

    def test_example_3(self):
        a = [3, 4]
        b = [24, 48]
        expected = [12, 24]
        self.assertEqual(get_numbers_in_between(a, b), expected)

    def test_no_common_numbers(self):
        a = [5]
        b = [12]
        expected = []
        self.assertEqual(get_numbers_in_between(a, b), expected)

    def test_single_element_lists(self):
        a = [4]
        b = [16]
        expected = [4, 8, 16]
        self.assertEqual(get_numbers_in_between(a, b), expected)

    def test_empty_b(self):
        a = [4, 8]
        b = []
        with self.assertRaises(TypeError):  # Оскільки reduce() не працює з порожнім списком
            get_numbers_in_between(a, b)

if __name__ == "__main__":
    unittest.main()
