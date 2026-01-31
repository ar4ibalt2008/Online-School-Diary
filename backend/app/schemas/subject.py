from pydantic import BaseModel
from typing import Optional


class SubjectBase(BaseModel):
    """Base subject schema"""
    name: str
    description: Optional[str] = None


class SubjectCreate(SubjectBase):
    """Subject creation schema"""
    pass


class SubjectUpdate(BaseModel):
    """Subject update schema"""
    name: Optional[str] = None
    description: Optional[str] = None


class SubjectResponse(SubjectBase):
    """Subject response schema"""
    id: int
    
    class Config:
        from_attributes = True
