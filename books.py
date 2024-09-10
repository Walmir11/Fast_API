from fastapi import FastAPI

app = FastAPI()

@app.get('/api-endpoint')
# async é usado para funções assíncronas, ele é opcional
async def first_api():
    return {'messege': 'Hello World'}


