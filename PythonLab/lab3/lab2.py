def find_balance_point(weights):
    total_weight = sum(weights)  # Обчислюємо загальну масу
    n = len(weights)  # Кількість вагів
    left_weight = 0  # Ліва вага

    # Перебираємо кожну вагу як потенційну точку опори
    for i in range(n):
        # Розрахунок моментів ліворуч
        left_moment = sum(weights[j] * (i - j) for j in range(i))  # Моменти зліва

        # Розрахунок моментів праворуч
        right_moment = sum(weights[j] * (j - i) for j in range(i + 1, n))  # Моменти справа

        # Порівнюємо ліві і праві моменти
        if left_moment == right_moment:
            return i  # Повертаємо індекс точки опори

    return -1  # Якщо не знайдено

user_input = input("Введіть ваги через кому: ")
weights = list(map(int, user_input.split(',')))  # Розділяємо введений рядок за комами та перетворюємо в цілі числа

# Виклик функції та вивід результату
result = find_balance_point(weights)
print("Індекс точки опори:", result)