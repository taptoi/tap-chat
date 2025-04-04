from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    user_message: str

@app.post("/chat")
async def chat(message: Message):
    user_message = message.user_message
    bot_response = f"Echo: {user_message}"
    return {"response": bot_response}
