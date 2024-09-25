"""
Este módulo contiene la clase abstracta ProductsAPI(ABC) y su implementacion en la clase SupabaseProductsAPI.
"""
from supabase import create_client, Client
from abc import ABC, abstractmethod
from products.products import Tight, Glove

"""
Variables que almacenan las credenciales de acceso a la DDBB en Supabase.
"""
SUPABASE_URL = 'https://cpgvtgbknlxmlqgorcby.supabase.co/'
SUPABASE_KEY = ('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNwZ3Z0Z2Jrbmx4bWxxZ29yY2J5Iiwi'
                'cm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcyNjAwOTMyNiwiZXhwIjoyMDQxNTg1MzI2fQ.3_2xeZkbA9sc2DcLx57PSZMh8oF'
                'ZPSO1KlCvsB6r-WE')


class ProductsAPI(ABC):
    """
    Clase abstracta definida para consumir informacion de una API.
    """
    @abstractmethod
    def get_all_products(self):
        """
        Método abstracto que obtiene todos los productos de la API.
        Parámetros:
        Retorno:
        """
        pass


class SupabaseProductsAPI(ProductsAPI):
    """
    Clase que hereda de ProductsAPI para obtener los datos de una
    película desde una API.
    """
    def __init__(self, supabase: Client):
        self._supabase = supabase

    def get_all_products(self):
        try:
            tight_response = self._supabase.table('tight_view').select("*").execute()
            glove_response = self._supabase.table('glove_view').select("*").execute()
            products = []
            print(f"tight_response: {tight_response}")
            print(f"glove_response: {glove_response}")
            for item in tight_response.data:
                product = Tight(
                    type="TIGHT",
                    id=item['tight_id'],
                    previewUrl=item['tight_preview_url'],
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
                    previewUrl=item['glove_preview_url'],
                    colour=item['glove_colour'],
                    model=item['glove_model'],
                    pattern=item['glove_pattern'],
                    gemColour=item['gem_colour'],
                    gemOpacity=item['gem_opacity'],
                    strassColour=item['gem_opacity'],
                    strassQuantity=item['strass_quantity'],
                    price=item['glove_price'],
                    stock=item['glove_stock']
                )
                products.append(product)

            products.sort(key=lambda x: x.price)

            return products
        except Exception as e:
            print(f"Error fetching products: {e}")
            return None


supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
product_api = SupabaseProductsAPI(supabase)