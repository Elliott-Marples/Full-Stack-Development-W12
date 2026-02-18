# Imports
from sqlalchemy.orm import Session
from app.models.user import User as UserModel
from app.schemas.user import UserCreate
from app.core.security import hash_password

# Returns user from their email
def get_user_by_email(db: Session, email: str):
    return db.query(UserModel).filter(UserModel.email == email).first()

# Creates user using model (with hashed password) and adds to the database
def create_user(db: Session, user_in: UserCreate):
    user = UserModel(
        name=user_in.name,
        email=user_in.email,
        password_hash=hash_password(user_in.password),
        role=user_in.role or "user",
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user