from pydantic import BaseModel
from typing import Optional
from app.models.schedule import DayOfWeek


class ScheduleBase(BaseModel):
    """Base schedule schema"""
    class_id: int
    subject_id: int
    teacher_id: int
    day_of_week: DayOfWeek
    time_slot: str


class ScheduleCreate(ScheduleBase):
    """Schedule creation schema"""
    pass


class ScheduleUpdate(BaseModel):
    """Schedule update schema"""
    class_id: Optional[int] = None
    subject_id: Optional[int] = None
    teacher_id: Optional[int] = None
    day_of_week: Optional[DayOfWeek] = None
    time_slot: Optional[str] = None


class ScheduleResponse(ScheduleBase):
    """Schedule response schema"""
    id: int
    
    class Config:
        from_attributes = True
