class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Поповнено на " + str(amount) + ". Баланс: " + str(self.balance))

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Знято " + str(amount) + ". Баланс: " + str(self.balance))
        else:
            print("Недостатньо коштів")


account = BankAccount("UA12345", 1000)
account.deposit(500)
account.withdraw(300)
account.withdraw(2000)
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return str(self.year) + " " + self.make + " " + self.model


my_car = Car("Toyota", "Camry", 2020)
print(my_car.get_info())
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)


rect = Rectangle(10, 5)

print("Площа: " + str(rect.calculate_area()))
print("Периметр: " + str(rect.calculate_perimeter()))