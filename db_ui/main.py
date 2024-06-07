# db_ui/main.py
from fastapi import FastAPI, Request
import requests

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to DB_UI Module"}

@app.post("/query")
async def query_db(request: Request):
    data = await request.json()
    query = data.get('query', '')
    # Beispielhafte API-Anfrage an DB-GPT
    response = requests.post("http://db-gpt:8200/chat", json={"input": query})
    return response.json()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8300)
