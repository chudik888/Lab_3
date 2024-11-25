import unittest
from lab2.lab2 import find_balance_point

class TestFindBalancePoint(unittest.TestCase):
    def test_single_balance_point(self):
        self.assertEqual(find_balance_point([19, 25, 5, 42, 38, 8, 34, 16, 14, 8, 47, 42, 4, 20, 23]), 7)
    
    def test_no_balance_point(self):
        self.assertEqual(find_balance_point([6, 6, 9]), -1)

    def test_multiple_elements(self):
        self.assertEqual(find_balance_point([43, 51, 35, 4]), 1)

    def test_empty_list(self):
        self.assertEqual(find_balance_point([]), -1)

    def test_one_element(self):
        self.assertEqual(find_balance_point([7, 24, 3, 38]), 2)

if __name__ == "__main__":
    unittest.main()