from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="AELARA Backend")

class ChatInput(BaseModel):
    input: str

@app.get("/")
def root():
    return {"status": "AELARA backend online"}

@app.post("/chat")
def chat(data: ChatInput):
    return {
        "response": f"AELARA recibió: {data.input}"
    }
