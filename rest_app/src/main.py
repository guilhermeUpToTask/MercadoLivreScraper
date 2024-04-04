from typing import Union
from fastapi import FastAPI

from src.controllers.product_controller import  router as product_router

app = FastAPI()
app.include_router(product_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}