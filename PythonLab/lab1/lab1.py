def price_to_float(price_str: str) -> float:
    # Видалити знак долара та перетворити рядок ціни на float
    return float(price_str.replace("$", "").strip())

def percent_to_float(percent_str: str) -> float:
    # Видалити знак процента та перетворити рядок відсотків на float
    return float(percent_str.replace("%", "").strip()) / 100

def calculate_tip(price_str: str, tip_percentage_str: str) -> float:
    # Перетворити ціну та відсотки
    price = price_to_float(price_str)
    tip_percentage = percent_to_float(tip_percentage_str)
    
    # Розрахувати чайові
    return price * tip_percentage

def main():
    # Запитати у користувача введення ціни та відсотків
    price = input("Введіть ціну (формат $xx.xx): ")
    tip_percentage = input("Введіть відсоток чайових (формат yy%): ")
    
    # Розрахувати чайові
    tip = calculate_tip(price, tip_percentage)
    
    # Вивести результат
    print(f"Кількість чайових: ${tip:.2f}")

# Викликаємо основну функцію
if __name__ == "__main__":
    main()
