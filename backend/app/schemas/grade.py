from pydantic import BaseModel, field_validator
from typing import Optional
from datetime import datetime


class GradeBase(BaseModel):
    """Base grade schema"""
    student_id: int
    subject_id: int
    value: int
    comment: Optional[str] = None
    
    @field_validator('value')
    @classmethod
    def validate_value(cls, v):
        if v < 1 or v > 5:
            raise ValueError('Grade value must be between 1 and 5')
        return v


class GradeCreate(GradeBase):
    """Grade creation schema"""
    pass


class GradeUpdate(BaseModel):
    """Grade update schema"""
    value: Optional[int] = None
    comment: Optional[str] = None
    
    @field_validator('value')
    @classmethod
    def validate_value(cls, v):
        if v is not None and (v < 1 or v > 5):
            raise ValueError('Grade value must be between 1 and 5')
        return v


class GradeResponse(GradeBase):
    """Grade response schema"""
    id: int
    teacher_id: int
    date: datetime
    
    class Config:
        from_attributes = True
