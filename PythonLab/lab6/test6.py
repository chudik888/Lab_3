import unittest
from lab6 import fibonacci

class TestFibonacci(unittest.TestCase):

    # Тести для функції fibonacci

    def test_fibonacci_valid(self):
        # Перевірка правильності обчислення числа Фібоначчі
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(6), 8)
        self.assertEqual(fibonacci(8), 21)
        self.assertEqual(fibonacci(10), 55)
        self.assertEqual(fibonacci(20), 6765)

    def test_fibonacci_invalid(self):
        # Перевірка на помилку при введенні невірних значень
        with self.assertRaises(ValueError):
            fibonacci(0)  # Число має бути додатнім

        with self.assertRaises(ValueError):
            fibonacci(-5)  # Число має бути додатнім

if __name__ == "__main__":
    unittest.main()