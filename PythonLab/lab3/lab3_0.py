def reverse_exercise(list_: list[int]) -> None:
    n = len(list_)
    for i in range(n // 2):
        list_[i], list_[n - 1 - i] = list_[n - 1 - i], list_[i]

def main():
    # Приклад використання
    list_ = list(map(int, input("Введіть числа через пробіл: ").split(",")))
    reverse_exercise(list_)
    '''
    # Перевірка
    assert list_ == [2, 10, 5, 1]'''

    print("Перевернутий список:", list_)

if __name__ == "__main__":
    main()