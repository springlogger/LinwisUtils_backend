from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import create_db_and_tables
from app.routes import users

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()  # Инициализируем БД
    yield  # Здесь можно добавить код для закрытия ресурсов, если нужно

app = FastAPI(lifespan=lifespan)

# Подключение CORS
origins = ["http://localhost", "http://localhost:8080"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключаем маршруты
app.include_router(users.router, prefix="/user", tags=["users"])