from pydantic import BaseModel, EmailStr
from typing import List, Optional

class NoteBase(BaseModel):
    title: str
    content: str

class NoteCreate(NoteBase):
    pass

class Note(NoteBase):
    id: int
    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    notes: List[Note] = []

    class Config:
        orm_mode = True
