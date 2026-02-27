from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from uuid import uuid4
from datetime import datetime

from database import read_db, write_db
from typing import List


router = APIRouter(prefix="/api/notes", tags=["Notes"])


# Request body schema
class NoteCreate(BaseModel):
    title: str
    content: str


# Response schema
class NoteResponse(BaseModel):
    id: str
    title: str
    content: str
    tags: list
    created_at: str
    updated_at: str


@router.post("/", response_model=NoteResponse)
def create_note(note: NoteCreate):
    db = read_db()

    new_note = {
        "id": str(uuid4()),
        "title": note.title,
        "content": note.content,
        "tags": [],
        "created_at": datetime.utcnow().isoformat(),
        "updated_at": datetime.utcnow().isoformat()
    }

    db["notes"].append(new_note)
    write_db(db)

    return new_note



@router.get("/", response_model=List[NoteResponse])
def get_all_notes():
    db = read_db()
    return db["notes"]    