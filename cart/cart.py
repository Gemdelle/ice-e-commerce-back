"""
Este módulo contiene la clase Cart.
"""
from typing import List
from cart.cart_product import CartProduct
from products.products import Product


class Cart:
    """
    Clase que contiene una lista de CartProduct.
    """
    def __init__(self):
        """
        Constructor que inicializa los atributos.
        Parámetros:
        Atributos:
            products (List[CartProduct]): La lista que almacenará los CartProduct seleccionados por el usuario.
        """
        self.products: List[CartProduct] = []

    @property
    def total_price(self) -> float:
        """
        Propiedad que calcula el precio total a pagar por el usuario en función de los productos existentes en el Cart.
        Parámetros:
        Retorno:
            float: suma total de los productos existentes en el Cart.
        """
        return sum(product.total_price for product in self.products)

    def add_product(self, product: Product, quantity: int) -> None:
        """
        Función que añade una cantidad de un producto al Cart.
        Parámetros:
            Product: Producto a agregar.
            int: Cantidad de producto a agregar.
        Retorno:
        """
        existing_product = next((p for p in self.products if p.product.id == product.id), None)
        if existing_product:
            existing_product.quantity += quantity
        else:
            self.products.append(CartProduct(product, quantity))

    def remove_product(self, product_id: int) -> bool:
        """
        Funcioón que que elimina un producto del Cart.
        Parámetros:
            Product: Producto a agregar.
            int: Cantidad de producto a agregar.
        Retorno:
            float: suma total de los productos existentes en el Cart.
        """
        initial_length = len(self.products)
        self.products = [p for p in self.products if p.product.id != product_id]
        return len(self.products) < initial_length

    def to_dict(self) -> dict:
        """
        Propiedad que convierte las propiedades de un Cart en un diccionario.
        Parámetros:
        Retorno:
            dict: Diccionario que se le devolverá al front-end.
        """
        return {
            "products": [p.to_dict() for p in self.products],
            "total_price": self.total_price
        }
