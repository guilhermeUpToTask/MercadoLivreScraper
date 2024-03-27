# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import psycopg2
from psycopg2 import OperationalError
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MercadoLivrePipeline:
    def __init__(self, *args, **kwargs):
       self.conn = None
       self.cursor = None
       try:
           self.conn = psycopg2.connect(
               dbname="mercado_livre_data",
               user="postgres",
               password="12345",
               host="localhost"
           )
           self.cursor = self.conn.cursor()
       except OperationalError as e:
           print(f"Error connecting to PostgreSQL: {e}")
       super().__init__(*args, **kwargs)
    
    def process_item(self, item, spider):
        try:
            if item['id'] == 0:
                return item
            
            sql_product = 'INSERT INTO products (id, name, url, rating_number, rating_amount) VALUES (%s, %s, %s, %s, %s) ON CONFLICT(id) DO NOTHING'
            self.cursor.execute(sql_product, (item['id'], item['name'], item['url'], item['rating_number'], item['rating_amount']))

            sql_price = 'INSERT INTO product_prices (product_id, price, price_date) VALUES (%s, %s, CURRENT_TIMESTAMP)'
            self.cursor.execute(sql_price, (item['id'], item['price']))

            self.conn.commit()
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
           print(f"Error closing PostgreSQL connection: {e}")