from typing import Callable

# Декоратор для кешування результатів функції
def cached(func: Callable[[int], int]) -> Callable[[int], int]:
    cache = {}  # Словник для збереження результатів
    def wrapper(n: int) -> int:
        if n in cache:
            return cache[n]  # Повернути значення з кешу
        result = func(n)   # Обчислити значення
        cache[n] = result  # Зберегти результат у кеш
        return result
    return wrapper

# Функція для обчислення числа Фібоначчі
@cached
def fibonacci(n: int) -> int:
    if n <= 0:
        raise ValueError("Число має бути додатнім.")
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# Основний блок виконання програми
if __name__ == "__main__":
    try:
        n = int(input("Введіть номер числа Фібоначчі: "))
        result = fibonacci(n)
        print(f"{n}-те число Фібоначчі: {result}")
    except ValueError as e:
        print(f"Помилка: {e}")
