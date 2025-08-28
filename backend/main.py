from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware  # Добавляем импорт CORS
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError

from config import SessionLocal, engine
from models import Base, User, Course

app = FastAPI()

# Добавляем настройку CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Разрешаем запросы с React-приложения
    allow_credentials=True,
    allow_methods=["*"],  # Разрешаем все методы (GET, POST, etc.)
    allow_headers=["*"],  # Разрешаем все заголовки
)

# Инициализация БД
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    # Добавляем тестовые курсы, если их нет
    async with SessionLocal() as session:
        result = await session.execute(select(Course))
        if not result.scalars().first():
            test_courses = [
                Course(title="Python для начинающих", description="Базовый курс Python"),
                Course(title="Web-разработка", description="Создание веб-приложений"),
                Course(title="Data Science", description="Основы науки о данных")
            ]
            for course in test_courses:
                session.add(course)
            await session.commit()

# Подключаем инициализацию БД при старте приложения
@app.on_event("startup")
async def startup_event():
    await init_db()

# Получение сессии БД
async def get_db():
    async with SessionLocal() as session:
        yield session

# Маршрут для получения курсов
@app.get("/courses/")
async def get_courses(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Course))
    courses = result.scalars().all()
    return {"courses": [{"id": c.id, "title": c.title, "description": c.description} for c in courses]}

# Маршрут для регистрации пользователей
@app.post("/register/")
async def register_user(username: str, password: str, db: AsyncSession = Depends(get_db)):
    new_user = User(username=username, password=password)
    db.add(new_user)
    try:
        await db.commit()
        await db.refresh(new_user)
        return {"message": "Пользователь успешно зарегистрирован"}
    except IntegrityError:
        await db.rollback()
        raise HTTPException(status_code=400, detail="Пользователь с таким именем уже существует")
