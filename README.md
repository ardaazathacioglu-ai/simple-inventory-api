# Simple Inventory Management API

A lightweight RESTful inventory management API built with Python, SQLite, and Flask.

## Features
- **Database Integration:** SQLite database with automatic table initialization.
- **REST Endpoints:**
  - `GET /products` : List all inventory items.
  - `POST /products` : Add a new product with JSON payload.
- **Input Validation:** Basic payload checks for required fields (`name`, `quantity`, `price`).

## Tech Stack
- **Language:** Python 3
- **Framework:** Flask
- **Database:** SQLite

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/ardaazathacioglu-ai/simple-inventory-api.git
   cd simple-inventory-api
   pip install flask
   python app.py
   ```
