from fastapi import FastAPI
from pydantic import BaseModel
from chatbot import chatbot

app = FastAPI()

class Request(BaseModel):
    message: str
    user_id: str = "user1"

@app.get("/")
def home():
    return {"message": "AI Chatbot Running 🚀"}

@app.post("/chat")
def chat(req: Request):
    response = chatbot(req.message, req.user_id)
    return {"response": response}