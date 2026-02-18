# Imports
from sqlalchemy import Column, Integer, String
from app.db.base import Base

# Book Model (Defines columns for tables)
class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=False)
    title = Column(String(255), nullable=False)
    author = Column(String(255), nullable=False)
    year_published = Column(Integer, nullable=True)
    publisher = Column(String(255), nullable=True)