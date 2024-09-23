from products.products import Product


class CartProduct:
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity

    @property
    def total_price(self) -> float:
        return self.quantity * self.product.price

    def to_dict(self) -> dict:
        return {
            "product": self.product.__dict__,
            "quantity": self.quantity,
            "total_price": self.total_price
        }
