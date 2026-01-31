from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models import User, Subject, Class, Schedule
from app.schemas import (
    UserCreate, UserUpdate, UserResponse,
    SubjectCreate, SubjectUpdate, SubjectResponse,
    ClassCreate, ClassUpdate, ClassResponse,
    ScheduleCreate, ScheduleUpdate, ScheduleResponse
)
from app.api.deps import get_current_admin
from app.core.security import get_password_hash
from app.core.exceptions import NotFoundException, AlreadyExistsException

router = APIRouter(prefix="/admin", tags=["admin"])


# User management
@router.post("/users", response_model=UserResponse)
def create_user(
    user_data: UserCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin)
):
    """Create new user"""
    # Check if username exists
    if db.query(User).filter(User.username == user_data.username).first():
        raise AlreadyExistsException("Username already exists")
    
    # Check if email exists
    if db.query(User).filter(User.email == user_data.email).first():
        raise AlreadyExistsException("Email already exists")
    
    # Create user
    user = User(
        username=user_data.username,
        email=user_data.email,
        full_name=user_data.full_name,
        role=user_data.role,
        password_hash=get_password_hash(user_data.password)
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    
    return user


@router.get("/users", response_model=List[UserResponse])
def get_users(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin)
):
    """Get all users"""
    return db.query(User).all()


@router.get("/users/{user_id}", response_model=UserResponse)
def get_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin)
):
    """Get user by ID"""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise NotFoundException("User not found")
    return user


@router.put("/users/{user_id}", response_model=UserResponse)
def update_user(
    user_id: int,
    user_data: UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin)
):
    """Update user"""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise NotFoundException("User not found")
    
    # Update fields
    if user_data.email:
        user.email = user_data.email
    if user_data.full_name:
        user.full_name = user_data.full_name
    if user_data.password:
        user.password_hash = get_password_hash(user_data.password)
    
    db.commit()
    db.refresh(user)
    return user


@router.delete("/users/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin)
):
    """Delete user"""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise NotFoundException("User not found")
    
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}


# Subject management
@router.post("/subjects", response_model=SubjectResponse)
def create_subject(
    subject_data: SubjectCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin)
):
    """Create new subject"""
    if db.query(Subject).filter(Subject.name == subject_data.name).first():
        raise AlreadyExistsException("Subject already exists")
    
    subject = Subject(**subject_data.model_dump())
    db.add(subject)
    db.commit()
    db.refresh(subject)
    return subject


@router.get("/subjects", response_model=List[SubjectResponse])
def get_subjects(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin)
):
    """Get all subjects"""
    return db.query(Subject).all()


# Class management
@router.post("/classes", response_model=ClassResponse)
def create_class(
    class_data: ClassCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin)
):
    """Create new class"""
    if db.query(Class).filter(Class.name == class_data.name).first():
        raise AlreadyExistsException("Class already exists")
    
    class_obj = Class(**class_data.model_dump())
    db.add(class_obj)
    db.commit()
    db.refresh(class_obj)
    return class_obj


@router.get("/classes", response_model=List[ClassResponse])
def get_classes(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin)
):
    """Get all classes"""
    return db.query(Class).all()


# Schedule management
@router.post("/schedules", response_model=ScheduleResponse)
def create_schedule(
    schedule_data: ScheduleCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin)
):
    """Create new schedule entry"""
    schedule = Schedule(**schedule_data.model_dump())
    db.add(schedule)
    db.commit()
    db.refresh(schedule)
    return schedule


@router.get("/schedules", response_model=List[ScheduleResponse])
def get_schedules(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin)
):
    """Get all schedules"""
    return db.query(Schedule).all()


@router.delete("/schedules/{schedule_id}")
def delete_schedule(
    schedule_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin)
):
    """Delete schedule entry"""
    schedule = db.query(Schedule).filter(Schedule.id == schedule_id).first()
    if not schedule:
        raise NotFoundException("Schedule not found")
    
    db.delete(schedule)
    db.commit()
    return {"message": "Schedule deleted successfully"}

