from fastapi import FastAPI, Request, Form, HTTPException, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from crud import get_todos, create_todo, get_todo, mark_todo_complete, delete_todo
from schemas import TodoCreate
from database import get_db

app = FastAPI()
templates = Jinja2Templates(directory='templates')

@app.on_event("startup")
def startup():
    from database import init_db
    init_db()

@app.get('/', response_class=HTMLResponse)
async def read_todos(request: Request, db: Session = Depends(get_db)):
    todos = get_todos(db)
    return templates.TemplateResponse(request=request, name='index.html', context={'todos': todos})

@app.post('/todos', response_class=RedirectResponse)
async def create_todo_view(title: str = Form(...), db: Session = Depends(get_db)):
    todo_data = TodoCreate(title=title)
    create_todo(db, todo_data)
    return RedirectResponse(url='/', status_code=303)

@app.post('/todos/{id}/complete', response_class=RedirectResponse)
async def complete_todo_view(id: int, db: Session = Depends(get_db)):
    todo = mark_todo_complete(db, id)
    if not todo:
        raise HTTPException(status_code=404, detail='Todo not found')
    return RedirectResponse(url='/', status_code=303)

@app.post('/todos/{id}/delete', response_class=RedirectResponse)
async def delete_todo_view(id: int, db: Session = Depends(get_db)):
    todo = delete_todo(db, id)
    if not todo:
        raise HTTPException(status_code=404, detail='Todo not found')
    return RedirectResponse(url='/', status_code=303)
