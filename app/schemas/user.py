# Imports
from pydantic import BaseModel
from typing import Optional

# User Schema (ensures data stays valid and consistent)
class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    password: str
    role: Optional[str] = "user"

class User(UserBase):
    id: int
    role: str
    class Config():
        orm_mode = True