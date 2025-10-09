class Transport:
    def __init__(self, name, speed, capacity):
        self.name = name
        self.speed = speed
        self.capacity = capacity

    def move(self, distance):
        return distance / self.speed

    def fuel(self, distance):
        return 0

    def info(self):
        return f"{self.name}: швидкість {self.speed} км/год, місць {self.capacity}"

class Car(Transport):
    def fuel(self, distance):
        return distance * 0.07

class Bus(Transport):
    def fuel(self, distance):
        return distance * 0.15

class Bicycle(Transport):
    def move(self, distance):
        time1 = distance / self.speed
        time2 = distance / 20
        if time1 > time2:
            return time2
        else:
            return time1

    def fuel(self, distance):
        return 0

class ElectricCar(Car):
    def __init__(self, name, speed, capacity, battery_capacity):
        self.name = name
        self.speed = speed
        self.capacity = capacity
        self.battery_capacity = battery_capacity

    def fuel(self, distance):
        return distance * 0.05

    def battery_usage(self, distance):
        return (distance / 100) * self.battery_capacity

car = Car("Автомобіль", 100, 5)
bus = Bus("Автобус", 80, 50)
bicycle = Bicycle("Велосипед", 15, 1)
electric_car = ElectricCar("Електрокар", 90, 4, 50)

transports = [car, bus, bicycle, electric_car]

for t in transports:
    print(t.info())
    print("Час для 100 км:", round(t.move(100), 2), "годин")
    print("Витрата пального:", round(t.fuel(100), 2))
    if t == electric_car:
        print("Витрата батареї:", round(t.battery_usage(100), 2), "кВт·год")
    print()