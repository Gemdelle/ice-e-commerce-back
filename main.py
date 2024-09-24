from flask import Flask, jsonify, request
from flask_cors import CORS

from api.products_api import product_api
from cart.cart import Cart
from errors.no_data_found_error import NoDataFoundError
from products.products import Product

app = Flask(__name__)
CORS(app)
cart = Cart()


def find_product_by_id(product_id: int) -> Product:
    all_products = product_api.get_all_products()
    if all_products is None:
        raise NoDataFoundError("Unable to retrieve products")
    return next((p for p in all_products if p.id == product_id), None)


@app.route('/api/products', methods=['GET'])
def get_products():
    try:
        products = product_api.get_all_products()
        if products:
            return jsonify([product.toJson().json for product in products])
        else:
            return jsonify({"error": "Unable to fetch products"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/cart', methods=['POST'])
def add_to_cart():
    try:
        data = request.json
        product_id = data.get('product_id')
        quantity = data.get('quantity', 1)

        if not product_id:
            return jsonify({"error": "Product ID is required"}), 400

        product = find_product_by_id(product_id)
        if product is None:
            return jsonify({"error": "Unable to fetch product information"}), 500
        if not product:
            return jsonify({"error": "Product not found"}), 404

        cart.add_product(product, quantity)
        return jsonify(cart.to_dict()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/cart', methods=['DELETE'])
def remove_from_cart():
    try:
        data = request.json
        product_id = data.get('product_id')

        if cart.remove_product(product_id):
            return jsonify(cart.to_dict()), 200
        else:
            return jsonify({"error": "Product not found in cart"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/cart', methods=['GET'])
def get_cart():
    return jsonify(cart.to_dict()), 200


@app.route('/api/buy', methods=['POST'])
def buy_cart():
    try:
        cart_contents = cart.to_dict()
        cart.products.clear()
        return jsonify({"message": "Purchase successful", "purchased_items": cart_contents}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
