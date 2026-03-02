from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

from database.tags_db import create_tag, get_all_tags

router = APIRouter(prefix="/api/tags", tags=["Tags"])


class TagCreate(BaseModel):
    name: str


class TagResponse(BaseModel):
    id: str
    name: str


@router.post("/", response_model=TagResponse)
def create_tag_api(tag: TagCreate):
    result = create_tag(tag.name)

    if result is None:
        raise HTTPException(status_code=400, detail="Tag already exists")

    return result


@router.get("/", response_model=List[TagResponse])
def get_tags_api():
    return get_all_tags()
    