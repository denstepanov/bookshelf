from src.api.schemas.wishlist import CreateWishlist
from fastapi import APIRouter
from starlette.responses import JSONResponse

router = APIRouter(
    prefix="/wishlists",
    tags=["wishlists"]
)

@router.post("/")
async def create(wishlistToCreate: CreateWishlist):
    return JSONResponse(wishlistToCreate.json(), status_code=201)


