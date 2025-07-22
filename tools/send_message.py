from pydantic import BaseModel, Field
from langchain_core.tools import tool
import asyncio

class MessageInput(BaseModel):
    message: str = Field(description="message text that will be sent to user")
    user: str = Field(description="user to whom the message will be sent")
    
@tool("send-message-tool", args_schema=MessageInput)
def send_message(message: str, user: str) -> None:
    """Send a message to the user."""
    return f"Mensagem enviada ao {user}: {message}"
