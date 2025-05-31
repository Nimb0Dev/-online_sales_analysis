from product import Product
from product_manager import ProductManager
from cart import Cart

cart = Cart()
cart.add_to_cart(ProductManager.products[0])
cart.add_to_cart(ProductManager.products[1])
cart.add_to_cart(ProductManager.products[2])

print("Sadržaj korpe:")
cart.show_cart()
print("Ukupna vrednost za naplatu:", cart.total_price(), "RSD")

manager = ProductManager()

# Dodavanje proizvoda
manager.add_product(Product("Laptop", 70000, 5))
manager.add_product(Product("Bežični Miš", 1500, 15))
manager.add_product(Product("Tastatura", 2500, 7))

