# /mnt/f/chatbot/backend/main.py
import logging
from fastapi import FastAPI, Request
from transformers import AutoTokenizer, AutoModelForCausalLM
import openai
import torch

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Lade das GPT4All-13B-Snoozy Modell
tokenizer = AutoTokenizer.from_pretrained("nomic-ai/gpt4all-13b-snoozy", legacy=False)
model = AutoModelForCausalLM.from_pretrained("nomic-ai/gpt4all-13b-snoozy")

# OpenAI API Key setzen (für Online-Modell)
openai.api_key = 'sk-proj-Iy5hqvFFUZvheJiMEk3TT3BlbkFJgbRoHnYeJfzFKvi00h11'

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    message = data.get('message', '')
    model_type = data.get('model', 'local')  # 'local' oder 'online'

    logger.info(f"Received message: {message}")
    logger.info(f"Model type: {model_type}")
    
    if model_type == 'online':
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=message,
            max_tokens=50
        ).choices[0].text.strip()
    else:
        inputs = tokenizer(message, return_tensors="pt")
        outputs = model.generate(**inputs, max_length=50)
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    logger.info(f"Response: {response}")
    return {"response": response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8100)
