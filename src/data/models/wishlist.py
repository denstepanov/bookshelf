from sqlalchemy import Column, String, Integer, ForeignKey

from src.core.db.config import Base

class Wishlist(Base):
    __tablename__ = "wishlist"

    id: int = Column(Integer, primary_key=True)
    name: str = Column(String(50))
    description: str = Column(String(255))