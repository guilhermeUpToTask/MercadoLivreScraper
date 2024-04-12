# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
import sqlite3

from itemadapter import ItemAdapter

class MercadoLivrePipeline:
    def __init__(self):
        print("Initializing database connection...")
        self.conn = None
        self.cursor = None
        try:
            self.conn = sqlite3.connect('../dbs/mercado_livre.db')
            self.cursor = self.conn.cursor()

            # Create tables if not exists
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT, url TEXT, rating_number FLOAT, rating_amount INTEGER)''')
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS product_prices (id INTEGER PRIMARY KEY, product_id INTEGER, price FLOAT, price_date DATETIME, FOREIGN KEY(product_id) REFERENCES products(id))''')
       
        except sqlite3.Error as e:
            print(f"Error connecting to SQLite: {e}")

    def process_item(self, item, spider):
        try:
            if item['id'] == 0:
                return item
            
            if self.cursor:
                sql_product = 'INSERT INTO products (id, name, url, rating_number, rating_amount) VALUES (?, ?, ?, ?, ?) ON CONFLICT(id) DO NOTHING'
                self.cursor.execute(sql_product, (item['id'], item['name'], item['url'], item['rating_number'], item['rating_amount']))

                sql_price = 'INSERT INTO product_prices (product_id, price, price_date) VALUES (?, ?, CURRENT_TIMESTAMP)'
                self.cursor.execute(sql_price, (item['id'], item['price']))

                self.conn.commit()
            else:
                print("Database cursor is not initialized.")
        except Exception as e:
            print(f"Error processing item: {e}")
            self.conn.rollback()
        return item

    def close_spider(self, spider):
        try:
            if self.cursor:
                self.cursor.close()
            if self.conn:
                self.conn.close()
        except Exception as e:
            print(f"Error closing connection: {e}")