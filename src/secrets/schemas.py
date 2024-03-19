from typing import Optional, List, Any

from pydantic import (
    BaseModel, EmailStr, validator,  field_validator, Field)

from src.db.session import Session
from src.tags.models import Tag



class SecretFileModel(BaseModel):
    title: str
    description: Optional[str]
    tags: List[str]
    
    
    @field_validator('tags')
    @classmethod
    def unique_tags(cls, vars: List[str]) -> str:
        return list(set(vars))
    
    
    @field_validator('tags')
    @classmethod
    def exists_tags(cls, vars: List[str]):
        for name in vars:
            tag = Session.query(Tag).filter_by(id=name).one_or_none()
            if tag is None:
                raise ValueError(f"The '{tag}' tag does not exist")
        return vars
    