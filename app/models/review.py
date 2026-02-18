# Imports
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

# Review Model
class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True, index=False)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    rating = Column(Integer, nullable=False)
    comment = Column(String(500), nullable=True)
    book = relationship("Book", backref="reviews")
    user = relationship("User")