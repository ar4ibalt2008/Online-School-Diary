from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models import User, Subject, Class, Schedule, Grade
from app.schemas import (
    SubjectResponse,
    ClassResponse,
    ScheduleResponse,
    GradeCreate,
    GradeUpdate,
    GradeResponse
)
from app.api.deps import get_current_teacher
from app.core.exceptions import NotFoundException

router = APIRouter(prefix="/teacher", tags=["teacher"])


@router.get("/subjects", response_model=List[SubjectResponse])
def get_my_subjects(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_teacher)
):
    """Get subjects taught by current teacher"""
    schedules = db.query(Schedule).filter(Schedule.teacher_id == current_user.id).all()
    subject_ids = list(set([s.subject_id for s in schedules]))
    subjects = db.query(Subject).filter(Subject.id.in_(subject_ids)).all()
    return subjects


@router.get("/classes", response_model=List[ClassResponse])
def get_my_classes(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_teacher)
):
    """Get classes taught by current teacher"""
    schedules = db.query(Schedule).filter(Schedule.teacher_id == current_user.id).all()
    class_ids = list(set([s.class_id for s in schedules]))
    classes = db.query(Class).filter(Class.id.in_(class_ids)).all()
    return classes


@router.get("/schedules", response_model=List[ScheduleResponse])
def get_my_schedule(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_teacher)
):
    """Get schedule for current teacher"""
    return db.query(Schedule).filter(Schedule.teacher_id == current_user.id).all()


@router.post("/grades", response_model=GradeResponse)
def create_grade(
    grade_data: GradeCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_teacher)
):
    """Create new grade"""
    grade = Grade(
        student_id=grade_data.student_id,
        subject_id=grade_data.subject_id,
        teacher_id=current_user.id,
        value=grade_data.value,
        comment=grade_data.comment
    )
    db.add(grade)
    db.commit()
    db.refresh(grade)
    return grade


@router.put("/grades/{grade_id}", response_model=GradeResponse)
def update_grade(
    grade_id: int,
    grade_data: GradeUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_teacher)
):
    """Update grade"""
    grade = db.query(Grade).filter(
        Grade.id == grade_id,
        Grade.teacher_id == current_user.id
    ).first()
    
    if not grade:
        raise NotFoundException("Grade not found or you don't have permission")
    
    if grade_data.value:
        grade.value = grade_data.value
    if grade_data.comment is not None:
        grade.comment = grade_data.comment
    
    db.commit()
    db.refresh(grade)
    return grade


@router.get("/grades/subject/{subject_id}", response_model=List[GradeResponse])
def get_grades_by_subject(
    subject_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_teacher)
):
    """Get all grades for a subject taught by current teacher"""
    return db.query(Grade).filter(
        Grade.subject_id == subject_id,
        Grade.teacher_id == current_user.id
    ).all()
