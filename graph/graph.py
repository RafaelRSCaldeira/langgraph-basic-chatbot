from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.memory import MemorySaver 

from nodes.chatbot import chatbot
from nodes.initial_node import initial_node
from nodes.final_node import final_node
from state.state import OverallState, InputState, OutputState
from tools.tools import tools_list

# Initialize graph builder
graph_builder = StateGraph(OverallState, input=InputState, output=OutputState)

# Add nodes
# graph_builder.add_node("chatbot", chatbot)
# graph_builder.add_node("tools", ToolNode(tools_list))

graph_builder.add_node("initial_node", initial_node)
graph_builder.add_node("final_node", final_node)

# Add edges
# graph_builder.add_edge(START, "chatbot")
# graph_builder.add_conditional_edges(
#     "chatbot",
#     tools_condition
# )
# graph_builder.add_edge("tools", "chatbot")

graph_builder.add_edge(START, "initial_node")
graph_builder.add_edge("initial_node", "final_node")
graph_builder.add_edge("final_node", END)

# Initialize memory
memory = MemorySaver()

# Compile graph with memory
graph = graph_builder.compile(checkpointer=memory)