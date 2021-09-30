from fastapi import FastAPI

from .api.routers import wishlist

app = FastAPI()

app.include_router(wishlist.router)
