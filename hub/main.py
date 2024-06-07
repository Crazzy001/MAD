# /mnt/f/chatbot/hub/main.py

from fastapi import FastAPI, Request

from fastapi import FastAPI, Request
import requests
from chat_module import chat_router

app = FastAPI()


# Beispielendpunkt
@app.get("/")
def read_root():
    return {"Hello": "Hub"}


# Inkludiert den Chat-Router
app.include_router(chat_router, prefix="/chat")

DB_GPT_URL = "http://db-gpt:8600/chat"
DB_UI_URL = "http://db-ui:8300/query"


@app.post("/query_db_ui")
async def query_db_ui(request: Request):
    data = await request.json()
    response = requests.post(DB_UI_URL, json=data)
    return response.json()


@app.post("/llama")
async def llama(request: Request):
    data = await request.json()
    response = requests.post("http://backend:8100/llama", json=data)
    return response.json()


@app.post("/whisper")
async def whisper(request: Request):
    data = await request.json()
    response = requests.post("http://backend:8100/whisper", json=data)
    return response.json()


@app.post("/control_pc")
async def control_pc(request: Request):
    data = await request.json()
    response = requests.post("http://backend:8100/control_pc", json=data)
    return response.json()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8500)


import requests
from chat_module import chat_router

app = FastAPI()

# Beispielendpunkt
@app.get("/")
def read_root():
    return {"Hello": "Hub"}

# Inkludiert den Chat-Router
app.include_router(chat_router, prefix="/chat")

DB_GPT_URL = "http://db-gpt:8600/chat"
DB_UI_URL = "http://db-ui:8300/query"

@app.post("/query_db_ui")
async def query_db_ui(request: Request):
    data = await request.json()
    response = requests.post(DB_UI_URL, json=data)
    return response.json()

@app.post("/llama")
async def llama(request: Request):
    data = await request.json()
    response = requests.post("http://backend:8100/llama", json=data)
    return response.json()

@app.post("/whisper")
async def whisper(request: Request):
    data = await request.json()
    response = requests.post("http://backend:8100/whisper", json=data)
    return response.json()

@app.post("/control_pc")
async def control_pc(request: Request):
    data = await request.json()
    response = requests.post("http://backend:8100/control_pc", json=data)
    return response.json()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8500)
