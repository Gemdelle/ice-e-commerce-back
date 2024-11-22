from flask import jsonify

from products.product import Product


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

    def __init__(self, id, type, preview_url, colour, model, pattern, price, colour_code, pattern_elements, default_colour_code):
        super().__init__(id, type, preview_url, price)
        self._colour = colour
        self._model = model
        self._pattern = pattern
        self._colour_code = colour_code
        self._pattern_elements = pattern_elements
        self._default_colour_code = default_colour_code

    def to_json(self):
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
            "colour_code": self._colour_code,
            "pattern_elements": self._pattern_elements,
            "default_colour_code": self._default_colour_code,
        })
