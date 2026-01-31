from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from app.database import Base


class Subject(Base):
    """Subject model"""
    __tablename__ = "subjects"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=True)
    
    # Relationships
    schedules = relationship("Schedule", back_populates="subject")
    grades = relationship("Grade", back_populates="subject")
    
    def __repr__(self):
        return f"<Subject {self.name}>"
