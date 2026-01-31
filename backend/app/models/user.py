from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from app.database import Base
import enum


class UserRole(str, enum.Enum):
    """User roles enum"""
    ADMIN = "admin"
    TEACHER = "teacher"
    STUDENT = "student"


class User(Base):
    """User model"""
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    email = Column(String(100), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    role = Column(Enum(UserRole), nullable=False)
    full_name = Column(String(100), nullable=False)
    
    # Relationships
    grades_as_student = relationship("Grade", back_populates="student", foreign_keys="Grade.student_id")
    grades_as_teacher = relationship("Grade", back_populates="teacher", foreign_keys="Grade.teacher_id")
    classes_as_teacher = relationship("Class", back_populates="teacher")
    
    def __repr__(self):
        return f"<User {self.username} ({self.role})>"
