class ShoppingCart:
    def __init__(self):
        self.__items = {}

    def add_item(self, name: str, price: float, quantity: int = 1):
        if price <= 0:
            raise ValueError("Ціна повинна бути більшою за 0.")
        if quantity <= 0:
            raise ValueError("Кількість повинна бути позитивною.")

        # Додаємо або оновлюємо товар у кошику
        if name not in self.__items:
            self.__items[name] = {"price": price, "quantity": 0}
        
        self.__items[name]["quantity"] += quantity  # Додаємо до кількості для даної назви
        
        return self

    @property
    def total_cost(self) -> float:
        """Повертає загальну вартість усіх товарів у кошику."""
        return sum(item["price"] * item["quantity"] for item in self.__items.values())

    def __len__(self):
        """Повертає кількість унікальних товарів у кошику."""
        return len(self.__items)

    def __str__(self):
        """Повертає строкове представлення кошика."""
        result = "Назва\tЦіна\tКількість\n"
        for name, details in self.__items.items():
            result += f"{name}\t{details['price']:.2f}\t{details['quantity']}\n"
        result += f"Загальна вартість: {self.total_cost:.2f}"
        return result

def main():
    cart = ShoppingCart()
    
    while True:
        user_input = input("Введіть товар (назва, ціна, кількість) або 'exit' для виходу: ")
        if user_input.lower() == 'exit':
            break
        
        try:
            name, price, quantity = user_input.split(',')
            name = name.strip()
            price = float(price.strip())
            quantity = int(quantity.strip())
            cart.add_item(name, price, quantity)
            print(f"Товар '{name}' додано до кошика.")
            print(cart)
            print(f"Кількість унікальних товарів у кошику: {len(cart)}")  # Вивід кількості унікальних товарів
        except ValueError as e:
            print(f"Помилка: {e}. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
