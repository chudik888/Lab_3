import unittest
from lab1.lab1 import price_to_float, percent_to_float, calculate_tip

class TestPriceFunctions(unittest.TestCase):

    def test_price_to_float(self):
        """Тест для функції price_to_float."""
        result = price_to_float("$10.50")
        self.assertEqual(result, 10.50)
        
        result = price_to_float("  $20.99 ")
        self.assertEqual(result, 20.99)
        
        result = price_to_float("$0.99")
        self.assertEqual(result, 0.99)

    def test_percent_to_float(self):
        """Тест для функції percent_to_float."""
        result = percent_to_float("15%")
        self.assertEqual(result, 0.15)
        
        result = percent_to_float("  20% ")
        self.assertEqual(result, 0.20)
        
        result = percent_to_float("5%")
        self.assertEqual(result, 0.05)

    def test_calculate_tip(self):
        """Тест для функції calculate_tip."""
        result = calculate_tip("$100.00", "15%")
        self.assertEqual(result, 15.00)
        
        result = calculate_tip("$50.00", "20%")
        self.assertEqual(result, 10.00)
        
        result = calculate_tip("$200.00", "10%")
        self.assertEqual(result, 20.00)

    def test_invalid_price(self):
        """Тест для некоректного формату ціни."""
        with self.assertRaises(ValueError):
            price_to_float("invalid price")

    def test_invalid_percent(self):
        """Тест для некоректного формату відсотків."""
        with self.assertRaises(ValueError):
            percent_to_float("invalid percent")

    def test_calculate_tip_invalid_input(self):
        """Тест для некоректних вхідних даних для calculate_tip."""
        with self.assertRaises(ValueError):
            calculate_tip("invalid price", "15%")
        with self.assertRaises(ValueError):
            calculate_tip("$100.00", "invalid percent")

if __name__ == "__main__":
    unittest.main()
