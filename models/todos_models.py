from typing import Optional
from pydantic import BaseModel, Field

class Todo(BaseModel):
    name: str = Field(min_length=1)
    description: str= Field(min_length=1, max_length=100)
    completed: Optional[bool]
    date: str
    # rate: int = Field(gt = -1, lt = 100)