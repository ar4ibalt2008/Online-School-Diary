from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Class(Base):
    """Class model"""
    __tablename__ = "classes"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, nullable=False)  # e.g., "10A", "11B"
    year = Column(Integer, nullable=False)  # e.g., 2024
    teacher_id = Column(Integer, ForeignKey("users.id"), nullable=True)  # Class teacher
    
    # Relationships
    teacher = relationship("User", back_populates="classes_as_teacher")
    schedules = relationship("Schedule", back_populates="class_obj")
    
    def __repr__(self):
        return f"<Class {self.name}>"
