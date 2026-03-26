from pydantic import BaseModel, Field

class TodoCreate(BaseModel):
    title: str = Field(..., min_length=1, description='The title of the todo')
