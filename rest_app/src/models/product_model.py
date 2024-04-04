from pydantic import BaseModel
from typing import Union
from src.common.product import Product

class ProductModel():

    def get_product_by_id(id:int) -> Union[Product, None]:
        return Product(id=id, name="test", url="test", rating_number=5, rating_amount=10)