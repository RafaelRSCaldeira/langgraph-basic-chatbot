from pydantic import BaseModel, Field
from langchain_core.tools import tool

class RetrieveInfoInput(BaseModel):
    user: str = Field(description="user whose info will be retrieved")
    
@tool("retrieve-info-tool", args_schema=RetrieveInfoInput)
def retrieve_info(user: str) -> None:
    """Retrieve info of a user."""
    return f"Informações recuperadas de {user}"
