import unittest
from lab8 import LinkedList

class TestLinkedList(unittest.TestCase):

    def setUp(self):
        """Ініціалізуємо список перед кожним тестом."""
        self.ll = LinkedList[int]()

    def test_len_empty(self):
        """Перевіряємо довжину порожнього списку."""
        self.assertEqual(len(self.ll), 0)

    def test_len_after_append(self):
        """Перевіряємо довжину після додавання елементів."""
        self.ll.append(1)
        self.ll.append(2)
        self.assertEqual(len(self.ll), 2)

    def test_append(self):
        """Перевіряємо, чи додаються елементи правильно."""
        self.ll.append(1)
        self.ll.append(2)
        self.assertEqual(str(self.ll), "1 => 2")

    def test_remove_existing_element(self):
        """Перевіряємо видалення існуючого елемента."""
        self.ll.append(1)
        self.ll.append(2)
        self.ll.remove(1)
        self.assertEqual(str(self.ll), "2")
        self.assertEqual(len(self.ll), 1)

    def test_remove_non_existing_element(self):
        """Перевіряємо видалення неіснуючого елемента."""
        self.ll.append(1)
        with self.assertRaises(ValueError):
            self.ll.remove(42)

    def test_reverse_empty_list(self):
        """Перевіряємо реверс порожнього списку."""
        reversed_ll = self.ll.reverse()
        self.assertEqual(str(reversed_ll), "")
        self.assertEqual(len(reversed_ll), 0)

    def test_reverse_non_empty_list(self):
        """Перевіряємо реверс непорожнього списку."""
        self.ll.append(1)
        self.ll.append(2)
        self.ll.append(3)
        reversed_ll = self.ll.reverse()
        self.assertEqual(str(reversed_ll), "3 => 2 => 1")
        self.assertEqual(len(reversed_ll), 3)
        # Переконуємося, що оригінальний список не змінено
        self.assertEqual(str(self.ll), "1 => 2 => 3")


if __name__ == "__main__":
    unittest.main()
