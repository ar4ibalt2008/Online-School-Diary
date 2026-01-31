from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.database import Base
import enum


class DayOfWeek(str, enum.Enum):
    """Days of week enum"""
    MONDAY = "monday"
    TUESDAY = "tuesday"
    WEDNESDAY = "wednesday"
    THURSDAY = "thursday"
    FRIDAY = "friday"
    SATURDAY = "saturday"


class Schedule(Base):
    """Schedule model"""
    __tablename__ = "schedules"
    
    id = Column(Integer, primary_key=True, index=True)
    class_id = Column(Integer, ForeignKey("classes.id"), nullable=False)
    subject_id = Column(Integer, ForeignKey("subjects.id"), nullable=False)
    teacher_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    day_of_week = Column(Enum(DayOfWeek), nullable=False)
    time_slot = Column(String(20), nullable=False)  # e.g., "08:00-08:45"
    
    # Relationships
    class_obj = relationship("Class", back_populates="schedules")
    subject = relationship("Subject", back_populates="schedules")
    teacher = relationship("User")
    
    def __repr__(self):
        return f"<Schedule {self.day_of_week} {self.time_slot}>"
