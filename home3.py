class Product:
    def __init__(self, name, price, in_stock):
        self.name = name
        self.price = price
        self.in_stock = in_stock


class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)

    def calculate_total(self):
        total = 0
        for product in self.products:
            total += product.price
        return total

    def print_cart(self):
        if self.products != []:
            print("Кошик покупця:")
            for product in self.products:
                print(f"- {product.name}: {product.price} грн")
            print(f"Загальна вартість: {self.calculate_total()} грн")
        else:
            print("Кошик порожній")


product1 = Product("Товар 1", 100, True)
product2 = Product("Товар 2", 200, True)

cart = Cart()

cart.add_product(product1)
cart.add_product(product2)

cart.print_cart()
