class Person:
    def __init__(self, name):
        self.name = name

    def age(self, value):
        print(f"Вік: {value}")


class Driver(Person):
    def __init__(self, name, license_number):
        super().__init__(name)
        self.license_number = license_number