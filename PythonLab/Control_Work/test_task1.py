import unittest
from task1 import ShoppingCart

class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        self.cart = ShoppingCart()

    # Vanity tests (базова поведінка методів класа)
    def test_add_item(self):
        # Додаємо елемент і перевіряємо базову поведінку
        self.cart.add_item("Яблука", 0.5, 3)
        self.assertEqual(len(self.cart), 1)
        self.assertEqual(self.cart.total_cost, 1.5)

        # Додаємо інший елемент
        self.cart.add_item("Груші", 0.3, 5)
        self.assertEqual(len(self.cart), 2)
        self.assertEqual(self.cart.total_cost, 3.0)

        # Оновлюємо кількість існуючого товару
        self.cart.add_item("Яблука", 0.5, 2)
        self.assertEqual(len(self.cart), 2)
        self.assertEqual(self.cart.total_cost, 4.0)

    def test_len(self):
        # Перевіряємо кількість унікальних товарів
        self.assertEqual(len(self.cart), 0)
        self.cart.add_item("Яблука", 0.5, 3)
        self.assertEqual(len(self.cart), 1)

    def test_str(self):
        # Перевіряємо формат рядка
        self.cart.add_item("Яблука", 0.5, 3)
        self.cart.add_item("Груші", 0.3, 5)
        expected_output = (
            "Назва\tЦіна\tКількість\n"
            "Яблука\t0.50\t3\n"
            "Груші\t0.30\t5\n"
            "Загальна вартість: 3.00"
        )
        self.assertEqual(str(self.cart), expected_output)

    # Validation tests (тести на «погані» значення)
    def test_invalid_price(self):
        # Перевірка від'ємної ціни
        with self.assertRaises(ValueError):
            self.cart.add_item("Яблука", -0.5, 3)

    def test_invalid_quantity(self):
        # Перевірка нульової кількості
        with self.assertRaises(ValueError):
            self.cart.add_item("Груші", 0.3, 0)

        # Перевірка від'ємної кількості
        with self.assertRaises(ValueError):
            self.cart.add_item("Груші", 0.3, -1)

        # Перевірка нової негативної кількості
        with self.assertRaises(ValueError):
            self.cart.add_item('Banana', 0.1, -2)

if __name__ == '__main__':
    unittest.main()
