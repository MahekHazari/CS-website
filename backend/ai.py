from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def ask_ai(question):

    prompt = f"""
You are an assistant for Car Sajawat car accessories shop.

Services include:
- PPF
- Seat covers
- Ambient lights
- Dashcams
- Interior upgrades

Help customers with:
1. Answering queries
2. Suggesting accessories
3. Booking installation

Customer question:
{question}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are a friendly and helpful car accessories assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content