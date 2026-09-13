from contextlib import asynccontextmanager

from fastapi import FastAPI

from core.config import settings
from core.database import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(title=settings.APP_NAME, debug=settings.DEBUG, lifespan=lifespan)

@app.get('/')
async def root():
    return {'message': f'{settings.APP_NAME} is running', 'environment': settings.ENVIRONMENT}