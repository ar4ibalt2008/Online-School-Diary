from pydantic import BaseModel
from typing import Optional


class ClassBase(BaseModel):
    """Base class schema"""
    name: str
    year: int
    teacher_id: Optional[int] = None


class ClassCreate(ClassBase):
    """Class creation schema"""
    pass


class ClassUpdate(BaseModel):
    """Class update schema"""
    name: Optional[str] = None
    year: Optional[int] = None
    teacher_id: Optional[int] = None


class ClassResponse(ClassBase):
    """Class response schema"""
    id: int
    
    class Config:
        from_attributes = True
