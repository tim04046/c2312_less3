class Human:
    def __init__(self, name):
        self.name = name


class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passengers(self, human):
        self.passengers.append(human)

    def print_passengers(self):
        if not self.passengers:
            print(f"В авто {self.brand} немає пасажирів!")
            return
        print(f"Пасажири {self.brand}:")
        for p in self.passengers:
            print(" - ", p.name)


tim = Human("Timofiy")
kate = Human("Kate")
car = Auto("Ferrari")
car.add_passengers(tim)
car.add_passengers(kate)

car.print_passengers()  
