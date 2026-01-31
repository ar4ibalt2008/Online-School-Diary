from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List, Dict
from app.database import get_db
from app.models import User, Subject, Schedule, Grade
from app.schemas import SubjectResponse, ScheduleResponse, GradeResponse
from app.api.deps import get_current_student

router = APIRouter(prefix="/student", tags=["student"])


@router.get("/subjects", response_model=List[SubjectResponse])
def get_my_subjects(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_student)
):
    """Get subjects for current student"""
    # For simplicity, we'll return all subjects
    # In production, you'd filter by student's class
    return db.query(Subject).all()


@router.get("/schedule", response_model=List[ScheduleResponse])
def get_my_schedule(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_student)
):
    """Get schedule for current student"""
    # For simplicity, returning all schedules
    # In production, you'd filter by student's class
    return db.query(Schedule).all()


@router.get("/grades", response_model=List[GradeResponse])
def get_my_grades(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_student)
):
    """Get all grades for current student"""
    return db.query(Grade).filter(Grade.student_id == current_user.id).all()


@router.get("/grades/subject/{subject_id}", response_model=List[GradeResponse])
def get_grades_by_subject(
    subject_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_student)
):
    """Get grades for specific subject"""
    return db.query(Grade).filter(
        Grade.student_id == current_user.id,
        Grade.subject_id == subject_id
    ).all()


@router.get("/grades/average")
def get_average_grade(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_student)
):
    """Get average grade for current student"""
    avg = db.query(func.avg(Grade.value)).filter(
        Grade.student_id == current_user.id
    ).scalar()
    
    return {
        "average": round(float(avg), 2) if avg else 0,
        "student_id": current_user.id
    }


@router.get("/grades/average/subjects")
def get_average_by_subjects(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_student)
):
    """Get average grade per subject"""
    results = db.query(
        Subject.name,
        func.avg(Grade.value).label('average')
    ).join(
        Grade, Grade.subject_id == Subject.id
    ).filter(
        Grade.student_id == current_user.id
    ).group_by(
        Subject.name
    ).all()
    
    return [
        {"subject": name, "average": round(float(avg), 2)}
        for name, avg in results
    ]
