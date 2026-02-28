from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from uuid import uuid4
from typing import List

from database import read_db, write_db

router = APIRouter(prefix="/api/tags", tags=["Tags"])


class TagCreate(BaseModel):
    name: str


class TagResponse(BaseModel):
    id: str
    name: str


@router.post("/", response_model=TagResponse)
def create_tag(tag: TagCreate):
    db = read_db()

    # prevent duplicate tag names
    for existing_tag in db["tags"]:
        if existing_tag["name"].lower() == tag.name.lower():
            raise HTTPException(status_code=400, detail="Tag already exists")

    new_tag = {
        "id": str(uuid4()),
        "name": tag.name
    }

    db["tags"].append(new_tag)
    write_db(db)

    return new_tag






@router.get("/", response_model=List[TagResponse])
def get_all_tags():
    db = read_db()
    return db["tags"]


