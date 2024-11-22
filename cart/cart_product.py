"""
Este módulo contiene la clase CartProduct, que representa un producto dentro del carrito de compras.
"""
from products.product import Product


class CartProduct:
    """
    Clase que representa un producto en el carrito de compras (Cart).

    Atributos:
        product (Product): El producto que se agrega al carrito.
        quantity (int): La cantidad de unidades del producto en el carrito.
    """

    def __init__(self, product: Product, quantity: int):
        """
        Constructor que inicializa los atributos del producto en el carrito.

        Argumentos:
            product (Product): El producto que se va a agregar al carrito.
            quantity (int): La cantidad de unidades del producto a agregar.
        """
        self.product = product
        self.quantity = quantity

    @property
    def total_price(self) -> float:
        """
        Calcula el precio total basado en la cantidad de productos y el precio unitario.

        Retorna:
            float: El precio total de las unidades del producto.
        """
        return self.quantity * self.product.price

    def to_dict(self) -> dict:
        """
        Convierte las propiedades del CartProduct en un diccionario para ser enviado al front-end.

        Retorna:
            dict: Diccionario que representa el producto en el carrito, incluyendo el producto,
            la cantidad y el precio total.
        """
        return {
            "product": self.product.__dict__,  # Se usa __dict__ para convertir el objeto producto a un diccionario.
            "quantity": self.quantity,
            "total_price": self.total_price
        }
