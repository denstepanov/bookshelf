from typing import Optional
from pydantic import BaseModel
from pydantic.fields import Field

class CreateWishlist(BaseModel):
    name: str = Field("my wishlist", title="The name of the wishlist", max_length=100)
    description: Optional[str] = Field(None, title="The description of the wishlist", max_length=300)