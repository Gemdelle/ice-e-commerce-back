"""
Este módulo contiene los productos que se comercializan, junto con la clase abstracta de la que heredan: Product().
"""

from abc import ABC, abstractmethod


class Product(ABC):
    """
    Clase abstracta que representa un producto. Define los atributos comunes y un método abstracto `toJson`.

    Argumentos:
        id (int): El ID único del producto.
        type (str): El tipo de producto.
        previewUrl (str): URL de vista previa del producto.
        price (float): Precio del producto.
    """

    def __init__(self, id, type, preview_url, price):
        self._id = id
        self._type = type
        self._preview_url = preview_url
        self._price = price

    @property
    def id(self):
        """
        Propiedad que devuelve el ID del producto.

        Retorna:
            int: El ID del producto.
        """
        return self._id

    @property
    def price(self):
        """
        Propiedad que devuelve el precio del producto.

        Retorna:
            float: El precio del producto.
        """
        return self._price

    @abstractmethod
    def to_json(self):
        """
        Método abstracto que debe ser implementado en las subclases para devolver el producto en formato JSON.
        """
        pass
