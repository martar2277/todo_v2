from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from fastapi import Depends

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def init_db():
    import models  # Importing models to register them in Base.metadata
    Base.metadata.create_all(bind=engine)

# Ensure tables are created when the application starts
init_db()

def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
