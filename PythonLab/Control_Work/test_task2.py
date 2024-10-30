import unittest
from task2 import process_scores

class TestProcessScores(unittest.TestCase):
    
    def test_normal_case(self):
        scores = [("Анна", 85), ("Олег", 75), ("Марія", 80), ("Іван", 90)]
        expected_output = {'Іван': 90, 'Анна': 85}
        result = process_scores(scores)
        print(f"Normal case - Expected: {expected_output}, Got: {result}")
        self.assertEqual(result, expected_output)
    
    def test_all_above_average(self):
        scores = [("Іван", 95), ("Олег", 95), ("Марія", 95)]
        expected_output = {'Іван': 95, 'Олег': 95, 'Марія': 95}
        result = process_scores(scores)
        print(f"Normal case - Expected: {expected_output}, Got: {result}")
        self.assertEqual(result, expected_output)
    
    def test_all_below_average(self):
        scores = [("Олег", 50), ("Марія", 40)]
        expected_output = {'Олег': 50}  
        result = process_scores(scores)
        print(f"Normal case - Expected: {expected_output}, Got: {result}")
        self.assertEqual(result, expected_output)

    def test_multiple_same_scores(self):
        scores = [("Анна", 85), ("Іван", 80), ("Марія", 75), ("Олег", 75)]
        expected_output = {'Анна': 85, 'Іван': 80}
        result = process_scores(scores)
        print(f"Normal case - Expected: {expected_output}, Got: {result}")
        self.assertEqual(result, expected_output)

    def test_empty_list(self):
        scores = []
        expected_output = {}
        result = process_scores(scores)
        print(f"Normal case - Expected: {expected_output}, Got: {result}")
        self.assertEqual(result, expected_output)

    def test_invalid_data(self):
        scores = [("Анна", "eighty"), ("Олег", 75), (123, 80)]  # Некоректні дані
        expected_output = "Неправильний формат. Спробуйте ще раз."
        with self.assertRaises(ValueError):  # Переконатися, що ValueError піднімається
            process_scores(scores)

if __name__ == '__main__':
    unittest.main()
