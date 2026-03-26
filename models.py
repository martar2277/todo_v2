from sqlalchemy import Boolean, Column, Integer, String, DateTime, func
from database import Base

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    completed = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=func.now())
