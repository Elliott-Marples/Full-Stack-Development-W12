# Imports
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

# Database URL ("mysqldb" is the dialect for mysqlclient)
SQLALCHEMY_DATABASE_URL = "mysql+mysqldb://root:SEPS@127.0.0.1:3306/bookstore"

# Engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)

# Session Factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Gives each request a session (and closes when finished)
def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()