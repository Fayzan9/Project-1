from pydantic import BaseModel
from typing import List,Optional

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


class NoteUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None


class TagCreate(BaseModel):
    name: str


class TagResponse(BaseModel):
    id: str
    name: str
