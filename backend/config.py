from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+asyncpg://user:password@db:5432/online_courses"

# Создаём движок для подключения к базе
engine = create_async_engine(DATABASE_URL, echo=True)

# Фабрика сессий для взаимодействия с базой
SessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)
