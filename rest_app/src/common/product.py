from pydantic import BaseModel

class Product(BaseModel):
    id:int
    name: str
    url: str
    rating_number: float
    rating_amount: int


class ProductPrice(BaseModel):
    price: float
    price_date: str


class ProductPrices(BaseModel):
    prices: list[ProductPrice]