from typing import Self
from math import sqrt

class Complex:
    def __init__(self, _re: float = 0., _im: float = 0.) -> None:
        self.__re = _re
        self.__im = _im

    def __str__(self) -> str:
        return f"{self.real} + {self.imaginary}*i"

    @property
    def real(self) -> float:
        return self.__re

    @real.setter
    def real(self, val: float) -> None:
        self.__re = val

    @property
    def imaginary(self) -> float:
        return self.__im

    @imaginary.setter
    def imaginary(self, val: float) -> None:
        self.__im = val

    def __add__(self, other: Self) -> Self:  # Додавання
        return Complex(self.__re + other.real, self.__im + other.imaginary)

    def __sub__(self, other: Self) -> Self:  # Віднімання
        return Complex(self.__re - other.real, self.__im - other.imaginary)

    def __mul__(self, other: Self) -> Self:  # Множення
        re = self.__re * other.real - self.__im * other.imaginary
        im = self.__re * other.imaginary + self.__im * other.real
        return Complex(re, im)

    def __truediv__(self, other: Self) -> Self:  # Ділення
        denominator = other.real**2 + other.imaginary**2
        if denominator == 0:
            raise ZeroDivisionError("Cannot divide by zero complex number")
        re = (self.__re * other.real + self.__im * other.imaginary) / denominator
        im = (self.__im * other.real - self.__re * other.imaginary) / denominator
        return Complex(re, im)

    def __abs__(self) -> float:  # Модуль
        return sqrt(self.__re**2 + self.__im**2)

    def __eq__(self, other: Self) -> bool:  # Перевірка на рівність
        return self.__re == other.real and self.__im == other.imaginary

    def __ne__(self, other: Self) -> bool:  # Перевірка на нерівність
        return not self == other
    
    def __iadd__(self, other: Self) -> Self:  # Інкрементарне додавання
        self.__re += other.real
        self.__im += other.imaginary
        return self
    
       
    def __isub__(self, other: Self) -> Self:  # Інкрементарне віднімання
        self.__re -= other.real
        self.__im -= other.imaginary
        return self
    
    def __imul__(self, other: Self) -> Self:  # Інкрементарне множення
        re = self.__re * other.real - self.__im * other.imaginary
        im = self.__re * other.imaginary + self.__im * other.real
        self.__re, self.__im = re, im
        return self
    
    def __itruediv__(self, other: Self) -> Self:  # Інкрементарне ділення
        denominator = other.real**2 + other.imaginary**2
        if denominator == 0:
            raise ZeroDivisionError("Cannot divide by zero complex number")
        re = (self.__re * other.real + self.__im * other.imaginary) / denominator
        im = (self.__im * other.real - self.__re * other.imaginary) / denominator
        self.__re, self.__im = re, im
        return self

def input_complex(prompt: str) -> Complex:
    """Функція для вводу комплексного числа користувачем"""
    re = float(input(f"{prompt} Введіть дійсну частину: "))
    im = float(input(f"{prompt} Введіть уявну частину: "))
    return Complex(re, im)


if __name__ == "__main__":
    print("Введіть перше комплексне число:")
    c1 = input_complex("Число 1")

    print("\nВведіть друге комплексне число:")
    c2 = input_complex("Число 2")

    # Використовуємо операції без виклику __iadd__ безпосередньо
    print("\nВиконання операцій:")

    c3 = c1 + c2  # Додавання
    print(f"c3 = c1 + c2 = {c3}")

    c4 = c1 - c2  # Віднімання
    print(f"c4 = c3 - c2 = {c4}")

    c5 = c1 * c2  # Множення
    print(f"c5 = c1 * c2 = {c5}")

    c6 = c1 / c2  # Ділення
    print(f"c6 = c5 / c2 = {c6}")

    # Інкрементні операції
    print("\nІнкрементні операції:")

    с3=c1.__iadd__(c2)  # c1 = c1 + c2
    print(f"c1 після інкрементного додавання: {c3}")

    с4=c1.__isub__(c2)  # c1 = c1 - c2
    print(f"c1 після інкрементного віднімання: {c4}")

    с5=c1.__imul__(c2)  # c1 = c1 * c2
    print(f"c1 після інкрементного множення: {c5}")

    с6=c1.__itruediv__(c2)  # c1 = c1 / c2
    print(f"c1 після інкрементного ділення: {c6}")

    print("\nМодуль c1:", abs(c1))  # Модуль c1
    print("c1 == c2:", c1 == c2)  # Порівняння на рівність
    print("c1 != c2:", c1 != c2)  # Порівняння на нерівність