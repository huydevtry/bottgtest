from pydantic import BaseModel
from typing import Optional

class Chat(BaseModel):
    id: int

class Message(BaseModel):
    message_id: int
    text: Optional[str]
    chat: Chat

class Update(BaseModel):
    update_id: int
    message: Optional[Message]
