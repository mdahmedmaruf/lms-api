from fastapi import FastAPI

app = FastAPI(title='Library Management API')

@app.get('/')
async def root():
    return {'message': 'Library Management API is running'}