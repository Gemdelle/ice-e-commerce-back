from products.product import Product
from flask import jsonify


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

    def to_json(self):
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
