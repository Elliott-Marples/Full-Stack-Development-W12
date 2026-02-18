# Imports
from fastapi import FastAPI
from app.api import auth, books, users, reviews
from app.db.init_db import init_db

# Creates app instance
app = FastAPI(title="Bookstore API (Week 12)", version="1.0.0")

# Creates any missing tables from database
init_db()

# Includes all defined routers for crud operations on database
app.include_router(auth.router)
app.include_router(books.router)
app.include_router(users.router)
app.include_router(reviews.router)

# Root URI returns message confirming API is running
@app.get("/")
def root():
    return {"message": "Bookstore API is running"}