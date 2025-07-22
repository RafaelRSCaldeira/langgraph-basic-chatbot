from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.memory import MemorySaver 

from nodes.chatbot import chatbot
from state.state import State
from tools.tools import tools_list

# Initialize graph builder
graph_builder = StateGraph(State)

# Add nodes
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("tools", ToolNode(tools_list))

# Add edges
graph_builder.add_edge(START, "chatbot")
graph_builder.add_conditional_edges(
    "chatbot",
    tools_condition
)
graph_builder.add_edge("tools", "chatbot")

# Initialize memory
memory = MemorySaver()

# Compile graph with memory
graph = graph_builder.compile()