from abc import ABC, abstractmethod

class Medicine(ABC):
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = float(price)

    def total_price(self):
        return self.quantity * self.price * 1.1

    def info(self):
        return (f"{self.name} | Кількість: {self.quantity} | "
                f"Ціна за одиницю: {self.price:.2f} | "
                f"Разом: {self.total_price():.2f} | "
                f"Рецепт: {self.requires_prescription()} | "
                f"Зберігання: {self.storage_requirements()}")

    @abstractmethod
    def requires_prescription(self):
        pass

    @abstractmethod
    def storage_requirements(self):
        pass

class Antibiotic(Medicine):
    def requires_prescription(self):
        return True
    def storage_requirements(self):
        return "8–15°C, темне місце"

class Vitamin(Medicine):
    def requires_prescription(self):
        return False
    def storage_requirements(self):
        return "15–25°C, сухо"

class Vaccine(Medicine):
    def requires_prescription(self):
        return True
    def storage_requirements(self):
        return "2–8°C, холодильник"