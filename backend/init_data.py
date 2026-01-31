"""
Script to initialize database with sample data
Run: python init_data.py
"""
from app.database import SessionLocal
from app.models import User, Subject, Class, UserRole
from app.core.security import get_password_hash


def init_database():
    """Initialize database with sample data"""
    db = SessionLocal()
    
    try:
        # Check if admin already exists
        admin = db.query(User).filter(User.username == "admin").first()
        if admin:
            print("Database already initialized")
            return
        
        # Create admin user
        admin = User(
            username="admin",
            email="admin@school.com",
            full_name="Administrator",
            role=UserRole.ADMIN,
            password_hash=get_password_hash("admin123")
        )
        db.add(admin)
        
        # Create teacher user
        teacher = User(
            username="teacher",
            email="teacher@school.com",
            full_name="Иван Иванович Иванов",
            role=UserRole.TEACHER,
            password_hash=get_password_hash("teacher123")
        )
        db.add(teacher)
        
        # Create student user
        student = User(
            username="student",
            email="student@school.com",
            full_name="Петр Петрович Петров",
            role=UserRole.STUDENT,
            password_hash=get_password_hash("student123")
        )
        db.add(student)
        
        # Create subjects
        subjects = [
            Subject(name="Математика", description="Алгебра и геометрия"),
            Subject(name="Русский язык", description="Грамматика и литература"),
            Subject(name="Физика", description="Механика и электричество"),
            Subject(name="История", description="История России и мира"),
            Subject(name="Английский язык", description="Грамматика и разговорная практика"),
        ]
        for subject in subjects:
            db.add(subject)
        
        # Create class
        class_obj = Class(
            name="10А",
            year=2025,
            teacher_id=None
        )
        db.add(class_obj)
        
        db.commit()
        print("Database initialized successfully!")
        print("\nTest credentials:")
        print("Admin: admin / admin123")
        print("Teacher: teacher / teacher123")
        print("Student: student / student123")
        
    except Exception as e:
        print(f"Error initializing database: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    init_database()
