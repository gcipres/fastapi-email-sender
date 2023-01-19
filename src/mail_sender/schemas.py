from pydantic import BaseModel

class Message(BaseModel):
    email: str
    text: str