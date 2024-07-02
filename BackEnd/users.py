from fastapi import FastAPI
from pydantic import BaseModel # Definir una entidad users



app = FastAPI()

@app.get('/users')
async def users():
    return [
        {
            'name': 'Carlos',
            'surname': 'Blanco'
        },
        {
            'name': 'Javier',
            'surname': 'Blanco'
        },]