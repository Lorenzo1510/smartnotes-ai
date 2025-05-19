from fastapi import APIRouter, Depends
from app.models.user import User
from app.security.jwt import get_current_user

router = APIRouter(prefix="/notes", tags=["notes"])

@router.get("/me")
def read_my_notes(current_user: User = Depends(get_current_user)):
    return {"message": f"Hello {current_user.username}, here are your notes!"}
