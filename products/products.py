from abc import ABC, abstractmethod
from flask import jsonify


class Product(ABC):
    def __init__(self, id, type, previewUrl):
        self._id = id
        self._type = type
        self._previewUrl = previewUrl

    @property
    def id(self):
        return self._id

    @abstractmethod
    def toJson(self):
        pass


class Tight(Product):
    def __init__(self, id, type, previewUrl, size, model, pattern, price, stock, strassColour, strassQuantity):
        super().__init__(id, type, previewUrl)
        print(f"price: {price}")
        self._size = size
        self._model = model
        self._pattern = pattern
        self._price = price
        self._stock = stock
        self._strassColour = strassColour
        self._strassQuantity = strassQuantity

    @property
    def price(self):
        return self._price

    def toJson(self):
        return jsonify({
            "id": self._id,
            "type": self._type,
            "previewUrl": self._previewUrl,
            "size": self._size,
            "model": self._model,
            "pattern": self._pattern,
            "price": self._price,
            "stock": self._stock,
            "strass_quantity": self._strassQuantity,
            "strass_colour": self._strassColour
        })


class Glove(Product):
    def __init__(self, id, type, previewUrl, colour, model, pattern, price, stock, gemColour, gemOpacity, strassColour, strassQuantity):
        super().__init__(id, type, previewUrl)
        self._colour = colour
        self._model = model
        self._pattern = pattern
        self._price = price
        self._stock = stock
        self._gemColour = gemColour
        self._gemOpacity = gemOpacity
        self._strassColour = strassColour
        self._strassQuantity = strassQuantity

    @property
    def price(self):
        return self._price

    def toJson(self):
        return jsonify({
            "id": self._id,
            "type": self._type,
            "previewUrl": self._previewUrl,
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
