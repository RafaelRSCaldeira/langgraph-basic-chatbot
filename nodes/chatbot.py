from models.openai_model import OpenAIModel
from state.state import State
from langchain_core.messages import SystemMessage


def chatbot(state: State):
    # Initialize model
    model = OpenAIModel()

    # System message
    sys_msg = SystemMessage(
    content="You are a helpful assistant that provides accurate responses based on the given tools.")

    return { "messages": [model.llm_with_tools.invoke([sys_msg] + state["messages"])] }