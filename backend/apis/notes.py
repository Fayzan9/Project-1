from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List,Optional
from database.notes_db import attach_tag_to_note, detach_tag_from_note,get_tags_for_note,get_notes_for_tag,update_note,delete_note
from database.notes_db import (
    create_note as db_create_note,
    get_all_notes as db_get_all_notes,
)

router = APIRouter(prefix="/api/notes", tags=["Notes"])


class NoteCreate(BaseModel):
    title: str
    content: str
    tags: List[str] = []


class NoteResponse(BaseModel):
    id: str
    title: str
    content: str
    tags: List[str]
    created_at: str
    updated_at: str


@router.post("/", response_model=dict)
def create_note_api(note: NoteCreate):
    note_id = db_create_note(
        title=note.title,
        content=note.content,
        tags=note.tags
    )
    return {"id": note_id}


@router.get("/", response_model=List[NoteResponse])
def get_notes_api():
    return db_get_all_notes()



@router.post("/{note_id}/tags/{tag_id}")
def attach_tag_api(note_id: str, tag_id: str):
    result = attach_tag_to_note(note_id, tag_id)

    if result == "NOTE_NOT_FOUND":
        raise HTTPException(status_code=404, detail="Note not found")

    if result == "TAG_NOT_FOUND":
        raise HTTPException(status_code=404, detail="Tag not found")

    if result == "ALREADY_ATTACHED":
        raise HTTPException(status_code=400, detail="Tag already attached")

    return {"message": "Tag attached successfully"}



@router.delete("/{note_id}/tags/{tag_id}")
def detach_tag_api(note_id: str, tag_id: str):
    result = detach_tag_from_note(note_id, tag_id)

    if result == "NOT_ATTACHED":
        raise HTTPException(status_code=404, detail="Tag not attached to note")

    return {"message": "Tag detached successfully"}




@router.get("/{note_id}/tags")
def get_note_tags_api(note_id: str):
    tags = get_tags_for_note(note_id)

    if tags is None:
        raise HTTPException(status_code=404, detail="Note not found")

    return {"tags": tags}


@router.get("/{tag_id}/notes")
def get_notes_for_tag_api(tag_id: str):
    notes = get_notes_for_tag(tag_id)

    if notes is None:
        raise HTTPException(status_code=404, detail="Tag not found")

    return {"notes": notes}




class NoteUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None


@router.put("/{note_id}")
def update_note_api(note_id: str, note: NoteUpdate):
    result = update_note(
        note_id=note_id,
        title=note.title,
        content=note.content,
    )

    if result is None:
        raise HTTPException(status_code=404, detail="Note not found")

    return {"message": "Note updated successfully"}


@router.delete("/{note_id}")
def delete_note_api(note_id: str):
    result = delete_note(note_id)

    if result is None:
        raise HTTPException(status_code=404, detail="Note not found")

    return {"message": "Note deleted successfully"}