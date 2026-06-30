from flask import Flask, jsonify, request
from data import products

app = Flask(__name__)

# TODO: Implement homepage route that returns a welcome message

@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Product Catalog API"})

@app.route("/products")
def get_products():
    category = request.args.get("category")
    if category:
        filtered = [p for p in products if p["category"].lower() == category.lower()]
        return jsonify(filtered)
    return jsonify(products)

@app.route("/products/<int:id>")
def get_product_by_id(id):  # noqa: A002
    product = next((p for p in products if p["id"] == id), None)
    if product is None:
        return jsonify({"error": "Product not found"}), 404
    return jsonify(product)

if __name__ == "__main__":
    app.run(debug=True)
