import sqlite3
from flask import Flask, jsonify, request

app = Flask(__name__)
DB_NAME = "inventory.db"

def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                price REAL NOT NULL
            )
        """)
        conn.commit()

@app.route("/products", methods=["GET"])
def get_products():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, quantity, price FROM products")
        rows = cursor.fetchall()
        products = [
            {"id": r[0], "name": r[1], "quantity": r[2], "price": r[3]}
            for r in rows
        ]
    return jsonify(products), 200

@app.route("/products", methods=["POST"])
def add_product():
    data = request.get_json()
    if not data or "name" not in data or "quantity" not in data or "price" not in data:
        return jsonify({"error": "Eksik veri gönderildi"}), 400

    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO products (name, quantity, price) VALUES (?, ?, ?)",
            (data["name"], data["quantity"], data["price"])
        )
        conn.commit()
    return jsonify({"message": "Urun basariyla eklendi"}), 201

if __name__ == "__main__":
    init_db()
    app.run(debug=True)

