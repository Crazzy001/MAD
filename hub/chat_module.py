# /mnt/f/chatbot/hub/chat_module.py

from fastapi import APIRouter, Request
from transformers import AutoTokenizer, AutoModelForCausalLM
import openai
import torch

chat_router = APIRouter()

# Lade das GPT4All-13B-Snoozy Modell
tokenizer = AutoTokenizer.from_pretrained("nomic-ai/gpt4all-13b-snoozy", use_fast=False)
model = AutoModelForCausalLM.from_pretrained("nomic-ai/gpt4all-13b-snoozy")

# OpenAI API Key setzen (für Online-Modell)
openai.api_key = 'Iy5hqvFFUZvheJiMEk3TT3BlbkFJgbRoHnYeJfzFKvi00h11'

@chat_router.post("/chat")
async def chat(request: Request):
    data = await request.json()
    message = data.get('message', '')
    model_type = data.get('model', 'local')  # 'local' oder 'online'
    
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
    
    return {"response": response}
