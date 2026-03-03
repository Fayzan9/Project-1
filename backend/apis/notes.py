from fastapi import APIRouter, HTTPException
from typing import List
from database.repositories.notes_repository import NotesRepository
from model import NoteCreate, NoteResponse, NoteUpdate


router = APIRouter(prefix="/api/notes", tags=["Notes"])




@router.post("/", response_model=dict)
def create_note_api(note: NoteCreate):
    note_id = NotesRepository.create_note(
        title=note.title,
        content=note.content,
        tags=note.tags
    )
    return {"id": note_id}


@router.get("/", response_model=List[NoteResponse])
def get_notes_api():
    return NotesRepository.get_all_notes()



@router.post("/{note_id}/tags/{tag_id}")
def attach_tag_api(note_id: str, tag_id: str):
    result = NotesRepository.attach_tag_to_note(note_id, tag_id)

    if result == "NOTE_NOT_FOUND":
        raise HTTPException(status_code=404, detail="Note not found")

    if result == "TAG_NOT_FOUND":
        raise HTTPException(status_code=404, detail="Tag not found")

    if result == "ALREADY_ATTACHED":
        raise HTTPException(status_code=400, detail="Tag already attached")

    return {"message": "Tag attached successfully"}



@router.delete("/{note_id}/tags/{tag_id}")
def detach_tag_api(note_id: str, tag_id: str):
    result = NotesRepository.detach_tag_from_note(note_id, tag_id)

    if result == "NOT_ATTACHED":
        raise HTTPException(status_code=404, detail="Tag not attached to note")

    return {"message": "Tag detached successfully"}




@router.get("/{note_id}/tags")
def get_note_tags_api(note_id: str):
    tags = NotesRepository.get_tags_for_note(note_id)

    if tags is None:
        raise HTTPException(status_code=404, detail="Note not found")

    return {"tags": tags}


@router.get("/{tag_id}/notes")
def get_notes_for_tag_api(tag_id: str):
    notes = NotesRepository.get_notes_for_tag(tag_id)

    if notes is None:
        raise HTTPException(status_code=404, detail="Tag not found")

    return {"notes": notes}





@router.put("/{note_id}")
def update_note_api(note_id: str, note: NoteUpdate):
    result = NotesRepository.update_note(
        note_id=note_id,
        title=note.title,
        content=note.content,
    )

    if result is None:
        raise HTTPException(status_code=404, detail="Note not found")

    return {"message": "Note updated successfully"}


@router.delete("/{note_id}")
def delete_note_api(note_id: str):
    result = NotesRepository.delete_note(note_id)

    if result is None:
        raise HTTPException(status_code=404, detail="Note not found")

    return {"message": "Note deleted successfully"}