"""
Este módulo contiene la clase abstracta ProductsAPI(ABC) y su implementación en la clase SupabaseProductsAPI, establece
la conexión entre el back-end y la base de datos.
"""

from supabase import create_client, Client
from abc import ABC, abstractmethod

from api.products_api import ProductsAPI
from products.glove import Glove
from products.product import Product
from products.tight import Tight
from api.keys import SUPABASE_KEY, SUPABASE_URL


class SupabaseProductsAPI(ProductsAPI):
    """
    Clase que hereda de ProductsAPI para obtener los datos de productos desde una API Supabase.

    Argumentos:
        supabase (Client): Cliente de Supabase para hacer queries a la base de datos.
    """

    def __init__(self, supabase: Client):
        self._supabase = supabase

    def get_all_products(self) -> [Product]:
        """
        Obtiene todos los productos de las vistas 'tight_view' y 'glove_view' en la base de datos Supabase.

        Retorna:
            List: Lista de productos (Tight y Glove) ordenados por precio.
        """
        try:
            tight_response = self._supabase.table('tight_view').select("*").execute() # Queries a supabase
            glove_response = self._supabase.table('view_glove').select("*").execute()
            products = []

            for item in tight_response.data:
                product = Tight(
                    type="TIGHT",
                    id=item['tight_id'],
                    preview_url=item['tight_preview_url'],
                    size=item['tight_size'],
                    model=item['tight_model'],
                    pattern=item['tight_pattern'],
                    strassColour=item['strass_colour'],
                    strassQuantity=item['strass_quantity'],
                    price=item['tight_price'],
                    stock=item['tight_stock']
                )
                products.append(product)

            for item in glove_response.data:
                product = Glove(
                    type="GLOVE",
                    id=item['glove_id'],
                    preview_url=item['glove_preview_url'],
                    colour=item['glove_colour'],
                    colour_code=item['glove_colour_code'],
                    model=item['glove_model'],
                    pattern=item['glove_pattern'],
                    price=item['glove_price'],
                    pattern_elements=item['glove_pattern_elements'],
                    default_colour_code=item['default_glove_colour_code'],
                )
                products.append(product)

            products.sort(key=lambda x: x.price)

            return products # Todos los guantes y medias ordenados por precio de menor a mayor
        except Exception as e:
            print(f"Error fetching products: {e}")
            return None


# Inicializa el cliente de Supabase y la API de productos
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
product_api: SupabaseProductsAPI = SupabaseProductsAPI(supabase)
