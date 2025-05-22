from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.security.jwt import get_current_user
from app.models.user import User
from app.models.note import Note
from app.schemas.schemas import NoteCreate
from app.schemas.schemas import NoteAIRequest
import requests

router = APIRouter(prefix="/ai", tags=["ai"])

OLLAMA_URL = "http://localhost:11434/api/generate"  # Ollama locale

@router.post("/notes", response_model=NoteCreate)
def generate_note(
    data: NoteAIRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    try:
        prompt_istruzioni = (
            f"Scrivi una nota in stile {data.stile}, in {data.lingua}, "
            f"di lunghezza {data.lunghezza}, basata su questo contenuto: {data.prompt}"
        )

        # CHIAMATA a Ollama
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt_istruzioni,
                "stream": False
            }
        )

        result = response.json()
        content = result.get("response", "").strip()

        note = Note(title="Nota AI", content=content, owner_id=current_user.id)
        db.add(note)
        db.commit()
        db.refresh(note)

        return note

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Errore AI: {str(e)}")
    