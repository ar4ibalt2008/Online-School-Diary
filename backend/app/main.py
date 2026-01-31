from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from app.config import settings
from app.database import engine, Base
from app.api import auth, admin, teacher, student
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create database tables
Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="Online School Diary API",
)

# Mount static files
app.mount("/static", StaticFiles(directory="/app/static"), name="static")

# Setup templates
templates = Jinja2Templates(directory="app/templates")

# Include API routers
app.include_router(auth.router, prefix="/api")
app.include_router(admin.router, prefix="/api")
app.include_router(teacher.router, prefix="/api")
app.include_router(student.router, prefix="/api")


# Frontend routes
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    """Login page"""
    return templates.TemplateResponse("login.html", {"request": request})


@app.get("/admin/dashboard", response_class=HTMLResponse)
async def admin_dashboard(request: Request):
    """Admin dashboard"""
    return templates.TemplateResponse("admin/dashboard.html", {"request": request})


@app.get("/admin/users", response_class=HTMLResponse)
async def admin_users(request: Request):
    """Admin users management"""
    return templates.TemplateResponse("admin/users.html", {"request": request})


@app.get("/admin/schedule", response_class=HTMLResponse)
async def admin_schedule(request: Request):
    """Admin schedule management"""
    return templates.TemplateResponse("admin/schedule.html", {"request": request})


@app.get("/teacher/dashboard", response_class=HTMLResponse)
async def teacher_dashboard(request: Request):
    """Teacher dashboard"""
    return templates.TemplateResponse("teacher/dashboard.html", {"request": request})


@app.get("/teacher/grades", response_class=HTMLResponse)
async def teacher_grades(request: Request):
    """Teacher grades management"""
    return templates.TemplateResponse("teacher/grades.html", {"request": request})


@app.get("/student/dashboard", response_class=HTMLResponse)
async def student_dashboard(request: Request):
    """Student dashboard"""
    return templates.TemplateResponse("student/dashboard.html", {"request": request})


@app.get("/student/schedule", response_class=HTMLResponse)
async def student_schedule(request: Request):
    """Student schedule"""
    return templates.TemplateResponse("student/schedule.html", {"request": request})


@app.get("/student/grades", response_class=HTMLResponse)
async def student_grades(request: Request):
    """Student grades"""
    return templates.TemplateResponse("student/grades.html", {"request": request})


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
