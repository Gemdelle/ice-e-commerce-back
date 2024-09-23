from typing import List

from cart.cart_product import CartProduct
from products.products import Product

class Cart:
    def __init__(self):
        self.products: List[CartProduct] = []

    @property
    def total_price(self) -> float:
        return sum(product.total_price for product in self.products)

    def add_product(self, product: Product, quantity: int) -> None:
        existing_product = next((p for p in self.products if p.product.id == product.id), None)
        if existing_product:
            existing_product.quantity += quantity
        else:
            self.products.append(CartProduct(product, quantity))

    def remove_product(self, product_id: int) -> bool:
        initial_length = len(self.products)
        self.products = [p for p in self.products if p.product.id != product_id]
        return len(self.products) < initial_length

    def to_dict(self) -> dict:
        return {
            "products": [p.to_dict() for p in self.products],
            "total_price": self.total_price
        }
