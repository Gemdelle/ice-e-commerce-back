"""
Este módulo contiene la clase CartProduct.
"""
from products.products import Product


class CartProduct:
    """
    Clase que representa el producto en Cart.
    """
    def __init__(self, product: Product, quantity: int):
        """
        Constructor que inicializa los atributos.
        Parámetros:
            Product: Producto.
            quantity: Cantidad de unidades del producto a agregar al Cart.
        Atributos:
            Product: Producto.
            quantity: Cantidad de unidades del producto a agregar al Cart.
        """
        self.product = product
        self.quantity = quantity

    @property
    def total_price(self) -> float:
        """
        Propiedad que calcula el precio total a pagar por el producto.
        Parámetros:
        Retorno:
            float: suma total del producto según la cantidad.
        """
        return self.quantity * self.product.price

    def to_dict(self) -> dict:
        """
        Propiedad que convierte las propiedades de un CartProduct en un diccionario.
        Parámetros:
        Retorno:
            dict: Diccionario que se le devolverá al front-end.
        """
        return {
            "product": self.product.__dict__,
            "quantity": self.quantity,
            "total_price": self.total_price
        }
