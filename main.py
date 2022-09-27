# Nama  : Fatih Darielma Gaizta
# NIM   : 18220009

# FILE main.py
# Membuat API dengan HTTP method GET dan POST menggunakan FastAPI
# How to test the API: Jalankan local server > run get.py/post.py dalam folder client
# How to run local server on terminal: uvicorn main:app --reload

from fastapi import FastAPI

app = FastAPI()

@app.get('/api/')
async def root():
    data = {
        'message': 'Hello, World!'
    }
    return data

@app.post('/api/post/')
async def post(mahasiswa:dict):
    return mahasiswa