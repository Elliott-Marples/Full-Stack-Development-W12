# Imports
from typing import Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import JWTError, jwt

from app.db.session import get_db
from app.crud import user as crud_user
from app.core.security import SECRET_KEY, ALGORITHM

# Extracts token from request
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

# Gets user from login
def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    # Creates unauthorised exception
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    # Attempts to retrieve email (subject) from token, otherwise raises credentials exception
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: Optional[str] = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    # Attempts to find user from the email retrieved from token, otherwise raises crendentials exception
    user = crud_user.get_user_by_email(db, email)
    if user is None:
        raise credentials_exception
    
    return user