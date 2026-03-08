from fastapi import FastAPI
from pydantic import BaseModel
from ai import ask_ai

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Car Sajawat API running"}

class Message(BaseModel):

    message:str


@app.post("/chat")

def chat(msg:Message):

    reply = ask_ai(msg.message)

    return {"reply":reply}