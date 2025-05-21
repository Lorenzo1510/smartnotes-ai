from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.note import Note
from app.models.user import User
from app.schemas.schemas import NoteCreate, NoteOut
from app.database import get_db
from app.security.dependencies import get_current_user
from typing import List


router = APIRouter(prefix="/notes", tags=["notes"])

@router.get("/me", response_model=List[NoteOut])
def read_my_notes(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    notes = db.query(Note).filter(Note.owner_id == current_user.id).all()
    return notes

@router.get("/", response_model=list[NoteOut])
def get_notes(
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user)
):
    return db.query(Note).filter(Note.owner_id == current_user.id).all()

@router.post("/", response_model=NoteOut)
def create_note(
    note: NoteCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    db_note = Note(**note.dict(), owner_id=current_user.id)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

@router.delete("/{note_id}", status_code=204)
def delete_note(
    note_id: int, 
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user)
):
    note = db.query(Note).filter(Note.id == note_id, Note.owner_id == current_user.id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    db.delete(note)
    db.commit()
