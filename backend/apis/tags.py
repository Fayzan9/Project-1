from fastapi import APIRouter, HTTPException
from typing import List
from model import TagCreate, TagResponse
from database.repositories.tags_repository import TagsRepository

router = APIRouter(prefix="/api/tags", tags=["Tags"])




@router.post("/", response_model=TagResponse)
def create_tag_api(tag: TagCreate):
    result = TagsRepository.create_tag(tag.name)

    if result is None:
        raise HTTPException(status_code=400, detail="Tag already exists")

    return result


@router.get("/", response_model=List[TagResponse])
def get_tags_api():
    return TagsRepository.get_all_tags()
    