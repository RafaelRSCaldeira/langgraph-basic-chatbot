from typing import Annotated, List
from typing_extensions import TypedDict

from langgraph.graph.message import add_messages
from langchain_core.messages import AnyMessage

class State(TypedDict):
    messages: Annotated[List[AnyMessage], add_messages]

class InputState(TypedDict):
    name: str

class OutputState(TypedDict):
    answer: str
    
class OverallState(TypedDict):
    user: str
    message: str