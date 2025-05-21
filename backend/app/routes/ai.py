from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.security.jwt import get_current_user
from app.models.user import User
from app.models.note import Note
from app.schemas.schemas import NoteCreate
import requests

router = APIRouter(prefix="/ai", tags=["ai"])

OLLAMA_URL = "http://localhost:11434/api/generate"  # Ollama locale

@router.post("/notes", response_model=NoteCreate)
def generate_note(
    prompt: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": "mistral",  # puoi usare anche "llama2", "gemma", ecc.
                "prompt": f"Scrivi una nota chiara e sintetica su questo argomento:\n{prompt}",
                "stream": False
            }
        )

        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="Errore nella generazione della nota")

        result = response.json()
        content = result.get("response", "").strip()

        note = Note(title="Nota AI", content=content, owner_id=current_user.id)
        db.add(note)
        db.commit()
        db.refresh(note)

        return note

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Errore AI: {str(e)}")
