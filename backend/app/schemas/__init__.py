from app.schemas.auth import Token, TokenData, LoginRequest
from app.schemas.user import UserCreate, UserUpdate, UserResponse, UserInDB
from app.schemas.subject import SubjectCreate, SubjectUpdate, SubjectResponse
from app.schemas.class_schema import ClassCreate, ClassUpdate, ClassResponse
from app.schemas.schedule import ScheduleCreate, ScheduleUpdate, ScheduleResponse
from app.schemas.grade import GradeCreate, GradeUpdate, GradeResponse

__all__ = [
    "Token",
    "TokenData",
    "LoginRequest",
    "UserCreate",
    "UserUpdate",
    "UserResponse",
    "UserInDB",
    "SubjectCreate",
    "SubjectUpdate",
    "SubjectResponse",
    "ClassCreate",
    "ClassUpdate",
    "ClassResponse",
    "ScheduleCreate",
    "ScheduleUpdate",
    "ScheduleResponse",
    "GradeCreate",
    "GradeUpdate",
    "GradeResponse",
]
