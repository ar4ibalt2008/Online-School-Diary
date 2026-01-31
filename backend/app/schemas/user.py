from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional
from app.models.user import UserRole


class UserBase(BaseModel):
    """Base user schema"""
    username: str
    email: EmailStr
    full_name: str
    role: UserRole


class UserCreate(UserBase):
    """User creation schema"""
    password: str
    
    @field_validator('password')
    @classmethod
    def validate_password(cls, v):
        if len(v) < 6:
            raise ValueError('Password must be at least 6 characters long')
        return v


class UserUpdate(BaseModel):
    """User update schema"""
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    password: Optional[str] = None


class UserResponse(UserBase):
    """User response schema"""
    id: int
    
    class Config:
        from_attributes = True


class UserInDB(UserResponse):
    """User in database schema"""
    password_hash: str
