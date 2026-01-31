# Структура проекта Online School Diary

## Версии технологий

### Backend
- Python: 3.11
- FastAPI: 0.109.0
- PostgreSQL: 15
- SQLAlchemy: 2.0.25
- Alembic: 1.13.1
- PyJWT: 2.8.0
- Passlib: 1.7.4
- Python-multipart: 0.0.6
- Uvicorn: 0.27.0
- Psycopg2-binary: 2.9.9

### Frontend
- Bootstrap: 5.3.2
- Jinja2: 3.1.3

### DevOps
- Docker: 24.0+
- Docker Compose: 2.0+

## Структура файлов

```
online-school-diary/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py                 # Точка входа FastAPI
│   │   ├── config.py               # Конфигурация приложения
│   │   ├── database.py             # Настройка БД
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── user.py             # Модель User
│   │   │   ├── subject.py          # Модель Subject
│   │   │   ├── class_model.py      # Модель Class
│   │   │   ├── schedule.py         # Модель Schedule
│   │   │   └── grade.py            # Модель Grade
│   │   ├── schemas/
│   │   │   ├── __init__.py
│   │   │   ├── user.py             # Pydantic схемы User
│   │   │   ├── subject.py          # Pydantic схемы Subject
│   │   │   ├── class_schema.py     # Pydantic схемы Class
│   │   │   ├── schedule.py         # Pydantic схемы Schedule
│   │   │   ├── grade.py            # Pydantic схемы Grade
│   │   │   └── auth.py             # Схемы авторизации
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   ├── deps.py             # Зависимости (auth, db)
│   │   │   ├── auth.py             # Эндпоинты авторизации
│   │   │   ├── admin.py            # Эндпоинты администратора
│   │   │   ├── teacher.py          # Эндпоинты учителя
│   │   │   └── student.py          # Эндпоинты ученика
│   │   ├── core/
│   │   │   ├── __init__.py
│   │   │   ├── security.py         # JWT, хеширование паролей
│   │   │   └── exceptions.py       # Кастомные исключения
│   │   └── templates/
│   │       ├── base.html           # Базовый шаблон
│   │       ├── login.html          # Страница входа
│   │       ├── admin/
│   │       │   ├── dashboard.html  # Панель администратора
│   │       │   ├── users.html      # Управление пользователями
│   │       │   └── schedule.html   # Управление расписанием
│   │       ├── teacher/
│   │       │   ├── dashboard.html  # Панель учителя
│   │       │   └── grades.html     # Выставление оценок
│   │       └── student/
│   │           ├── dashboard.html  # Панель ученика
│   │           ├── schedule.html   # Расписание
│   │           └── grades.html     # Оценки
│   ├── alembic/
│   │   ├── versions/               # Миграции БД
│   │   ├── env.py
│   │   └── script.py.mako
│   ├── alembic.ini                 # Конфигурация Alembic
│   ├── requirements.txt            # Python зависимости
│   └── Dockerfile                  # Docker для backend
├── static/
│   ├── css/
│   │   └── style.css               # Кастомные стили
│   └── js/
│       └── main.js                 # JavaScript функции
├── docker-compose.yml              # Docker Compose конфигурация
├── .env.example                    # Пример переменных окружения
├── .gitignore
└── README.md                       # Документация проекта
```

## Описание основных компонентов

### Models (SQLAlchemy)
- **User**: id, username, password_hash, role (admin/teacher/student), email
- **Subject**: id, name, description
- **Class**: id, name, year, teacher_id
- **Schedule**: id, class_id, subject_id, teacher_id, day_of_week, time_slot
- **Grade**: id, student_id, subject_id, value, comment, date, teacher_id

### API Routes
- `/api/auth/login` - Авторизация
- `/api/admin/*` - Эндпоинты администратора
- `/api/teacher/*` - Эндпоинты учителя
- `/api/student/*` - Эндпоинты ученика

### Frontend Routes
- `/` - Страница входа
- `/admin/dashboard` - Панель администратора
- `/teacher/dashboard` - Панель учителя
- `/student/dashboard` - Панель ученика
