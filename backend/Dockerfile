<<<<<<< HEAD
# /mnt/f/chatbot/backend/Dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install watchdog

COPY . .

CMD ["uvicorn", "main:app", "--reload", "--port", "8100"]
=======
# /mnt/f/chatbot/backend/Dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install watchdog

COPY . .

CMD ["uvicorn", "main:app", "--reload", "--port", "8100"]
>>>>>>> origin/main
