import unittest
from lab7 import count_rotations

class TestCountRotations(unittest.TestCase):
    def test_standard_cases(self):
        self.assertEqual(count_rotations([15, 18, 2, 3, 6, 12]), 2)
        self.assertEqual(count_rotations([7, 1, 2, 3, 4, 5, 6]), 1)
        self.assertEqual(count_rotations([4, 5, 6, 7, 1, 2, 3]), 4)

    def test_no_rotation(self):
        self.assertEqual(count_rotations([1, 2, 3, 4, 5, 6, 7]), 0)

    def test_duplicates(self):
        self.assertEqual(count_rotations([10, 10, 10, 1, 10, 10]), 3)

    def test_edge_cases(self):
        self.assertEqual(count_rotations([1]), 0)  # Single element
        self.assertEqual(count_rotations([2, 1]), 1)  # Two elements

    def test_additional_cases(self):
        self.assertEqual(count_rotations([3, 4, 5, 6, 1, 2]), 4)
        self.assertEqual(count_rotations([1, 2, 3, 4, 5]), 0)
        self.assertEqual(count_rotations([2, 3, 4, 5, 1]), 4)

if __name__ == "__main__":
    unittest.main()
