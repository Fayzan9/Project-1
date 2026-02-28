from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from uuid import uuid4
from datetime import datetime

from database import read_db, write_db
from typing import List, Optional


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


@router.get("/{note_id}", response_model=NoteResponse)
def get_note_by_id(note_id: str):
    db = read_db()

    for note in db["notes"]:
        if note["id"] == note_id:
            return note

    raise HTTPException(status_code=404, detail="Note not found")    



class NoteUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None


@router.put("/{note_id}", response_model=NoteResponse)
def update_note(note_id: str, note: NoteUpdate):
    db = read_db()

    for existing_note in db["notes"]:
        if existing_note["id"] == note_id:

            if note.title is not None:
                existing_note["title"] = note.title

            if note.content is not None:
                existing_note["content"] = note.content

            existing_note["updated_at"] = datetime.utcnow().isoformat()

            write_db(db)
            return existing_note

    raise HTTPException(status_code=404, detail="Note not found")


@router.delete("/{note_id}")
def delete_note(note_id: str):
    db = read_db()

    for index, note in enumerate(db["notes"]):
        if note["id"] == note_id:
            db["notes"].pop(index)
            write_db(db)
            return {"message": "Note deleted successfully"}

    raise HTTPException(status_code=404, detail="Note not found")



class TagAttach(BaseModel):
    tag_id: str


@router.post("/{note_id}/tags", response_model=NoteResponse)
def attach_tag_to_note(note_id: str, payload: TagAttach):
    db = read_db()

    # find note
    note = next((n for n in db["notes"] if n["id"] == note_id), None)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")

    # find tag
    tag = next((t for t in db["tags"] if t["id"] == payload.tag_id), None)
    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")

    # prevent duplicate tag attach
    for existing_tag in note["tags"]:
        if existing_tag["id"] == tag["id"]:
            raise HTTPException(status_code=400, detail="Tag already attached")

    note["tags"].append({
        "id": tag["id"],
        "name": tag["name"]
    })

    note["updated_at"] = datetime.utcnow().isoformat()
    write_db(db)

    return note

@router.delete("/{note_id}/tags/{tag_id}", response_model=NoteResponse)
def remove_tag_from_note(note_id: str, tag_id: str):
    db = read_db()

    # find note
    note = next((n for n in db["notes"] if n["id"] == note_id), None)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")

    # find tag inside note
    for index, tag in enumerate(note["tags"]):
        if tag["id"] == tag_id:
            note["tags"].pop(index)
            note["updated_at"] = datetime.utcnow().isoformat()
            write_db(db)
            return note

    raise HTTPException(status_code=404, detail="Tag not attached to note")