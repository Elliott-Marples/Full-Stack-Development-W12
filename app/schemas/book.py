# Imports
from pydantic import BaseModel
from typing import Optional

# Book Schema (ensures data stays valid and consistent)
class BookBase(BaseModel):
    title: str
    author: str
    year_published: Optional[int] = None
    publisher: Optional[str] = None

class Book(BookBase):
    id: int
    class Config():
        orm_mode = True