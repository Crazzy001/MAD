# /mnt/f/chatbot/backend/main.py
import logging
from fastapi import FastAPI, Request
from transformers import AutoTokenizer, AutoModelForCausalLM
import openai
from w_s_u import WatchSecurityUpdates
from llama_module import llama_function
from whisper_module import whisper_function
from pc_control_module import control_pc

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

watch_security_updates = WatchSecurityUpdates()
watch_security_updates.start()

tokenizer = AutoTokenizer.from_pretrained("nomic-ai/gpt4all-13b-snoozy", use_fast=False)
model = AutoModelForCausalLM.from_pretrained("nomic-ai/gpt4all-13b-snoozy")

openai.api_key = 'sk-proj-Iy5hqvFFUZvheJiMEk3TT3BlbkFJgbRoHnYeJfzFKvi00h11'

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    message = data.get('message', '')
    model_type = data.get('model', 'local')

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

"""
Handles the /llama endpoint for the FastAPI application.

This endpoint accepts a POST request with a JSON payload, and passes the payload data to the `llama_function` to generate a response. The response is then returned as the result of the API call.

Args:
    request (Request): The incoming HTTP request object.

Returns:
    dict: A dictionary containing the response from the `llama_function`.
"""


@app.post("/llama")
async def llama(request: Request):
    data = await request.json()
    response = llama_function(data)
    return response


@app.post("/whisper")
async def whisper(request: Request):
    data = await request.json()
    response = whisper_function(data)
    return response

@app.post("/control_pc")
async def control_pc(request: Request):
    data = await request.json()
    response = control_pc(data)
    return response

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8100)
