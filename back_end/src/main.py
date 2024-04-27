from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from src.controllers.product_controller import router as product_router
from fastapi.middleware.cors import CORSMiddleware
import os
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(product_router)

# Get the absolute path to the static directory
static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")

app.mount("/", StaticFiles(directory=static_dir, html=True), name="static")


#if __name__ == "__main__":
 #   port = os.getenv("PORT")
  #  if not port:
   #     port = 8080
   # uvicorn.run(app, host="0.0.0.0", port=8080) 

