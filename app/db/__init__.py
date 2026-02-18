# Imports
from app.db.base import Base
from app.db.session import engine

from app.models.book import Book
from app.models.user import User
from app.models.review import Review

# Creates any missing tables upon start-up
def init_db():
    Base.metadata.create_all(bind=engine)