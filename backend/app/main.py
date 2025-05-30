from fastapi import FastAPI
from app.routes import auth
from app.database import Base, engine
from app.routes import auth  # auth routes
from app.routes import note  # protected notes
from app.routes import ai
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # oppure ["*"] per test locali
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "SmartNotes API is up and running!"}


app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(auth.router)
app.include_router(note.router)
app.include_router(ai.router)