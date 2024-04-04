from pydantic import BaseModel
from typing import Union, List
from src.common.product import Product, ProductPrice, ProductPrices
import sqlite3
from os import path
from fastapi import HTTPException

# Get the currenct directory path
current_dir = path.dirname(path.abspath(__file__))
# Construct the absolute path to the database file
db_path = path.join(current_dir, '../../../dbs/mercado_livre.db')


class ProductModel:

    def __init__(self):
        print("Initializing database connection...")
        self.conn = None
        self.cursor = None
        try:
            self.conn = sqlite3.connect(db_path)
            self.cursor = self.conn.cursor()

            # Create tables if not exists
            self.cursor.execute(
                '''CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT, url TEXT, rating_number FLOAT, rating_amount INTEGER)''')
            self.cursor.execute(
                '''CREATE TABLE IF NOT EXISTS product_prices (id INTEGER PRIMARY KEY, product_id INTEGER, price FLOAT, price_date DATETIME, FOREIGN KEY(product_id) REFERENCES products(id))''')

        except sqlite3.Error as e:
            print(f"Error connecting to SQLite: {e}")

    def close_connection(self):
        try:
            if self.cursor:
                self.cursor.close()
            if self.conn:
                self.conn.close()
            print("Database connection closed.")
        except sqlite3.Error as e:
            print(f"Error closing database connection: {e}")


    def get_all_products(self) -> Union[List[Product], None]:
        try:
            self.cursor.execute("SELECT * FROM products")
            products = self.cursor.fetchall()
            if products:
                return products
            else :
                print(f"No products found.")
                raise HTTPException(status_code=404, detail="No products found")
        except sqlite3.Error as e:
            print(f"Error getting products: {e}")
            raise HTTPException(status_code=500, detail='Database Internal Server Error')


    def get_product_by_id(self, id: int) -> Union[Product, None]:
        try:
            self.cursor.execute("SELECT * FROM products WHERE id=?", (id,))
            product = self.cursor.fetchone()
            if product:
                return Product(
                    id=product[0],
                    name=product[1],
                    url=product[2],
                    rating_number=product[3],
                    rating_amount=product[4]
                )
            else:
                print(f"Product with id {id} not found.")
                raise HTTPException(
                    status_code=404, detail="Product not found")

        except sqlite3.Error as e:
            print(f"Error getting product by id: {e}")
            raise HTTPException(
                status_code=500, detail='Database Internal Server Error')


    def get_prices_by_product_id(self, product_id: int) -> Union[ProductPrices, None]:
        try:
            self.cursor.execute(
                "SELECT * FROM product_prices WHERE product_id=?", (product_id, ))
            prices = self.cursor.fetchall()
            if prices:
                return ProductPrices(prices=[ProductPrice(product_id=price[1], price=price[2], price_date=price[3]) for price in prices])
            else:
                raise HTTPException(
                    status_code=404, detail="Prices not found for product")
            
        except sqlite3.Error as e:
            print(f"Error getting prices by product id: {e}")
            raise HTTPException(
                    status_code=500, detail='Database Internal Server Error')
