from abc import ABC, abstractmethod
from flask import jsonify

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
    def toJson(self):
        """
        Método abstracto que debe ser implementado en las subclases para devolver el producto en formato JSON.
        """
        pass


class Tight(Product):
    """
    Subclase de Product que representa una prenda ajustada, como unas mallas.

    Argumentos:
        id (int): El ID único del producto.
        type (str): El tipo de producto.
        previewUrl (str): URL de vista previa del producto.
        size (str): El tamaño de la prenda.
        model (str): El modelo de la prenda.
        pattern (str): El patrón de la prenda.
        price (float): Precio de la prenda.
        stock (int): Cantidad en stock.
        strassColour (str): Color de las piedras (strass).
        strassQuantity (int): Cantidad de piedras (strass).
    """
    def __init__(self, id, type, preview_url, size, model, pattern, price, stock, strassColour, strassQuantity):
        super().__init__(id, type, preview_url, price)
        print(f"price: {price}")
        self._size = size
        self._model = model
        self._pattern = pattern
        self._stock = stock
        self._strassColour = strassColour
        self._strassQuantity = strassQuantity

    def toJson(self):
        """
        Devuelve los atributos de la prenda ajustada en formato JSON.

        Retorna:
            json: Un objeto JSON que representa la prenda ajustada.
        """
        return jsonify({
            "id": self._id,
            "type": self._type,
            "previewUrl": self._preview_url,
            "size": self._size,
            "model": self._model,
            "pattern": self._pattern,
            "price": self._price,
            "stock": self._stock,
            "strass_quantity": self._strassQuantity,
            "strass_colour": self._strassColour
        })


class Glove(Product):
    """
    Subclase de Product que representa un guante.

    Argumentos:
        id (int): El ID único del producto.
        type (str): El tipo de producto.
        previewUrl (str): URL de vista previa del producto.
        colour (str): El color del guante.
        model (str): El modelo del guante.
        pattern (str): El patrón del guante.
        price (float): Precio del guante.
        stock (int): Cantidad en stock.
        gemColour (str): Color de las gemas.
        gemOpacity (float): Opacidad de las gemas.
        strassColour (str): Color de las piedras (strass).
        strassQuantity (int): Cantidad de piedras (strass).
    """
    def __init__(self, id, type, preview_url, colour, model, pattern, price, stock, gemColour, gemOpacity, strassColour, strassQuantity):
        super().__init__(id, type, preview_url, price)
        self._colour = colour
        self._model = model
        self._pattern = pattern
        self._stock = stock
        self._gemColour = gemColour
        self._gemOpacity = gemOpacity
        self._strassColour = strassColour
        self._strassQuantity = strassQuantity

    def toJson(self):
        """
        Devuelve los atributos del guante en formato JSON.

        Retorna:
            json: Un objeto JSON que representa el guante.
        """
        return jsonify({
            "id": self._id,
            "type": self._type,
            "previewUrl": self._preview_url,
            "colour": self._colour,
            "model": self._model,
            "pattern": self._pattern,
            "price": self._price,
            "stock": self._stock,
            "gem_colour": self._gemColour,
            "gem_opacity": self._gemOpacity,
            "strass_colour": self._strassColour,
            "strass_quantity": self._strassQuantity,
        })
