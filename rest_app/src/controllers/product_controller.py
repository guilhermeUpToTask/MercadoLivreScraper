from typing import Union
from pydantic import BaseModel
from fastapi import APIRouter, HTTPException
from src.models.product_model import ProductModel
from src.common.product import Product, ProductPrices

router = APIRouter()
product_model = ProductModel()

@router.get("/products",)
async def get_products() -> Union[list[Product],None]:
    try:
        products = product_model.get_all_products()
        return products
    except HTTPException as e:
        raise e
    except Exception as e:
        print(f'Internal Server Error from product Controler... ')
        print(f"{str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        product_model.close_connection()


@router.get("/products/{id}")
async def get_product(id: int) -> Union[Product, None]:
    try:
        product = product_model.get_product_by_id(id)
        return product
    
    except HTTPException as e:
        raise e
    
    except Exception as e:
        print(f'Internal Server Error from product Controler... ')
        print(f"{str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        product_model.close_connection()


@router.get("/products/{id}/price_story")
async def get_product_prices(id: int) -> Union[ProductPrices, None]:
    try:
        prices = product_model.get_prices_by_product_id(id)
        return prices
    
    except HTTPException as e:
        raise e
    except Exception as e:
        print(f'Internal Server Error from product Controler... ')
        print(f"{str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        product_model.close_connection()
