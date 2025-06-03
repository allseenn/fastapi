# 3-4 example Возврат другого типа ответа с помощью аргумента response_model
import datetime
from fastapi import APIRouter
from  example.tags.model.tag import TagIn, Tag, TagOut
import example.tags.service.tag as service

routes = APIRouter(prefix="/api/tag", tags=["Chapter 3. FastAPI Tour"])

@routes.post("/", summary="3-4. Возврат другого типа ответа с помощью аргумента response_model")
def create(tag_in: TagIn) -> TagIn:
    tag: Tag = Tag(tag=tag_in.tag, created=datetime. datetime.utcnow(), secret="shhhh")
    service.create(tag)
    return tag

@routes.get("/{tag_str}", response_model=TagOut, summary="3-4. Возврат другого типа ответа с помощью аргумента response_model")
def get_one(tag_str: str) -> TagOut:
    tag: Tag = service.get(tag_str)
    return tag

