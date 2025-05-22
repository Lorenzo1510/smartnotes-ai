from pydantic import BaseModel, EmailStr
from typing import List, Optional

class NoteBase(BaseModel):
    title: str
    content: Optional[str] = None

class NoteCreate(NoteBase):
    pass

class NoteOut(NoteBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class NoteAIRequest(BaseModel):
    prompt: str
    stile: Optional[str] = "schematico"
    lingua: Optional[str] = "italiano"
    lunghezza: Optional[str] = "media"


class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    notes: List[NoteBase] = []

    class Config:
        orm_mode = True
