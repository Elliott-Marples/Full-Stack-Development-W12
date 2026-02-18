# Imports
from sqlalchemy.orm import Session
from app.models.book import Book as BookModel

# Returns all books in database
def get_books(db: Session):
    return db.query(BookModel).all()

# Returns book matching the book id
def get_book(db: Session, book_id: id):
    return db.query(BookModel).filter(BookModel.id == book_id).first()