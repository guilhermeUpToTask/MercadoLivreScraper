from typing import Union
from pydantic import BaseModel
from fastapi import APIRouter
from src.models.product_model import ProductModel
from src.common.product import Product, ProductPrice, ProductPrices

router = APIRouter()


@router.get("/products",)
def get_products() -> Union[list[Product],None]:
    products = [
        Product(id='23232', name="teste", url="teste",
                rating_number=3.5, rating_amount=10),
        Product(id='255',name="teste", url="teste",
                rating_number=3.5, rating_amount=10),
        Product(id='2663',name="teste", url="teste", rating_number=3.5, rating_amount=10)
    ]
    return products


@router.get("/products/{id}")
def get_product(id: int) -> Union[Product, None]:
    return ProductModel.get_product_by_id(id)


@router.get("/products/{id}/price_story")
def get_product_prices(id: int) -> Union[ProductPrices, None]:
    return ProductPrices(
        prices=[
            ProductPrice(price=10.0, price_date="2021-01-01"),
            ProductPrice(price=12.0, price_date="2021-02-01"),
            ProductPrice(price=10.0, price_date="2021-03-01")
        ]
    )
