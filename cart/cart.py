"""
Este módulo contiene la clase Cart, que representa un carrito de compras con una lista de productos.
"""

from typing import List
from cart.cart_product import CartProduct
from products.product import Product


class Cart:
    """
    Clase que contiene una lista de CartProduct.

    Atributos:
        products (List[CartProduct]): La lista que almacenará los CartProduct seleccionados por el usuario.
    """

    def __init__(self):
        """
        Constructor que inicializa los atributos del carrito de compras.
        """
        self.products: List[CartProduct] = []

    @property
    def total_price(self) -> float:
        """
        Propiedad que calcula el precio total a pagar por el usuario en función de los productos existentes en el carrito.

        Retorna:
            float: La suma total de los productos existentes en el carrito.
        """
        return sum(product.total_price for product in self.products)

    def add_product(self, product: Product, quantity: int) -> None:
        """
        Función que añade una cantidad de un producto al carrito.

        Argumentos:
            product (Product): El producto a agregar.
            quantity (int): La cantidad de producto a agregar.
        """
        existing_product = next((p for p in self.products if p.product.id == product.id), None)
        if existing_product:
            existing_product.quantity += quantity
        else:
            self.products.append(CartProduct(product, quantity))

    def remove_product(self, product_id: int) -> bool:
        """
        Función que elimina un producto del carrito.

        Argumentos:
            product_id (int): El ID del producto a eliminar.

        Retorna:
            bool: True si el producto fue eliminado, False en caso contrario.
        """
        initial_length = len(self.products)
        self.products = [p for p in self.products if p.product.id != product_id]
        return len(self.products) < initial_length

    def to_dict(self) -> dict:
        """
        Propiedad que convierte las propiedades del carrito en un diccionario.

        Retorna:
            dict: Diccionario que representa los productos en el carrito y el precio total.
        """
        return {
            "products": [p.to_dict() for p in self.products],
            "total_price": self.total_price
        }
