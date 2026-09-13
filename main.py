from fastapi import FastAPI

from core.config import settings

app = FastAPI(title=settings.APP_NAME, debug=settings.DEBUG)

@app.get('/')
async def root():
    return {'message': f'{settings.APP_NAME} is running', 'environment': settings.ENVIRONMENT}