from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from typing import Optional
from app.database import get_db
from app.models import User, UserRole
from app.core.security import decode_access_token
from app.core.exceptions import CredentialsException, PermissionDeniedException

# Security scheme
security = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
) -> User:
    """Get current authenticated user"""
    token = credentials.credentials
    payload = decode_access_token(token)
    
    if payload is None:
        raise CredentialsException()
    
    username: str = payload.get("sub")
    if username is None:
        raise CredentialsException()
    
    user = db.query(User).filter(User.username == username).first()
    if user is None:
        raise CredentialsException()
    
    return user


def get_current_admin(current_user: User = Depends(get_current_user)) -> User:
    """Get current user and verify admin role"""
    if current_user.role != UserRole.ADMIN:
        raise PermissionDeniedException()
    return current_user


def get_current_teacher(current_user: User = Depends(get_current_user)) -> User:
    """Get current user and verify teacher role"""
    if current_user.role != UserRole.TEACHER:
        raise PermissionDeniedException()
    return current_user


def get_current_student(current_user: User = Depends(get_current_user)) -> User:
    """Get current user and verify student role"""
    if current_user.role != UserRole.STUDENT:
        raise PermissionDeniedException()
    return current_user
