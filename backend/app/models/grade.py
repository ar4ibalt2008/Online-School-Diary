from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base


class Grade(Base):
    """Grade model"""
    __tablename__ = "grades"
    
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    subject_id = Column(Integer, ForeignKey("subjects.id"), nullable=False)
    teacher_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    value = Column(Integer, nullable=False)  # Grade value (e.g., 1-5 or 1-100)
    comment = Column(Text, nullable=True)
    date = Column(DateTime, default=datetime.utcnow, nullable=False)
    
    # Relationships
    student = relationship("User", back_populates="grades_as_student", foreign_keys=[student_id])
    teacher = relationship("User", back_populates="grades_as_teacher", foreign_keys=[teacher_id])
    subject = relationship("Subject", back_populates="grades")
    
    def __repr__(self):
        return f"<Grade {self.value} for student_id={self.student_id}>"
