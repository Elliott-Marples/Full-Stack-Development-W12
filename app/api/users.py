# Imports
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.user import User, UserCreate
from app.crud import user as crud_user

# Router (defines URI path for users)
router = APIRouter(prefix="/users", tags=["users"])

# URI ending in /users creates a new user
@router.post("/", response_model=User, status_code=201)
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    # If a user exists with inputted email, raises an exception
    existing = crud_user.get_user_by_email(db, user_in.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    return crud_user.create_user(db, user_in)