class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        return f"{self.name} - {self.price} RSD, količina: {self.quantity}"

    def update_quantity(self, amount):
        self.quantity += amount
