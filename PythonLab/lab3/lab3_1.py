import math
from functools import reduce

def get_numbers_in_between(a: list[int], b: list[int]) -> list[int]:
    """Функція для знаходження чисел між двома множинами"""
    # Знаходимо НСК для першого списку і НСД для другого
    lcm_a = reduce(lambda x, y: x * y // math.gcd(x, y), a)
    gcd_b = reduce(math.gcd, b)
    
    # Пошук чисел між НСК і НСД
    return [num for num in range(lcm_a, gcd_b + 1, lcm_a) if gcd_b % num == 0]

def main():
# Введення списків користувачем
    a = list(map(int, input("Введіть числа для першого списку (через пробіл): ").split()))
    b = list(map(int, input("Введіть числа для другого списку (через пробіл): ").split()))

    # Виклик функції та виведення результату
    result = get_numbers_in_between(a, b)
    print("Числа, які підходять:", result)

    """
    Examples:
    a = [2, 4], b = [32, 16, 96] -> [4, 8, 16]
    a = [6, 2], b = [24, 36]     -> [6, 12]
    a = [3, 4], b = [24, 48]     -> [12, 24]
    """

if __name__ == "__main__":
    main()