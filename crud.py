from sqlalchemy.orm import Session
from models import Todo
import schemas

def get_todos(db: Session):
    return db.query(Todo).order_by(Todo.created_at.desc()).all()

def create_todo(db: Session, todo: schemas.TodoCreate):
    new_todo = Todo(title=todo.title)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

def get_todo(db: Session, todo_id: int):
    return db.query(Todo).filter(Todo.id == todo_id).first()

def mark_todo_complete(db: Session, todo_id: int):
    todo = get_todo(db, todo_id)
    if todo:
        todo.completed = True
        db.commit()
    return todo

def delete_todo(db: Session, todo_id: int):
    todo = get_todo(db, todo_id)
    if todo:
        db.delete(todo)
        db.commit()
    return todo
