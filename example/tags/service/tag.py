# Данный модуль написал сам, что схема с тэгами работала (web/tag.py и
# model/tag.py)
from typing import Dict
from example.tags.model.tag import Tag

# Простое хранилище тегов в памяти
_tag_store: Dict[str, Tag] = {}

def create(tag: Tag) -> None:
    _tag_store[tag.tag] = tag

def get(tag_str: str) -> Tag:
    tag = _tag_store.get(tag_str)
    if tag is None:
        raise ValueError(f"Tag '{tag_str}' not found.")
    return tag

