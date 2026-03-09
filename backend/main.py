from fastapi import FastAPI
from pydantic import BaseModel
from ai import ask_ai

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Car Sajawat API running"}

class Message(BaseModel):
    message: str

@app.post("/chat")
def chat(msg: Message):
    reply = ask_ai(msg.message)
    return {"reply": reply}

