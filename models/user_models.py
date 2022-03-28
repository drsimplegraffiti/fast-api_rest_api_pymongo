from typing import Optional
from pydantic import BaseModel, Field


class User(BaseModel):
    username: str | None = Field(min_length=2, max_length=12)
    email: str | None = None
    full_name: str | None = None
    password: str | None = Field(min_length=1, max_length=10)
    disabled: bool | None = None
