from models.openai_model import OpenAIModel
from state.state import State


def chatbot(state: State):
    model = OpenAIModel()
    return { "messages": [model.llm_with_tools.invoke(state["messages"])] }