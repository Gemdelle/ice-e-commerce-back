"""
Este módulo contiene la clase de tipo excepción que se lanza cuando una buúsqueda en la base de datos no trajo
resultados.
"""


class NoDataFoundError(Exception):
    """Excepción personalizada que se lanza cuando no se encuentran datos en una operación de búsqueda."""
    pass

