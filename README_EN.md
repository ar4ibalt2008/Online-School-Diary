# 🎓 Online School Diary

A full-stack web application for school diary management with role-based access control (Admin, Teacher, Student).

## 📋 Table of Contents

- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Database Schema](#database-schema)
- [Development](#development)
- [Testing](#testing)
- [Deployment](#deployment)

## ✨ Features

### 👨‍💼 Administrator
- User management (create, edit, delete)
- Subject management
- Class management
- Schedule creation and editing
- System statistics viewing

### 👨‍🏫 Teacher
- Grade assignment to students
- Grade editing and commenting
- Viewing subjects and classes taught
- Personal schedule viewing

### 👨‍🎓 Student
- Grade viewing by subjects
- Academic performance statistics
- GPA calculation
- Performance charts
- Schedule viewing

## 🛠 Technology Stack

### Backend
- **Python 3.11**
- **FastAPI 0.109.0** - Modern web framework
- **SQLAlchemy 2.0.25** - ORM for database
- **Alembic 1.13.1** - Database migrations
- **PostgreSQL 15** - Main database
- **Pydantic 2.5.3** - Data validation
- **PyJWT** - JWT token authentication
- **Passlib & Bcrypt** - Password hashing

### Frontend
- **Jinja2 3.1.3** - Template engine
- **Bootstrap 5.3.2** - CSS framework
- **Chart.js** - Charts and graphs
- **Vanilla JavaScript** - Client-side logic

### DevOps
- **Docker & Docker Compose** - Containerization
- **Uvicorn** - ASGI server

## 📁 Project Structure

```
online-school-diary/
├── backend/
│   ├── app/
│   │   ├── api/              # API endpoints
│   │   │   ├── admin.py      # Admin routes
│   │   │   ├── auth.py       # Authentication
│   │   │   ├── teacher.py    # Teacher routes
│   │   │   └── student.py    # Student routes
│   │   ├── core/             # Core functionality
│   │   │   ├── config.py     # Configuration
│   │   │   ├── security.py   # Security utilities
│   │   │   └── exceptions.py # Custom exceptions
│   │   ├── models/           # Database models
│   │   │   ├── user.py
│   │   │   ├── subject.py
│   │   │   ├── class_model.py
│   │   │   ├── schedule.py
│   │   │   └── grade.py
│   │   ├── schemas/          # Pydantic schemas
│   │   ├── templates/        # HTML templates
│   │   │   ├── admin/
│   │   │   ├── teacher/
│   │   │   └── student/
│   │   ├── database.py       # Database connection
│   │   └── main.py           # Application entry point
│   ├── alembic/              # Database migrations
│   ├── Dockerfile
│   └── requirements.txt
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
├── docker-compose.yml
├── .env.example
└── README.md
```

## 🚀 Installation

### Prerequisites

- Docker Desktop 24.0+
- Docker Compose 2.0+

### Quick Start with Docker

1. **Clone the repository:**
```bash
git clone <repository-url>
cd online-school-diary
```

2. **Create environment file:**
```bash
cp .env.example .env
```

3. **Edit `.env` file:**
```env
DATABASE_URL=postgresql://postgres:postgres@db:5432/school_diary
SECRET_KEY=your-secret-key-here-change-in-production
ACCESS_TOKEN_EXPIRE_MINUTES=1440
```

4. **Start the application:**
```bash
docker-compose up -d
```

5. **Apply database migrations:**
```bash
docker-compose exec backend alembic upgrade head
```

6. **Initialize test data:**
```bash
docker-compose exec backend python init_data.py
```

7. **Open in browser:**
```
http://localhost:8000
```

### Manual Installation (Without Docker)

1. **Install Python 3.11**

2. **Install PostgreSQL 15**

3. **Create virtual environment:**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

4. **Install dependencies:**
```bash
pip install -r requirements.txt
```

5. **Create database:**
```sql
CREATE DATABASE school_diary;
```

6. **Configure environment:**
```bash
cp ../.env.example ../.env
# Edit .env with your settings
```

7. **Run migrations:**
```bash
alembic upgrade head
```

8. **Initialize data:**
```bash
python init_data.py
```

9. **Start server:**
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `DATABASE_URL` | PostgreSQL connection string | `postgresql://postgres:postgres@db:5432/school_diary` |
| `SECRET_KEY` | JWT secret key | `your-secret-key-change-in-production` |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Token lifetime (minutes) | `1440` (24 hours) |
| `ALGORITHM` | JWT algorithm | `HS256` |

### Default Test Credentials

| Role | Username | Password |
|------|----------|----------|
| Administrator | `admin` | `admin123` |
| Teacher | `teacher` | `teacher123` |
| Student | `student` | `student123` |

**⚠️ Important:** Change passwords in production!

## 📖 Usage

### Access the Application

1. Open browser: `http://localhost:8000`
2. Log in with test credentials
3. Explore the interface

### Main Features

#### Administrator Panel
- **Users:** `/admin/users` - User management
- **Schedule:** `/admin/schedule` - Schedule management
- **Dashboard:** `/admin/dashboard` - Statistics

#### Teacher Panel
- **Dashboard:** `/teacher/dashboard` - Subjects and classes
- **Grades:** `/teacher/grades` - Grade management

#### Student Panel
- **Dashboard:** `/student/dashboard` - GPA and recent grades
- **Grades:** `/student/grades` - Grade history with charts
- **Schedule:** `/student/schedule` - Weekly schedule

## 📚 API Documentation

### Interactive Documentation

- **Swagger UI:** `http://localhost:8000/docs`
- **ReDoc:** `http://localhost:8000/redoc`

### Authentication

All protected endpoints require JWT token in header:
```
Authorization: Bearer <token>
```

### Main Endpoints

#### Authentication
```
POST /api/auth/login - User authentication
```

#### Admin Routes
```
GET    /api/admin/users           - Get all users
POST   /api/admin/users           - Create user
GET    /api/admin/users/{id}      - Get user by ID
PUT    /api/admin/users/{id}      - Update user
DELETE /api/admin/users/{id}      - Delete user

GET    /api/admin/subjects        - Get all subjects
POST   /api/admin/subjects        - Create subject
PUT    /api/admin/subjects/{id}   - Update subject
DELETE /api/admin/subjects/{id}   - Delete subject

GET    /api/admin/classes         - Get all classes
POST   /api/admin/classes         - Create class
PUT    /api/admin/classes/{id}    - Update class
DELETE /api/admin/classes/{id}    - Delete class

GET    /api/admin/schedules       - Get all schedules
POST   /api/admin/schedules       - Create schedule
PUT    /api/admin/schedules/{id}  - Update schedule
DELETE /api/admin/schedules/{id}  - Delete schedule
```

#### Teacher Routes
```
GET  /api/teacher/subjects              - Get my subjects
GET  /api/teacher/classes               - Get my classes
GET  /api/teacher/schedules             - Get my schedule
GET  /api/teacher/students              - Get all students
POST /api/teacher/grades                - Create grade
PUT  /api/teacher/grades/{id}           - Update grade
GET  /api/teacher/grades/subject/{id}   - Get grades by subject
```

#### Student Routes
```
GET /api/student/schedule               - Get my schedule
GET /api/student/grades                 - Get my grades
GET /api/student/grades/subject/{id}    - Get grades by subject
GET /api/student/grades/average         - Get average grade
GET /api/student/grades/average/{id}    - Get average by subject
```

### Request/Response Examples

#### Login
```http
POST /api/auth/login
Content-Type: application/json

{
  "username": "teacher",
  "password": "teacher123"
}
```

Response:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

#### Create Grade
```http
POST /api/teacher/grades
Authorization: Bearer <token>
Content-Type: application/json

{
  "student_id": 3,
  "subject_id": 1,
  "value": 5,
  "comment": "Excellent work!"
}
```

Response:
```json
{
  "id": 1,
  "student_id": 3,
  "subject_id": 1,
  "teacher_id": 2,
  "value": 5,
  "comment": "Excellent work!",
  "date": "2025-01-31"
}
```

## 🗄 Database Schema

### Entity-Relationship Diagram

```
┌─────────────┐
│    User     │
├─────────────┤
│ id          │◄──┐
│ username    │   │
│ email       │   │
│ password    │   │
│ role        │   │
│ full_name   │   │
└─────────────┘   │
                  │
┌─────────────┐   │    ┌─────────────┐
│   Subject   │   │    │    Class    │
├─────────────┤   │    ├─────────────┤
│ id          │◄──┼────┤ id          │
│ name        │   │    │ name        │
│ description │   │    │ year        │
└─────────────┘   │    │ teacher_id  │─┐
                  │    └─────────────┘ │
                  │                    │
┌─────────────┐   │                    │
│   Grade     │   │                    │
├─────────────┤   │                    │
│ id          │   │    ┌─────────────┐ │
│ student_id  │───┘    │  Schedule   │ │
│ teacher_id  │───────►│─────────────│ │
│ subject_id  │───┐    │ id          │ │
│ value       │   │    │ class_id    │◄┘
│ comment     │   │    │ subject_id  │◄─┘
│ date        │   │    │ teacher_id  │──┘
└─────────────┘   │    │ day_of_week │
                  │    │ time_slot   │
                  └────┤ created_at  │
                       └─────────────┘
```

### Tables

#### users
- `id` - Primary key
- `username` - Unique login
- `email` - Unique email
- `password_hash` - Bcrypt password hash
- `role` - User role (ADMIN, TEACHER, STUDENT)
- `full_name` - Full name

#### subjects
- `id` - Primary key
- `name` - Subject name
- `description` - Description

#### classes
- `id` - Primary key
- `name` - Class name (e.g., "10A")
- `year` - Academic year
- `teacher_id` - Class teacher (FK → users)

#### schedules
- `id` - Primary key
- `class_id` - FK → classes
- `subject_id` - FK → subjects
- `teacher_id` - FK → users
- `day_of_week` - Day (MONDAY...SUNDAY)
- `time_slot` - Time (e.g., "08:00-08:45")

#### grades
- `id` - Primary key
- `student_id` - FK → users
- `teacher_id` - FK → users
- `subject_id` - FK → subjects
- `value` - Grade (1-5)
- `comment` - Optional comment
- `date` - Date assigned

## 💻 Development

### Running in Development Mode

```bash
# Backend with auto-reload
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Or with Docker
docker-compose up
```

### Creating Database Migrations

```bash
# Auto-generate migration
alembic revision --autogenerate -m "Description"

# Apply migrations
alembic upgrade head

# Rollback
alembic downgrade -1
```

### Code Style

- **Backend:** Follow PEP 8
- **Frontend:** Use Prettier/ESLint
- **Commits:** Conventional Commits format

### Project Guidelines

1. All API endpoints must have documentation
2. All functions must have type hints
3. All models must have relationships defined
4. All schemas must have examples
5. Error handling for all endpoints

## 🧪 Testing

### Manual Testing

1. **Authentication:**
   - Login as admin/teacher/student
   - Token validation
   - Logout

2. **CRUD Operations:**
   - Create/Read/Update/Delete for all entities
   - Validation testing
   - Permission testing

3. **Business Logic:**
   - Grade calculation
   - GPA computation
   - Schedule conflicts

### API Testing

Use Swagger UI at `http://localhost:8000/docs`:

1. Authenticate with POST `/api/auth/login`
2. Copy access token
3. Click "Authorize" button
4. Paste token
5. Test endpoints

## 🚢 Deployment

### Docker Deployment (Recommended)

1. **Set production environment:**
```bash
cp .env.example .env
# Edit .env with production values
```

2. **Build and run:**
```bash
docker-compose -f docker-compose.prod.yml up -d
```

3. **Apply migrations:**
```bash
docker-compose exec backend alembic upgrade head
```

### Security Checklist

- [ ] Change `SECRET_KEY` to random string
- [ ] Change default passwords
- [ ] Use HTTPS
- [ ] Configure CORS properly
- [ ] Set up firewall rules
- [ ] Enable database backups
- [ ] Set up logging
- [ ] Configure rate limiting

### Production Settings

```env
# .env for production
DATABASE_URL=postgresql://user:password@prod-db:5432/school_diary
SECRET_KEY=<generate-strong-random-key>
ACCESS_TOKEN_EXPIRE_MINUTES=60
ENVIRONMENT=production
```

## 📝 Common Issues

### Docker Issues

**Problem:** Containers won't start
```bash
# Solution: Check logs
docker-compose logs backend
docker-compose logs db

# Restart with rebuild
docker-compose down
docker-compose up -d --build
```

**Problem:** Database connection error
```bash
# Solution: Check database is healthy
docker-compose ps

# Reset database
docker-compose down -v
docker-compose up -d
```

### Application Issues

**Problem:** 404 on static files
```bash
# Solution: Check static path in main.py
app.mount("/static", StaticFiles(directory="/app/static"), name="static")
```

**Problem:** Token expired immediately
```bash
# Solution: Check ACCESS_TOKEN_EXPIRE_MINUTES in .env
ACCESS_TOKEN_EXPIRE_MINUTES=1440
```

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## 📄 License

This project is licensed under the MIT License.

## 👨‍💻 Author

Developed by [Your Name]

## 📧 Contact

- Email: your.email@example.com
- Telegram: @yourusername
- GitHub: @yourusername

## 🙏 Acknowledgments

- FastAPI documentation
- SQLAlchemy documentation
- Bootstrap documentation
- PostgreSQL community

---

**Built with ❤️ using Python, FastAPI, and PostgreSQL**
