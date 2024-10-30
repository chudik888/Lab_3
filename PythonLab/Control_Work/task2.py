import time

def process_scores(scores):
    if not scores:
        return {}# O(1), константна складність, оскільки лише повертає порожній словник

    for name, score in scores:
        if not isinstance(score, int):
            raise ValueError("Неправильний формат. Спробуйте ще раз.")

    total_score = sum(score for _, score in scores) # має складність O(n), оскільки потрібно пройти всі елементи в scores, щоб підсумувати бали
    average_score = total_score / len(scores) # має складність O(1), оскільки це лише операція ділення

    filtered_scores = {name: score for name, score in scores if score >= average_score} # має складність O(n), оскільки це ще одна ітерація по списку scores для відбору студентів із середнім або вищим балом
    sorted_scores = dict(sorted(filtered_scores.items(), key=lambda item: item[1], reverse=True)) # O(n) для отримання items, O(n log n) для сортування, O(n) для створення нового словника з відсортованих даних. Загальна складність цього підходу до сортування словника за значенням — O(n log n)

    return sorted_scores

def main():
    scores = []
    while True:
        user_input = input("Введіть ім'я та бали (формат: 'ім'я, бали') або 'стоп' для завершення: ")
        if user_input.lower() == 'стоп':
            break
        try:
            name, score = user_input.split(',')
            name = name.strip()
            score = int(score.strip())
            scores.append((name, score))
        except ValueError:
            print("Неправильний формат. Спробуйте ще раз.")

    start_time = time.time()
    
    result = process_scores(scores)

    end_time = time.time()

    print("Студенти, які отримали бали вище або дорівнюють середньому:")
    for name, score in result.items():
        print(f"{name}: {score}")

    print(f"\nЧас виконання функції: {end_time - start_time:.6f} секунд")

if __name__ == "__main__":
    main()


'''
  Оскільки операції O(n) і O(n log n) є основними, загальна складність часу функції process_scores — O(n log n)
  Cтруктури займають пам'ять пропорційно кількості студентів, тобто O(n), тому загальна складність пам'яті — O(n)
'''