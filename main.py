"""
Este módulo contiene todos los endpoints disponibles para ser consumidos desde el front-end.
"""

from flask import Flask, jsonify, request
from flask_cors import CORS

from api.products_api import product_api
from cart.cart import Cart
from errors.no_data_found_error import NoDataFoundError
from products.products import Product

# Inicializa la aplicación Flask y habilita el soporte para CORS
app = Flask(__name__)
CORS(app)
cart = Cart()


@app.route('/api/products', methods=['GET'])
def get_products():
    """
    Endpoint para obtener todos los productos disponibles.

    Retorna:
        json: Una lista de productos en formato JSON o un mensaje de error en caso de fallo.
    """
    try:
        products = product_api.get_all_products()
        if products:
            return jsonify([product.to_json().json for product in products])
        else:
            return jsonify({"error": "No se pueden recuperar los productos"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/cart', methods=['POST'])
def add_to_cart():
    """
    Endpoint para agregar un producto al carrito.

    Retorna:
        json: El estado actual del carrito en formato JSON o un mensaje de error si algo falla.
    """
    try:
        data = request.json
        product_id = data.get('product_id')
        quantity = data.get('quantity', 1)

        if not product_id:
            return jsonify({"error": "Se requiere el ID del producto"}), 400

        product = find_product_by_id(product_id)
        if product is None:
            return jsonify({"error": "No se puede recuperar la información del producto"}), 500
        if not product:
            return jsonify({"error": "Producto no encontrado"}), 404

        cart.add_product(product, quantity)
        return jsonify(cart.to_dict()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/cart', methods=['DELETE'])
def remove_from_cart():
    """
    Endpoint para eliminar un producto del carrito.

    Retorna:
        json: El estado actual del carrito o un mensaje de error si el producto no se encuentra.
    """
    try:
        data = request.json
        product_id = data.get('product_id')

        if cart.remove_product(product_id):
            return jsonify(cart.to_dict()), 200
        else:
            return jsonify({"error": "Producto no encontrado en el carrito"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/cart', methods=['GET'])
def get_cart():
    """
    Endpoint para obtener el contenido del carrito.

    Retorna:
        json: El estado actual del carrito en formato JSON.
    """
    return jsonify(cart.to_dict()), 200


@app.route('/api/buy', methods=['POST'])
def buy_cart():
    """
    Endpoint para realizar la compra de los productos en el carrito.

    Retorna:
        json: Un mensaje de confirmación de compra o un mensaje de error en caso de fallo.
    """
    try:
        cart_contents = cart.to_dict()
        cart.products.clear()
        return jsonify({"message": "Compra exitosa", "purchased_items": cart_contents}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def find_product_by_id(product_id: int) -> Product:
    """
    Busca un producto por su ID.

    Argumentos:
        product_id (int): El ID del producto a buscar.

    Retorna:
        Product: El producto con el ID coincidente, o None si no se encuentra.

    Lanza Excepcion:
        NoDataFoundError: Si no se puede recuperar la lista de productos.
    """
    all_products = product_api.get_all_products()
    if all_products is None:
        raise NoDataFoundError("No se pueden recuperar los productos")
    return next((p for p in all_products if p.id == product_id), None)


if __name__ == '__main__':
    # Ejecuta la aplicación Flask en modo depuración
    app.run(debug=True)
