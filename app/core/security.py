# Imports
import os
from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext
from jose import jwt

# Consts
SECRET_KEY = os.getenv("SECRET_KEY", "CHANGE_ME_IN_PRODUCTION")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRES_MINUTES = 30

# Defines hashing function
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Hashes password
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# Checks if the plain password matches the hashed password
def verify_password(plain_password: str, password_hash: str) -> bool:
    return pwd_context.verify(plain_password, password_hash)

# Creates an encoded access token with an expiry
def create_access_token(subject: str, expires_minutes: int = ACCESS_TOKEN_EXPIRES_MINUTES) -> str:
    expire = datetime.now(timezone.utc) + timedelta(minutes=expires_minutes)
    payload = {"sub": subject, "exp": expire}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)