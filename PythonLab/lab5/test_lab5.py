import unittest
from lab5 import Complex  # Імпортуємо клас Complex з файлу з основною програмою

class TestComplexOperations(unittest.TestCase):

    def setUp(self):
        """Функція, яка виконується перед кожним тестом."""
        self.c1 = Complex(3, 2)
        self.c2 = Complex(1, -1)

    def test_addition(self):
        """Тест для операції додавання."""
        result = self.c1 + self.c2
        self.assertEqual(result.real, 4)
        self.assertEqual(result.imaginary, 1)

    def test_subtraction(self):
        """Тест для операції віднімання."""
        result = self.c1 - self.c2
        self.assertEqual(result.real, 2)
        self.assertEqual(result.imaginary, 3)

    def test_multiplication(self):
        """Тест для операції множення."""
        result = self.c1 * self.c2
        self.assertEqual(result.real, 5)
        self.assertEqual(result.imaginary, -1)

    def test_division(self):
        """Тест для операції ділення."""
        result = self.c1 / self.c2
        self.assertEqual(result.real, 0.5)
        self.assertEqual(result.imaginary, 2.5)

    def test_increment_addition(self):
        """Тест для інкрементного додавання."""
        self.c1 += self.c2
        self.assertEqual(self.c1.real, 4)
        self.assertEqual(self.c1.imaginary, 1)

    def test_increment_subtraction(self):
        """Тест для інкрементного віднімання."""
        self.c1 -= self.c2
        self.assertEqual(self.c1.real, 2)
        self.assertEqual(self.c1.imaginary, 3)

    def test_increment_multiplication(self):
        """Тест для інкрементного множення."""
        self.c1 *= self.c2
        self.assertEqual(self.c1.real, 5)
        self.assertEqual(self.c1.imaginary, -1)

    def test_increment_division(self):
        """Тест для інкрементного ділення."""
        self.c1 /= self.c2
        self.assertEqual(self.c1.real, 0.5)
        self.assertEqual(self.c1.imaginary, 2.5)

    def test_equality(self):
        """Тест для порівняння рівності."""
        c3 = Complex(3, 2)
        self.assertTrue(self.c1 == c3)
        self.assertFalse(self.c1 == self.c2)

    def test_inequality(self):
        """Тест для порівняння нерівності."""
        self.assertTrue(self.c1 != self.c2)
        self.assertFalse(self.c1 != Complex(3, 2))

    def test_absolute(self):
        """Тест для функції модулю."""
        self.assertEqual(abs(self.c1), 3.605551275463989)
        self.assertEqual(abs(self.c2), 1.4142135623730951)
        self.assertEqual(abs(self.c1+self.c2), 4.123105625617661)

if __name__ == "__main__":
    unittest.main()
