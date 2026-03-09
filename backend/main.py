from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from ai import ask_ai

app = FastAPI()

# CORS (allow Vercel frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    message: str


@app.get("/")
async def home():
    return {"message": "Car Sajawat API running"}


@app.post("/chat")
async def chat(msg: Message):
    reply = ask_ai(msg.message)
    return {"reply": reply}

