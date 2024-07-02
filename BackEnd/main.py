from fastapi import FastAPI

app = FastAPI()

# url local: http://127.0.0.1:8000

@app.get("/")
async def root():
    return 'Hello World'

# url local: http://127.0.0.1:8000/url

@app.get('/url')
async def url():
    return {'url': 'https://www.urlexample.com'}

# Inicia el server: uvicorn main:app --reload
# Detener el server: CTRL+C

# Documentacion con Swagger: http://127.0.0.1:8000/docs
# Documentacion con Redocly: http://127.0.0.1:8000/redoc

