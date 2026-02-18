# Imports
from sqlalchemy.orm import Session
from app.models.review import Review as ReviewModel
from app.schemas.review import ReviewCreate

# Creates review using model and adds to the database
def create_review(db: Session, review_in: ReviewCreate, user_id: int):
    review = ReviewModel(
        book_id=review_in.book_id,
        user_id=user_id,
        rating=review_in.rating,
        comment=review_in.comment,
    )
    db.add(review)
    db.commit()
    db.refresh(review)
    return review