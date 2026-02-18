# Imports
from pydantic import BaseModel
from typing import Optional

# Review Schema (ensures data stays valid and consistent)
class ReviewCreate(BaseModel):
    book_id: int
    rating: int
    comment: Optional[str] = None

class Review(ReviewCreate):
    id: int
    user_id: int
    class Config():
        orm_mode = True