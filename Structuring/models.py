from abc import ABC, abstractmethod

class Medicine(ABC):
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = float(price)

    def total_price(self):
        return self.quantity * self.price * 1.1  

    def info(self):
        return (f"{self.name} | Quantity: {self.quantity} | "
                f"Price per unit: {self.price:.2f} | "
                f"Total: {self.total_price():.2f} | "
                f"Prescription required: {self.requires_prescription()} | "
                f"Storage: {self.storage_requirements()}")

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
        return "8–15°C, dark place"


class Vitamin(Medicine):
    def requires_prescription(self):
        return False
    def storage_requirements(self):
        return "15–25°C, dry place"


class Vaccine(Medicine):
    def requires_prescription(self):
        return True
    def storage_requirements(self):
        return "2–8°C, refrigerator"
