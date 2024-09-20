from flask import Flask, jsonify
from flask_cors import CORS

from api.products_api import product_api

app = Flask(__name__)
CORS(app)

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

if __name__ == '__main__':
    app.run(debug=True)
