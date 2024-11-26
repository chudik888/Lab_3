def count_rotations(nums: list[int]) -> int:

    print(f"Вхідний список: {nums}")
    low, high = 0, len(nums) - 1

    while low < high:
        print(f"Поточні межі: low={low}, high={high}")

        mid = (low + high) // 2
        print(f"Середина: mid={mid}, значення={nums[mid]}")

        # Якщо середній елемент менший за останній, мінімум ліворуч
        if nums[mid] < nums[high]:
            high = mid
        # Якщо середній елемент більший за останній, мінімум праворуч
        elif nums[mid] > nums[high]:
            low = mid + 1
        # Якщо nums[mid] == nums[high], зменшуємо праву межу
        else:
            high -= 1

    print(f"Мінімум знайдено на індексі: {low}")
    return low

if __name__ == "__main__":
    # Запит у користувача на введення списку
    user_input = input("Введіть список чисел, розділених пробілом: ")
    try:
        nums = list(map(int, user_input.split()))
        result = count_rotations(nums)
        print(f"Кількість циклічних зсувів: {result}")
    except ValueError:
        print("Будь ласка, введіть коректний список цілих чисел.")

    """
    Функція визначає кількість циклічних зсувів, зроблених для отримання даного списку з початково відсортованого списку.
    Використовується бінарний пошук для знаходження індексу мінімального елемента.
    Складність: O(log n), де n - довжина списку.
    
    :param nums: Список чисел, отриманий циклічним зсувом відсортованого списку.
    :return: Кількість зсувів.
    """