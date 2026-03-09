from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from ai import ask_ai

app = FastAPI()

# Allow requests from frontend (Vercel)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # you can restrict later to your domain
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

