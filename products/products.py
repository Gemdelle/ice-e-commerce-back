from abc import ABC, abstractmethod
from flask import jsonify

class Product(ABC):
    def __init__(self, type, previewUrl):
        self.type = type
        self.previewUrl = previewUrl

    @abstractmethod
    def toJson(self):
        pass

class Tight(Product):
    def __init__(self, type, previewUrl, size, model, pattern, price, stock, strassColour, strassQuantity):
        super().__init__(type, previewUrl)
        self.size = size
        self.model = model
        self.pattern = pattern
        self.price = price
        self.stock = stock
        self.strassColour = strassColour
        self.strassQuantity = strassQuantity

    def toJson(self):
        return jsonify({
            "type": self.type,
            "previewUrl": self.previewUrl,
            "size": self.size,
            "model": self.model,
            "pattern": self.pattern,
            "price": self.price,
            "stock": self.stock,
            "strass_quantity": self.strassQuantity,
            "strass_colour": self.strassColour
        })

class Glove(Product):
    def __init__(self, type, previewUrl, colour, model, pattern, price, stock, gemColour, gemOpacity, strassColour, strassQuantity):
        super().__init__(type, previewUrl)
        self.colour = colour
        self.model = model
        self.pattern = pattern
        self.price = price
        self.stock = stock
        self.gemColour = gemColour
        self.gemOpacity = gemOpacity
        self.strassColour = strassColour
        self.strassQuantity = strassQuantity

    def toJson(self):
        return jsonify({
            "type": self.type,
            "previewUrl": self.previewUrl,
            "colour": self.colour,
            "model": self.model,
            "pattern": self.pattern,
            "price": self.price,
            "stock": self.stock,
            "gem_colour": self.gemColour,
            "gem_opacity": self.gemOpacity,
            "strass_colour": self.strassColour,
            "strass_quantity": self.strassQuantity,
        })