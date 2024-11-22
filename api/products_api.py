from abc import ABC, abstractmethod

from products.product import Product


class ProductsAPI(ABC):
    """
    Clase abstracta definida para consumir información de una API.
    """

    @abstractmethod
    def get_all_products(self) -> [Product]:
        """
        Método abstracto que obtiene todos los productos de la API.

        Retorna:
            List: Lista de productos obtenidos de la API.
        """
        pass