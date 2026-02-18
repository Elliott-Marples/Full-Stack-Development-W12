# Imports
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.schemas.book import Book
from app.crud import book as crud_book

# Router (defines URI path for books)
router = APIRouter(prefix="/books", tags=["books"])

# URI ending in /books returns all books in database
@router.get("/", response_model=List[Book])
def list_books(db: Session = Depends(get_db)):
    return crud_book.get_books(db)

# URI ending in /books/{book_id} attempts to return the book with inputted id
@router.get("/{book_id}", response_model=Book)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = crud_book.get_book(db, book_id)
    
    # If book with id cannot be found, raises exception
    if not book:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )
    
    return book