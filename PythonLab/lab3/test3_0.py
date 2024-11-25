import unittest
from lab3_0 import reverse_exercise

class TestReverseExercise(unittest.TestCase):
    def test_even_length_list(self):
        data = [1, 2, 3, 4]
        reverse_exercise(data)
        self.assertEqual(data, [4, 3, 2, 1])

    def test_odd_length_list(self):
        data = [1, 2, 3, 4, 5]
        reverse_exercise(data)
        self.assertEqual(data, [5, 4, 3, 2, 1])

    def test_single_element_list(self):
        data = [1]
        reverse_exercise(data)
        self.assertEqual(data, [1])

    def test_empty_list(self):
        data = []
        reverse_exercise(data)
        self.assertEqual(data, [])

    def test_negative_numbers(self):
        data = [-1, -2, -3, -4]
        reverse_exercise(data)
        self.assertEqual(data, [-4, -3, -2, -1])

    def test_mixed_numbers(self):
        data = [1, -2, 0, 4, -5]
        reverse_exercise(data)
        self.assertEqual(data, [-5, 4, 0, -2, 1])

if __name__ == "__main__":
    unittest.main()
